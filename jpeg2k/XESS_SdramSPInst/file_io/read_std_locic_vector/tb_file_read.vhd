
library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_arith.all;
--use IEEE.NUMERIC_STD.all;

entity TB_FILE_READ is
end TB_FILE_READ;

architecture test of TB_FILE_READ is


component FILE_READ 
  generic (
           stim_file:       string  := "sim.dat"
          );
  port(
        CLK              : in  std_logic;
       RST              : in  std_logic;
       Y                : inout std_logic_vector(15 downto 0);
--		 Y_u                : inout unsigned(15 downto 0);
       EOG              : out std_logic
      );
end component;


signal rst:  std_logic;
signal clk:  std_logic := '0';
signal eog:  std_logic;
signal y:    std_logic_vector(15 downto 0);
--signal y_u:    unsigned(15 downto 0);
begin

          
rst <= '0', '1' after 40 ns, '0' after 100 ns;    
clk <= not clk after 10 ns;


input_stim: FILE_READ 
  port map(
       CLK      => clk,
       RST      => rst,
       Y        => y,
--		 Y_u      => y_u,
       EOG      => eog
      );


end test;



