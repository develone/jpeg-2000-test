-- File: multi_jpeg.vhd
-- Generated by MyHDL 0.9dev
-- Date: Mon Feb  2 07:51:14 2015


library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
use std.textio.all;

use work.pck_myhdl_09.all;

entity multi_jpeg is
    port (
        clk_fast: in std_logic;
        sig0_in_x: in unsigned(31 downto 0);
        noupdate0_s: out std_logic;
        res0_s: out signed (10 downto 0);
        sig1_in_x: in unsigned(31 downto 0);
        noupdate1_s: out std_logic;
        res1_s: out signed (10 downto 0);
        sig2_in_x: in unsigned(31 downto 0);
        noupdate2_s: out std_logic;
        res2_s: out signed (10 downto 0);
        sig3_in_x: in unsigned(31 downto 0);
        noupdate3_s: out std_logic;
        res3_s: out signed (10 downto 0);
        sig4_in_x: in unsigned(31 downto 0);
        noupdate4_s: out std_logic;
        res4_s: out signed (10 downto 0);
        sig5_in_x: in unsigned(31 downto 0);
        noupdate5_s: out std_logic;
        res5_s: out signed (10 downto 0);
        sig6_in_x: in unsigned(31 downto 0);
        noupdate6_s: out std_logic;
        res6_s: out signed (10 downto 0);
        sig7_in_x: in unsigned(31 downto 0);
        noupdate7_s: out std_logic;
        res7_s: out signed (10 downto 0);
        sig8_in_x: in unsigned(31 downto 0);
        noupdate8_s: out std_logic;
        res8_s: out signed (10 downto 0);
        sig9_in_x: in unsigned(31 downto 0);
        noupdate9_s: out std_logic;
        res9_s: out signed (10 downto 0);
        sig10_in_x: in unsigned(31 downto 0);
        noupdate10_s: out std_logic;
        res10_s: out signed (10 downto 0);
        sig11_in_x: in unsigned(31 downto 0);
        noupdate11_s: out std_logic;
        res11_s: out signed (10 downto 0);
        sig12_in_x: in unsigned(31 downto 0);
        noupdate12_s: out std_logic;
        res12_s: out signed (10 downto 0);
        sig13_in_x: in unsigned(31 downto 0);
        noupdate13_s: out std_logic;
        res13_s: out signed (10 downto 0);
        sig14_in_x: in unsigned(31 downto 0);
        noupdate14_s: out std_logic;
        res14_s: out signed (10 downto 0);
        sig15_in_x: in unsigned(31 downto 0);
        noupdate15_s: out std_logic;
        res15_s: out signed (10 downto 0)
    );
end entity multi_jpeg;


architecture MyHDL of multi_jpeg is






begin




MULTI_JPEG_INSTANCE_0_JPEG: process (clk_fast) is
begin
    if rising_edge(clk_fast) then
        if bool(sig0_in_x(29)) then
            noupdate0_s <= '0';
            if bool(sig0_in_x(27)) then
                if bool(sig0_in_x(28)) then
                    res0_s <= signed(resize(sig0_in_x(18-1 downto 9), 11) - (shift_right(resize(sig0_in_x(9-1 downto 0), 11), 1) + shift_right(resize(sig0_in_x(27-1 downto 18), 11), 1)));
                else
                    res0_s <= signed(resize(sig0_in_x(18-1 downto 9), 11) + (shift_right(resize(sig0_in_x(9-1 downto 0), 11), 1) + shift_right(resize(sig0_in_x(27-1 downto 18), 11), 1)));
                end if;
            else
                if bool(sig0_in_x(28)) then
                    res0_s <= signed(resize(sig0_in_x(18-1 downto 9), 11) + shift_right(((resize(sig0_in_x(9-1 downto 0), 11) + sig0_in_x(27-1 downto 18)) + 2), 2));
                else
                    res0_s <= signed(resize(sig0_in_x(18-1 downto 9), 11) - shift_right(((resize(sig0_in_x(9-1 downto 0), 11) + sig0_in_x(27-1 downto 18)) + 2), 2));
                end if;
            end if;
        else
            noupdate0_s <= '1';
        end if;
    end if;
end process MULTI_JPEG_INSTANCE_0_JPEG;


MULTI_JPEG_INSTANCE_1_JPEG: process (clk_fast) is
begin
    if rising_edge(clk_fast) then
        if bool(sig1_in_x(29)) then
            noupdate1_s <= '0';
            if bool(sig1_in_x(27)) then
                if bool(sig1_in_x(28)) then
                    res1_s <= signed(resize(sig1_in_x(18-1 downto 9), 11) - (shift_right(resize(sig1_in_x(9-1 downto 0), 11), 1) + shift_right(resize(sig1_in_x(27-1 downto 18), 11), 1)));
                else
                    res1_s <= signed(resize(sig1_in_x(18-1 downto 9), 11) + (shift_right(resize(sig1_in_x(9-1 downto 0), 11), 1) + shift_right(resize(sig1_in_x(27-1 downto 18), 11), 1)));
                end if;
            else
                if bool(sig1_in_x(28)) then
                    res1_s <= signed(resize(sig1_in_x(18-1 downto 9), 11) + shift_right(((resize(sig1_in_x(9-1 downto 0), 11) + sig1_in_x(27-1 downto 18)) + 2), 2));
                else
                    res1_s <= signed(resize(sig1_in_x(18-1 downto 9), 11) - shift_right(((resize(sig1_in_x(9-1 downto 0), 11) + sig1_in_x(27-1 downto 18)) + 2), 2));
                end if;
            end if;
        else
            noupdate1_s <= '1';
        end if;
    end if;
end process MULTI_JPEG_INSTANCE_1_JPEG;


MULTI_JPEG_INSTANCE_2_JPEG: process (clk_fast) is
begin
    if rising_edge(clk_fast) then
        if bool(sig2_in_x(29)) then
            noupdate2_s <= '0';
            if bool(sig2_in_x(27)) then
                if bool(sig2_in_x(28)) then
                    res2_s <= signed(resize(sig2_in_x(18-1 downto 9), 11) - (shift_right(resize(sig2_in_x(9-1 downto 0), 11), 1) + shift_right(resize(sig2_in_x(27-1 downto 18), 11), 1)));
                else
                    res2_s <= signed(resize(sig2_in_x(18-1 downto 9), 11) + (shift_right(resize(sig2_in_x(9-1 downto 0), 11), 1) + shift_right(resize(sig2_in_x(27-1 downto 18), 11), 1)));
                end if;
            else
                if bool(sig2_in_x(28)) then
                    res2_s <= signed(resize(sig2_in_x(18-1 downto 9), 11) + shift_right(((resize(sig2_in_x(9-1 downto 0), 11) + sig2_in_x(27-1 downto 18)) + 2), 2));
                else
                    res2_s <= signed(resize(sig2_in_x(18-1 downto 9), 11) - shift_right(((resize(sig2_in_x(9-1 downto 0), 11) + sig2_in_x(27-1 downto 18)) + 2), 2));
                end if;
            end if;
        else
            noupdate2_s <= '1';
        end if;
    end if;
end process MULTI_JPEG_INSTANCE_2_JPEG;


MULTI_JPEG_INSTANCE_3_JPEG: process (clk_fast) is
begin
    if rising_edge(clk_fast) then
        if bool(sig3_in_x(29)) then
            noupdate3_s <= '0';
            if bool(sig3_in_x(27)) then
                if bool(sig3_in_x(28)) then
                    res3_s <= signed(resize(sig3_in_x(18-1 downto 9), 11) - (shift_right(resize(sig3_in_x(9-1 downto 0), 11), 1) + shift_right(resize(sig3_in_x(27-1 downto 18), 11), 1)));
                else
                    res3_s <= signed(resize(sig3_in_x(18-1 downto 9), 11) + (shift_right(resize(sig3_in_x(9-1 downto 0), 11), 1) + shift_right(resize(sig3_in_x(27-1 downto 18), 11), 1)));
                end if;
            else
                if bool(sig3_in_x(28)) then
                    res3_s <= signed(resize(sig3_in_x(18-1 downto 9), 11) + shift_right(((resize(sig3_in_x(9-1 downto 0), 11) + sig3_in_x(27-1 downto 18)) + 2), 2));
                else
                    res3_s <= signed(resize(sig3_in_x(18-1 downto 9), 11) - shift_right(((resize(sig3_in_x(9-1 downto 0), 11) + sig3_in_x(27-1 downto 18)) + 2), 2));
                end if;
            end if;
        else
            noupdate3_s <= '1';
        end if;
    end if;
end process MULTI_JPEG_INSTANCE_3_JPEG;


MULTI_JPEG_INSTANCE_4_JPEG: process (clk_fast) is
begin
    if rising_edge(clk_fast) then
        if bool(sig4_in_x(29)) then
            noupdate4_s <= '0';
            if bool(sig4_in_x(27)) then
                if bool(sig4_in_x(28)) then
                    res4_s <= signed(resize(sig4_in_x(18-1 downto 9), 11) - (shift_right(resize(sig4_in_x(9-1 downto 0), 11), 1) + shift_right(resize(sig4_in_x(27-1 downto 18), 11), 1)));
                else
                    res4_s <= signed(resize(sig4_in_x(18-1 downto 9), 11) + (shift_right(resize(sig4_in_x(9-1 downto 0), 11), 1) + shift_right(resize(sig4_in_x(27-1 downto 18), 11), 1)));
                end if;
            else
                if bool(sig4_in_x(28)) then
                    res4_s <= signed(resize(sig4_in_x(18-1 downto 9), 11) + shift_right(((resize(sig4_in_x(9-1 downto 0), 11) + sig4_in_x(27-1 downto 18)) + 2), 2));
                else
                    res4_s <= signed(resize(sig4_in_x(18-1 downto 9), 11) - shift_right(((resize(sig4_in_x(9-1 downto 0), 11) + sig4_in_x(27-1 downto 18)) + 2), 2));
                end if;
            end if;
        else
            noupdate4_s <= '1';
        end if;
    end if;
end process MULTI_JPEG_INSTANCE_4_JPEG;


MULTI_JPEG_INSTANCE_5_JPEG: process (clk_fast) is
begin
    if rising_edge(clk_fast) then
        if bool(sig5_in_x(29)) then
            noupdate5_s <= '0';
            if bool(sig5_in_x(27)) then
                if bool(sig5_in_x(28)) then
                    res5_s <= signed(resize(sig5_in_x(18-1 downto 9), 11) - (shift_right(resize(sig5_in_x(9-1 downto 0), 11), 1) + shift_right(resize(sig5_in_x(27-1 downto 18), 11), 1)));
                else
                    res5_s <= signed(resize(sig5_in_x(18-1 downto 9), 11) + (shift_right(resize(sig5_in_x(9-1 downto 0), 11), 1) + shift_right(resize(sig5_in_x(27-1 downto 18), 11), 1)));
                end if;
            else
                if bool(sig5_in_x(28)) then
                    res5_s <= signed(resize(sig5_in_x(18-1 downto 9), 11) + shift_right(((resize(sig5_in_x(9-1 downto 0), 11) + sig5_in_x(27-1 downto 18)) + 2), 2));
                else
                    res5_s <= signed(resize(sig5_in_x(18-1 downto 9), 11) - shift_right(((resize(sig5_in_x(9-1 downto 0), 11) + sig5_in_x(27-1 downto 18)) + 2), 2));
                end if;
            end if;
        else
            noupdate5_s <= '1';
        end if;
    end if;
end process MULTI_JPEG_INSTANCE_5_JPEG;


MULTI_JPEG_INSTANCE_6_JPEG: process (clk_fast) is
begin
    if rising_edge(clk_fast) then
        if bool(sig6_in_x(29)) then
            noupdate6_s <= '0';
            if bool(sig6_in_x(27)) then
                if bool(sig6_in_x(28)) then
                    res6_s <= signed(resize(sig6_in_x(18-1 downto 9), 11) - (shift_right(resize(sig6_in_x(9-1 downto 0), 11), 1) + shift_right(resize(sig6_in_x(27-1 downto 18), 11), 1)));
                else
                    res6_s <= signed(resize(sig6_in_x(18-1 downto 9), 11) + (shift_right(resize(sig6_in_x(9-1 downto 0), 11), 1) + shift_right(resize(sig6_in_x(27-1 downto 18), 11), 1)));
                end if;
            else
                if bool(sig6_in_x(28)) then
                    res6_s <= signed(resize(sig6_in_x(18-1 downto 9), 11) + shift_right(((resize(sig6_in_x(9-1 downto 0), 11) + sig6_in_x(27-1 downto 18)) + 2), 2));
                else
                    res6_s <= signed(resize(sig6_in_x(18-1 downto 9), 11) - shift_right(((resize(sig6_in_x(9-1 downto 0), 11) + sig6_in_x(27-1 downto 18)) + 2), 2));
                end if;
            end if;
        else
            noupdate6_s <= '1';
        end if;
    end if;
end process MULTI_JPEG_INSTANCE_6_JPEG;


MULTI_JPEG_INSTANCE_7_JPEG: process (clk_fast) is
begin
    if rising_edge(clk_fast) then
        if bool(sig7_in_x(29)) then
            noupdate7_s <= '0';
            if bool(sig7_in_x(27)) then
                if bool(sig7_in_x(28)) then
                    res7_s <= signed(resize(sig7_in_x(18-1 downto 9), 11) - (shift_right(resize(sig7_in_x(9-1 downto 0), 11), 1) + shift_right(resize(sig7_in_x(27-1 downto 18), 11), 1)));
                else
                    res7_s <= signed(resize(sig7_in_x(18-1 downto 9), 11) + (shift_right(resize(sig7_in_x(9-1 downto 0), 11), 1) + shift_right(resize(sig7_in_x(27-1 downto 18), 11), 1)));
                end if;
            else
                if bool(sig7_in_x(28)) then
                    res7_s <= signed(resize(sig7_in_x(18-1 downto 9), 11) + shift_right(((resize(sig7_in_x(9-1 downto 0), 11) + sig7_in_x(27-1 downto 18)) + 2), 2));
                else
                    res7_s <= signed(resize(sig7_in_x(18-1 downto 9), 11) - shift_right(((resize(sig7_in_x(9-1 downto 0), 11) + sig7_in_x(27-1 downto 18)) + 2), 2));
                end if;
            end if;
        else
            noupdate7_s <= '1';
        end if;
    end if;
end process MULTI_JPEG_INSTANCE_7_JPEG;


MULTI_JPEG_INSTANCE_8_JPEG: process (clk_fast) is
begin
    if rising_edge(clk_fast) then
        if bool(sig8_in_x(29)) then
            noupdate8_s <= '0';
            if bool(sig8_in_x(27)) then
                if bool(sig8_in_x(28)) then
                    res8_s <= signed(resize(sig8_in_x(18-1 downto 9), 11) - (shift_right(resize(sig8_in_x(9-1 downto 0), 11), 1) + shift_right(resize(sig8_in_x(27-1 downto 18), 11), 1)));
                else
                    res8_s <= signed(resize(sig8_in_x(18-1 downto 9), 11) + (shift_right(resize(sig8_in_x(9-1 downto 0), 11), 1) + shift_right(resize(sig8_in_x(27-1 downto 18), 11), 1)));
                end if;
            else
                if bool(sig8_in_x(28)) then
                    res8_s <= signed(resize(sig8_in_x(18-1 downto 9), 11) + shift_right(((resize(sig8_in_x(9-1 downto 0), 11) + sig8_in_x(27-1 downto 18)) + 2), 2));
                else
                    res8_s <= signed(resize(sig8_in_x(18-1 downto 9), 11) - shift_right(((resize(sig8_in_x(9-1 downto 0), 11) + sig8_in_x(27-1 downto 18)) + 2), 2));
                end if;
            end if;
        else
            noupdate8_s <= '1';
        end if;
    end if;
end process MULTI_JPEG_INSTANCE_8_JPEG;


MULTI_JPEG_INSTANCE_9_JPEG: process (clk_fast) is
begin
    if rising_edge(clk_fast) then
        if bool(sig9_in_x(29)) then
            noupdate9_s <= '0';
            if bool(sig9_in_x(27)) then
                if bool(sig9_in_x(28)) then
                    res9_s <= signed(resize(sig9_in_x(18-1 downto 9), 11) - (shift_right(resize(sig9_in_x(9-1 downto 0), 11), 1) + shift_right(resize(sig9_in_x(27-1 downto 18), 11), 1)));
                else
                    res9_s <= signed(resize(sig9_in_x(18-1 downto 9), 11) + (shift_right(resize(sig9_in_x(9-1 downto 0), 11), 1) + shift_right(resize(sig9_in_x(27-1 downto 18), 11), 1)));
                end if;
            else
                if bool(sig9_in_x(28)) then
                    res9_s <= signed(resize(sig9_in_x(18-1 downto 9), 11) + shift_right(((resize(sig9_in_x(9-1 downto 0), 11) + sig9_in_x(27-1 downto 18)) + 2), 2));
                else
                    res9_s <= signed(resize(sig9_in_x(18-1 downto 9), 11) - shift_right(((resize(sig9_in_x(9-1 downto 0), 11) + sig9_in_x(27-1 downto 18)) + 2), 2));
                end if;
            end if;
        else
            noupdate9_s <= '1';
        end if;
    end if;
end process MULTI_JPEG_INSTANCE_9_JPEG;


MULTI_JPEG_INSTANCE_10_JPEG: process (clk_fast) is
begin
    if rising_edge(clk_fast) then
        if bool(sig10_in_x(29)) then
            noupdate10_s <= '0';
            if bool(sig10_in_x(27)) then
                if bool(sig10_in_x(28)) then
                    res10_s <= signed(resize(sig10_in_x(18-1 downto 9), 11) - (shift_right(resize(sig10_in_x(9-1 downto 0), 11), 1) + shift_right(resize(sig10_in_x(27-1 downto 18), 11), 1)));
                else
                    res10_s <= signed(resize(sig10_in_x(18-1 downto 9), 11) + (shift_right(resize(sig10_in_x(9-1 downto 0), 11), 1) + shift_right(resize(sig10_in_x(27-1 downto 18), 11), 1)));
                end if;
            else
                if bool(sig10_in_x(28)) then
                    res10_s <= signed(resize(sig10_in_x(18-1 downto 9), 11) + shift_right(((resize(sig10_in_x(9-1 downto 0), 11) + sig10_in_x(27-1 downto 18)) + 2), 2));
                else
                    res10_s <= signed(resize(sig10_in_x(18-1 downto 9), 11) - shift_right(((resize(sig10_in_x(9-1 downto 0), 11) + sig10_in_x(27-1 downto 18)) + 2), 2));
                end if;
            end if;
        else
            noupdate10_s <= '1';
        end if;
    end if;
end process MULTI_JPEG_INSTANCE_10_JPEG;


MULTI_JPEG_INSTANCE_11_JPEG: process (clk_fast) is
begin
    if rising_edge(clk_fast) then
        if bool(sig11_in_x(29)) then
            noupdate11_s <= '0';
            if bool(sig11_in_x(27)) then
                if bool(sig11_in_x(28)) then
                    res11_s <= signed(resize(sig11_in_x(18-1 downto 9), 11) - (shift_right(resize(sig11_in_x(9-1 downto 0), 11), 1) + shift_right(resize(sig11_in_x(27-1 downto 18), 11), 1)));
                else
                    res11_s <= signed(resize(sig11_in_x(18-1 downto 9), 11) + (shift_right(resize(sig11_in_x(9-1 downto 0), 11), 1) + shift_right(resize(sig11_in_x(27-1 downto 18), 11), 1)));
                end if;
            else
                if bool(sig11_in_x(28)) then
                    res11_s <= signed(resize(sig11_in_x(18-1 downto 9), 11) + shift_right(((resize(sig11_in_x(9-1 downto 0), 11) + sig11_in_x(27-1 downto 18)) + 2), 2));
                else
                    res11_s <= signed(resize(sig11_in_x(18-1 downto 9), 11) - shift_right(((resize(sig11_in_x(9-1 downto 0), 11) + sig11_in_x(27-1 downto 18)) + 2), 2));
                end if;
            end if;
        else
            noupdate11_s <= '1';
        end if;
    end if;
end process MULTI_JPEG_INSTANCE_11_JPEG;


MULTI_JPEG_INSTANCE_12_JPEG: process (clk_fast) is
begin
    if rising_edge(clk_fast) then
        if bool(sig12_in_x(29)) then
            noupdate12_s <= '0';
            if bool(sig12_in_x(27)) then
                if bool(sig12_in_x(28)) then
                    res12_s <= signed(resize(sig12_in_x(18-1 downto 9), 11) - (shift_right(resize(sig12_in_x(9-1 downto 0), 11), 1) + shift_right(resize(sig12_in_x(27-1 downto 18), 11), 1)));
                else
                    res12_s <= signed(resize(sig12_in_x(18-1 downto 9), 11) + (shift_right(resize(sig12_in_x(9-1 downto 0), 11), 1) + shift_right(resize(sig12_in_x(27-1 downto 18), 11), 1)));
                end if;
            else
                if bool(sig12_in_x(28)) then
                    res12_s <= signed(resize(sig12_in_x(18-1 downto 9), 11) + shift_right(((resize(sig12_in_x(9-1 downto 0), 11) + sig12_in_x(27-1 downto 18)) + 2), 2));
                else
                    res12_s <= signed(resize(sig12_in_x(18-1 downto 9), 11) - shift_right(((resize(sig12_in_x(9-1 downto 0), 11) + sig12_in_x(27-1 downto 18)) + 2), 2));
                end if;
            end if;
        else
            noupdate12_s <= '1';
        end if;
    end if;
end process MULTI_JPEG_INSTANCE_12_JPEG;


MULTI_JPEG_INSTANCE_13_JPEG: process (clk_fast) is
begin
    if rising_edge(clk_fast) then
        if bool(sig13_in_x(29)) then
            noupdate13_s <= '0';
            if bool(sig13_in_x(27)) then
                if bool(sig13_in_x(28)) then
                    res13_s <= signed(resize(sig13_in_x(18-1 downto 9), 11) - (shift_right(resize(sig13_in_x(9-1 downto 0), 11), 1) + shift_right(resize(sig13_in_x(27-1 downto 18), 11), 1)));
                else
                    res13_s <= signed(resize(sig13_in_x(18-1 downto 9), 11) + (shift_right(resize(sig13_in_x(9-1 downto 0), 11), 1) + shift_right(resize(sig13_in_x(27-1 downto 18), 11), 1)));
                end if;
            else
                if bool(sig13_in_x(28)) then
                    res13_s <= signed(resize(sig13_in_x(18-1 downto 9), 11) + shift_right(((resize(sig13_in_x(9-1 downto 0), 11) + sig13_in_x(27-1 downto 18)) + 2), 2));
                else
                    res13_s <= signed(resize(sig13_in_x(18-1 downto 9), 11) - shift_right(((resize(sig13_in_x(9-1 downto 0), 11) + sig13_in_x(27-1 downto 18)) + 2), 2));
                end if;
            end if;
        else
            noupdate13_s <= '1';
        end if;
    end if;
end process MULTI_JPEG_INSTANCE_13_JPEG;


MULTI_JPEG_INSTANCE_14_JPEG: process (clk_fast) is
begin
    if rising_edge(clk_fast) then
        if bool(sig14_in_x(29)) then
            noupdate14_s <= '0';
            if bool(sig14_in_x(27)) then
                if bool(sig14_in_x(28)) then
                    res14_s <= signed(resize(sig14_in_x(18-1 downto 9), 11) - (shift_right(resize(sig14_in_x(9-1 downto 0), 11), 1) + shift_right(resize(sig14_in_x(27-1 downto 18), 11), 1)));
                else
                    res14_s <= signed(resize(sig14_in_x(18-1 downto 9), 11) + (shift_right(resize(sig14_in_x(9-1 downto 0), 11), 1) + shift_right(resize(sig14_in_x(27-1 downto 18), 11), 1)));
                end if;
            else
                if bool(sig14_in_x(28)) then
                    res14_s <= signed(resize(sig14_in_x(18-1 downto 9), 11) + shift_right(((resize(sig14_in_x(9-1 downto 0), 11) + sig14_in_x(27-1 downto 18)) + 2), 2));
                else
                    res14_s <= signed(resize(sig14_in_x(18-1 downto 9), 11) - shift_right(((resize(sig14_in_x(9-1 downto 0), 11) + sig14_in_x(27-1 downto 18)) + 2), 2));
                end if;
            end if;
        else
            noupdate14_s <= '1';
        end if;
    end if;
end process MULTI_JPEG_INSTANCE_14_JPEG;


MULTI_JPEG_INSTANCE_15_JPEG: process (clk_fast) is
begin
    if rising_edge(clk_fast) then
        if bool(sig15_in_x(29)) then
            noupdate15_s <= '0';
            if bool(sig15_in_x(27)) then
                if bool(sig15_in_x(28)) then
                    res15_s <= signed(resize(sig15_in_x(18-1 downto 9), 11) - (shift_right(resize(sig15_in_x(9-1 downto 0), 11), 1) + shift_right(resize(sig15_in_x(27-1 downto 18), 11), 1)));
                else
                    res15_s <= signed(resize(sig15_in_x(18-1 downto 9), 11) + (shift_right(resize(sig15_in_x(9-1 downto 0), 11), 1) + shift_right(resize(sig15_in_x(27-1 downto 18), 11), 1)));
                end if;
            else
                if bool(sig15_in_x(28)) then
                    res15_s <= signed(resize(sig15_in_x(18-1 downto 9), 11) + shift_right(((resize(sig15_in_x(9-1 downto 0), 11) + sig15_in_x(27-1 downto 18)) + 2), 2));
                else
                    res15_s <= signed(resize(sig15_in_x(18-1 downto 9), 11) - shift_right(((resize(sig15_in_x(9-1 downto 0), 11) + sig15_in_x(27-1 downto 18)) + 2), 2));
                end if;
            end if;
        else
            noupdate15_s <= '1';
        end if;
    end if;
end process MULTI_JPEG_INSTANCE_15_JPEG;

end architecture MyHDL;