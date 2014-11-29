--------------------------------------------------------------------------------
-- Company: 
-- Engineer:
--
-- Create Date:   03:15:57 11/29/2014
-- Design Name:   
-- Module Name:   C:/Xilinx/14.7/ISE_DS/SdramSPInst/SdramSPInstTB.vhd
-- Project Name:  SdramSPInst
-- Target Device:  
-- Tool versions:  
-- Description:   
-- 
-- VHDL Test Bench Created by ISE for module: SdramSPInst
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
 
-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--USE ieee.numeric_std.ALL;
 
ENTITY SdramSPInstTB IS
END SdramSPInstTB;
 
ARCHITECTURE behavior OF SdramSPInstTB IS 
 
    -- Component Declaration for the Unit Under Test (UUT)
 
    COMPONENT SdramSPInst
    PORT(
         fpgaClk_i : IN  std_logic;
         sdClk_o : OUT  std_logic;
         sdClkFb_i : IN  std_logic;
         sdCke_o : OUT  std_logic;
         sdCe_bo : OUT  std_logic;
         sdRas_bo : OUT  std_logic;
         sdCas_bo : OUT  std_logic;
         sdWe_bo : OUT  std_logic;
         sdBs_o : OUT  std_logic_vector(1 downto 0);
         sdAddr_o : OUT  std_logic_vector(12 downto 0);
         sdData_io : INOUT  std_logic_vector(15 downto 0);
         sdDqmh_o : OUT  std_logic;
         sdDqml_o : OUT  std_logic
        );
    END COMPONENT;
    
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
   signal sdAddr_o : std_logic_vector(12 downto 0);
   signal sdDqmh_o : std_logic;
   signal sdDqml_o : std_logic;
   -- No clocks detected in port list. Replace <clock> below with 
   -- appropriate port name 
 constant fpgaClk_period : time := 83.3333 ns; -- 12 MHz XuLA clock.
--   constant <clock>_period : time := 10 ns;
 
BEGIN
 
	-- Instantiate the Unit Under Test (UUT)
   uut: SdramSPInst PORT MAP (
  fpgaClk_i => fpgaClk_i, -- 12 MHz XuLA clock.
  sdClk_o => sdClk_o, -- 100 MHz clock from DCM.
  sdClkFb_i => sdClkFb_i, -- 100 MHz clock fed back into FPGA.
  sdRas_bo => sdRas_bo, -- Row-address strobe.
  sdCas_bo => sdCas_bo, -- Column-address strobe.
  sdWe_bo => sdWe_bo, -- Write-enable.
  sdBs_o => sdBs_o, -- Bank-select.
  sdAddr_o => sdAddr_o, -- 12-bit address bus.
  sdData_io => sdData_io -- 16-bit data bus.
  );
  sdClkFb_i <= sdClk_o; -- Feedback 100 MHz clock to FPGA.
 
  -- Use the mt48lc8m16a2 declaration from above to instantiate
  -- the SDRAM here and connect it to the UUT.
  sdram: mt48lc8m16a2 port map(
   Dq => sdData_io, -- 16-bit data bus.
   Addr => sdAddr_o, -- 12-bit address bus.
   Ba(0) => sdBs_o, -- One bank-select pin.
   Ba(1) => '0', -- The other is tied to GND on XuLA PCB.
   Clk => sdClk_o, -- 100 MHz clock.
   Cke => '1', -- Clock-enable tied high on XuLA PCB.
   Cs_n => '0', -- Chip-enable tied low on XuLA PCB.
   Ras_n => sdRas_bo, -- Row-address strobe.
   Cas_n => sdCas_bo, -- Column-address strobe.
   We_n => sdWe_bo, -- Write-enable.
   Dqm(0) => '0', -- Data qualifier masks tied low ...
   Dqm(1) => '0' -- on the XuLA PCB.
  );
  fpgaClk_process :process
  begin
  fpgaClk_i <= '0';
  wait for fpgaClk_period/2;
  fpgaClk_i <= '1';
  wait for fpgaClk_period/2;
  end process;
   -- Clock process definitions
--   <clock>_process :process
--   begin
--		<clock> <= '0';
--		wait for <clock>_period/2;
--		<clock> <= '1';
--		wait for <clock>_period/2;
--   end process;
 

   -- Stimulus process
--   stim_proc: process
--   begin		
--      -- hold reset state for 100 ns.
--      wait for 100 ns;	
--
--      wait for <clock>_period*10;
--
--      -- insert stimulus here 
--
--      wait;
--   end process;

END;
