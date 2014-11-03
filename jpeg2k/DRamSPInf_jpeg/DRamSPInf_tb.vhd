--------------------------------------------------------------------------------
-- Company: 
-- Engineer:
--
-- Create Date:   21:25:53 12/29/2011
-- Design Name:   
-- Module Name:   C:/xesscorp/PRODUCTS/TUTORIALS/FpgasNowWhat/Chapters/Rams/FPGA/DRamSPInf/DRamSPInf_tb.vhd
-- Project Name:  DRamSPInf
-- Target Device:  
-- Tool versions:  
-- Description:   
-- 
-- VHDL Test Bench Created by ISE for module: DRamSPInf
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
use IEEE.NUMERIC_STD.all;
 
-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--USE ieee.numeric_std.ALL;
 
ENTITY DRamSPInf_tb IS
END DRamSPInf_tb;
 
ARCHITECTURE behavior OF DRamSPInf_tb IS 
 
    -- Component Declaration for the Unit Under Test (UUT)
 
    COMPONENT DRamSPInf
    PORT(
         clk_i : IN  std_logic;
         sum_o : OUT  std_logic_vector(31 downto 0)
        );
    END COMPONENT;
    

   --Inputs
   signal clk_i : std_logic := '0';

 	--Outputs
   signal sum_o : std_logic_vector(31 downto 0);

   -- Clock period definitions
   constant clk_i_period : time := 10 ns;
component FILE_READ 
  generic (
           stim_file:       string  := "sim.dat"
          );
  port(
       CLK              : in  std_logic;
       RST              : in  std_logic;
       Y                : out std_logic_vector(15 downto 0);
       EOG              : out std_logic
      );
end component; 

signal rst:  std_logic;
--signal clk:  std_logic := '0';
signal eog:  std_logic;
signal y:    std_logic_vector(15 downto 0);
  constant NO          : std_logic := '0';
  constant YES         : std_logic := '1';
  constant RAM_SIZE_C  : natural   := 48;  -- Number of words in RAM.
  constant RAM_WIDTH_C : natural   := 16;   -- Width of RAM words.
  constant MIN_ADDR_C  : natural   := 1;   -- Process RAM from this address ...
  constant MAX_ADDR_C  : natural   := 5;   -- ... to this address.
  subtype RamWord_t is unsigned(RAM_WIDTH_C-1 downto 0);   -- RAM word type.
  type Ram_t is array (0 to RAM_SIZE_C-1) of RamWord_t;  -- array of RAM words type.
  signal ram_r         : Ram_t;         -- RAM declaration.
  signal wr_s          : std_logic;     -- Write-enable control.
  signal addr_r        : natural range 0 to RAM_SIZE_C-1;  -- RAM address.
  signal dataToRam_r   : RamWord_t;     -- Data to write to RAM.
  signal dataFromRam_s : RamWord_t;     -- Data read from RAM.
  signal sum_r         : natural range 0 to RAM_SIZE_C * (2**RAM_WIDTH_C) - 1;
BEGIN
--rst <= '0', '1' after 40 ns, '0' after 100 ns; 
input_stim: FILE_READ 
  port map(
       CLK      => clk_i,
       RST      => rst,
       Y        => y,
       EOG      => eog
      ); 
		
	-- Instantiate the Unit Under Test (UUT)
   uut: DRamSPInf PORT MAP (
          clk_i => clk_i,
          sum_o => sum_o
        );
--*********************************************************************
  -- RAM is inferred from this process.
  --*********************************************************************
  Ram_p : process (clk_i)
  begin
    -- Write to the RAM at the given address if the write-enable is high.
    if rising_edge(clk_i) then
      if wr_s = YES then
        ram_r(addr_r) <= dataToRam_r;
      end if;
    end if;
  end process;
  -- Continually read from whatever RAM address is present.
  dataFromRam_s <= ram_r(addr_r);
   -- Clock process definitions
   clk_i_process :process
   begin
		clk_i <= '0';
		wait for clk_i_period/2;
		clk_i <= '1';
		wait for clk_i_period/2;
   end process;
 
 --*********************************************************************
  -- State machine that initializes RAM and then reads RAM to compute
  -- the sum of products of the RAM address and data.
  --*********************************************************************
  Fsm_p : process (clk_i)
    type state_t is (INIT, WRITE_DATA, READ_AND_SUM_DATA, DONE);
    variable state_v : state_t := INIT;    -- Start off in init state.
  begin
    if rising_edge(clk_i) then
      case state_v is
        when INIT =>
          wr_s        <= YES;           -- Enable writing of RAM.
			 rst <= YES; 
          addr_r      <= MIN_ADDR_C;    -- Start writing data at this address.
          --dataToRam_r <= TO_UNSIGNED(1, RAM_WIDTH_C);  -- Initial value to write.
          state_v     := WRITE_DATA;    -- Go to next state.
        when WRITE_DATA =>

			 if (rst = YES) then
				addr_r      <= MIN_ADDR_C - 1;
				rst <= NO after 40 ns;
			 elsif (eog = NO)  then   -- If haven't reach final address ...
					dataToRam_r <= RamWord_t(y);
               if addr_r <= RAM_SIZE_C then 
						addr_r      <= addr_r + 1;  -- go to next address ...
					end if; 
            
            --dataToRam_r <= dataToRam_r + 3;            -- and write this value.
				
          else  -- Else, the final address has been written...
			     wr_s    <= NO;              -- so turn off writing, ...
              addr_r  <= MIN_ADDR_C;      -- go back to the start, ...
              sum_r   <= 0;               -- clear the sum-of-products, ...
              state_v := READ_AND_SUM_DATA;  -- and go to next state.
			
          end if;
        when READ_AND_SUM_DATA =>
          if addr_r <= MAX_ADDR_C then  -- If haven't reached final address ...
            -- add product of RAM address and data read 
            -- from RAM to the summation ...
            sum_r  <= sum_r + TO_INTEGER(dataFromRam_s * addr_r);
            addr_r <= addr_r + 1;       -- and go to next address.
          else  -- Else, the final address has been read ...
            state_v := DONE;            -- so go to the next state.
          end if;
        when DONE =>                    -- Summation complete ...
          null;                         -- so wait here and do nothing.
        when others =>                  -- Erroneous state ...
          state_v := INIT;              -- so re-run the entire process.
      end case;
    end if;
  end process;
   -- Stimulus process
   stim_proc: process
   begin		
      -- hold reset state for 100 ns.
      wait for 100 ns;	

      wait for clk_i_period*10;

      -- insert stimulus here 

      wait;
   end process;

END;
