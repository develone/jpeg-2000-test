----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date:    09:11:52 09/12/2014 
-- Design Name: 
-- Module Name:    top_level_mod - Behavioral 
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

use IEEE.STD_LOGIC_UNSIGNED.ALL;
use IEEE.NUMERIC_STD.ALL;

use XESS.ClkgenPckg.all;     -- For the clock generator module.
use XESS.SdramCntlPckg.all;  -- For the SDRAM controller module.
use XESS.HostIoPckg.all;     -- For the FPGA<=>PC transfer link module.

use work.pck_myhdl_09.all;
-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx primitives in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity top_level_mod is
    Port (fpgaClk_i : in    std_logic;  -- 12 MHz clock input from external clock source.
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
end top_level_mod;

architecture Behavioral of top_level_mod is
-- Connections between the shift-register module and  jpeg.
  --    80          70         60        50        40          30        20        10         0
  --   1 0 9876543210987654 3210987654321098 7654321098765432 1098765432109876 5432109876543210
  --                                                                           5432109876543210
  signal fromjpeg_s : std_logic_vector(15 downto 0); -- From jpeg to PC.
  --                                     9 8 7654321098765432 1098765432109876 5432109876543210
  signal tojpeg_s : std_logic_vector(49 downto 0); -- From PC to jpeg.
  alias toeven_odd_s is tojpeg_s(48);
  alias tofwd_inv_s is tojpeg_s(49);

  signal clk_fast : std_logic;
  signal clk_s                    : std_logic;  -- Internal 
  
  signal inShiftDr_s : std_logic; -- True when bits shift btwn PC & FPGA.
  signal drck_s : std_logic; -- Bit shift clock.
  signal tdi_s : std_logic; -- Bits from host PC to the blinker.
  signal tdo_s : std_logic; -- Bits from blinker to the host PC.
  signal  even_odd_s : std_logic;
  signal  fwd_inv_s : std_logic;
  alias even_odd_tmp_s is  tojpeg_s(48);
  alias fwd_inv_tmp_s is tojpeg_s(49);
  alias right_s is tojpeg_s(15 downto 0); -- jpeg's 1st operand.
  alias left_s is tojpeg_s(31 downto 16); -- jpeg's 2nd operand.
  alias sam_s is tojpeg_s(47 downto 32); 
  alias signed_res_s is signed(fromjpeg_s);
component jpeg is
    port (
        clk_fast: in std_logic;
        left_s: in signed (15 downto 0);
        right_s: in signed (15 downto 0);
        sam_s: in signed (15 downto 0);
        res_s: out signed (15 downto 0);
		  even_odd_s : in std_logic ;
		  fwd_inv_s : in std_logic
    );
end component;
signal cnt_r : std_logic_vector(22 downto 0) := (others => '0');
--Signals constants needed by Sdram---------------------------------------  
constant NO                     : std_logic := '0';
constant YES                    : std_logic := '1';
constant RAM_SIZE_C             : natural   := 8192;  -- Number of words in RAM.
constant RAM_WIDTH_C            : natural   := 16;  -- Width of RAM words.
constant MIN_ADDR_C             : natural   := 0;  -- Process RAM from this address ...
constant LEFT_ADDR_C             : natural   := 2;
constant SAM_ADDR_C             : natural   := 3;
constant RIGHT_ADDR_C             : natural   := 4;
constant MAX_ADDR_C             : natural   := 5;  -- ... to this address.
subtype RamWord_t is unsigned(RAM_WIDTH_C-1 downto 0);  -- RAM word type.

 
signal wr_s                     : std_logic;  -- Write-enable control.
signal rd_s                     : std_logic;  -- Read-enable control.
signal done_s                   : std_logic;  -- SDRAM R/W operation done signal.
--Signals constants needed by Sdram---------------------------------------
begin
  even_odd_s <= even_odd_tmp_s;
  fwd_inv_s <= fwd_inv_tmp_s;

ujpeg: jpeg 
	port map(
        clk_fast => clk_fast,
        left_s => signed(left_s),
        right_s => signed(right_s),
        sam_s => signed(sam_s),
        res_s => signed_res_s,
        even_odd_s => even_odd_s,
		  fwd_inv_s => fwd_inv_s  
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
      --addr_i    => addrSdram_s,
      --data_i    => dataToSdram_s,
      --data_o    => dataFromSdram_s,
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
  --dataToSdram_s <= std_logic_vector(dataToRam_r);
  --dataFromRam_s <= RamWord_t(dataFromSdram_s);
  --addrSdram_s   <= std_logic_vector(TO_UNSIGNED(addr_r, addrSdram_s'length))
 process(clk_fast) is
	begin
	   if rising_edge(clk_fast) then
	 
			cnt_r <= cnt_r + 1;
		end if;
	end process; 
  
--blinker_o <= cnt_r(22);
end Behavioral;

