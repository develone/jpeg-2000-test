-- TestBench Template 

  LIBRARY ieee;
  USE ieee.std_logic_1164.ALL;
  USE ieee.numeric_std.ALL;
  use work.pck_myhdl_09.all;
  ENTITY testbench IS
  END testbench;

  ARCHITECTURE behavior OF testbench IS 
  signal sig_in : unsigned(27 downto 0) := (others => '0');
  signal noupdate_s : std_logic;
  signal rdy : std_logic;
  signal addr_not_reached : std_logic;
  signal res_s : signed(7 downto 0) := (others => '0');
  signal res_u : unsigned(7 downto 0) := (others => '0');
  signal jp_lf : unsigned(7 downto 0) := (others => '0');
  signal jp_sa: unsigned(7 downto 0) := (others => '0');
  signal jp_rh : unsigned(7 downto 0) := (others => '0');
  signal jp_flgs : unsigned(3 downto 0) := (others => '0');
  signal Clk_i : std_logic;
  component xess_jpeg_para is
    port (
        clk_fast: in std_logic;
        sig_in: inout unsigned(27 downto 0);
        noupdate_s: out std_logic;
        res_s: inout signed (7 downto 0);
        res_u: out unsigned(7 downto 0);
        jp_lf: in unsigned(7 downto 0);
        jp_sa: in unsigned(7 downto 0);
        jp_rh: in unsigned(7 downto 0);
        jp_flgs: in unsigned(3 downto 0);
        rdy: in std_logic;
        addr_not_reached: in std_logic
    );
end component xess_jpeg_para;
  -- Component Declaration
          COMPONENT para_jpeg
          PORT(
                  Clk_i : IN std_logic
 
                  );
          END COMPONENT;

 
 constant Clk_i_period : time := 83.3333 ns; -- 12 MHz XuLA clock.        

  BEGIN

  -- Component Instantiation
          uut: para_jpeg PORT MAP(
                  Clk_i => clk_i
             
          );

xess_jpeg_para_u0 : xess_jpeg_para
  port map(
   clk_fast => Clk_i,
   sig_in => sig_in,
   noupdate_s => noupdate_s,
   res_s => res_s,
   jp_lf => jp_lf,
   jp_sa => jp_sa,
   jp_rh => jp_rh,
	jp_flgs => jp_flgs,
   rdy => rdy,
   addr_not_reached => addr_not_reached
); 
   Clk_i_process :process
   begin
		Clk_i <= '0';
		wait for Clk_i_period/2;
		Clk_i <= '1';
		wait for Clk_i_period/2;
   end process;
	   stim_proc: process
   begin		
      -- hold reset state for 100 ns.
      wait for 100 ns;	

      wait for Clk_i_period*10;

      -- insert stimulus here 
     jp_lf <= to_unsigned(125,8);
	  jp_sa <= to_unsigned(120,8);
	  jp_rh <= to_unsigned(128,8);
	  jp_flgs <= to_unsigned(7,4);
	  rdy <= '1';
	  addr_not_reached <= '1';
	  wait for 20 ns;
	  
--	  addr_not_reached <= '0';
--	  wait for 10 ns;
--	  rdy <= '0';
      wait;
   end process;
--  Test Bench Statements
     tb : PROCESS
     BEGIN

        wait for 100 ns; -- wait until global set/reset completes

        -- Add user defined stimulus here

        wait; -- will wait forever
     END PROCESS tb;
  --  End Test Bench 

  END;
