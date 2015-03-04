-- File: tounsigned.vhd
-- Generated by MyHDL 0.9dev
-- Date: Wed Mar  4 14:25:08 2015


library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
use std.textio.all;

use work.pck_myhdl_09.all;

entity tounsigned is
    port (
        bits_in: in signed (9 downto 0);
        v: out unsigned(9 downto 0)
    );
end entity tounsigned;
-- return an unsigned value to represent a possibly 'signed' value

architecture MyHDL of tounsigned is


constant w: integer := 10;




begin




TOUNSIGNED_UNSIGNED_LOGIC: process (bits_in) is
begin
    if (bits_in >= 0) then
        v <= unsigned(bits_in);
    else
        v <= unsigned((2 ** w) + bits_in);
    end if;
end process TOUNSIGNED_UNSIGNED_LOGIC;

end architecture MyHDL;