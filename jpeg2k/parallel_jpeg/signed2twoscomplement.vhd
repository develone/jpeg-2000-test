-- File: signed2twoscomplement.vhd
-- Generated by MyHDL 0.9dev
-- Date: Thu Apr  2 05:33:09 2015


library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
use std.textio.all;

use work.pck_myhdl_09.all;

entity signed2twoscomplement is
    port (
        x: in signed (9 downto 0);
        z: out unsigned(8 downto 0)
    );
end entity signed2twoscomplement;
-- return 

architecture MyHDL of signed2twoscomplement is






begin





z <= resize(unsigned(x), 9);

end architecture MyHDL;
