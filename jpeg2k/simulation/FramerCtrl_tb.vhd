--------------------------------------------------------------------------------
-- Company: 
-- Engineer:
--
-- Create Date:   05:37:10 10/19/2014
-- Design Name:   
-- Module Name:   C:/Xilinx/14.7/ISE_DS/fsm/FramerCtrl_tb.vhd
-- Project Name:  fsm
-- Target Device:  
-- Tool versions:  
-- Description:   
-- 
-- VHDL Test Bench Created by ISE for module: FramerCtrl
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
use IEEE.numeric_std.all;
use std.textio.all;

use work.pck_myhdl_09.all;

use work.pck_FramerCtrl.all; 
-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--USE ieee.numeric_std.ALL;
 
ENTITY FramerCtrl_tb IS
END FramerCtrl_tb;
 
ARCHITECTURE behavior OF FramerCtrl_tb IS 
--type ram_type is array (0 to 31) of unsigned(15 downto 0);
--signal mem : ram_type :=
--(
--X"00A3", X"00A0", X"009B", X"009B", X"009D", X"00AA", X"00A8", X"0088",
--X"005E", X"0069", X"006B", X"006C", X"006A", X"0075", X"0078", X"007D",
--X"0082", X"0082", X"0083", X"0083", X"0084", X"0085", X"0086", X"0085",
--X"0084", X"0086", X"0085", X"0083", X"0085", X"0083", X"0087", X"0083"
--);
 

signal dout_rom : unsigned(15 downto 0);
signal x :unsigned(15 downto 0);
--signal din_rht : unsigned(15 downto 0);    
signal addr_rom : unsigned(11 downto 0);
--signal we_rht : std_logic;

signal dout_res : unsigned(15 downto 0);
signal din_res : unsigned(15 downto 0);    
signal addr_res : unsigned(8 downto 0);
signal we_res : std_logic;

signal   left_s, sam_s, right_s, res_s :  signed(15 downto 0);
signal  even_odd_s, even_odd_x, even_odd_r, fwd_inv_s, noupdate_s, updated_s : std_logic;
signal leftlatch_ctrl, samlatch_ctrl, rightlatch_ctrl, sel : STD_LOGIC;
signal left_latch, sam_latch, right_latch, z_o : std_logic_vector(15 downto 0);
   COMPONENT mux
    PORT(      
	     z_o: out std_logic_vector(15 downto 0);
        left_i: in std_logic_vector(15 downto 0);
        right_i: in std_logic_vector(15 downto 0);
        sel : IN  std_logic
        );
	END COMPONENT;  
	 COMPONENT latch
	    port (
        q_o : out std_logic_vector(15 downto 0);
        d_i : in std_logic_vector(15 downto 0);
        g: in std_logic
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
COMPONENT rom is
    port (
        dout_rom: out unsigned(15 downto 0);
        addr_rom: in unsigned(11 downto 0)
    );
end component;
 	 
COMPONENT ram
    PORT(
         dout : OUT  unsigned(15 downto 0) := (others => '0');
         din : IN  unsigned(15 downto 0) := (others => '0');
         addr : IN  unsigned(8 downto 0) := (others => '0');
         we : IN  std_logic;
         clk_fast : IN  std_logic
        );
END COMPONENT;
    -- Component Declaration for the Unit Under Test (UUT)
	 COMPONENT FramerUpdate
	 Port (
        clk : IN  std_logic;
		  addr_i: out unsigned(8 downto 0);
        addr_o: in unsigned(8 downto 0);
		  rd_i : out std_logic;
		  rd_o : in std_logic;
		  wr_i : out std_logic;
		  wr_o : in std_logic
        );
    END COMPONENT; 
    COMPONENT FramerCtrl
    PORT(
         SOF : OUT  std_logic;
         state : inout t_enum_t_State_1;
         syncFlag : IN  std_logic;
         clk : IN  std_logic;
         reset_n : IN  std_logic;
			addr_i: in unsigned(8 downto 0);
         addr_o: inout unsigned(8 downto 0);
			rd_i : in std_logic;
			rd_o : out std_logic;
			wr_i : in std_logic;
			wr_o : out std_logic;
			YES : in std_logic;
			NO : in std_logic
			
        );
    END COMPONENT;
    
	 
	  
   --Inputs
   signal syncFlag : std_logic := '0';
   signal clk : std_logic := '0';
   signal reset_n : std_logic := '0';
	signal addr_i : unsigned(8 downto 0);
	signal wr_i : std_logic := '0';
	signal rd_i : std_logic := '0';
	signal YES : std_logic := '0';
	signal NO : std_logic := '0';
	--BiDirs
   signal state : t_enum_t_State_1;
	
 	--Outputs
	signal wr_o : std_logic := '0';
	signal rd_o : std_logic := '0';
   signal SOF : std_logic;
	signal addr_o : unsigned(8 downto 0);
   -- Clock period definitions
   constant clk_period : time := 10 ns;
 
BEGIN
leftlatch : latch
	port map (
	q_o => left_latch,
	d_i => std_logic_vector(dout_rom),
	g => leftlatch_ctrl
	);
samlatch : latch
	port map (
	q_o => sam_latch,
	d_i => std_logic_vector(dout_rom),
	g => samlatch_ctrl
	);

rightlatch : latch
	port map (
	q_o => right_latch,
	d_i => std_logic_vector(dout_rom),
	g => rightlatch_ctrl
	);
resram : ram
  port map(
     dout => dout_res,
	  din => unsigned(res_s),
	  addr => addr_res,
	  we => we_res,
	  --clk_fast => clk_i
	  clk_fast => clk
	  );	 
urom : rom
  port map(
     dout_rom => dout_rom,
	  addr_rom => addr_rom
	  ); 
	  
ujpeg: jpeg 
	port map( 
		  clk_fast => clk,	
        --clk_fast => clk_i,
        left_s => signed(left_latch),
        right_s => signed(dout_rom),
        sam_s => signed(sam_latch),
        res_s => res_s,
        even_odd_s => even_odd_s,
		  fwd_inv_s => fwd_inv_s,
        updated_s => updated_s,
        noupdate_s => noupdate_s
  		  );		  
	-- Instantiate the Unit Under Test (UUT)
   uut: FramerCtrl PORT MAP (
          SOF => SOF,
          state => state,
          syncFlag => syncFlag,
          clk => clk,
          reset_n => reset_n,
			 addr_i => addr_i,
			 addr_o => addr_o,
			 rd_i => rd_i,
			 wr_i => wr_i,
			 rd_o => rd_o,
			 wr_o => wr_o,
			 YES => YES,
			 NO => NO
			 );
   uFramerUpdate : FramerUpdate
		port map(
		clk => clk,
		addr_i => addr_i,
		addr_o => addr_o,
		rd_i => rd_i,
		wr_i => wr_i,
		rd_o => rd_o,
		wr_o => wr_o
		);
	umux : mux
	port map (
		  z_o => z_o,
	     left_i => left_latch,
		  --right_i => std_logic_vector(right_i),
		  right_i =>  right_latch,
		  --right_i => rightDut_s,
		  sel => sel);	
		  
   -- Clock process definitions
   clk_process :process
   begin
		clk <= '0';
		wait for clk_period/2;
		clk <= '1';
		wait for clk_period/2;
   end process;
 

   -- Stimulus process
   stim_proc: process
   begin		
      -- hold reset state for 100 ns.
      wait for 100 ns;	

      wait for clk_period*10;

      -- insert stimulus here 
		sel <= '1';
		leftlatch_ctrl <= '1';
      addr_rom <=b"000000000000";
		 wait for 10 ns;
--		z_o <= dout_rom;
      wait for 10 ns;
		leftlatch_ctrl <= '0';
		left_s <= signed(z_o);
		
	   wait for 10 ns;
		samlatch_ctrl <= '1';
		addr_rom <=b"000000000001";
		wait for 10 ns;
		samlatch_ctrl <= '0';
		sam_s <= signed(sam_latch);
		
		wait for 10 ns;
		rightlatch_ctrl <= '1';
      addr_rom <=b"000000000010";
		 wait for 10 ns;
--		x <= dout_rom;
      wait for 10 ns;
		rightlatch_ctrl <= '0';
		right_s <= signed(right_latch);
		sel <= '0';
--
--		wait for 10 ns;
-- 
--		
--		wait for 10 ns;	
		
--	   addr_rom <=b"000000000010";
--		right_s <= signed(dout_rom);
		wait for 10 ns;
		
		even_odd_s <= '0';
		updated_s <= '1';
		fwd_inv_s<= '1';
		wait for 10 ns;
		updated_s <= '0';
		
		we_res <= '1';
		
		addr_res <=  b"000000001";

		leftlatch_ctrl <= '1';
      addr_rom <=b"000000000010";
		 wait for 10 ns;
--		x <= dout_rom;
      wait for 10 ns;
		leftlatch_ctrl <= '0';
		left_s <= signed(z_o);
		
	   wait for 10 ns;
		samlatch_ctrl <= '1';
		addr_rom <=b"000000000011";
		wait for 10 ns;
		samlatch_ctrl <= '0';
		sam_s <= signed(sam_latch);
		
		wait for 10 ns;
		rightlatch_ctrl <= '1';
      addr_rom <=b"000000000100";
		 wait for 10 ns;
		x <= dout_rom;
      wait for 10 ns;
		rightlatch_ctrl <= '0';
		right_s <= signed(right_latch);
--
--		wait for 10 ns;
-- 
--		
--		wait for 10 ns;	
		
--	   addr_rom <=b"000000000100";
----		right_s <= signed(dout_rom);
		wait for 10 ns;
		
		even_odd_s <= '0';
		updated_s <= '1';
		fwd_inv_s<= '1';
		wait for 10 ns;
		updated_s <= '0';
		
		we_res <= '1';
		
		addr_res <=  b"000000011";		
--		addr_rom <=b"000000000010";
--		left_s <= signed(left_latch);
--		wait for 10 ns;
--
--	   addr_rom <=b"000000000011";
--		sam_s <= signed(sam_latch);
--		wait for 10 ns;	
		
--	   addr_rom <=b"000000000100";
--		right_s <= signed(dout_rom);
--		wait for 10 ns;
		
 
		wait for 10 ns;
--		updated_s <= '1';
		
		wait for 10 ns;
		
--		updated_s <= '0';
--		addr_res <=  b"000000011";
		
		
 
--		wait for 10 ns;
--		updated_s <= '1';
--		
--		wait for 10 ns;
--		updated_s <= '0';
--		addr_rom <=b"000000000100";
--		left_s <= signed(dout_rom);
--		wait for 10 ns;
--
--	   addr_rom <=b"000000000101";
--		sam_s <= signed(dout_rom);
--		wait for 10 ns;	
--		
--	   addr_rom <=b"000000000110";
--		right_s <= signed(dout_rom);
--		wait for 10 ns;		
--		addr_res <=  b"000000101";
--		reset_n <= '1';
		--wait for 10 ns;
		--reset_n <= '0';
		--wait for 50 ns;
		syncFlag <= '1';
		wait for 400 ns;
		syncFlag <= '0';
		wait for 20 ns;
		reset_n <= '0';
		wait for 20 ns;
		reset_n <= '1';
		wait for 20 ns;
		syncFlag <= '1';
      wait;
   end process;

END;
