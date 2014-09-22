----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date:    09:11:52 09/12/2014 
-- Design Name: 
-- Module Name:    top_level_mod - Behavioral 
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

use IEEE.STD_LOGIC_UNSIGNED.ALL;
use IEEE.NUMERIC_STD.ALL;

use XESS.ClkgenPckg.all;     -- For the clock generator module.
use XESS.SdramCntlPckg.all;  -- For the SDRAM controller module.
use XESS.HostIoPckg.all;     -- For the FPGA<=>PC transfer link module.

use work.pck_myhdl_09.all;
library UNISIM;
use UNISIM.VComponents.all;
-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx primitives in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity top_level_mod is
    Port (fpgaClk_i : in    std_logic;  -- 12 MHz clock input from external clock source.
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
          sdDqml_o  : out   std_logic);  -- SDRAM low-byte databus qualifier.
end top_level_mod;

architecture Behavioral of top_level_mod is
-- Connections between the shift-register module and  jpeg.
  --    80          70         60        50        40          30        20        10         0
  --   1 0 9876543210987654 3210987654321098 7654321098765432 1098765432109876 5432109876543210
  --                                                                           5432109876543210
  
  signal x : std_logic_vector(15 downto 0);  
  signal fromjpeg_s : std_logic_vector(113 downto 0); -- From jpeg to PC.
  alias fromresult_s is fromjpeg_s(15 downto 0); -- jpeg output.
  alias fromsum_s is fromjpeg_s(31 downto 16); -- sum_r.
  alias fromleft_s is fromjpeg_s(47 downto 32); -- left_r.
  alias fromsam_s is fromjpeg_s(63 downto 48); -- sam_r.
  alias fromright_s is fromjpeg_s(79 downto 64); -- right_r.
  alias fromaddr_sam_s is fromjpeg_s(95 downto 80); --addr_sam_r 
  alias fromaddrjpeg_s is fromjpeg_s(111 downto 96); --addr_sam_r
 
  alias fromupdated_s is fromjpeg_s(112);
  alias fromnoupdate_s is fromjpeg_s(113);
  --alias fromjpegram_s is fromjpeg_s(128 downto 113); --addr_sam_r
  signal  even_odd_s : std_logic;
  signal  fwd_inv_s : std_logic;
  
  signal tojpeg_s : std_logic_vector(15 downto 0); -- From PC to jpeg.
  alias even_odd_tmp_s is  tojpeg_s(14);
  alias fwd_inv_tmp_s is tojpeg_s(15);  
  
  --signal fromram_s : std_logic_vector(15 downto 0); -- From ram to PC.
  signal toram_s : std_logic_vector(15 downto 0); -- From PC to jpeg.
   
  --alias sam_addr_s is tojpeg_s (13 downto 0);
  signal left_s : std_logic_vector(15 downto 0);
  signal sam_s : std_logic_vector(15 downto 0);
  signal right_s : std_logic_vector(15 downto 0);
  signal clk_fast : std_logic;
  signal clk_s                    : std_logic;  -- Internal 
  
  signal inShiftDr_s : std_logic; -- True when bits shift btwn PC & FPGA.
  signal drck_s : std_logic; -- Bit shift clock.
  signal tdi_s : std_logic; -- Bits from host PC to the blinker.
  signal tdo_s : std_logic; -- Bits from blinker to the host PC.

  
  --alias right_s is tojpeg_s(15 downto 0); -- jpeg's 1st operand.
  --alias left_s is tojpeg_s(31 downto 16); -- jpeg's 2nd operand.
  --alias sam_s is tojpeg_s(47 downto 32); 
  alias signed_res_s is signed(fromresult_s);
  
  --alias fromsum_s is fromjpeg_s(31 downto 16); -- jpeg output.

 
  
  

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
signal cnt_r : std_logic_vector(22 downto 0) := (others => '0');
--Signals constants needed by Sdram---------------------------------------  
constant NO                     : std_logic := '0';
constant YES                    : std_logic := '1';
constant ROW_C             : natural   := 63;  -- Number of words in RAM.
constant RAM_SIZE_C             : natural   := 16384;  -- Number of words in RAM.
constant RAM_WIDTH_C            : natural   := 16;  -- Width of RAM words.
constant MIN_ADDR_C             : natural   := 0;  -- Process RAM from this address ...
constant MAX_ADDR_C             : natural   := 8191;  -- ... to this address.
constant MIN_ADDRJPEG_C             : natural   := 8192;  -- Process RAM from this address ...
constant MAX_ADDRJPEG_C             : natural   := 16384;  -- ... to this address.
subtype RamWord_t is unsigned(RAM_WIDTH_C-1 downto 0);  -- RAM word type.
signal updated_r, updated_x : std_logic;  
signal noupdate_r, noupdate_x : std_logic; 
signal updated_s, noupdate_s : std_logic;  -- jpeg left sam  right are valid
signal addrSdram_s              : std_logic_vector(23 downto 0);  -- Address.
signal dataToSdram_s            : std_logic_vector(sdData_io'range);  -- Data.
signal dataFromSdram_s          : std_logic_vector(sdData_io'range);  -- 
signal dataToRam_r, dataToRam_x : RamWord_t;  -- Data to write to RAM.
signal dataToRam_res_r, dataToRam_res_x : RamWord_t;  -- Data to write to RAM.
signal dataFromRam_s            : RamWord_t;  -- Data read from RAM.
signal left_r, sam_r, right_r, left_x, sam_x, right_x    : RamWord_t;  
-- Data read from RAM for left, sam, and right.
--signal addr needed for HostIoToRam not for HostIoToDut
signal addr_s                   : std_logic_vector(22 downto 0); 
signal addrjpeg_r, addrjpeg_x           : natural range 0 to RAM_SIZE_C-1;  -- RAM address.
signal addr_r, addr_x           : natural range 0 to RAM_SIZE_C-1;  -- RAM address.
signal sam_addr_r, sam_addr_x    :  natural range 0 to RAM_SIZE_C-1; 
signal sam_addr_stor_r, sam_addr_stor_x    :  natural range 0 to RAM_SIZE_C-1; 
signal wr_s                     : std_logic;  -- Write-enable control.
signal rd_s                     : std_logic;  -- Read-enable control.
signal done_s                   : std_logic;  -- SDRAM R/W operation done signal.

--Signals constants needed by Sdram---------------------------------------
-- FSM state.
type state_t is (INIT, READ_AND_SUM_DATA, WRITE_DATA, DONE);  -- FSM states.
signal state_r, state_x         : state_t   := INIT;  -- FSM starts off in init state.
signal sum_r, sum_x             : natural range 0 to RAM_SIZE_C * (2**RAM_WIDTH_C) - 1;
signal sumDut_s                 : std_logic_vector(15 downto 0);  -- Send sum back to PC.
signal leftDut_s                 : std_logic_vector(15 downto 0);  -- Send left back to PC.
signal samDut_s                 : std_logic_vector(15 downto 0);  -- Send sam back to PC.
signal rightDut_s                 : std_logic_vector(15 downto 0);  -- Send right back to PC.
signal sam_addr_rDut_s                 : std_logic_vector(15 downto 0);  -- Send addr_sam_r back to PC.
signal addrjpeg_rDut_s                 : std_logic_vector(15 downto 0);  -- Send addrjpeg_r back to PC.
signal jpegram_rDut_s                 : std_logic_vector(15 downto 0);  -- Send jpegram_r back to PC.

signal nullDutOut_s             : std_logic_vector(0 downto 0);  -- Dummy output for HostIo module.

begin
  

  --updated_r <= '1';
  --updated_s <= updated_r;
  --sam_addr_r <= conv_integer(sam_addr_s);
    
ujpeg: jpeg 
	port map( 
        clk_fast => clk_fast,
        left_s => signed(left_s),
        right_s => signed(right_s),
        sam_s => signed(sam_s),
        res_s => signed_res_s,
        even_odd_s => even_odd_s,
		  fwd_inv_s => fwd_inv_s,
        updated_s => updated_s,
        noupdate_s => noupdate_s		  
		  );

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
  -- This is the shift-register module between Ram and JTAG entry point.
--UHostIoToRam : HostIoToRam
--  generic map (ID_G => "00000100") -- The identifier used by the PC.
--    port map (
--   
--    -- Connections to ram
--	 wr_o => wr_s,
--	 clk_i => clk_fast,
--	 rd_o => rd_s,
--	 addr_o => addr_s,
--    dataFromHost_o => toram_s, -- From PC to jpeg sam left right.
--    dataToHost_i => fromram_s, -- From jpeg to PC.
--	 done_i => done_s -- True when memory read/write operation is done.
--    );  
	 
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

  -- Connect the SDRAM controller signals to the FSM signals.
  dataToSdram_s <= std_logic_vector(dataToRam_r);
  dataFromRam_s <= RamWord_t(dataFromSdram_s);
  addrSdram_s   <= std_logic_vector(TO_UNSIGNED(addr_r, addrSdram_s'length));
 process(clk_fast) is
	begin
	   if rising_edge(clk_fast) then
	 
			cnt_r <= cnt_r + 1;
		end if;
	end process; 
  
--blinker_o <= cnt_r(22);

--*********************************************************************
  -- State machine that initializes RAM and then reads RAM to compute
  -- the sum of products of the RAM address and data. This section
  -- is combinatorial logic that sets the control bits for each state
  -- and determines the next state.
  --*********************************************************************
  FsmComb_p : process(state_r, addr_r, dataToRam_r,
                      sum_r, dataFromRam_s, done_s, left_r, sam_r, right_r, sam_addr_r,
							 dataToRam_res_r, addrjpeg_r, updated_r)
  begin
    -- Disable RAM reads and writes by default.
    rd_s        <= NO;                  -- Don't write to RAM.
    wr_s        <= NO;                  -- Don't read from RAM.
	 
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
	 addrjpeg_x      <= addrjpeg_r;
	 updated_x  <= updated_r;
    case state_r is

      when INIT =>                      -- Initialize the FSM.
       
        
		  --dataToRam_res_x <= TO_UNSIGNED(1, RAM_WIDTH_C);
		  sam_addr_x  <=   7;
		  addr_x  <=   0;
		  addrjpeg_x  <=   MIN_ADDRJPEG_C + 7;
        --state_x     <= WRITE_DATA;      -- Go to next state.
        state_x <= READ_AND_SUM_DATA;    -- and go to next state.
        updated_x <= NO;

      when READ_AND_SUM_DATA =>  -- Read RAM and sum address*data products
        if done_s = NO then      -- While current RAM read is not complete ...
          rd_s <= YES;                  -- keep read-enable active.
        elsif addr_r <= (MIN_ADDR_C + 8) then  -- If not the end of row ...
          -- add product of previous RAM address and data read
          -- from that address to the summation ...
          sum_x  <= sum_r + TO_INTEGER(dataFromRam_s );
			 if addr_r = (sam_addr_r - 1) then
			      left_x <= dataFromRam_s;
					
			 elsif addr_r = (sam_addr_r ) then	
                sam_x <= dataFromRam_s;	
          elsif addr_r = (sam_addr_r + 1) then	
                right_x <= dataFromRam_s;
					 updated_x <= YES;
					 sam_addr_x <= sam_addr_r + 2;
					 --addrjpeg_x <= addrjpeg_r + 2;
			 end if;							
          addr_x <= addr_r + 1;         -- and go to next address.
          
       --elsif addr_r = MAX_ADDR_C then  -- Else, the final address has been read ...			 
		 elsif addr_r <= (MIN_ADDR_C + 8) then  -- Else, the final address has been read ...
		         addr_x <= MIN_ADDRJPEG_C;
               state_x     <= WRITE_DATA;      -- Go to next state.
		 else 	
					state_x     <= DONE;      -- Go to next state.
       end if;
		  
      when WRITE_DATA =>                -- Load RAM with values.
        if done_s = NO then  -- While current RAM write is not complete ...
		   
          wr_s <= YES;                  -- keep write-enable active.
        elsif addr_r <=  (MIN_ADDRJPEG_C + 8) then  -- If haven't reach final address ...
          if addr_r = (addrjpeg_r) then
		          dataToRam_x <= dataToRam_res_r;
              addrjpeg_x <= addrjpeg_r + 2;
          end if; 		  
			 elsif addr_r <= (MIN_ADDRJPEG_C + 8) then
          state_x <= DONE;
        end if;   
 
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
		left_r      <= left_x;
		right_r     <= right_x;
		sam_addr_r  <= sam_addr_x; 
		
		--dataToRam_res_r  <= dataToRam_res_x;
		addrjpeg_r      <= addrjpeg_x;
		updated_r <= updated_x;
    end if;
  end process;

  --*********************************************************************
  -- Send the summation, left, sam, right from ram to the HostIoToDut module and then on to the PC.
  --*********************************************************************
  sumDut_s <= std_logic_vector(TO_UNSIGNED(sum_r, 16));
  leftDut_s <= std_logic_vector((left_r));
  samDut_s <= std_logic_vector((sam_r));
  rightDut_s <= std_logic_vector((right_r));
  fromsum_s <= sumDut_s; --back to PC
  
  --setting jpeg signals
  updated_s <= updated_r; 
  left_s <= leftDut_s; --to jpeg
  sam_s <= samDut_s; --to jpeg
  right_s <= rightDut_s; --to jpeg
  even_odd_s <= even_odd_tmp_s;
  fwd_inv_s <= fwd_inv_tmp_s;
  
  dataToRam_res_r <= RamWord_t(fromresult_s); --jpeg result to sdram
  sam_addr_rDut_s <= std_logic_vector(TO_UNSIGNED(sam_addr_r,16));
  fromaddr_sam_s <= sam_addr_rDut_s;
  addrjpeg_rDut_s <= std_logic_vector(TO_UNSIGNED(addrjpeg_r,16));
  fromaddrjpeg_s <= addrjpeg_rDut_s;
  fromnoupdate_s <= noupdate_s;
  fromupdated_s <= updated_s;
  
  fromleft_s <= leftDut_s; --back to PC
  fromsam_s <= samDut_s; --back to PC 
  fromright_s <= rightDut_s; --back to PC
end Behavioral;

