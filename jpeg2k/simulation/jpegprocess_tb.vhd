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
 
   signal state_r : t_enum_t_State_1 := INIT; 

   --Inputs
	signal reset_n, reset_fsm_r, addr_not_reached, sig_out_valid  : std_logic := '1';

	signal dout_res : unsigned(15 downto 0);
--	signal din_res : unsigned(15 downto 0);    
	signal addr_res : unsigned(8 downto 0);
 
 
   signal jp_lf : unsigned(15 downto 0) := (others => '0');
   signal jp_sa: unsigned(15 downto 0) := (others => '0');
	signal jp_rh : unsigned(15 downto 0) := (others => '0');
   signal jp_flgs : unsigned(3 downto 0) := (others => '0');
	signal addr_rom : unsigned(11 downto 0);	
   signal offset, offset_r  : unsigned(11 downto 0) := (others => '0');	 
   signal rdy : std_logic := '1';
	signal dout_rom : unsigned(15 downto 0);
	signal clk_fast : std_logic := '0';
   signal sig_in : unsigned(51 downto 0) := (others => '0');	
   signal noupdate_s : std_logic;
   signal res_s : signed(15 downto 0);

COMPONENT ram
    PORT(
         dout : OUT  unsigned(15 downto 0) := (others => '0');
         din : IN  unsigned(15 downto 0) := (others => '0');
         addr : IN  unsigned(8 downto 0) := (others => '0');
         we : IN  std_logic;
         clk_fast : IN  std_logic
        );
END COMPONENT;    
   -- Clock period definitions
   constant clk_fast_period : time := 10 ns;
COMPONENT rom 
    port (
        dout_rom: out unsigned(15 downto 0);
        addr_rom: in unsigned(11 downto 0)
    );
end COMPONENT;  

COMPONENT jpeg_top 
    port (
        clk_fast: in std_logic;
        offset: inout unsigned(11 downto 0);
        dout_rom: in unsigned(15 downto 0);
        addr_rom: inout unsigned(11 downto 0);
        jp_lf: inout unsigned(15 downto 0);
        jp_sa: inout unsigned(15 downto 0);
        jp_rh: inout unsigned(15 downto 0);
        jp_flgs: inout unsigned(3 downto 0);
        reset_n: inout std_logic;
        rdy: inout std_logic;
        sig_in: inout unsigned(51 downto 0);
        noupdate_s: inout std_logic;
        res_s: out signed (15 downto 0);
        state_r: inout t_enum_t_State_1;
        reset_fsm_r: in std_logic;
        addr_res: out unsigned(8 downto 0);
        offset_r: inout unsigned(11 downto 0);
		  addr_not_reached: inout std_logic;
		  sig_out_valid: out std_logic
    );
end COMPONENT;
 

 


BEGIN
ujpeg_top : jpeg_top
	port map (
		clk_fast => clk_fast,
		offset => offset,
		dout_rom => dout_rom,
		addr_rom =>  addr_rom,
		jp_lf => jp_lf,
		jp_sa => jp_sa,
		jp_rh => jp_rh,
		jp_flgs => jp_flgs,
		reset_n => reset_n,
		rdy => rdy,
--		sig_out => sig_out,
		sig_in => sig_in,
		noupdate_s => noupdate_s,
		res_s => res_s,
		state_r => state_r,
		reset_fsm_r =>  reset_fsm_r,      	
		addr_res => addr_res, 
		offset_r => offset_r,
		addr_not_reached => addr_not_reached,
		sig_out_valid => sig_out_valid	
	);


 
urom : rom 
    port map(
        dout_rom => dout_rom,
        addr_rom => addr_rom
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

resram : ram
  port map(
     dout => dout_res,
	  din => unsigned(res_s),
	  addr => addr_res,
--	  we => reset_n,
	  we =>  reset_fsm_r,
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
 
--		offset_r <= X"000";
		wait for 10 ns;
		reset_fsm_r <= '0';
		wait for 10 ns;
		reset_fsm_r <= '1';
--      wait for 60 ns;
---- 
--		offset_r <= X"002";
--		wait for 10 ns;
----		reset_fsm_r <= '0';
----		wait for 10 ns;
----		reset_fsm_r <= '1';
--      wait for 60 ns;
---- 
--		offset_r <= X"004";
--		wait for 10 ns;
----		reset_fsm_r <= '0';
----		wait for 10 ns;
----		reset_fsm_r <= '1';
--      wait for 60 ns;		
--  
       wait;
   end process;

END;
