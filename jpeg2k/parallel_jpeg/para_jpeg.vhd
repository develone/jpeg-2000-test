----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date:    14:07:35 01/21/2015 
-- Design Name: 
-- Module Name:    para_jpeg - Behavioral 
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
use IEEE.NUMERIC_STD.all;
use work.pck_myhdl_09.all;
use work.pck_xess_jpeg_para.all;
-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx primitives in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity para_jpeg is
  port (Clk_i : in    std_logic);
  end  entity para_jpeg;

architecture Behavioral of para_jpeg is 
  signal state_r, state_x         : t_enum_t_State_1   := INIT;  -- FSM starts off in init state.
  signal sig_in_r,sig_in_x : unsigned(30 downto 0) := (others => '0');
  signal noupdate_s : std_logic;
 
 
  signal res_s : signed(8 downto 0) := (others => '0');
 
  signal dout_rom : unsigned(30 downto 0):= (others => '0');
  signal  addr_rom_r, addr_rom_x : unsigned(16 downto 0):= (others => '0');
 

  component xess_jpeg_para is
    port (
        clk_fast: in std_logic;
        state_r: inout t_enum_t_State_1;
        state_x: inout t_enum_t_State_1;
        sig_in_r: inout unsigned(30 downto 0);
        sig_in_x: inout unsigned(30 downto 0);
        noupdate_s: out std_logic;
        res_s: out signed (8 downto 0);
        dout_rom: inout unsigned(30 downto 0);
        addr_rom_r: inout unsigned(16 downto 0);
        addr_rom_x: inout unsigned(16 downto 0)
    );
end component xess_jpeg_para;

begin
xess_jpeg_para_u0 : xess_jpeg_para
  port map(
   clk_fast => Clk_i,
   sig_in_r => sig_in_r,
	sig_in_x => sig_in_x,
   noupdate_s => noupdate_s,
   res_s => res_s,
   state_r => state_r,
	state_x => state_x,
	dout_rom => dout_rom,
	addr_rom_r => addr_rom_r,
	addr_rom_x => addr_rom_x
);

end Behavioral;

