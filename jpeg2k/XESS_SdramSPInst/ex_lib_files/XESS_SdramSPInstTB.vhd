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
  constant NO                     : std_logic := '0';
  constant YES                    : std_logic := '1';
  --00_0000 to 03_FFFF is total memory allocated
  --00_0000 to 01_FFFF is where lena256.hex is initially installed
  constant RAM_SIZE_C             : natural   := 262144;  -- Number of words in RAM.
  constant RAM_WIDTH_C            : natural   := 16;  -- Width of RAM words.
  constant MIN_ADDR_C             : natural   := 1;  -- Process RAM from this address ...
  constant MAX_ADDR_C             : natural   := 5;  -- ... to this address.
  subtype RamWord_t is unsigned(RAM_WIDTH_C-1 downto 0);  -- RAM word type. 
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
----signal needed by XESS_SdramSPinst.vhd and xess_jpeg_top.vhd*************************** 
  signal clk_s                    : std_logic;  -- Internal clock.
  signal sumDut_s                 : std_logic_vector(158 downto 0);  -- Send sum back to PC.
  alias fromsiginDut_s is sumDut_s(158 downto 107);
  alias fromjpflgsDut_s is sumDut_s(106 downto 103);
  alias fromjprhDut_s is sumDut_s(102 downto 87);
  alias fromjpsaDut_s is sumDut_s(86 downto 71);
  alias fromjplfDut_s is sumDut_s(70 downto 55);
   
  alias fromresdataDut_s is sumDut_s(54 downto 39);
  alias fromsdramdataDut_s is sumDut_s(38 downto 23);
  alias fromsdramaddrDut_s is sumDut_s(22 downto 0);
  signal nullDutOut_s             : std_logic_vector(0 downto 0);  -- Dummy output for HostIo module.
  signal dataFromSdram_s          : std_logic_vector(sdData_io'range);  -- Data.
  signal addrSdram_s              : unsigned(22 downto 0);  -- Address.
  signal dataToSdram_s            : unsigned(15 downto 0);  -- Data.
  signal dataFromRam_r  : unsigned(15 downto 0); 
  signal sum_r, sum_x             : unsigned( 15 downto 0);
  signal wr_s                     : std_logic;  -- Write-enable control.
  signal rd_s                     : std_logic;  -- Read-enable control.
  signal done_s                   : std_logic;  -- SDRAM R/W operation done signal.
  signal addr_r, addr_x           : unsigned(22 downto 0);  -- RAM address.
  signal dataToRam_r, dataToRam_x, dataFromRam_s : unsigned(15 downto 0);  -- Data to write to RAM.
----signal needed by XESS_SdramSPinst.vhd and xess_jpeg_top.vhd***************************
--
----signal needed by xess_jpeg_top.vhd***************************
  signal state_r, state_x         : t_enum_t_State_1   := INIT;  -- FSM starts off in init state.
  signal sig_in : unsigned(51 downto 0) := (others => '0');
  signal noupdate_s : std_logic;
  signal res_s : signed(15 downto 0) := (others => '0');
  signal res_u : unsigned(15 downto 0) := (others => '0');
  signal jp_lf_r : unsigned(15 downto 0) := (others => '0');
  signal jp_sa_r: unsigned(15 downto 0) := (others => '0');
  signal jp_rh_r : unsigned(15 downto 0) := (others => '0');
  signal jp_lf_x : unsigned(15 downto 0) := (others => '0');
  signal jp_sa_x: unsigned(15 downto 0) := (others => '0');
  signal jp_rh_x : unsigned(15 downto 0) := (others => '0');

  signal jp_flgs_r, jp_flgs_x : unsigned(3 downto 0) := (others => '0');
  signal reset_col_r, reset_col_x : std_logic := '0';
  signal rdy_r, rdy_x : std_logic := '1';
  signal addr_not_reached_r, addr_not_reached_x : std_logic := '0';
  signal offset_r, offset_x           : unsigned(22 downto 0);  -- RAM address.
  signal col_r, col_x, row_r, row_x : unsigned(7 downto 0) := (others => '0');
----signal needed by xess_jpeg_top.vhd*************************** 

  
--signal needed by FIFO*************************** 
  signal empty_r:  std_logic:= '0';
  signal full_r:  std_logic:= '0';
  signal enr_r:  std_logic:= '0';
  signal enw_r:  std_logic:= '0';
  signal dataout_r:  unsigned(15 downto 0):= (others => '0');
  signal datain_r:  unsigned(15 downto 0):= (others => '0');
  signal empty_x:  std_logic:= '0';
  signal full_x:  std_logic:= '0';
  signal enr_x:  std_logic:= '0';
  signal enw_x:  std_logic:= '0';
  signal dataout_x:  unsigned(15 downto 0):= (others => '0');
  signal datain_x:  unsigned(15 downto 0):= (others => '0'); 
  
--signal needed by FIFO*************************** 
 
 
component xess_jpeg_top is
    port (
        clk_fast: in std_logic;
        addr_r: inout unsigned(22 downto 0);
        addr_x: inout unsigned(22 downto 0);
        state_r: inout t_enum_t_State_1;
        state_x: inout t_enum_t_State_1;
        dataToRam_r: inout unsigned(15 downto 0);
        dataToRam_x: inout unsigned(15 downto 0);
        dataFromRam_r: inout unsigned(15 downto 0);
        dataFromRam_x: inout unsigned(15 downto 0);
        sig_in: inout unsigned(51 downto 0);
        noupdate_s: out std_logic;
        res_s: inout signed (15 downto 0);
		  res_u: out unsigned(15 downto 0);
        jp_lf_r: inout unsigned(15 downto 0);
        jp_lf_x: inout unsigned(15 downto 0);
        jp_sa_r: inout unsigned(15 downto 0);
        jp_sa_x: inout unsigned(15 downto 0);
        jp_rh_r: inout unsigned(15 downto 0);
        jp_rh_x: inout unsigned(15 downto 0);

        jp_flgs_r: inout unsigned(3 downto 0);
		  jp_flgs_x: inout unsigned(3 downto 0);
        reset_col_r: inout std_logic;
		  reset_col_x: inout std_logic;
        rdy_r: inout std_logic;
		  rdy_x: inout std_logic;
        addr_not_reached_r: inout std_logic;
		  addr_not_reached_x: inout std_logic;
		  offset_r: inout unsigned(22 downto 0);
        offset_x: inout unsigned(22 downto 0);
        dataFromRam_s: in unsigned(15 downto 0);
        done_s: in std_logic;
        wr_s: out std_logic;
        rd_s: out std_logic;
        sum_r: inout unsigned(15 downto 0);
        sum_x: inout unsigned(15 downto 0);
        empty_r: out std_logic;
        full_r: out std_logic;
        enr_r: inout std_logic;
        enw_r: inout std_logic;
        dataout_r: inout unsigned(15 downto 0);
        datain_r: inout unsigned(15 downto 0);
        empty_x: inout std_logic;
        full_x: inout std_logic;
        enr_x: inout std_logic;
        enw_x: inout std_logic;
        dataout_x: inout unsigned(15 downto 0);
        datain_x: inout unsigned(15 downto 0);
		  col_r: inout unsigned(7 downto 0);
        col_x: inout unsigned(7 downto 0);
		  row_r: inout unsigned(7 downto 0);
        row_x: inout unsigned(7 downto 0)
 
    );
end component xess_jpeg_top;
 
BEGIN
--muxsel <= '0';
--  --*********************************************************************
--  -- Instantiate the jpeg_top step1JPEG_TOP_INSTANCE_7_FSMUPDATE
--  -- updates signals for the FSM.
--  --*********************************************************************
xess_jpeg_top_u0 : xess_jpeg_top
  port map (
     clk_fast => clk_s,
	  addr_r => addr_r,
	  addr_x => addr_x,
	  state_r => state_r,
	  state_x => state_x,
	  dataToRam_r => dataToRam_r,
	  dataToRam_x => dataToRam_x,
	  dataFromRam_r =>  dataFromRam_r,
	  sig_in => sig_in,
	  noupdate_s => noupdate_s,
	  res_s => res_s,
	  res_u => res_u,
	  jp_lf_r => jp_lf_r,
	  jp_sa_r => jp_sa_r,
	  jp_rh_r => jp_rh_r,
	  jp_lf_x => jp_lf_x,
	  jp_sa_x => jp_sa_x,
	  jp_rh_x => jp_rh_x,
	  jp_flgs_r => jp_flgs_r,
	  jp_flgs_x => jp_flgs_x,
	  reset_col_r => reset_col_r,
	  reset_col_x => reset_col_x,
	  rdy_r => rdy_r,
	  rdy_x => rdy_x,
	  addr_not_reached_r => addr_not_reached_r,
	  addr_not_reached_x => addr_not_reached_x,
     offset_r => offset_r,
	  offset_x => offset_x,
     dataFromRam_s => dataFromRam_s,
	  done_s => done_s,
	  wr_s => wr_s,
	  rd_s => rd_s,
	  sum_r => sum_r,
	  sum_x => sum_x,
	  empty_r => empty_r,
	  full_r => full_r,
	  enr_r => enr_r,
	  enw_r => enw_r,
	  dataout_r => dataout_r,
	  datain_r => datain_r,
	  empty_x => empty_x,
	  full_x => full_x,
	  enr_x => enr_x,
	  enw_x => enw_x,
	  dataout_x => dataout_x,
	  datain_x => datain_x,
	  col_x => col_x,
	  col_r => col_r
 
   
  ); 
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
   clk_s <= sdClkFb_i;     
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
 --*********************************************************************
  -- Instantiate the SDRAM controller that connects to the FSM
  -- and interfaces to the external SDRAM chip.
  --*********************************************************************
  SdramCntl_u0 : SdramCntl
    generic map(
      FREQ_G       => 100.0,  -- Use clock freq. to compute timing parameters.
      DATA_WIDTH_G => RAM_WIDTH_C,       -- Width of data words.
		
		NROWS_G       => 4096,  -- Number of rows in SDRAM array.
      NCOLS_G       => 512,  -- Number of columns in SDRAM array.
      HADDR_WIDTH_G => 23,   -- Host-side address width.
      SADDR_WIDTH_G => 12   -- SDRAM-side address width.
      )
    port map(
      clk_i     => clk_s,
      -- FSM side.
      rd_i      => rd_s,
      wr_i      => wr_s,
      done_o    => done_s,
      addr_i    => std_logic_vector(addrSdram_s),
      data_i    => std_logic_vector(dataToSdram_s),
      data_o    => dataFromSdram_s,
      -- SDRAM side.
      sdCke_o   => sdCke_o, -- SDRAM clock-enable pin is connected on the XuLA2.
      sdCe_bo   => sdCe_bo, -- SDRAM chip-enable is connected on the XuLA2.
      sdRas_bo  => sdRas_bo,
      sdCas_bo  => sdCas_bo,
      sdWe_bo   => sdWe_bo,
      sdBs_o    => sdBs_o, -- Both SDRAM bank selects are connected on the XuLA2.
      sdAddr_o  => sdAddr_o,
      sdData_io => sdData_io,
      sdDqmh_o  => sdDqmh_o, -- SDRAM high-byte databus qualifier is connected on the XuLA2.
      sdDqml_o  => sdDqml_o  -- SDRAM low-byte databus qualifier is connected on the XuLA2.
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
 
  fromsdramaddrDut_s <= std_logic_vector(addr_r);
  fromsdramdataDut_s <= std_logic_vector(sum_r);
  fromresdataDut_s <= std_logic_vector(res_s);
  fromjplfDut_s <= std_logic_vector(jp_lf_x);
  fromjpsaDut_s <= std_logic_vector(jp_sa_x);
  fromjprhDut_s <= std_logic_vector(jp_rh_x);
  fromjpflgsDut_s <= std_logic_vector(jp_flgs_x);
  fromsiginDut_s  <= std_logic_vector(sig_in);
   -- Stimulus process.
   -- This is not used in this testbench. The FSM in the
   -- UUT steps through all the operations.
   stim_proc: process
   begin		
      -- hold reset state for 100 ns.
      wait for 100 ns;	

      wait for fpgaClk_period*10;

      -- insert stimulus here 
--      jp_lf <= X"00A3";
--		jp_sa <= X"00A0";
--		jp_rh <= X"00A3";
--		jp_flgs <= X"7";
--		rdy <= '1';
--		addr_not_reached <= '1';
--		wait for 40 ns ;
--		rdy <= '0';
--		addr_not_reached <= '0';
		sig_in <= X"7_00A3_00A0_00B0";
      wait;
   end process;

END;
