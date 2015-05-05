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
         do_mul : IN  std_logic;
         x_sig : IN  signed(30 downto 0);
         y_sig : IN  signed(30 downto 0);
         prod_sig : OUT  unsigned(61 downto 0);
			done_mul: out std_logic
        );
    END COMPONENT;
	 
    COMPONENT fixbv_add 
    port (
        clk: in std_logic;
        do_add: in std_logic;
        x_sig: in signed(30 downto 0);
        y_sig: in signed(30 downto 0);
        sum_sig: out unsigned(31 downto 0);
        done_add: out std_logic   
		  );
    END COMPONENT;
	 
	 COMPONENT fixbv_sub 
    port (
        clk: in std_logic;
        do_sub: in std_logic;
        x_sig: in signed(30 downto 0);
        y_sig: in signed(30 downto 0);
        sub_sig: out signed(31 downto 0);
        done_sub: out std_logic   
		  );
    END COMPONENT;
   --Inputs
   signal clk : std_logic := '0';
   signal do_mul : std_logic := '0';
	signal do_add : std_logic := '0';
	signal do_sub : std_logic := '0';
   signal x_sig : signed(30 downto 0) := (others => '0');
   signal y_sig : signed(30 downto 0) := (others => '0');

 	--Outputs
   signal prod_sig : unsigned(61 downto 0);
   signal sum_sig: unsigned(31 downto 0);
	signal sub_sig: signed(31 downto 0);
	signal done_mul : std_logic := '0';

	signal done_add : std_logic := '0';
   signal done_sub : std_logic := '0';  
 -- Clock period definitions
   constant clk_period : time := 10 ns;
 
BEGIN
 
	-- Instantiate the Unit Under Test (UUT)
   uut: fixbv_mul PORT MAP (
          clk => clk,
          do_mul => do_mul,
          x_sig => x_sig,
          y_sig => y_sig,
          prod_sig => prod_sig,
			 done_mul => done_mul
        );

   uut1: fixbv_add PORT MAP (
          clk => clk,
          do_add => do_add,
          x_sig => x_sig,
          y_sig => y_sig,
          sum_sig => sum_sig,
			 done_add => done_add
        );
		  
	   uut2: fixbv_sub PORT MAP (
          clk => clk,
          do_sub => do_sub,
          x_sig => x_sig,
          y_sig => y_sig,
          sub_sig => sub_sig,
			 done_sub => done_sub
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
      x_sig <= b"0000000001100100100001111110110";
		wait for 10 ns;
		y_sig <= b"0011111111010000000000000000000";
		wait for 10 ns;
		do_add <= '1';
		wait for 10 ns;
		do_add <= '0';
		wait for 10 ns;
			
		do_sub <= '1';
		wait for 10 ns;
		do_sub <= '0';
		wait for 10 ns;
		
		do_mul <= '1';
		wait for 10 ns;
		do_mul <= '0';
		wait for 10 ns;
      wait;
   end process;

END;
