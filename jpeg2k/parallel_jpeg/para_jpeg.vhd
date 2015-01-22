----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date:    14:07:35 01/21/2015 
-- Design Name: 
-- Module Name:    para_jpeg - Behavioral 
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
use IEEE.NUMERIC_STD.all;
use work.pck_myhdl_09.all;
-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx primitives in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity para_jpeg is
  port (Clk_i : in    std_logic);
  end  entity para_jpeg;

architecture Behavioral of para_jpeg is 
  signal sig_in : unsigned(27 downto 0) := (others => '0');
  signal noupdate_s : std_logic;
  signal rdy : std_logic;
  signal addr_not_reached : std_logic;
  signal res_s : signed(7 downto 0) := (others => '0');
  signal res_u : unsigned(7 downto 0) := (others => '0');
  signal jp_lf : unsigned(7 downto 0) := (others => '0');
  signal jp_sa: unsigned(7 downto 0) := (others => '0');
  signal jp_rh : unsigned(7 downto 0) := (others => '0');
  signal jp_flgs : unsigned(3 downto 0) := (others => '0');
 

  component xess_jpeg_para is
    port (
        clk_fast: in std_logic;
        sig_in: inout unsigned(27 downto 0);
        noupdate_s: out std_logic;
        res_s: inout signed (7 downto 0);
        res_u: out unsigned(7 downto 0);
        jp_lf: in unsigned(7 downto 0);
        jp_sa: in unsigned(7 downto 0);
        jp_rh: in unsigned(7 downto 0);
        jp_flgs: in unsigned(3 downto 0);
        rdy: in std_logic;
        addr_not_reached: in std_logic
    );
end component xess_jpeg_para;

begin
xess_jpeg_para_u0 : xess_jpeg_para
  port map(
   clk_fast => Clk_i,
   sig_in => sig_in,
   noupdate_s => noupdate_s,
   res_s => res_s,
   jp_lf => jp_lf,
   jp_sa => jp_sa,
   jp_rh => jp_rh,
	jp_flgs => jp_flgs,
   rdy => rdy,
   addr_not_reached => addr_not_reached
);

end Behavioral;

