--------------------------------------------------------------------------------
-- Company: 
-- Engineer:
--
-- Create Date:   15:36:43 09/09/2014
-- Design Name:   
-- Module Name:   C:/Xilinx/14.7/ISE_DS/demo_sim/jpegTB.vhd
-- Project Name:  demo_sim
-- Target Device:  
-- Tool versions:  
-- Description:   
-- 
-- VHDL Test Bench Created by ISE for module: jpeg
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

use work.pck_myhdl_09.all; 
-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--USE ieee.numeric_std.ALL;
 
ENTITY jpegTB IS
END jpegTB;
 
ARCHITECTURE behavior OF jpegTB IS 
 
    -- Component Declaration for the Unit Under Test (UUT)
 
    COMPONENT jpeg
    PORT(
         clk_fast : IN  std_logic;
         left_s : IN  signed(15 downto 0);
         right_s : IN  signed(15 downto 0);
         sam_s : IN  signed(15 downto 0);
         res_s : OUT  signed(15 downto 0);
         even_odd_s : IN  std_logic;
         fwd_inv_s : IN  std_logic
        );
    END COMPONENT;
    

   --Inputs
   signal clk_fast : std_logic := '0';
   signal left_s : signed(15 downto 0) := (others => '0');
   signal right_s : signed(15 downto 0) := (others => '0');
   signal sam_s : signed(15 downto 0) := (others => '0');
   signal even_odd_s : std_logic := '0';
   signal fwd_inv_s : std_logic := '0';

 	--Outputs
   signal res_s : signed(15 downto 0);

   -- Clock period definitions
   constant clk_fast_period : time := 10 ns;
 
BEGIN
 
	-- Instantiate the Unit Under Test (UUT)
   uut: jpeg PORT MAP (
          clk_fast => clk_fast,
          left_s => left_s,
          right_s => right_s,
          sam_s => sam_s,
          res_s => res_s,
          even_odd_s => even_odd_s,
          fwd_inv_s => fwd_inv_s
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
