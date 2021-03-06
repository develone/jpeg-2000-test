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
library IEEE,XESS;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;
--use XESS.HostIoCommPckg.all; -- Package for PC <=> FPGA communications.
use XESS.HostIoPckg.all; -- Package for PC <=> FPGA communications.
use IEEE.numeric_std.all;
use std.textio.all;

use work.pck_myhdl_090.all;
-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx primitives in this code.
library UNISIM;
use UNISIM.VComponents.all;

entity test_lifting_jpeg_step_lib is
    Port ( clk_i : in std_logic;
          blinker_o : out  STD_LOGIC);
end test_lifting_jpeg_step_lib;

architecture Behavioral of test_lifting_jpeg_step_lib is
  signal  clk_fast : std_logic;
  signal cnt_r : std_logic_vector(22 downto 0) := (others => '0');
  -- Connections between the shift-register module and the pc_read.
  
  signal toSub_s : std_logic_vector(20 downto 0); -- From PC to dut
  signal fromSub_s : std_logic_vector(10 downto 0); -- From dut to PC.
  
  alias datatodut is toSub_s(8 downto 0); 
  alias pc_data_rdy is toSub_s(10 downto 9);   
  alias addr_in_toLift_Step is toSub_s(18 downto 11); 
  alias fifo_wr is toSub_s(19);
  alias fifo_rd is toSub_s(19);  
  alias datafromdut is fromSub_s(8 downto 0); 
  alias status_s is fromSub_s(10 downto 9);

  -- Connections between JTAG entry point and the shift-register module.
  signal inShiftDr_s : std_logic; -- True when bits shift btwn PC & FPGA.
  signal drck_s : std_logic; -- Bit shift clock.
  signal tdi_s : std_logic; -- Bits from host PC to the blinker.
  signal tdo_s : std_logic; -- Bits from blinker to the host PC.
  
--  signal tdoBlinker_s : std_logic; -- Bits from the blinker to the host PC.
--  signal tdoSub_s : std_logic; -- Bits from the sbtrctr to the host PC.
  
  signal pc_data_i: std_logic:= '0';
  signal data_in : unsigned(8 downto 0) := (others => '0');
  
  signal  clk : std_logic;
  signal  we_in : std_logic := '0';
  signal  muxsel_i : std_logic := '0';
  signal  read_pc_i : std_logic := '0';
  signal addr_in :  unsigned(7  downto 0) := (others => '0');
  signal  datactn_in : unsigned(7  downto 0) := (others => '0');
  signal  pc_data_in : unsigned(1  downto 0) := (others => '0');

--   signal clk : std_logic := '0';
--   signal enr_r : std_logic := '0';
--   signal enw_r : std_logic := '0';
   signal datain_r : unsigned(8 downto 0) := (others => '0');

 	--Outputs
   signal empty_r : std_logic;
   signal full_r : std_logic;
   signal dataout_r : unsigned(8 downto 0);
  
  COMPONENT pc_read  
    port (
        clk: in std_logic;
        data_in: out unsigned(8 downto 0);
        toLift_Step: in unsigned(8 downto 0);
        addr_in: out unsigned(7 downto 0);
        addr_in_toLift_Step: in unsigned(7 downto 0);
        read_pc_i: in std_logic;
        muxsel_i: in std_logic;
        pc_data_in: out unsigned(1 downto 0);
        pc_data_rdy: in unsigned(1 downto 0);
        we_in: out std_logic
    );
END COMPONENT;

    COMPONENT fifo
    PORT(
         clk : IN  std_logic;
         empty_r : OUT  std_logic;
         full_r : OUT  std_logic;
         enr_r : IN  std_logic;
         enw_r : IN  std_logic;
         dataout_r : OUT  unsigned(8 downto 0);
         datain_r : IN  unsigned(8 downto 0)
        );
    END COMPONENT; 
	 
begin

read_pc_i <= '1';
muxsel_i <= '1';

u1 : pc_read 
	PORT MAP (
	  clk => clk_fast,
	  data_in => data_in,
	  toLift_Step => unsigned(datatodut),
	  addr_in => addr_in,
	  addr_in_toLift_Step => unsigned(addr_in_toLift_Step),
	  read_pc_i => read_pc_i,
	  muxsel_i => muxsel_i,
 	  pc_data_in => pc_data_in,
	  pc_data_rdy => unsigned(pc_data_rdy),	  
     we_in => we_in
	  );   
	  
	  u2: fifo PORT MAP (
          clk => clk_fast,
          empty_r => empty_r,
          full_r => full_r,
          enr_r => fifo_rd,
          enw_r => fifo_wr,
          dataout_r => (dataout_r),
          datain_r => unsigned(datatodut)
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
---------------------------------------------------------------------------
---- Shift-register.
---------------------------------------------------------------------------
---- This is the shift-register module between blinker and JTAG entry point.
UHostIoToSubtracter : HostIoToDut
  generic map (ID_G => "00000100") -- The identifier used by the PC.
    port map (
    -- Connections to the BscanToHostIo JTAG entry-point module.
    inShiftDr_i => inShiftDr_s,
    drck_i => drck_s,
    tdi_i => tdi_s,
    tdo_o => tdo_s,
    -- Connections to the subtractor.
    vectorToDut_o => toSub_s, -- From PC to pc_read
    vectorFromDut_i => fromSub_s -- From pc_read to PC.
   );

   -- DCM_SP: Digital Clock Manager
   --         Spartan-6
   -- Xilinx HDL Language Template, version 14.6

  DCM_SP_inst : DCM_SP
   generic map (
   
      CLKFX_DIVIDE => 3,                     -- Divide value on CLKFX outputs - D - (1-32)
      CLKFX_MULTIPLY => 25                   -- Multiply value on CLKFX outputs - M - (2-32)
  
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
 
	 
	datafromdut <= datatodut;
	status_s <= std_logic_vector(pc_data_in);
 
   blinker_o <= cnt_r(22);
 
   --fromBlinker_s <= cnt_r(22 downto 22); -- Blinker output to shift reg. this commented out
end Behavioral;

