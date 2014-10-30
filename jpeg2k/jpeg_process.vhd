-- File: jpeg_process.vhd
-- Generated by MyHDL 0.9dev
-- Date: Thu Oct 23 15:32:58 2014


library IEEE,XESS;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
use std.textio.all;
use XESS.ClkgenPckg.all;     -- For the clock generator module.
use XESS.SdramCntlPckg.all;  -- For the SDRAM controller module.
use XESS.HostIoPckg.all;     -- For the FPGA<=>PC transfer link module
use work.pck_myhdl_09.all;

entity jpeg_process is
    port (
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
          sdDqml_o  : out   std_logic  -- SDRAM low-byte databus qualifier.
	  );
end entity jpeg_process;

architecture MyHDL of jpeg_process is
   signal fromjpeg_s : std_logic_vector(15 downto 0); -- From jpeg to PC.
   signal tojpeg_s : std_logic_vector(51 downto 0); -- From PC to jpeg.
   alias fromresDut_s is fromjpeg_s(15 downto 0); -- res_s.
   signal clk_fast : std_logic := '0';
   signal sig_in : unsigned(51 downto 0) := (others => '0');
   signal noupdate_s : std_logic;
   signal res_s : signed(15 downto 0);
-------------------------------------------------------------------------
-- JTAG
------------------------------------------------------------------------- 
 -- Main entry point for the JTAG signals between the PC and the FPGA.
 --Signals constants needed by JTAG--------------------------------------- 
  signal inShiftDr_s : std_logic; -- True when bits shift btwn PC & FPGA.
  --signal clk_fast : std_logic;
  signal clk_s                    : std_logic;  -- Internal 
  signal drck_s : std_logic; -- Bit shift clock.
  signal tdi_s : std_logic; -- Bits from host PC to the blinker.
  signal tdo_s : std_logic; -- Bits from blinker to the host PC.
  --signal tojpeg_s : std_logic_vector(15 downto 0); -- From PC to jpeg.
  --signal fromjpeg_s : std_logic_vector(145 downto 0); -- From jpeg to PC.
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
constant RIGHT_USE_C         : natural   := 3;  -- Enable right to jpeg ...
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
signal dataFromRam_s            : RamWord_t;  -- Data read from RAM.
--Signals constants needed by FsmUpdate_p---------------------------------------
signal resDut_s                 : std_logic_vector(15 downto 0);  -- Send left back to PC.


begin
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

JPEG_PROCESS_JPEG: process (clk_fast) is
begin
    if rising_edge(clk_fast) then
        if bool(sig_in(50)) then
            noupdate_s <= '0';
            if bool(sig_in(48)) then
                if bool(sig_in(49)) then
                    res_s <= signed(sig_in(32-1 downto 16) - (shift_right(sig_in(16-1 downto 0), 1) + shift_right(sig_in(48-1 downto 32), 1)));
                else
                    res_s <= signed(sig_in(32-1 downto 16) + (shift_right(sig_in(16-1 downto 0), 1) + shift_right(sig_in(48-1 downto 32), 1)));
                end if;
            else
                if bool(sig_in(49)) then
                    res_s <= signed(sig_in(32-1 downto 16) + shift_right(((sig_in(16-1 downto 0) + sig_in(48-1 downto 32)) + 2), 2));
                else
                    res_s <= signed(sig_in(32-1 downto 16) - shift_right(((sig_in(16-1 downto 0) + sig_in(48-1 downto 32)) + 2), 2));
                end if;
            end if;
        else
            noupdate_s <= '1';
        end if;
    end if;
end process JPEG_PROCESS_JPEG;
sig_in <=  unsigned(tojpeg_s);
resDut_s <= std_logic_vector(res_s);
fromresDut_s <= resDut_s;  --jpeg res back to PC
end architecture MyHDL;