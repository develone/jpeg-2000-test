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
use IEEE.NUMERIC_STD.ALL;
use work.pck_myhdl_09.all;
--use work.jpeg.all; 
use work.HostIoPckg.all; -- Package for PC <=> FPGA communications.

-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx primitives in this code.
library UNISIM;
use UNISIM.VComponents.all;

entity pc_fast_blinker_test_jpeg is
    Port ( clk_i : in std_logic;
          blinker_o : out  STD_LOGIC);
end pc_fast_blinker_test_jpeg;

architecture Behavioral of pc_fast_blinker_test_jpeg is

component jpeg is
    port (
        clk_fast: in std_logic;
        left_s: in signed (16 downto 0);
        right_s: in signed (16 downto 0);
        sam_s: in signed (16 downto 0);
        res_s: out signed (16 downto 0);
		  even_odd_s : in std_logic ;
		  fwd_inv_s : in std_logic
    );
end component;

  signal  clk_fast : std_logic;
  signal cnt_r : std_logic_vector(22 downto 0) := (others => '0');
  -- Connections between the shift-register module and  jpeg.
  --     50        40         30        20        10         0
  --   2109876543210987654 32109876543210987 65432109876543210
  signal fromjpeg_s : std_logic_vector(16 downto 0); -- From jpeg to PC.
  signal tojpeg_s : std_logic_vector(52 downto 0); -- From PC to jpeg.
   
  signal  even_odd_s : std_logic;
  signal  fwd_inv_s : std_logic;
  alias even_odd_tmp_s is  tojpeg_s(51);
  alias fwd_inv_tmp_s is tojpeg_s(52);
  alias right_s is tojpeg_s(16 downto 0); -- jpeg's 1st operand.
  alias left_s is tojpeg_s(33 downto 17); -- jpeg's 2nd operand.
  alias sam_s is tojpeg_s(50 downto 34); -- jpeg's 3rd operand.
  --alias res_s is fromjpeg_s; -- jpeg output.
  alias signed_res_s is signed(fromjpeg_s);
  -- Connections between the shift-register module and the subtractor.
  -- signal toSub_s : std_logic_vector(15 downto 0); -- From PC to subtrctr.
  -- signal fromSub_s : std_logic_vector(7 downto 0); -- From subtrctr to PC.
  -- alias minuend_s is toSub_s(7 downto 0); -- Subtrctr's 1st operand.
  -- alias subtrahend_s is toSub_s(15 downto 8); -- Subtrctr's 2nd oprnd.
  -- alias difference_s is fromSub_s; -- Subtractor's output.

  -- Connections between the shift-register module and the blinker.
  --signal toBlinker_s : std_logic_vector(0 downto 0); -- From PC to blnkr.
  --signal fromBlinker_s : std_logic_vector(0 downto 0); -- From blnkr to PC.
  -- Connections between JTAG entry point and the shift-register module.
  signal inShiftDr_s : std_logic; -- True when bits shift btwn PC & FPGA.
  signal drck_s : std_logic; -- Bit shift clock.
  signal tdi_s : std_logic; -- Bits from host PC to the blinker.
  signal tdo_s : std_logic; -- Bits from blinker to the host PC.
  signal tdoBlinker_s : std_logic; -- Bits from the blinker to the host PC.
  signal tdoSub_s : std_logic; -- Bits from the sbtrctr to the host PC.
begin

-------------------------------------------------------------------------
-- JTAG entry point.
-------------------------------------------------------------------------
-- Main entry point for the JTAG signals between the PC and the FPGA.
UBscanToHostIo : BscanToHostIo
  port map (
    inShiftDr_o => inShiftDr_s,
    drck_o => drck_s,
    tdi_o => tdi_s,
    tdo_i => tdo_s
    );
-------------------------------------------------------------------------
-- Shift-register.
-------------------------------------------------------------------------
-- This is the shift-register module between jpeg and JTAG entry point.
UHostIoToJpeg : HostIoToDut
  generic map (ID_G => "00000100") -- The identifier used by the PC.
    port map (
    -- Connections to the BscanToHostIo JTAG entry-point module.
    inShiftDr_i => inShiftDr_s,
    drck_i => drck_s,
    tdi_i => tdi_s,
    tdo_o => tdo_s,
    -- Connections to jpeg
    vectorToDut_o => tojpeg_s, -- From PC to jpeg sam left right.
    vectorFromDut_i => fromjpeg_s -- From jpeg to PC.
    -- Connections to the subtractor.
    -- vectorToDut_o => toSub_s, -- From PC to sbtrctr subtrahend & minuend.
    -- vectorFromDut_i => fromSub_s -- From subtractor difference to PC.

    -- Connections to the blinker.
    --vectorToDut_o => toBlinker_s, this commented out 
    -- From PC to blinker (dummy sig).
    --vectorFromDut_i => fromBlinker_s -- From blinker to PC. this commented out

   );

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
  
  even_odd_s <= even_odd_tmp_s;
  fwd_inv_s <= fwd_inv_tmp_s;
  --even_odd_s <= '1';
  --fwd_inv_s <= '1';
  ujpeg: jpeg port map(
        clk_fast => clk_fast,
        left_s => signed(left_s),
        right_s => signed(right_s),
        sam_s => signed(sam_s),
        res_s => signed_res_s,
        even_odd_s => even_odd_s,
		  fwd_inv_s => fwd_inv_s  
		  );
  
   -- This is the subtractor.
   -- difference_s <= minuend_s - subtrahend_s;
--   res_s <= (sam_s - ((left_s) + (right_s)));
   blinker_o <= cnt_r(22);
   --fromBlinker_s <= cnt_r(22 downto 22); -- Blinker output to shift reg. this commented out
end Behavioral;

