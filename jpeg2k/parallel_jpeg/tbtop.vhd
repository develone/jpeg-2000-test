--------------------------------------------------------------------------------
-- Company: 
-- Engineer:
--
-- Create Date:   08:51:57 04/07/2015
-- Design Name:   
-- Module Name:   C:/Xilinx/14.7/ISE_DS/lift_step/tbtop.vhd
-- Project Name:  lift_step
-- Target Device:  
-- Tool versions:  
-- Description:   
-- 
-- VHDL Test Bench Created by ISE for module: top
-- 
-- Dependencies:
-- 
-- Revision:
-- Revision 0.01 - File Created
-- Additional Comments:
--
-- Notes: 
-- This testbench has been automatically generated using types std_logic and
--unsigned for the ports of the unit under test.  Xilinx recommends
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
 
ENTITY tbtop IS
END tbtop;
 
ARCHITECTURE behavior OF tbtop IS 
 
    -- Component Declaration for the Unit Under Test (UUT)
 
    COMPONENT top
    PORT(
         clk : IN  std_logic;
         x : IN signed(9 downto 0);
         z : OUT unsigned(8 downto 0)
        );
    END COMPONENT;
    

   --Inputs
   signal clk : std_logic := '0';
   signal x :signed(9 downto 0) := (others => '0');

 	--Outputs
   signal z :unsigned(8 downto 0);

   -- Clock period definitions
   constant clk_period : time := 10 ns;
signal jpeg_instance_15_update_i: std_logic:= '0';
signal jpeg_instance_15_left_i: unsigned(8 downto 0):= (others => '0');
signal jpeg_instance_15_right_i: unsigned(8 downto 0):= (others => '0');
signal jpeg_instance_15_flgs_i: unsigned(4 downto 0):= (others => '0');
signal jpeg_instance_15_res_o: signed (9 downto 0):= (others => '0');
signal jpeg_instance_15_sam_i: unsigned(8 downto 0):= (others => '0');
signal jpeg_instance_15_update_o: std_logic:= '1';
signal jpeg_instance_14_update_i: std_logic:= '0';
signal jpeg_instance_14_left_i: unsigned(8 downto 0):= (others => '0');
signal jpeg_instance_14_right_i: unsigned(8 downto 0):= (others => '0');
signal jpeg_instance_14_flgs_i: unsigned(4 downto 0):= (others => '0');
signal jpeg_instance_14_res_o: signed (9 downto 0):= (others => '0');
signal jpeg_instance_14_sam_i: unsigned(8 downto 0);
signal jpeg_instance_14_update_o: std_logic;
signal jpeg_instance_13_update_i: std_logic;
signal jpeg_instance_13_left_i: unsigned(8 downto 0);
signal jpeg_instance_13_right_i: unsigned(8 downto 0);
signal jpeg_instance_13_flgs_i: unsigned(4 downto 0);
signal jpeg_instance_13_res_o: signed (9 downto 0);
signal jpeg_instance_13_sam_i: unsigned(8 downto 0);
signal jpeg_instance_13_update_o: std_logic;
signal jpeg_instance_12_update_i: std_logic;
signal jpeg_instance_12_left_i: unsigned(8 downto 0);
signal jpeg_instance_12_right_i: unsigned(8 downto 0);
signal jpeg_instance_12_flgs_i: unsigned(4 downto 0);
signal jpeg_instance_12_res_o: signed (9 downto 0);
signal jpeg_instance_12_sam_i: unsigned(8 downto 0);
signal jpeg_instance_12_update_o: std_logic;
signal jpeg_instance_11_update_i: std_logic;
signal jpeg_instance_11_left_i: unsigned(8 downto 0);
signal jpeg_instance_11_right_i: unsigned(8 downto 0);
signal jpeg_instance_11_flgs_i: unsigned(4 downto 0);
signal jpeg_instance_11_res_o: signed (9 downto 0);
signal jpeg_instance_11_sam_i: unsigned(8 downto 0);
signal jpeg_instance_11_update_o: std_logic;
signal jpeg_instance_10_update_i: std_logic;
signal jpeg_instance_10_left_i: unsigned(8 downto 0);
signal jpeg_instance_10_right_i: unsigned(8 downto 0);
signal jpeg_instance_10_flgs_i: unsigned(4 downto 0);
signal jpeg_instance_10_res_o: signed (9 downto 0);
signal jpeg_instance_10_sam_i: unsigned(8 downto 0);
signal jpeg_instance_10_update_o: std_logic;
signal jpeg_instance_9_update_i: std_logic;
signal jpeg_instance_9_left_i: unsigned(8 downto 0);
signal jpeg_instance_9_right_i: unsigned(8 downto 0);
signal jpeg_instance_9_flgs_i: unsigned(4 downto 0);
signal jpeg_instance_9_res_o: signed (9 downto 0);
signal jpeg_instance_9_sam_i: unsigned(8 downto 0);
signal jpeg_instance_9_update_o: std_logic;
signal jpeg_instance_8_update_i: std_logic;
signal jpeg_instance_8_left_i: unsigned(8 downto 0);
signal jpeg_instance_8_right_i: unsigned(8 downto 0);
signal jpeg_instance_8_flgs_i: unsigned(4 downto 0);
signal jpeg_instance_8_res_o: signed (9 downto 0);
signal jpeg_instance_8_sam_i: unsigned(8 downto 0);
signal jpeg_instance_8_update_o: std_logic;
signal jpeg_instance_7_update_i: std_logic;
signal jpeg_instance_7_left_i: unsigned(8 downto 0);
signal jpeg_instance_7_right_i: unsigned(8 downto 0);
signal jpeg_instance_7_flgs_i: unsigned(4 downto 0);
signal jpeg_instance_7_res_o: signed (9 downto 0);
signal jpeg_instance_7_sam_i: unsigned(8 downto 0);
signal jpeg_instance_7_update_o: std_logic;
signal jpeg_instance_6_update_i: std_logic;
signal jpeg_instance_6_left_i: unsigned(8 downto 0);
signal jpeg_instance_6_right_i: unsigned(8 downto 0);
signal jpeg_instance_6_flgs_i: unsigned(4 downto 0);
signal jpeg_instance_6_res_o: signed (9 downto 0);
signal jpeg_instance_6_sam_i: unsigned(8 downto 0);
signal jpeg_instance_6_update_o: std_logic;
signal jpeg_instance_5_update_i: std_logic;
signal jpeg_instance_5_left_i: unsigned(8 downto 0);
signal jpeg_instance_5_right_i: unsigned(8 downto 0);
signal jpeg_instance_5_flgs_i: unsigned(4 downto 0);
signal jpeg_instance_5_res_o: signed (9 downto 0);
signal jpeg_instance_5_sam_i: unsigned(8 downto 0);
signal jpeg_instance_5_update_o: std_logic;
signal jpeg_instance_4_update_i: std_logic;
signal jpeg_instance_4_left_i: unsigned(8 downto 0);
signal jpeg_instance_4_right_i: unsigned(8 downto 0);
signal jpeg_instance_4_flgs_i: unsigned(4 downto 0);
signal jpeg_instance_4_res_o: signed (9 downto 0);
signal jpeg_instance_4_sam_i: unsigned(8 downto 0);
signal jpeg_instance_4_update_o: std_logic;
signal jpeg_instance_3_update_i: std_logic;
signal jpeg_instance_3_left_i: unsigned(8 downto 0);
signal jpeg_instance_3_right_i: unsigned(8 downto 0);
signal jpeg_instance_3_flgs_i: unsigned(4 downto 0);
signal jpeg_instance_3_res_o: signed (9 downto 0);
signal jpeg_instance_3_sam_i: unsigned(8 downto 0);
signal jpeg_instance_3_update_o: std_logic;
signal jpeg_instance_2_update_i: std_logic;
signal jpeg_instance_2_left_i: unsigned(8 downto 0);
signal jpeg_instance_2_right_i: unsigned(8 downto 0);
signal jpeg_instance_2_flgs_i: unsigned(4 downto 0);
signal jpeg_instance_2_res_o: signed (9 downto 0);
signal jpeg_instance_2_sam_i: unsigned(8 downto 0);
signal jpeg_instance_2_update_o: std_logic;
signal jpeg_instance_1_update_i: std_logic;
signal jpeg_instance_1_left_i: unsigned(8 downto 0);
signal jpeg_instance_1_right_i: unsigned(8 downto 0);
signal jpeg_instance_1_flgs_i: unsigned(4 downto 0);
signal jpeg_instance_1_res_o: signed (9 downto 0);
signal jpeg_instance_1_sam_i: unsigned(8 downto 0);
signal jpeg_instance_1_update_o: std_logic;
signal jpeg_instance_0_update_i: std_logic;
signal jpeg_instance_0_left_i: unsigned(8 downto 0);
signal jpeg_instance_0_right_i: unsigned(8 downto 0);
signal jpeg_instance_0_flgs_i: unsigned(4 downto 0);
signal jpeg_instance_0_res_o: signed (9 downto 0);
signal jpeg_instance_0_sam_i: unsigned(8 downto 0);
signal jpeg_instance_0_update_o: std_logic;
BEGIN
 
	-- Instantiate the Unit Under Test (UUT)
   uut: top PORT MAP (
          clk => clk,
          x => x,
          z => z
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
jpeg_instance_15_left_i <= b"010100100";
wait for 10 ns;
jpeg_instance_15_sam_i <= b"011101111";
wait for 10 ns;
jpeg_instance_15_right_i <= b"010011100";
wait for 10 ns;
jpeg_instance_15_flgs_i <= b"00111";
wait for 10 ns;
jpeg_instance_15_update_i <= '1';
wait for 10 ns;
jpeg_instance_15_update_i <= '0';
wait for 10 ns;
x <= jpeg_instance_15_res_o;
 wait for 10 ns;  

jpeg_instance_14_left_i <= b"010100100";
wait for 10 ns;
jpeg_instance_14_sam_i <= b"011101111";
wait for 10 ns;
jpeg_instance_14_right_i <= b"010011100";
wait for 10 ns;
jpeg_instance_14_flgs_i <= b"00111";
wait for 10 ns;
jpeg_instance_14_update_i <= '1';
wait for 10 ns;
jpeg_instance_14_update_i <= '0';
wait for 10 ns;
x <= jpeg_instance_14_res_o;
wait for 10 ns;

jpeg_instance_13_left_i <= b"010100100";
wait for 10 ns;
jpeg_instance_13_sam_i <= b"011101111";
wait for 10 ns;
jpeg_instance_13_right_i <= b"010011100";
wait for 10 ns;
jpeg_instance_13_flgs_i <= b"00111";
wait for 10 ns;
jpeg_instance_13_update_i <= '1';
wait for 10 ns;
jpeg_instance_13_update_i <= '0';
wait for 10 ns;
x <= jpeg_instance_13_res_o;
 wait for 10 ns;

jpeg_instance_12_left_i <= b"010100100";
wait for 10 ns;
jpeg_instance_12_sam_i <= b"011101111";
wait for 10 ns;
jpeg_instance_12_right_i <= b"010011100";
wait for 10 ns;
jpeg_instance_12_flgs_i <= b"00111";
wait for 10 ns;
jpeg_instance_12_update_i <= '1';
wait for 10 ns;
jpeg_instance_12_update_i <= '0';
wait for 10 ns;
x <= jpeg_instance_12_res_o;
 wait for 10 ns;

jpeg_instance_11_left_i <= b"010100100";
wait for 10 ns;
jpeg_instance_11_sam_i <= b"011101111";
wait for 10 ns;
jpeg_instance_11_right_i <= b"010011100";
wait for 10 ns;
jpeg_instance_11_flgs_i <= b"00111";
wait for 10 ns;
jpeg_instance_11_update_i <= '1';
wait for 10 ns;
jpeg_instance_11_update_i <= '0';
wait for 10 ns;
x <= jpeg_instance_11_res_o;
 wait for 10 ns;

jpeg_instance_10_left_i <= b"010100100";
wait for 10 ns;
jpeg_instance_10_sam_i <= b"011101111";
wait for 10 ns;
jpeg_instance_10_right_i <= b"010011100";
wait for 10 ns;
jpeg_instance_10_flgs_i <= b"00111";
wait for 10 ns;
jpeg_instance_10_update_i <= '1';
wait for 10 ns;
jpeg_instance_10_update_i <= '0';
wait for 10 ns;
x <= jpeg_instance_10_res_o;
wait for 10 ns;

jpeg_instance_9_left_i <= b"010100100";
wait for 10 ns;
jpeg_instance_9_sam_i <= b"011101111";
wait for 10 ns;
jpeg_instance_9_right_i <= b"010011100";
wait for 10 ns;
jpeg_instance_9_flgs_i <= b"00111";
wait for 10 ns;
jpeg_instance_9_update_i <= '1';
wait for 10 ns;
jpeg_instance_9_update_i <= '0';
wait for 10 ns;
x <= jpeg_instance_9_res_o;
wait for 10 ns;

wait;
   end process;

END;
