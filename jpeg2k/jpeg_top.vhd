-- File: jpeg_top.vhd
-- Generated by MyHDL 0.9dev
-- Date: Thu Nov 13 16:45:16 2014



package pck_jpeg_top is

attribute enum_encoding: string;

    type t_enum_t_State_1 is (
    INIT,
    ODD_SA,
    EVEN_SA,
    TR_RES,
    TR_INIT,
    TRAN_RAM
);
attribute enum_encoding of t_enum_t_State_1: type is "000001 000010 000100 001000 010000 100000";

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
        offset: inout unsigned(11 downto 0);
        dataFromRam_s: in unsigned(15 downto 0);
        addr_r: inout unsigned(5 downto 0);
        jp_lf: inout unsigned(15 downto 0);
        jp_sa: inout unsigned(15 downto 0);
        jp_rh: inout unsigned(15 downto 0);
        jp_flgs: inout unsigned(3 downto 0);
        reset_n: inout std_logic;
        rdy: inout std_logic;
        sig_in: inout unsigned(51 downto 0);
        noupdate_s: inout std_logic;
        res_s: out signed (15 downto 0);
        state_r: inout t_enum_t_State_1;
        state_x: inout t_enum_t_State_1;
        reset_fsm_r: in std_logic;
        addr_res: inout unsigned(8 downto 0);
        offset_r: inout unsigned(11 downto 0);
        addr_not_reached: inout std_logic;
        addr_rom_r: out unsigned(5 downto 0);
        dataToRam_r: out unsigned(15 downto 0);
        addr_sdram: inout unsigned(5 downto 0);
        wr_s: out std_logic;
        rst: inout std_logic;
        eog: in std_logic;
        rst_file_in: in std_logic;
        addr_r1: in unsigned(5 downto 0);
        addr_r2: in unsigned(5 downto 0);
        sel: in std_logic;
        y: in unsigned(15 downto 0)
    );
end entity jpeg_top;


architecture MyHDL of jpeg_top is


constant ACTIVE_LOW: integer := 0;



signal addr_res_r: unsigned(8 downto 0);
signal instance_7_addr_r: unsigned(5 downto 0);

begin




JPEG_TOP_INSTANCE_1_SDRAM_RD: process (clk_fast) is
begin
    if rising_edge(clk_fast) then
        if bool(reset_n) then
            jp_lf <= to_unsigned(0, 16);
            jp_sa <= to_unsigned(0, 16);
            jp_rh <= to_unsigned(0, 16);
            addr_not_reached <= '0';
            if (jp_flgs(0) = '1') then
                addr_sdram <= resize(1 + offset, 6);
            else
                addr_sdram <= resize(0 + offset, 6);
            end if;
        else
            if bool(jp_flgs(0)) then
                if (addr_sdram = (1 + offset)) then
                    jp_lf <= dataFromRam_s;
                    addr_sdram <= (addr_sdram + 1);
                else
                    if (addr_sdram = (2 + offset)) then
                        jp_sa <= dataFromRam_s;
                        addr_sdram <= (addr_sdram + 1);
                    else
                        if (addr_sdram = (3 + offset)) then
                            jp_rh <= dataFromRam_s;
                            addr_not_reached <= '1';
                        end if;
                    end if;
                end if;
            elsif (addr_sdram = (0 + offset)) then
                jp_lf <= dataFromRam_s;
                addr_sdram <= (addr_sdram + 1);
            else
                if (addr_sdram = (1 + offset)) then
                    jp_sa <= dataFromRam_s;
                    addr_sdram <= (addr_sdram + 1);
                else
                    if (addr_sdram = (2 + offset)) then
                        jp_rh <= dataFromRam_s;
                        addr_not_reached <= '1';
                    end if;
                end if;
            end if;
        end if;
    end if;
end process JPEG_TOP_INSTANCE_1_SDRAM_RD;


JPEG_TOP_INSTANCE_2_RAM2SIG: process (jp_sa, jp_flgs, jp_rh, rdy, addr_not_reached, jp_lf) is
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
end process JPEG_TOP_INSTANCE_2_RAM2SIG;


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


JPEG_TOP_INSTANCE_4_FSM: process (addr_res_r, addr_not_reached, reset_fsm_r, noupdate_s, state_r, offset_r) is
begin
    state_x <= state_r;
    if (reset_fsm_r = '0') then
        offset <= offset_r;
        addr_res <= addr_res_r;
        state_x <= INIT;
    else
        case state_r is
            when INIT =>
                reset_n <= '1';
                rdy <= '0';
                offset <= to_unsigned(0, 12);
                addr_res <= to_unsigned(0, 9);
                state_x <= EVEN_SA;
            when ODD_SA =>
                rdy <= '1';
                reset_n <= '0';
                jp_flgs <= to_unsigned(6, 4);
                offset <= offset_r;
                if (offset_r <= 10) then
                    if ((noupdate_s /= '1') and bool(addr_not_reached)) then
                        offset <= (offset_r + 2);
                        addr_res <= (addr_res_r + 2);
                        rdy <= '1';
                        reset_n <= '1';
                    end if;
                else
                    -- Setting up for next state
                    reset_n <= '1';
                    rdy <= '1';
                    offset <= to_unsigned(1, 12);
                    addr_res <= to_unsigned(2, 9);
                    state_x <= INIT;
                end if;
            when EVEN_SA =>
                rdy <= '1';
                reset_n <= '0';
                jp_flgs <= to_unsigned(7, 4);
                offset <= offset_r;
                if (offset_r <= 12) then
                    if ((noupdate_s /= '1') and bool(addr_not_reached)) then
                        offset <= (offset_r + 2);
                        addr_res <= (addr_res_r + 2);
                        rdy <= '1';
                        reset_n <= '1';
                    end if;
                else
                    -- Need to setup for next state
                    rdy <= '1';
                    reset_n <= '1';
                    rdy <= '0';
                    offset <= to_unsigned(0, 12);
                    addr_res <= to_unsigned(0, 9);
                    state_x <= TR_RES;
                end if;
            when TR_RES =>
                offset <= offset_r;
                addr_res <= to_unsigned(0, 9);
                state_x <= TR_INIT;
            when TR_INIT =>
                reset_n <= '1';
                rdy <= '0';
                offset <= to_unsigned(0, 12);
                addr_res <= to_unsigned(0, 9);
                state_x <= ODD_SA;
            when TRAN_RAM =>
                state_x <= INIT;
            when others =>
                assert False report "End of Simulation" severity Failure;
        end case;
    end if;
end process JPEG_TOP_INSTANCE_4_FSM;


JPEG_TOP_INSTANCE_5_FSMUPDATE: process (clk_fast) is
begin
    if rising_edge(clk_fast) then
        offset_r <= offset;
        state_r <= state_x;
        addr_res_r <= addr_res;
        addr_rom_r <= addr_sdram;
    end if;
end process JPEG_TOP_INSTANCE_5_FSMUPDATE;


JPEG_TOP_INSTANCE_7_FILE_RD: process (clk_fast) is
begin
    if falling_edge(clk_fast) then
        if (rst_file_in = '0') then
            rst <= '1';
            instance_7_addr_r <= to_unsigned(0, 6);
            wr_s <= '1';
        else
            if (rst = '1') then
                rst <= '0';
            elsif (eog = '0') then
                if (instance_7_addr_r <= 48) then
                    dataToRam_r <= y;
                    instance_7_addr_r <= (instance_7_addr_r + 1);
                end if;
            else
                wr_s <= '0';
            end if;
        end if;
    end if;
end process JPEG_TOP_INSTANCE_7_FILE_RD;

end architecture MyHDL;
