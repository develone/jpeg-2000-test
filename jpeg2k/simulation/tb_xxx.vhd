-- TestBench Template 

  LIBRARY ieee;
  USE ieee.std_logic_1164.ALL;
  USE ieee.numeric_std.ALL;

  ENTITY tb_xxx IS
  END tb_xxx;

  ARCHITECTURE behavior OF tb_xxx IS

   component xxx   
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
	 --reset_sav : in std_logic;
	 --incRes : in std_logic
	 
	 );
	 
end component;
signal we_res : std_logic;
--
--signal left_s, sam_s, right_s, res_s :  signed(15 downto 0);
--signal  even_odd_s, fwd_inv_s, clk_fast : std_logic;
--signal updated_s, noupdate_s : std_logic; 
--signal dout_res : unsigned(15 downto 0);
--signal din_res : unsigned(15 downto 0);    
signal addr_res : unsigned(8 downto 0);
--signal we_res : std_logic;
--signal  din_res : unsigned(15 downto 0);
signal dout_res : unsigned(15 downto 0) := (others => '0');
--signal reset_sav_s : std_logic := '0' ;
--signal incRes : std_logic := '0' ;
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
--signal sam_addr_r, sam_addr_x :  natural range 0 to RAM_SIZE_C-1; 

--signal updated_r, updated_x : std_logic := '0';
--signal left_s, sam_s, right_s, res_s :  signed(15 downto 0);
--signal  even_odd_s, even_odd_x, even_odd_r,  fwd_inv_s, clk_fast : std_logic;
--signal updated_s, noupdate_s : std_logic; 
 
--signal reset_sav_s, reset_sav_x, reset_sav_r  : std_logic := '0' ;
--signal updated_s, noupdate_s : std_logic; 
signal sam_addr_r, sam_addr_x :  natural range 0 to RAM_SIZE_C-1; 

signal updated_r, updated_x : std_logic := '0';
--signal left_s, sam_s, right_s, res_s :  signed(15 downto 0);
signal  even_odd_s, even_odd_x, even_odd_r,  fwd_inv_s, clk_fast : std_logic;
signal updated_s, noupdate_s : std_logic; 
 
signal reset_sav_s, reset_sav_x, reset_sav_r  : std_logic := '0' ;
signal incRes_s, incRes_x, incRes_r : std_logic := '0' ;

signal  din_res : unsigned(15 downto 0);		 
type state_t is (INIT, ODD_SAMPLES, EVEN_SAMPLES, WRITE_DATA, DONE);  -- FSM states.
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
			odd_i : in std_logic
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
	    signal clk_i : std_logic := '0' ;

 
   --signal even_odd_s : std_logic := '0' ; 
   --signal fwd_inv_s : std_logic := '0' ;
 --  signal updated_s : std_logic := '0' ;
   --signal noupdate_s : std_logic := '0' ;
   signal left_s, sam_s, right_s, res_s : signed(15 downto 0);

 
 
       constant clk_i_period : time := 10 ns;  

  BEGIN
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
  -- Component Instantiation
          uut: xxx PORT MAP(
                   clk_i => clk_i,
						 --addr_res => addr_res,
        left_s => left_s,
        right_s => right_s,
        sam_s => sam_s,
        res_s => res_s
		  --even_odd_s => even_odd_s,
		  --fwd_inv_s  => fwd_inv_s,
		  --updated_s =>  updated_s,
		  --noupdate_s =>  noupdate_s,
		  --reset_sav => reset_sav,
		  --incRes => incRes
		  --odd => even_odd_s
          );
   clk_i_process :process
   begin
		clk_i <= '0';
		wait for clk_i_period/2;
		clk_i <= '1';
		wait for clk_i_period/2;
   end process;
FsmComb_p : process(state_r,   even_odd_r, reset_sav_r,   sam_addr_r,
							   updated_r, addr_r, incRes_r
							  )	
	begin
		 even_odd_x  <= NO; --wkg on odd samples
	    reset_sav_x <= YES; --ram addr 1 set to odd
		 addr_x      <= addr_r;
   case state_r is

      when INIT =>                      -- Initialize the FSM.
					   
		  if even_odd_r =  YES then
			    sam_addr_x <= 2;
		  else		 
			    sam_addr_x  <=   1;
        end if;
		  addr_x  <=   0;
			state_x <= ODD_SAMPLES;    -- and go to next state.
		when ODD_SAMPLES => 
		   reset_sav_x <= NO;
			even_odd_x <= NO;
         if addr_r <= (MIN_ADDR_C + 62) then
            --sam_addr_r = sam_addr_r + 1;
				addr_x <= addr_r + 1;         -- and go to next address.
				sam_addr_x <= sam_addr_r + 2;
				incRes_x <= YES;
         elsif addr_r = (MIN_ADDR_C + 63) then
            sam_addr_x <= 2;
            even_odd_x <= YES;
				reset_sav_x <= YES;
            addr_x <= 0;				
			   state_x     <= EVEN_SAMPLES;      -- Go to next state.
			end if;
		when EVEN_SAMPLES => 
		   reset_sav_x <= NO;
			even_odd_x <= YES;
         if addr_r <= (MIN_ADDR_C + 62) then
            --sam_addr_r = sam_addr_r + 1;
				addr_x <= addr_r + 1;         -- and go to next address.
				sam_addr_x <= sam_addr_r + 2;
         elsif addr_r = (MIN_ADDR_C + 63) then	
			   state_x     <= WRITE_DATA;      -- Go to next state.
			end if;				
		when WRITE_DATA =>
		   --even_odd_x <= YES;
			state_x <= DONE;
		when DONE =>  
        	state_x <= INIT;
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
  --incRes_s <= incRes_r;
  
  --  Test Bench Statements
     tb : PROCESS
     BEGIN

        wait for 100 ns; -- wait until global set/reset completes

        -- Add user defined stimulus here

        wait; -- will wait forever
     END PROCESS tb;
  --  End Test Bench 
   stim_proc: process
   begin		
      -- hold reset state for 100 ns.
      wait for 100 ns;	

      wait for clk_i_period*10;

      -- insert stimulus here 
		--reset_sav_s <= reset_sav_r;
		--incRes <= '0';
		--odd <= '0';
		--even_odd_s <= '0';
		wait for 40 ns;
		--reset_sav_s <= '1';
		wait for 40 ns; 
		--reset_sav_s <= '0';
		left_s <= x"00A3";
		sam_s <= x"00A0";
		right_s <= x"009B";
		
		fwd_inv_s <= '1';
		---updated_s <= '1';
		wait for 40 ns;
		--incRes <= '1';
		wait for 10ns;
		--incRes <= '0';
		 
		wait for 20ns;
	   left_s <= x"009B";
		sam_s <= x"009D";
		right_s <= x"0090";
		
		wait for 40 ns;
		--incRes <= '1';
		wait for 10ns;
		--incRes <= '0';
		wait for 40 ns;
		--odd <= '1';
		--even_odd_s <= '1';
		wait for 40 ns;
		--reset_sav_s <= '1';
		wait for 40 ns; 
		--reset_sav_s <= '0';
		wait;
   end process;
  END;
