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
use IEEE.STD_LOGIC_UNSIGNED.ALL;
use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx primitives in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity std_sig is
    Port ( 
			  
			  clk_i : in STD_LOGIC;
			  sigDel_s : in STD_LOGIC;
			  sigDelayed_s : out STD_LOGIC;
			  left_sv : in  STD_LOGIC_VECTOR :=(15 downto 0 => '0');
           leftDelDut_s : out  STD_LOGIC_VECTOR :=(15 downto 0 => '0');
			  even_odd_s, fwd_inv_s, updated_s  : in std_logic;
			  noupdate_s : out std_logic;
           left_s, sam_s, right_s : in signed(15 downto 0);
			  res_s : out signed(15 downto 0)
			  );
end std_sig;

architecture Behavioral of std_sig is
  --signal left_s, sam_s, right_s, res_s : signed(15 downto 0);
  --signal even_odd_s, fwd_inv_s, updated_s, noupdate_s  : std_logic;
   
component jpeg is
    port (
        clk_fast: in std_logic;
        left_s : in signed (15 downto 0);
        right_s : in signed (15 downto 0);
        sam_s : in signed (15 downto 0);
        res_s: out signed (15 downto 0);
		  even_odd_s : in std_logic ;
		  fwd_inv_s : in std_logic;
		  updated_s : in std_logic;
		  noupdate_s : out std_logic
    );
end component;
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
end Behavioral;

