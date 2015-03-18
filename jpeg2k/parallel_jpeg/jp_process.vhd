-- File: jp_process.vhd
-- Generated by MyHDL 0.9dev
-- Date: Wed Mar 18 10:19:47 2015


library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
use std.textio.all;

use work.pck_myhdl_09.all;

entity jp_process is
    port (
        res_out_x: out signed (9 downto 0);
        left_s_i: in unsigned(143 downto 0);
        sam_s_i: in unsigned(143 downto 0);
        right_s_i: in unsigned(143 downto 0);
        flgs_s_i: in unsigned(79 downto 0);
        noupdate_s: out std_logic;
        update_s: in std_logic
    );
end entity jp_process;


architecture MyHDL of jp_process is


constant LVL0: integer := 2**4;
constant YES: integer := 1;
constant NO: integer := 0;



type t_array_right_s is array(0 to 16-1) of unsigned(8 downto 0);
signal right_s: t_array_right_s;
type t_array_flgs_s is array(0 to 16-1) of unsigned(4 downto 0);
signal flgs_s: t_array_flgs_s;
type t_array_sam_s is array(0 to 16-1) of unsigned(8 downto 0);
signal sam_s: t_array_sam_s;
type t_array_left_s is array(0 to 16-1) of unsigned(8 downto 0);
signal left_s: t_array_left_s;

begin


right_s(0) <= right_s_i(9-1 downto 0);
right_s(1) <= right_s_i(18-1 downto 9);
right_s(2) <= right_s_i(27-1 downto 18);
right_s(3) <= right_s_i(36-1 downto 27);
right_s(4) <= right_s_i(45-1 downto 36);
right_s(5) <= right_s_i(54-1 downto 45);
right_s(6) <= right_s_i(63-1 downto 54);
right_s(7) <= right_s_i(72-1 downto 63);
right_s(8) <= right_s_i(81-1 downto 72);
right_s(9) <= right_s_i(90-1 downto 81);
right_s(10) <= right_s_i(99-1 downto 90);
right_s(11) <= right_s_i(108-1 downto 99);
right_s(12) <= right_s_i(117-1 downto 108);
right_s(13) <= right_s_i(126-1 downto 117);
right_s(14) <= right_s_i(135-1 downto 126);
right_s(15) <= right_s_i(144-1 downto 135);
flgs_s(0) <= flgs_s_i(5-1 downto 0);
flgs_s(1) <= flgs_s_i(10-1 downto 5);
flgs_s(2) <= flgs_s_i(15-1 downto 10);
flgs_s(3) <= flgs_s_i(20-1 downto 15);
flgs_s(4) <= flgs_s_i(25-1 downto 20);
flgs_s(5) <= flgs_s_i(30-1 downto 25);
flgs_s(6) <= flgs_s_i(35-1 downto 30);
flgs_s(7) <= flgs_s_i(40-1 downto 35);
flgs_s(8) <= flgs_s_i(45-1 downto 40);
flgs_s(9) <= flgs_s_i(50-1 downto 45);
flgs_s(10) <= flgs_s_i(55-1 downto 50);
flgs_s(11) <= flgs_s_i(60-1 downto 55);
flgs_s(12) <= flgs_s_i(65-1 downto 60);
flgs_s(13) <= flgs_s_i(70-1 downto 65);
flgs_s(14) <= flgs_s_i(75-1 downto 70);
flgs_s(15) <= flgs_s_i(80-1 downto 75);
sam_s(0) <= sam_s_i(9-1 downto 0);
sam_s(1) <= sam_s_i(18-1 downto 9);
sam_s(2) <= sam_s_i(27-1 downto 18);
sam_s(3) <= sam_s_i(36-1 downto 27);
sam_s(4) <= sam_s_i(45-1 downto 36);
sam_s(5) <= sam_s_i(54-1 downto 45);
sam_s(6) <= sam_s_i(63-1 downto 54);
sam_s(7) <= sam_s_i(72-1 downto 63);
sam_s(8) <= sam_s_i(81-1 downto 72);
sam_s(9) <= sam_s_i(90-1 downto 81);
sam_s(10) <= sam_s_i(99-1 downto 90);
sam_s(11) <= sam_s_i(108-1 downto 99);
sam_s(12) <= sam_s_i(117-1 downto 108);
sam_s(13) <= sam_s_i(126-1 downto 117);
sam_s(14) <= sam_s_i(135-1 downto 126);
sam_s(15) <= sam_s_i(144-1 downto 135);
left_s(0) <= left_s_i(9-1 downto 0);
left_s(1) <= left_s_i(18-1 downto 9);
left_s(2) <= left_s_i(27-1 downto 18);
left_s(3) <= left_s_i(36-1 downto 27);
left_s(4) <= left_s_i(45-1 downto 36);
left_s(5) <= left_s_i(54-1 downto 45);
left_s(6) <= left_s_i(63-1 downto 54);
left_s(7) <= left_s_i(72-1 downto 63);
left_s(8) <= left_s_i(81-1 downto 72);
left_s(9) <= left_s_i(90-1 downto 81);
left_s(10) <= left_s_i(99-1 downto 90);
left_s(11) <= left_s_i(108-1 downto 99);
left_s(12) <= left_s_i(117-1 downto 108);
left_s(13) <= left_s_i(126-1 downto 117);
left_s(14) <= left_s_i(135-1 downto 126);
left_s(15) <= left_s_i(144-1 downto 135);

-- update_s needs to be 1
-- for the res_out_x to be valid
-- noupdate_s goes lo when a
-- res_out_x valid
-- fwd dwt even flgs_s eq 7
-- inv dwt even flgs_s eq 5
-- fwd dwt odd flgs_s eq 6
-- inv dwt odd flgs_s eq 4
JP_PROCESS_JPEG_LOGIC: process (update_s, right_s, flgs_s, sam_s, left_s) is
begin
    if bool(update_s) then
        noupdate_s <= '0';
        for i in 0 to LVL0-1 loop
            if (flgs_s(i) = 7) then
                res_out_x <= (resize(signed(sam_s(i)), 10) - (shift_right(resize(signed(left_s(i)), 10), 1) + shift_right(resize(signed(right_s(i)), 10), 1)));
            elsif (flgs_s(i) = 5) then
                res_out_x <= (resize(signed(sam_s(i)), 10) + (shift_right(resize(signed(left_s(i)), 10), 1) + shift_right(resize(signed(right_s(i)), 10), 1)));
            elsif (flgs_s(i) = 6) then
                res_out_x <= (resize(signed(sam_s(i)), 10) + shift_right(((resize(signed(left_s(i)), 10) + resize(signed(right_s(i)), 10)) + 2), 2));
            elsif (flgs_s(i) = 4) then
                res_out_x <= (resize(signed(sam_s(i)), 10) - shift_right(((resize(signed(left_s(i)), 10) + resize(signed(right_s(i)), 10)) + 2), 2));
            end if;
        end loop;
    else
        noupdate_s <= '1';
    end if;
end process JP_PROCESS_JPEG_LOGIC;

end architecture MyHDL;
