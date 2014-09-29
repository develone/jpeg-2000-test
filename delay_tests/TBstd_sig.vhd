--------------------------------------------------------------------------------
-- Company: 
-- Engineer:
--
-- Create Date:   05:55:44 09/29/2014
-- Design Name:   
-- Module Name:   C:/Xilinx/14.7/ISE_DS/delay_tests/TBstd_sig.vhd
-- Project Name:  delay_tests
-- Target Device:  
-- Tool versions:  
-- Description:   
-- 
-- VHDL Test Bench Created by ISE for module: std_sig
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
 
ENTITY TBstd_sig IS
END TBstd_sig;
 
ARCHITECTURE behavior OF TBstd_sig IS 
 
    -- Component Declaration for the Unit Under Test (UUT)
 
    COMPONENT std_sig
    PORT(
         clk_i : IN  std_logic;
         bus_i : IN  std_logic_vector :=(15 downto 0 => '0') ;
         busDelayed_o : OUT  std_logic_vector :=(15 downto 0 => '0')
        );
    END COMPONENT;
    

   --Inputs
   signal clk_i : std_logic := '0' ;
   signal bus_i : std_logic_vector (15 downto 0);

 	--Outputs
   signal busDelayed_o : std_logic_vector (15 downto 0);

   -- Clock period definitions
   constant clk_i_period : time := 10 ns;
 
BEGIN
 
	-- Instantiate the Unit Under Test (UUT)
   uut: std_sig PORT MAP (
          clk_i => clk_i,
          bus_i => bus_i,
          busDelayed_o => busDelayed_o
        );

   -- Clock process definitions
   clk_i_process :process
   begin
		clk_i <= '0';
		wait for clk_i_period/2;
		clk_i <= '1';
		wait for clk_i_period/2;
   end process;
 

   -- Stimulus process
   stim_proc: process
   begin		
      -- hold reset state for 100 ns.
      wait for 100 ns;	

      wait for clk_i_period*10;

      -- insert stimulus here 
		bus_i <= x"00FA";
      wait;
   end process;

END;
