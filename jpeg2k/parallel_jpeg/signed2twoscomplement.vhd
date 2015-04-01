-- File: signed2twoscomplement.vhd
-- Generated by MyHDL 0.9dev
-- Date: Wed Apr  1 12:49:32 2015


library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
use std.textio.all;

use work.pck_myhdl_09.all;

entity signed2twoscomplement is
    port (
        bits_in_sig: in signed (9 downto 0);
        vv: out unsigned(8 downto 0)
    );
end entity signed2twoscomplement;
-- return 

architecture MyHDL of signed2twoscomplement is






begin





vv <= resize(unsigned(bits_in_sig), 9);

end architecture MyHDL;
