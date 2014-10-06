--------------------------------------------------------------------------------
-- Company: 
-- Engineer:
--
-- Create Date:   11:51:10 10/06/2014
-- Design Name:   
-- Module Name:   C:/Xilinx/14.7/ISE_DS/rammyhdl/ram_tb.vhd
-- Project Name:  rammyhdl
-- Target Device:  
-- Tool versions:  
-- Description:   
-- 
-- VHDL Test Bench Created by ISE for module: ram
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
 
ENTITY jpeg2k_tb IS
END jpeg2k_tb;
 
ARCHITECTURE behavior OF jpeg2k_tb IS 
signal dout_lf : unsigned(15 downto 0);
signal din_lf : unsigned(15 downto 0);    
signal addr_lf : unsigned(6 downto 0);
signal we_lf : std_logic;

signal dout_sam : unsigned(15 downto 0);
signal din_sam : unsigned(15 downto 0);    
signal addr_sam : unsigned(6 downto 0);
signal we_sam : std_logic;

signal dout_rht : unsigned(15 downto 0);
signal din_rht : unsigned(15 downto 0);    
signal addr_rht : unsigned(6 downto 0);
signal we_rht : std_logic;

signal dout_res : unsigned(15 downto 0);
signal din_res : unsigned(15 downto 0);    
signal addr_res : unsigned(6 downto 0);
signal we_res : std_logic;

signal left_s, sam_s, right_s, res_s :  signed(15 downto 0);
signal  even_odd_s, fwd_inv_s, clk_fast : std_logic;
signal updated_s, noupdate_s : std_logic; 
 
    -- Component Declaration for the Unit Under Test (UUT)
    COMPONENT jpeg2k
    PORT(
         clk_i : IN  std_logic
        );
    END COMPONENT;   
	 
COMPONENT ram
    PORT(
         dout : OUT  unsigned(15 downto 0);
         din : IN  unsigned(15 downto 0);
         addr : IN  unsigned(6 downto 0);
         we : IN  std_logic;
         clk_fast : IN  std_logic
        );
    END COMPONENT;
component jpeg is
    port (
        clk_fast: in std_logic;
        left_s: in signed (15 downto 0);
        right_s: in signed (15 downto 0);
        sam_s: in signed (15 downto 0);
        res_s: out signed (15 downto 0);
		  even_odd_s : in std_logic ;
		  fwd_inv_s : in std_logic;
		  updated_s : in std_logic;
		  noupdate_s : out std_logic
    );
	 end component;	 


   --Inputs
--   signal din : unsigned(15 downto 0) := (others => '0');
--   signal addr : unsigned(6 downto 0) := (others => '0');
--   signal we : std_logic := '0';
--   signal clk : std_logic := '0';
--
-- 	--Outputs
--   signal dout : unsigned(15 downto 0);

   -- Clock period definitions
   constant clk_period : time := 10 ns;
   --Inputs
   signal clk_i : std_logic := '0';

   -- Clock period definitions
   constant clk_i_period : time := 10 ns; 
BEGIN
lfram : ram
  port map(
     dout => dout_lf,
	  din => din_lf,
	  addr => addr_lf,
	  we => we_lf,
	  clk_fast => clk_i
	  );
	  
samram : ram
  port map(
     dout => dout_sam,
	  din => din_sam,
	  addr => addr_sam,
	  we => we_sam,
	  clk_fast => clk_i
	  );
	  
rhtram : ram
  port map(
     dout => dout_rht,
	  din => din_rht,
	  addr => addr_rht,
	  we => we_rht,
	  clk_fast => clk_i
	  );

resram : ram
  port map(
     dout => dout_res,
	  din => din_res,
	  addr => addr_res,
	  we => we_res,
	  clk_fast => clk_i
	  );
		  
ujpeg: jpeg 
	port map( 
        clk_fast => clk_i,
        left_s => left_s,
        right_s => right_s,
        sam_s => sam_s,
        res_s => res_s,
        even_odd_s => even_odd_s,
		  fwd_inv_s => fwd_inv_s,
        updated_s => updated_s,
        noupdate_s => noupdate_s		  
		  );	 
	-- Instantiate the Unit Under Test (UUT)
 

   -- Clock process definitions
   clk_process :process
   begin
		clk_i <= '0';
		wait for clk_period/2;
		clk_i <= '1';
		wait for clk_period/2;
   end process;
 

   -- Stimulus process
   stim_proc: process
   begin		
      -- hold reset state for 100 ns.
      wait for 100 ns;	

      wait for clk_period*10;

      -- insert stimulus here 
     we_lf <= '1';
		we_sam <= '1';
		we_rht <= '1';
		we_res <= '1';
		
      addr_lf <= b"0000001";
		addr_sam <= b"0000001";	
		addr_rht <= b"0000001";
		addr_res <= b"0000001";
		
		din_lf <= x"00a3";
		din_sam <= x"00a0";
      din_rht <= x"009b";
		wait for 20 ns;
		updated_s <= '1';
		even_odd_s <= '1';
		fwd_inv_s <= '1';
		left_s <= signed(dout_lf);
	   sam_s <= signed(dout_sam);
      right_s <= signed(dout_rht);
		wait for 20 ns;
      din_res <= unsigned(res_s);

      addr_lf <= b"0000011";
		addr_sam <= b"0000011";	
		addr_rht <= b"0000011";
		addr_res <= b"0000011";
		
		din_lf <= x"009b";
		din_sam <= x"009b";
      din_rht <= x"009d";
		
		wait for 20 ns;
		updated_s <= '1';
		even_odd_s <= '0';
		fwd_inv_s <= '1';
		left_s <= signed(dout_lf);
	   sam_s <= signed(dout_sam);
      right_s <= signed(dout_rht);
		wait for 20 ns;
      din_res <= unsigned(res_s);
      wait;
   end process;

END;
