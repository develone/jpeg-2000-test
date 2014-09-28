----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date:    13:15:24 09/28/2014 
-- Design Name: 
-- Module Name:    std_sig - Behavioral 
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
library IEEE,XESS;
use IEEE.STD_LOGIC_1164.ALL;
use XESS.DelayPckg.DelayLine;

-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx primitives in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity std_sig is
    Port ( clk_i : in STD_LOGIC;
			  a_i : in  STD_LOGIC;
           aDelayed_o : out  STD_LOGIC);
end std_sig;

architecture Behavioral of std_sig is

begin
DelayLine_u0 : DelayLine
	generic map (NUM_DELAY_CYCLES_G => 5)
		port map (
				clk_i => clk_i,
				a_i => a_i,
				aDelayed_o => aDelayed_o
				);
end Behavioral;

