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

use work.pck_jpegFsm.all;
-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--USE ieee.numeric_std.ALL;
 
ENTITY jpegprocess_tb IS
END jpegprocess_tb;
 
ARCHITECTURE behavior OF jpegprocess_tb IS 


  

   --Inputs
	signal reset_n, reset_fsm_r, reset_fsm_x : std_logic := '1';
	signal reset_n_r,  reset_n_x : std_logic := '1';
	signal dout_res : unsigned(15 downto 0);
	signal din_res : unsigned(15 downto 0);    
	signal addr_res : unsigned(8 downto 0);
   signal addr_res_r, addr_res_x : unsigned(11 downto 0);
	signal we_res : std_logic; 
--	signal we_res_r, we_res_x : std_logic; 
   signal jp_lf : unsigned(15 downto 0) := (others => '0');
   signal jp_sa: unsigned(15 downto 0) := (others => '0');
	signal jp_rh : unsigned(15 downto 0) := (others => '0');
   --signal jp_flgs : unsigned(3 downto 0) := (others => '0');
	signal jp_flgs, jp_flgs_r, jp_flgs_x : unsigned(3 downto 0) := (others => '0');
   signal rdy : std_logic := '1';
 	--Outputs
   signal sig_out : unsigned(51 downto 0);
	signal ttt : std_logic_vector(51 downto 0);
   signal do : std_logic_vector(51 downto 0);	
	alias tofilewr_s is ttt (51 downto 0); 
    signal dout_rom : unsigned(15 downto 0);
    signal addr_rom, addr_rom_r, addr_rom_x : unsigned(11 downto 0);	
	 --signal addr_rom : unsigned(11 downto 0);	
    signal offset, offset_r, offset_x : unsigned(11 downto 0);	 
	 
	 signal offset_i, offset_o : unsigned(11 downto 0);	 
    -- Component Declaration for the Unit Under Test (UUT)
--COMPONENT FsmUpdate_p 
--    port (
--        clk_fast: in std_logic;
--        addr_rom_x: inout unsigned(11 downto 0);
--        addr_res_x: inout unsigned(11 downto 0);
--        offset_x: inout unsigned(11 downto 0);
--        jp_flgs_x: inout unsigned(3 downto 0)
--    );
--end COMPONENT;
COMPONENT filewrite_explicitopen 
    generic (data_width: integer:= 52);
    port (  clk : in  std_logic;
            di  : in  std_logic_vector (data_width - 1 downto 0);
            do  : out std_logic_vector (data_width - 1 downto 0));	    
end COMPONENT;
COMPONENT jprow 
    port (
        clk_fast: in std_logic;
        offset_o: out unsigned(11 downto 0);
        offset_i: in unsigned(11 downto 0)
    );
end COMPONENT;
	 
   COMPONENT ram2sig
    PORT(
         jp_lf : IN  unsigned(15 downto 0);
         jp_sa : IN  unsigned(15 downto 0);
         jp_rh : IN  unsigned(15 downto 0);
			jp_flgs : IN  unsigned(3 downto 0);
			sig_out : OUT unsigned(51 downto 0);
			rdy : in std_logic
        );
    END COMPONENT;
COMPONENT rom_rd 
    port (
        clk_fast: in std_logic := '1';
		  offset : inout unsigned(11 downto 0);
        dout_rom : in unsigned(15 downto 0);
        addr_rom : inout unsigned(11 downto 0);
        jp_lf: out unsigned(15 downto 0);
        jp_sa: out unsigned(15 downto 0);
        jp_rh: out unsigned(15 downto 0);
		  jp_flgs : in unsigned(3 downto 0) := (others => '0');
        reset_n: in std_logic
    );
end COMPONENT; 
COMPONENT jpegFsm  
    port (
        state_r: inout t_enum_t_State_1;
        reset_fsm_r: in std_logic;
        addr_res: out unsigned(8 downto 0);
        offset: out unsigned(11 downto 0);
		  offset_r: in unsigned(11 downto 0);
        jp_flgs: out unsigned(3 downto 0);
		  reset_n: out std_logic;
		  rdy: out std_logic
    );
end COMPONENT; 
    COMPONENT jpeg_process
    PORT(
--	 	    fpgaClk_i : in    std_logic;  -- 12 MHz clock input from external clock source.
--          sdClk_o   : out   std_logic;  -- 100 MHz clock to SDRAM.
--			 sdClkFb_i : in    std_logic;  -- 100 MHz clock fed back into FPGA.
-- 
--          --blinker_o : out  STD_LOGIC;
--			 sdCke_o   : out   std_logic;  -- SDRAM clock enable.
--          sdCe_bo   : out   std_logic;  -- SDRAM chip-enable.
--          sdRas_bo  : out   std_logic;  -- SDRAM row address strobe.
--          sdCas_bo  : out   std_logic;  -- SDRAM column address strobe.
--          sdWe_bo   : out   std_logic;  -- SDRAM write-enable.
--          sdBs_o    : out   std_logic_vector(1 downto 0);  -- SDRAM bank-address.
--          sdAddr_o  : out   std_logic_vector(12 downto 0);  -- SDRAM address bus.
--          sdData_io : inout std_logic_vector(15 downto 0);    -- SDRAM data bus.
--          sdDqmh_o  : out   std_logic;  -- SDRAM high-byte databus qualifier.
--          sdDqml_o  : out   std_logic;  -- SDRAM low-byte databus qualifier.
         clk_fast : IN  std_logic;
         sig_in : IN  unsigned(51 downto 0);
--         fwd_inv_s : IN  std_logic;
--         even_odd_s : IN  std_logic;
--         updated_s : IN  std_logic;
         noupdate_s : OUT  std_logic;
         res_s : OUT  signed(15 downto 0)
        );
    END COMPONENT;
COMPONENT ram
    PORT(
         dout : OUT  unsigned(15 downto 0) := (others => '0');
         din : IN  unsigned(15 downto 0) := (others => '0');
         addr : IN  unsigned(8 downto 0) := (others => '0');
         we : IN  std_logic;
         clk_fast : IN  std_logic
        );
END COMPONENT;    
   signal state_r : t_enum_t_State_1;
   signal state_x :  t_enum_t_State_1;
   --Inputs
   signal clk_fast : std_logic := '0';
   signal sig_in : unsigned(51 downto 0) := (others => '0');
 
   signal fwd_inv_s : std_logic := '0';
   signal even_odd_s : std_logic := '0';
--   signal updated_s : std_logic := '0';

 	--Outputs
   signal noupdate_s : std_logic;
   signal res_s : signed(15 downto 0);
 
   -- Clock period definitions
   constant clk_fast_period : time := 10 ns;
COMPONENT rom 
    port (
        dout_rom: out unsigned(15 downto 0);
        addr_rom: in unsigned(11 downto 0)
    );
end COMPONENT;  


 

 


BEGIN
ufilewrite_explicitopen : filewrite_explicitopen
--    generic map (data_width  => 52)
    port map (  clk => clk_fast, 
            di => tofilewr_s,
            do => do
				); 
 
--uFsmUpdate_p : FsmUpdate_p 
--    port map (
--        clk_fast => clk_fast,
----        reset_fsm_x => reset_fsm_x,
-- 
--        addr_rom_x => addr_rom_r,
--  
--        addr_res_x => addr_res_r,
-- 
--        offset_x => offset_r,
-- 
--        jp_flgs_x => jp_flgs_r
-- 
--    );
 

ujpegFsm : jpegFsm
    port map (
        state_r => state_r,
		  reset_fsm_r => reset_fsm_r,
        addr_res => addr_res, 
        offset => offset,
		  offset_r => offset_r,
		  jp_flgs => jp_flgs,
			reset_n => reset_n,
			rdy => rdy
    );
 
urom_rd : rom_rd 
    port  map(
        clk_fast => clk_fast,
--		  offset =>  offset_x,
  
		  offset =>  offset,
        dout_rom => dout_rom,
        addr_rom =>  addr_rom,
        jp_lf => jp_lf,
        jp_sa => jp_sa,
        jp_rh => jp_rh,
        jp_flgs => jp_flgs,
        reset_n => reset_n
--			reset_n => reset_n_x
    );
  uram2sig: ram2sig PORT MAP (
          jp_lf => jp_lf,
          jp_sa => jp_sa,
          jp_rh => jp_rh,
			 jp_flgs => jp_flgs,
--			 rdy => rdy,
--			 jp_flgs => jp_flgs_x,
			 rdy => rdy, 
			 sig_out => sig_out
        );
 
urom : rom 
    port map(
        dout_rom => dout_rom,
        addr_rom => addr_rom
    );

	-- Instantiate the Unit Under Test (UUT)
   uut: jpeg_process PORT MAP (
          clk_fast => clk_fast,
          sig_in => sig_in,
--          fwd_inv_s => fwd_inv_s,
--          even_odd_s => even_odd_s,
--          updated_s => updated_s,
          noupdate_s => noupdate_s,
          res_s => res_s
        );

   -- Clock process definitions
   clk_fast_process :process
   begin
		clk_fast <= '0';
		wait for clk_fast_period/2;
		clk_fast <= '1';
		wait for clk_fast_period/2;
   end process;

resram : ram
  port map(
     dout => dout_res,
	  din => unsigned(res_s),
	  addr => addr_res,
	  we => reset_n,
--	  we => rdy,
	  --clk_fast => clk_i
	  clk_fast => clk_fast
	  );	 

   -- Stimulus process
   stim_proc: process
   begin		
      -- hold reset state for 100 ns.
      wait for 100 ns;	

      wait for clk_fast_period*10;

      -- insert stimulus here
		offset_i <= X"000";
		offset_r <= X"000";
		wait for 10 ns;
		reset_fsm_r <= '0';
		wait for 10 ns;
		reset_fsm_r <= '1';
      wait for 60 ns;
		sig_in <= sig_out;
		tofilewr_s <= x"6009b00a0009b";
		wait for 10 ns;
		offset_r <= X"002";
		wait for 10 ns;
		reset_fsm_r <= '0';
		wait for 10 ns;
		reset_fsm_r <= '1';
      wait for 60 ns;
		sig_in <= sig_out;
		
		wait for 10 ns;
		offset_r <= X"004";
		wait for 10 ns;
		reset_fsm_r <= '0';
		wait for 10 ns;
		reset_fsm_r <= '1';
      wait for 60 ns;
		sig_in <= sig_out;
		
-- 		offset_r <= X"001";
--		wait for 10 ns;
--		reset_fsm_r <= '0';
--		wait for 10 ns;
--		reset_fsm_r <= '1';
--      wait for 60 ns;
--		sig_in <= sig_out;
--		
--		wait for 10 ns;
--		offset_r <= X"003";
--		wait for 10 ns;
--		reset_fsm_r <= '0';
--		wait for 10 ns;
--		reset_fsm_r <= '1';
--      wait for 60 ns;
--		sig_in <= sig_out;
--		
--		wait for 10 ns;
--		offset_r <= X"005";
--		wait for 10 ns;
--		reset_fsm_r <= '0';
--		wait for 10 ns;
--		reset_fsm_r <= '1';
--      wait for 60 ns;
--		sig_in <= sig_out;
     
 
       wait;
   end process;

END;
