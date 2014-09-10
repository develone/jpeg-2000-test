--*********************************************************************
-- SDRAM, single-port, instantiated.
--*********************************************************************

library IEEE,XESS;
use IEEE.STD_LOGIC_1164.all;
use IEEE.NUMERIC_STD.all;
use XESS.ClkgenPckg.all;     -- For the clock generator module.
use XESS.SdramCntlPckg.all;  -- For the SDRAM controller module.
use XESS.HostIoPckg.all;     -- For the FPGA<=>PC transfer link module.
--use work.pck_myhdl_09.all;
library UNISIM;
use UNISIM.VComponents.all;

entity SdramSPInst is
  port (
    fpgaClk_i : in    std_logic;  -- 12 MHz clock input from external clock source.
    sdClk_o   : out   std_logic;  -- 100 MHz clock to SDRAM.
    sdClkFb_i : in    std_logic;  -- 100 MHz clock fed back into FPGA.
    sdCke_o   : out   std_logic;  -- SDRAM clock enable.
    sdCe_bo   : out   std_logic;  -- SDRAM chip-enable.
    sdRas_bo  : out   std_logic;  -- SDRAM row address strobe.
    sdCas_bo  : out   std_logic;  -- SDRAM column address strobe.
    sdWe_bo   : out   std_logic;  -- SDRAM write-enable.
    sdBs_o    : out   std_logic_vector(1 downto 0);  -- SDRAM bank-address.
    sdAddr_o  : out   std_logic_vector(12 downto 0);  -- SDRAM address bus.
    sdData_io : inout std_logic_vector(15 downto 0);    -- SDRAM data bus.
    sdDqmh_o  : out   std_logic;  -- SDRAM high-byte databus qualifier.
    sdDqml_o  : out   std_logic  -- SDRAM low-byte databus qualifier.
    );
end entity;

architecture Behavioral of SdramSPInst is

  -- Connections between the shift-register module and  jpeg.
  --    80          70         60        50        40          30        20        10         0
  --   1 0 9876543210987654 3210987654321098 7654321098765432 1098765432109876 5432109876543210
  signal fromjpeg_s : std_logic_vector(81 downto 0); -- From jpeg to PC.
  alias fromresult_s is fromjpeg_s(15 downto 0); -- jpeg output.
  alias fromsum_s is fromjpeg_s(31 downto 16); -- sum_r.
  alias fromleft_s is fromjpeg_s(47 downto 32);  -- jpeg's left pixel
  alias fromsam_s is fromjpeg_s(63 downto 48);  -- jpeg's sam pixel
  alias fromright_s is fromjpeg_s(79 downto 64); --jpeg's right right
  alias fromev_o_s is fromjpeg_s(80);
  alias fromfd_iv_s is fromjpeg_s(81);
  
  signal tojpeg_s : std_logic_vector(1 downto 0); -- From PC to jpeg.
  --signal tojpeg_s : std_logic_vector(49 downto 0); -- From PC to jpeg.
  --signal fromsum_s : std_logic_vector(15 downto 0);
  --signal ev_o_tmp_s : std_logic;
  --signal fd_iv_tmp_s : std_logic;
  alias ev_o_s is tojpeg_s(0);
  alias fd_iv_s is tojpeg_s(1);
  
  

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
  signal clk_s                    : std_logic;  -- Internal clock.
  signal wr_s                     : std_logic;  -- Write-enable control.
  signal rd_s                     : std_logic;  -- Read-enable control.
  signal done_s                   : std_logic;  -- SDRAM R/W operation done signal.
  signal addr_r, addr_x           : natural range 0 to RAM_SIZE_C-1;  -- RAM address.
  signal dataToRam_r, dataToRam_x : RamWord_t;  -- Data to write to RAM.
  signal dataFromRam_s            : RamWord_t;  -- Data read from RAM.
  signal ev_o_x, ev_o_r, fd_iv_x, fd_iv_r                  : std_logic;
  signal left_r, right_r, sam_r ,left_x, right_x, sam_x : RamWord_t; 
  --signal result_r, result_x, result_s : std_logic_vector(15 downto 0);
  signal result_r, result_x : integer range -32768 to 32767;
  signal right_s                  : RamWord_t;
  signal left_s                   : RamWord_t;
  signal sam_s                    : RamWord_t;
  -- Convert the busses for connection to the SDRAM controller.
  signal addrSdram_s              : std_logic_vector(23 downto 0);  -- Address.
  signal dataToSdram_s            : std_logic_vector(sdData_io'range);  -- Data.
  signal dataFromSdram_s          : std_logic_vector(sdData_io'range);  -- Data.
  -- FSM state.
  type state_t is (INIT, WRITE_DATA, READ_AND_SUM_DATA, DONE);  -- FSM states.
  signal state_r, state_x         : state_t   := INIT;  -- FSM starts off in init state.
  signal  sum_r, sum_x            : natural range 0 to RAM_SIZE_C * (2**RAM_WIDTH_C) - 1;
    
  signal sumDut_s                 : std_logic_vector(15 downto 0);  -- Send sum back to PC.
  
  signal nullDutOut_s             : std_logic_vector(0 downto 0);  -- Dummy output for HostIo module.
  signal inShiftDr_s : std_logic; -- True when bits shift btwn PC & FPGA.
  signal drck_s : std_logic; -- Bit shift clock.
  signal tdi_s : std_logic; -- Bits from host PC to the blinker.
  signal tdo_s : std_logic; -- Bits from blinker to the host PC.

begin
   
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
  --send back signals	 
  --ev_o_tmp_s <= ev_o_s;
  --ev_o_s <= '1';
  --fd_iv_tmp_s <= fd_iv_s;
  --fd_iv_s <= '1';

   

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
  clk_s <= sdClkFb_i;                   -- SDRAM clock feeds back into FPGA.

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

  --*********************************************************************
  -- State machine that initializes RAM and then reads RAM to compute
  -- the sum of products of the RAM address and data. This section
  -- is combinatorial logic that sets the control bits for each state
  -- and determines the next state.
  --*********************************************************************
  FsmComb_p : process(state_r, addr_r, dataToRam_r,
                      sum_r, dataFromRam_s, done_s,left_r,sam_r,right_r, result_r, ev_o_r, fd_iv_r)
  begin
    -- Disable RAM reads and writes by default.
    rd_s        <= NO;                  -- Don't write to RAM.
    wr_s        <= NO;                  -- Don't read from RAM.
    -- Load the registers with their current values by default.
    addr_x      <= addr_r;
    sum_x       <= sum_r;
    dataToRam_x <= dataToRam_r;
    state_x     <= state_r;
	 result_x <= result_r;
    left_x <= left_r;
	 right_x <= right_r;
	 sam_x <= sam_r;
	 ev_o_x <= ev_o_r;
	 fd_iv_x <= fd_iv_r;
    case state_r is

      when INIT =>                      -- Initialize the FSM.
        addr_x      <= MIN_ADDR_C;      -- Start writing data at this address.
        dataToRam_x <= TO_UNSIGNED(161, RAM_WIDTH_C);  -- Initial value to write.
		   
        state_x     <= WRITE_DATA;      -- Go to next state.

      when WRITE_DATA =>                -- Load RAM with values.
        if done_s = NO then  -- While current RAM write is not complete ...

          wr_s <= YES;                  -- keep write-enable active.
        elsif addr_r < MAX_ADDR_C + 1 then  -- If haven't reach final address ...
          addr_x      <= addr_r + 1;    -- go to next address ...
          dataToRam_x <= dataToRam_r + 3 ;  -- and write this value.
        else                 -- Else, the final address has been written ...
          addr_x  <= MIN_ADDR_C;        -- go back to the start, ...
          sum_x   <= 0;                 -- clear the sum-of-products, ...
			 result_x   <= 0;                 -- clear the sum-of-products, ...
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
			    sam_x <= dataFromRam_s ;
			 elsif addr_r = RIGHT_ADDR_C then	 
			    right_x <= dataFromRam_s;
				 --sum_x <= TO_INTEGER(dataFromRam_s);
				 --sum_x <= TO_INTEGER(shift_right(((left_r + right_r) + 2), 2));
				 --sum_x <= TO_INTEGER((left_r + right_r) + 2);
				 if  (ev_o_x) = YES then
					if  (fd_iv_x) = YES then	
						result_x <= TO_INTEGER(sam_r - (shift_right(left_r, 1) + shift_right(right_r, 1)));
					else
						result_x <= TO_INTEGER(sam_r + (shift_right(left_r, 1) + shift_right(right_r, 1)));
					end if;
				else
					if  (fd_iv_x) = YES then
						result_x <= TO_INTEGER(sam_r + shift_right(((left_r + right_r) + 2), 2));
					else
						result_x <= TO_INTEGER(sam_r - shift_right(((left_r + right_r) + 2), 2));
					end if;	 
				end if;
				  
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
		left_r      <= left_x;
		right_r      <= right_x;
		sam_r      <= sam_x;
		result_r <= result_x;
		ev_o_r <= ev_o_s;
		--ev_o_r <= '1';
		fd_iv_r <= ev_o_s;
		--fd_iv_r <= '1';
    end if;
  end process;

  --*********************************************************************
  -- Send the summation to the HostIoToDut module and then on to the PC.
  --*********************************************************************
  sumDut_s <= std_logic_vector(TO_UNSIGNED(sum_r, 16));
  --sumDut_s <= std_logic_vector(sam_r);
  fromresult_s <= std_logic_vector(TO_SIGNED(result_r,16));
 
fromleft_s <= std_logic_vector(left_r);
fromsam_s <= std_logic_vector(sam_r);
fromright_s <= std_logic_vector(right_r);
 
fromsum_s <= sumDut_s;
 

fromev_o_s <= ev_o_r;
fromfd_iv_s <= fd_iv_r;

end architecture;
