-- File: m_ex1.vhd
-- Generated by MyHDL 0.9dev
-- Date: Wed Jul  2 09:37:08 2014


library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
use std.textio.all;

use work.pck_myhdl_09.all;

entity m_ex1 is
    port (
        clk: in std_logic;
        p: in std_logic;
        even_odd: in std_logic;
        fwd_inv: in std_logic;
        pix_x2_3: in signed (39 downto 0);
        pix_x2_2: in signed (39 downto 0);
        pix_x2_1: in signed (39 downto 0);
        pix_x4_1: in signed (39 downto 0);
        pix_x4_3: in signed (39 downto 0);
        pix_x4_2: in signed (39 downto 0);
        pix_x3_2: in signed (39 downto 0);
        pix_d3: out signed (39 downto 0);
        pix_x3_1: in signed (39 downto 0);
        pix_d3_3: out signed (39 downto 0);
        pix_x5_1: in signed (39 downto 0);
        pix_x5_2: in signed (39 downto 0);
        pix_x5_3: in signed (39 downto 0);
        pix_a2_3: out signed (39 downto 0);
        pix_x3_3: in signed (39 downto 0);
        pix_a2: out signed (39 downto 0);
        pix_x2: in signed (39 downto 0);
        pix_x3: in signed (39 downto 0);
        pix_x4: in signed (39 downto 0);
        pix_x5: in signed (39 downto 0);
        pix_d3_2: out signed (39 downto 0);
        pix_a2_1: out signed (39 downto 0);
        pix_a2_2: out signed (39 downto 0);
        pix_d3_1: out signed (39 downto 0)
    );
end entity m_ex1;


architecture MyHDL of m_ex1 is






begin




M_EX1_HDL: process (clk) is
    variable ca3: signed(39 downto 0);
    variable ca2: signed(39 downto 0);
    variable ca1: signed(39 downto 0);
    variable ca4: signed(39 downto 0);
    variable ra4: signed(39 downto 0);
    variable ra2: signed(39 downto 0);
    variable ra3: signed(39 downto 0);
    variable ra1: signed(39 downto 0);
begin
    if rising_edge(clk) then
        if (not bool(p)) then
            if bool(even_odd) then
                if bool(fwd_inv) then
                    -- p false 1st pass even_odd True fwd_inv True (x2+x3) * ca1 
                    pix_d3 <= resize((pix_x2 + pix_x3) * ca1, 40);
                    pix_d3_1 <= resize((pix_x2_1 + pix_x3_1) * ca1, 40);
                    pix_d3_2 <= resize((pix_x2_2 + pix_x3_2) * ca1, 40);
                    pix_d3_3 <= resize((pix_x2_2 + pix_x3_2) * ca1, 40);
                else
                    -- p false 1st pass even_odd True fwd_inv False (x4+x5) * ra4 
                    pix_a2 <= resize((pix_x4 + pix_x5) * ra4, 40);
                    pix_a2_1 <= resize((pix_x4_1 + pix_x5_1) * ra4, 40);
                    pix_a2_2 <= resize((pix_x4_2 + pix_x5_2) * ra4, 40);
                    pix_a2_3 <= resize((pix_x4_3 + pix_x5_3) * ra4, 40);
                end if;
            else
                if bool(fwd_inv) then
                    -- p false 1st pass even_odd false fwd_inv True (x4+x5) * ca2 
                    pix_a2 <= resize((pix_x4 + pix_x5) * ca2, 40);
                    pix_a2_1 <= resize((pix_x4_1 + pix_x5_1) * ca2, 40);
                    pix_a2_2 <= resize((pix_x4_2 + pix_x5_2) * ca2, 40);
                    pix_a2_3 <= resize((pix_x4_3 + pix_x5_3) * ca2, 40);
                else
                    -- p false 1st pass even_odd false fwd_inv False (x2+x3) * ra3 
                    pix_d3 <= resize((pix_x2 + pix_x3) * ra3, 40);
                    pix_d3_1 <= resize((pix_x2_1 + pix_x3_1) * ra3, 40);
                    pix_d3_2 <= resize((pix_x2_2 + pix_x3_2) * ra3, 40);
                    pix_d3_3 <= resize((pix_x2_2 + pix_x3_3) * ra3, 40);
                end if;
            end if;
        else
            if bool(even_odd) then
                if bool(fwd_inv) then
                    -- p True 2nd pass even_odd True fwd_inv True (x2+x3) * ca3 
                    pix_d3 <= resize((pix_x2 + pix_x3) * ca3, 40);
                    pix_d3_1 <= resize((pix_x2_1 + pix_x3_1) * ca3, 40);
                    pix_d3_2 <= resize((pix_x2_2 + pix_x3_2) * ca3, 40);
                    pix_d3_3 <= resize((pix_x2_3 + pix_x3_3) * ca3, 40);
                else
                    -- p True 2nd pass even_odd True fwd_inv False (x4+x5) * ra2 
                    pix_a2 <= resize((pix_x4 + pix_x5) * ra2, 40);
                    pix_a2_1 <= resize((pix_x4_1 + pix_x5_1) * ra2, 40);
                    pix_a2_2 <= resize((pix_x4_2 + pix_x5_2) * ra2, 40);
                    pix_a2_3 <= resize((pix_x4_3 + pix_x5_3) * ra2, 40);
                end if;
            else
                if bool(fwd_inv) then
                    -- p True 2nd pass even_odd False fwd_inv True (x2+x3) * ca4 
                    pix_a2 <= resize((pix_x4 + pix_x5) * ca4, 40);
                    pix_a2_1 <= resize((pix_x4_1 + pix_x5_1) * ca4, 40);
                    pix_a2_2 <= resize((pix_x4_2 + pix_x5_2) * ca4, 40);
                    pix_a2_3 <= resize((pix_x4_3 + pix_x5_3) * ca4, 40);
                else
                    -- p True 2nd pass even_odd False fwd_inv False (x2+x3) * ra1 
                    pix_d3 <= resize((pix_x2 + pix_x3) * ra1, 40);
                    pix_d3_1 <= resize((pix_x2_1 + pix_x3_1) * ra1, 40);
                    pix_d3_2 <= resize((pix_x2_2 + pix_x3_2) * ra1, 40);
                    pix_d3_3 <= resize((pix_x2_3 + pix_x3_3) * ra1, 40);
                end if;
            end if;
        end if;
    end if;
end process M_EX1_HDL;

end architecture MyHDL;
