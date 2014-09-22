--------------------------------------------------------------------------------
-- Company: 
-- Engineer:
--
-- Create Date:   09:04:56 09/22/2014
-- Design Name:   
-- Module Name:   C:/Xilinx/14.7/ISE_DS/jpeg_ramctrl/TBRamCtrl.vhd
-- Project Name:  jpeg_ramctrl
-- Target Device:  
-- Tool versions:  
-- Description:   
-- 
-- VHDL Test Bench Created by ISE for module: RamCtrl
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
LIBRARY ieee,XESS;
USE ieee.std_logic_1164.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;
use IEEE.NUMERIC_STD.ALL;

use XESS.ClkgenPckg.all;     -- For the clock generator module.
use XESS.SdramCntlPckg.all;  -- For the SDRAM controller module.
use XESS.HostIoPckg.all;     -- For the FPGA<=>PC transfer link module.
library UNISIM;
use UNISIM.VComponents.all;
 
-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--USE ieee.numeric_std.ALL;
 
ENTITY TBRamCtrl IS
	Port (
		   fpgaClk_i : in    std_logic;  -- 12 MHz clock input from external clock source.
         sdClk_o   : out   std_logic;  -- 100 MHz clock to SDRAM.
			sdClkFb_i : in    std_logic;  -- 100 MHz clock fed back into FPGA.
         --blinker_o : out  STD_LOGIC;
			sdCke_o   : out   std_logic;  -- SDRAM clock enable.
         sdCe_bo   : out   std_logic;  -- SDRAM chip-enable.
         sdRas_bo  : out   std_logic;  -- SDRAM row address strobe.
         sdCas_bo  : out   std_logic;  -- SDRAM column address strobe.
         sdWe_bo   : out   std_logic;  -- SDRAM write-enable.
         sdBs_o    : out   std_logic_vector(1 downto 0);  -- SDRAM bank-address.
         sdAddr_o  : out   std_logic_vector(12 downto 0);  -- SDRAM address bus.
         sdData_io : inout std_logic_vector(15 downto 0);    -- SDRAM data bus.
         sdDqmh_o  : out   std_logic;  -- SDRAM high-byte databus qualifier.
         sdDqml_o  : out   std_logic);  -- SDRAM low-byte databus qualifier.
END TBRamCtrl;
 
ARCHITECTURE behavior OF TBRamCtrl IS 
-- Connections between the shift-register module and  jpeg.
  --    80          70         60        50        40          30        20        10         0
  --   1 0 9876543210987654 3210987654321098 7654321098765432 1098765432109876 5432109876543210
  --                                                                           5432109876543210
  
  signal x : std_logic_vector(15 downto 0);  
  signal fromjpeg_s : std_logic_vector(113 downto 0); -- From jpeg to PC.
  alias fromresult_s is fromjpeg_s(15 downto 0); -- jpeg output.
  alias fromsum_s is fromjpeg_s(31 downto 16); -- sum_r.
  alias fromleft_s is fromjpeg_s(47 downto 32); -- left_r.
  alias fromsam_s is fromjpeg_s(63 downto 48); -- sam_r.
  alias fromright_s is fromjpeg_s(79 downto 64); -- right_r.
  alias fromaddr_sam_s is fromjpeg_s(95 downto 80); --addr_sam_r 
  alias fromaddrjpeg_s is fromjpeg_s(111 downto 96); --addr_sam_r
 
  alias fromupdated_s is fromjpeg_s(112);
  alias fromnoupdate_s is fromjpeg_s(113);
  --alias fromjpegram_s is fromjpeg_s(128 downto 113); --addr_sam_r
  signal  even_odd_s : std_logic;
  signal  fwd_inv_s : std_logic;
  
  signal tojpeg_s : std_logic_vector(15 downto 0); -- From PC to jpeg.
  alias even_odd_tmp_s is  tojpeg_s(14);
  alias fwd_inv_tmp_s is tojpeg_s(15);  
  
  --signal fromram_s : std_logic_vector(15 downto 0); -- From ram to PC.
  signal toram_s : std_logic_vector(15 downto 0); -- From PC to jpeg.
   
  --alias sam_addr_s is tojpeg_s (13 downto 0);
  signal left_s : std_logic_vector(15 downto 0);
  signal sam_s : std_logic_vector(15 downto 0);
  signal right_s : std_logic_vector(15 downto 0);
  signal clk_fast : std_logic;
  signal clk_s                    : std_logic;  -- Internal 
  
  signal inShiftDr_s : std_logic; -- True when bits shift btwn PC & FPGA.
  signal drck_s : std_logic; -- Bit shift clock.
  signal tdi_s : std_logic; -- Bits from host PC to the blinker.
  signal tdo_s : std_logic; -- Bits from blinker to the host PC.

  
  --alias right_s is tojpeg_s(15 downto 0); -- jpeg's 1st operand.
  --alias left_s is tojpeg_s(31 downto 16); -- jpeg's 2nd operand.
  --alias sam_s is tojpeg_s(47 downto 32); 
  alias signed_res_s is signed(fromresult_s);
  
  --alias fromsum_s is fromjpeg_s(31 downto 16); -- jpeg output.


signal cnt_r : std_logic_vector(22 downto 0) := (others => '0');
--Signals constants needed by Sdram---------------------------------------  
constant NO                     : std_logic := '0';
constant YES                    : std_logic := '1';
constant ROW_C             : natural   := 63;  -- Number of words in RAM.
constant RAM_SIZE_C             : natural   := 16384;  -- Number of words in RAM.
constant RAM_WIDTH_C            : natural   := 16;  -- Width of RAM words.
constant MIN_ADDR_C             : natural   := 0;  -- Process RAM from this address ...
constant MAX_ADDR_C             : natural   := 8191;  -- ... to this address.
constant MIN_ADDRJPEG_C             : natural   := 8192;  -- Process RAM from this address ...
constant MAX_ADDRJPEG_C             : natural   := 16384;  -- ... to this address.
subtype RamWord_t is unsigned(RAM_WIDTH_C-1 downto 0);  -- RAM word type.
signal updated_r, updated_x : std_logic;  
signal noupdate_r, noupdate_x : std_logic; 
signal updated_s, noupdate_s : std_logic;  -- jpeg left sam  right are valid
signal addrSdram_s              : std_logic_vector(23 downto 0);  -- Address.
signal dataToSdram_s            : std_logic_vector(sdData_io'range);  -- Data.
signal dataFromSdram_s          : std_logic_vector(sdData_io'range);  -- 
signal dataToRam_r, dataToRam_x : RamWord_t;  -- Data to write to RAM.
signal dataToRam_res_r, dataToRam_res_x : RamWord_t;  -- Data to write to RAM.
signal dataFromRam_s            : RamWord_t;  -- Data read from RAM.
signal left_r, sam_r, right_r, left_x, sam_x, right_x    : RamWord_t;  
-- Data read from RAM for left, sam, and right.
--signal addr needed for HostIoToRam not for HostIoToDut
signal addr_s                   : std_logic_vector(22 downto 0); 
signal addrjpeg_r, addrjpeg_x           : natural range 0 to RAM_SIZE_C-1;  -- RAM address.
signal addr_r, addr_x           : natural range 0 to RAM_SIZE_C-1;  -- RAM address.
signal sam_addr_r, sam_addr_x    :  natural range 0 to RAM_SIZE_C-1; 
signal sam_addr_stor_r, sam_addr_stor_x    :  natural range 0 to RAM_SIZE_C-1; 
signal wr_s                     : std_logic;  -- Write-enable control.
signal rd_s                     : std_logic;  -- Read-enable control.
signal done_s                   : std_logic;  -- SDRAM R/W operation done signal.

--Signals constants needed by Sdram---------------------------------------
-- FSM state.
type state_t is (INIT, READ_AND_SUM_DATA, WRITE_DATA, DONE);  -- FSM states.
signal state_r, state_x         : state_t   := INIT;  -- FSM starts off in init state.
signal sum_r, sum_x             : natural range 0 to RAM_SIZE_C * (2**RAM_WIDTH_C) - 1;
signal sumDut_s                 : std_logic_vector(15 downto 0);  -- Send sum back to PC.
signal leftDut_s                 : std_logic_vector(15 downto 0);  -- Send left back to PC.
signal samDut_s                 : std_logic_vector(15 downto 0);  -- Send sam back to PC.
signal rightDut_s                 : std_logic_vector(15 downto 0);  -- Send right back to PC.
signal sam_addr_rDut_s                 : std_logic_vector(15 downto 0);  -- Send addr_sam_r back to PC.
signal addrjpeg_rDut_s                 : std_logic_vector(15 downto 0);  -- Send addrjpeg_r back to PC.
signal jpegram_rDut_s                 : std_logic_vector(15 downto 0);  -- Send jpegram_r back to PC.

signal nullDutOut_s             : std_logic_vector(0 downto 0);  -- Dummy output for HostIo module. 
    -- Component Declaration for the Unit Under Test (UUT)
 
    COMPONENT RamCtrl
    PORT(
			SOF : OUT  std_logic;
         state : OUT  std_logic_vector(4 downto 0);
         WR_DATAFlag : IN  std_logic;
         clk_fast : IN  std_logic;
         reset_n : IN  std_logic
        );
    END COMPONENT;
    

   --Inputs
   signal WR_DATAFlag : std_logic := '0';
   --signal clk_fast : std_logic := '0';
   signal reset_n : std_logic := '0';

 	--Outputs
   signal SOF : std_logic;
   signal state : std_logic_vector(4 downto 0);

   -- Clock period definitions
   constant clk_fast_period : time := 10 ns;
   component jpeg is
      port (
        clk_fast: in std_logic;
        left_s: in signed (15 downto 0);
        right_s: in signed (15 downto 0);
        sam_s: in signed (15 downto 0);
        res_s: out signed (15 downto 0);
		  even_odd_s : in std_logic ;
		  fwd_inv_s : in std_logic;
		  updated_s : in std_logic;
		  noupdate_s : out std_logic
      );
end component;

BEGIN
 
	-- Instantiate the Unit Under Test (UUT)
   uut: RamCtrl PORT MAP (
          SOF => SOF,
          state => state,
          WR_DATAFlag => WR_DATAFlag,
          clk_fast => clk_fast,
          reset_n => reset_n
        );

--   -- Clock process definitions
--   clk_fast_process :process
--   begin
--		clk_fast <= '0';
--		wait for clk_fast_period/2;
--		clk_fast <= '1';
--		wait for clk_fast_period/2;
--   end process;
 ujpeg: jpeg 
	port map( 
        clk_fast => clk_fast,
        left_s => signed(left_s),
        right_s => signed(right_s),
        sam_s => signed(sam_s),
        res_s => signed_res_s,
        even_odd_s => even_odd_s,
		  fwd_inv_s => fwd_inv_s,
        updated_s => updated_s,
        noupdate_s => noupdate_s		  
		  );

-------------------------------------------------------------------------
-- JTAG entry point.
-------------------------------------------------------------------------
-- Main entry point for the JTAG signals between the PC and the FPGA.
UBscanToHostIo : BscanToHostIo
  port map (
    inShiftDr_o => inShiftDr_s,
    drck_o => drck_s,
    tdi_o => tdi_s,
    tdo_i => tdo_s
    );
-------------------------------------------------------------------------
-- Shift-register.
-------------------------------------------------------------------------
-- This is the shift-register module between jpeg and JTAG entry point.
UHostIoToJpeg : HostIoToDut
  generic map (ID_G => "00000100") -- The identifier used by the PC.
    port map (
    -- Connections to the BscanToHostIo JTAG entry-point module.
    inShiftDr_i => inShiftDr_s,
    drck_i => drck_s,
    tdi_i => tdi_s,
    tdo_o => tdo_s,
    -- Connections to jpeg
    vectorToDut_o => tojpeg_s, -- From PC to jpeg sam left right.
    vectorFromDut_i => fromjpeg_s -- From jpeg to PC.
    );
  -- This is the shift-register module between Ram and JTAG entry point.
--UHostIoToRam : HostIoToRam
--  generic map (ID_G => "00000100") -- The identifier used by the PC.
--    port map (
--   
--    -- Connections to ram
--	 wr_o => wr_s,
--	 clk_i => clk_fast,
--	 rd_o => rd_s,
--	 addr_o => addr_s,
--    dataFromHost_o => toram_s, -- From PC to jpeg sam left right.
--    dataToHost_i => fromram_s, -- From jpeg to PC.
--	 done_i => done_s -- True when memory read/write operation is done.
--    );  
	 
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
	  
  clk_fast <= sdClkFb_i;    -- SDRAM clock feeds back into FPGA.
  clk_s <= sdClkFb_i;
  --*********************************************************************
  -- Instantiate the SDRAM controller that connects to the FSM
  -- and interfaces to the external SDRAM chip.
  --*********************************************************************
  SdramCntl_u0 : SdramCntl
    generic map(
      FREQ_G       => 100.0,  -- Use clock freq. to compute timing parameters.
      DATA_WIDTH_G => RAM_WIDTH_C       -- Width of data words.
      )
    port map(
      clk_i     => clk_s,
      -- FSM side.
      rd_i      => rd_s,
      wr_i      => wr_s,
      done_o    => done_s,
      addr_i    => addrSdram_s,
      data_i    => dataToSdram_s,
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

--   -- Stimulus process
--   stim_proc: process
--   begin		
--      -- hold reset state for 100 ns.
--      wait for 100 ns;	
--
--      wait for clk_fast_period*10;
--
--      -- insert stimulus here 
--   reset_n <= '1';
--	WR_DATAFlag <= '1';
--      wait;
--   end process;

END;
