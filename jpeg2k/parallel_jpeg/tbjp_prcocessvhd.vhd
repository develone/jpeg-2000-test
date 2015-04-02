--------------------------------------------------------------------------------
-- Company: 
-- Engineer:
--
-- Create Date:   17:45:17 04/01/2015
-- Design Name:   
-- Module Name:   C:/Xilinx/14.7/ISE_DS/jpeg_para/tbjp_prcocessvhd.vhd
-- Project Name:  jpeg_para
-- Target Device:  
-- Tool versions:  
-- Description:   
-- 
-- VHDL Test Bench Created by ISE for module: top_jpeg
-- 
-- Dependencies:
-- 
-- Revision:
-- Revision 0.01 - File Created
-- Additional Comments:
--
-- Notes: 
-- This testbench has been automatically generated using types std_logic and
-- unsigned for the ports of the unit under test.  Xilinx recommends
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
 
ENTITY tbjp_prcocessvhd IS
END tbjp_prcocessvhd;
 
ARCHITECTURE behavior OF tbjp_prcocessvhd IS 
 
    -- Component Declaration for the Unit Under Test (UUT)
 
    COMPONENT top_jpeg
    PORT(
         clk : IN  std_logic;
         res_out_x : OUT  signed(9 downto 0);
         left_s_i : IN  unsigned(143 downto 0):= (others => '0');
         sam_s_i : IN  unsigned(143 downto 0):= (others => '0');
         right_s_i : IN  unsigned(143 downto 0):= (others => '0');
         flgs_s_i : IN  unsigned(79 downto 0):= (others => '0');
         noupdate_s : OUT  std_logic;
         update_s : IN  std_logic;
         row_ind : IN  unsigned(9 downto 0);
         col_ind : IN  unsigned(9 downto 0);
         flat_lf : OUT  unsigned(143 downto 0);
         flat_sa : OUT  unsigned(143 downto 0);
         flat_rt : OUT  unsigned(143 downto 0);
         z : IN  unsigned(8 downto 0);
         x : IN  signed(9 downto 0);
         ma_row : IN  unsigned(3 downto 0);
         ma_col : IN  unsigned(3 downto 0);
         bits_in_sig : IN  signed(9 downto 0);
         vv : OUT  unsigned(8 downto 0);
         dout_lf : OUT  unsigned(143 downto 0);
         dout_sa : OUT  unsigned(143 downto 0);
         dout_rt : OUT  unsigned(143 downto 0);
         dout_res : OUT  unsigned(8 downto 0);
         din_lf : IN  unsigned(143 downto 0);
         din_sa : IN  unsigned(143 downto 0);
         din_rt : IN  unsigned(143 downto 0);
         din_res : IN  unsigned(8 downto 0);
         addr_lf : IN  unsigned(9 downto 0);
         addr_sa : IN  unsigned(9 downto 0);
         addr_rt : IN  unsigned(9 downto 0);
         addr_res : IN  unsigned(9 downto 0);
         we_lf : IN  std_logic;
         we_sa : IN  std_logic;
         we_rt : IN  std_logic;
         we_res : IN  std_logic;
         dout_flgs : OUT  unsigned(79 downto 0);
         addr_flgs : IN  unsigned(9 downto 0)
        );
    END COMPONENT;
    

   --Inputs
   signal clk : std_logic := '0';
   signal left_s_i : unsigned(143 downto 0) := (others => '0');
   signal sam_s_i : unsigned(143 downto 0) := (others => '0');
   signal right_s_i : unsigned(143 downto 0) := (others => '0');
   signal flgs_s_i : unsigned(79 downto 0) := (others => '0');
   signal update_s : std_logic := '0';
   signal row_ind : unsigned(9 downto 0) := (others => '0');
   signal col_ind : unsigned(9 downto 0) := (others => '0');
   signal z : unsigned(8 downto 0) := (others => '0');
   signal x : signed(9 downto 0) := (others => '0');
   signal ma_row : unsigned(3 downto 0) := (others => '0');
   signal ma_col : unsigned(3 downto 0) := (others => '0');
   signal bits_in_sig : signed(9 downto 0) := (others => '0');
   signal din_lf : unsigned(143 downto 0) := (others => '0');
   signal din_sa : unsigned(143 downto 0) := (others => '0');
   signal din_rt : unsigned(143 downto 0) := (others => '0');
   signal din_res : unsigned(8 downto 0) := (others => '0');
   signal addr_lf : unsigned(9 downto 0) := (others => '0');
   signal addr_sa : unsigned(9 downto 0) := (others => '0');
   signal addr_rt : unsigned(9 downto 0) := (others => '0');
   signal addr_res : unsigned(9 downto 0) := (others => '0');
   signal we_lf : std_logic := '0';
   signal we_sa : std_logic := '0';
   signal we_rt : std_logic := '0';
   signal we_res : std_logic := '0';
   signal addr_flgs : unsigned(9 downto 0) := (others => '0');

 	--Outputs
   signal res_out_x : signed(9 downto 0);
   signal noupdate_s : std_logic;
   signal flat_lf : unsigned(143 downto 0);
   signal flat_sa : unsigned(143 downto 0);
   signal flat_rt : unsigned(143 downto 0);
   signal vv : unsigned(8 downto 0);
   signal dout_lf : unsigned(143 downto 0);
   signal dout_sa : unsigned(143 downto 0);
   signal dout_rt : unsigned(143 downto 0);
   signal dout_res : unsigned(8 downto 0);
   signal dout_flgs : unsigned(79 downto 0);

   -- Clock period definitions
   constant clk_period : time := 10 ns;
 
BEGIN
 
	-- Instantiate the Unit Under Test (UUT)
   uut: top_jpeg PORT MAP (
          clk => clk,
          res_out_x => res_out_x,
          left_s_i => left_s_i,
          sam_s_i => sam_s_i,
          right_s_i => right_s_i,
          flgs_s_i => flgs_s_i,
          noupdate_s => noupdate_s,
          update_s => update_s,
          row_ind => row_ind,
          col_ind => col_ind,
          flat_lf => flat_lf,
          flat_sa => flat_sa,
          flat_rt => flat_rt,
          z => z,
          x => x,
          ma_row => ma_row,
          ma_col => ma_col,
          bits_in_sig => bits_in_sig,
          vv => vv,
          dout_lf => dout_lf,
          dout_sa => dout_sa,
          dout_rt => dout_rt,
          dout_res => dout_res,
          din_lf => din_lf,
          din_sa => din_sa,
          din_rt => din_rt,
          din_res => din_res,
          addr_lf => addr_lf,
          addr_sa => addr_sa,
          addr_rt => addr_rt,
          addr_res => addr_res,
          we_lf => we_lf,
          we_sa => we_sa,
          we_rt => we_rt,
          we_res => we_res,
          dout_flgs => dout_flgs,
          addr_flgs => addr_flgs
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
	  wait for 10 ns;
	  ma_col <= "0011";
	  wait for 10 ns;
	  ma_row <= "0011";
--	  testing -1 to x
	  x <= "1111111111";
	  wait for 10 ns;
	  bits_in_sig <= x;
	  wait for 10 ns;
	  z <= vv;
	  wait for 10 ns;
--	  testing -2 to x
     x <= "1111111110";
	  wait for 10 ns;
	  bits_in_sig <= x;
	  wait for 10 ns;
	  z <= vv;
	  wait for 10 ns;
	  
--	  testing 258 to x
	  x <= "0100000010";
	  wait for 10 ns;
	  bits_in_sig <= x;
	  wait for 10 ns;
	  z <= vv;
	  wait for 10 ns;
--	  testing 110 to x
     x <= "0001101110";
	  wait for 10 ns;
	  bits_in_sig <= x;
	  wait for 10 ns;
	  z <= vv;
	  wait for 10 ns;
--	  lines 259-290
--	  are to test the matrix flat_i
--	  flat_i(3)(3)  <= "0000000001";
--	  wait for 10 ns;
--	  flat_i(3)(2)  <= "0010100010";
--	  wait for 10 ns;
--	  flat_i(3)(1)  <= "0010100011";
--	  wait for 10 ns;
--	  flat_i(3)(0)  <= "0010100100";
--	  wait for 10 ns;
--	  flat_i(2)(3)  <= "0010100001";
--	  wait for 10 ns;
--	  flat_i(2)(2)  <= "0010100010";
--	  wait for 10 ns;
--	  flat_i(2)(1)  <= "0010100011";
--	  wait for 10 ns;
--	  flat_i(2)(0)  <= "0010100100";
--	  wait for 10 ns;	  
--	  flat_i(1)(3)  <= "0000000001";
--	  wait for 10 ns;
--	  flat_i(1)(2)  <= "0110100010";
--	  wait for 10 ns; 
--	  flat_i(1)(1)  <= "0110100011";
--	  wait for 10 ns;
--	  flat_i(1)(0)  <= "0110100100";
--	  wait for 10 ns;
--	  flat_i(0)(3)  <= "0110100001";
--	  wait for 10 ns;
--	  flat_i(0)(2)  <= "0110100010";
--	  wait for 10 ns;
--	  flat_i(0)(1)  <= "0110100011";
--	  wait for 10 ns;
--	  flat_i(0)(0)  <= "0110100100";
	  wait for 10 ns;	  	  
	  addr_lf <= b"0000000000";
	  wait for 10 ns;
	  addr_sa <= b"0000000000";
	  wait for 10 ns;
	  addr_rt <= b"0000000000";
	  wait for 10 ns;
	  addr_flgs <= b"0000000000";
	  wait for 10 ns;
	  we_lf <= '1';
	  wait for 10 ns;
     we_sa <= '1';
	  wait for 10 ns;
     we_sa <= '1';
	  wait for 10 ns;
     we_rt <= '1';
	  wait for 10 ns;
     we_res <= '1';
	  wait for 10 ns;
     din_lf <= x"5229138a452291389c4e271389c5227148a4";
	  wait for 10 ns;
	  din_sa <= x"5627148a452291489c4e271389c4e27138a4";
	  wait for 10 ns;
	  din_rt <= x"52291489c52291489c4e271389c4e29138a4";
	  wait for 10 ns;
	  we_lf <= '0';
	  wait for 10 ns;
	  we_sa <= '0';
     wait for 10 ns;
	  wait for 10 ns;
	  we_rt <= '0';
	  left_s_i <= dout_lf;
	  wait for 10 ns;
	  sam_s_i <=dout_sa;
	  wait for 10 ns;
	  right_s_i <= dout_rt;

	  wait for 10 ns;
	  flgs_s_i <= dout_flgs;
	  wait for 10 ns;
	  addr_res <= b"0000000000";
	  wait for 10 ns;
	  update_s <= '1';
	  wait for 10 ns;
	  bits_in_sig <= res_out_x;
	  wait for 10 ns;
	  din_res <= vv;
	  wait for 10 ns;
	  update_s <= '0';
	  wait for 10 ns;
	  addr_res <= b"0000000001";
	  wait for 10 ns;
	  addr_flgs <= b"0000010000";
	  wait for 10 ns;
	  flgs_s_i <= dout_flgs;
	  wait for 10 ns;
	  update_s <= '1';
	  wait for 10 ns;
	  wait for 10 ns;
	  bits_in_sig <= res_out_x;
	  wait for 10 ns;
	  din_res <= vv;
	  wait for 10 ns;
	  update_s <= '0';
	  wait for 10 ns;
      wait;
   end process;

END;
