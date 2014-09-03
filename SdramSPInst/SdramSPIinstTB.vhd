--------------------------------------------------------------------------------
-- Company: 
-- Engineer:
--
-- Create Date:   15:53:33 09/02/2014
-- Design Name:   
-- Module Name:   C:/Xilinx/14.7/ISE_DS/SdramSPInst/SdramSPIinstTB.vhd
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
 
ENTITY SdramSPIinstTB IS
END SdramSPIinstTB;
 
ARCHITECTURE behavior OF SdramSPIinstTB IS 
 
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
 
   constant <clock>_period : time := 10 ns;
 
BEGIN
 
	-- Instantiate the Unit Under Test (UUT)
   uut: SdramSPInst PORT MAP (
          fpgaClk_i => fpgaClk_i,
          sdClk_o => sdClk_o,
          sdClkFb_i => sdClkFb_i,
          sdCke_o => sdCke_o,
          sdCe_bo => sdCe_bo,
          sdRas_bo => sdRas_bo,
          sdCas_bo => sdCas_bo,
          sdWe_bo => sdWe_bo,
          sdBs_o => sdBs_o,
          sdAddr_o => sdAddr_o,
          sdData_io => sdData_io,
          sdDqmh_o => sdDqmh_o,
          sdDqml_o => sdDqml_o
        );

   -- Clock process definitions
   <clock>_process :process
   begin
		<clock> <= '0';
		wait for <clock>_period/2;
		<clock> <= '1';
		wait for <clock>_period/2;
   end process;
 

   -- Stimulus process
   stim_proc: process
   begin		
      -- hold reset state for 100 ns.
      wait for 100 ns;	

      wait for <clock>_period*10;

      -- insert stimulus here 

      wait;
   end process;

END;
