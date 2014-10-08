--------------------------------------------------------------------------------
-- Company: 
-- Engineer:
--
-- Create Date:   11:51:10 10/06/2014
-- Design Name:   
-- Module Name:   C:/Xilinx/14.7/ISE_DS/rammyhdl/ram_tb.vhd
-- Project Name:  rammyhdl
-- Target Device:  
-- Tool versions:  
-- Description:   
-- 
-- VHDL Test Bench Created by ISE for module: ram
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
LIBRARY ieee,XESS;
USE ieee.std_logic_1164.ALL;
use XESS.DelayPckg.all;
use IEEE.numeric_std.all;
use std.textio.all;

use work.pck_myhdl_09.all;
-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--USE ieee.numeric_std.ALL;
 
ENTITY jpeg2k_tb IS
END jpeg2k_tb;
 
ARCHITECTURE behavior OF jpeg2k_tb IS 
signal dout_lf : unsigned(15 downto 0);
signal din_lf : unsigned(15 downto 0);    
signal addr_lf : unsigned(8 downto 0);
signal we_lf : std_logic;

signal dout_sam : unsigned(15 downto 0);
signal din_sam : unsigned(15 downto 0);    
signal addr_sam : unsigned(8 downto 0);
signal we_sam : std_logic;

signal dout_rht : unsigned(15 downto 0);
signal din_rht : unsigned(15 downto 0);    
signal addr_rht : unsigned(8 downto 0);
signal we_rht : std_logic;

signal dout_res : unsigned(15 downto 0);
signal din_res : unsigned(15 downto 0);    
signal addr_res : unsigned(8 downto 0);
signal we_res : std_logic;

signal left_s, sam_s, right_s, res_s :  signed(15 downto 0);
signal  even_odd_s, fwd_inv_s, clk_fast : std_logic;
signal updated_s, noupdate_s : std_logic; 
signal reset_jpeg, odd : std_logic; 

signal sigdel_s : std_logic;
signal sigDelayed_s : std_logic;
signal left_sv :   STD_LOGIC_VECTOR(15 downto 0) ;
signal leftDelDut_s :   STD_LOGIC_VECTOR(15 downto 0);
signal leftDel_r, leftDel_x :   STD_LOGIC_VECTOR(15 downto 0);

    -- Component Declaration for the Unit Under Test (UUT)
    COMPONENT jpeg2k
    PORT(
			fpgaClk_i : in    std_logic;  -- 12 MHz clock input from external clock source.
			sdClkFb_i : in    std_logic;  -- 100 MHz clock fed back into FPGA.
         clk_i : IN  std_logic
			 
        );
    END COMPONENT;   
	 
COMPONENT ram
    PORT(
         dout : OUT  unsigned(15 downto 0);
         din : IN  unsigned(15 downto 0);
         addr : IN  unsigned(8 downto 0);
         we : IN  std_logic;
         clk_fast : IN  std_logic
        );
    END COMPONENT;
component jpeg is
    port (
        clk_fast: in std_logic;
        left_s: in signed (15 downto 0);
        right_s: in signed (15 downto 0);
        sam_s: in signed (15 downto 0);
        res_s: out signed (15 downto 0);
		  even_odd_s : in std_logic ;
		  fwd_inv_s : in std_logic;
		  updated_s : in std_logic;
		  noupdate_s : out std_logic
    );
	 end component;	 
COMPONENT approx is
    port (
        clk_fast: in std_logic;
        even_odd_s: out std_logic;
        left_s: out signed (15 downto 0);
        sam_s: out signed (15 downto 0);
        right_s: out signed (15 downto 0);
        we_lf: out std_logic;
        we_sam: out std_logic;
        we_rht: out std_logic;
        we_res: out std_logic;
        addr_lf: inout unsigned(8 downto 0);
        addr_sam: inout unsigned(8 downto 0);
        addr_rht: inout unsigned(8 downto 0);
		  addr_res: inout unsigned(8 downto 0);
        dout_lf: in unsigned(15 downto 0);
        dout_sam: in unsigned(15 downto 0);
        dout_rht: in unsigned(15 downto 0);
        odd: in std_logic;
        reset_jpeg: in std_logic;
        updated_s: out std_logic
    );
end COMPONENT;

   --Inputs
--   signal din : unsigned(15 downto 0) := (others => '0');
--   signal addr : unsigned(8 downto 0) := (others => '0');
--   signal we : std_logic := '0';
--   signal clk : std_logic := '0';
--
-- 	--Outputs
--   signal dout : unsigned(15 downto 0);

   -- Clock period definitions
   constant clk_period : time := 10 ns;
   --Inputs
   signal clk_i : std_logic := '0';

   -- Clock period definitions
   constant clk_i_period : time := 10 ns; 
BEGIN
lfram : ram
  port map(
     dout => dout_lf,
	  din => din_lf,
	  addr => addr_lf,
	  we => we_lf,
	  clk_fast => clk_i
	  );
	  
samram : ram
  port map(
     dout => dout_sam,
	  din => din_sam,
	  addr => addr_sam,
	  we => we_sam,
	  clk_fast => clk_i
	  );
	  
rhtram : ram
  port map(
     dout => dout_rht,
	  din => din_rht,
	  addr => addr_rht,
	  we => we_rht,
	  clk_fast => clk_i
	  );

resram : ram
  port map(
     dout => dout_res,
	  din => din_res,
	  addr => addr_res,
	  we => we_res,
	  clk_fast => clk_i
	  );
		  
ujpeg: jpeg 
	port map( 
        clk_fast => clk_i,
        left_s => left_s,
        right_s => right_s,
        sam_s => sam_s,
        res_s => res_s,
        even_odd_s => even_odd_s,
		  fwd_inv_s => fwd_inv_s,
        updated_s => updated_s,
        noupdate_s => noupdate_s		  
		  );	 
u_approx : approx 
    port map(
        clk_fast => clk_i,
        even_odd_s => even_odd_s,
        left_s => left_s,
        sam_s => sam_s,
        right_s => right_s,
        we_lf => we_lf,
        we_sam => we_sam,
        we_rht => we_rht,
        we_res => we_res,
        addr_lf => addr_lf,
        addr_sam => addr_sam,
        addr_rht => addr_rht,
		  addr_res => addr_res,
        dout_lf => dout_lf,
        dout_sam => dout_sam,
        dout_rht => dout_rht,
        odd => odd,
        reset_jpeg => reset_jpeg,
        updated_s => updated_s 
    );

DelayBus_u0 : DelayBus
	generic map (NUM_DELAY_CYCLES_G => 2)
		port map (
		      --clk_s => clk_s,
			   --This clk used during simulation  
				clk_i => clk_i,
				bus_i => left_sv,
				busDelayed_o => leftDelDut_s
				);
DelayLine_u1 : DelayLine
	generic map (NUM_DELAY_CYCLES_G => 2)
		port map (
		      --clk_s => clk_s,
			   --This clk used during simulation  
				clk_i => clk_i,
				a_i => sigDel_s,
				aDelayed_o => sigDelayed_s
				);
				
	-- Instantiate the Unit Under Test (UUT)
    uut: jpeg2k PORT MAP (
			 fpgaClk_i => clk_i,
			 sdClkFb_i => clk_i,
          clk_i => clk_i
        );

   -- Clock process definitions
   clk_process :process
   begin
		clk_i <= '0';
		wait for clk_period/2;
		clk_i <= '1';
		wait for clk_period/2;
   end process;
 

   -- Stimulus process
   stim_proc: process
   begin		
      -- hold reset state for 100 ns.
      wait for 100 ns;	

      wait for clk_period*10;

      -- insert stimulus here 
		reset_jpeg <= '0';
      we_lf <= '1';
		we_sam <= '1';
		we_rht <= '1';
		we_res <= '1';
		
		even_odd_s <= '1';
		fwd_inv_s <= '1';		
      addr_lf <= b"000000001";
		addr_sam <= b"000000001";	
		addr_rht <= b"000000001";
		addr_res <= b"000000001";
		
		din_lf <= x"00a3";
		din_sam <= x"00a0";
      din_rht <= x"009b";
      wait for 40 ns;
		left_s <= signed(dout_lf);
	   sam_s <= signed(dout_sam);
      right_s <= signed(dout_rht);
		
		wait for 20 ns;
		updated_s <= '1';
		even_odd_s <= '1';
		fwd_inv_s <= '1';
		wait for 40 ns;
      din_res <= unsigned(res_s);

      addr_lf <= b"000000011";
		addr_sam <= b"000000011";	
		addr_rht <= b"000000011";
		addr_res <= b"000000011";
		
		din_lf <= x"009b";
		din_sam <= x"009b";
      din_rht <= x"009d";
		
		wait for 20 ns;
		--updated_s <= '1';
		--even_odd_s <= '0';
		--fwd_inv_s <= '1';
		left_s <= signed(dout_lf);
	   sam_s <= signed(dout_sam);
      right_s <= signed(dout_rht);
		wait for 300 ns;
      din_res <= unsigned(res_s);
		wait for 300 ns;
		wait for 40 ns;
		odd <= '1';
		reset_jpeg <= '1';
		wait for 80 ns;
		reset_jpeg <= '0';
		wait for 400 ns;
		odd <= '0';
	   reset_jpeg <= '1'; 
		wait for 80 ns;
		reset_jpeg <= '0';
		wait for 400 ns;
		odd <= '1';
	   reset_jpeg <= '1'; 
		wait for 80 ns;
		reset_jpeg <= '0';	
      --xxx <= dout_lf;		
		wait;
   end process;

END;
