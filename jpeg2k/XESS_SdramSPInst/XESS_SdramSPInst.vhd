--*********************************************************************
-- SDRAM, single-port, instantiated.
--*********************************************************************

library IEEE;
use IEEE.STD_LOGIC_1164.all;
use IEEE.NUMERIC_STD.all;
use work.ClkgenPckg.all;     -- For the clock generator module.
use work.SdramCntlPckg.all;  -- For the SDRAM controller module.
use work.HostIoPckg.HostIoToDut;     -- For the FPGA<=>PC transfer link module.  
use work.pck_myhdl_09.all;
use work.pck_xess_jpeg_top.all;
entity XESS_SdramSPInst is
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
    sdAddr_o  : out   std_logic_vector(11 downto 0);  -- SDRAM address bus.
    sdData_io : inout std_logic_vector(15 downto 0);    -- SDRAM data bus.
    sdDqmh_o  : out   std_logic;  -- SDRAM high-byte databus qualifier.
    sdDqml_o  : out   std_logic  -- SDRAM low-byte databus qualifier.
    );
end entity;

architecture Behavioral of XESS_SdramSPInst is
  constant NO                     : std_logic := '0';
  constant YES                    : std_logic := '1';
  --00_0000 to 03_FFFF is total memory allocated
  --00_0000 to 01_FFFF is where lena256.hex is initially installed
  constant RAM_SIZE_C             : natural   := 262144;  -- Number of words in RAM.
  constant RAM_WIDTH_C            : natural   := 16;  -- Width of RAM words.
  constant MIN_ADDR_C             : natural   := 1;  -- Process RAM from this address ...
  constant MAX_ADDR_C             : natural   := 5;  -- ... to this address.
  subtype RamWord_t is unsigned(RAM_WIDTH_C-1 downto 0);  -- RAM word type.
 

 
--  signal dataFromRam_s            : RamWord_t;  -- Data read from RAM.
  -- Convert the busses for connection to the SDRAM controller.
 

  -- FSM state.
--  type state_t is (INIT, WRITE_DATA, READ_AND_SUM_DATA, DONE);  -- FSM states.
--  signal state_r, state_x         : state_t   := INIT;  -- FSM starts off in init state.

--signal needed by XESS_SdramSPinst.vhd and xess_jpeg_top.vhd*************************** 
  signal clk_s                    : std_logic;  -- Internal clock.
  signal sumDut_s                 : std_logic_vector(54 downto 0);  -- Send sum back to PC.
 
  alias fromfifodataDut_s is sumDut_s(54 downto 39);
  alias fromsdramdataDut_s is sumDut_s(38 downto 23);
  alias fromsdramaddrDut_s is sumDut_s(22 downto 0);
  signal nullDutOut_s             : std_logic_vector(0 downto 0);  -- Dummy output for HostIo module.
  signal dataFromSdram_s          : std_logic_vector(sdData_io'range);  -- Data.
  signal addrSdram_s              : unsigned(22 downto 0);  -- Address.
  signal dataToSdram_s            : unsigned(15 downto 0);  -- Data.
  signal dataFromRam_r, dataFromRam_r1, dataFromRam_r2  : unsigned(15 downto 0); 
  signal sum_r, sum_x             : unsigned( 15 downto 0);
  signal wr_s                     : std_logic;  -- Write-enable control.
  signal rd_s                     : std_logic;  -- Read-enable control.
  signal done_s                   : std_logic;  -- SDRAM R/W operation done signal.
  signal addr_r, addr_x           : unsigned(22 downto 0);  -- RAM address.
  signal addr_r1, addr_r2           : unsigned(22 downto 0);  -- RAM address.
  signal dataToRam_r, dataToRam_x, dataFromRam_s : unsigned(15 downto 0);  -- Data to write to RAM.
--signal needed by XESS_SdramSPinst.vhd and xess_jpeg_top.vhd***************************

--signal needed by xess_jpeg_top.vhd***************************
  signal state_r, state_x         : t_enum_t_State_1   := INIT;  -- FSM starts off in init state.
  signal sig_in : unsigned(51 downto 0) := (others => '0');
  signal noupdate_s : std_logic;
  signal res_s : signed(15 downto 0) := (others => '0');
  signal jp_lf : unsigned(15 downto 0) := (others => '0');
  signal jp_sa: unsigned(15 downto 0) := (others => '0');
  signal jp_rh : unsigned(15 downto 0) := (others => '0');
  signal jp_flgs : unsigned(3 downto 0) := (others => '0');
  signal reset_col : std_logic := '1';
  signal rdy : std_logic := '1';
  signal addr_not_reached : std_logic := '0';
  signal offset           : unsigned(22 downto 0);  -- RAM address.
  signal muxsel_r, muxsel_x  : std_logic :=  '0';
--signal needed by xess_jpeg_top.vhd*************************** 

--signal needed by FIFO*************************** 
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
--signal needed by FIFO*************************** 
 
 
component xess_jpeg_top is
    port (
        clk_fast: in std_logic;
        addr_r: out unsigned(22 downto 0);
        addr_x: inout unsigned(22 downto 0);
        state_r: inout t_enum_t_State_1;
        state_x: inout t_enum_t_State_1;
        addr_r1: inout unsigned(22 downto 0);
        addr_r2: inout unsigned(22 downto 0);
        dataToRam_r: inout unsigned(15 downto 0);
        dataToRam_x: inout unsigned(15 downto 0);
        dataFromRam_r: out unsigned(15 downto 0);
        dataFromRam_r1: inout unsigned(15 downto 0);
        dataFromRam_r2: in unsigned(15 downto 0);
        dataFromRam_x: inout unsigned(15 downto 0);
        sig_in: inout unsigned(51 downto 0);
        noupdate_s: out std_logic;
        res_s: out signed (15 downto 0);
        jp_lf: inout unsigned(15 downto 0);
        jp_sa: inout unsigned(15 downto 0);
        jp_rh: inout unsigned(15 downto 0);
        jp_flgs: in unsigned(3 downto 0);
        reset_col: in std_logic;
        rdy: in std_logic;
        addr_not_reached: inout std_logic;
        offset: in unsigned(22 downto 0);
        dataFromRam_s: in unsigned(15 downto 0);
        done_s: in std_logic;
        wr_s: out std_logic;
        rd_s: out std_logic;
        sum_r: inout unsigned(15 downto 0);
        sum_x: inout unsigned(15 downto 0);
        muxsel_r: inout std_logic;
        muxsel_x: inout std_logic;
        empty_r: out std_logic;
        full_r: out std_logic;
        enr_r: inout std_logic;
        enw_r: inout std_logic;
        dataout_r: inout unsigned(15 downto 0);
        datain_r: inout unsigned(15 downto 0);
        empty_x: inout std_logic;
        full_x: inout std_logic;
        enr_x: inout std_logic;
        enw_x: inout std_logic;
        dataout_x: inout unsigned(15 downto 0);
        datain_x: inout unsigned(15 downto 0)
    );
end component xess_jpeg_top;

begin
--muxsel_x <= '0';
  --*********************************************************************
  -- Instantiate the jpeg_top step1JPEG_TOP_INSTANCE_7_FSMUPDATE
  -- updates signals for the FSM.
  --*********************************************************************
xess_jpeg_top_u0 : xess_jpeg_top
  port map (
     clk_fast => clk_s,
	  addr_r => addr_r,
	  addr_x => addr_x,
	  state_r => state_r,
	  state_x => state_x,
	  addr_r1 => addr_r1,
     addr_r2 => addr_r2,
	  dataToRam_r => dataToRam_r,
	  dataToRam_x => dataToRam_x,
	  dataFromRam_r =>  dataFromRam_r,
	  dataFromRam_r1 =>  dataFromRam_r1,
	  dataFromRam_r2  => dataFromRam_r2,
	  sig_in => sig_in,
	  noupdate_s => noupdate_s,
	  res_s => res_s,
	  jp_lf => jp_lf,
	  jp_sa => jp_sa,
	  jp_rh => jp_rh,
	  jp_flgs => jp_flgs,
	  reset_col => reset_col,
	  rdy => rdy,
	  addr_not_reached => addr_not_reached,
     offset => offset,
     dataFromRam_s => dataFromRam_s,
	  done_s => done_s,
	  wr_s => wr_s,
	  rd_s => rd_s,
	  sum_r => sum_r,
	  sum_x => sum_x,
 
	  muxsel_r => muxsel_r, 
     muxsel_x => muxsel_x,
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
      DATA_WIDTH_G => RAM_WIDTH_C,       -- Width of data words.
		
		NROWS_G       => 4096,  -- Number of rows in SDRAM array.
      NCOLS_G       => 512,  -- Number of columns in SDRAM array.
      HADDR_WIDTH_G => 23,   -- Host-side address width.
      SADDR_WIDTH_G => 12   -- SDRAM-side address width.
      )
    port map(
      clk_i     => clk_s,
      -- FSM side.
      rd_i      => rd_s,
      wr_i      => wr_s,
      done_o    => done_s,
      addr_i    => std_logic_vector(addrSdram_s),
      data_i    => std_logic_vector(dataToSdram_s),
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
  dataToSdram_s <= dataToRam_r;  
--  dataToSdram_s <= std_logic_vector(dataToRam_r);
  dataFromRam_s <= RamWord_t(dataFromSdram_s);
--  addrSdram_s   <= std_logic_vector(TO_UNSIGNED(addr_r, addrSdram_s'length));
  addrSdram_s   <= addr_r;
  --*********************************************************************
  -- State machine that initializes RAM and then reads RAM to compute
  -- the sum of products of the RAM address and data. This section
  -- is combinatorial logic that sets the control bits for each state 
  -- and determines the next state.
  --*********************************************************************
--  FsmComb_p : process(state_r, addr_r, dataToRam_r,
--                      sum_r, dataFromRam_s, done_s)
--  begin
--    -- Disable RAM reads and writes by default.
--    rd_s        <= NO;                  -- Don't write to RAM.
--    wr_s        <= NO;                  -- Don't read from RAM.
--    -- Load the registers with their current values by default.
--    addr_x      <= addr_r;
--    sum_x       <= sum_r;
--    dataToRam_x <= dataToRam_r;
--    state_x     <= state_r;
--
--    case state_r is
--
--      when INIT =>                      -- Initialize the FSM.
--        addr_x      <= X"00_0000";      -- Start writing data at this address.
--        dataToRam_x <= TO_UNSIGNED(1, RAM_WIDTH_C);  -- Initial value to write.
----        state_x     <= WRITE_DATA;      -- Go to next state.
--        state_x     <= READ_AND_SUM_DATA;      -- Go to next state.
--
--      when WRITE_DATA =>                -- Load RAM with values.
--        if done_s = NO then  -- While current RAM write is not complete ...
--          wr_s <= YES;                  -- keep write-enable active.
--        elsif addr_r < MAX_ADDR_C then  -- If haven't reach final address ...
--          addr_x      <= addr_r + 1;    -- go to next address ...
--          dataToRam_x <= dataToRam_r + 3;  -- and write this value.
--        else                 -- Else, the final address has been written ...
--          addr_x  <= X"00_0000";        -- go back to the start, ...
--          sum_x   <= 0;                 -- clear the sum-of-products, ...
--          state_x <= READ_AND_SUM_DATA;    -- and go to next state.
--        end if;
--
--      when READ_AND_SUM_DATA =>  -- Read RAM and sum address*data products
--        if done_s = NO then      -- While current RAM read is not complete ...
--          rd_s <= YES;                  -- keep read-enable active.
--        elsif addr_r <= MAX_ADDR_C then  -- If not the final address ...
--          -- add product of previous RAM address and data read 
--          -- from that address to the summation ...
--          sum_x  <= sum_r + TO_INTEGER(dataFromRam_s * addr_r);
--          addr_x <= addr_r + 1;         -- and go to next address.
--          if addr_r = MAX_ADDR_C then  -- Else, the final address has been read ...
--            state_x <= DONE;            -- so go to the next state.
--          end if;
--        end if;
--
--      when DONE =>                      -- Summation complete ...
--        null;                           -- so wait here and do nothing.
--      when others =>                    -- Erroneous state ...
--        state_x <= INIT;                -- so re-run the entire process.
--        
--    end case;
--
--  end process;

  --*********************************************************************
  -- Update the FSM's registers with their next values as computed by
  -- the FSM's combinatorial section.       
  --*********************************************************************
--  FsmUpdate_p : process(clk_s)
--  begin
--    if rising_edge(clk_s) then
----      addr_r      <= addr_x;
----      dataToRam_r <= dataToRam_x;
--      state_r     <= state_x;
--      sum_r       <= sum_x;
--    end if;
--  end process;

  --*********************************************************************
  -- Send the summation to the HostIoToDut module and then on to the PC.
  --*********************************************************************
  --sumDut_s <= std_logic_vector(TO_UNSIGNED(sum_r, 16));
  --sumDut_s <= std_logic_vector(sum_r);
  fromsdramaddrDut_s <= std_logic_vector(addr_r);
  fromsdramdataDut_s <= std_logic_vector(sum_r);
  --fromfifodataDut_s <= std_logic_vector(instance_14_dout);
--  din <= dataFromRam_s;
  HostIoToDut_u2 : HostIoToDut
    generic map (SIMPLE_G => true)
    port map (
      vectorFromDut_i => sumDut_s,
      vectorToDut_o   => nullDutOut_s
      );

end architecture;
