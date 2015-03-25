-- File: matrix_wrap.vhd
-- Generated by MyHDL 0.9dev
-- Date: Wed Mar 25 10:40:01 2015


library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
use std.textio.all;

use work.pck_myhdl_09.all;

entity matrix_wrap is
    port (
        flat: out unsigned(143 downto 0);
        z: in unsigned(8 downto 0);
        x: in signed (9 downto 0);
        mrow: in unsigned(3 downto 0);
        mcol: in unsigned(3 downto 0)
    );
end entity matrix_wrap;


architecture MyHDL of matrix_wrap is





signal mat__flat: unsigned(143 downto 0);
signal mat_mcol: unsigned(8 downto 0);

begin

mat_mcol <= to_unsigned(0, 9);

mat__flat(144-1 downto 135) <= None;
mat__flat(135-1 downto 126) <= None;
mat__flat(126-1 downto 117) <= None;
mat__flat(117-1 downto 108) <= None;
mat__flat(108-1 downto 99) <= None;
mat__flat(99-1 downto 90) <= None;
mat__flat(90-1 downto 81) <= None;
mat__flat(81-1 downto 72) <= None;
mat__flat(72-1 downto 63) <= None;
mat__flat(63-1 downto 54) <= None;
mat__flat(54-1 downto 45) <= None;
mat__flat(45-1 downto 36) <= None;
mat__flat(36-1 downto 27) <= None;
mat__flat(27-1 downto 18) <= None;
mat__flat(18-1 downto 9) <= None;
mat__flat(9-1 downto 0) <= mat_mcol(9-1 downto 0);



flat <= mat__flat;

end architecture MyHDL;
