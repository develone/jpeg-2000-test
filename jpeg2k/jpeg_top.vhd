-- File: jpeg_top.vhd
-- Generated by MyHDL 0.9dev
-- Date: Wed Dec  3 11:52:07 2014



package pck_jpeg_top is

attribute enum_encoding: string;

    type t_enum_t_State_1 is (
    INIT,
    ODD_SA,
    EVEN_SA,
    ODD_SA_COL,
    EVEN_SA_COL,
    TR_RES,
    TR_INIT,
    TRAN_RAM,
    DONE_PASS1
);
attribute enum_encoding of t_enum_t_State_1: type is "000000001 000000010 000000100 000001000 000010000 000100000 001000000 010000000 100000000";

end package pck_jpeg_top;

library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
use std.textio.all;

use work.pck_myhdl_09.all;

use work.pck_jpeg_top.all;

entity jpeg_top is
    port (
        clk_fast: in std_logic;
        rst: inout std_logic;
        eog: in std_logic;
        wr_s: out std_logic;
        rst_file_in: in std_logic;
        addr_r: out unsigned(8 downto 0);
        dataToRam_r: out unsigned(15 downto 0);
        y: in unsigned(15 downto 0);
        addr_r1: inout unsigned(8 downto 0);
        addr_r2: inout unsigned(8 downto 0);
        addr_r3: inout unsigned(8 downto 0);
        addr_r4: inout unsigned(8 downto 0);
        muxsel: inout unsigned(2 downto 0);
        muxsel_r: out unsigned(2 downto 0);
        sig_in: inout unsigned(51 downto 0);
        sig_in1: inout unsigned(51 downto 0);
        sig_in2: inout unsigned(51 downto 0);
        noupdate_s: inout std_logic;
        res_s: out signed (15 downto 0);
        offset: inout unsigned(8 downto 0);
        dataFromRam_s: in unsigned(15 downto 0);
        jp_lf: inout unsigned(15 downto 0);
        jp_sa: inout unsigned(15 downto 0);
        jp_rh: inout unsigned(15 downto 0);
        jp_flgs: inout unsigned(3 downto 0);
        jp_row_lf: inout unsigned(15 downto 0);
        jp_row_sa: inout unsigned(15 downto 0);
        jp_row_rh: inout unsigned(15 downto 0);
        jp_row_flgs: inout unsigned(3 downto 0);
        reset_col: inout std_logic;
        reset_col_r: inout std_logic;
        reset_row: inout std_logic;
        reset_row_r: inout std_logic;
        addr_not_reached: out std_logic;
        addr_not_reached1: inout std_logic;
        addr_not_reached2: inout std_logic;
        rdy: inout std_logic;
        state_r: inout t_enum_t_State_1;
        state_x: inout t_enum_t_State_1;
        reset_fsm_r: inout std_logic;
        addr_res: out unsigned(8 downto 0);
        addr_res1: inout unsigned(8 downto 0);
        addr_res2: inout unsigned(8 downto 0);
        addr_res_r: inout unsigned(8 downto 0);
        offset_r: inout unsigned(8 downto 0);
        dout_res: inout unsigned(15 downto 0);
        din_res: in unsigned(15 downto 0);
        we_res: inout std_logic;
        pass1_done: inout std_logic;
        pass1_done_r: inout std_logic;
        index: inout unsigned(8 downto 0);
        index_r: inout unsigned(8 downto 0);
        col: inout unsigned(3 downto 0);
        col_r: inout unsigned(3 downto 0);
        wr_s1: inout std_logic;
        wr_s2: inout std_logic;
        reset_ctn: inout unsigned(3 downto 0)
    );
end entity jpeg_top;


architecture MyHDL of jpeg_top is


constant YES: integer := 1;
constant NO: integer := 0;
constant reset_dly_c: integer := 10;
constant ACTIVE_LOW: integer := 0;



signal dataToRam_r2: unsigned(15 downto 0);
signal dataToRam_r1: unsigned(15 downto 0);
type t_array_instance_8_mem is array(0 to 256-1) of unsigned(15 downto 0);
signal instance_8_mem: t_array_instance_8_mem;

begin




JPEG_TOP_INSTANCE_1_FILE_RD: process (clk_fast) is
begin
    if falling_edge(clk_fast) then
        if (rst_file_in = '0') then
            rst <= '1';
            addr_r1 <= to_unsigned(0, 9);
            wr_s1 <= '1';
        else
            if (rst = '1') then
                rst <= '0';
            elsif (eog = '0') then
                if (addr_r1 <= 256) then
                    dataToRam_r1 <= y;
                    addr_r1 <= (addr_r1 + 1);
                end if;
            else
                wr_s1 <= '0';
            end if;
        end if;
    end if;
end process JPEG_TOP_INSTANCE_1_FILE_RD;


JPEG_TOP_INSTANCE_2_MUXLOGIC: process (muxsel, wr_s2, wr_s1, addr_r1, addr_r2, addr_r3, sig_in1, dataToRam_r2, dataToRam_r1, addr_not_reached1, addr_not_reached2, addr_r4, addr_res2, sig_in2, addr_res1) is
begin
    addr_r <= addr_r1;
    addr_not_reached <= addr_not_reached1;
    sig_in <= sig_in1;
    wr_s <= wr_s1;
    addr_res <= addr_res1;
    dataToRam_r <= dataToRam_r1;
    if (muxsel = 0) then
        addr_r <= addr_r2;
    elsif (muxsel = 1) then
        addr_r <= addr_r3;
        addr_not_reached <= addr_not_reached2;
        sig_in <= sig_in2;
    elsif (muxsel = 2) then
        wr_s <= wr_s2;
        addr_res <= addr_res2;
        addr_r <= addr_r4;
        dataToRam_r <= dataToRam_r2;
    end if;
end process JPEG_TOP_INSTANCE_2_MUXLOGIC;


JPEG_TOP_INSTANCE_3_JPEG: process (clk_fast) is
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
        else
            noupdate_s <= '1';
        end if;
    end if;
end process JPEG_TOP_INSTANCE_3_JPEG;


JPEG_TOP_INSTANCE_4_SDRAM_RD: process (clk_fast) is
begin
    if rising_edge(clk_fast) then
        if bool(reset_col) then
            jp_lf <= to_unsigned(0, 16);
            jp_sa <= to_unsigned(0, 16);
            jp_rh <= to_unsigned(0, 16);
            addr_not_reached1 <= '0';
            if (jp_flgs(0) = '1') then
                addr_r2 <= (1 + offset);
            else
                addr_r2 <= (0 + offset);
            end if;
        else
            if bool(jp_flgs(0)) then
                if (addr_r2 = (1 + offset)) then
                    jp_lf <= dataFromRam_s;
                    addr_r2 <= (addr_r2 + 16);
                else
                    if (addr_r2 = (17 + offset)) then
                        jp_sa <= dataFromRam_s;
                        addr_r2 <= (addr_r2 + 16);
                    else
                        if (addr_r2 = (33 + offset)) then
                            jp_rh <= dataFromRam_s;
                            addr_not_reached1 <= '1';
                        end if;
                    end if;
                end if;
            elsif (addr_r2 = (0 + offset)) then
                jp_lf <= dataFromRam_s;
                addr_r2 <= (addr_r2 + 16);
            else
                if (addr_r2 = (16 + offset)) then
                    jp_sa <= dataFromRam_s;
                    addr_r2 <= (addr_r2 + 16);
                else
                    if (addr_r2 = (32 + offset)) then
                        jp_rh <= dataFromRam_s;
                        addr_not_reached1 <= '1';
                    end if;
                end if;
            end if;
        end if;
    end if;
end process JPEG_TOP_INSTANCE_4_SDRAM_RD;


JPEG_TOP_INSTANCE_5_RAM2SIG: process (jp_sa, jp_flgs, jp_rh, rdy, addr_not_reached1, jp_lf) is
begin
    if bool(rdy) then
        if bool(addr_not_reached1) then
            sig_in1 <= unsigned'(jp_flgs & jp_rh & jp_sa & jp_lf);
        else
            sig_in1 <= to_unsigned(0, 52);
        end if;
    else
        sig_in1 <= to_unsigned(0, 52);
    end if;
end process JPEG_TOP_INSTANCE_5_RAM2SIG;


JPEG_TOP_INSTANCE_6_FSM: process (pass1_done_r, reset_col_r, reset_row_r, index_r, addr_res_r, addr_not_reached1, reset_fsm_r, col_r, noupdate_s, state_r, offset_r) is
begin
    state_x <= state_r;
    offset <= offset_r;
    addr_res1 <= addr_res_r;
    reset_col <= reset_col_r;
    reset_row <= reset_row_r;
    pass1_done <= pass1_done_r;
    index <= index_r;
    col <= col_r;
    if (reset_fsm_r = '0') then
        offset <= offset_r;
        addr_res1 <= addr_res_r;
        muxsel <= to_unsigned(0, 3);
        col <= to_unsigned(0, 4);
        state_x <= INIT;
    else
        case state_r is
            when INIT =>
                reset_col <= '1';
                rdy <= '0';
                offset <= to_unsigned(15, 9);
                addr_res1 <= to_unsigned(16, 9);
                index <= to_unsigned(0, 9);
                we_res <= '1';
                state_x <= EVEN_SA;
            when ODD_SA =>
                rdy <= '1';
                reset_col <= '0';
                jp_flgs <= to_unsigned(6, 4);
                offset <= offset_r;
                if (offset_r < 205) then
                    if ((noupdate_s /= '1') and bool(addr_not_reached1)) then
                        rdy <= '1';
                        reset_col <= '1';
                    elsif bool(addr_not_reached1) then
                        offset <= (offset_r + 32);
                        addr_res1 <= (addr_res_r + 32);
                    end if;
                else
                    if (col_r <= 14) then
                        col <= (col_r + 1);
                        offset <= (offset_r - 191);
                        addr_res1 <= (addr_res_r - 191);
                    else
                        -- Need to setup for next state
                        rdy <= '1';
                        reset_col <= '1';
                        rdy <= '0';
                        offset <= to_unsigned(2, 9);
                        addr_res1 <= to_unsigned(0, 9);
                        state_x <= TR_RES;
                    end if;
                end if;
            when EVEN_SA =>
                rdy <= '1';
                reset_col <= '0';
                jp_flgs <= to_unsigned(7, 4);
                offset <= offset_r;
                if (offset_r < 207) then
                    if ((noupdate_s /= '1') and bool(addr_not_reached1)) then
                        rdy <= '1';
                        reset_col <= '1';
                    elsif bool(addr_not_reached1) then
                        offset <= (offset_r + 32);
                        addr_res1 <= (addr_res_r + 32);
                    end if;
                else
                    if (col_r <= 14) then
                        col <= (col_r + 1);
                        offset <= (offset_r - 191);
                        addr_res1 <= (addr_res_r - 191);
                    else
                        -- Need to setup for next state
                        rdy <= '1';
                        reset_col <= '1';
                        rdy <= '0';
                        offset <= to_unsigned(0, 9);
                        addr_res1 <= to_unsigned(1, 9);
                        jp_flgs <= to_unsigned(6, 4);
                        we_res <= '0';
                        state_x <= TR_RES;
                    end if;
                end if;
            when TR_RES =>
                offset <= offset_r;
                addr_res1 <= to_unsigned(0, 9);
                state_x <= TR_INIT;
            when TR_INIT =>
                reset_col <= '1';
                rdy <= '0';
                offset <= to_unsigned(0, 9);
                addr_res1 <= to_unsigned(1, 9);
                muxsel <= to_unsigned(0, 3);
                col <= to_unsigned(0, 4);
                state_x <= ODD_SA;
            when TRAN_RAM =>
                state_x <= INIT;
            when DONE_PASS1 =>
                if (reset_col_r = '1') then
                    reset_col <= '1';
                    pass1_done <= '1';
                end if;
            when EVEN_SA_COL =>
                rdy <= '1';
                reset_row <= '0';
                jp_row_flgs <= to_unsigned(7, 4);
                offset <= offset_r;
                if (offset_r <= 252) then
                    if ((noupdate_s /= '1') and bool(addr_not_reached1)) then
                        offset <= (offset_r + 2);
                        addr_res1 <= (addr_res_r + 2);
                        rdy <= '1';
                        reset_col <= '1';
                        case index_r is
                            when "000001111" =>
                                col <= to_unsigned(0, 4);
                            when "000011111" =>
                                col <= to_unsigned(1, 4);
                            when "000101111" =>
                                col <= to_unsigned(2, 4);
                            when "000111111" =>
                                col <= to_unsigned(3, 4);
                            when "001001111" =>
                                col <= to_unsigned(4, 4);
                            when "001011111" =>
                                col <= to_unsigned(5, 4);
                            when "001101111" =>
                                col <= to_unsigned(6, 4);
                            when "001111111" =>
                                col <= to_unsigned(7, 4);
                            when others =>
                                index <= (index_r + 1);
                        end case;
                    end if;
                else
                    -- Need to setup for next state
                    rdy <= '1';
                    reset_col <= '1';
                    rdy <= '0';
                    offset <= to_unsigned(0, 9);
                    addr_res1 <= to_unsigned(0, 9);
                    state_x <= ODD_SA_COL;
                end if;
            when ODD_SA_COL =>
                rdy <= '1';
                reset_row <= '0';
                jp_row_flgs <= to_unsigned(6, 4);
                offset <= offset_r;
                if (offset_r <= 252) then
                    if ((noupdate_s /= '1') and bool(addr_not_reached1)) then
                        offset <= (offset_r + 2);
                        addr_res1 <= (addr_res_r + 2);
                        rdy <= '1';
                        reset_col <= '1';
                        case index_r is
                            when "010001111" =>
                                col <= to_unsigned(8, 4);
                            when "010011111" =>
                                col <= to_unsigned(9, 4);
                            when "010101111" =>
                                col <= to_unsigned(10, 4);
                            when "010111111" =>
                                col <= to_unsigned(11, 4);
                            when "011001111" =>
                                col <= to_unsigned(12, 4);
                            when "011011111" =>
                                col <= to_unsigned(13, 4);
                            when "011101111" =>
                                col <= to_unsigned(14, 4);
                            when "011111111" =>
                                col <= to_unsigned(15, 4);
                            when others =>
                                index <= (index_r + 1);
                        end case;
                    end if;
                else
                    -- Need to setup for next state
                    rdy <= '1';
                    reset_row <= '1';
                    rdy <= '0';
                    offset <= to_unsigned(0, 9);
                    addr_res1 <= to_unsigned(0, 9);
                    state_x <= DONE_PASS1;
                end if;
            when others =>
                assert False report "End of Simulation" severity Failure;
        end case;
    end if;
end process JPEG_TOP_INSTANCE_6_FSM;


JPEG_TOP_INSTANCE_7_FSMUPDATE: process (clk_fast) is
begin
    if rising_edge(clk_fast) then
        offset_r <= offset;
        state_r <= state_x;
        addr_res_r <= addr_res1;
        reset_col_r <= reset_col;
        reset_row_r <= reset_row;
        pass1_done_r <= pass1_done;
        index_r <= index;
        muxsel_r <= muxsel;
        col_r <= col;
    end if;
end process JPEG_TOP_INSTANCE_7_FSMUPDATE;


JPEG_TOP_INSTANCE_8_WRITE: process (clk_fast) is
begin
    if rising_edge(clk_fast) then
        if bool(we_res) then
            instance_8_mem(to_integer(addr_res1)) <= din_res;
        end if;
    end if;
end process JPEG_TOP_INSTANCE_8_WRITE;



dout_res <= instance_8_mem(to_integer(addr_res1));


JPEG_TOP_INSTANCE_9_SDRAM_RD_COL: process (clk_fast) is
begin
    if rising_edge(clk_fast) then
        if bool(reset_row) then
            jp_row_lf <= to_unsigned(0, 16);
            jp_row_sa <= to_unsigned(0, 16);
            jp_row_rh <= to_unsigned(0, 16);
            addr_not_reached2 <= '0';
            if (jp_row_flgs(0) = '1') then
                addr_r3 <= (1 + offset);
            else
                addr_r3 <= (0 + offset);
            end if;
        else
            if bool(jp_row_flgs(0)) then
                if (addr_r3 = (1 + offset)) then
                    jp_row_lf <= dataFromRam_s;
                    addr_r3 <= (addr_r3 + 1);
                else
                    if (addr_r3 = (2 + offset)) then
                        jp_row_sa <= dataFromRam_s;
                        addr_r3 <= (addr_r3 + 1);
                    else
                        if (addr_r3 = (3 + offset)) then
                            jp_row_rh <= dataFromRam_s;
                            addr_not_reached2 <= '1';
                        end if;
                    end if;
                end if;
            elsif (addr_r3 = (0 + offset)) then
                jp_row_lf <= dataFromRam_s;
                addr_r3 <= (addr_r3 + 1);
            else
                if (addr_r3 = (1 + offset)) then
                    jp_row_sa <= dataFromRam_s;
                    addr_r3 <= (addr_r3 + 1);
                else
                    if (addr_r3 = (2 + offset)) then
                        jp_row_rh <= dataFromRam_s;
                        addr_not_reached2 <= '1';
                    end if;
                end if;
            end if;
        end if;
    end if;
end process JPEG_TOP_INSTANCE_9_SDRAM_RD_COL;


JPEG_TOP_INSTANCE_10_RAM2SIGCOL: process (jp_row_lf, jp_row_sa, rdy, jp_row_rh, addr_not_reached2, jp_row_flgs) is
begin
    if bool(rdy) then
        if bool(addr_not_reached2) then
            sig_in2 <= unsigned'(jp_row_flgs & jp_row_rh & jp_row_sa & jp_row_lf);
        else
            sig_in2 <= to_unsigned(0, 52);
        end if;
    else
        sig_in2 <= to_unsigned(0, 52);
    end if;
end process JPEG_TOP_INSTANCE_10_RAM2SIGCOL;


JPEG_TOP_INSTANCE_11_TRRAM: process (clk_fast) is
begin
    if falling_edge(clk_fast) then
        if (addr_r4 <= 256) then
            wr_s2 <= '1';
            dataToRam_r2 <= dout_res;
            addr_r4 <= (addr_r4 + 1);
            addr_res2 <= (addr_res2 + 1);
        else
            wr_s2 <= '0';
        end if;
    end if;
end process JPEG_TOP_INSTANCE_11_TRRAM;


JPEG_TOP_INSTANCE_12_RTL: process (clk_fast) is
begin
    if rising_edge(clk_fast) then
        reset_fsm_r <= '1';
        if (reset_ctn < reset_dly_c) then
            reset_fsm_r <= '0';
            reset_ctn <= (reset_ctn + 1);
        end if;
    end if;
end process JPEG_TOP_INSTANCE_12_RTL;

end architecture MyHDL;
