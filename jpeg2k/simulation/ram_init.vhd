--
-- Initializing Block RAM from external data file
--
library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_unsigned.all;
use std.textio.all;
entity rams_20c is
port(clk : in std_logic;
    we : in std_logic;
    addr : in std_logic_vector(5 downto 0);
    din : in std_logic_vector(15 downto 0);
    dout : out std_logic_vector(15 downto 0));
end rams_20c;
architecture syn of rams_20c is

    type RamType is array(0 to 31) of bit_vector(15 downto 0);
impure function InitRamFromFile (RamFileName : in string) return RamType is
    FILE RamFile : text is in RamFileName;
    variable RamFileLine : line;
    variable leftRAM : RamType;
	 variable samRAM : RamType;
	 variable rightRAM : RamType;

begin
    for I in RamType'range loop
        readline (RamFile, RamFileLine);
        read (RamFileLine, leftRAM(I));
        end loop;
    return leftRAM;
    end function;
    signal leftRAM : RamType := InitRamFromFile("left.data");
    signal samRAM : RamType := InitRamFromFile("sam.data");
    signal rightRAM : RamType := InitRamFromFile("right.data");    
	 begin
    process (clk)
        begin
            if clk'event and clk = '1' then
        if we = '1' then
        leftRAM(conv_integer(addr)) <= to_bitvector(din);
		  samRAM(conv_integer(addr)) <= to_bitvector(din);
        rightRAM(conv_integer(addr)) <= to_bitvector(din);
        end if;
        dout <= to_stdlogicvector(leftRAM(conv_integer(addr)));
    end if;
end process;
 
 
end syn;