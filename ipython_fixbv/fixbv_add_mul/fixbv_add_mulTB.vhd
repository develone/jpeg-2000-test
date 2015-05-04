--------------------------------------------------------------------------------
-- Company: 
-- Engineer:
--
-- Create Date:   13:06:25 05/04/2015
-- Design Name:   
-- Module Name:   C:/Users/vidal/Documents/GitHub/jpeg-2000-test/ipython_fixbv/fixbv_add_mul/fixbv_add_mulTB.vhd
-- Project Name:  fixbv_add_mul
-- Target Device:  
-- Tool versions:  
-- Description:   
-- 
-- VHDL Test Bench Created by ISE for module: fixbv_mul
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
use std.textio.all;

use work.pck_myhdl_090.all;
-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--USE ieee.numeric_std.ALL;
 
ENTITY fixbv_add_mulTB IS
END fixbv_add_mulTB;
 
ARCHITECTURE behavior OF fixbv_add_mulTB IS 
 
    -- Component Declaration for the Unit Under Test (UUT)
 
    COMPONENT fixbv_mul
    PORT(
         clk : IN  std_logic;
         do_prod : IN  std_logic;
         x_sig : IN  unsigned(31 downto 0);
         y_sig : IN  unsigned(31 downto 0);
         prod_sig : OUT  unsigned(63 downto 0)
        );
    END COMPONENT;
	 
    COMPONENT fixbv_add 
    port (
        clk: in std_logic;
        do_add: in std_logic;
        x_sig: in unsigned(31 downto 0);
        y_sig: in unsigned(31 downto 0);
        sum_sig: out unsigned(31 downto 0)
    );
    END COMPONENT;
	 
   --Inputs
   signal clk : std_logic := '0';
   signal do_prod : std_logic := '0';
	signal do_add : std_logic := '0';
   signal x_sig : unsigned(31 downto 0) := (others => '0');
   signal y_sig : unsigned(31 downto 0) := (others => '0');

 	--Outputs
   signal prod_sig : unsigned(63 downto 0);
   signal sum_sig: unsigned(31 downto 0);
	
   -- Clock period definitions
   constant clk_period : time := 10 ns;
 
BEGIN
 
	-- Instantiate the Unit Under Test (UUT)
   uut: fixbv_mul PORT MAP (
          clk => clk,
          do_prod => do_prod,
          x_sig => x_sig,
          y_sig => y_sig,
          prod_sig => prod_sig
        );

   uut1: fixbv_add PORT MAP (
          clk => clk,
          do_add => do_add,
          x_sig => x_sig,
          y_sig => y_sig,
          sum_sig => sum_sig
        );
   -- Clock process definitions
   clk_process :process
   begin
		clk <= '0';
		wait for clk_period/2;
		clk <= '1';
		wait for clk_period/2;
   end process;
 

   -- Stimulus process
   stim_proc: process
   begin		
      -- hold reset state for 100 ns.
      wait for 100 ns;	

      wait for clk_period*10;

      -- insert stimulus here 
      x_sig <= X"00c90fde";
		wait for 10 ns;
		y_sig <= X"00200000";
		wait for 10 ns;
		do_add <= '1';
		wait for 10 ns;
		do_add <= '0';
		wait for 10 ns;
		do_prod <= '1';
		wait for 10 ns;
		do_prod <= '0';
		wait for 10 ns;
      wait;
   end process;

END;
