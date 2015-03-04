-- File: combine.vhd
-- Generated by MyHDL 0.9dev
-- Date: Mon Mar  2 08:40:55 2015


library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
use std.textio.all;

use work.pck_myhdl_09.all;

entity combine is
    port (
        left_com_x: out unsigned(159 downto 0);
        sam_com_x: out unsigned(159 downto 0);
        right_com_x: out unsigned(159 downto 0);
        lft_s_i: in unsigned(159 downto 0);
        sa_s_i: in unsigned(159 downto 0);
        rht_s_i: in unsigned(159 downto 0);
        combine_rdy_s: in std_logic;
        nocombine_s: out std_logic
    );
end entity combine;


architecture MyHDL of combine is





type t_array_rht_s is array(0 to 16-1) of unsigned(9 downto 0);
signal rht_s: t_array_rht_s;
type t_array_sa_s is array(0 to 16-1) of unsigned(9 downto 0);
signal sa_s: t_array_sa_s;
type t_array_lft_s is array(0 to 16-1) of unsigned(9 downto 0);
signal lft_s: t_array_lft_s;

begin


rht_s(0) <= rht_s_i(10-1 downto 0);
rht_s(1) <= rht_s_i(20-1 downto 10);
rht_s(2) <= rht_s_i(30-1 downto 20);
rht_s(3) <= rht_s_i(40-1 downto 30);
rht_s(4) <= rht_s_i(50-1 downto 40);
rht_s(5) <= rht_s_i(60-1 downto 50);
rht_s(6) <= rht_s_i(70-1 downto 60);
rht_s(7) <= rht_s_i(80-1 downto 70);
rht_s(8) <= rht_s_i(90-1 downto 80);
rht_s(9) <= rht_s_i(100-1 downto 90);
rht_s(10) <= rht_s_i(110-1 downto 100);
rht_s(11) <= rht_s_i(120-1 downto 110);
rht_s(12) <= rht_s_i(130-1 downto 120);
rht_s(13) <= rht_s_i(140-1 downto 130);
rht_s(14) <= rht_s_i(150-1 downto 140);
rht_s(15) <= rht_s_i(160-1 downto 150);
sa_s(0) <= sa_s_i(10-1 downto 0);
sa_s(1) <= sa_s_i(20-1 downto 10);
sa_s(2) <= sa_s_i(30-1 downto 20);
sa_s(3) <= sa_s_i(40-1 downto 30);
sa_s(4) <= sa_s_i(50-1 downto 40);
sa_s(5) <= sa_s_i(60-1 downto 50);
sa_s(6) <= sa_s_i(70-1 downto 60);
sa_s(7) <= sa_s_i(80-1 downto 70);
sa_s(8) <= sa_s_i(90-1 downto 80);
sa_s(9) <= sa_s_i(100-1 downto 90);
sa_s(10) <= sa_s_i(110-1 downto 100);
sa_s(11) <= sa_s_i(120-1 downto 110);
sa_s(12) <= sa_s_i(130-1 downto 120);
sa_s(13) <= sa_s_i(140-1 downto 130);
sa_s(14) <= sa_s_i(150-1 downto 140);
sa_s(15) <= sa_s_i(160-1 downto 150);
lft_s(0) <= lft_s_i(10-1 downto 0);
lft_s(1) <= lft_s_i(20-1 downto 10);
lft_s(2) <= lft_s_i(30-1 downto 20);
lft_s(3) <= lft_s_i(40-1 downto 30);
lft_s(4) <= lft_s_i(50-1 downto 40);
lft_s(5) <= lft_s_i(60-1 downto 50);
lft_s(6) <= lft_s_i(70-1 downto 60);
lft_s(7) <= lft_s_i(80-1 downto 70);
lft_s(8) <= lft_s_i(90-1 downto 80);
lft_s(9) <= lft_s_i(100-1 downto 90);
lft_s(10) <= lft_s_i(110-1 downto 100);
lft_s(11) <= lft_s_i(120-1 downto 110);
lft_s(12) <= lft_s_i(130-1 downto 120);
lft_s(13) <= lft_s_i(140-1 downto 130);
lft_s(14) <= lft_s_i(150-1 downto 140);
lft_s(15) <= lft_s_i(160-1 downto 150);


COMBINE_COMBINE_LOGIC: process (rht_s, sa_s, lft_s, combine_rdy_s) is
begin
    if (combine_rdy_s = '1') then
        left_com_x <= unsigned'(lft_s(15) & lft_s(14) & lft_s(13) & lft_s(12) & lft_s(11) & lft_s(10) & lft_s(9) & lft_s(8) & lft_s(7) & lft_s(6) & lft_s(5) & lft_s(4) & lft_s(3) & lft_s(2) & lft_s(1) & lft_s(0));
        sam_com_x <= unsigned'(sa_s(15) & sa_s(14) & sa_s(13) & sa_s(12) & sa_s(11) & sa_s(10) & sa_s(9) & sa_s(8) & sa_s(7) & sa_s(6) & sa_s(5) & sa_s(4) & sa_s(3) & sa_s(2) & sa_s(1) & sa_s(0));
        right_com_x <= unsigned'(rht_s(15) & rht_s(14) & rht_s(13) & rht_s(12) & rht_s(11) & rht_s(10) & rht_s(9) & rht_s(8) & rht_s(7) & rht_s(6) & rht_s(5) & rht_s(4) & rht_s(3) & rht_s(2) & rht_s(1) & rht_s(0));
        nocombine_s <= '0';
    else
        left_com_x <= to_unsigned(0, 160);
        sam_com_x <= to_unsigned(0, 160);
        right_com_x <= to_unsigned(0, 160);
        nocombine_s <= '1';
    end if;
end process COMBINE_COMBINE_LOGIC;

end architecture MyHDL;