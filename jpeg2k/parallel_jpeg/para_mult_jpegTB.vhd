-- TestBench Template 

  LIBRARY ieee;
  USE ieee.std_logic_1164.ALL;
  USE ieee.numeric_std.ALL;
  use work.pck_myhdl_09.all;
 
  ENTITY testbench IS
  END testbench;

  ARCHITECTURE behavior OF testbench IS 
    signal sig0_in_x,sig1_in_x, sig2_in_x,sig3_in_x : unsigned(30 downto 0) := (others => '0');
  signal noupdate0_s, noupdate1_s, noupdate2_s, noupdate3_s : std_logic;
 
 
  signal res0_s, res1_s, res2_s, res3_s : signed(8 downto 0) := (others => '0');

  signal sig4_in_x,sig5_in_x, sig6_in_x,sig7_in_x : unsigned(30 downto 0) := (others => '0');
  signal noupdate4_s, noupdate5_s, noupdate6_s, noupdate7_s : std_logic;
 
 
  signal res4_s, res5_s, res6_s, res7_s : signed(8 downto 0) := (others => '0'); 
  signal Clk_i : std_logic;
 component multi_jpeg is
    port (
        clk_fast: in std_logic;
        sig0_in_x: in unsigned(30 downto 0);
        noupdate0_s: out std_logic;
        res0_s: out signed (8 downto 0);
        sig1_in_x: in unsigned(30 downto 0);
        noupdate1_s: out std_logic;
        res1_s: out signed (8 downto 0);
        sig2_in_x: in unsigned(30 downto 0);
        noupdate2_s: out std_logic;
        res2_s: out signed (8 downto 0);
        sig3_in_x: in unsigned(30 downto 0);
        noupdate3_s: out std_logic;
        res3_s: out signed (8 downto 0)
    );
end component multi_jpeg;
  -- Component Declaration
          COMPONENT para_multi_jpeg
          PORT(
                  Clk_i : IN std_logic
 
                  );
          END COMPONENT;

 
 constant Clk_i_period : time := 83.3333 ns; -- 12 MHz XuLA clock.        

  BEGIN

  -- Component Instantiation
          uut: para_multi_jpeg PORT MAP(
                  Clk_i => clk_i
             
          );
multi_jpeg_u0 : multi_jpeg
  port map(
   clk_fast => Clk_i,

	sig0_in_x => sig0_in_x,
   noupdate0_s => noupdate0_s,
   res0_s => res0_s,
	
	sig1_in_x => sig1_in_x,
   noupdate1_s => noupdate1_s,
   res1_s => res1_s,
 
	sig2_in_x => sig2_in_x,
   noupdate2_s => noupdate2_s,
   res2_s => res2_s,
	
	sig3_in_x => sig3_in_x,
   noupdate3_s => noupdate3_s,
   res3_s => res3_s
);
multi_jpeg_u1 : multi_jpeg
  port map(
   clk_fast => Clk_i,

	sig0_in_x => sig4_in_x,
   noupdate0_s => noupdate4_s,
   res0_s => res4_s,
	
	sig1_in_x => sig5_in_x,
   noupdate1_s => noupdate5_s,
   res1_s => res5_s,
 
	sig2_in_x => sig6_in_x,
   noupdate2_s => noupdate6_s,
   res2_s => res6_s,
	
	sig3_in_x => sig7_in_x,
   noupdate3_s => noupdate7_s,
   res3_s => res7_s
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
	   sig0_in_x <= "0000000000000000000000000000000";
		sig1_in_x <= "0000000000000000000000000000000";
		sig2_in_x <= "0000000000000000000000000000000";
		sig3_in_x <= "0000000000000000000000000000000";
		sig4_in_x <= "0000000000000000000000000000000";
		sig5_in_x <= "0000000000000000000000000000000";
		sig6_in_x <= "0000000000000000000000000000000";
		sig7_in_x <= "0000000000000000000000000000000";
      wait for 80 ns;
		sig0_in_x <= "0111010100100010101100010100101";
		sig1_in_x <= "0111010011100010011100010100100";
		sig2_in_x <= "0111010100100010111100010011100";
		sig3_in_x <= "0111010011101010011100010100100";
		sig4_in_x <= "0111010011111010011100010011100";
		sig5_in_x <= "0111010011111110011100010011100";
		sig6_in_x <= "0111011111100010011100010011100";
		sig7_in_x <= "0111110011100010011100010011100";
		wait for 80 ns;
		sig0_in_x <= "0000000000000000000000000000000";
		sig1_in_x <= "0000000000000000000000000000000";
		sig2_in_x <= "0000000000000000000000000000000";
		sig3_in_x <= "0000000000000000000000000000000";
		sig4_in_x <= "0000000000000000000000000000000";
		sig5_in_x <= "0000000000000000000000000000000";
		sig6_in_x <= "0000000000000000000000000000000";
		sig7_in_x <= "0000000000000000000000000000000";
      wait for 80 ns;
		sig0_in_x <= "0101010100100010101100010100101";
		sig1_in_x <= "0101010011100010011100010100100";
		sig2_in_x <= "0101010100100010111100010011100";
		sig3_in_x <= "0101010011101010011100010100100";
		sig4_in_x <= "0101010011111010011100010011100";
		sig5_in_x <= "0101010011111110011100010011100";
		sig6_in_x <= "0101011111100010011100010011100";
		sig7_in_x <= "0101110011100010011100010011100";
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
