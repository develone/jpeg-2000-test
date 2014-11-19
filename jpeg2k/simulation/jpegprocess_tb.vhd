--------------------------------------------------------------------------------
-- Company: 
-- Engineer:
--
-- Create Date:   10:56:57 10/23/2014
-- Design Name:   
-- Module Name:   C:/Xilinx/14.7/ISE_DS/jp_process/jpegprocess_tb.vhd
-- Project Name:  jp_process
-- Target Device:  
-- Tool versions:  
-- Description:   
-- 
-- VHDL Test Bench Created by ISE for module: jpeg_process
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
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
use std.textio.all;
--use XESS.ClkgenPckg.all;     -- For the clock generator module.
--use XESS.SdramCntlPckg.all;  -- For the SDRAM controller module.
--use XESS.HostIoPckg.all;     -- For the FPGA<=>PC transfer link module
use work.pck_myhdl_09.all;
use work.pck_jpeg_top.all;
--use work.pck_jpegFsm.all;
-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--USE ieee.numeric_std.ALL;
 
ENTITY jpegprocess_tb IS
END jpegprocess_tb;

ARCHITECTURE behavior OF jpegprocess_tb IS 
	signal dataToRam_r, dataFromRam_s, dout_res : unsigned(15 downto 0);
   signal state_r : t_enum_t_State_1 := INIT;
   signal state_x : t_enum_t_State_1 := INIT; 	
	signal reset_row, reset_row_r, reset_fsm_r : std_logic := '1';
	signal reset_col, reset_col_r : std_logic := '1';
   signal addr_not_reached,  addr_not_reached1, addr_not_reached2 : std_logic := '1';
	signal addr_res : unsigned(8 downto 0);
   signal jp_lf : unsigned(15 downto 0) := (others => '0');
   signal jp_sa: unsigned(15 downto 0) := (others => '0');
	signal jp_rh : unsigned(15 downto 0) := (others => '0');
   signal jp_flgs : unsigned(3 downto 0) := (others => '0');
	signal jp_col_lf : unsigned(15 downto 0) := (others => '0');
   signal jp_col_sa: unsigned(15 downto 0) := (others => '0');
	signal jp_col_rh : unsigned(15 downto 0) := (others => '0');
   signal jp_col_flgs : unsigned(3 downto 0) := (others => '0');
	signal offset, offset_r  : unsigned(8 downto 0) := (others => '0');	 
   signal rdy : std_logic := '1';
	signal clk_fast : std_logic := '0';
   signal sig_in, sig_in1, sig_in2 : unsigned(51 downto 0) := (others => '0');	
   signal noupdate_s : std_logic;
   signal res_s : signed(15 downto 0);
   signal index, index_r : unsigned(8 downto 0);
 	signal row, row_r : unsigned(3 downto 0);
	signal addr_r : unsigned(8 downto 0);
	signal addr_r1 : unsigned(8 downto 0);
	signal addr_r2 : unsigned(8 downto 0);
	signal addr_r3 : unsigned(8 downto 0);	
	signal sel, sel_col : std_logic := '0';
 	signal we_res : std_logic := '1';
	signal pass1_done, pass1_done_r : std_logic := '0';
	--Signals to match DRamSPInf_tb.vhd 
signal rst:  std_logic;
signal rst_file_in : std_logic := '1';
--signal clk:  std_logic := '0';
signal eog:  std_logic;
signal y:    std_logic_vector(15 downto 0);
  constant NO          : std_logic := '0';
  constant YES         : std_logic := '1';
  constant RAM_SIZE_C  : natural   := 256;  -- Number of words in RAM.
  constant RAM_WIDTH_C : natural   := 16;   -- Width of RAM words.
  constant MIN_ADDR_C  : natural   := 1;   -- Process RAM from this address ...
  constant MAX_ADDR_C  : natural   := 5;   -- ... to this address.
  subtype RamWord_t is unsigned(RAM_WIDTH_C-1 downto 0);   -- RAM word type.
  type Ram_t is array (0 to RAM_SIZE_C-1) of RamWord_t;  -- array of RAM words type.
  signal ram_r         : Ram_t;         -- RAM declaration.
  signal wr_s          : std_logic;     -- Write-enable control.
--  signal addr_r        : natural range 0 to RAM_SIZE_C-1;  -- RAM address.
--  signal dataToRam_r   : RamWord_t;     -- Data to write to RAM.
--  signal dataFromRam_s : RamWord_t;     -- Data read from RAM.
  signal sum_r         : natural range 0 to RAM_SIZE_C * (2**RAM_WIDTH_C) - 1;
  	--Signals to match DRamSPInf_tb.vhd 
component FILE_READ 
  generic (
           stim_file:       string  := "sim.dat"
          );
  port(
       CLK              : in  std_logic;
       RST              : in  std_logic;
       Y                : out std_logic_vector(15 downto 0);
       EOG              : out std_logic
      );
end component; 

   
   -- Clock period definitions
   constant clk_fast_period : time := 10 ns;

COMPONENT jpeg_top 
    port (
        clk_fast: in std_logic;
        rst: inout std_logic;
        eog: in std_logic;
        wr_s: out std_logic;
        rst_file_in: in std_logic;
        addr_r: out unsigned(8 downto 0);
        dataToRam_r: out unsigned(15 downto 0);
        y: in unsigned(15 downto 0);
        addr_r1: inout unsigned(8 downto 0);
        addr_r2: inout unsigned(8 downto 0);
        addr_r3: inout unsigned(8 downto 0);
        sel: inout std_logic;
        sel_col: inout std_logic;
        sig_in: inout unsigned(51 downto 0);
		  sig_in1: inout unsigned(51 downto 0);
        sig_in2: inout unsigned(51 downto 0);
        noupdate_s: inout std_logic;
        res_s: out signed (15 downto 0);
        offset: inout unsigned(8 downto 0);
        dataFromRam_s: in unsigned(15 downto 0);
        jp_lf: inout unsigned(15 downto 0);
        jp_sa: inout unsigned(15 downto 0);
        jp_rh: inout unsigned(15 downto 0);
        jp_flgs: inout unsigned(3 downto 0);
        jp_col_lf: inout unsigned(15 downto 0);
        jp_col_sa: inout unsigned(15 downto 0);
        jp_col_rh: inout unsigned(15 downto 0);
        jp_col_flgs: inout unsigned(3 downto 0);
        reset_row: inout std_logic;
        reset_row_r: inout std_logic;
        reset_col: inout std_logic;
        reset_col_r: inout std_logic;
        addr_not_reached: inout std_logic;
        addr_not_reached1: inout std_logic;
        addr_not_reached2: inout std_logic;
        rdy: inout std_logic;
        state_r: inout t_enum_t_State_1;
        state_x: inout t_enum_t_State_1;
        reset_fsm_r: in std_logic;
        addr_res: inout unsigned(8 downto 0);
        addr_res_r: inout unsigned(8 downto 0);
        offset_r: inout unsigned(8 downto 0);
        dout_res: out unsigned(15 downto 0);
        din_res: in unsigned(15 downto 0);
        we_res: in std_logic;
        pass1_done: inout std_logic;
        pass1_done_r: inout std_logic;
		  index: inout unsigned(8 downto 0);
        index_r: inout unsigned(8 downto 0);
        row: inout unsigned(3 downto 0);
        row_r: out unsigned(3 downto 0)
    );
end COMPONENT;
 

 


BEGIN

--*********************************************************************
  -- RAM is inferred from this process.
  --*********************************************************************
  Ram_p : process (clk_fast)
  begin
    -- Write to the RAM at the given address if the write-enable is high.
    if rising_edge(clk_fast) then
      if wr_s = YES then
        ram_r(TO_INTEGER(addr_r)) <= dataToRam_r;
      end if;
    end if;
  end process;
  -- Continually read from whatever RAM address is present.
  dataFromRam_s <= ram_r(TO_INTEGER(addr_r));
input_stim: FILE_READ 
  port map(
       CLK      => clk_fast,
--       CLK      => clk_i,
       RST      => rst,
       Y        => y,
       EOG      => eog
      ); 

ujpeg_top : jpeg_top
	port map (
		clk_fast => clk_fast,
		offset => offset,
		dataFromRam_s => dataFromRam_s,
		addr_r =>  addr_r,
		jp_lf => jp_lf,
		jp_sa => jp_sa,
		jp_rh => jp_rh,
		jp_flgs => jp_flgs,
		jp_col_lf => jp_col_lf,
		jp_col_sa => jp_col_sa,
		jp_col_rh => jp_col_rh,
		jp_col_flgs => jp_col_flgs,
		reset_row => reset_row,
		reset_col => reset_col,
		reset_col_r => reset_col_r,		
		rdy => rdy,
		sig_in => sig_in,
		sig_in1 => sig_in1,
		sig_in2 => sig_in2,
		noupdate_s => noupdate_s,
		res_s => res_s,
		state_r => state_r,
		state_x => state_x,
		reset_fsm_r =>  reset_fsm_r,      	
		addr_res => addr_res,
		din_res => unsigned(res_s),
 		offset_r => offset_r,
		addr_not_reached => addr_not_reached,
		addr_not_reached1 => addr_not_reached1,
		addr_not_reached2 => addr_not_reached2,		
 		dataToRam_r => dataToRam_r,
		we_res => we_res,
		wr_s => wr_s,
		rst => rst,
		eog => eog,
		rst_file_in => rst_file_in,
		addr_r1 => addr_r1,
		addr_r2 => addr_r2,
		addr_r3 => addr_r3,
		sel => sel,
		sel_col => sel_col,
		y => unsigned(y),
		dout_res => dout_res,
		pass1_done => pass1_done,
		pass1_done_r => pass1_done_r,
		index => index,
		index_r => index_r,
		row => row,
		row_r => row_r
	
	);


 
 

	-- Instantiate the Unit Under Test (UUT)
	

    -- Clock process definitions
   clk_fast_process :process
   begin
		clk_fast <= '0';
		wait for clk_fast_period/2;
		clk_fast <= '1';
		wait for clk_fast_period/2;
   end process;
 

   -- Stimulus process
   stim_proc: process
   begin		
      -- hold reset state for 100 ns.
 
      wait for 100 ns;	
--		sel <= '0';
--		reset_fsm_r <= '0';
 
		rst_file_in <= '0';

      wait for clk_fast_period*10;

      -- insert stimulus here
 
 
		rst_file_in <= '1';
		wait for 10 ns;
 
		--reset_fsm_r <= '1';
		wait for 2700 ns;
--		sel <= '1';
		reset_fsm_r <= '0';
		wait for 10 ns;
		reset_fsm_r <= '1';
      wait;
   end process;

END;
