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
-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--USE ieee.numeric_std.ALL;
 
ENTITY jpegprocess_tb IS
END jpegprocess_tb;
 
ARCHITECTURE behavior OF jpegprocess_tb IS 
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
    

   --Inputs
	signal dout_res : unsigned(15 downto 0);
	signal din_res : unsigned(15 downto 0);    
	signal addr_res : unsigned(8 downto 0);
--	signal addr_res, addr_res_r, addr_res_x : unsigned(8 downto 0);
	signal we_res : std_logic; 
--	signal we_res_r, we_res_x : std_logic; 
   signal jp_lf : unsigned(15 downto 0) := (others => '0');
   signal jp_sa: unsigned(15 downto 0) := (others => '0');
	signal jp_rh : unsigned(15 downto 0) := (others => '0');
   signal jp_flgs : unsigned(3 downto 0) := (others => '0');
   signal rdy : std_logic := '0';
 	--Outputs
   signal sig_out : unsigned(51 downto 0);
    signal dout_rom : unsigned(15 downto 0);
    signal addr_rom : unsigned(11 downto 0);	 
    -- Component Declaration for the Unit Under Test (UUT)
 
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

   --Inputs
   signal clk_fast : std_logic := '0';
   signal sig_in : unsigned(51 downto 0) := (others => '0');
 
--   signal fwd_inv_s : std_logic := '0';
--   signal even_odd_s : std_logic := '0';
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
  uram2sig: ram2sig PORT MAP (
          jp_lf => jp_lf,
          jp_sa => jp_sa,
          jp_rh => jp_rh,
			 jp_flgs => jp_flgs,
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
	  we => we_res,
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
 
--		wait for 20 ns;
--		rdy <= '1';

		 
		addr_rom <= X"000";

		wait for 10 ns;
      --left
      jp_lf <= dout_rom;
		 
		wait for 10 ns;
 
		addr_rom <= X"001";
		wait for 10 ns;
		--sam
		jp_sa <= dout_rom;
		 
		wait for 10 ns;
 
		addr_rom <= X"002";
		wait for 10 ns;
		--right
		jp_rh <= dout_rom;
--		sig_in <= sig_rom or (sig_in);
		wait for 10 ns;
		--flags
		jp_flgs <= b"0111";
 

		wait for 10 ns;
		rdy <= '1';
 		wait for 20 ns;
		sig_in <= sig_out;
--		wait for 10 ns;
		rdy <= '0';
		addr_res <= b"000000000";
		we_res <= '1';
		wait for 20 ns;
		we_res <= '0';
		wait for 10 ns;
      wait;
   end process;

END;
