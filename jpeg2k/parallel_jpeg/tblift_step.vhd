--------------------------------------------------------------------------------
-- Company: 
-- Engineer:
--
-- Create Date:   17:47:25 04/06/2015
-- Design Name:   
-- Module Name:   C:\Users\vidal\Documents\GitHub\jpeg-2000-test\jpeg2k\parallel_jpeg\tblift_step.vhd
-- Project Name:  lift_step
-- Target Device:  
-- Tool versions:  
-- Description:   
-- 
-- VHDL Test Bench Created by ISE for module: lift_step
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
 
ENTITY tblift_step IS
END tblift_step;
 
ARCHITECTURE behavior OF tblift_step IS 
 
    -- Component Declaration for the Unit Under Test (UUT)
 
    COMPONENT lift_step
    PORT(
         left_i : IN  unsigned(8 downto 0);
         sam_i : IN  unsigned(8 downto 0);
         right_i : IN  unsigned(8 downto 0);
         flgs_i : IN  unsigned(4 downto 0);
         update_i : IN  std_logic;
         clk : IN  std_logic;
         res_o : OUT  signed(9 downto 0);
         update_o : OUT  std_logic
        );
    END COMPONENT;
	 
COMPONENT signed2twoscomplement
    port (
        x: in signed (9 downto 0);
        z: out unsigned(8 downto 0)
    );
end COMPONENT;    

   --Inputs
   signal left_i : unsigned(8 downto 0) := (others => '0');
   signal sam_i : unsigned(8 downto 0) := (others => '0');
   signal right_i : unsigned(8 downto 0) := (others => '0');
   signal flgs_i : unsigned(4 downto 0) := (others => '0');
   signal update_i : std_logic := '0';
   signal clk : std_logic := '0';
   signal x : signed(9 downto 0);
 	--Outputs
   signal res_o : signed(9 downto 0);
   signal update_o : std_logic;
	signal z : unsigned(8 downto 0) := (others => '0');

   -- Clock period definitions
   constant clk_period : time := 10 ns;
 
BEGIN
 
	-- Instantiate the Unit Under Test (UUT)
   uut: lift_step PORT MAP (
          left_i => left_i,
          sam_i => sam_i,
          right_i => right_i,
          flgs_i => flgs_i,
          update_i => update_i,
          clk => clk,
          res_o => res_o,
          update_o => update_o
        );
   signed2twoscomplement_u0 : signed2twoscomplement PORT MAP(
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
	  left_i <= b"010100100";
	  wait for 10 ns;
	  sam_i <= b"010011111";
	  wait for 10 ns;
	  right_i <= b"010011100";
	  wait for 10 ns;
	  flgs_i <= b"00111";
	  wait for 10 ns;
	  update_i <= '1';
	  wait for 10 ns;
	  x <= res_o;
	  wait for 10 ns;
	  update_i <= '0';
	  sam_i <= b"111111111";
	  wait for 10 ns;
	  flgs_i <= b"00101";
	  wait for 10 ns;
	  update_i <= '1';
	  wait for 10 ns;
	  x <= res_o;
	  wait for 10 ns;
	  update_i <= '0';
	  wait for 10 ns;
	  sam_i <= b"010011111";
	  wait for 10 ns;
	  flgs_i <= b"00110";
	  wait for 10 ns;
	  update_i <= '1';
	  wait for 10 ns;
	  x <= res_o;
	  wait for 10 ns;
	  update_i <= '0';
	  wait for 10 ns;
	  sam_i <= b"011101111";
	  wait for 10 ns;
	  flgs_i <= b"00100";
	  wait for 10 ns;
	  update_i <= '1';
	  wait for 10 ns;
	  x <= res_o;
	  wait for 10 ns;
	  update_i <= '0';
	  wait for 10 ns;
      wait;
   end process;

END;
