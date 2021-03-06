--------------------------------------------------------------------------------
-- Company: 
-- Engineer:
--
-- Create Date:   05:55:44 09/29/2014
-- Design Name:   
-- Module Name:   C:/Xilinx/14.7/ISE_DS/delay_tests/TBstd_sig.vhd
-- Project Name:  delay_tests
-- Target Devxice:  
-- Tool versions:  
-- Description:   
-- 
-- VHDL Test Bench Created by ISE for module: std_sig
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
use IEEE.STD_LOGIC_UNSIGNED.ALL;
use IEEE.NUMERIC_STD.ALL;
use XESS.DelayPckg.all;

-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--USE ieee.numeric_std.ALL;
 
ENTITY TBstd_sig IS
END TBstd_sig;
 
ARCHITECTURE behavior OF TBstd_sig IS 
 
    -- Component Declaration for the Unit Under Test (UUT)
 
    COMPONENT std_sig
    PORT(
         clk_i : IN  std_logic;
		
			sigDel_flag : in std_logic;

			even_odd_s : in std_logic;
			fwd_inv_s : in std_logic;
			updated_s : in std_logic;
			noupdate_s : out std_logic;
         left_s, sam_s, right_s, lf_del : in signed(15 downto 0);
         res_s : out signed(15 downto 0);
			fpgaClk_i : in    std_logic; -- 12 MHz clock input from external clock source.
			sdClkFb_i : in    std_logic;  -- 100 MHz clock fed back into FPGA.
			--The following signal were not be stimulated in simul
			--These need to be in the entity of std_signal
			updated_r : out std_logic;
			updated_x : in std_logic;
			sigDelayed_r : out std_logic;
			sigDelayed_x : in std_logic;
			sam_addr_r : out unsigned(13 downto 0) := (others => '0');
			sam_addr_x : in unsigned(13 downto 0) := (others => '0');
			addrjpeg_r : out unsigned(13 downto 0) := (others => '0');
			addrjpeg_x : in unsigned(13 downto 0) := (others => '0');
			addr_r : out unsigned(13 downto 0) := (others => '0');
			addr_x : in unsigned(13 downto 0) := (others => '0')
			);
    END COMPONENT;
	 

	
   --Inputs
   signal clk_i : std_logic := '0' ;

   signal sigDel_flag  : std_logic := '0' ;
   signal even_odd_s : std_logic := '0' ; 
   signal fwd_inv_s : std_logic := '0' ;
   signal updated_s : std_logic := '0' ;

   signal left_s, sam_s, right_s, lf_del : signed(15 downto 0);
   signal fpgaClk_i : std_logic := '0' ;
   signal sdClkFb_i : std_logic := '0' ;
	signal addr_x : unsigned(13 downto 0) := (others => '0');
	signal sam_addr_x : unsigned(13 downto 0) := (others => '0');
   signal updated_x : std_logic := '0';
   signal sigDelayed_x : std_logic := '0';
	signal addrjpeg_x : unsigned(13 downto 0) := (others => '0');
	signal dataToRam_x : unsigned(15 downto 0) := (others => '0');
 	--Outputs
   signal addr_r : unsigned(13 downto 0);
	signal sam_addr_r : unsigned(13 downto 0) := (others => '0');
   signal updated_r : std_logic := '0';
   signal sigDelayed_r : std_logic := '0';
	signal addrjpeg_r : unsigned(13 downto 0) := (others => '0');
	signal dataToRam_r : unsigned(15 downto 0) := (others => '0');
 	--Outputs

	signal res_s : signed(15 downto 0);
	signal sigDel_s  : std_logic := '0' ;
	signal sigDelayed_s, noupdate_s  : std_logic;
	signal left_sv :   STD_LOGIC_VECTOR (15 downto 0);
   signal leftDelDut_s :   STD_LOGIC_VECTOR (15 downto 0);
 --signal noupdate_s  : std_logic;
   -- Clock period definitions
   constant clk_i_period : time := 10 ns;
 
BEGIN
 
	-- Instantiate the Unit Under Test (UUT)
   uut: std_sig PORT MAP (
          clk_i => clk_i,
          --left_sv => left_sv,
          --leftDelDut_s => leftDelDut_s,
			 lf_del => lf_del,

			 sigDel_flag => sigDel_flag,
			 
			 left_s => left_s,
			 sam_s => sam_s,
			 right_s => right_s,
			 res_s => res_s,
			 even_odd_s => even_odd_s,
			 fwd_inv_s => fwd_inv_s,
			 updated_s => updated_s,
			 noupdate_s => noupdate_s,
			 fpgaClk_i => fpgaClk_i,
			 sdClkFb_i => sdClkFb_i,
			 updated_r => updated_r,
          updated_x => updated_x,
			 sigDelayed_r => sigDelayed_r,
          sigDelayed_x => sigDelayed_x,
	       sam_addr_r => sam_addr_r,
          sam_addr_x => sam_addr_x,		 
          addrjpeg_r => addrjpeg_r,
          addrjpeg_x => addrjpeg_x,

          addr_r => addr_r,
          addr_x => addr_x			 
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


   -- Clock process definitions
   clk_i_process :process
   begin
		clk_i <= '0';
		wait for clk_i_period/2;
		clk_i <= '1';
		wait for clk_i_period/2;
   end process;
 

   -- Stimulus process
   stim_proc: process
   begin		
      -- hold reset state for 100 ns.
      wait for 100 ns;	

      wait for clk_i_period*10;

      -- insert stimulus here 

		left_s <= x"00A3";
		sam_s <= x"00A0";
		right_s <= x"009B";
		even_odd_s <= '1';
		fwd_inv_s <= '1';
		updated_s <= '0';
		wait for 100 ns;	
		updated_s <= '1';
		wait for 100 ns;
		
		wait for 100 ns;
      left_s <= x"00A3";
		sam_s <= x"00A0";
		right_s <= x"009B";      
      wait for 100 ns;
      left_s <= x"009B";
		sam_s <= x"009B";
		right_s <= x"009D";
      left_sv <= x"009B";
		sigDel_s <= '1';
		dataToRam_x <= x"AA55";
		updated_x <= '1';
		sigDelayed_x <= '1';
		sam_addr_x <= b"00000000000001";
		addrjpeg_x <= b"10000000000001";
		addr_x <= b"10000000000001";
		--sigDelayed_x <= sigDelayed_s;
		wait;
   end process;

END;
