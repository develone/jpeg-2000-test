-- File: combine.vhd
-- Generated by MyHDL 0.9dev
-- Date: Sun Mar 15 06:22:40 2015


library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
use std.textio.all;

use work.pck_myhdl_09.all;

entity combine is
    port (
        left_com_x: out unsigned(255 downto 0);
        sam_com_x: out unsigned(255 downto 0);
        right_com_x: out unsigned(255 downto 0);
        lft_s_i: in unsigned(255 downto 0);
        sa_s_i: in unsigned(255 downto 0);
        rht_s_i: in unsigned(255 downto 0);
        combine_rdy_s: in std_logic;
        nocombine_s: out std_logic
    );
end entity combine;


architecture MyHDL of combine is





type t_array_rht_s is array(0 to 16-1) of unsigned(15 downto 0);
signal rht_s: t_array_rht_s;
type t_array_sa_s is array(0 to 16-1) of unsigned(15 downto 0);
signal sa_s: t_array_sa_s;
type t_array_lft_s is array(0 to 16-1) of unsigned(15 downto 0);
signal lft_s: t_array_lft_s;

begin


rht_s(0) <= rht_s_i(16-1 downto 0);
rht_s(1) <= rht_s_i(32-1 downto 16);
rht_s(2) <= rht_s_i(48-1 downto 32);
rht_s(3) <= rht_s_i(64-1 downto 48);
rht_s(4) <= rht_s_i(80-1 downto 64);
rht_s(5) <= rht_s_i(96-1 downto 80);
rht_s(6) <= rht_s_i(112-1 downto 96);
rht_s(7) <= rht_s_i(128-1 downto 112);
rht_s(8) <= rht_s_i(144-1 downto 128);
rht_s(9) <= rht_s_i(160-1 downto 144);
rht_s(10) <= rht_s_i(176-1 downto 160);
rht_s(11) <= rht_s_i(192-1 downto 176);
rht_s(12) <= rht_s_i(208-1 downto 192);
rht_s(13) <= rht_s_i(224-1 downto 208);
rht_s(14) <= rht_s_i(240-1 downto 224);
rht_s(15) <= rht_s_i(256-1 downto 240);
sa_s(0) <= sa_s_i(16-1 downto 0);
sa_s(1) <= sa_s_i(32-1 downto 16);
sa_s(2) <= sa_s_i(48-1 downto 32);
sa_s(3) <= sa_s_i(64-1 downto 48);
sa_s(4) <= sa_s_i(80-1 downto 64);
sa_s(5) <= sa_s_i(96-1 downto 80);
sa_s(6) <= sa_s_i(112-1 downto 96);
sa_s(7) <= sa_s_i(128-1 downto 112);
sa_s(8) <= sa_s_i(144-1 downto 128);
sa_s(9) <= sa_s_i(160-1 downto 144);
sa_s(10) <= sa_s_i(176-1 downto 160);
sa_s(11) <= sa_s_i(192-1 downto 176);
sa_s(12) <= sa_s_i(208-1 downto 192);
sa_s(13) <= sa_s_i(224-1 downto 208);
sa_s(14) <= sa_s_i(240-1 downto 224);
sa_s(15) <= sa_s_i(256-1 downto 240);
lft_s(0) <= lft_s_i(16-1 downto 0);
lft_s(1) <= lft_s_i(32-1 downto 16);
lft_s(2) <= lft_s_i(48-1 downto 32);
lft_s(3) <= lft_s_i(64-1 downto 48);
lft_s(4) <= lft_s_i(80-1 downto 64);
lft_s(5) <= lft_s_i(96-1 downto 80);
lft_s(6) <= lft_s_i(112-1 downto 96);
lft_s(7) <= lft_s_i(128-1 downto 112);
lft_s(8) <= lft_s_i(144-1 downto 128);
lft_s(9) <= lft_s_i(160-1 downto 144);
lft_s(10) <= lft_s_i(176-1 downto 160);
lft_s(11) <= lft_s_i(192-1 downto 176);
lft_s(12) <= lft_s_i(208-1 downto 192);
lft_s(13) <= lft_s_i(224-1 downto 208);
lft_s(14) <= lft_s_i(240-1 downto 224);
lft_s(15) <= lft_s_i(256-1 downto 240);


COMBINE_COMBINE_LOGIC: process (rht_s, sa_s, lft_s, combine_rdy_s) is
begin
    if (combine_rdy_s = '1') then
        left_com_x <= unsigned'(lft_s(15) & lft_s(14) & lft_s(13) & lft_s(12) & lft_s(11) & lft_s(10) & lft_s(9) & lft_s(8) & lft_s(7) & lft_s(6) & lft_s(5) & lft_s(4) & lft_s(3) & lft_s(2) & lft_s(1) & lft_s(0));
        sam_com_x <= unsigned'(sa_s(15) & sa_s(14) & sa_s(13) & sa_s(12) & sa_s(11) & sa_s(10) & sa_s(9) & sa_s(8) & sa_s(7) & sa_s(6) & sa_s(5) & sa_s(4) & sa_s(3) & sa_s(2) & sa_s(1) & sa_s(0));
        right_com_x <= unsigned'(rht_s(15) & rht_s(14) & rht_s(13) & rht_s(12) & rht_s(11) & rht_s(10) & rht_s(9) & rht_s(8) & rht_s(7) & rht_s(6) & rht_s(5) & rht_s(4) & rht_s(3) & rht_s(2) & rht_s(1) & rht_s(0));
        nocombine_s <= '0';
    else
        left_com_x <= to_unsigned(0, 256);
        sam_com_x <= to_unsigned(0, 256);
        right_com_x <= to_unsigned(0, 256);
        nocombine_s <= '1';
    end if;
end process COMBINE_COMBINE_LOGIC;

end architecture MyHDL;
