----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date:    13:15:24 09/28/2014 
-- Design Name: 
-- Module Name:    std_sig - Behavioral 
-- Project Name: 
-- Target Devices: 
-- Tool versions: 
-- Description: 
--
-- Dependencies: 
--
-- Revision: 
-- Revision 0.01 - File Created
-- Additional Comments: 
--
----------------------------------------------------------------------------------
library IEEE,XESS;
use IEEE.STD_LOGIC_1164.ALL;
use XESS.ClkgenPckg.all;     -- For the clock generator module.
use XESS.SdramCntlPckg.all;  -- For the SDRAM controller module.
use XESS.HostIoPckg.all;     -- For the FPGA<=>PC transfer link module.
use XESS.DelayPckg.all;
use IEEE.STD_LOGIC_UNSIGNED.ALL;
use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx primitives in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity std_sig is
    Port ( 
			  
			  clk_i : in STD_LOGIC;

			  sigDel_flag :  in STD_LOGIC;

			  even_odd_s, fwd_inv_s, updated_s  : in std_logic;
			  noupdate_s : out std_logic;
           left_s, sam_s, right_s, lf_del : in signed(15 downto 0);
			  res_s : out signed(15 downto 0);
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
           sdDqml_o  : out   std_logic;  -- SDRAM low-byte databus qualifier.
			  --for simulation these signals need to be in the entity section
			  updated_r : out std_logic;
			  updated_x : in std_logic;
			  sigDelayed_r : out std_logic;
			  sigDelayed_x : in std_logic;
			  sam_addr_r : out unsigned(13 downto 0) := (others => '0');
			  sam_addr_x : in unsigned(13 downto 0) := (others => '0');
			  addrjpeg_r : out unsigned(13 downto 0) := (others => '0');
			  addrjpeg_x : in unsigned(13 downto 0) := (others => '0');
			  addr_r : out unsigned(13 downto 0) := (others => '0');
			  addr_x : in unsigned(13 downto 0) := (others => '0')
			  );
end std_sig;

architecture Behavioral of std_sig is
-------------------------------------------------------------------------
-- JTAG
------------------------------------------------------------------------- 
 -- Main entry point for the JTAG signals between the PC and the FPGA.
 --Signals constants needed by JTAG--------------------------------------- 
  signal inShiftDr_s : std_logic; -- True when bits shift btwn PC & FPGA.
  signal clk_fast : std_logic;
  signal clk_s                    : std_logic;  -- Internal 
  signal drck_s : std_logic; -- Bit shift clock.
  signal tdi_s : std_logic; -- Bits from host PC to the blinker.
  signal tdo_s : std_logic; -- Bits from blinker to the host PC.
  signal tojpeg_s : std_logic_vector(15 downto 0); -- From PC to jpeg.
  signal fromjpeg_s : std_logic_vector(145 downto 0); -- From jpeg to PC.
--Signals constants needed by JTAG---------------------------------------
  
--Signals constants needed by Sdram---------------------------------------  
constant NO                     : std_logic := '0';
constant YES                    : std_logic := '1';
constant ROW_C             : natural   := 63;  -- Number of words in RAM.
constant RAM_SIZE_C             : natural   := 16384;  -- Number of words in RAM.
constant RAM_WIDTH_C            : natural   := 16;  -- Width of RAM words.
constant MIN_ADDR_C             : natural   := 0;  -- Process RAM from this address ...
constant LEFT_ADDR_C             : natural   := 0;  -- Process RAM from this address ...
constant SAM_ADDR_C             : natural   := 1;  -- Process RAM from this address ...
constant RIGHT_ADDR_C             : natural   := 2;  -- Process RAM from this address ...
constant MAX_ADDR_C             : natural   := 8191;  -- ... to this address.
constant MIN_ADDRJPEG_C             : natural   := 8192;  -- Process RAM from this address ...
constant MAX_ADDRJPEG_C             : natural   := 16384;  -- ... to this address.
subtype RamWord_t is unsigned(RAM_WIDTH_C-1 downto 0);  -- RAM word type.
signal wr_s                     : std_logic;  -- Write-enable control.
signal rd_s                     : std_logic;  -- Read-enable control.
signal done_s                   : std_logic;  -- SDRAM R/W operation done signal.component jpeg is
signal addrSdram_s              : std_logic_vector(23 downto 0);  -- Address.
signal dataToSdram_s            : std_logic_vector(sdData_io'range);  -- Data.
signal dataFromSdram_s          : std_logic_vector(sdData_io'range);  --
signal dataToRam_r, dataToRam_x : RamWord_t;  -- Data to write to RAM.
--Signals constants needed by Sdram--------------------------------------- 

signal sigdel_s : std_logic;
signal sigDelayed_s : std_logic;
signal left_sv :   STD_LOGIC_VECTOR(15 downto 0) ;
signal leftDelDut_s :   STD_LOGIC_VECTOR(15 downto 0);

--Signals constants needed by FsmUpdate_p---------------------------------------	
--signal addr_x : unsigned(13 downto 0) := (others => '0');
--signal sam_addr_x : unsigned(13 downto 0) := (others => '0');
--signal updated_x : std_logic := '0';
--signal sigDelayed_x : std_logic := '0';
--signal addrjpeg_x : unsigned(13 downto 0) := (others => '0');
--signal dataToRam_x : unsigned(15 downto 0) := (others => '0');   
--signal addr_r : unsigned(13 downto 0);
--signal sam_addr_r : unsigned(13 downto 0) := (others => '0');
--signal updated_r : std_logic := '0';
--signal sigDelayed_r : std_logic := '0';
--signal addrjpeg_r : unsigned(13 downto 0) := (others => '0');
--signal dataToRam_r : unsigned(15 downto 0) := (others => '0');
--Signals constants needed by FsmUpdate_p---------------------------------------

component jpeg is
    port (
        clk_fast: in std_logic;
        left_s : in signed (15 downto 0);
		  leftDelDut_s : in signed (15 downto 0);
        right_s : in signed (15 downto 0);
        sam_s : in signed (15 downto 0);
        res_s: out signed (15 downto 0);
		  even_odd_s : in std_logic ;
		  fwd_inv_s : in std_logic;
		  updated_s : in std_logic;
		  noupdate_s : out std_logic;
		  sigDelayed_s : in std_logic
    );
end component;    
COMPONENT FsmUpdate_p
    PORT(
         clk_s : IN  std_logic;
         addr_r : OUT  unsigned(13 downto 0);
         addr_x : IN  unsigned(13 downto 0);
			sam_addr_r : OUT  unsigned(13 downto 0);
         sam_addr_x : IN  unsigned(13 downto 0);
			updated_r : OUT  std_logic;
         updated_x : IN  std_logic;
			sigDelayed_r : OUT  std_logic;
         sigDelayed_x : IN  std_logic;
         addrjpeg_r : OUT  unsigned(13 downto 0);
         addrjpeg_x : IN  unsigned(13 downto 0);
			dataToRam_r : OUT  unsigned(15 downto 0);
         dataToRam_x : IN  unsigned(15 downto 0)
			);
END COMPONENT;
begin
DelayBus_u0 : DelayBus
	generic map (NUM_DELAY_CYCLES_G => 2)
		port map (
		      --clk_s => clk_s,
			   --This clk used during simulation  
				clk_i => clk_i,
				bus_i => left_sv,
				busDelayed_o => leftDelDut_s
				);
DelayLine_u1 : DelayLine
	generic map (NUM_DELAY_CYCLES_G => 2)
		port map (
		      --clk_s => clk_s,
			   --This clk used during simulation  
				clk_i => clk_i,
				a_i => sigDel_s,
				aDelayed_o => sigDelayed_s
				);
ujpeg: jpeg 
	port map( 
        --clk_fast => clk_fast,
		  --This clk used during simulation
		  clk_fast => clk_i,
        left_s => left_s,
		  leftDelDut_s => lf_del,
        right_s => right_s,
        sam_s => sam_s,
        res_s => res_s,
        even_odd_s => even_odd_s,
		  fwd_inv_s => fwd_inv_s,
        updated_s => updated_s,
        noupdate_s => noupdate_s,
        sigDelayed_s => sigDel_flag 		  
		  );	
uFsmUpdate_p : FsmUpdate_p 
	PORT MAP (
			 --clk_s => clk_s,
			 --This clk used during simulation          
			 clk_s => clk_i,
          addr_r => addr_r,
          addr_x => addr_x,
			 sam_addr_r => sam_addr_r,
          sam_addr_x => sam_addr_x,
			 updated_r => updated_r,
          updated_x => updated_x,
			 sigDelayed_r => sigDelayed_r,
          sigDelayed_x => sigDelayed_x,
			 addrjpeg_r => addrjpeg_r,
          addrjpeg_x => addrjpeg_x,
			 dataToRam_r => dataToRam_r,
          dataToRam_x => dataToRam_x
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

  -- Connect the SDRAM controller signals to the FSM signals.
  dataToSdram_s <= std_logic_vector(dataToRam_r);
--  dataFromRam_s <= RamWord_t(dataFromSdram_s);
--  addrSdram_s   <= std_logic_vector(TO_UNSIGNED(addr_r, addrSdram_s'length)); 
end Behavioral;

