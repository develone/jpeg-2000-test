-- File: sig2one.vhd
-- Generated by MyHDL 0.9dev
-- Date: Thu Mar 12 08:16:52 2015


library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
use std.textio.all;

use work.pck_myhdl_09.all;

entity sig2one is
    port (
        Sout_s: out std_logic_vector(159 downto 0);
        clk_fast: in std_logic;
        combine_sig_s: in std_logic;
        Sin0: in std_logic_vector(9 downto 0);
        Sin1: in std_logic_vector(9 downto 0);
        Sin2: in std_logic_vector(9 downto 0);
        Sin3: in std_logic_vector(9 downto 0);
        Sin4: in std_logic_vector(9 downto 0);
        Sin5: in std_logic_vector(9 downto 0);
        Sin6: in std_logic_vector(9 downto 0);
        Sin7: in std_logic_vector(9 downto 0);
        Sin8: in std_logic_vector(9 downto 0);
        Sin9: in std_logic_vector(9 downto 0);
        Sin10: in std_logic_vector(9 downto 0);
        Sin11: in std_logic_vector(9 downto 0);
        Sin12: in std_logic_vector(9 downto 0);
        Sin13: in std_logic_vector(9 downto 0);
        Sin14: in std_logic_vector(9 downto 0);
        Sin15: in std_logic_vector(9 downto 0)
    );
end entity sig2one;


architecture MyHDL of sig2one is






begin




SIG2ONE_COMBINE_LOGIC: process (clk_fast) is
begin
    if rising_edge(clk_fast) then
        if (combine_sig_s = '1') then
            Sout_s <= std_logic_vector(resize(unsigned'(unsigned(Sin14) & unsigned(Sin13) & unsigned(Sin12) & unsigned(Sin11) & unsigned(Sin10) & unsigned(Sin9) & unsigned(Sin8) & unsigned(Sin7) & unsigned(Sin6) & unsigned(Sin5) & unsigned(Sin4) & unsigned(Sin3) & unsigned(Sin2) & unsigned(Sin1) & unsigned(Sin0)), 160));
        else
            Sout_s <= std_logic_vector(to_unsigned(0, 160));
        end if;
    end if;
end process SIG2ONE_COMBINE_LOGIC;

end architecture MyHDL;
