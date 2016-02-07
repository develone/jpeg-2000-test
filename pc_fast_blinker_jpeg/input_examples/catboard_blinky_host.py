
import argparse
import subprocess

from myhdl import (Signal, intbv, always_seq, always_comb, concat,)


from rhea.cores.uart import uartlite
from rhea.cores.memmap import memmap_command_bridge
from rhea.cores.misc import glbl_timer_ticks
from rhea.system import Global, Clock, Reset
from rhea.system import Barebone
from rhea.system import FIFOBus
from rhea.build.boards import get_board


def catboard_blinky_host(clock, led, pmod, uart_tx, uart_rx,
                         uart_dtr, uart_rts):
    """
    This example is similar to the other examples in this directory but
    the LEDs are controlled externally via command packets sent from a
    host via the UART on the catboard.

    Ports:
      clock:
      led:
      pmod:
      uart_tx:
      uart_rx:
    """

    glbl = Global(clock, None)
    ledreg = Signal(intbv(0)[8:])

    # create the timer tick instance
    tick_inst = glbl_timer_ticks(glbl, include_seconds=True)

    # create the interfaces to the UART
    fbustx = FIFOBus(width=8, size=4)
    fbusrx = FIFOBus(width=8, size=4)

    # create the memmap (CSR) interface
    memmap = Barebone(glbl, data_width=32, address_width=32)

    # create the UART instance.
    uart_inst = uartlite(glbl, fbustx, fbusrx, uart_rx, uart_tx)

    # create the packet command instance
    cmd_inst = memmap_command_bridge(glbl, fbusrx, fbustx, memmap)

    @always_seq(clock.posedge, reset=None)
    def beh_led_control():
        memmap.done.next = not (memmap.write or memmap.read)
        if memmap.write and memmap.mem_addr == 0x20:
            ledreg.next = memmap.write_data

    @always_comb
    def beh_led_read():
        if memmap.read and memmap.mem_addr == 0x20:
            memmap.read_data.next = ledreg
        else:
            memmap.read_data.next = 0

    # blink one of the LEDs
    tone = Signal(intbv(0)[8:])

    @always_seq(clock.posedge, reset=None)
    def beh_assign():
        if glbl.tick_sec:
            tone.next = (~tone) & 0x1
        led.next = ledreg | tone[5:] 
            
        pmod.next = 0

    # @todo: PMOD OLED memmap control

    return (tick_inst, uart_inst, cmd_inst, 
            beh_led_control, beh_led_read, beh_assign)


def build(args):
    brd = get_board('catboard')
    flow = brd.get_flow(top=catboard_blinky_host)
    flow.run()


def program(args):
    subprocess.check_call(["iceprog", "iceriver/catboard.bin"])


def cliparse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--build", default=False, action='store_true')
    parser.add_argument("--test", default=False, action='store_true')
    parser.add_argument("--program", default=False, action='store_true')
    parser.add_argument("--walk", default=False, action='store_true')
    args = parser.parse_args()
    return args


def main():
    args = cliparse()
    if args.test:
        # check for basic syntax errors, use test_ice* to test
        # functionality
        catboard_blinky_host(
            clock=Clock(0, frequency=100e6),
            led=Signal(intbv(0)[8:]), 
            pmod=Signal(intbv(0)[8:]),
            uart_tx=Signal(bool(0)),
            uart_rx=Signal(bool(0)),
            uart_dtr=Signal(bool(0)),
            uart_rts=Signal(bool(0)) )
        
    if args.build:
        build(args)

    if args.program:
        program(args)

    # @todo: add walk function


if __name__ == '__main__':
    main()

