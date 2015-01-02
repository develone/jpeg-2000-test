-- File: xess_jpeg_top.vhd
-- Generated by MyHDL 0.9dev
-- Date: Fri Jan  2 14:04:11 2015



package pck_xess_jpeg_top is

attribute enum_encoding: string;

    type t_enum_t_State_1 is (
    INIT,
    WRITE,
    READ_AND_SUM_DATA,
    CK_SDRAM_RD,
    CK_SDRAM_WR,
    ODD_SAMPLES,
    EVEN_SAMPLES,
    WR_DATA,
    INTERLACE,
    DONE
);
attribute enum_encoding of t_enum_t_State_1: type is "0000000001 0000000010 0000000100 0000001000 0000010000 0000100000 0001000000 0010000000 0100000000 1000000000";

end package pck_xess_jpeg_top;

library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
use std.textio.all;

use work.pck_myhdl_09.all;

use work.pck_xess_jpeg_top.all;

entity xess_jpeg_top is
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
        res_s: inout signed (15 downto 0);
        res_u: out unsigned(15 downto 0);
        jp_lf: inout unsigned(15 downto 0);
        jp_sa: inout unsigned(15 downto 0);
        jp_rh: inout unsigned(15 downto 0);
        jp_flgs: inout unsigned(3 downto 0);
        reset_col: inout std_logic;
        rdy: in std_logic;
        addr_not_reached: inout std_logic;
        offset_r: inout unsigned(22 downto 0);
        offset_x: inout unsigned(22 downto 0);
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
        datain_x: inout unsigned(15 downto 0);
        col_r: inout unsigned(7 downto 0);
        col_x: inout unsigned(7 downto 0);
        row_r: inout unsigned(7 downto 0);
        row_x: inout unsigned(7 downto 0)
    );
end entity xess_jpeg_top;
-- The following between the single quotes ':= "0000"' needs to added to line below
-- signal instance_1_reset_ctn: unsigned(3 downto 0);
-- before the ';' to be like the following
-- signal instance_1_reset_ctn: unsigned(3 downto 0):= "0000";

architecture MyHDL of xess_jpeg_top is


constant YES: integer := 1;
constant reset_dly_c: integer := 10;
constant NO: integer := 0;



signal instance_1_reset_ctn: unsigned(3 downto 0):= "0000";
signal instance_1_writeptr: unsigned(9 downto 0);
signal instance_1_readptr: unsigned(9 downto 0);
type t_array_instance_1_mem is array(0 to 1024-1) of unsigned(15 downto 0);
signal instance_1_mem: t_array_instance_1_mem;

begin




XESS_JPEG_TOP_INSTANCE_1_RTL: process (clk_fast) is
begin
    if rising_edge(clk_fast) then
        if (instance_1_reset_ctn < reset_dly_c) then
            instance_1_readptr <= to_unsigned(0, 10);
            instance_1_writeptr <= to_unsigned(0, 10);
            instance_1_reset_ctn <= (instance_1_reset_ctn + 1);
        end if;
        if (enr_r = '1') then
            dataout_x <= instance_1_mem(to_integer(instance_1_readptr));
            instance_1_readptr <= (instance_1_readptr + 1);
        end if;
        if (enw_r = '1') then
            instance_1_mem(to_integer(instance_1_writeptr)) <= datain_x;
            instance_1_writeptr <= (instance_1_writeptr + 1);
        end if;
        if (instance_1_readptr = 1023) then
            instance_1_readptr <= to_unsigned(0, 10);
        end if;
        if (instance_1_writeptr = 1023) then
            full_x <= '1';
            instance_1_writeptr <= to_unsigned(0, 10);
        else
            empty_x <= '0';
        end if;
    end if;
end process XESS_JPEG_TOP_INSTANCE_1_RTL;


XESS_JPEG_TOP_INSTANCE_2_MUXLOGIC: process (dataFromRam_r2, dataFromRam_r1, addr_r1, muxsel_r, addr_r2) is
begin
    addr_r <= addr_r1;
    dataFromRam_r <= dataFromRam_r1;
    if (muxsel_r = '1') then
        addr_r <= addr_r2;
        dataFromRam_r <= dataFromRam_r2;
    end if;
end process XESS_JPEG_TOP_INSTANCE_2_MUXLOGIC;


XESS_JPEG_TOP_INSTANCE_3_JPEG: process (clk_fast) is
begin
    if rising_edge(clk_fast) then
        if bool(sig_in(50)) then
            noupdate_s <= '0';
            if bool(sig_in(48)) then
                if bool(sig_in(49)) then
                    res_s <= signed(sig_in(32-1 downto 16) - (shift_right(sig_in(16-1 downto 0), 1) + shift_right(sig_in(48-1 downto 32), 1)));
                else
                    res_s <= signed(sig_in(32-1 downto 16) + (shift_right(sig_in(16-1 downto 0), 1) + shift_right(sig_in(48-1 downto 32), 1)));
                end if;
            else
                if bool(sig_in(49)) then
                    res_s <= signed(sig_in(32-1 downto 16) + shift_right(((sig_in(16-1 downto 0) + sig_in(48-1 downto 32)) + 2), 2));
                else
                    res_s <= signed(sig_in(32-1 downto 16) - shift_right(((sig_in(16-1 downto 0) + sig_in(48-1 downto 32)) + 2), 2));
                end if;
            end if;
            res_u <= unsigned(res_s);
        else
            noupdate_s <= '1';
        end if;
    end if;
end process XESS_JPEG_TOP_INSTANCE_3_JPEG;


XESS_JPEG_TOP_INSTANCE_4_SDRAM_RD: process (clk_fast) is
begin
    if rising_edge(clk_fast) then
        if bool(reset_col) then
            jp_lf <= to_unsigned(0, 16);
            jp_sa <= to_unsigned(0, 16);
            jp_rh <= to_unsigned(0, 16);
            addr_not_reached <= '0';
            if (jp_flgs(0) = '1') then
                addr_r2 <= (1 + offset_x);
            else
                addr_r2 <= (0 + offset_x);
            end if;
        else
            if bool(jp_flgs(0)) then
                if (addr_r2 = (1 + offset_x)) then
                    jp_lf <= dataFromRam_s;
                    addr_r2 <= (addr_r2 + 256);
                else
                    if (addr_r2 = (257 + offset_x)) then
                        jp_sa <= dataFromRam_s;
                        addr_r2 <= (addr_r2 + 256);
                    else
                        if (addr_r2 = (513 + offset_x)) then
                            jp_rh <= dataFromRam_s;
                            addr_not_reached <= '1';
                        end if;
                    end if;
                end if;
            elsif (addr_r2 = (0 + offset_x)) then
                jp_lf <= dataFromRam_s;
                addr_r2 <= (addr_r2 + 256);
            else
                if (addr_r2 = (256 + offset_x)) then
                    jp_sa <= dataFromRam_s;
                    addr_r2 <= (addr_r2 + 256);
                else
                    if (addr_r2 = (512 + offset_x)) then
                        jp_rh <= dataFromRam_s;
                        addr_not_reached <= '1';
                    end if;
                end if;
            end if;
        end if;
    end if;
end process XESS_JPEG_TOP_INSTANCE_4_SDRAM_RD;


XESS_JPEG_TOP_INSTANCE_5_RAM2SIG: process (jp_sa, jp_flgs, jp_rh, rdy, addr_not_reached, jp_lf) is
begin
    if bool(rdy) then
        if bool(addr_not_reached) then
            sig_in <= unsigned'(jp_flgs & jp_rh & jp_sa & jp_lf);
        else
            sig_in <= to_unsigned(0, 52);
        end if;
    else
        sig_in <= to_unsigned(0, 52);
    end if;
end process XESS_JPEG_TOP_INSTANCE_5_RAM2SIG;


XESS_JPEG_TOP_INSTANCE_6_FSM: process (addr_r1, dataFromRam_r1, state_r, dataFromRam_s, dataout_r, done_s, datain_r, enr_r, addr_not_reached, offset_r, row_r, col_r, dataToRam_r, sum_r, muxsel_r, enw_r) is
begin
    muxsel_x <= muxsel_r;
    addr_x <= addr_r1;
    state_x <= state_r;
    sum_x <= sum_r;
    wr_s <= '0';
    rd_s <= '0';
    dataToRam_x <= dataToRam_r;
    dataFromRam_x <= dataFromRam_r1;
    enr_x <= enr_r;
    enw_x <= enw_r;
    datain_x <= datain_r;
    offset_x <= offset_r;
    col_x <= col_r;
    row_x <= row_r;
    case state_r is
        when INIT =>
            enr_x <= '0';
            enw_x <= '0';
            addr_x <= to_unsigned(65536, 23);
            dataToRam_x <= to_unsigned(0, 16);
            datain_x <= to_unsigned(0, 16);
            muxsel_x <= '0';
            offset_x <= to_unsigned(0, 23);
            col_x <= to_unsigned(0, 8);
            row_x <= to_unsigned(0, 8);
            state_x <= WRITE;
        when WRITE =>
            if (done_s = '0') then
                wr_s <= '1';
            elsif (addr_r1 <= 65541) then
                addr_x <= (addr_r1 + 1);
                dataToRam_x <= (dataToRam_r + 1);
            else
                addr_x <= to_unsigned(65536, 23);
                enw_x <= '0';
                enr_x <= '0';
                sum_x <= to_unsigned(0, 16);
                state_x <= READ_AND_SUM_DATA;
            end if;
        when READ_AND_SUM_DATA =>
            if (done_s = '0') then
                rd_s <= '1';
            elsif (addr_r1 <= 65541) then
                sum_x <= (sum_r + dataFromRam_s);
                addr_x <= (addr_r1 + 1);
            else
                muxsel_x <= '1';
                enr_x <= '0';
                addr_x <= to_unsigned(0, 23);
                state_x <= EVEN_SAMPLES;
            end if;
        when CK_SDRAM_RD =>
            if (done_s = '0') then
                rd_s <= '1';
                enw_x <= '0';
            else
                if (addr_r1 <= 1023) then
                    enw_x <= '1';
                    addr_x <= (addr_r1 + 1);
                    datain_x <= dataFromRam_s;
                else
                    addr_x <= to_unsigned(131072, 23);
                    state_x <= CK_SDRAM_WR;
                end if;
            end if;
        when CK_SDRAM_WR =>
            if (done_s = '0') then
                wr_s <= '1';
                enr_x <= '0';
            elsif (addr_r1 <= 132095) then
                enr_x <= '1';
                dataToRam_x <= dataout_r;
                addr_x <= (addr_r1 + 1);
            else
                state_x <= DONE;
            end if;
        when ODD_SAMPLES =>
            if (done_s = '0') then
                rd_s <= '1';
                reset_col <= '0';
            else
                if (offset_r <= 65278) then
                    reset_col <= '1';
                    jp_flgs <= to_unsigned(6, 4);
                    if (addr_not_reached = '1') then
                        offset_x <= (offset_r + 256);
                        row_x <= (row_r + 1);
                    end if;
                    if (row_r = 254) then
                        if (col_r <= 254) then
                            row_x <= to_unsigned(0, 8);
                            offset_x <= (offset_r - 65022);
                            col_x <= (col_r + 1);
                        else
                            offset_x <= to_unsigned(0, 23);
                            row_x <= to_unsigned(0, 8);
                            col_x <= to_unsigned(0, 8);
                            state_x <= DONE;
                        end if;
                    end if;
                end if;
            end if;
        when EVEN_SAMPLES =>
            if (done_s = '0') then
                rd_s <= '1';
                reset_col <= '0';
            else
                if (offset_r <= 65278) then
                    reset_col <= '1';
                    jp_flgs <= to_unsigned(7, 4);
                    if (addr_not_reached = '1') then
                        offset_x <= (offset_r + 256);
                        row_x <= (row_r + 1);
                    end if;
                    if (row_r = 254) then
                        if (col_r <= 254) then
                            row_x <= to_unsigned(0, 8);
                            offset_x <= (offset_r - 65022);
                            col_x <= (col_r + 1);
                        else
                            offset_x <= to_unsigned(0, 23);
                            row_x <= to_unsigned(0, 8);
                            col_x <= to_unsigned(0, 8);
                            state_x <= ODD_SAMPLES;
                        end if;
                    end if;
                end if;
            end if;
        when WR_DATA =>
            if (addr_r1 = 1) then
                addr_x <= to_unsigned(8, 23);
            else
                state_x <= DONE;
            end if;
        when INTERLACE =>
            if (addr_r1 = 16) then
                state_x <= DONE;
            end if;
        when others => -- DONE
            state_x <= INIT;
    end case;
end process XESS_JPEG_TOP_INSTANCE_6_FSM;


XESS_JPEG_TOP_INSTANCE_7_FSMUPDATE: process (clk_fast) is
begin
    if rising_edge(clk_fast) then
        muxsel_r <= muxsel_x;
        addr_r1 <= addr_x;
        dataToRam_r <= dataToRam_x;
        dataFromRam_r1 <= dataFromRam_x;
        state_r <= state_x;
        sum_r <= sum_x;
        empty_r <= empty_x;
        full_r <= full_x;
        enr_r <= enr_x;
        enw_r <= enw_x;
        dataout_r <= dataout_x;
        datain_r <= datain_x;
        offset_r <= offset_x;
        col_r <= col_x;
        row_r <= row_x;
    end if;
end process XESS_JPEG_TOP_INSTANCE_7_FSMUPDATE;

end architecture MyHDL;
