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
 
-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx primitives in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity para_multi_jpeg is
  port (Clk_i : in    std_logic);
  end  entity para_multi_jpeg;

architecture Behavioral of para_multi_jpeg is 
  --Signals needed for multi_jpeg_u0 : multi_jpeg
  signal sig0_in_x,sig1_in_x, sig2_in_x,sig3_in_x : unsigned(30 downto 0) := (others => '0');
  signal noupdate0_s, noupdate1_s, noupdate2_s, noupdate3_s : std_logic;
  signal res0_s, res1_s, res2_s, res3_s : signed(10 downto 0) := (others => '0');
 
 
  signal sig4_in_x,sig5_in_x, sig6_in_x,sig7_in_x :unsigned(30 downto 0) := (others => '0');
  signal noupdate4_s, noupdate5_s, noupdate6_s, noupdate7_s : std_logic;
  signal res4_s, res5_s, res6_s, res7_s : signed(10 downto 0) := (others => '0');

  signal sig8_in_x,sig9_in_x, sig10_in_x,sig11_in_x : unsigned(30 downto 0) := (others => '0');
  signal noupdate8_s, noupdate9_s, noupdate10_s, noupdate11_s : std_logic;
  signal res8_s, res9_s, res10_s, res11_s : signed(10 downto 0) := (others => '0');
 
 
  signal sig12_in_x,sig13_in_x, sig14_in_x,sig15_in_x :unsigned(30 downto 0) := (others => '0');
  signal noupdate12_s, noupdate13_s, noupdate14_s, noupdate15_s : std_logic;
  signal res12_s, res13_s, res14_s, res15_s : signed(10 downto 0) := (others => '0');  

  component multi_jpeg is
    port (
        clk_fast: in std_logic;
        sig0_in_x: in unsigned(30 downto 0);
        noupdate0_s: out std_logic;
        res0_s: out signed (10 downto 0);
        sig1_in_x: in unsigned(30 downto 0);
        noupdate1_s: out std_logic;
        res1_s: out signed (10 downto 0);
        sig2_in_x: in unsigned(30 downto 0);
        noupdate2_s: out std_logic;
        res2_s: out signed (10 downto 0);
        sig3_in_x: in unsigned(30 downto 0);
        noupdate3_s: out std_logic;
        res3_s: out signed (10 downto 0);
        sig4_in_x: in unsigned(30 downto 0);
        noupdate4_s: out std_logic;
        res4_s: out signed (10 downto 0);
        sig5_in_x: in unsigned(30 downto 0);
        noupdate5_s: out std_logic;
        res5_s: out signed (10 downto 0);
        sig6_in_x: in unsigned(30 downto 0);
        noupdate6_s: out std_logic;
        res6_s: out signed (10 downto 0);
        sig7_in_x: in unsigned(30 downto 0);
        noupdate7_s: out std_logic;
        res7_s: out signed (10 downto 0);
        sig8_in_x: in unsigned(30 downto 0);
        noupdate8_s: out std_logic;
        res8_s: out signed (10 downto 0);
        sig9_in_x: in unsigned(30 downto 0);
        noupdate9_s: out std_logic;
        res9_s: out signed (10 downto 0);
        sig10_in_x: in unsigned(30 downto 0);
        noupdate10_s: out std_logic;
        res10_s: out signed (10 downto 0);
        sig11_in_x: in unsigned(30 downto 0);
        noupdate11_s: out std_logic;
        res11_s: out signed (10 downto 0);
        sig12_in_x: in unsigned(30 downto 0);
        noupdate12_s: out std_logic;
        res12_s: out signed (10 downto 0);
        sig13_in_x: in unsigned(30 downto 0);
        noupdate13_s: out std_logic;
        res13_s: out signed (10 downto 0);
        sig14_in_x: in unsigned(30 downto 0);
        noupdate14_s: out std_logic;
        res14_s: out signed (10 downto 0);
        sig15_in_x: in unsigned(30 downto 0);
        noupdate15_s: out std_logic;
        res15_s: out signed (10 downto 0)
    );
end component multi_jpeg;

begin
multi_jpeg_u0 : multi_jpeg
  port map(
   clk_fast => Clk_i,
	sig0_in_x => sig0_in_x,
   noupdate0_s => noupdate0_s,
   res0_s => res0_s,
 
	sig1_in_x => sig1_in_x,
   noupdate1_s => noupdate1_s,
   res1_s => res1_s,

 
 
	sig2_in_x => sig2_in_x,
   noupdate2_s => noupdate2_s,
   res2_s => res2_s,
 
	
	sig3_in_x => sig3_in_x,
   noupdate3_s => noupdate3_s,
   res3_s => res3_s,
 


	sig4_in_x => sig4_in_x,
   noupdate4_s => noupdate4_s,
   res4_s => res4_s,
 
	
	sig5_in_x => sig5_in_x,
   noupdate5_s => noupdate5_s,
   res5_s => res5_s,
 
 
	sig6_in_x => sig6_in_x,
   noupdate6_s => noupdate6_s,
   res6_s => res6_s,
 
	
	sig7_in_x => sig7_in_x,
   noupdate7_s => noupdate7_s,
   res7_s => res7_s,
 
	
	sig8_in_x => sig8_in_x,
   noupdate8_s => noupdate8_s,
   res8_s => res8_s,
 
	
	sig9_in_x => sig9_in_x,
   noupdate9_s => noupdate9_s,
   res9_s => res9_s,
 
 
	sig10_in_x => sig10_in_x,
   noupdate10_s => noupdate10_s,
   res10_s => res10_s,
 
	
	sig11_in_x => sig11_in_x,
   noupdate11_s => noupdate11_s,
   res11_s => res11_s,
 

	sig12_in_x => sig12_in_x,
   noupdate12_s => noupdate12_s,
   res12_s => res12_s,
 	
	sig13_in_x => sig13_in_x,
   noupdate13_s => noupdate13_s,
   res13_s => res13_s,
 
 
	sig14_in_x => sig14_in_x,
   noupdate14_s => noupdate14_s,
   res14_s => res14_s,
 
	
	sig15_in_x => sig15_in_x,
   noupdate15_s => noupdate15_s,
   res15_s => res15_s
);
 
end Behavioral;

