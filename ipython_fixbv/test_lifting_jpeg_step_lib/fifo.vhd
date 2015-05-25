-- File: fifo.vhd
-- Generated by MyHDL 0.9.dev0
-- Date: Mon May 25 11:44:30 2015


library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
use std.textio.all;

use work.pck_myhdl_090.all;

entity fifo is
    port (
        clk: in std_logic;
        empty_r: out std_logic;
        full_r: out std_logic;
        enr_r: in std_logic;
        enw_r: in std_logic;
        dataout_r: out unsigned(8 downto 0);
        datain_r: in unsigned(8 downto 0)
    );
end entity fifo;
-- The following between the single quotes ':= "0000"' needs to added to line below
-- signal instance_1_reset_ctn: unsigned(3 downto 0);
-- before the ';' to be like the following
-- signal instance_1_reset_ctn: unsigned(3 downto 0):= "0000";
--  

architecture MyHDL of fifo is


constant ASZ: integer := 8;
constant YES: integer := 1;
constant reset_dly_c: integer := 10;
constant NO: integer := 0;



signal reset_ctn: unsigned(3 downto 0):= "0000";
signal readptr: unsigned(7 downto 0);
signal writeptr: unsigned(7 downto 0);
type t_array_mem is array(0 to 256-1) of unsigned(8 downto 0);
signal mem: t_array_mem;

begin




FIFO_RTL: process (clk) is
begin
    if rising_edge(clk) then
        if (reset_ctn < reset_dly_c) then
            readptr <= to_unsigned(0, 8);
            writeptr <= to_unsigned(0, 8);
            reset_ctn <= (reset_ctn + 1);
        end if;
        if (enr_r = '1') then
            dataout_r <= mem(to_integer(readptr));
            if (signed(resize(readptr, 9)) < ((2 ** ASZ) - 1)) then
                readptr <= (readptr + 1);
            end if;
        end if;
        if (enw_r = '1') then
            mem(to_integer(writeptr)) <= datain_r;
            writeptr <= (writeptr + 1);
        end if;
        if (signed(resize(readptr, 9)) = ((2 ** ASZ) - 1)) then
            readptr <= to_unsigned(0, 8);
        end if;
        if (signed(resize(writeptr, 9)) = ((2 ** ASZ) - 1)) then
            full_r <= '1';
            writeptr <= to_unsigned(0, 8);
        else
            full_r <= '0';
        end if;
        if (writeptr = 0) then
            empty_r <= '1';
        else
            empty_r <= '0';
        end if;
    end if;
end process FIFO_RTL;

end architecture MyHDL;
