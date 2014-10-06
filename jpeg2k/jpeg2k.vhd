----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date:    14:20:36 10/06/2014 
-- Design Name: 
-- Module Name:    jpeg2k - Behavioral 
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
-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx primitives in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity jpeg2k is
    Port ( clk_i : in  STD_LOGIC);
end jpeg2k;

architecture Behavioral of jpeg2k is

signal dout_lf : unsigned(15 downto 0);
signal din_lf : unsigned(15 downto 0);    
signal addr_lf : unsigned(6 downto 0);
signal we_lf : std_logic;

signal dout_sam : unsigned(15 downto 0);
signal din_sam : unsigned(15 downto 0);    
signal addr_sam : unsigned(6 downto 0);
signal we_sam : std_logic;

signal dout_rht : unsigned(15 downto 0);
signal din_rht : unsigned(15 downto 0);    
signal addr_rht : unsigned(6 downto 0);
signal we_rht : std_logic;

signal dout_res : unsigned(15 downto 0);
signal din_res : unsigned(15 downto 0);    
signal addr_res : unsigned(6 downto 0);
signal we_res : std_logic;

signal left_s, sam_s, right_s, res_s :  signed(15 downto 0);
signal  even_odd_s, fwd_inv_s, clk_fast : std_logic;
signal updated_s, noupdate_s : std_logic; 
component jpeg is
    port (
        clk_fast: in std_logic;
        left_s: in signed (15 downto 0);
        right_s: in signed (15 downto 0);
        sam_s: in signed (15 downto 0);
        res_s: out signed (15 downto 0);
		  even_odd_s : in std_logic ;
		  fwd_inv_s : in std_logic;
		  updated_s : in std_logic;
		  noupdate_s : out std_logic
    );
	 end component;

COMPONENT ram
    PORT(
         dout : OUT  unsigned(15 downto 0) := (others => '0');
         din : IN  unsigned(15 downto 0) := (others => '0');
         addr : IN  unsigned(6 downto 0) := (others => '0');
         we : IN  std_logic;
         clk_fast : IN  std_logic
        );
END COMPONENT;  
	 
begin
 lfram : ram
  port map(
     dout => dout_lf,
	  din => din_lf,
	  addr => addr_lf,
	  we => we_lf,
	  clk_fast => clk_i
	  );
	  
samram : ram
  port map(
     dout => dout_sam,
	  din => din_sam,
	  addr => addr_sam,
	  we => we_sam,
	  clk_fast => clk_i
	  );
	  
rhtram : ram
  port map(
     dout => dout_rht,
	  din => din_rht,
	  addr => addr_rht,
	  we => we_rht,
	  clk_fast => clk_i
	  );

resram : ram
  port map(
     dout => dout_res,
	  din => din_res,
	  addr => addr_res,
	  we => we_res,
	  clk_fast => clk_i
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

