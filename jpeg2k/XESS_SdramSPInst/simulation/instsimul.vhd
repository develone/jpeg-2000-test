----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date:    17:53:23 12/06/2014 
-- Design Name: 
-- Module Name:    instsimul - Behavioral 
-- Project Name: 
-- Target Devices: 
-- Tool versions: 
-- Description: 
--
-- Dependencies: 
--
-- Revision: 
-- Revision 0.01 - File Created
-- Additional Comments: 
--
----------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.numeric_std.all;
use std.textio.all;
use work.pck_myhdl_09.all;

use work.pck_simul.all;
-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx primitives in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity instsimul is
    Port ( clk_fast : in  STD_LOGIC);
end instsimul;

architecture Behavioral of instsimul is
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
			

end Behavioral;

