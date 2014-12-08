--------------------------------------------------------------------------------
-- Company: 
-- Engineer:
--
-- Create Date:   18:10:27 12/06/2014
-- Design Name:   
-- Module Name:   C:/Xilinx/14.7/ISE_DS/jpeg_top_simul/instRamCtrl_tb.vhd
-- Project Name:  jpeg_top_simul
-- Target Device:  
-- Tool versions:  
-- Description:   
-- 
-- VHDL Test Bench Created by ISE for module: instRamCtrl
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

use work.pck_simul.all; 
-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--USE ieee.numeric_std.ALL;
 
ENTITY instRamCtrl_tb IS
END instRamCtrl_tb;
 
ARCHITECTURE behavior OF instRamCtrl_tb IS 
 
    -- Component Declaration for the Unit Under Test (UUT)
 
    COMPONENT instRamCtrl
    PORT(
         clk_fast : IN  std_logic
        );
    END COMPONENT;
    

   --Inputs
   signal clk_fast : std_logic := '0';

   -- Clock period definitions
   constant clk_fast_period : time := 10 ns;
        signal addr_r, addr_r1, addr_r2 : unsigned(23 downto 0):= (others => '0');
        signal addr_x:  unsigned(23 downto 0):= (others => '0');
        signal state_r:  t_enum_t_State_1 := INIT;
        signal state_x:  t_enum_t_State_1 := INIT;
		  signal dataToRam_r, dataToRam_x:  unsigned(15 downto 0):= (others => '0');
		  signal dataFromRam_r, dataFromRam_x, dataFromRam_s:  unsigned(15 downto 0):= (others => '0');
		  signal dataFromRam_r1, dataFromRam_r2:  unsigned(15 downto 0):= (others => '0');		  
		  signal sum_r, sum_x:  unsigned(15 downto 0):= (others => '0');
        signal done_s:  std_logic:= '0';
		  signal muxsel:  std_logic:= '0';
        signal wr_s: std_logic:= '0';
        signal rd_s:  std_logic:= '0';
component simul 
    port (
        clk_fast: in std_logic;
        addr_r: out unsigned(23 downto 0);
        addr_r1: inout unsigned(23 downto 0);
        addr_x: inout unsigned(23 downto 0);
        state_r: inout t_enum_t_State_1;
        state_x: inout t_enum_t_State_1;
        addr_r2: in unsigned(23 downto 0);
        muxsel: in std_logic;
        dataToRam_r: inout unsigned(15 downto 0);
        dataToRam_x: inout unsigned(15 downto 0);
        dataFromRam_r: inout unsigned(15 downto 0);
		  dataFromRam_r1: inout unsigned(15 downto 0);
        dataFromRam_r2: in unsigned(15 downto 0);			  
        dataFromRam_x: inout unsigned(15 downto 0);
		  datafromRam_s: in unsigned(15 downto 0);
        done_s: in std_logic;
        wr_s: out std_logic;
        rd_s: out std_logic;
        sum_r: inout unsigned(15 downto 0);
        sum_x: inout unsigned(15 downto 0)
    );
end component; 
BEGIN
simul_u0 : simul
port map (
         clk_fast => clk_fast,
			addr_r => addr_r,
			addr_r1 => addr_r1,
			addr_x => addr_x,
			state_r => state_r,
			state_x => state_x,
			addr_r2 => addr_r2,
			muxsel => muxsel,
			dataToRam_r => dataToRam_r,
			dataToRam_x => dataToRam_x,
			dataFromRam_r => dataFromRam_r,
			dataFromRam_r1 => dataFromRam_r1,
			dataFromRam_r2 => dataFromRam_r2,
			dataFromRam_x => dataFromRam_x,
			dataFromRam_s => dataFromRam_s,
			done_s => done_s,
			wr_s => wr_s,
			rd_s => rd_s,
			sum_r => sum_r,
			sum_x => sum_x
			);
 		 
	-- Instantiate the Unit Under Test (UUT)
   uut: instRamCtrl PORT MAP (
          clk_fast => clk_fast
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
      dataFromRam_s <= X"009c";
--		wait for 100 ns;
		done_s <= '1';
      wait;
   end process;

END;
