library ieee;
use ieee.std_logic_1164.all;

use std.textio.all;
use work.txt_util.all;
 
 
entity FILE_LOG is
  generic (
           log_file:       string  := "res.log"
          );
  port(
       CLK              : in std_logic;
       RST              : in std_logic;
       x1               : in std_logic;
       x2               : in std_logic_vector(7 downto 0)
      );
end FILE_LOG;
   
   
architecture log_to_file of FILE_LOG is
  
  
    file l_file: TEXT open write_mode is log_file;


begin



-- write data and control information to a file

receive_data: process

variable l: line;
   
begin                                       

   -- print header for the logfile
   print(l_file, "#  x1   x2 ");
   print(l_file, "#----------");
   print(l_file, " ");


   wait until RST='1';
   wait until RST='0';

   
   while true loop

     -- write digital data into log file
     --* write(l, str(x1)& " "& hstr(x2)& "h");
     --* writeline(l_file, l);
     print(l_file, str(x1)& " "& hstr(x2)& "h");

     wait until CLK = '1';
    
   end loop;

 end process receive_data;



end log_to_file;
 
