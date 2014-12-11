--------------------------------------------------------------------------------
-- Company: 
-- Engineer:
--
-- Create Date:   13:37:43 01/03/2013
-- Design Name:   
-- Module Name:   C:/xesscorp/PRODUCTS/TUTORIALS/FpgasNowWhat/Chapters/Verilog/FPGA/SdramSPInst/SdramSPInstTb.vhd
-- Project Name:  SdramSPInst
-- Target Device:  
-- Tool versions:  
-- Description:   
-- 
-- VHDL Test Bench Created by ISE for module: SdramSPInst
-- 
-- Dependencies:
-- 
-- Revision:
-- Revision 0.01 - File Created
-- Additional Comments:
--
-- Notes: 
-- This testbench has been automatically generated using types std_logic and
-- std_logic_vector for the ports of the unit under test.  Xilinx recommends
-- that these types always be used for the top-level I/O of a design in order
-- to guarantee that the testbench will bind correctly to the post-implementation 
-- simulation model.
--------------------------------------------------------------------------------
LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
use IEEE.NUMERIC_STD.all;
use work.ClkgenPckg.all;     -- For the clock generator module.
use work.SdramCntlPckg.all;  -- For the SDRAM controller module.
use work.HostIoPckg.HostIoToDut;     -- For the FPGA<=>PC transfer link module.
 
use work.pck_myhdl_09.all;
use work.pck_xess_jpeg_top.all; 
-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--USE ieee.numeric_std.ALL;
 
ENTITY XESS_SdramSPInstTb IS
END XESS_SdramSPInstTb;
 
ARCHITECTURE behavior OF XESS_SdramSPInstTb IS 
 
    -- Component Declaration for the Unit Under Test (UUT)
 
    COMPONENT XESS_SdramSPInst
    PORT(
         fpgaClk_i : IN  std_logic;
         sdClk_o : OUT  std_logic;
         sdClkFb_i : IN  std_logic;
         sdCke_o   : OUT   std_logic;  -- SDRAM clock enable.
         sdCe_bo   : OUT   std_logic;  -- SDRAM chip-enable.
         sdRas_bo : OUT  std_logic;
         sdCas_bo : OUT  std_logic;
         sdWe_bo : OUT  std_logic;
         sdBs_o    : OUT   std_logic_vector(1 downto 0);  -- 2-bit SDRAM bank-address.
         sdAddr_o : OUT  std_logic_vector(11 downto 0); -- 13-bit SDRAM address bus.
         sdData_io : INOUT  std_logic_vector(15 downto 0);
         sdDqmh_o  : OUT   std_logic;  -- SDRAM high-byte databus qualifier.
         sdDqml_o  : OUT   std_logic  -- SDRAM low-byte databus qualifier.
        );
    END COMPONENT;

    -- Take the SDRAM module I/O description from mt48lc8m16a2.v Verilog file
    --    module mt48lc8m16a2 (Dq, Addr, Ba, Clk, Cke, Cs_n, Ras_n, Cas_n, We_n, Dqm);
    -- and convert it into a VHDL component declaration like this:
    
    component mt48lc8m16a2 
    port(
      Dq : inout std_logic_vector(15 downto 0);
      Addr : in std_logic_vector(11 downto 0); 
      Ba : in std_logic_vector(1 downto 0); 
      Clk : in std_logic; 
      Cke : in std_logic;
      Cs_n : in std_logic;
      Ras_n : in std_logic;
      Cas_n : in std_logic;
      We_n : in std_logic;
      Dqm : in std_logic_vector(1 downto 0)
      );
    end component;
    

   --Inputs
   signal fpgaClk_i : std_logic := '0';
   signal sdClkFb_i : std_logic := '0';

	--BiDirs
   signal sdData_io : std_logic_vector(15 downto 0);

 	--Outputs
   signal sdClk_o : std_logic;
   signal sdCke_o : std_logic;
   signal sdCe_bo : std_logic;
   signal sdRas_bo : std_logic;
   signal sdCas_bo : std_logic;
   signal sdWe_bo : std_logic;
   signal sdBs_o : std_logic_vector(1 downto 0);
   signal sdAddr_o : std_logic_vector(11 downto 0);
   signal sdDqmh_o : std_logic;
   signal sdDqml_o : std_logic;
   -- No clocks detected in port list. Replace <clock> below with 
   -- appropriate port name 
 
   constant fpgaClk_period : time := 83.3333 ns; -- 12 MHz XuLA clock.
--signal needed by XESS_SdramSPinst.vhd and xess_jpeg_top.vhd*************************** 
  signal clk_s                    : std_logic;  -- Internal clock.
  signal sumDut_s                 : std_logic_vector(38 downto 0);  -- Send sum back to PC.
  alias fromsdramdataDut_s is sumDut_s(38 downto 23);
  alias fromsdramaddrDut_s is sumDut_s(22 downto 0);
  signal nullDutOut_s             : std_logic_vector(0 downto 0);  -- Dummy output for HostIo module.
  signal dataFromSdram_s          : std_logic_vector(sdData_io'range);  -- Data.
  signal addrSdram_s              : unsigned(22 downto 0);  -- Address.
  signal dataToSdram_s            : unsigned(15 downto 0);  -- Data.
  signal dataFromRam_r, dataFromRam_r1, dataFromRam_r2  : unsigned(15 downto 0); 
  signal sum_r, sum_x             : unsigned( 15 downto 0);
  signal wr_s                     : std_logic;  -- Write-enable control.
  signal rd_s                     : std_logic;  -- Read-enable control.
  signal done_s                   : std_logic;  -- SDRAM R/W operation done signal.
  signal addr_r, addr_x           : unsigned(22 downto 0);  -- RAM address.
  signal addr_r1, addr_r2           : unsigned(22 downto 0);  -- RAM address.
  signal dataToRam_r, dataToRam_x, dataFromRam_s : unsigned(15 downto 0);  -- Data to write to RAM.
--signal needed by XESS_SdramSPinst.vhd and xess_jpeg_top.vhd***************************

----signal needed by xess_jpeg_top.vhd***************************
--  signal state_r, state_x         : t_enum_t_State_1   := INIT;  -- FSM starts off in init state.
--  signal sig_in : unsigned(51 downto 0) := (others => '0');
--  signal noupdate_s : std_logic;
--  signal res_s : signed(15 downto 0) := (others => '0');
--  signal jp_lf : unsigned(15 downto 0) := (others => '0');
--  signal jp_sa: unsigned(15 downto 0) := (others => '0');
--  signal jp_rh : unsigned(15 downto 0) := (others => '0');
--  signal jp_flgs : unsigned(3 downto 0) := (others => '0');
--  signal reset_col : std_logic := '1';
--  signal rdy : std_logic := '1';
--  signal addr_not_reached : std_logic := '0';
--  signal offset           : unsigned(22 downto 0);  -- RAM address.
--  signal muxsel  : std_logic :=  '0';
----signal needed by xess_jpeg_top.vhd***************************
--component xess_jpeg_top is
--    port (
--        clk_fast: in std_logic;
--        addr_r: out unsigned(22 downto 0);
--        addr_x: in unsigned(22 downto 0);
--		  state_r: inout t_enum_t_State_1;
--        state_x: inout t_enum_t_State_1;
--        addr_r1: inout unsigned(22 downto 0);
--        addr_r2: inout unsigned(22 downto 0);
--        muxsel: in std_logic;
--        dataToRam_r: out unsigned(15 downto 0);
--        dataToRam_x: in unsigned(15 downto 0);
--		  dataFromRam_r: out unsigned(15 downto 0);
--        dataFromRam_r1: inout unsigned(15 downto 0);
--        dataFromRam_r2: in unsigned(15 downto 0);
--        sig_in: inout unsigned(51 downto 0);
--        noupdate_s: out std_logic;
--        res_s: out signed (15 downto 0);
--        jp_lf: inout unsigned(15 downto 0);
--        jp_sa: inout unsigned(15 downto 0);
--        jp_rh: inout unsigned(15 downto 0);
--        jp_flgs: in unsigned(3 downto 0);
--		  reset_col: in std_logic;
--        rdy: in std_logic;
--        addr_not_reached: inout std_logic;
--		  offset: in unsigned(22 downto 0);
--        dataFromRam_s: in unsigned(15 downto 0);
--        done_s: in std_logic;
--        wr_s: out std_logic;
--        rd_s: out std_logic;
--        sum_r: inout unsigned(15 downto 0);
--        sum_x: inout unsigned(15 downto 0)
-- 	  
--    );
--end component xess_jpeg_top; 
BEGIN
--muxsel <= '0';
--  --*********************************************************************
--  -- Instantiate the jpeg_top step1JPEG_TOP_INSTANCE_7_FSMUPDATE
--  -- updates signals for the FSM.
--  --*********************************************************************
--xess_jpeg_top_u0 : xess_jpeg_top
--  port map (
--     clk_fast => clk_s,
--	  addr_r => addr_r,
--	  addr_x => addr_x,
--	  state_r => state_r,
--	  state_x => state_x,
--	  addr_r1 => addr_r1,
--     addr_r2 => addr_r2,
--	  muxsel => muxsel,
--	  dataToRam_r => dataToRam_r,
--	  dataToRam_x => dataToRam_x,
--	  dataFromRam_r =>  dataFromRam_r,
--	  dataFromRam_r1 =>  dataFromRam_r1,
--	  dataFromRam_r2  => dataFromRam_r2,
--	  sig_in => sig_in,
--	  noupdate_s => noupdate_s,
--	  res_s => res_s,
--	  jp_lf => jp_lf,
--	  jp_sa => jp_sa,
--	  jp_rh => jp_rh,
--	  jp_flgs => jp_flgs,
--	  reset_col => reset_col,
--	  rdy => rdy,
--	  addr_not_reached => addr_not_reached,
--     offset => offset,
--     dataFromRam_s => dataFromRam_s,
--	  done_s => done_s,
--	  wr_s => wr_s,
--	  rd_s => rd_s,
--	  sum_r => sum_r,
--	  sum_x => sum_x
--   
--  ); 
	-- Instantiate the Unit Under Test (UUT)
   uut: XESS_SdramSPInst PORT MAP (
          fpgaClk_i => fpgaClk_i, -- 12 MHz XuLA clock.
          sdClk_o => sdClk_o, -- 100 MHz clock from DCM.
          sdClkFb_i => sdClkFb_i, -- 100 MHz clock fed back into FPGA.
          sdCke_o => sdCke_o,  -- SDRAM clock enable.
          sdCe_bo => sdCe_bo,  -- SDRAM chip-enable.
          sdRas_bo => sdRas_bo, -- Row-address strobe.
          sdCas_bo => sdCas_bo, -- Column-address strobe.
          sdWe_bo => sdWe_bo, -- Write-enable.
          sdBs_o => sdBs_o, -- Bank-select.
          sdAddr_o => sdAddr_o, -- 12-bit address bus.
          sdData_io => sdData_io, -- 16-bit data bus.
          sdDqmh_o => sdDqmh_o,  -- SDRAM high-byte databus qualifier.
          sdDqml_o => sdDqml_o  -- SDRAM low-byte databus qualifier.
        );
   sdClkFb_i <= sdClk_o; -- Feedback 100 MHz clock to FPGA.
        
    -- Use the mt48lc8m16a2 declaration from above to instantiate
    -- the SDRAM here and connect it to the UUT.
   sdram: mt48lc8m16a2 port map(
     Dq => sdData_io,  -- 16-bit data bus.
     Addr => sdAddr_o,  -- 12-bit address bus.
     Ba => sdBs_o,  -- Bank-select pins.
     Clk => sdClk_o,  -- 100 MHz clock.
     Cke => sdCke_o,  -- Clock-enable.
     Cs_n => sdCe_bo, -- Chip-enable.
     Ras_n => sdRas_bo, -- Row-address strobe.
     Cas_n => sdCas_bo, -- Column-address strobe.
     We_n => sdWe_bo, -- Write-enable.
     Dqm(0) => sdDqml_o, -- Lower-byte databus qualifier.
     Dqm(1) => sdDqmh_o  -- Upper-byte databus qualifier.
     );

   -- Clock process definitions.
   -- This generates the 12 MHz clock.
   fpgaClk_process :process
   begin
		fpgaClk_i <= '0';
		wait for fpgaClk_period/2;
		fpgaClk_i <= '1';
		wait for fpgaClk_period/2;
   end process;
 

   -- Stimulus process.
   -- This is not used in this testbench. The FSM in the
   -- UUT steps through all the operations.
   stim_proc: process
   begin		
      -- hold reset state for 100 ns.
      wait for 100 ns;	

      wait for fpgaClk_period*10;

      -- insert stimulus here 

      wait;
   end process;

END;
