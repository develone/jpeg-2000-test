----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date:    15:20:09 08/08/2014 
-- Design Name: 
-- Module Name:    blinker - Behavioral 
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
use IEEE.STD_LOGIC_UNSIGNED.ALL;

-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx primitives in this code.
library UNISIM;
use UNISIM.VComponents.all;

entity fast_blinker is
    Port ( clk_i : in std_logic;
          blinker_o : out  STD_LOGIC);
end fast_blinker;

architecture Behavioral of fast_blinker is
  signal  clk_fast : std_logic;
  signal cnt_r : std_logic_vector(22 downto 0) := (others => '0');
begin
   -- DCM_SP: Digital Clock Manager
   --         Spartan-6
   -- Xilinx HDL Language Template, version 14.6

  DCM_SP_inst : DCM_SP
   generic map (
   
      CLKFX_DIVIDE => 1,                     -- Divide value on CLKFX outputs - D - (1-32)
      CLKFX_MULTIPLY => 10                   -- Multiply value on CLKFX outputs - M - (2-32)
  
   )
   port map (
		CLKFX => clk_fast,		-- 1-bit output: Digital Frequency Synthesizer output (DFS)
		CLKIN => clk_i, 
		RST => '0'            -- 1-bit input: Active high reset input	
       
   );



  
	process(clk_fast) is
	begin
		if rising_edge(clk_fast) then
			cnt_r <= cnt_r + 1;
		end if;
	end process;

   blinker_o <= cnt_r(22);

end Behavioral;

