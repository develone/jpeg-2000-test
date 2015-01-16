--*********************************************************************
-- SDRAM, dual-port, instantiated.
--*********************************************************************

library IEEE;
use IEEE.STD_LOGIC_1164.all;
use IEEE.NUMERIC_STD.all;
use work.ClkgenPckg.all;     -- For the clock generator module.
use work.SdramCntlPckg.all;  -- For the SDRAM controller module.
use work.HostIoPckg.HostIoToDut;     -- For the FPGA<=>PC transfer link module.  
use work.pck_myhdl_09.all;
use work.pck_xess_jpeg_top.all;
entity XESS_SdramDPInst is
  port (
    fpgaClk_i : in    std_logic;  -- 12 MHz clock input from external clock source.
    sdClk_o   : out   std_logic;  -- 100 MHz clock to SDRAM.
    sdClkFb_i : in    std_logic;  -- 100 MHz clock fed back into FPGA.
    sdCke_o   : out   std_logic;  -- SDRAM clock enable.
    sdCe_bo   : out   std_logic;  -- SDRAM chip-enable.
    sdRas_bo  : out   std_logic;  -- SDRAM row address strobe.
    sdCas_bo  : out   std_logic;  -- SDRAM column address strobe.
    sdWe_bo   : out   std_logic;  -- SDRAM write-enable.
    sdBs_o    : out   std_logic_vector(1 downto 0);  -- SDRAM bank-address.
    sdAddr_o  : out   std_logic_vector(11 downto 0);  -- SDRAM address bus.
    sdData_io : inout std_logic_vector(15 downto 0);    -- SDRAM data bus.
    sdDqmh_o  : out   std_logic;  -- SDRAM high-byte databus qualifier.
    sdDqml_o  : out   std_logic  -- SDRAM low-byte databus qualifier.
    );
end entity;

architecture Behavioral of XESS_SdramDPInst is
  constant ZERO                     : std_logic := '0';
  constant NO                     : std_logic := '0';
  constant YES                    : std_logic := '1';
  --00_0000 to 03_FFFF is total memory allocated
  --00_0000 to 01_FFFF is where lena256.hex is initially installed
  constant RAM_SIZE_C             : natural   := 262144;  -- Number of words in RAM.
  constant RAM_WIDTH_C            : natural   := 16;  -- Width of RAM words.
  constant MIN_ADDR_C             : natural   := 1;  -- Process RAM from this address ...
  constant MAX_ADDR_C             : natural   := 5;  -- ... to this address.
  subtype RamWord_t is unsigned(RAM_WIDTH_C-1 downto 0);  -- RAM word type.
 

 
--  signal dataFromRam_s            : RamWord_t;  -- Data read from RAM.
  -- Convert the busses for connection to the SDRAM controller.
 

  -- FSM state.
--  type state_t is (INIT, WRITE_DATA, READ_AND_SUM_DATA, DONE);  -- FSM states.
--  signal state_r, state_x         : state_t   := INIT;  -- FSM starts off in init state.

----signal needed by XESS_SdramDPInst.vhd and xess_jpeg_top.vhd*************************** 
  signal clk_s                    : std_logic;  -- Internal clock.
  signal sumDut_s                 : std_logic_vector(106 downto 0);  -- Send sum back to PC.
  alias fromjpflgsDut_s is sumDut_s(106 downto 103);
  alias fromjprhDut_s is sumDut_s(102 downto 87);
  alias fromjpsaDut_s is sumDut_s(86 downto 71);
  alias fromjplfDut_s is sumDut_s(70 downto 55);
   
  alias fromresdataDut_s is sumDut_s(54 downto 39);
  alias fromsdramdataDut_s is sumDut_s(38 downto 23);
  alias fromsdramaddrDut_s is sumDut_s(22 downto 0);
  signal nullDutOut_s             : std_logic_vector(0 downto 0);  -- Dummy output for HostIo module.
  signal dataFromSdram_s          : std_logic_vector(sdData_io'range);  -- Data.
  signal dataFromSdram0_s          : std_logic_vector(sdData_io'range);  -- Data.
  signal dataFromSdram1_s          : std_logic_vector(sdData_io'range);  -- Data.
  signal addrSdram_s              : std_logic_vector(22 downto 0);  -- Address.
  signal addrSdram0_s              :std_logic_vector(22 downto 0);  -- Address.
  signal addrSdram1_s              : std_logic_vector(22 downto 0);  -- Address.
  signal dataToSdram_s            : unsigned(15 downto 0);  -- Data.
  signal dataToSdram0_s            : unsigned(15 downto 0);  -- Data.
  signal dataToSdram1_s            : unsigned(15 downto 0);  -- Data.
   
  signal dataFromRam0_r  : unsigned(15 downto 0);
  signal dataFromRam1_r  : unsigned(15 downto 0);   
--  signal dataToSdram1_s            : unsigned(15 downto 0);  -- Data.
--  signal dataFromRam1_r  : unsigned(15 downto 0);
  signal sum_r, sum_x             : unsigned( 15 downto 0);
 
  
  signal wr_s                     : std_logic:= NO;  -- Write-enable control.
  signal rd_s                     : std_logic:= NO;  -- Read-enable control.
  signal wr0_i                     : std_logic:= NO;  -- Write-enable control.
  signal rd0_i                     : std_logic:= NO;  -- Read-enable control.
  signal wr1_i                     : std_logic:= NO;  -- Write-enable control.
  signal rd1_i                     : std_logic:= NO;  -- Read-enable control.
  signal wr0_s                     : std_logic:= NO;  -- Write-enable control.
  signal rd0_s                     : std_logic:= NO;  -- Read-enable control.
  signal wr1_s                     : std_logic:= NO;  -- Write-enable control.
  signal rd1_s                     : std_logic:= NO;  -- Read-enable control.
  signal done_s                   : std_logic:= NO;  -- SDRAM R/W operation done signal.
  signal done0_o                   : std_logic:= NO;  -- SDRAM R/W operation done signal.
  signal done1_o                   : std_logic:= NO;  -- SDRAM R/W operation done signal.
  signal done0_s                   : std_logic:= NO;  -- SDRAM R/W operation done signal.
  signal done1_s                   : std_logic:= NO;  -- SDRAM R/W operation done signal.
 
  signal addr0_r, addr0_x           : unsigned(22 downto 0):= (others => '0');  -- RAM address.
  signal addr1_r, addr1_x           : unsigned(22 downto 0):= (others => '0');  -- RAM address.
  signal addr_i           : std_logic_vector(22 downto 0):= (others => '0');  -- RAM address.
  signal addr0_i           : std_logic_vector(22 downto 0):= (others => '0');  -- RAM address.
  signal addr1_i           : std_logic_vector(22 downto 0):= (others => '0');  -- RAM address. 
  signal index1_r, index2_r, index3_r           : unsigned(22 downto 0):= (others => '0'); 
  signal index1_x, index2_x, index3_x           : unsigned(22 downto 0):= (others => '0');
  signal dataFromRam_s : unsigned(15 downto 0);  -- Data to write to RAM.
  signal dataToRam0_r, dataToRam0_x, dataFromRam0_s  : unsigned(15 downto 0);  -- Data to write to RAM.
  signal dataToRam1_r, dataToRam1_x, dataFromRam1_s  : unsigned(15 downto 0);  -- Data to write to RAM.
 
 
          -- Host-side port 0.
  signal   rst0_i          :   std_logic                                  := NO;  -- reset.
  signal   earlyOpBegun0_o :  std_logic:= NO;
  signal   opBegun0_o      :  std_logic                                  := NO;
  signal   rdPending0_o    :  std_logic:= NO;
  signal   rdDone0_o       :  std_logic:= NO;  -- read operation is done_i and data is available.
  signal   status0_o       :  std_logic_vector(3 downto 0):="0000";  -- diagnostic status of the SDRAM controller FSM         .
        -- Host-side port 1.
  signal   rst1_i          :   std_logic                                  := NO;  -- reset.
  signal   earlyOpBegun1_o :  std_logic:= NO;
  signal   opBegun1_o      :  std_logic                                  := NO;
  signal   rdPending1_o    :  std_logic:= NO;
  signal   rdDone1_o       :  std_logic:= NO;  -- read operation is done_i and data is available.
  signal   status1_o       :  std_logic_vector(3 downto 0):="0000";  -- diagnostic status of the SDRAM controller FSM
  signal   earlyOpBegun_i :   std_logic:= NO;
  signal   earlyOpBegun_s :   std_logic:= NO;
  signal      opBegun_i      :   std_logic:= NO;
  signal      opBegun_s      :   std_logic:= NO;
  signal    rdPending_i    :   std_logic:= NO;
  signal    rdPending_s    :   std_logic:= NO;
  signal   earlyOpBegun_o :   std_logic:= NO;
  signal      opBegun_o      :   std_logic:= NO;
  signal    rdPending_o    :   std_logic:= NO;
  signal status_i       :   std_logic_vector(3 downto 0):="0000";
  signal status_s       :   std_logic_vector(3 downto 0):="0000";  
  signal rdDone_s       :   std_logic:= NO;
  signal rdDone_i       :   std_logic:= NO;
  signal rdDone_o       :   std_logic:= NO;
  signal   rst_s          :   std_logic                                  := NO;  -- reset.
  ----signal needed by XESS_SdramDPInst.vhd and xess_jpeg_top.vhd***************************

--signal needed by xess_jpeg_top.vhd***************************
  signal state_r, state_x         : t_enum_t_State_1   := INIT;  -- FSM starts off in init state.
  signal sig_in : unsigned(51 downto 0) := (others => '0');
  signal noupdate_s : std_logic;
  signal res_s : signed(15 downto 0) := (others => '0');
  signal res_u : unsigned(15 downto 0) := (others => '0');
  signal jp_lf : unsigned(15 downto 0) := (others => '0');
  signal jp_sa: unsigned(15 downto 0) := (others => '0');
  signal jp_rh : unsigned(15 downto 0) := (others => '0');
  signal jp_flgs : unsigned(3 downto 0) := (others => '0');
  signal reset_col : std_logic := '0';
  signal rdy : std_logic := '1';
  signal addr_not_reached : std_logic := '0';
  signal offset_r, offset_x           : unsigned(22 downto 0);  -- RAM address.
 
  signal col_r, col_x, row_r, row_x : unsigned(7 downto 0) := (others => '0');
  signal dout_rom : unsigned(15 downto 0) := (others => '0');
  signal addr_rom_r, addr_rom_x : unsigned(11 downto 0) := (others => '0');
--signal needed by xess_jpeg_top.vhd*************************** 

--signal needed by FIFO*************************** 
  signal empty_r:  std_logic:= '0';
  signal full_r:  std_logic:= '0';
  signal enr_r:  std_logic:= '0';
  signal enw_r:  std_logic:= '0';
  signal dataout_r:  unsigned(15 downto 0):= (others => '0');
  signal datain_r:  unsigned(15 downto 0):= (others => '0');
  signal empty_x:  std_logic:= '0';
  signal full_x:  std_logic:= '0';
  signal enr_x:  std_logic:= '0';
  signal enw_x:  std_logic:= '0';
  signal dataout_x:  unsigned(15 downto 0):= (others => '0');
  signal datain_x:  unsigned(15 downto 0):= (others => '0'); 
 
--signal needed by FIFO*************************** 
 
 
component xess_jpeg_top is
    port (
        clk_fast: in std_logic;
        addr0_r: inout unsigned(22 downto 0);
        addr0_x: inout unsigned(22 downto 0);
        addr1_r: inout unsigned(22 downto 0);
        addr1_x: inout unsigned(22 downto 0);
        state_r: inout t_enum_t_State_1;
        state_x: inout t_enum_t_State_1;
        dataToRam0_r: inout unsigned(15 downto 0);
        dataToRam0_x: inout unsigned(15 downto 0);
        dataFromRam0_r: inout unsigned(15 downto 0);
        dataFromRam0_x: inout unsigned(15 downto 0);
        dataToRam1_r: inout unsigned(15 downto 0);
        dataToRam1_x: inout unsigned(15 downto 0);
        dataFromRam1_r: inout unsigned(15 downto 0);
        dataFromRam1_x: inout unsigned(15 downto 0);
        sig_in: inout unsigned(51 downto 0);
        noupdate_s: out std_logic;
        res_s: inout signed (15 downto 0);
        res_u: out unsigned(15 downto 0);
        jp_lf: inout unsigned(15 downto 0);
        jp_sa: inout unsigned(15 downto 0);
        jp_rh: inout unsigned(15 downto 0);
        jp_flgs: inout unsigned(3 downto 0);
        reset_col: out std_logic;
        rdy: inout std_logic;
        addr_not_reached: inout std_logic;
        offset_r: inout unsigned(22 downto 0);
        offset_x: inout unsigned(22 downto 0);
 
        dataFromRam0_s: in unsigned(15 downto 0);
        dataFromRam1_s: in unsigned(15 downto 0);
        done1_s: in std_logic;
        wr1_s: out std_logic;
        rd1_s: out std_logic;
        done0_s: in std_logic;
        wr0_s: out std_logic;
        rd0_s: out std_logic;
        sum_r: inout unsigned(15 downto 0);
        sum_x: inout unsigned(15 downto 0);
        empty_r: out std_logic;
        full_r: out std_logic;
        enr_r: inout std_logic;
        enw_r: inout std_logic;
        dataout_r: inout unsigned(15 downto 0);
        datain_r: inout unsigned(15 downto 0);
        empty_x: inout std_logic;
        full_x: inout std_logic;
        enr_x: inout std_logic;
        enw_x: inout std_logic;
        dataout_x: inout unsigned(15 downto 0);
        datain_x: inout unsigned(15 downto 0);
        col_r: inout unsigned(7 downto 0);
        col_x: inout unsigned(7 downto 0);
        row_r: inout unsigned(7 downto 0);
        row_x: inout unsigned(7 downto 0);
        dout_rom: inout unsigned(15 downto 0);
        addr_rom_r: inout unsigned(11 downto 0);
        addr_rom_x: inout unsigned(11 downto 0);
        index1_r: inout unsigned(22 downto 0);
        index2_r: inout unsigned(22 downto 0);
        index3_r: inout unsigned(22 downto 0);
        index1_x: inout unsigned(22 downto 0);
        index2_x: inout unsigned(22 downto 0);
        index3_x: inout unsigned(22 downto 0)
    );
end component xess_jpeg_top;
  component DualPort is
    generic(
      PIPE_EN_G         : boolean                       := false;  -- enable pipelined read operations.
      PORT_TIME_SLOTS_G : std_logic_vector(15 downto 0) := "1111000011110000";
      DATA_WIDTH_G      : natural                       := 16;  -- host & SDRAM data width.
      HADDR_WIDTH_G     : natural                       := 23  -- host-side address width.
      );
    port(
     clk_i  : in std_logic;             -- master clock.

      -- Host-side port 0.
      rst0_i          : in  std_logic                                  := NO;  -- reset.
      rd0_i           : in  std_logic                                  := NO;  -- initiate read operation.
      wr0_i           : in  std_logic                                  := NO;  -- initiate write operation.
      earlyOpBegun0_o : out std_logic;  -- read/write op has begun (async).
      opBegun0_o      : out std_logic                                  := NO;  -- read/write op has begun (clocked).
      rdPending0_o    : out std_logic;  -- true if read operation(s) are still in the pipeline.
      done0_o         : out std_logic;  -- read or write operation is done_i.
      rdDone0_o       : out std_logic;  -- read operation is done_i and data is available.
      addr0_i         : in  std_logic_vector(HADDR_WIDTH_G-1 downto 0) := (others => ZERO);  -- address from host to SDRAM.
      data0_i         : in  std_logic_vector(DATA_WIDTH_G-1 downto 0)  := (others => ZERO);  -- data from host to SDRAM.
      data0_o         : out std_logic_vector(DATA_WIDTH_G-1 downto 0)  := (others => ZERO);  -- data from SDRAM to host.
      status0_o       : out std_logic_vector(3 downto 0);  -- diagnostic status of the SDRAM controller FSM         .

      -- Host-side port 1.
      rst1_i          : in  std_logic                                  := NO;
      rd1_i           : in  std_logic                                  := NO;
      wr1_i           : in  std_logic                                  := NO;
      earlyOpBegun1_o : out std_logic;
      opBegun1_o      : out std_logic                                  := NO;
      rdPending1_o    : out std_logic;
      done1_o         : out std_logic;
      rdDone1_o       : out std_logic;
      addr1_i         : in  std_logic_vector(HADDR_WIDTH_G-1 downto 0) := (others => ZERO);
      data1_i         : in  std_logic_vector(DATA_WIDTH_G-1 downto 0)  := (others => ZERO);
      data1_o         : out std_logic_vector(DATA_WIDTH_G-1 downto 0)  := (others => ZERO);
      status1_o       : out std_logic_vector(3 downto 0);

      -- SDRAM controller host-side port.
      rst_o          : out std_logic;
      rd_o           : out std_logic;
      wr_o           : out std_logic;
      earlyOpBegun_i : in  std_logic;
      opBegun_i      : in  std_logic;
      rdPending_i    : in  std_logic;
      done_i         : in  std_logic;
      rdDone_i       : in  std_logic;
      addr_o         : out std_logic_vector(HADDR_WIDTH_G-1 downto 0);
      data_o         : out std_logic_vector(DATA_WIDTH_G-1 downto 0);
      data_i         : in  std_logic_vector(DATA_WIDTH_G-1 downto 0);
      status_i       : in  std_logic_vector(3 downto 0)
      );
  end component;
begin
--muxsel_x <= '0';
  --*********************************************************************
  -- Instantiate the jpeg_top step1JPEG_TOP_INSTANCE_7_FSMUPDATE
  -- updates signals for the FSM.
  --*********************************************************************
xess_jpeg_top_u0 : xess_jpeg_top
  port map (
     clk_fast => clk_s,
	  addr0_r => addr0_r,
	  addr0_x => addr0_x,
	  addr1_r => addr1_r,
	  addr1_x => addr1_x,
	  state_r => state_r,
	  state_x => state_x,
 
	  dataToRam0_r => dataToRam0_r,
	  dataToRam0_x => dataToRam0_x,
	  dataFromRam0_r =>  dataFromRam0_r,
	  
	  dataToRam1_r => dataToRam1_r,
	  dataToRam1_x => dataToRam1_x,
	  dataFromRam1_r =>  dataFromRam1_r,
 
	  sig_in => sig_in,
	  noupdate_s => noupdate_s,
	  res_s => res_s,
	  res_u => res_u,
	  jp_lf => jp_lf,
	  jp_sa => jp_sa,
	  jp_rh => jp_rh,
	  jp_flgs => jp_flgs,
	  reset_col => reset_col,
	  rdy => rdy,
	  addr_not_reached => addr_not_reached,
     offset_r => offset_r,
	  offset_x => offset_x,
 
	  dataFromRam0_s => unsigned(dataFromRam0_s),
	  dataFromRam1_s => unsigned(dataFromRam1_s),
--	  wr_s => wr_s,
--	  rd_s => rd_s,
--	  done_s => done_s,
	  wr0_s => wr0_s,
	  rd0_s => rd0_s,
	  done0_s => done0_s,	  
	  wr1_s => wr1_s,
	  rd1_s => rd1_s,
	  done1_s => done1_s,
	  sum_r => sum_r,
	  sum_x => sum_x,
 
 
	  empty_r => empty_r,
	  full_r => full_r,
	  enr_r => enr_r,
	  enw_r => enw_r,
	  dataout_r => dataout_r,
	  datain_r => datain_r,
	  empty_x => empty_x,
	  full_x => full_x,
	  enr_x => enr_x,
	  enw_x => enw_x,
	  dataout_x => dataout_x,
	  datain_x => datain_x,
	  col_x => col_x,
	  col_r => col_r,
	  row_x => row_x,
	  row_r => row_r,
     dout_rom => dout_rom,
	  addr_rom_r => addr_rom_r,
	  addr_rom_x => addr_rom_x,
	  index1_r => index1_r,
	  index2_r => index2_r,
	  index3_r => index3_r,
	  index1_x => index1_x,
	  index2_x => index2_x,
	  index3_x => index3_x  
	  
   
  );
 
		
  --*********************************************************************
  -- Generate a 100 MHz clock from the 12 MHz input clock and send it out
  -- to the SDRAM. Then feed it back in to clock the internal logic.
  -- (The Spartan-6 FPGAs are a bit picky about what their DCM outputs
  -- are allowed to drive, so I have to use the clkToLogic_o output to
  -- send the clock signal to the output pin of the FPGA and on to the
  -- SDRAM chip.)
  --*********************************************************************
  Clkgen_u1 : Clkgen
    generic map (BASE_FREQ_G => 12.0, CLK_MUL_G => 25, CLK_DIV_G => 3)
    port map(I               => fpgaClk_i, clkToLogic_o => sdClk_o);
  clk_s <= sdClkFb_i;                   -- SDRAM clock feeds back into FPGA.

  --*********************************************************************
  -- Instantiate the SDRAM controller that connects to the FSM
  -- and interfaces to the external SDRAM chip.
  --*********************************************************************
  SdramCntl_u0 : SdramCntl
    generic map(
      FREQ_G       => 100.0,  -- Use clock freq. to compute timing parameters.
      DATA_WIDTH_G => RAM_WIDTH_C,       -- Width of data words.
		
		NROWS_G       => 4096,  -- Number of rows in SDRAM array.
      NCOLS_G       => 512,  -- Number of columns in SDRAM array.
      HADDR_WIDTH_G => 23,   -- Host-side address width.
      SADDR_WIDTH_G => 12   -- SDRAM-side address width.
      )
    port map(
      clk_i     => clk_s,
      -- FSM side.
      rd_i      => rd_s,
      wr_i      => wr_s,
      done_o    => done_s,
--      addr_i    => std_logic_vector(addrSdram_s),
--      data_i    => std_logic_vector(dataToSdram_s),
--      data_o    => dataFromSdram_s,
      -- SDRAM side.
      sdCke_o   => sdCke_o, -- SDRAM clock-enable pin is connected on the XuLA2.
      sdCe_bo   => sdCe_bo, -- SDRAM chip-enable is connected on the XuLA2.
      sdRas_bo  => sdRas_bo,
      sdCas_bo  => sdCas_bo,
      sdWe_bo   => sdWe_bo,
      sdBs_o    => sdBs_o, -- Both SDRAM bank selects are connected on the XuLA2.
      sdAddr_o  => sdAddr_o,
      sdData_io => sdData_io,
      sdDqmh_o  => sdDqmh_o, -- SDRAM high-byte databus qualifier is connected on the XuLA2.
      sdDqml_o  => sdDqml_o  -- SDRAM low-byte databus qualifier is connected on the XuLA2.
      );
DualPort_u0 : DualPort 
    generic map(
      PIPE_EN_G  =>       true,
      PORT_TIME_SLOTS_G => "1111000011110000",
      DATA_WIDTH_G     => 16,
      HADDR_WIDTH_G     => 23
      )
    port map( 
	 clk_i => clk_s,
	 rst0_i => rst0_i,
	 rd0_i => rd0_s,
	 wr0_i => wr0_s,
    earlyOpBegun0_o => earlyOpBegun0_o,
    opBegun0_o => opBegun0_o,
    rdPending0_o => rdPending0_o,
    done0_o => done0_s,	 
	 rdDone0_o => rdDone_o,
    addr0_i => std_logic_vector(addrSdram0_s),
	 data0_i => std_logic_vector(dataToSdram0_s),
	 data0_o => dataFromSdram0_s,
	 status0_o => status0_o,
	 
	 rst1_i => rst1_i,
	 rd1_i => rd1_s,
	 wr1_i => wr1_s,
    earlyOpBegun1_o => earlyOpBegun1_o,
    opBegun1_o => opBegun1_o,
    rdPending1_o => rdPending1_o,
    done1_o => done1_s,	 
	 rdDone1_o => rdDone_i,
    addr1_i => std_logic_vector(addrSdram1_s),
	 data1_i => std_logic_vector(dataToSdram1_s),
	 data1_o => dataFromSdram1_s,	 
	 status1_o => status1_o,
	 rst_o => rst_s,	
    rd_o => rd_s,
    wr_o	=> wr_s,
	 done_i => done_s,
	 earlyOpBegun_i => earlyOpBegun_s,
	 opBegun_i => opBegun_s,
	 rdPending_i => rdPending_s,
	 rdDone_i => rdDone_s,
	 status_i => status_s,
	 data_i    => std_logic_vector(dataToSdram_s),
    data_o    => dataFromSdram_s,
	 addr_o  => addrSdram_s
	 );
  -- Connect the SDRAM controller signals to the FSM signals. 
  dataToSdram_s <= dataToRam0_r; 
  addrSdram0_s   <= std_logic_vector(addr0_r); 
--  dataFromRam0_s <= unsigned(dataFromSdram0_s);
--  dataToSdram1_s <= dataToRam1_r;  
--  dataToSdram_s <= std_logic_vector(dataToRam_r);

--  dataFromRam1_s <= RamWord_t(dataFromSdram1_s);
--  addrSdram_s   <= std_logic_vector(TO_UNSIGNED(addr_r, addrSdram_s'length));

--  addrSdram1_s   <= std_logic_vector(addr1_r);
--addrSdram_s   <= std_logic_vector(TO_UNSIGNED(addr0_r,16));
 
  --*********************************************************************
  -- State machine that initializes RAM and then reads RAM to compute
  -- the sum of products of the RAM address and data. This section
  -- is combinatorial logic that sets the control bits for each state 
  -- and determines the next state.
  --*********************************************************************
--  FsmComb_p : process(state_r, addr_r, dataToRam_r,
--                      sum_r, dataFromRam_s, done_s)
--  begin
--    -- Disable RAM reads and writes by default.
--    rd_s        <= NO;                  -- Don't write to RAM.
--    wr_s        <= NO;                  -- Don't read from RAM.
--    -- Load the registers with their current values by default.
--    addr_x      <= addr_r;
--    sum_x       <= sum_r;
--    dataToRam_x <= dataToRam_r;
--    state_x     <= state_r;
--
--    case state_r is
--
--      when INIT =>                      -- Initialize the FSM.
--        addr_x      <= X"00_0000";      -- Start writing data at this address.
--        dataToRam_x <= TO_UNSIGNED(1, RAM_WIDTH_C);  -- Initial value to write.
----        state_x     <= WRITE_DATA;      -- Go to next state.
--        state_x     <= READ_AND_SUM_DATA;      -- Go to next state.
--
--      when WRITE_DATA =>                -- Load RAM with values.
--        if done_s = NO then  -- While current RAM write is not complete ...
--          wr_s <= YES;                  -- keep write-enable active.
--        elsif addr_r < MAX_ADDR_C then  -- If haven't reach final address ...
--          addr_x      <= addr_r + 1;    -- go to next address ...
--          dataToRam_x <= dataToRam_r + 3;  -- and write this value.
--        else                 -- Else, the final address has been written ...
--          addr_x  <= X"00_0000";        -- go back to the start, ...
--          sum_x   <= 0;                 -- clear the sum-of-products, ...
--          state_x <= READ_AND_SUM_DATA;    -- and go to next state.
--        end if;
--
--      when READ_AND_SUM_DATA =>  -- Read RAM and sum address*data products
--        if done_s = NO then      -- While current RAM read is not complete ...
--          rd_s <= YES;                  -- keep read-enable active.
--        elsif addr_r <= MAX_ADDR_C then  -- If not the final address ...
--          -- add product of previous RAM address and data read 
--          -- from that address to the summation ...
--          sum_x  <= sum_r + TO_INTEGER(dataFromRam_s * addr_r);
--          addr_x <= addr_r + 1;         -- and go to next address.
--          if addr_r = MAX_ADDR_C then  -- Else, the final address has been read ...
--            state_x <= DONE;            -- so go to the next state.
--          end if;
--        end if;
--
--      when DONE =>                      -- Summation complete ...
--        null;                           -- so wait here and do nothing.
--      when others =>                    -- Erroneous state ...
--        state_x <= INIT;                -- so re-run the entire process.
--        
--    end case;
--
--  end process;

  --*********************************************************************
  -- Update the FSM's registers with their next values as computed by
  -- the FSM's combinatorial section.       
  --*********************************************************************
--  FsmUpdate_p : process(clk_s)
--  begin
--    if rising_edge(clk_s) then
----      addr_r      <= addr_x;
----      dataToRam_r <= dataToRam_x;
--      state_r     <= state_x;
--      sum_r       <= sum_x;
--    end if;
--  end process;

  --*********************************************************************
  -- Send the summation to the HostIoToDut module and then on to the PC.
  --*********************************************************************
  --sumDut_s <= std_logic_vector(TO_UNSIGNED(sum_r, 16));
  --sumDut_s <= std_logic_vector(sum_r);
  fromsdramaddrDut_s <= std_logic_vector(addr0_r);
  fromsdramdataDut_s <= std_logic_vector(sum_r);
  fromresdataDut_s <= std_logic_vector(res_s);
  fromjplfDut_s <= std_logic_vector(jp_lf);
  fromjpsaDut_s <= std_logic_vector(jp_sa);
  fromjprhDut_s <= std_logic_vector(jp_rh);
  fromjpflgsDut_s <= std_logic_vector(jp_flgs);

  HostIoToDut_u2 : HostIoToDut
    generic map (SIMPLE_G => true)
    port map (
      vectorFromDut_i => sumDut_s,
      vectorToDut_o   => nullDutOut_s
      );

end architecture;
