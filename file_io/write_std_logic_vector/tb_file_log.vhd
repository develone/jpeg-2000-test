
library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;


entity tb_file_log is
end tb_file_log;


architecture structure of tb_file_log is


component file_log
  generic (
           log_file:       string  := "res.log"
          );
  port(
       CLK              : in std_logic;
       RST              : in std_logic;
       x1               : in std_logic;
       x2               : in std_logic_vector(7 downto 0)
      );
end component;



component stim_gen2
   port(
        RST:  out  std_logic;
        CLK:  out  std_logic;
        X1:   out  std_logic;
        X2:   out  std_logic_vector(7 downto 0)
       );
end component;



signal RST:  std_logic;
signal CLK:  std_logic;
signal X1:  std_logic;
signal X2:  std_logic_vector(7 downto 0);


begin


U_FILE_LOG: FILE_LOG
   port map (
    CLK  => clk,
    RST  => rst,
    x1   => x1,
    x2   => x2
   );



U_STIM_GEN2: STIM_GEN2
   port map (
    RST  => rst,
    CLK  => clk,
    X1   => x1,
    X2   => x2
   );

end structure;

