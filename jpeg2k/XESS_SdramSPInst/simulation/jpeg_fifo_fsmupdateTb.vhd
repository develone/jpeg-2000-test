-- TestBench Template 

  LIBRARY ieee;
  USE ieee.std_logic_1164.ALL;

use IEEE.numeric_std.all;
use std.textio.all;

use work.pck_myhdl_09.all;
  ENTITY testbench IS
  END testbench;

  ARCHITECTURE behavior OF testbench IS 

  -- Component Declaration
   Component jpeg_fifo_fsmupdate
    port (
        clk_fast: in std_logic;
        empty_r: out std_logic;
        full_r: out std_logic;
        enr_r: inout std_logic;
        enw_r: inout std_logic;
        dataout_r: out unsigned(15 downto 0);
        datain_r: out unsigned(15 downto 0);
        empty_x: inout std_logic;
        full_x: inout std_logic;
        enr_x: in std_logic;
        enw_x: in std_logic;
        dataout_x: inout unsigned(15 downto 0);
        datain_x: in unsigned(15 downto 0)
    );
end  Component;
 
          
        signal clk_fast:  std_logic:= '0';
        --signal readptr:  unsigned(7 downto 0):= (others => '0');
        --signal writeptr:  unsigned(7 downto 0):= (others => '0');
        signal empty_r:  std_logic:= '0';
        signal full_r:  std_logic:= '0';
        signal enr_r:  std_logic:= '0';
        signal enw_r:  std_logic:= '0';
        signal dataout_r:  unsigned(15 downto 0):= (others => '0');
        signal datain_r:  unsigned(15 downto 0):= (others => '0');
		  signal empty_x:  std_logic:= '0';
        signal full_x:  std_logic:= '0';
        signal enr_x:  std_logic:= '0';
        signal enw_x:  std_logic:= '0';
        signal dataout_x:  unsigned(15 downto 0):= (others => '0');
        signal datain_x:  unsigned(15 downto 0):= (others => '0');
		    -- Clock period definitions
        constant clk_fast_period : time := 10 ns;
  BEGIN

  -- Component Instantiation
          uut: jpeg_fifo_fsmupdate PORT MAP(
                  clk_fast => clk_fast,
--                readptr => readptr,
--						writeptr => writeptr,
						empty_r => empty_r,
						full_r => full_r,
						enr_r => enr_r,
						enw_r => enw_r,
						dataout_r => dataout_r,
						datain_r => datain_r,
						empty_x => empty_x,
						full_x => full_x,
						enr_x => enr_x,
						enw_x => enw_x,
						dataout_x => dataout_x,
						datain_x => datain_x
          );

  -- Clock process definitions
   clk_fast_process :process
   begin
		clk_fast <= '0';
		wait for clk_fast_period/2;
		clk_fast <= '1';
		wait for clk_fast_period/2;
   end process;
  --  Test Bench Statements
     tb : PROCESS
     BEGIN

        wait for 100 ns; -- wait until global set/reset completes

        -- Add user defined stimulus here
enw_x <= '1';
datain_x <= X"0001";
wait for 20 ns;
enw_x <= '0';
wait for 20 ns;
enw_x <= '1';
datain_x <= X"0002";
wait for 20 ns;

enw_x <= '1';
datain_x <= X"0003";
wait for 20 ns;
enw_x <= '0';
wait for 20 ns;
enw_x <= '1';
datain_x <= X"0004";
wait for 20 ns;
enw_x <= '0';
wait for 20 ns;
enr_x <= '1';
wait for 20 ns;
enr_x <= '0';
wait for 20 ns;
enr_x <= '1';
wait for 20 ns;
enr_x <= '0';
enw_x <= '0';
wait for 20 ns;
enr_x <= '1';
wait for 20 ns;
enr_x <= '0';
wait for 20 ns;
enr_x <= '1';
wait for 20 ns;
enr_x <= '0';
        wait; -- will wait forever
     END PROCESS tb;
  --  End Test Bench 

  END;
