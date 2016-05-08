
import argparse
import subprocess
from pprint import pprint

from myhdl import (Signal, intbv, always_seq, always_comb, concat,ResetSignal,always)

from rhea.cores.uart import uartlite
from rhea.cores.memmap import command_bridge
from rhea.cores.misc import glbl_timer_ticks
from rhea.system import Global, Clock, Reset
from rhea.system import Barebone
from rhea.system import FIFOBus
from rhea.build.boards import get_board


def xula2_blinky_host(clock, led, bcm14_txd, bcm15_rxd):
    """
    The LEDs are controlled from the RPi over the UART
    to the FPGA.
    """
    reset = ResetSignal(0, active=0,async=True)
    glbl = Global(clock, reset)
    ledreg = Signal(intbv(0)[8:])

    # create the timer tick instance
    tick_inst = glbl_timer_ticks(glbl, include_seconds=True)

    # create the interfaces to the UART
    uart_fifo = FIFOBus(width=8, size=4)

    # create the memmap (CSR) interface
    memmap = Barebone(glbl, data_width=32, address_width=32)

    # create the UART instance.
    uart_inst = uartlite(glbl, uart_fifo,
                         serial_in=bcm14_txd,
                         serial_out=bcm15_rxd)

    # create the packet command instance
    cmd_inst = command_bridge(glbl, uart_fifo, memmap)

    @always_seq(clock.posedge, reset=reset)
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
    reset_dly_cnt = Signal(intbv(0)[5:])
    

    @always_seq(clock.posedge, reset=None)
    def beh_assign():
        if glbl.tick_sec:
            tone.next = (~tone) & 0x1
        led.next = ledreg | tone[5:]
	
	
    @always(clock.posedge)
    def reset_tst():
		'''
		For the first 4 clocks the reset is forced to lo
		for clock 6 to 31 the reset is set hi
		then the reset is lo
		'''
		if (reset_dly_cnt < 31):
			reset_dly_cnt.next = reset_dly_cnt + 1
			if (reset_dly_cnt <= 4):
				reset.next = 1
			if (reset_dly_cnt >= 5):
				reset.next = 0
		else:
			reset.next = 1
                        
    return (tick_inst, uart_inst, cmd_inst,
            beh_led_control, beh_led_read, beh_assign, reset_tst)


def build(args):
    brd = get_board('xula2_stickit_mb')
    brd.add_port_name('led', 'pm2', slice(0, 8))
    brd.device = 'XC6SLX9' 
    brd.add_reset('reset', active=0, async=True, pins=('H2',))
    flow = brd.get_flow(top=xula2_blinky_host)
    flow.run()
    info = flow.get_utilization()
    pprint(info)


def program(args):
    subprocess.check_call(["xsload", 
                           "--fpga", "xilinx/xula2_stickit_mb.bit",
                           "-b", "xula2-lx25"])


def cliparse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--build", default=False, action='store_true')
    parser.add_argument("--test", default=False, action='store_true')
    parser.add_argument("--program", default=False, action='store_true')
    parser.add_argument("--walk", default=False, action='store_true')
    args = parser.parse_args()
    return args


def test_instance():    
    # check for basic syntax errors, use test_ice* to test
    # functionality
    xula2_blinky_host(
        clock=Clock(0, frequency=50e6),
        led=Signal(intbv(0)[8:]), 
        uart_tx=Signal(bool(0)),
        uart_rx=Signal(bool(0)), )

    
def main():
    args = cliparse()
    if args.test:
        test_instance()
        
    if args.build:
        build(args)

    if args.program:
        program(args)

    # @todo: add walk function


if __name__ == '__main__':
    main()

