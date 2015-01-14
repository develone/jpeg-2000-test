--------------------------------------------------------------------------------
-- Company: 
-- Engineer:
--
-- Create Date:   13:37:43 01/03/2013
-- Design Name:   
-- Module Name:   C:/xesscorp/PRODUCTS/TUTORIALS/FpgasNowWhat/Chapters/Verilog/FPGA/SdramDPInst/SdramDPInstTb.vhd
-- Project Name:  SdramDPInst
-- Target Device:  
-- Tool versions:  
-- Description:   
-- 
-- VHDL Test Bench Created by ISE for module: SdramDPInst
-- 
-- Dependencies:
-- 
-- Revision:
-- Revision 0.01 - File Created
-- Additional Comments:
--
-- Notes: 
-- This testbench has been automatically generated using types std_logic and
-- std_logic_vector for the ports of the unit under test.  Xilinx recommends
-- that these types always be used for the top-level I/O of a design in order
-- to guarantee that the testbench will bind correctly to the post-implementation 
-- simulation model.
--------------------------------------------------------------------------------
LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
use IEEE.NUMERIC_STD.all;
use work.ClkgenPckg.all;     -- For the clock generator module.
use work.SdramCntlPckg.all;  -- For the SDRAM controller module.
use work.HostIoPckg.HostIoToDut;     -- For the FPGA<=>PC transfer link module.
 
use work.pck_myhdl_09.all;
use work.pck_xess_jpeg_top.all; 
-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--USE ieee.numeric_std.ALL;
 
ENTITY XESS_SdramDPInstTb IS
END XESS_SdramDPInstTb;
 
ARCHITECTURE behavior OF XESS_SdramDPInstTb IS 
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
    -- Component Declaration for the Unit Under Test (UUT)
 
    COMPONENT XESS_SdramDPInst
    PORT(
         fpgaClk_i : IN  std_logic;
         sdClk_o : OUT  std_logic;
         sdClkFb_i : IN  std_logic;
         sdCke_o   : OUT   std_logic;  -- SDRAM clock enable.
         sdCe_bo   : OUT   std_logic;  -- SDRAM chip-enable.
         sdRas_bo : OUT  std_logic;
         sdCas_bo : OUT  std_logic;
         sdWe_bo : OUT  std_logic;
         sdBs_o    : OUT   std_logic_vector(1 downto 0);  -- 2-bit SDRAM bank-address.
         sdAddr_o : OUT  std_logic_vector(11 downto 0); -- 13-bit SDRAM address bus.
         sdData_io : INOUT  std_logic_vector(15 downto 0);
         sdDqmh_o  : OUT   std_logic;  -- SDRAM high-byte databus qualifier.
         sdDqml_o  : OUT   std_logic  -- SDRAM low-byte databus qualifier.
        );
    END COMPONENT;

    -- Take the SDRAM module I/O description from mt48lc8m16a2.v Verilog file
    --    module mt48lc8m16a2 (Dq, Addr, Ba, Clk, Cke, Cs_n, Ras_n, Cas_n, We_n, Dqm);
    -- and convert it into a VHDL component declaration like this:
    
    component mt48lc8m16a2 
    port(
      Dq : inout std_logic_vector(15 downto 0);
      Addr : in std_logic_vector(11 downto 0); 
      Ba : in std_logic_vector(1 downto 0); 
      Clk : in std_logic; 
      Cke : in std_logic;
      Cs_n : in std_logic;
      Ras_n : in std_logic;
      Cas_n : in std_logic;
      We_n : in std_logic;
      Dqm : in std_logic_vector(1 downto 0)
      );
    end component;
    

   --Inputs
   signal fpgaClk_i : std_logic := '0';
   signal sdClkFb_i : std_logic := '0';

	--BiDirs
   signal sdData_io : std_logic_vector(15 downto 0);

 	--Outputs
   signal sdClk_o : std_logic;
   signal sdCke_o : std_logic;
   signal sdCe_bo : std_logic;
   signal sdRas_bo : std_logic;
   signal sdCas_bo : std_logic;
   signal sdWe_bo : std_logic;
   signal sdBs_o : std_logic_vector(1 downto 0);
   signal sdAddr_o : std_logic_vector(11 downto 0);
   signal sdDqmh_o : std_logic;
   signal sdDqml_o : std_logic;
   -- No clocks detected in port list. Replace <clock> below with 
   -- appropriate port name 
 
   constant fpgaClk_period : time := 83.3333 ns; -- 12 MHz XuLA clock.
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
  signal addrSdram_s              : unsigned(22 downto 0);  -- Address.
  signal dataToSdram_s            : unsigned(15 downto 0);  -- Data.
  signal dataToSdram0_s            : unsigned(15 downto 0);  -- Data.
  signal dataToSdram1_s            : unsigned(15 downto 0);  -- Data.
  signal dataFromRam_r  : unsigned(15 downto 0); 
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
  signal addr_r, addr_x           : unsigned(22 downto 0):= (others => '0');  -- RAM address.
  signal addr0_r, addr0_x           : unsigned(22 downto 0):= (others => '0');  -- RAM address.
  signal addr1_r, addr1_x           : unsigned(22 downto 0):= (others => '0');  -- RAM address.
  signal addr_i           : std_logic_vector(22 downto 0):= (others => '0');  -- RAM address.
  signal addr0_i           : std_logic_vector(22 downto 0):= (others => '0');  -- RAM address.
  signal addr1_i           : std_logic_vector(22 downto 0):= (others => '0');  -- RAM address. 
  signal index1_r, index2_r, index3_r           : unsigned(22 downto 0):= (others => '0'); 
  signal index1_x, index2_x, index3_x           : unsigned(22 downto 0):= (others => '0');
  signal dataToRam_r, dataToRam_x, dataFromRam_s : unsigned(15 downto 0);  -- Data to write to RAM.
  signal dataToRam0_r, dataToRam0_x, dataFromRam0_s : unsigned(15 downto 0);  -- Data to write to RAM.
  signal dataToRam1_r, dataToRam1_x, dataFromRam1_s : unsigned(15 downto 0);  -- Data to write to RAM.
  signal data0_i, data1_i  : std_logic_vector(15 downto 0);  -- Data to write to RAM.
  signal data0_o, data1_o  : std_logic_vector(15 downto 0);  -- Data to write to RAM.
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
--
----signal needed by xess_jpeg_top.vhd***************************
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
----signal needed by xess_jpeg_top.vhd*************************** 

  
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
        addr_r: inout unsigned(22 downto 0);
        addr_x: inout unsigned(22 downto 0);
        addr0_r: inout unsigned(22 downto 0);
        addr0_x: inout unsigned(22 downto 0);
        addr1_r: inout unsigned(22 downto 0);
        addr1_x: inout unsigned(22 downto 0);
        state_r: inout t_enum_t_State_1;
        state_x: inout t_enum_t_State_1;
        dataToRam_r: inout unsigned(15 downto 0);
        dataToRam_x: inout unsigned(15 downto 0);
        dataFromRam_r: inout unsigned(15 downto 0);
        dataFromRam_x: inout unsigned(15 downto 0);
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
        dataFromRam_s: in unsigned(15 downto 0);
        dataFromRam0_s: in unsigned(15 downto 0);
        dataFromRam1_s: in unsigned(15 downto 0);
        done_s: in std_logic;
        wr_s: out std_logic;
        rd_s: out std_logic;
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
      clk_i : in std_logic;             -- master clock.

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
BEGIN


--muxsel <= '0';
--  --*********************************************************************
--  -- Instantiate the jpeg_top step1JPEG_TOP_INSTANCE_7_FSMUPDATE
--  -- updates signals for the FSM.
--  --*********************************************************************
xess_jpeg_top_u0 : xess_jpeg_top
  port map (
     clk_fast => clk_s,
	  addr_r => addr_r,
	  addr_x => addr_x,
	  state_r => state_r,
	  state_x => state_x,
 
	  dataToRam_r => dataToRam_r,
	  dataToRam_x => dataToRam_x,
	  dataFromRam_r =>  dataFromRam_r,
 
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
     dataFromRam_s => dataFromRam_s,
	  dataFromRam0_s => dataFromRam0_s,
	  dataFromRam1_s => dataFromRam1_s,
	  wr_s => wr_s,
	  rd_s => rd_s,
	  done_s => done_s,
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
	-- Instantiate the Unit Under Test (UUT)
   uut: XESS_SdramDPInst PORT MAP (
          fpgaClk_i => fpgaClk_i, -- 12 MHz XuLA clock.
          sdClk_o => sdClk_o, -- 100 MHz clock from DCM.
          sdClkFb_i => sdClkFb_i, -- 100 MHz clock fed back into FPGA.
          sdCke_o => sdCke_o,  -- SDRAM clock enable.
          sdCe_bo => sdCe_bo,  -- SDRAM chip-enable.
          sdRas_bo => sdRas_bo, -- Row-address strobe.
          sdCas_bo => sdCas_bo, -- Column-address strobe.
          sdWe_bo => sdWe_bo, -- Write-enable.
          sdBs_o => sdBs_o, -- Bank-select.
          sdAddr_o => sdAddr_o, -- 12-bit address bus.
          sdData_io => sdData_io, -- 16-bit data bus.
          sdDqmh_o => sdDqmh_o,  -- SDRAM high-byte databus qualifier.
          sdDqml_o => sdDqml_o  -- SDRAM low-byte databus qualifier.
        );
   sdClkFb_i <= sdClk_o; -- Feedback 100 MHz clock to FPGA.
   clk_s <= sdClkFb_i;     
    -- Use the mt48lc8m16a2 declaration from above to instantiate
    -- the SDRAM here and connect it to the UUT.
   sdram: mt48lc8m16a2 port map(
     Dq => sdData_io,  -- 16-bit data bus.
     Addr => sdAddr_o,  -- 12-bit address bus.
     Ba => sdBs_o,  -- Bank-select pins.
     Clk => sdClk_o,  -- 100 MHz clock.
     Cke => sdCke_o,  -- Clock-enable.
     Cs_n => sdCe_bo, -- Chip-enable.
     Ras_n => sdRas_bo, -- Row-address strobe.
     Cas_n => sdCas_bo, -- Column-address strobe.
     We_n => sdWe_bo, -- Write-enable.
     Dqm(0) => sdDqml_o, -- Lower-byte databus qualifier.
     Dqm(1) => sdDqmh_o  -- Upper-byte databus qualifier.
     );
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
      addr_i    => std_logic_vector(addrSdram_s),
      data_i    => std_logic_vector(dataToSdram_s),
      data_o    => dataFromSdram_s,
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
	 rd0_i => rd0_i,
	 wr0_i => wr0_i,
    earlyOpBegun0_o => earlyOpBegun0_o,
    opBegun0_o => opBegun0_o,
    rdPending0_o => rdPending0_o,
    done0_o => done0_o,	 
	 rdDone0_o => rdDone_o,
    addr0_i => addr0_i,
	 data0_i => data0_i,
	 data0_o => data0_o,
	 status0_o => status0_o,
	 
	 rst1_i => rst1_i,
	 rd1_i => rd1_i,
	 wr1_i => wr1_i,
    earlyOpBegun1_o => earlyOpBegun1_o,
    opBegun1_o => opBegun1_o,
    rdPending1_o => rdPending1_o,
    done1_o => done1_o,	 
	 rdDone1_o => rdDone_i,
    addr1_i => addr1_i,
	 data1_i => data1_i,
	 data1_o => data1_o,	 
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
    data_o    => dataFromSdram_s
--	 addr_o  => addrSdram_s
	 );

  -- Connect the SDRAM controller signals to the FSM signals. 
  dataToSdram_s <= dataToRam0_r;  
--  dataToSdram_s <= std_logic_vector(dataToRam_r);
  dataFromRam0_s <= RamWord_t(dataFromSdram_s);
--  addrSdram_s   <= std_logic_vector(TO_UNSIGNED(addr_r, addrSdram_s'length));
  addrSdram_s   <= addr0_r;
--  addrSdram_s   <= std_logic_vector(TO_UNSIGNED(addr0_r,16));
 
   -- Clock process definitions.
   -- This generates the 12 MHz clock.
   fpgaClk_process :process
   begin
		fpgaClk_i <= '0';
		wait for fpgaClk_period/2;
		fpgaClk_i <= '1';
		wait for fpgaClk_period/2;
   end process;
 
  fromsdramaddrDut_s <= std_logic_vector(addr0_r);
  fromsdramdataDut_s <= std_logic_vector(sum_r);
  fromresdataDut_s <= std_logic_vector(res_s);
  fromjplfDut_s <= std_logic_vector(jp_lf);
  fromjpsaDut_s <= std_logic_vector(jp_sa);
  fromjprhDut_s <= std_logic_vector(jp_rh);
  fromjpflgsDut_s <= std_logic_vector(jp_flgs);

   -- Stimulus process.
   -- This is not used in this testbench. The FSM in the
   -- UUT steps through all the operations.
   stim_proc: process
   begin		
      -- hold reset state for 100 ns.
      wait for 100 ns;	

      wait for fpgaClk_period*10;

      -- insert stimulus here 
--		wait for 200 ns;
--		rst_s <= '1';
--		wait for 10 ns ;
--		rst_s <= '0';
      wait;
   end process;

END;
