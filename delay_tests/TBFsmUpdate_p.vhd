--------------------------------------------------------------------------------
-- Company: 
-- Engineer:
--
-- Create Date:   17:51:26 10/02/2014
-- Design Name:   
-- Module Name:   C:/Xilinx/14.7/ISE_DS/ttt/TBFsmUpdate_p.vhd
-- Project Name:  ttt
-- Target Device:  
-- Tool versions:  
-- Description:   
-- 
-- VHDL Test Bench Created by ISE for module: FsmUpdate_p
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
use work.pck_myhdl_09.all;

-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
USE ieee.numeric_std.ALL;
 
ENTITY TBFsmUpdate_p IS
END TBFsmUpdate_p;
 
ARCHITECTURE behavior OF TBFsmUpdate_p IS 
 
    -- Component Declaration for the Unit Under Test (UUT)
 
    COMPONENT FsmUpdate_p
    PORT(
         clk_s : IN  std_logic;
         addr_r : OUT  unsigned(13 downto 0);
         addr_x : IN  unsigned(13 downto 0);
			sam_addr_r : OUT  unsigned(13 downto 0);
         sam_addr_x : IN  unsigned(13 downto 0);
			updated_r : OUT  std_logic;
         updated_x : IN  std_logic;
			sigDelayed_r : OUT  std_logic;
         sigDelayed_x : IN  std_logic;
         addrjpeg_r : OUT  unsigned(13 downto 0);
         addrjpeg_x : IN  unsigned(13 downto 0);
			dataToRam_r : OUT  unsigned(15 downto 0);
         dataToRam_x : IN  unsigned(15 downto 0)
			);
    END COMPONENT;
    

   --Inputs
   signal clk_s : std_logic := '0';
   signal addr_x : unsigned(13 downto 0) := (others => '0');
	signal sam_addr_x : unsigned(13 downto 0) := (others => '0');
	signal updated_x : std_logic := '0';
	signal sigDelayed_x : std_logic := '0';
	signal addrjpeg_x : unsigned(13 downto 0) := (others => '0');
	signal dataToRam_x : unsigned(15 downto 0) := (others => '0');
 	--Outputs
   signal addr_r : unsigned(13 downto 0);
	signal sam_addr_r : unsigned(13 downto 0) := (others => '0');
	signal updated_r : std_logic := '0';
	signal sigDelayed_r : std_logic := '0';
	signal addrjpeg_r : unsigned(13 downto 0) := (others => '0');
	signal dataToRam_r : unsigned(15 downto 0) := (others => '0');

   -- Clock period definitions
   constant clk_s_period : time := 10 ns;
 
BEGIN
 
	-- Instantiate the Unit Under Test (UUT)
   uut: FsmUpdate_p PORT MAP (
          clk_s => clk_s,
          addr_r => addr_r,
          addr_x => addr_x,
			 sam_addr_r => sam_addr_r,
          sam_addr_x => sam_addr_x,
			 updated_r => updated_r,
          updated_x => updated_x,
			 sigDelayed_r => sigDelayed_r,
          sigDelayed_x => sigDelayed_x,
			 addrjpeg_r => addrjpeg_r,
          addrjpeg_x => addrjpeg_x,
			 dataToRam_r => dataToRam_r,
          dataToRam_x => dataToRam_x
        );

   -- Clock process definitions
   clk_s_process :process
   begin
		clk_s <= '0';
		wait for clk_s_period/2;
		clk_s <= '1';
		wait for clk_s_period/2;
   end process;
 

   -- Stimulus process
   stim_proc: process
   begin		
      -- hold reset state for 100 ns.
      wait for 100 ns;	

      wait for clk_s_period*10;

      -- insert stimulus here 
      addr_x <= b"00000000000001";
		wait for 20 ns;
		addr_x <= b"01000000000001";
      wait;
   end process;

END;
