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
use IEEE.STD_LOGIC_UNSIGNED.ALL;
use IEEE.NUMERIC_STD.ALL;

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
			sigDel_s : in STD_LOGIC;
			sigDel_flag : in std_logic;
			sigDelayed_s : out STD_LOGIC;
         left_sv : IN  std_logic_vector :=(15 downto 0 => '0') ;
         leftDelDut_s : OUT  std_logic_vector :=(15 downto 0 => '0');
			even_odd_s : in std_logic;
			fwd_inv_s : in std_logic;
			updated_s : in std_logic;
			noupdate_s : out std_logic;
         left_s, sam_s, right_s, lf_del : in signed(15 downto 0);
         res_s : out signed(15 downto 0);
			fpgaClk_i : in    std_logic; -- 12 MHz clock input from external clock source.
			sdClkFb_i : in    std_logic  -- 100 MHz clock fed back into FPGA.
			);
    END COMPONENT;
    

   --Inputs
   signal clk_i : std_logic := '0' ;
	signal sigDel_s  : std_logic := '0' ;
	signal sigDel_flag  : std_logic := '0' ;
	signal even_odd_s : std_logic := '0' ; 
	signal fwd_inv_s : std_logic := '0' ;
	signal updated_s : std_logic := '0' ;
	signal left_sv : std_logic_vector (15 downto 0);
   signal left_s, sam_s, right_s, lf_del : signed(15 downto 0);
	signal fpgaClk_i : std_logic := '0' ;
	signal sdClkFb_i : std_logic := '0' ;
 	--Outputs
   signal leftDelDut_s : std_logic_vector (15 downto 0);
	signal res_s : signed(15 downto 0);
	signal sigDelayed_s, noupdate_s  : std_logic;
 
   -- Clock period definitions
   constant clk_i_period : time := 10 ns;
 
BEGIN
 
	-- Instantiate the Unit Under Test (UUT)
   uut: std_sig PORT MAP (
          clk_i => clk_i,
          left_sv => left_sv,
          leftDelDut_s => leftDelDut_s,
			 lf_del => lf_del,
          sigDel_s => sigDel_s,
			 sigDel_flag => sigDel_flag,
			 sigDelayed_s => sigDelayed_s,
			 left_s => left_s,
			 sam_s => sam_s,
			 right_s => right_s,
			 res_s => res_s,
			 even_odd_s => even_odd_s,
			 fwd_inv_s => fwd_inv_s,
			 updated_s => updated_s,
			 noupdate_s => noupdate_s,
			 fpgaClk_i => fpgaClk_i,
			 sdClkFb_i => sdClkFb_i
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

		left_s <= x"00A3";
		sam_s <= x"00A0";
		right_s <= x"009B";
		even_odd_s <= '1';
		fwd_inv_s <= '1';
		updated_s <= '0';
		wait for 100 ns;	
		updated_s <= '1';
		wait for 100 ns;
		
		wait for 100 ns;
      left_s <= x"00A3";
		sam_s <= x"00A0";
		right_s <= x"009B";      
      wait for 100 ns;
      left_s <= x"009B";
		sam_s <= x"009B";
		right_s <= x"009D";
      left_sv <= x"009B";
		sigDel_s <= '1';		
		wait;
   end process;

END;
