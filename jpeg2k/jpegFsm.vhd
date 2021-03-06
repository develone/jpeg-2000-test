-- File: jpegFsm.vhd
-- Generated by MyHDL 0.9dev
-- Date: Wed Oct 29 12:03:03 2014



package pck_jpegFsm is

attribute enum_encoding: string;

    type t_enum_t_State_1 is (
    ODD_SA,
    EVEN_SA,
    TRAN_RAM
);
attribute enum_encoding of t_enum_t_State_1: type is "001 010 100";

end package pck_jpegFsm;

library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
use std.textio.all;

use work.pck_myhdl_09.all;

use work.pck_jpegFsm.all;

entity jpegFsm is
    port (
        state_r: inout t_enum_t_State_1;
        reset_fsm_r: in std_logic;
        addr_res: out unsigned(8 downto 0);
        offset: out unsigned(11 downto 0);
        offset_r: in unsigned(11 downto 0);
        jp_flgs: out unsigned(3 downto 0);
        reset_n: out std_logic;
        rdy: out std_logic
    );
end entity jpegFsm;


architecture MyHDL of jpegFsm is


constant ACTIVE_LOW: integer := 0;




begin




JPEGFSM_FSM: process (state_r, offset_r, reset_fsm_r) is
begin
    if (reset_fsm_r = '0') then
        -- The start up value for reset_n is 1 |__
        -- Need to added after 70 ns to the line below
        -- which will total 80 ns 
        -- cut after 70 ns and paste in the line below  
        addr_res <= resize(offset_r + 1, 9) after 70 ns;
        reset_n <= '0';
        state_r <= ODD_SA;
    else
        case state_r is
            when ODD_SA =>
                rdy <= '1';
                jp_flgs <= to_unsigned(6, 4);
                offset <= offset_r;
                -- The start up value for reset_n is 1 |__
                -- Need to added after 70 ns to the line below
                -- which will total 80 ns
                -- rdy needs to go hi 30 ns after reset_n goes lo
                -- rdy needs go lo 10 ns before reset_n goes hi
                -- cut after 70 ns and paste in the line below 
                reset_n <= '1' after 70 ns;
                -- The start up value for rdy is 0 __|
                -- rdy needs to go hi 10 ns after reset_n goes lo
                -- rdy needs go lo 10 ns before reset_n goes hi
                -- cut after 60 ns and paste in the line below 
                rdy <= '0' after 60 ns;
                state_r <= ODD_SA;
            when EVEN_SA =>
                jp_flgs <= to_unsigned(7, 4);
                state_r <= ODD_SA;
            when TRAN_RAM =>
                state_r <= ODD_SA;
            when others =>
                assert False report "End of Simulation" severity Failure;
        end case;
    end if;
end process JPEGFSM_FSM;

end architecture MyHDL;
