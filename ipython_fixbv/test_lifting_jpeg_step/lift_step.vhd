-- File: lift_step.vhd
-- Generated by MyHDL 0.9.dev0
-- Date: Fri May 15 14:27:14 2015


library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
use std.textio.all;

use work.pck_myhdl_090.all;

entity lift_step is
    port (
        left_i: in unsigned(8 downto 0);
        sam_i: in unsigned(8 downto 0);
        right_i: in unsigned(8 downto 0);
        flgs_i: in unsigned(3 downto 0);
        update_i: in std_logic;
        clk: in std_logic;
        res_o: out signed (9 downto 0);
        update_o: out std_logic
    );
end entity lift_step;


architecture MyHDL of lift_step is






begin




LIFT_STEP_RTL: process (clk) is
begin
    if rising_edge(clk) then
        if (update_i = '1') then
            update_o <= '0';
            if (flgs_i = 7) then
                res_o <= (resize(signed(sam_i), 10) - (shift_right(resize(signed(left_i), 10), 1) + shift_right(resize(signed(right_i), 10), 1)));
            elsif (flgs_i = 5) then
                res_o <= (resize(signed(sam_i), 10) + (shift_right(resize(signed(left_i), 10), 1) + shift_right(resize(signed(right_i), 10), 1)));
            elsif (flgs_i = 6) then
                res_o <= (resize(signed(sam_i), 10) + shift_right(((resize(signed(left_i), 10) + resize(signed(right_i), 10)) + 2), 2));
            elsif (flgs_i = 4) then
                res_o <= (resize(signed(sam_i), 10) - shift_right(((resize(signed(left_i), 10) + resize(signed(right_i), 10)) + 2), 2));
            end if;
        else
            update_o <= '1';
        end if;
    end if;
end process LIFT_STEP_RTL;

end architecture MyHDL;
