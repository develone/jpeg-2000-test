--------------------------------------------------------------------------------
-- Company: 
-- Engineer:
--
-- Create Date:   08:33:57 03/24/2015
-- Design Name:   
-- Module Name:   C:/Xilinx/14.7/ISE_DS/jpeg_para/tbjp_procesvhd.vhd
-- Project Name:  jpeg_para
-- Target Device:  
-- Tool versions:  
-- Description:   
-- 
-- VHDL Test Bench Created by ISE for module: jp_process
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
-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--USE ieee.numeric_std.ALL;
 
ENTITY tbjp_procesvhd IS
END tbjp_procesvhd;
 
ARCHITECTURE behavior OF tbjp_procesvhd IS 
 
    -- Component Declaration for the Unit Under Test (UUT)
    COMPONENT signed2twoscomplement 
    port (
        bits_in_sig: in signed (9 downto 0);
        vv: out unsigned(8 downto 0)
    );
	 END COMPONENT;
    COMPONENT jp_process
    PORT(
         res_out_x : OUT  signed(9 downto 0);
         left_s_i : IN  unsigned(143 downto 0);
         sam_s_i : IN  unsigned(143 downto 0);
         right_s_i : IN  unsigned(143 downto 0);
         flgs_s_i : IN  unsigned(79 downto 0);
         noupdate_s : OUT  std_logic;
         update_s : IN  std_logic
        );
    END COMPONENT;
	 
    COMPONENT rom_flgs 
    port (
        dout_flgs: out unsigned(79 downto 0);
        addr_flgs: in unsigned(9 downto 0)
    );
    END COMPONENT;
    
	 COMPONENT ram
    port (
        dout: out unsigned(143 downto 0);
        din: in unsigned(143 downto 0);
        addr: in unsigned(9 downto 0);
        we: in std_logic;
        clk_fast: in std_logic
    );
	 END COMPONENT;
	 
	 COMPONENT ram_res 
    port (
        dout_res: out unsigned(8 downto 0);
        din_res: in unsigned(8 downto 0);
        addr_res: in unsigned(9 downto 0);
        we_res: in std_logic;
        clk_fast: in std_logic
    );
    END COMPONENT;
	 
	 COMPONENT m_flatten 
    port (
        flat: out unsigned(143 downto 0)
    );
    end COMPONENT;
   --Inputs
   signal left_s_i : unsigned(143 downto 0) := (others => '0');
   signal sam_s_i : unsigned(143 downto 0) := (others => '0');
   signal right_s_i : unsigned(143 downto 0) := (others => '0');
   signal flgs_s_i : unsigned(79 downto 0) := (others => '0');
	
   signal din_lf : unsigned(143 downto 0) := (others => '0');
   signal din_sa : unsigned(143 downto 0) := (others => '0');
   signal din_rt : unsigned(143 downto 0) := (others => '0');
	signal din_res : unsigned(8 downto 0) := (others => '0');
	
   signal update_s : std_logic := '0';
   signal clk_fast : std_logic := '0';
	signal we_lf : std_logic := '0';
	signal we_sa : std_logic := '0';
	signal we_rt : std_logic := '0';
	signal we_res : std_logic := '0';
	
   signal    addr_flgs: unsigned(9 downto 0);
	signal    addr_lf: unsigned(9 downto 0);
	signal    addr_sa: unsigned(9 downto 0);
	signal    addr_rt: unsigned(9 downto 0);
	signal    addr_res: unsigned(9 downto 0);
	signal bits_in_sig: signed (9 downto 0);
   signal vv:  unsigned(8 downto 0);
   signal z : unsigned(8 downto 0):= (others => '0');
   signal x : signed (9 downto 0);
   signal ma_row: unsigned(3 downto 0);
   signal ma_col: unsigned(3 downto 0);
	
 	--Outputs
   signal res_out_x : signed(9 downto 0);
   signal noupdate_s : std_logic;
	signal dout_flgs: unsigned(79 downto 0);
	
	signal dout_lf : unsigned(143 downto 0) := (others => '0');
   signal dout_sa : unsigned(143 downto 0) := (others => '0');
   signal dout_rt : unsigned(143 downto 0) := (others => '0');
	signal dout_res : unsigned(8 downto 0) := (others => '0');
	
	signal flat_lf : unsigned(143 downto 0) := (others => '0');
	signal flat_sa : unsigned(143 downto 0) := (others => '0');
	signal flat_rt : unsigned(143 downto 0) := (others => '0');
	
	type t11 is array (0 to 3) of unsigned(9 downto 0);
	type t1 is array (0 to 3) of t11;
	signal flat_i : t1:=(others => (others => (others => '0')));
	
   -- No clocks detected in port list. Replace <clock> below with 
   -- appropriate port name 
 
 
    constant clk_fast_period : time := 10 ns;
BEGIN
 
	-- Instantiate the Unit Under Test (UUT)
   uut: jp_process PORT MAP (
          res_out_x => res_out_x,
          left_s_i => left_s_i,
          sam_s_i => sam_s_i,
          right_s_i => right_s_i,
          flgs_s_i => flgs_s_i,
          noupdate_s => noupdate_s,
          update_s => update_s
        );
   uut_rom_flgs : rom_flgs PORT MAP (
	      dout_flgs => dout_flgs,
	      addr_flgs => addr_flgs
	     );
   uut_ram_lf : ram PORT MAP (
	      dout => dout_lf,
			din  => din_lf,
			addr => addr_lf,
			we => we_lf,
			clk_fast => clk_fast
		);
   uut_ram_sa : ram PORT MAP (
	      dout => dout_sa,
			din  => din_sa,
			addr => addr_sa,
			we => we_sa,
			clk_fast => clk_fast
		);	
		
	   uut_ram_rt : ram PORT MAP (
	      dout => dout_rt,
			din  => din_rt,
			addr => addr_rt,
			we => we_rt,
			clk_fast => clk_fast
		);	
		
		uut_ram_res : ram_res PORT MAP (
	      dout_res => dout_res,
			din_res  => din_res,
			addr_res => addr_res,
			we_res => we_res,
			clk_fast => clk_fast
		);	
		
		m_flatten_lf_u1 : m_flatten PORT MAP (
         flat => flat_lf
		);
		
		m_flatten_lf_u2 : m_flatten PORT MAP (
         flat => flat_sa
      );
		
		m_flatten_lf_u3 : m_flatten PORT MAP (
         flat => flat_rt
      );
    signed2twoscomplement_u1 : signed2twoscomplement PORT MAP (
	      bits_in_sig => bits_in_sig,
			vv => vv
	 );
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

--      wait for <clock>_period*10;

      -- insert stimulus here 
	  wait for 10 ns;
	  ma_col <= "0011";
	  wait for 10 ns;
	  ma_row <= "0011";
--	  testing -1 to x
	  x <= "1111111111";
	  wait for 10 ns;
	  bits_in_sig <= x;
	  wait for 10 ns;
	  z <= vv;
	  wait for 10 ns;
--	  testing -2 to x
     x <= "1111111110";
	  wait for 10 ns;
	  bits_in_sig <= x;
	  wait for 10 ns;
	  z <= vv;
	  wait for 10 ns;
	  
--	  testing 258 to x
	  x <= "0100000010";
	  wait for 10 ns;
	  bits_in_sig <= x;
	  wait for 10 ns;
	  z <= vv;
	  wait for 10 ns;
--	  testing 110 to x
     x <= "0001101110";
	  wait for 10 ns;
	  bits_in_sig <= x;
	  wait for 10 ns;
	  z <= vv;
	  wait for 10 ns;
--	  lines 259-290
--	  are to test the matrix flat_i
--	  flat_i(3)(3)  <= "0000000001";
--	  wait for 10 ns;
--	  flat_i(3)(2)  <= "0010100010";
--	  wait for 10 ns;
--	  flat_i(3)(1)  <= "0010100011";
--	  wait for 10 ns;
--	  flat_i(3)(0)  <= "0010100100";
--	  wait for 10 ns;
--	  flat_i(2)(3)  <= "0010100001";
--	  wait for 10 ns;
--	  flat_i(2)(2)  <= "0010100010";
--	  wait for 10 ns;
--	  flat_i(2)(1)  <= "0010100011";
--	  wait for 10 ns;
--	  flat_i(2)(0)  <= "0010100100";
--	  wait for 10 ns;	  
--	  flat_i(1)(3)  <= "0000000001";
--	  wait for 10 ns;
--	  flat_i(1)(2)  <= "0110100010";
--	  wait for 10 ns; 
--	  flat_i(1)(1)  <= "0110100011";
--	  wait for 10 ns;
--	  flat_i(1)(0)  <= "0110100100";
--	  wait for 10 ns;
--	  flat_i(0)(3)  <= "0110100001";
--	  wait for 10 ns;
--	  flat_i(0)(2)  <= "0110100010";
--	  wait for 10 ns;
--	  flat_i(0)(1)  <= "0110100011";
--	  wait for 10 ns;
--	  flat_i(0)(0)  <= "0110100100";
	  wait for 10 ns;	  	  
	  addr_lf <= b"0000000000";
	  wait for 10 ns;
	  addr_sa <= b"0000000000";
	  wait for 10 ns;
	  addr_rt <= b"0000000000";
	  wait for 10 ns;
	  addr_flgs <= b"0000000000";
	  wait for 10 ns;
	  we_lf <= '1';
	  wait for 10 ns;
     we_sa <= '1';
	  wait for 10 ns;
     we_sa <= '1';
	  wait for 10 ns;
     we_rt <= '1';
	  wait for 10 ns;
     we_res <= '1';
	  wait for 10 ns;
     din_lf <= x"1a0d068341a0b088542e0b0581c120905824";
	  wait for 10 ns;
	  din_sa <= x"160b068341a0b068442a1106824120b05824";
	  wait for 10 ns;
	  din_rt <= x"160b068341a0d058442a170582c0e090482c";
	  wait for 10 ns;
	  we_lf <= '0';
	  wait for 10 ns;
	  we_sa <= '0';
     wait for 10 ns;
	  wait for 10 ns;
	  we_rt <= '0';
	  left_s_i <= dout_lf;
	  wait for 10 ns;
	  sam_s_i <=dout_sa;
	  wait for 10 ns;
	  right_s_i <= dout_rt;

	  wait for 10 ns;
	  flgs_s_i <= dout_flgs;
	  wait for 10 ns;
	  addr_res <= b"0000000000";
	  wait for 10 ns;
	  update_s <= '1';
	  wait for 10 ns;
	  bits_in_sig <= res_out_x;
	  wait for 10 ns;
	  din_res <= vv;
	  wait for 10 ns;
	  update_s <= '0';
	  wait for 10 ns;
	  addr_res <= b"0000000001";
	  wait for 10 ns;
	  addr_flgs <= b"0000010000";
	  wait for 10 ns;
	  flgs_s_i <= dout_flgs;
	  wait for 10 ns;
	  update_s <= '1';
	  wait for 10 ns;
	  wait for 10 ns;
	  bits_in_sig <= res_out_x;
	  wait for 10 ns;
	  din_res <= vv;
	  wait for 10 ns;
	  update_s <= '0';
	  wait for 10 ns;
      wait;
   end process;

END;
