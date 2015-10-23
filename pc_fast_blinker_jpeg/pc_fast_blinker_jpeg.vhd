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
use IEEE.numeric_std.all;

use work.HostIoPckg.all; -- Package for PC <=> FPGA communications.

-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx primitives in this code.
library UNISIM;
use UNISIM.VComponents.all;

entity pc_fast_blinker_jpeg is
    Port ( clk_i : in std_logic;
          blinker_o : out  STD_LOGIC);
end pc_fast_blinker_jpeg;

architecture Behavioral of pc_fast_blinker_jpeg is
  --***********signals from lift_step to lift_step*************************
  signal res_o : signed (8 downto 0) := (others => '0');
  signal flags_i : unsigned (2 downto 0) := (others => '0');
  signal left_i : unsigned (7 downto 0) := (others => '0');
  signal right_i : unsigned (7 downto 0) := (others => '0');
  signal sam_i : unsigned (7 downto 0) := (others => '0');
  signal  update_o : std_logic;
  signal  update : std_logic;
  signal z : unsigned (7 downto 0) := (others => '0');  
  
  --***********signals from lift_step to lift_step*************************
  signal lift_step_dut : std_logic_vector(7 downto 0);
  signal  clk_fast : std_logic;
  signal cnt_r : std_logic_vector(22 downto 0) := (others => '0');
  
  --***********signals from pc to pc*************************  
  signal tojpeg_s : std_logic_vector(26 downto 0); -- From PC to jpeg.
  signal fromjpeg_s : std_logic_vector(7 downto 0); -- From jpeg to PC.
  alias left_s is tojpeg_s(7 downto 0); -- left.
  alias sam_s is tojpeg_s(15 downto 8); -- sam.
  alias right_s is tojpeg_s(23 downto 16); -- sam.
  alias flags_s is tojpeg_s(26 downto 24);
  alias lifting_step_s is fromjpeg_s; -- lift_step output.
  --***********signals from pc to pc*************************
  
  --alias update_s is tojpeg_s(28 downto 28);
  
  
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
  constant YES                    : std_logic := '1';
  constant NO                    : std_logic := '0';
  component lift_step is
    port (
	     flags_i: in unsigned(2 downto 0);
		  update_i : in std_logic;
        left_i: in unsigned(7 downto 0);
        sam_i: in unsigned(7 downto 0);
        right_i: in unsigned(7 downto 0);
        res_o: out signed (8 downto 0);
		  update_o : out std_logic;
        clk_i: in std_logic
    );
  end component;
  
  component signed2twoscomplement is
    port (
	     clk: in std_logic;
        res_o: in signed (8 downto 0);
        z: out unsigned(7 downto 0)
     );
  end component;
  
begin
   update <= YES;
   ulift_step : lift_step 
       port map(
	       flags_i => unsigned(flags_s),
		    update_i => update,
          left_i => unsigned(left_s),
          sam_i => unsigned(sam_s),
          right_i => unsigned(right_s),
          res_o => res_o,
		    update_o => update_o,
          clk_i => clk_fast
	);
	
	usigned2twoscomplement : signed2twoscomplement
	    port map(
          clk => clk_fast,
          res_o => res_o,
          z => z
       );			 
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
UHostIoToJpeg : HostIoToDut
  generic map (ID_G => "00000100") -- The identifier used by the PC.
    port map (
    -- Connections to the BscanToHostIo JTAG entry-point module.
    inShiftDr_i => inShiftDr_s,
    drck_i => drck_s,
    tdi_i => tdi_s,
    tdo_o => tdo_s,
    -- Connections to the lift_step.
    vectorToDut_o => tojpeg_s, -- From PC to lift_step left sam right.
    vectorFromDut_i => fromjpeg_s -- From lift_step to PC.

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
   -- This is iifting_step.
	 
  lift_step_dut <= std_logic_vector(unsigned(z));
  lifting_step_s <= lift_step_dut;
  --lifting_step_s <= z;
  blinker_o <= cnt_r(22);
   
end Behavioral;

