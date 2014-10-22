----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date:    03:48:41 10/22/2014 
-- Design Name: 
-- Module Name:    fileio - Behavioral 
-- Project Name: 
-- Target Devices: 
-- Tool versions: 
-- Description: 
--
-- Dependencies: 
--
-- Revision: 
-- Revision 0.01 - File Created
-- Additional Comments: 
--
----------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.std_logic_textio.all;
use STD.textio.all;
-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx primitives in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity fileio is
end fileio;

architecture Behavioral of fileio is
  signal done : std_logic := '0';  -- flag set when simulation finished
begin  -- test of file_io
  done <= '1' after 5 sec;        -- probably set via logic, not time

  read_file:
    process    -- read file_io.in (one time at start of simulation)
      file my_input : TEXT open READ_MODE is "file_io.in";
      variable my_line : LINE;
      variable my_input_line : LINE;
    begin
      write(my_line, string'("reading file"));
      writeline(output, my_line);
      loop
        exit when endfile(my_input);
        readline(my_input, my_input_line);
        -- process input, possibly set up signals or arrays
        writeline(output, my_input_line);  -- optional, write to std out
      end loop;
      wait; -- one shot at time zero,
    end process read_file;

  write_file:
    process (done) is    -- write file_io.out (when done goes to '1')
      file my_output : TEXT open WRITE_MODE is "c:\Users\vidal\Documents\file_io.out";
      -- above declaration should be in architecture declarations for multiple
      variable my_line : LINE;
      variable my_output_line : LINE;
    begin
      if done='1' then
        write(my_line, string'("writing file"));
        writeline(output, my_line);
        write(my_output_line, string'("output from file_io.vhdl"));
        writeline(my_output, my_output_line);
        write(my_output_line, done);    -- or any other stuff
        writeline(my_output, my_output_line);
      end if;
    end process write_file;
--end architecture test; -- of file_io
 
end Behavioral;

