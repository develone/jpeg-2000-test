library ieee;
use ieee.std_logic_1164.all;
use std.textio.all;
use ieee.std_logic_arith.all;

use work.txt_util.all;
 
 
entity STIM_GEN2 is
   port(
        RST:  out  std_logic;
        CLK:  out  std_logic;
        X1:   out  std_logic;
        X2:   out  std_logic_vector(7 downto 0)
       );
end STIM_GEN2; 


architecture test of STIM_GEN2 is


signal i_clk: std_logic := '0';

begin

RST   <= '0', '1' after 10 ns, '0' after 30 ns;
i_clk <= not i_clk after 8 ns;
CLK   <= i_clk;


test_seq: process

variable cnt: integer := 0;
variable slv: std_logic_vector(X2'range);

begin
  
wait until i_clk = '1';

slv := conv_std_logic_vector(cnt, 8);
X2  <= slv;
X1  <= slv(4);
cnt := cnt + 1;

     
end process test_seq;


 
end test;

