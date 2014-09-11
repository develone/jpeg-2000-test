-- File: jpeg.vhd
-- Generated by MyHDL 0.9dev
-- Date: Thu Sep 11 05:16:34 2014


library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
use std.textio.all;

use work.pck_myhdl_09.all;

entity jpeg is
    port (
        clk_s: in std_logic;
        left_s: in signed (15 downto 0);
        right_s: in signed (15 downto 0);
        sam_s: in signed (15 downto 0);
        res_s: out signed (15 downto 0);
        even_odd_s: in std_logic;
        fwd_inv_s: in std_logic
    );
end entity jpeg;


architecture MyHDL of jpeg is






begin




JPEG_HDL: process (clk_s) is
begin
    if rising_edge(clk_s) then
        if bool(even_odd_s) then
            if bool(fwd_inv_s) then
                res_s <= (sam_s - (shift_right(left_s, 1) + shift_right(right_s, 1)));
            else
                res_s <= (sam_s + (shift_right(left_s, 1) + shift_right(right_s, 1)));
            end if;
        else
            if bool(fwd_inv_s) then
                res_s <= (sam_s + shift_right(((left_s + right_s) + 2), 2));
            else
                res_s <= (sam_s - shift_right(((left_s + right_s) + 2), 2));
            end if;
        end if;
    end if;
end process JPEG_HDL;

end architecture MyHDL;
