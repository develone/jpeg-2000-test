----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date:    17:13:05 10/08/2014 
-- Design Name: 
-- Module Name:    xxx - Behavioral 
-- Project Name: 
-- Target Devices: 
-- Tool versions: 
-- Description: 
--
-- Dependencies: 
--
-- Revision: 
-- Revision 0.01 - File Created
-- Additional Comments: 
--
----------------------------------------------------------------------------------
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.numeric_std.all;
use IEEE.STD_LOGIC_UNSIGNED.ALL;
use std.textio.all;
use work.pck_myhdl_09.all;

-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx primitives in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity xxx is
    Port ( clk_i : in  STD_LOGIC;
	 --addr_res : inout unsigned(8 downto 0);
 
	 left_s  : in signed(15 downto 0);
	 sam_s  : in signed(15 downto 0);
	 right_s  : in signed(15 downto 0);
	 res_s  : inout signed(15 downto 0)
	 --even_odd_s : in  STD_LOGIC;
	 --fwd_inv_s : in  STD_LOGIC;
	 --updated_s : in  STD_LOGIC;
	 --noupdate_s : out  STD_LOGIC;
	 --dout_res : out unsigned(15 downto 0)
	 --reset_sav_s : in std_logic;
	 --addr_res_o: inout unsigned(8 downto 0)
	 --incRes : in std_logic
	 
	 );
end xxx;

architecture Behavioral of xxx is
signal addr_res : unsigned(8 downto 0);
signal we_res : std_logic;
signal dout_res : unsigned(15 downto 0);
signal  din_res : unsigned(15 downto 0);
--
--Signals constants needed by Sdram---------------------------------------  
constant NO                     : std_logic := '0';
constant YES                    : std_logic := '1';
constant ROW_C             : natural   := 63;  -- Number of words in RAM.
constant RAM_SIZE_C             : natural   := 16384;  -- Number of words in RAM.
constant RAM_WIDTH_C            : natural   := 16;  -- Width of RAM words.
constant MIN_ADDR_C             : natural   := 0;  -- Process RAM from this address ...
constant LEFT_ADDR_C             : natural   := 0;  -- Process RAM from this address ...
constant SAM_ADDR_C             : natural   := 1;  -- Process RAM from this address ...
constant RIGHT_ADDR_C             : natural   := 2;  -- Process RAM from this address ...
constant MAX_ADDR_C             : natural   := 8191;  -- ... to this address.
constant MIN_ADDRJPEG_C             : natural   := 8192;  -- Process RAM from this address ...
constant MAX_ADDRJPEG_C             : natural   := 16384;  -- ... to this address.
signal sam_addr_r, sam_addr_x :  natural range 0 to RAM_SIZE_C-1; 

signal updated_r, updated_x : std_logic := '0';
--signal left_s, sam_s, right_s, res_s :  signed(15 downto 0);
signal  even_odd_s, even_odd_x, even_odd_r,  fwd_inv_s, clk_fast : std_logic;
signal updated_s, noupdate_s : std_logic; 
 
signal reset_sav_s, reset_sav_x, reset_sav_r  : std_logic := '0' ;
signal incRes_s, incRes_x, incRes_r : std_logic := '0' ;


 

type state_t is (INIT, READ_AND_SUM_DATA, WRITE_DATA, DONE);  -- FSM states.
signal state_r, state_x         : state_t   := INIT;  -- FSM starts off in init state
signal addr_r, addr_x           : natural range 0 to RAM_SIZE_C-1;  -- RAM address.
COMPONENT ram
    PORT(
         dout : OUT  unsigned(15 downto 0) := (others => '0');
         din : IN  unsigned(15 downto 0) := (others => '0');
         addr : IN  unsigned(8 downto 0) := (others => '0');
         we : IN  std_logic;
         clk_fast : IN  std_logic
        );
END COMPONENT;

COMPONENT save_to_ram
    PORT(
		   clk_fast : in std_logic;
			dout_res_o : OUT  unsigned(15 downto 0) := (others => '0');
			res_i : in signed (15 downto 0);
	      we_s_o : out  std_logic;
			reset_sav_i : in std_logic;
			addr_res_o: inout unsigned(8 downto 0);
			incRes_i: in std_logic;
			odd_i: in std_logic
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
begin
resram : ram
  port map(
     dout => dout_res,
	  din => din_res,
	  addr => addr_res,
	  we => we_res,
	  clk_fast => clk_i
	  --clk_fast => clk_fast
	  );
usave_to_ram : save_to_ram		  
   port map(
	      clk_fast => clk_i,
		   --clk_fast => clk_fast,
			dout_res_o => din_res,
			res_i => res_s,
	      we_s_o => we_res,
			reset_sav_i => reset_sav_s,
			addr_res_o => addr_res,
			incRes_i => incRes_s,
         odd_i => even_odd_s
			); 	

ujpeg: jpeg 
	port map( 
		  --clk_fast => clk_fast,	
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
FsmComb_p : process(state_r,   even_odd_r, reset_sav_r,   sam_addr_r,
							   updated_r, addr_r, incRes_r
							  )	
	begin
   case state_r is

      when INIT =>                      -- Initialize the FSM.
					   
		  if even_odd_r =  YES then
			    sam_addr_x <= 2;
		  else		 
			    sam_addr_x  <=   1;
        end if;
			state_x <= READ_AND_SUM_DATA;    -- and go to next state.
		when READ_AND_SUM_DATA => 
			state_x     <= WRITE_DATA;      -- Go to next state.
		when WRITE_DATA =>
			state_x <= DONE;
		when DONE =>  		
		end case;

  end process;	
FsmUpdate_p : process(clk_i)
  begin
    if rising_edge(clk_i) then
      addr_r      <= addr_x;
      --dataToRam_r <= dataToRam_x;
      state_r     <= state_x;
      --sum_r       <= sum_x;
		--sam_r       <= sam_x;
		
		--right_r     <= right_x;
		sam_addr_r  <= sam_addr_x; 
		
		--dataToRam_res_r  <= dataToRam_res_x;
		--addrjpeg_r      <= addrjpeg_x;
		updated_r <= updated_x;
		--leftDel_r <= leftDel_x;
		--sigDelayed_r <= sigDelayed_x;
		even_odd_r <= even_odd_x;
		reset_sav_r <= reset_sav_x;
		incRes_r <= incRes_x;
      --left_r      <= left_x;		
		
		
    end if;
  end process; 
  reset_sav_s <= reset_sav_r;
  even_odd_s <= even_odd_r;
  updated_s <= updated_r;  
end Behavioral;

