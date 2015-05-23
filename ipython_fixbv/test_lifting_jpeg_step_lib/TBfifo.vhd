--------------------------------------------------------------------------------
-- Company: 
-- Engineer:
--
-- Create Date:   09:16:40 05/23/2015
-- Design Name:   
-- Module Name:   C:/Users/vidal/Documents/GitHub/jpeg-2000-test/ipython_fixbv/test_lifting_jpeg_step_lib/test_lifting_jpeg_step_lib/TBfifo.vhd
-- Project Name:  test_lifting_jpeg_step_lib
-- Target Device:  
-- Tool versions:  
-- Description:   
-- 
-- VHDL Test Bench Created by ISE for module: fifo
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
 
-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--USE ieee.numeric_std.ALL;
 
ENTITY TBfifo IS
END TBfifo;
 
ARCHITECTURE behavior OF TBfifo IS 
 
    -- Component Declaration for the Unit Under Test (UUT)
 
    COMPONENT fifo
    PORT(
         clk : IN  std_logic;
         empty_r : OUT  std_logic;
         full_r : OUT  std_logic;
         enr_r : IN  std_logic;
         enw_r : IN  std_logic;
         dataout_r : OUT  std_logic_vector(8 downto 0);
         datain_r : IN  std_logic_vector(8 downto 0)
        );
    END COMPONENT;
    

   --Inputs
   signal clk : std_logic := '0';
   signal enr_r : std_logic := '0';
   signal enw_r : std_logic := '0';
   signal datain_r : std_logic_vector(8 downto 0) := (others => '0');

 	--Outputs
   signal empty_r : std_logic;
   signal full_r : std_logic;
   signal dataout_r : std_logic_vector(8 downto 0);

   -- Clock period definitions
   constant clk_period : time := 10 ns;
 
BEGIN
 
	-- Instantiate the Unit Under Test (UUT)
   uut: fifo PORT MAP (
          clk => clk,
          empty_r => empty_r,
          full_r => full_r,
          enr_r => enr_r,
          enw_r => enw_r,
          dataout_r => dataout_r,
          datain_r => datain_r
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

		datain_r <= b"010100000";
		wait for 10 ns;
		enw_r <= '1';
		wait for 10 ns;
		datain_r <= b"010100100";
		wait for 10 ns;
		datain_r <= b"010110010";
		wait for 10 ns;
		enw_r <= '0';
		wait for 10 ns;
		enr_r <= '1';
		wait for 10 ns;
		
      wait;
   end process;

END;
