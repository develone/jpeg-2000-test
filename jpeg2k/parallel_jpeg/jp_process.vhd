-- File: jp_process.vhd
-- Generated by MyHDL 0.9dev
-- Date: Mon Feb  9 07:45:50 2015


library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
use std.textio.all;

use work.pck_myhdl_09.all;

entity jp_process is
    port (
        res_out_x: out signed (7 downto 0);
        left_s_i: in unsigned(511 downto 0);
        sam_s_i: in unsigned(511 downto 0);
        right_s_i: in unsigned(511 downto 0);
        flgs_s_i: in unsigned(319 downto 0);
        noupdate_s: out std_logic;
        update_s: in std_logic
    );
end entity jp_process;


architecture MyHDL of jp_process is


constant LVL0: integer := 2**6;
constant YES: integer := 1;
constant NO: integer := 0;



type t_array_right_s is array(0 to 64-1) of unsigned(7 downto 0);
signal right_s: t_array_right_s;
type t_array_flgs_s is array(0 to 64-1) of unsigned(4 downto 0);
signal flgs_s: t_array_flgs_s;
type t_array_sam_s is array(0 to 64-1) of unsigned(7 downto 0);
signal sam_s: t_array_sam_s;
type t_array_left_s is array(0 to 64-1) of unsigned(7 downto 0);
signal left_s: t_array_left_s;

begin


right_s(0) <= right_s_i(8-1 downto 0);
right_s(1) <= right_s_i(16-1 downto 8);
right_s(2) <= right_s_i(24-1 downto 16);
right_s(3) <= right_s_i(32-1 downto 24);
right_s(4) <= right_s_i(40-1 downto 32);
right_s(5) <= right_s_i(48-1 downto 40);
right_s(6) <= right_s_i(56-1 downto 48);
right_s(7) <= right_s_i(64-1 downto 56);
right_s(8) <= right_s_i(72-1 downto 64);
right_s(9) <= right_s_i(80-1 downto 72);
right_s(10) <= right_s_i(88-1 downto 80);
right_s(11) <= right_s_i(96-1 downto 88);
right_s(12) <= right_s_i(104-1 downto 96);
right_s(13) <= right_s_i(112-1 downto 104);
right_s(14) <= right_s_i(120-1 downto 112);
right_s(15) <= right_s_i(128-1 downto 120);
right_s(16) <= right_s_i(136-1 downto 128);
right_s(17) <= right_s_i(144-1 downto 136);
right_s(18) <= right_s_i(152-1 downto 144);
right_s(19) <= right_s_i(160-1 downto 152);
right_s(20) <= right_s_i(168-1 downto 160);
right_s(21) <= right_s_i(176-1 downto 168);
right_s(22) <= right_s_i(184-1 downto 176);
right_s(23) <= right_s_i(192-1 downto 184);
right_s(24) <= right_s_i(200-1 downto 192);
right_s(25) <= right_s_i(208-1 downto 200);
right_s(26) <= right_s_i(216-1 downto 208);
right_s(27) <= right_s_i(224-1 downto 216);
right_s(28) <= right_s_i(232-1 downto 224);
right_s(29) <= right_s_i(240-1 downto 232);
right_s(30) <= right_s_i(248-1 downto 240);
right_s(31) <= right_s_i(256-1 downto 248);
right_s(32) <= right_s_i(264-1 downto 256);
right_s(33) <= right_s_i(272-1 downto 264);
right_s(34) <= right_s_i(280-1 downto 272);
right_s(35) <= right_s_i(288-1 downto 280);
right_s(36) <= right_s_i(296-1 downto 288);
right_s(37) <= right_s_i(304-1 downto 296);
right_s(38) <= right_s_i(312-1 downto 304);
right_s(39) <= right_s_i(320-1 downto 312);
right_s(40) <= right_s_i(328-1 downto 320);
right_s(41) <= right_s_i(336-1 downto 328);
right_s(42) <= right_s_i(344-1 downto 336);
right_s(43) <= right_s_i(352-1 downto 344);
right_s(44) <= right_s_i(360-1 downto 352);
right_s(45) <= right_s_i(368-1 downto 360);
right_s(46) <= right_s_i(376-1 downto 368);
right_s(47) <= right_s_i(384-1 downto 376);
right_s(48) <= right_s_i(392-1 downto 384);
right_s(49) <= right_s_i(400-1 downto 392);
right_s(50) <= right_s_i(408-1 downto 400);
right_s(51) <= right_s_i(416-1 downto 408);
right_s(52) <= right_s_i(424-1 downto 416);
right_s(53) <= right_s_i(432-1 downto 424);
right_s(54) <= right_s_i(440-1 downto 432);
right_s(55) <= right_s_i(448-1 downto 440);
right_s(56) <= right_s_i(456-1 downto 448);
right_s(57) <= right_s_i(464-1 downto 456);
right_s(58) <= right_s_i(472-1 downto 464);
right_s(59) <= right_s_i(480-1 downto 472);
right_s(60) <= right_s_i(488-1 downto 480);
right_s(61) <= right_s_i(496-1 downto 488);
right_s(62) <= right_s_i(504-1 downto 496);
right_s(63) <= right_s_i(512-1 downto 504);
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
flgs_s(16) <= flgs_s_i(85-1 downto 80);
flgs_s(17) <= flgs_s_i(90-1 downto 85);
flgs_s(18) <= flgs_s_i(95-1 downto 90);
flgs_s(19) <= flgs_s_i(100-1 downto 95);
flgs_s(20) <= flgs_s_i(105-1 downto 100);
flgs_s(21) <= flgs_s_i(110-1 downto 105);
flgs_s(22) <= flgs_s_i(115-1 downto 110);
flgs_s(23) <= flgs_s_i(120-1 downto 115);
flgs_s(24) <= flgs_s_i(125-1 downto 120);
flgs_s(25) <= flgs_s_i(130-1 downto 125);
flgs_s(26) <= flgs_s_i(135-1 downto 130);
flgs_s(27) <= flgs_s_i(140-1 downto 135);
flgs_s(28) <= flgs_s_i(145-1 downto 140);
flgs_s(29) <= flgs_s_i(150-1 downto 145);
flgs_s(30) <= flgs_s_i(155-1 downto 150);
flgs_s(31) <= flgs_s_i(160-1 downto 155);
flgs_s(32) <= flgs_s_i(165-1 downto 160);
flgs_s(33) <= flgs_s_i(170-1 downto 165);
flgs_s(34) <= flgs_s_i(175-1 downto 170);
flgs_s(35) <= flgs_s_i(180-1 downto 175);
flgs_s(36) <= flgs_s_i(185-1 downto 180);
flgs_s(37) <= flgs_s_i(190-1 downto 185);
flgs_s(38) <= flgs_s_i(195-1 downto 190);
flgs_s(39) <= flgs_s_i(200-1 downto 195);
flgs_s(40) <= flgs_s_i(205-1 downto 200);
flgs_s(41) <= flgs_s_i(210-1 downto 205);
flgs_s(42) <= flgs_s_i(215-1 downto 210);
flgs_s(43) <= flgs_s_i(220-1 downto 215);
flgs_s(44) <= flgs_s_i(225-1 downto 220);
flgs_s(45) <= flgs_s_i(230-1 downto 225);
flgs_s(46) <= flgs_s_i(235-1 downto 230);
flgs_s(47) <= flgs_s_i(240-1 downto 235);
flgs_s(48) <= flgs_s_i(245-1 downto 240);
flgs_s(49) <= flgs_s_i(250-1 downto 245);
flgs_s(50) <= flgs_s_i(255-1 downto 250);
flgs_s(51) <= flgs_s_i(260-1 downto 255);
flgs_s(52) <= flgs_s_i(265-1 downto 260);
flgs_s(53) <= flgs_s_i(270-1 downto 265);
flgs_s(54) <= flgs_s_i(275-1 downto 270);
flgs_s(55) <= flgs_s_i(280-1 downto 275);
flgs_s(56) <= flgs_s_i(285-1 downto 280);
flgs_s(57) <= flgs_s_i(290-1 downto 285);
flgs_s(58) <= flgs_s_i(295-1 downto 290);
flgs_s(59) <= flgs_s_i(300-1 downto 295);
flgs_s(60) <= flgs_s_i(305-1 downto 300);
flgs_s(61) <= flgs_s_i(310-1 downto 305);
flgs_s(62) <= flgs_s_i(315-1 downto 310);
flgs_s(63) <= flgs_s_i(320-1 downto 315);
sam_s(0) <= sam_s_i(8-1 downto 0);
sam_s(1) <= sam_s_i(16-1 downto 8);
sam_s(2) <= sam_s_i(24-1 downto 16);
sam_s(3) <= sam_s_i(32-1 downto 24);
sam_s(4) <= sam_s_i(40-1 downto 32);
sam_s(5) <= sam_s_i(48-1 downto 40);
sam_s(6) <= sam_s_i(56-1 downto 48);
sam_s(7) <= sam_s_i(64-1 downto 56);
sam_s(8) <= sam_s_i(72-1 downto 64);
sam_s(9) <= sam_s_i(80-1 downto 72);
sam_s(10) <= sam_s_i(88-1 downto 80);
sam_s(11) <= sam_s_i(96-1 downto 88);
sam_s(12) <= sam_s_i(104-1 downto 96);
sam_s(13) <= sam_s_i(112-1 downto 104);
sam_s(14) <= sam_s_i(120-1 downto 112);
sam_s(15) <= sam_s_i(128-1 downto 120);
sam_s(16) <= sam_s_i(136-1 downto 128);
sam_s(17) <= sam_s_i(144-1 downto 136);
sam_s(18) <= sam_s_i(152-1 downto 144);
sam_s(19) <= sam_s_i(160-1 downto 152);
sam_s(20) <= sam_s_i(168-1 downto 160);
sam_s(21) <= sam_s_i(176-1 downto 168);
sam_s(22) <= sam_s_i(184-1 downto 176);
sam_s(23) <= sam_s_i(192-1 downto 184);
sam_s(24) <= sam_s_i(200-1 downto 192);
sam_s(25) <= sam_s_i(208-1 downto 200);
sam_s(26) <= sam_s_i(216-1 downto 208);
sam_s(27) <= sam_s_i(224-1 downto 216);
sam_s(28) <= sam_s_i(232-1 downto 224);
sam_s(29) <= sam_s_i(240-1 downto 232);
sam_s(30) <= sam_s_i(248-1 downto 240);
sam_s(31) <= sam_s_i(256-1 downto 248);
sam_s(32) <= sam_s_i(264-1 downto 256);
sam_s(33) <= sam_s_i(272-1 downto 264);
sam_s(34) <= sam_s_i(280-1 downto 272);
sam_s(35) <= sam_s_i(288-1 downto 280);
sam_s(36) <= sam_s_i(296-1 downto 288);
sam_s(37) <= sam_s_i(304-1 downto 296);
sam_s(38) <= sam_s_i(312-1 downto 304);
sam_s(39) <= sam_s_i(320-1 downto 312);
sam_s(40) <= sam_s_i(328-1 downto 320);
sam_s(41) <= sam_s_i(336-1 downto 328);
sam_s(42) <= sam_s_i(344-1 downto 336);
sam_s(43) <= sam_s_i(352-1 downto 344);
sam_s(44) <= sam_s_i(360-1 downto 352);
sam_s(45) <= sam_s_i(368-1 downto 360);
sam_s(46) <= sam_s_i(376-1 downto 368);
sam_s(47) <= sam_s_i(384-1 downto 376);
sam_s(48) <= sam_s_i(392-1 downto 384);
sam_s(49) <= sam_s_i(400-1 downto 392);
sam_s(50) <= sam_s_i(408-1 downto 400);
sam_s(51) <= sam_s_i(416-1 downto 408);
sam_s(52) <= sam_s_i(424-1 downto 416);
sam_s(53) <= sam_s_i(432-1 downto 424);
sam_s(54) <= sam_s_i(440-1 downto 432);
sam_s(55) <= sam_s_i(448-1 downto 440);
sam_s(56) <= sam_s_i(456-1 downto 448);
sam_s(57) <= sam_s_i(464-1 downto 456);
sam_s(58) <= sam_s_i(472-1 downto 464);
sam_s(59) <= sam_s_i(480-1 downto 472);
sam_s(60) <= sam_s_i(488-1 downto 480);
sam_s(61) <= sam_s_i(496-1 downto 488);
sam_s(62) <= sam_s_i(504-1 downto 496);
sam_s(63) <= sam_s_i(512-1 downto 504);
left_s(0) <= left_s_i(8-1 downto 0);
left_s(1) <= left_s_i(16-1 downto 8);
left_s(2) <= left_s_i(24-1 downto 16);
left_s(3) <= left_s_i(32-1 downto 24);
left_s(4) <= left_s_i(40-1 downto 32);
left_s(5) <= left_s_i(48-1 downto 40);
left_s(6) <= left_s_i(56-1 downto 48);
left_s(7) <= left_s_i(64-1 downto 56);
left_s(8) <= left_s_i(72-1 downto 64);
left_s(9) <= left_s_i(80-1 downto 72);
left_s(10) <= left_s_i(88-1 downto 80);
left_s(11) <= left_s_i(96-1 downto 88);
left_s(12) <= left_s_i(104-1 downto 96);
left_s(13) <= left_s_i(112-1 downto 104);
left_s(14) <= left_s_i(120-1 downto 112);
left_s(15) <= left_s_i(128-1 downto 120);
left_s(16) <= left_s_i(136-1 downto 128);
left_s(17) <= left_s_i(144-1 downto 136);
left_s(18) <= left_s_i(152-1 downto 144);
left_s(19) <= left_s_i(160-1 downto 152);
left_s(20) <= left_s_i(168-1 downto 160);
left_s(21) <= left_s_i(176-1 downto 168);
left_s(22) <= left_s_i(184-1 downto 176);
left_s(23) <= left_s_i(192-1 downto 184);
left_s(24) <= left_s_i(200-1 downto 192);
left_s(25) <= left_s_i(208-1 downto 200);
left_s(26) <= left_s_i(216-1 downto 208);
left_s(27) <= left_s_i(224-1 downto 216);
left_s(28) <= left_s_i(232-1 downto 224);
left_s(29) <= left_s_i(240-1 downto 232);
left_s(30) <= left_s_i(248-1 downto 240);
left_s(31) <= left_s_i(256-1 downto 248);
left_s(32) <= left_s_i(264-1 downto 256);
left_s(33) <= left_s_i(272-1 downto 264);
left_s(34) <= left_s_i(280-1 downto 272);
left_s(35) <= left_s_i(288-1 downto 280);
left_s(36) <= left_s_i(296-1 downto 288);
left_s(37) <= left_s_i(304-1 downto 296);
left_s(38) <= left_s_i(312-1 downto 304);
left_s(39) <= left_s_i(320-1 downto 312);
left_s(40) <= left_s_i(328-1 downto 320);
left_s(41) <= left_s_i(336-1 downto 328);
left_s(42) <= left_s_i(344-1 downto 336);
left_s(43) <= left_s_i(352-1 downto 344);
left_s(44) <= left_s_i(360-1 downto 352);
left_s(45) <= left_s_i(368-1 downto 360);
left_s(46) <= left_s_i(376-1 downto 368);
left_s(47) <= left_s_i(384-1 downto 376);
left_s(48) <= left_s_i(392-1 downto 384);
left_s(49) <= left_s_i(400-1 downto 392);
left_s(50) <= left_s_i(408-1 downto 400);
left_s(51) <= left_s_i(416-1 downto 408);
left_s(52) <= left_s_i(424-1 downto 416);
left_s(53) <= left_s_i(432-1 downto 424);
left_s(54) <= left_s_i(440-1 downto 432);
left_s(55) <= left_s_i(448-1 downto 440);
left_s(56) <= left_s_i(456-1 downto 448);
left_s(57) <= left_s_i(464-1 downto 456);
left_s(58) <= left_s_i(472-1 downto 464);
left_s(59) <= left_s_i(480-1 downto 472);
left_s(60) <= left_s_i(488-1 downto 480);
left_s(61) <= left_s_i(496-1 downto 488);
left_s(62) <= left_s_i(504-1 downto 496);
left_s(63) <= left_s_i(512-1 downto 504);

-- update_s needs to be 1
-- for the res_out_x to be valid
-- noupdate_s goes lo when a
-- res_out_x valid
-- fwd dwt even flgs_s eq 7
-- inv dwt even flgs_s eq 5
-- fwd dwt odd flgs_s eq 6
-- inv dwt odd flgs_s eq 4
JP_PROCESS_JPEG_LOGIC: process (update_s, right_s(0), right_s(1), right_s(2), right_s(3), right_s(4), right_s(5), right_s(6), right_s(7), right_s(8), right_s(9), right_s(10), right_s(11), right_s(12), right_s(13), right_s(14), right_s(15), right_s(16), right_s(17), right_s(18), right_s(19), right_s(20), right_s(21), right_s(22), right_s(23), right_s(24), right_s(25), right_s(26), right_s(27), right_s(28), right_s(29), right_s(30), right_s(31), right_s(32), right_s(33), right_s(34), right_s(35), right_s(36), right_s(37), right_s(38), right_s(39), right_s(40), right_s(41), right_s(42), right_s(43), right_s(44), right_s(45), right_s(46), right_s(47), right_s(48), right_s(49), right_s(50), right_s(51), right_s(52), right_s(53), right_s(54), right_s(55), right_s(56), right_s(57), right_s(58), right_s(59), right_s(60), right_s(61), right_s(62), right_s(63), flgs_s(0), flgs_s(1), flgs_s(2), flgs_s(3), flgs_s(4), flgs_s(5), flgs_s(6), flgs_s(7), flgs_s(8), flgs_s(9), flgs_s(10), flgs_s(11), flgs_s(12), flgs_s(13), flgs_s(14), flgs_s(15), flgs_s(16), flgs_s(17), flgs_s(18), flgs_s(19), flgs_s(20), flgs_s(21), flgs_s(22), flgs_s(23), flgs_s(24), flgs_s(25), flgs_s(26), flgs_s(27), flgs_s(28), flgs_s(29), flgs_s(30), flgs_s(31), flgs_s(32), flgs_s(33), flgs_s(34), flgs_s(35), flgs_s(36), flgs_s(37), flgs_s(38), flgs_s(39), flgs_s(40), flgs_s(41), flgs_s(42), flgs_s(43), flgs_s(44), flgs_s(45), flgs_s(46), flgs_s(47), flgs_s(48), flgs_s(49), flgs_s(50), flgs_s(51), flgs_s(52), flgs_s(53), flgs_s(54), flgs_s(55), flgs_s(56), flgs_s(57), flgs_s(58), flgs_s(59), flgs_s(60), flgs_s(61), flgs_s(62), flgs_s(63), sam_s(0), sam_s(1), sam_s(2), sam_s(3), sam_s(4), sam_s(5), sam_s(6), sam_s(7), sam_s(8), sam_s(9), sam_s(10), sam_s(11), sam_s(12), sam_s(13), sam_s(14), sam_s(15), sam_s(16), sam_s(17), sam_s(18), sam_s(19), sam_s(20), sam_s(21), sam_s(22), sam_s(23), sam_s(24), sam_s(25), sam_s(26), sam_s(27), sam_s(28), sam_s(29), sam_s(30), sam_s(31), sam_s(32), sam_s(33), sam_s(34), sam_s(35), sam_s(36), sam_s(37), sam_s(38), sam_s(39), sam_s(40), sam_s(41), sam_s(42), sam_s(43), sam_s(44), sam_s(45), sam_s(46), sam_s(47), sam_s(48), sam_s(49), sam_s(50), sam_s(51), sam_s(52), sam_s(53), sam_s(54), sam_s(55), sam_s(56), sam_s(57), sam_s(58), sam_s(59), sam_s(60), sam_s(61), sam_s(62), sam_s(63), left_s(0), left_s(1), left_s(2), left_s(3), left_s(4), left_s(5), left_s(6), left_s(7), left_s(8), left_s(9), left_s(10), left_s(11), left_s(12), left_s(13), left_s(14), left_s(15), left_s(16), left_s(17), left_s(18), left_s(19), left_s(20), left_s(21), left_s(22), left_s(23), left_s(24), left_s(25), left_s(26), left_s(27), left_s(28), left_s(29), left_s(30), left_s(31), left_s(32), left_s(33), left_s(34), left_s(35), left_s(36), left_s(37), left_s(38), left_s(39), left_s(40), left_s(41), left_s(42), left_s(43), left_s(44), left_s(45), left_s(46), left_s(47), left_s(48), left_s(49), left_s(50), left_s(51), left_s(52), left_s(53), left_s(54), left_s(55), left_s(56), left_s(57), left_s(58), left_s(59), left_s(60), left_s(61), left_s(62), left_s(63)) is
begin
    if bool(update_s) then
        noupdate_s <= '0';
        for i in 0 to LVL0-1 loop
            if (flgs_s(i) = 7) then
                res_out_x <= signed(sam_s(i) - (shift_right(left_s(i), 1) + shift_right(right_s(i), 1)));
            elsif (flgs_s(i) = 5) then
                res_out_x <= signed(sam_s(i) + (shift_right(left_s(i), 1) + shift_right(right_s(i), 1)));
            elsif (flgs_s(i) = 6) then
                res_out_x <= signed(sam_s(i) + shift_right((left_s(i) + (right_s(i) + 2)), 2));
            elsif (flgs_s(i) = 4) then
                res_out_x <= signed(sam_s(i) - shift_right((left_s(i) + (right_s(i) + 2)), 2));
            end if;
        end loop;
    else
        noupdate_s <= '1';
    end if;
end process JP_PROCESS_JPEG_LOGIC;

end architecture MyHDL;
