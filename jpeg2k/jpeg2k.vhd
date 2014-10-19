----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date:    14:20:36 10/06/2014 
-- Design Name: 
-- Module Name:    jpeg2k - Behavioral 
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
library IEEE,XESS;
use IEEE.STD_LOGIC_1164.ALL;

use IEEE.numeric_std.all;
use std.textio.all;
use XESS.ClkgenPckg.all;     -- For the clock generator module.
use XESS.SdramCntlPckg.all;  -- For the SDRAM controller module.
use XESS.HostIoPckg.all;     -- For the FPGA<=>PC transfer link module.
use XESS.DelayPckg.all;
use work.pck_myhdl_09.all;
-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx primitives in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity jpeg2k is
    Port ( fpgaClk_i : in    std_logic;  -- 12 MHz clock input from external clock source.
          sdClk_o   : out   std_logic;  -- 100 MHz clock to SDRAM.
			 sdClkFb_i : in    std_logic;  -- 100 MHz clock fed back into FPGA.
 
          --blinker_o : out  STD_LOGIC;
			 sdCke_o   : out   std_logic;  -- SDRAM clock enable.
          sdCe_bo   : out   std_logic;  -- SDRAM chip-enable.
          sdRas_bo  : out   std_logic;  -- SDRAM row address strobe.
          sdCas_bo  : out   std_logic;  -- SDRAM column address strobe.
          sdWe_bo   : out   std_logic;  -- SDRAM write-enable.
          sdBs_o    : out   std_logic_vector(1 downto 0);  -- SDRAM bank-address.
          sdAddr_o  : out   std_logic_vector(12 downto 0);  -- SDRAM address bus.
          sdData_io : inout std_logic_vector(15 downto 0);    -- SDRAM data bus.
          sdDqmh_o  : out   std_logic;  -- SDRAM high-byte databus qualifier.
          sdDqml_o  : out   std_logic;  -- SDRAM low-byte databus qualifier.
	 clk_i : in  STD_LOGIC
	 
	
	 );
end jpeg2k;

architecture Behavioral of jpeg2k is
signal fromjpeg_s : std_logic_vector(80 downto 0); -- From jpeg to PC.
alias fromsum_s is fromjpeg_s(15 downto 0); -- sum_r.
alias fromleftDut_s is fromjpeg_s(31 downto 16); -- left
alias fromsamDut_s is fromjpeg_s(47 downto 32); -- sam 
alias fromrightDut_s is fromjpeg_s(63 downto 48); -- right
--alias fromleftDelDut_s is fromjpeg_s(95 downto 80); -- delayed
alias fromresDut_s is fromjpeg_s(79 downto 64); -- res_s
alias fromsel_s is fromjpeg_s(80); --sel back to PC
signal sumDut_s                 : std_logic_vector(15 downto 0);  -- Send sum back to PC.
signal tojpeg_s : std_logic_vector(1 downto 0); -- From PC to jpeg.
alias even_odd_tmp_s is  tojpeg_s(0);
alias fwd_inv_tmp_s is tojpeg_s(1);  
-------------------------------------------------------------------------
-- JTAG
------------------------------------------------------------------------- 
 -- Main entry point for the JTAG signals between the PC and the FPGA.
 --Signals constants needed by JTAG--------------------------------------- 
  signal inShiftDr_s : std_logic; -- True when bits shift btwn PC & FPGA.
  --signal clk_fast : std_logic;
  signal clk_s                    : std_logic;  -- Internal 
  signal drck_s : std_logic; -- Bit shift clock.
  signal tdi_s : std_logic; -- Bits from host PC to the blinker.
  signal tdo_s : std_logic; -- Bits from blinker to the host PC.
  --signal tojpeg_s : std_logic_vector(15 downto 0); -- From PC to jpeg.
  --signal fromjpeg_s : std_logic_vector(145 downto 0); -- From jpeg to PC.
--Signals constants needed by JTAG---------------------------------------
signal dout_lf : unsigned(15 downto 0);
signal din_lf : unsigned(15 downto 0);    
signal addr_lf : unsigned(8 downto 0);
signal we_lf : std_logic;

signal dout_sam : unsigned(15 downto 0);
signal din_sam : unsigned(15 downto 0);    
signal addr_sam : unsigned(8 downto 0);
signal we_sam : std_logic;

signal dout_rht : unsigned(15 downto 0);
signal din_rht : unsigned(15 downto 0);    
signal addr_rht : unsigned(8 downto 0);
signal we_rht : std_logic;

signal dout_res : unsigned(15 downto 0);
signal din_res : unsigned(15 downto 0);    
signal addr_res : unsigned(8 downto 0);
signal we_res : std_logic;

signal reset_sav_s, reset_sav_x, reset_sav_r  : std_logic := '0' ;
signal incRes_s, incRes_x, incRes_r : std_logic := '0' ;

signal left_s, sam_s, right_s, res_s :  signed(15 downto 0);
signal  even_odd_s, even_odd_x, even_odd_r, fwd_inv_s, clk_fast : std_logic;
signal updated_s, noupdate_s : std_logic; 
signal reset_jpeg, odd : std_logic;
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
constant RIGHT_USE_C         : natural   := 3;  -- Enable right to jpeg ...
constant MAX_ADDR_C             : natural   := 8191;  -- ... to this address.
constant MIN_ADDRJPEG_C             : natural   := 8192;  -- Process RAM from this address ...
constant MAX_ADDRJPEG_C             : natural   := 16384;  -- ... to this address.
subtype RamWord_t is unsigned(RAM_WIDTH_C-1 downto 0);  -- RAM word type.
signal wr_s                     : std_logic;  -- Write-enable control.
signal rd_s                     : std_logic;  -- Read-enable control.
signal done_s                   : std_logic;  -- SDRAM R/W operation done signal.component jpeg is
signal addrSdram_s              : std_logic_vector(23 downto 0);  -- Address.
signal dataToSdram_s            : std_logic_vector(sdData_io'range);  -- Data.
signal dataFromSdram_s          : std_logic_vector(sdData_io'range);  --
signal dataToRam_r, dataToRam_x : RamWord_t;  -- Data to write to RAM.
signal dataFromRam_s            : RamWord_t;  -- Data read from RAM.
--Signals constants needed by FsmUpdate_p---------------------------------------	
 
signal addr_r, addr_x           : natural range 0 to RAM_SIZE_C-1;  -- RAM address.
 
signal sam_addr_r, sam_addr_x :  natural range 0 to RAM_SIZE_C-1; 
signal updated_r, updated_x : std_logic := '0';
 
--Signals constants needed by FsmUpdate_p---------------------------------------
--Signals constants needed by Sdram---------------------------------------
signal left_r, sam_r, right_r, left_x, sam_x, right_x    : RamWord_t;
type state_t is (INIT, ODD_SAMPLES, EVEN_SAMPLES, WRITE_DATA, DONE);  -- FSM states.
signal state_r, state_x         : state_t   := INIT;  -- FSM starts off in init state
signal sum_r, sum_x             : natural range 0 to RAM_SIZE_C * (2**RAM_WIDTH_C) - 1;
signal dataToRam_res_r, dataToRam_res_x : RamWord_t;  -- Data to write to RAM.


--signal sigdel_s : std_logic;
--signal sigDelayed_s : std_logic;
signal left_sv, left_sv_r, left_sv_x :   std_logic_vector(15 downto 0) ;
signal leftDelDut_s :   std_logic_vector(15 downto 0);
 

signal leftDut_s                 : std_logic_vector(15 downto 0);  -- Send left back to PC.
signal samDut_s                 : std_logic_vector(15 downto 0);  -- Send left back to PC.
signal rightDut_s                 : std_logic_vector(15 downto 0);  -- Send left back to PC.
signal resDut_s                 : std_logic_vector(15 downto 0);  -- Send left back to PC.

signal z_o : std_logic_vector(15 downto 0);
signal sel, sel_r, sel_x : STD_LOGIC;
signal latch_ctrl, latch_ctrl_r, latch_ctrl_x : STD_LOGIC;
	 COMPONENT latch 
	    port (
        q_o : out std_logic_vector(15 downto 0);
        d_i : in std_logic_vector(15 downto 0);
        g: in std_logic
     );
	  END COMPONENT; 
    COMPONENT mux
    PORT(      
	     z_o: out std_logic_vector(15 downto 0);
        left_i: in std_logic_vector(15 downto 0);
        right_i: in std_logic_vector(15 downto 0);
        sel : IN  std_logic
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

 
begin
ulatch : latch
	port map (
	q_o => leftDelDut_s,
	d_i => left_sv_r,
	g => latch_ctrl_r
	);
umux : mux
	port map (
		  z_o => z_o,
	     left_i => leftDut_s,
		  --right_i => std_logic_vector(right_i),
		  right_i =>  leftDelDut_s,
		  --right_i => rightDut_s,
		  sel => sel);
	
--DelayBus_u0 : DelayBus
--	generic map (NUM_DELAY_CYCLES_G => 7)
--		port map (
--		      --clk_i => clk_s,
--			   --This clk used during simulation  
--				clk_i => clk_fast,
--				bus_i => left_sv,
--				busDelayed_o => leftDelDut_s
--				);
-------------------------------------------------------------------------
-- JTAG entry point.
-------------------------------------------------------------------------
-- Main entry point for the JTAG signals between the PC and the FPGA.
UBscanToHostIo : BscanToHostIo
  port map (
    inShiftDr_o => inShiftDr_s,
    drck_o => drck_s,
    tdi_o => tdi_s,
    tdo_i => tdo_s
    );
-------------------------------------------------------------------------
-- Shift-register.
-------------------------------------------------------------------------
-- This is the shift-register module between jpeg and JTAG entry point.
UHostIoToJpeg : HostIoToDut
  generic map (ID_G => "00000100") -- The identifier used by the PC.
    port map (
    -- Connections to the BscanToHostIo JTAG entry-point module.
    inShiftDr_i => inShiftDr_s,
    drck_i => drck_s,
    tdi_i => tdi_s,
    tdo_o => tdo_s,
    -- Connections to jpeg
    vectorToDut_o => tojpeg_s, -- From PC to jpeg sam left right.
    vectorFromDut_i => fromjpeg_s -- From jpeg to PC.
    );
 lfram : ram
  port map(
     dout => dout_lf,
	  din => din_lf,
	  addr => addr_lf,
	  we => we_lf,
	  --clk_fast => clk_i
	  clk_fast => clk_fast
	  );
	  
samram : ram
  port map(
     dout => dout_sam,
	  din => din_sam,
	  addr => addr_sam,
	  we => we_sam,
	  --clk_fast => clk_i
	  clk_fast => clk_fast
	  );
	  
rhtram : ram
  port map(
     dout => dout_rht,
	  din => din_rht,
	  addr => addr_rht,
	  we => we_rht,
	  --clk_fast => clk_i
	  clk_fast => clk_fast
	  );

resram : ram
  port map(
     dout => dout_res,
	  din => din_res,
	  addr => addr_res,
	  we => we_res,
	  --clk_fast => clk_i
	  clk_fast => clk_fast
	  );
		  
ujpeg: jpeg 
	port map( 
		  clk_fast => clk_fast,	
        --clk_fast => clk_i,
        left_s => left_s,
        right_s => right_s,
        sam_s => sam_s,
        res_s => res_s,
        even_odd_s => even_odd_r,
		  fwd_inv_s => fwd_inv_s,
        updated_s => updated_r,
        noupdate_s => noupdate_s
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

--*********************************************************************
  -- Generate a 100 MHz clock from the 12 MHz input clock and send it out
  -- to the SDRAM. Then feed it back in to clock the internal logic.
  -- (The Spartan-6 FPGAs are a bit picky about what their DCM outputs
  -- are allowed to drive, so I have to use the clkToLogic_o output to
  -- send the clock signal to the output pin of the FPGA and on to the
  -- SDRAM chip.)
  --*********************************************************************
  Clkgen_u1 : Clkgen
    generic map (BASE_FREQ_G => 12.0, CLK_MUL_G => 25, CLK_DIV_G => 3)
    port map(I               => fpgaClk_i, clkToLogic_o => sdClk_o);
	  
  clk_fast <= sdClkFb_i;    -- SDRAM clock feeds back into FPGA.
  clk_s <= sdClkFb_i;
  --*********************************************************************
  -- Instantiate the SDRAM controller that connects to the FSM
  -- and interfaces to the external SDRAM chip.
  --*********************************************************************
  SdramCntl_u0 : SdramCntl
    generic map(
      FREQ_G       => 100.0,  -- Use clock freq. to compute timing parameters.
      DATA_WIDTH_G => RAM_WIDTH_C       -- Width of data words.
      )
    port map(
      clk_i     => clk_s,
      -- FSM side.
      rd_i      => rd_s,
      wr_i      => wr_s,
      done_o    => done_s,
      addr_i    => addrSdram_s,
      data_i    => dataToSdram_s,
      data_o    => dataFromSdram_s,
      -- SDRAM side.
      sdCke_o   => sdCke_o, -- SDRAM clock-enable pin is connected on the XuLA2.
      sdCe_bo   => sdCe_bo, -- SDRAM chip-enable is connected on the XuLA2.
      sdRas_bo  => sdRas_bo,
      sdCas_bo  => sdCas_bo,
      sdWe_bo   => sdWe_bo,
      sdBs_o    => sdBs_o, -- Both SDRAM bank selects are connected on the XuLA2.
      sdAddr_o  => sdAddr_o,
      sdData_io => sdData_io,
      sdDqmh_o  => sdDqmh_o, -- SDRAM high-byte databus qualifier is connected on the XuLA2.
      sdDqml_o  => sdDqml_o  -- SDRAM low-byte databus qualifier is connected on the XuLA2.
      );
 
--DelayLine_u1 : DelayLine
--	generic map (NUM_DELAY_CYCLES_G => 2)
--		port map (
--		      --clk_s => clk_s,
--			   --This clk used during simulation  
--				clk_i => clk_i,
--				a_i => sigDel_s,
--				aDelayed_o => sigDelayed_s
--				);
  -- Connect the SDRAM controller signals to the FSM signals.
  dataToSdram_s <= std_logic_vector(dataToRam_r);
  dataFromRam_s <= RamWord_t(dataFromSdram_s);
  addrSdram_s   <= std_logic_vector(TO_UNSIGNED(addr_r, addrSdram_s'length));
--*********************************************************************
  -- State machine that initializes RAM and then reads RAM to compute
  -- the sum of products of the RAM address and data. This section
  -- is combinatorial logic that sets the control bits for each state
  -- and determines the next state.
  --*********************************************************************
  FsmComb_p : process(state_r, addr_r, dataToRam_r,
                      sum_r, dataFromRam_s, done_s, even_odd_r, reset_sav_r, incRes_r, left_r, sam_r, right_r, sam_addr_r,
							 dataToRam_res_r, updated_r, sel_r, left_sv_r, latch_ctrl_r) 
--							 addrjpeg_r, leftDel_r, sigDelayed_r) 
  begin
    -- Disable RAM reads and writes by default.
    rd_s        <= NO;                  -- Don't write to RAM.
    wr_s        <= NO;                  -- Don't read from RAM.
	 sel_x <= YES; --using left as input to jpeg 
	 latch_ctrl_x <= NO;
	 even_odd_x  <= NO; --wkg on odd samples
	 reset_sav_x <= YES; --ram addr 1 set to odd
    -- Load the registers with their current values by default.
    addr_x      <= addr_r;
    sum_x       <= sum_r;
    dataToRam_x <= dataToRam_r;
    state_x     <= state_r;
    left_x       <= left_r;
	 sam_x       <= sam_r;
	 right_x       <= right_r;
	 sam_addr_x    <= sam_addr_r;
    
    dataToRam_res_x 	  <=  dataToRam_res_r;
--	 addrjpeg_x      <= addrjpeg_r;
	 updated_x  <= updated_r;
--	 leftDel_x <= leftDel_r;
--	 sigDelayed_x <= sigDelayed_r;
    case state_r is

      when INIT =>                      -- Initialize the FSM.
       
        
		  --dataToRam_res_x <= TO_UNSIGNED(1, RAM_WIDTH_C);
		  if even_odd_r =  YES then
			    sam_addr_x <= 2;
		  else		 
			    sam_addr_x  <=   1;
        end if;
		  addr_x  <=   0;
		  --addrjpeg_x  <=   MIN_ADDRJPEG_C + 1;
        --state_x     <= WRITE_DATA;      -- Go to next state.
		  updated_x <= NO;
--        sigDelayed_x <= NO;
		  sel_x <= YES;
        state_x <= ODD_SAMPLES;    -- and go to next state.

		  
      when ODD_SAMPLES =>  -- Read RAM and sum address*data products
		  reset_sav_x <= NO;
		  even_odd_x <= NO;
        if done_s = NO then      -- While current RAM read is not complete ...
          rd_s <= YES;                  -- keep read-enable active.
		  --this code needs to go thru 1 more than the desire values sam_addr
		  --0 1 2 3 left_r sam_r right_r
		  -- if 2 the test is 3 & 4
		  -- if 1 the test is 2 & 3

        elsif addr_r <= (MIN_ADDR_C + 4) then  -- If not the end of row ...
          -- add product of previous RAM address and data read
          -- from that address to the summation ...
			 if sum_r < 1128 then
              sum_x  <= sum_r + TO_INTEGER(dataFromRam_s );
			 end if;	  
			 if addr_r = (LEFT_ADDR_C + sam_addr_r - 1) then
			      left_x <= dataFromRam_s;
					latch_ctrl_x <= YES;
							
			 elsif addr_r = (SAM_ADDR_C + sam_addr_r - 1 ) then	
                sam_x <= dataFromRam_s;
					 latch_ctrl_x <= YES; 
          elsif addr_r = (RIGHT_ADDR_C + sam_addr_r - 1) then	
                right_x <= dataFromRam_s;
					 left_sv_x <= std_logic_vector(dataFromRam_s);
					 latch_ctrl_x <= NO;
					 updated_x <= YES;
					 sam_addr_x <= sam_addr_r + 2;
          elsif addr_r = (RIGHT_USE_C + sam_addr_r) then
					sel_x <= NO; --using right as input to jpeg

					
			   
			 end if;							
          addr_x <= addr_r + 1;         -- and go to next address.
          if updated_r =  YES then
			       updated_x <= NO;
					 latch_ctrl_x <= NO;
          end if;
			 if incRes_r =  YES then
			       incRes_x <= NO;
		   
          end if;
       --elsif addr_r = MAX_ADDR_C then  -- Else, the final address has been read ...			 
		 elsif addr_r = (MIN_ADDR_C + 5) then  -- Else, the final address has been read ...
		         addr_x <= 0;
		         sam_addr_x <= 2;
               even_odd_x <= YES;
				   reset_sav_x <= YES;
               addr_x <= 0;
					
					state_x     <= DONE;
               --state_x     <= EVEN_SAMPLES;      -- Go to next state.
		 else 	
					state_x     <= DONE;      -- Go to next state.
       end if;
		when EVEN_SAMPLES =>  -- Read RAM and sum address*data products
--		   reset_sav_x <= NO;
--			even_odd_x <= YES;
--        if done_s = NO then      -- While current RAM read is not complete ...
--          rd_s <= YES;                  -- keep read-enable active.
--		  --this code needs to go thru 1 more than the desire values sam_addr
--		  --0 1 2 3 left_r sam_r right_r
--		  -- if 2 the test is 3 & 4
--		  -- if 1 the test is 2 & 3
--        elsif addr_r <= (MIN_ADDR_C + 5) then  -- If not the end of row ...
--          -- add product of previous RAM address and data read
--          -- from that address to the summation ...
--			 if sum_r < 1128 then
--              sum_x  <= sum_r + TO_INTEGER(dataFromRam_s );
--			 end if;	  
--			 if addr_r = (LEFT_ADDR_C + sam_addr_r - 1) then
--			      left_x <= dataFromRam_s;
--					
--			 elsif addr_r = (SAM_ADDR_C + sam_addr_r - 1) then	
--                sam_x <= dataFromRam_s;	
--          elsif addr_r = (RIGHT_ADDR_C + sam_addr_r - 1) then	
--                right_x <= dataFromRam_s;
--					 leftDel_x <= dataFromRam_s; --saving the right to leftDel_x
--					 sigDelayed_x <= YES;
--					 updated_x <= YES;
--					 sam_addr_x <= sam_addr_r + 2;
--					 --addrjpeg_x <= addrjpeg_r + 2;
--			 end if;							
--          addr_x <= addr_r + 1;         -- and go to next address.
--          if updated_r =  YES then
--			       updated_x <= NO;
--		   
--          end if;
--			 if incRes_r =  YES then
--			       incRes_x <= NO;
--		   
--          end if;          
--       --elsif addr_r = MAX_ADDR_C then  -- Else, the final address has been read ...			 
--		 elsif addr_r = (MIN_ADDR_C + 4) then  -- Else, the final address has been read ...
--		         addr_x <= MIN_ADDRJPEG_C;
--               state_x     <= WRITE_DATA;      -- Go to next state.
--		 else 	
--					state_x     <= DONE;      -- Go to next state.
--       end if;
				 
      when WRITE_DATA =>                -- Load RAM with values.
--        if done_s = NO then  -- While current RAM write is not complete ...
--		   
--          wr_s <= YES;                  -- keep write-enable active.
--        elsif addr_r <=  (MIN_ADDRJPEG_C + 2) then  -- If haven't reach final address ...
--          if addr_r = (addrjpeg_r) then
--		          --dataToRam_x <= dataToRam_res_r;
--              addrjpeg_x <= addrjpeg_r + 2;
--          end if;
--		        addr_x <= addr_r + 1;         -- and go to next address.		
--		 	 elsif addr_r <= (MIN_ADDRJPEG_C + 2) then
--          state_x <= DONE;
--        end if;   
-- 
      when DONE =>                      -- Summation complete ...
        null;                           -- so wait here and do nothing.
      when others =>                    -- Erroneous state ...
        state_x <= INIT;                -- so re-run the entire process.

    end case;

  end process;


--*********************************************************************
  -- Update the FSM's registers with their next values as computed by
  -- the FSM's combinatorial section.
  --*********************************************************************
  FsmUpdate_p : process(clk_s)
  begin
    if rising_edge(clk_s) then
      addr_r      <= addr_x;
      dataToRam_r <= dataToRam_x;
      state_r     <= state_x;
      sum_r       <= sum_x;
		sam_r       <= sam_x;
		
		right_r     <= right_x;
		sam_addr_r  <= sam_addr_x; 
		
		dataToRam_res_r  <= dataToRam_res_x;
 
		updated_r <= updated_x;
		left_sv_r      <= left_sv_x;
		even_odd_r <= even_odd_x;
		reset_sav_r <= reset_sav_x;
		incRes_r    <= incRes_x;
      left_r      <= left_x;
      sel_r 	<= sel_x;		
		latch_ctrl_r <= latch_ctrl_x;
		
    end if;
  end process;
    reset_sav_s <= reset_sav_r;
    --even_odd_s <= even_odd_r;
	 fwd_inv_s <= '1';	
    --sel <= sel_r;	
	 --fromsel_s <= sel_r;
    fromsel_s <= '0';
    sel  <= '0';	 
 
    
    sumDut_s <= std_logic_vector(TO_UNSIGNED(sum_r, 16));
	 fromsum_s <= sumDut_s; --sum_r back to PC
 
	 leftDut_s <=  std_logic_vector((left_r));
	 left_s <= signed(z_o); --to jpeg 
    fromleftDut_s <= z_o; --left signal back to PC
	 
	 samDut_s <=  std_logic_vector((sam_r));
	 sam_s <= signed(samDut_s); --to jpeg  
	 fromsamDut_s <= samDut_s; --sam signal back to PC
	 
--	 left_sv <=  std_logic_vector(right_r);	 
	 rightDut_s <=  std_logic_vector((right_r));
	 right_s <= signed(rightDut_s);  --to jpeg 
	 fromrightDut_s <= rightDut_s; --right signal back to PC
    
	 resDut_s <= std_logic_vector(res_s);
	 fromresDut_s <= resDut_s;  --jpeg res back to PC
	  
	 incRes_s <= incRes_r;
end Behavioral;


