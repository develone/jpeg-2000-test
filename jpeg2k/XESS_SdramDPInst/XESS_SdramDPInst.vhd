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
  constant RAM_SIZE_C             : natural   := 524288;  -- Number of words in RAM.
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

  signal dataFromSdram0_s          : std_logic_vector(sdData_io'range);  -- Data.
  signal dataFromSdram1_s          : std_logic_vector(sdData_io'range);  -- Data.

  signal addrSdram0_s              :std_logic_vector(22 downto 0);  -- Address.
  signal addrSdram1_s              : std_logic_vector(22 downto 0);  -- Address.

  signal dataToSdram0_s            : unsigned(15 downto 0);  -- Data.
  signal dataToSdram1_s            : unsigned(15 downto 0);  -- Data.
   
  signal dataFromRam0_r  : unsigned(15 downto 0);
  signal dataFromRam1_r  : unsigned(15 downto 0);   
 
  signal sum_r, sum_x             : unsigned( 15 downto 0);
 
  
 
  
  signal wr0_s                     : std_logic:= NO;  -- Write-enable control.
  signal rd0_s                     : std_logic:= NO;  -- Read-enable control.
  signal wr1_s                     : std_logic:= NO;  -- Write-enable control.
  signal rd1_s                     : std_logic:= NO;  -- Read-enable control.

 
  signal done0_s                   : std_logic:= NO;  -- SDRAM R/W operation done signal.
  signal done1_s                   : std_logic:= NO;  -- SDRAM R/W operation done signal.
 
  signal addr0_r, addr0_x           : unsigned(22 downto 0):= (others => '0');  -- RAM address.
  signal addr1_r, addr1_x           : unsigned(22 downto 0):= (others => '0');  -- RAM address.

  signal index1_r, index2_r, index3_r           : unsigned(22 downto 0):= (others => '0'); 
  signal index1_x, index2_x, index3_x           : unsigned(22 downto 0):= (others => '0');

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

begin

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
  DualPortSdram_u0 : DualPortSdram
    generic map(
      FREQ_G       => 100.0,  -- Use clock freq. to compute timing parameters.
      DATA_WIDTH_G => RAM_WIDTH_C,       -- Width of data words.
		PORT_TIME_SLOTS_G => "1111000011110000",
		PIPE_EN_G  =>       false,
		NROWS_G       => 4096,  -- Number of rows in SDRAM array.
      NCOLS_G       => 512,  -- Number of columns in SDRAM array.
      HADDR_WIDTH_G => 23,   -- Host-side address width.
      SADDR_WIDTH_G => 12   -- SDRAM-side address width.
      )
    port map(
      clk_i     => clk_s,
       -- Host-side port 0.
		rst0_i => rst0_i,
		rd0_i => rd0_s,
		wr0_i => wr0_s,
		earlyOpBegun0_o => earlyOpBegun0_o,
		opBegun0_o => opBegun0_o,
		rdPending0_o => rdPending0_o,
		done0_o => done0_s,	 
		rdDone0_o => rdDone0_o,
		addr0_i => std_logic_vector(addrSdram0_s),
		data0_i => std_logic_vector(dataToSdram0_s),
		data0_o => dataFromSdram0_s,
		status0_o => status0_o,
		
      -- Host-side port 1.	 
		rst1_i => rst1_i,
		rd1_i => rd1_s,
		wr1_i => wr1_s,
		earlyOpBegun1_o => earlyOpBegun1_o,
		opBegun1_o => opBegun1_o,
		rdPending1_o => rdPending1_o,
		done1_o => done1_s,	 
		rdDone1_o => rdDone1_o,
		addr1_i => std_logic_vector(addrSdram1_s),
		data1_i => std_logic_vector(dataToSdram1_s),
		data1_o => dataFromSdram1_s,	 
		status1_o => status1_o,
 
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
  -- Connect the SDRAM controller signals to the FSM signals. 
  dataToSdram0_s <= dataToRam0_r; 
  addrSdram0_s   <= std_logic_vector(addr0_r);
  dataFromRam0_s <=unsigned(dataFromSdram0_s);
  
  dataToSdram1_s <= dataToRam1_r; 
  addrSdram1_s   <= std_logic_vector(addr1_r);
  dataFromRam1_s <=unsigned(dataFromSdram1_s);
 
 
 
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
