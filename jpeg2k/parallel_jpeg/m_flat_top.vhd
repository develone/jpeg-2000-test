-- File: m_flat_top.vhd
-- Generated by MyHDL 0.9.dev0
-- Date: Wed Apr 22 07:03:15 2015


library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
use std.textio.all;

use work.pck_myhdl_090.all;

entity m_flat_top is
    port (
        clock: in std_logic;
        reset: in std_logic;
        sdo: out std_logic
    );
end entity m_flat_top;
-- example convertible top-level 

architecture MyHDL of m_flat_top is


constant nbits: integer := 144;



signal flati: unsigned(143 downto 0);
signal flato: unsigned(143 downto 0);
signal gflt_col: unsigned(8 downto 0);
signal gflt_flats: unsigned(143 downto 0);
signal gstk_g_14_y: unsigned(8 downto 0);
signal gstk_g_13_y: unsigned(8 downto 0);
signal gstk_g_12_y: unsigned(8 downto 0);
signal gstk_g_11_y: unsigned(8 downto 0);
signal gstk_g_10_y: unsigned(8 downto 0);
signal gstk_g_9_y: unsigned(8 downto 0);
signal gstk_g_8_y: unsigned(8 downto 0);
signal gstk_g_7_y: unsigned(8 downto 0);
signal gstk_g_6_y: unsigned(8 downto 0);
signal gstk_g_5_y: unsigned(8 downto 0);
signal gstk_g_4_y: unsigned(8 downto 0);
signal gstk_g_3_y: unsigned(8 downto 0);
signal gstk_g_2_y: unsigned(8 downto 0);
signal gstk_g_1_y: unsigned(8 downto 0);
signal gstk_g_0_y: unsigned(8 downto 0);

begin


gflt_flats(144-1 downto 135) <= gstk_g_0_y(9-1 downto 0);
gflt_flats(135-1 downto 126) <= gstk_g_1_y(9-1 downto 0);
gflt_flats(126-1 downto 117) <= gstk_g_2_y(9-1 downto 0);
gflt_flats(117-1 downto 108) <= gstk_g_3_y(9-1 downto 0);
gflt_flats(108-1 downto 99) <= gstk_g_4_y(9-1 downto 0);
gflt_flats(99-1 downto 90) <= gstk_g_5_y(9-1 downto 0);
gflt_flats(90-1 downto 81) <= gstk_g_6_y(9-1 downto 0);
gflt_flats(81-1 downto 72) <= gstk_g_7_y(9-1 downto 0);
gflt_flats(72-1 downto 63) <= gstk_g_8_y(9-1 downto 0);
gflt_flats(63-1 downto 54) <= gstk_g_9_y(9-1 downto 0);
gflt_flats(54-1 downto 45) <= gstk_g_10_y(9-1 downto 0);
gflt_flats(45-1 downto 36) <= gstk_g_11_y(9-1 downto 0);
gflt_flats(36-1 downto 27) <= gstk_g_12_y(9-1 downto 0);
gflt_flats(27-1 downto 18) <= gstk_g_13_y(9-1 downto 0);
gflt_flats(18-1 downto 9) <= gstk_g_14_y(9-1 downto 0);
gflt_flats(9-1 downto 0) <= gflt_col(9-1 downto 0);


M_FLAT_TOP_RTLI: process (clock) is
begin
    if rising_edge(clock) then
        if (reset = '1') then
            flati <= to_unsigned(0, 144);
        else
            flati <= resize(unsigned'(flati((nbits - 1)-1 downto 0)), 144);
        end if;
    end if;
end process M_FLAT_TOP_RTLI;



gstk_g_0_y <= flati(9-1 downto 0);



gstk_g_1_y <= flati(18-1 downto 9);



gstk_g_2_y <= flati(27-1 downto 18);



gstk_g_3_y <= flati(36-1 downto 27);



gstk_g_4_y <= flati(45-1 downto 36);



gstk_g_5_y <= flati(54-1 downto 45);



gstk_g_6_y <= flati(63-1 downto 54);



gstk_g_7_y <= flati(72-1 downto 63);



gstk_g_8_y <= flati(81-1 downto 72);



gstk_g_9_y <= flati(90-1 downto 81);



gstk_g_10_y <= flati(99-1 downto 90);



gstk_g_11_y <= flati(108-1 downto 99);



gstk_g_12_y <= flati(117-1 downto 108);



gstk_g_13_y <= flati(126-1 downto 117);



gstk_g_14_y <= flati(135-1 downto 126);



gflt_col <= flati(144-1 downto 135);



flato <= gflt_flats;


M_FLAT_TOP_RTLO: process (clock) is
begin
    if rising_edge(clock) then
        if (reset = '1') then
            sdo <= '0';
        else
--            sdo <= unsigned'(flato((nbits - 1)-1 downto 0) & False)(0);
        end if;
    end if;
end process M_FLAT_TOP_RTLO;

end architecture MyHDL;
