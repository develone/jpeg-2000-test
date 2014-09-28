--------------------------------------------------------------------------------
-- Company: 
-- Engineer:
--
-- Create Date:   13:45:40 09/28/2014
-- Design Name:   
-- Module Name:   C:/Xilinx/14.7/ISE_DS/delay/TBstd_sig.vhd
-- Project Name:  delay
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
         a_i : IN  std_logic;
         aDelayed_o : OUT  std_logic
        );
    END COMPONENT;
    

   --Inputs
   signal clk_i : std_logic := '0';
   signal a_i : std_logic := '0';

 	--Outputs
   signal aDelayed_o : std_logic;

   -- Clock period definitions
   constant clk_i_period : time := 10 ns;
 
BEGIN
 
	-- Instantiate the Unit Under Test (UUT)
   uut: std_sig PORT MAP (
          clk_i => clk_i,
          a_i => a_i,
          aDelayed_o => aDelayed_o
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
      a_i <= '1';
		wait for 100 ns;
		a_i <= '0';
      wait;
   end process;

END;
