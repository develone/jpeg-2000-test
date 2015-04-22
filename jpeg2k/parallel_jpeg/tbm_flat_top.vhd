--------------------------------------------------------------------------------
-- Company: 
-- Engineer:
--
-- Create Date:   14:56:43 04/20/2015
-- Design Name:   
-- Module Name:   C:/Users/vidal/Documents/GitHub/jpeg-2000-test/jpeg2k/parallel_jpeg/tbm_flat_top.vhd
-- Project Name:  jpeg_para
-- Target Device:  
-- Tool versions:  
-- Description:   
-- 
-- VHDL Test Bench Created by ISE for module: m_flat_top
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
 
ENTITY tbm_flat_top IS
END tbm_flat_top;
 
ARCHITECTURE behavior OF tbm_flat_top IS 
 
    -- Component Declaration for the Unit Under Test (UUT)
 
    COMPONENT m_flat_top
    PORT(
         clock : IN  std_logic;
         reset : IN  std_logic;
         sdi : IN  std_logic_vector(8 downto 0);
         sdo : OUT  std_logic_vector(8 downto 0)
        );
    END COMPONENT;
    

   --Inputs
   signal clock : std_logic := '0';
   signal reset : std_logic := '0';
   signal sdi : std_logic_vector(8 downto 0) := (others => '0');

 	--Outputs
   signal sdo : std_logic_vector(8 downto 0);

   -- Clock period definitions
   constant clock_period : time := 10 ns;
 
BEGIN
 
	-- Instantiate the Unit Under Test (UUT)
   uut: m_flat_top PORT MAP (
          clock => clock,
          reset => reset,
          sdi => sdi,
          sdo => sdo
        );

   -- Clock process definitions
   clock_process :process
   begin
		clock <= '0';
		wait for clock_period/2;
		clock <= '1';
		wait for clock_period/2;
   end process;
 

   -- Stimulus process
   stim_proc: process
   begin		
      -- hold reset state for 100 ns.
      wait for 100 ns;	

      wait for clock_period*10;

      -- insert stimulus here 

      wait;
   end process;

END;
