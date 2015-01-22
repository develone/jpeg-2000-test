-- TestBench Template 

  LIBRARY ieee;
  USE ieee.std_logic_1164.ALL;
  USE ieee.numeric_std.ALL;
  use work.pck_myhdl_09.all;
  use work.pck_xess_jpeg_para.all;
  ENTITY testbench IS
  END testbench;

  ARCHITECTURE behavior OF testbench IS 
  signal state_r, state_x         : t_enum_t_State_1   := INIT;  -- FSM starts off in init state.
  signal sig_in_r,sig_in_x : unsigned(30 downto 0) := (others => '0');
  signal noupdate_s : std_logic;
 
 
  signal res_s : signed(8 downto 0) := (others => '0');
 
  signal dout_rom : unsigned(30 downto 0):= (others => '0');
  signal  addr_rom_r, addr_rom_x : unsigned(16 downto 0):= (others => '0');
  signal Clk_i : std_logic;
  component xess_jpeg_para is
    port (
        clk_fast: in std_logic;
        state_r: inout t_enum_t_State_1;
        state_x: inout t_enum_t_State_1;
        sig_in_r: inout unsigned(30 downto 0);
        sig_in_x: inout unsigned(30 downto 0);
        noupdate_s: out std_logic;
        res_s: out signed (8 downto 0);
        dout_rom: inout unsigned(30 downto 0);
        addr_rom_r: inout unsigned(16 downto 0);
        addr_rom_x: inout unsigned(16 downto 0)
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
   sig_in_r => sig_in_r,
	sig_in_x => sig_in_x,
   noupdate_s => noupdate_s,
   res_s => res_s,
   state_r => state_r,
	state_x => state_x, 
	dout_rom => dout_rom,
	addr_rom_r => addr_rom_r,
	addr_rom_x => addr_rom_x
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
