--------------------------------------------------------------------------------
-- Company: 
-- Engineer:
--
-- Create Date:   08:07:26 09/28/2014
-- Design Name:   
-- Module Name:   C:/Xilinx/14.7/ISE_DS/delaytest/TBdel_test.vhd
-- Project Name:  delaytest
-- Target Device:  
-- Tool versions:  
-- Description:   
-- 
-- VHDL Test Bench Created by ISE for module: del_test
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
use IEEE.numeric_std.all;
-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--USE ieee.numeric_std.ALL;
 
ENTITY TBdel_test IS
END TBdel_test;
 
ARCHITECTURE behavior OF TBdel_test IS 
 
    -- Component Declaration for the Unit Under Test (UUT)
 
    COMPONENT del_test
    PORT(
         clk_fast : IN  std_logic;
         left_s : IN  signed(15 downto 0);
         signed_res_s : OUT  signed(15 downto 0)
        );
    END COMPONENT;
    

   --Inputs
   signal clk_fast : std_logic := '0';
   signal left_s : std_logic_vector(15 downto 0) := (others => '0');

 	--Outputs
   signal signed_res_s : signed(15 downto 0);

   -- Clock period definitions
   constant clk_fast_period : time := 10 ns;
 
BEGIN
 
	-- Instantiate the Unit Under Test (UUT)
   uut: del_test PORT MAP (
          clk_fast => clk_fast,
          left_s => signed(left_s),
          signed_res_s => signed_res_s
        );

   -- Clock process definitions
   clk_fast_process :process
   begin
		clk_fast <= '0';
		wait for clk_fast_period/2;
		clk_fast <= '1';
		wait for clk_fast_period/2;
   end process;
 

   -- Stimulus process
   stim_proc: process
   begin		
      -- hold reset state for 100 ns.
      wait for 100 ns;	

      wait for clk_fast_period*10;

      -- insert stimulus here 

      wait;
   end process;

END;
