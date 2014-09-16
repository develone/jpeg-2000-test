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
  signal fromjpeg_s : std_logic_vector(31 downto 0); -- From jpeg to PC.
  signal fromram_s : std_logic_vector(15 downto 0); -- From ram to PC.
  alias fromsum_s is fromjpeg_s(31 downto 16); -- sum_r.
  alias fromresult_s is fromjpeg_s(15 downto 0); -- jpeg output.
  --                                     9 8 7654321098765432 1098765432109876 5432109876543210
  signal tojpeg_s : std_logic_vector(49 downto 0); -- From PC to jpeg.
  signal toram_s : std_logic_vector(15 downto 0); -- From PC to jpeg.
  alias toeven_odd_s is tojpeg_s(48);
  alias tofwd_inv_s is tojpeg_s(49);

  signal clk_fast : std_logic;
  signal clk_s                    : std_logic;  -- Internal 
  
  signal inShiftDr_s : std_logic; -- True when bits shift btwn PC & FPGA.
  signal drck_s : std_logic; -- Bit shift clock.
  signal tdi_s : std_logic; -- Bits from host PC to the blinker.
  signal tdo_s : std_logic; -- Bits from blinker to the host PC.
  signal  even_odd_s : std_logic;
  signal  fwd_inv_s : std_logic;
  alias even_odd_tmp_s is  tojpeg_s(48);
  alias fwd_inv_tmp_s is tojpeg_s(49);
  alias right_s is tojpeg_s(15 downto 0); -- jpeg's 1st operand.
  alias left_s is tojpeg_s(31 downto 16); -- jpeg's 2nd operand.
  alias sam_s is tojpeg_s(47 downto 32); 
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
		  fwd_inv_s : in std_logic
    );
end component;
signal cnt_r : std_logic_vector(22 downto 0) := (others => '0');
--Signals constants needed by Sdram---------------------------------------  
constant NO                     : std_logic := '0';
constant YES                    : std_logic := '1';
constant RAM_SIZE_C             : natural   := 8192;  -- Number of words in RAM.
constant RAM_WIDTH_C            : natural   := 16;  -- Width of RAM words.
constant MIN_ADDR_C             : natural   := 0;  -- Process RAM from this address ...
constant LEFT_ADDR_C             : natural   := 2;
constant SAM_ADDR_C             : natural   := 3;
constant RIGHT_ADDR_C             : natural   := 4;
constant MAX_ADDR_C             : natural   := 5;  -- ... to this address.
subtype RamWord_t is unsigned(RAM_WIDTH_C-1 downto 0);  -- RAM word type.

signal addrSdram_s              : std_logic_vector(23 downto 0);  -- Address.
signal dataToSdram_s            : std_logic_vector(sdData_io'range);  -- Data.
signal dataFromSdram_s          : std_logic_vector(sdData_io'range);  -- 
signal dataToRam_r, dataToRam_x : RamWord_t;  -- Data to write to RAM.
signal dataFromRam_s            : RamWord_t;  -- Data read from RAM.
signal left_r, sam_r, right_r, left_x, sam_x, right_x    : RamWord_t;  
-- Data read from RAM for left, sam, and right.
--signal addr needed for HostIoToRam not for HostIoToDut
signal addr_s                   : std_logic_vector(22 downto 0); 

signal addr_r, addr_x           : natural range 0 to RAM_SIZE_C-1;  -- RAM address.

signal wr_s                     : std_logic;  -- Write-enable control.
signal rd_s                     : std_logic;  -- Read-enable control.
signal done_s                   : std_logic;  -- SDRAM R/W operation done signal.
--Signals constants needed by Sdram---------------------------------------
-- FSM state.
type state_t is (INIT, WRITE_DATA, READ_AND_SUM_DATA, DONE);  -- FSM states.
signal state_r, state_x         : state_t   := INIT;  -- FSM starts off in init state.
signal sum_r, sum_x             : natural range 0 to RAM_SIZE_C * (2**RAM_WIDTH_C) - 1;
signal sumDut_s                 : std_logic_vector(15 downto 0);  -- Send sum back to PC.
signal nullDutOut_s             : std_logic_vector(0 downto 0);  -- Dummy output for HostIo module.

begin
  even_odd_s <= even_odd_tmp_s;
  fwd_inv_s <= fwd_inv_tmp_s;

ujpeg: jpeg 
	port map(
        clk_fast => clk_fast,
        left_s => signed(left_s),
        right_s => signed(right_s),
        sam_s => signed(sam_s),
        res_s => signed_res_s,
        even_odd_s => even_odd_s,
		  fwd_inv_s => fwd_inv_s  
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
                      sum_r, dataFromRam_s, done_s, left_r, sam_r, right_r)
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
	 
    case state_r is

      when INIT =>                      -- Initialize the FSM.
        addr_x      <= MIN_ADDR_C;      -- Start writing data at this address.
        dataToRam_x <= TO_UNSIGNED(161, RAM_WIDTH_C);  -- Initial value to write.
        state_x     <= WRITE_DATA;      -- Go to next state.

      when WRITE_DATA =>                -- Load RAM with values.
        if done_s = NO then  -- While current RAM write is not complete ...
		   
          wr_s <= YES;                  -- keep write-enable active.
        elsif addr_r < MAX_ADDR_C then  -- If haven't reach final address ...
          addr_x      <= addr_r + 1;    -- go to next address ...
          dataToRam_x <= dataToRam_r + 3 ;  -- and write this value.
        else                 -- Else, the final address has been written ...
          addr_x  <= MIN_ADDR_C;        -- go back to the start, ...
          sum_x   <= 0;                 -- clear the sum-of-products, ...
          state_x <= READ_AND_SUM_DATA;    -- and go to next state.
        end if;

      when READ_AND_SUM_DATA =>  -- Read RAM and sum address*data products
        if done_s = NO then      -- While current RAM read is not complete ...
          rd_s <= YES;                  -- keep read-enable active.
        elsif addr_r <= MAX_ADDR_C then  -- If not the final address ...
          -- add product of previous RAM address and data read
          -- from that address to the summation ...
          sum_x  <= sum_r + TO_INTEGER(dataFromRam_s );
			        if addr_r = LEFT_ADDR_C then
					      left_x <= dataFromRam_s;
					  elsif addr_r = SAM_ADDR_C then	
                     sam_x <= dataFromRam_s;	
                 elsif addr_r = RIGHT_ADDR_C then	
                     right_x <= dataFromRam_s;
                 end if;							
          addr_x <= addr_r + 1;         -- and go to next address.
          if addr_r = MAX_ADDR_C then  -- Else, the final address has been read ...
            state_x <= DONE;            -- so go to the next state.
          end if;
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
		right_x     <= right_x;
    end if;
  end process;

  --*********************************************************************
  -- Send the summation to the HostIoToDut module and then on to the PC.
  --*********************************************************************
  --sumDut_s <= std_logic_vector(TO_UNSIGNED(sum_r, 16));
  sumDut_s <= std_logic_vector((sam_r));
fromsum_s <= sumDut_s;

end Behavioral;

