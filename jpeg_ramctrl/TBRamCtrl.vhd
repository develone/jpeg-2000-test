--------------------------------------------------------------------------------
-- Company: 
-- Engineer:
--
-- Create Date:   09:04:56 09/22/2014
-- Design Name:   
-- Module Name:   C:/Xilinx/14.7/ISE_DS/jpeg_ramctrl/TBRamCtrl.vhd
-- Project Name:  jpeg_ramctrl
-- Target Device:  
-- Tool versions:  
-- Description:   
-- 
-- VHDL Test Bench Created by ISE for module: RamCtrl
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
 
ENTITY TBRamCtrl IS
END TBRamCtrl;
 
ARCHITECTURE behavior OF TBRamCtrl IS 
 
    -- Component Declaration for the Unit Under Test (UUT)
 
    COMPONENT RamCtrl
    PORT(
         SOF : OUT  std_logic;
         state : OUT  std_logic_vector(4 downto 0);
         WR_DATAFlag : IN  std_logic;
         clk_fast : IN  std_logic;
         reset_n : IN  std_logic
        );
    END COMPONENT;
    

   --Inputs
   signal WR_DATAFlag : std_logic := '0';
   signal clk_fast : std_logic := '0';
   signal reset_n : std_logic := '0';

 	--Outputs
   signal SOF : std_logic;
   signal state : std_logic_vector(4 downto 0);

   -- Clock period definitions
   constant clk_fast_period : time := 10 ns;
 
BEGIN
 
	-- Instantiate the Unit Under Test (UUT)
   uut: RamCtrl PORT MAP (
          SOF => SOF,
          state => state,
          WR_DATAFlag => WR_DATAFlag,
          clk_fast => clk_fast,
          reset_n => reset_n
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
   reset_n <= '1';
	WR_DATAFlag <= '1';
      wait;
   end process;

END;
