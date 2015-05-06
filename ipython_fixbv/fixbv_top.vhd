-- File: fixbv_top.vhd
-- Generated by MyHDL 0.9.dev0
-- Date: Wed May  6 09:55:06 2015


library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
use std.textio.all;

use work.pck_myhdl_090.all;

entity fixbv_top is
    port (
        clk: in std_logic;
        do_add: in std_logic;
        x_sig: in signed (30 downto 0);
        y_sig: in signed (30 downto 0);
        sum_sig: out signed (31 downto 0);
        done_add: out std_logic;
        do_mul: in std_logic;
        prod_sig: out signed (62 downto 0);
        done_mul: out std_logic;
        do_sub: in std_logic;
        sub_sig: out signed (31 downto 0);
        done_sub: out std_logic
    );
end entity fixbv_top;


architecture MyHDL of fixbv_top is






begin




FIXBV_TOP_DUT_FIXBV_ADD_ADD_RTL: process (clk) is
begin
    if rising_edge(clk) then
        if (do_add = '1') then
            done_add <= '0';
            sum_sig <= (resize(x_sig, 32) + y_sig);
        else
            done_add <= '1';
            sum_sig <= to_signed(0, 32);
        end if;
    end if;
end process FIXBV_TOP_DUT_FIXBV_ADD_ADD_RTL;


FIXBV_TOP_DUT_FIXBV_SUB_SUB_RTL: process (clk) is
begin
    if rising_edge(clk) then
        if (do_sub = '1') then
            done_sub <= '0';
            sub_sig <= (resize(x_sig, 32) - y_sig);
        else
            done_sub <= '1';
            sub_sig <= to_signed(0, 32);
        end if;
    end if;
end process FIXBV_TOP_DUT_FIXBV_SUB_SUB_RTL;


FIXBV_TOP_DUT_FIXBV_MUL_ADD_RTL: process (clk) is
begin
    if rising_edge(clk) then
        if (do_mul = '1') then
            done_mul <= '0';
            prod_sig <= (resize(x_sig, 32) * y_sig);
        else
            done_mul <= '1';
            prod_sig <= to_signed(0, 63);
        end if;
    end if;
end process FIXBV_TOP_DUT_FIXBV_MUL_ADD_RTL;

end architecture MyHDL;
