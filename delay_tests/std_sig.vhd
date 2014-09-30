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
use XESS.DelayPckg.all;

-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx primitives in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity std_sig is
    Port ( clk_i : in STD_LOGIC;
			  sigDel_s : in STD_LOGIC;
			  sigDelayed_s : out STD_LOGIC;
			  left_sv : in  STD_LOGIC_VECTOR :=(15 downto 0 => '0');
           leftDelDut_s : out  STD_LOGIC_VECTOR :=(15 downto 0 => '0'));
end std_sig;

architecture Behavioral of std_sig is

begin
DelayBus_u0 : DelayBus
	generic map (NUM_DELAY_CYCLES_G => 2)
		port map (
				clk_i => clk_i,
				bus_i => left_sv,
				busDelayed_o => leftDelDut_s
				);
DelayLine_u1 : DelayLine
	generic map (NUM_DELAY_CYCLES_G => 2)
		port map (
				clk_i => clk_i,
				a_i => sigDel_s,
				aDelayed_o => sigDelayed_s
				);
--ujpeg: jpeg 
--	port map( 
--        clk_fast => clk_i,
--        left_s => signed(left_s),
--        right_s => signed(right_s),
--        sam_s => signed(sam_s),
--        res_s => signed_res_s,
--        even_odd_s => even_odd_s,
--		  fwd_inv_s => fwd_inv_s,
--        updated_s => updated_s,
--        noupdate_s => noupdate_s		  
--		  );				
end Behavioral;

