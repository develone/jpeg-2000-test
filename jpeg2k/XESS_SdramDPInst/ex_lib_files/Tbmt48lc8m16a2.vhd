--------------------------------------------------------------------------------
-- Company: 
-- Engineer:
--
-- Create Date:   13:23:01 01/09/2015
-- Design Name:   
-- Module Name:   C:/Xilinx/14.7/ISE_DS/test_sdram/Tbmt48lc8m16a2.vhd
-- Project Name:  test_sdram
-- Target Device:  
-- Tool versions:  
-- Description:   
-- 
-- VHDL Test Bench Created by ISE for module: mt48lc8m16a2
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
 
ENTITY Tbmt48lc8m16a2 IS
END Tbmt48lc8m16a2;
 
ARCHITECTURE behavior OF Tbmt48lc8m16a2 IS 
 
    -- Component Declaration for the Unit Under Test (UUT)
 
    COMPONENT mt48lc8m16a2
    PORT(
         Dq : INOUT  std_logic_vector(15 downto 0);
         Addr : IN  std_logic_vector(11 downto 0);
         Ba : IN  std_logic;
         Clk : IN  std_logic;
         Cke : IN  std_logic;
         Cs_n : IN  std_logic;
         Ras_n : IN  std_logic;
         Cas_n : IN  std_logic;
         We_n : IN  std_logic;
         Dqm : IN  std_logic_vector(1 downto 0)
        );
    END COMPONENT;
    

   --Inputs
   signal Addr : std_logic_vector(11 downto 0) := (others => '0');
   signal Ba : std_logic := '0';
   signal Clk : std_logic := '0';
   signal Cke : std_logic := '0';
   signal Cs_n : std_logic := '0';
   signal Ras_n : std_logic := '0';
   signal Cas_n : std_logic := '0';
   signal We_n : std_logic := '0';
   signal Dqm : std_logic_vector(1 downto 0) := (others => '0');

	--BiDirs
   signal Dq : std_logic_vector(15 downto 0);

   -- Clock period definitions
   constant Clk_period : time := 10 ns;
 
BEGIN
 
	-- Instantiate the Unit Under Test (UUT)
   uut: mt48lc8m16a2 PORT MAP (
          Dq => Dq,
          Addr => Addr,
          Ba => Ba,
          Clk => Clk,
          Cke => Cke,
          Cs_n => Cs_n,
          Ras_n => Ras_n,
          Cas_n => Cas_n,
          We_n => We_n,
          Dqm => Dqm
        );

   -- Clock process definitions
   Clk_process :process
   begin
		Clk <= '0';
		wait for Clk_period/2;
		Clk <= '1';
		wait for Clk_period/2;
   end process;
 

   -- Stimulus process
   stim_proc: process
   begin		
      -- hold reset state for 100 ns.
      wait for 100 ns;	

      wait for Clk_period*10;

      -- insert stimulus here 

      wait;
   end process;

END;
