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
use work.HostIoPckg.all; -- Package for PC <=> FPGA communications.

-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx primitives in this code.
library UNISIM;
use UNISIM.VComponents.all;

entity ram_rd is
    Port ( clk_i : in std_logic;
          blinker_o : out  STD_LOGIC);
end ram_rd;

architecture Behavioral of ram_rd is
  signal  clk_fast : std_logic;
  signal cnt_r : std_logic_vector(22 downto 0) := (others => '0');
  -- Connections between the shift-register module and the subtractor.
  signal toSub_s : std_logic_vector(15 downto 0); -- From PC to subtrctr.
  signal fromSub_s : std_logic_vector(7 downto 0); -- From subtrctr to PC.
  alias minuend_s is toSub_s(7 downto 0); -- Subtrctr's 1st operand.
  alias subtrahend_s is toSub_s(15 downto 8); -- Subtrctr's 2nd oprnd.
  alias difference_s is fromSub_s; -- Subtractor's output.

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
-- This is the shift-register module between blinker and JTAG entry point.
UHostIoToSubtracter : HostIoToDut
  generic map (ID_G => "00000100") -- The identifier used by the PC.
    port map (
    -- Connections to the BscanToHostIo JTAG entry-point module.
    inShiftDr_i => inShiftDr_s,
    drck_i => drck_s,
    tdi_i => tdi_s,
    tdo_o => tdo_s,
    -- Connections to the subtractor.
    vectorToDut_o => toSub_s, -- From PC to sbtrctr subtrahend & minuend.
    vectorFromDut_i => fromSub_s -- From subtractor difference to PC.

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
   -- This is the subtractor.
   difference_s <= minuend_s - subtrahend_s;
   blinker_o <= cnt_r(22);
   --fromBlinker_s <= cnt_r(22 downto 22); -- Blinker output to shift reg. this commented out
end Behavioral;

