
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
from jpeg import dwt
from signed2twoscomplement import signed2twoscomplement
from l2r import lift2res1
from sh_reg import toSig

WIDTH_OUT = 36
WIDTH = 31
W0 = 9
upd0 = Signal(bool(0))
upd1 = Signal(bool(0))
z0 = Signal(intbv(0)[W0:])
z1 = Signal(intbv(0)[W0:])
done0 = Signal(bool(0))
done1 = Signal(bool(0))
res0 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
res1 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
flgs0 = Signal(intbv(0)[3:])
flgs1 = Signal(intbv(0)[3:])
lft0 = Signal(intbv(0)[W0:])
lft1 = Signal(intbv(0)[W0:])
sam0 = Signal(intbv(0)[W0:])
sam1 = Signal(intbv(0)[W0:])
rht0 = Signal(intbv(0)[W0:])
rht1 = Signal(intbv(0)[W0:])
lift0 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
lift1 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))

upd2 = Signal(bool(0))
upd3 = Signal(bool(0))
z2 = Signal(intbv(0)[W0:])
z3 = Signal(intbv(0)[W0:])
done2 = Signal(bool(0))
done3 = Signal(bool(0))
res2 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
res3 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
flgs2 = Signal(intbv(0)[3:])
flgs3 = Signal(intbv(0)[3:])
lft2 = Signal(intbv(0)[W0:])
lft3 = Signal(intbv(0)[W0:])
sam2 = Signal(intbv(0)[W0:])
sam3 = Signal(intbv(0)[W0:])
rht2 = Signal(intbv(0)[W0:])
rht3 = Signal(intbv(0)[W0:])
lift2 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
lift3 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
myregister0 = Signal(intbv(0)[32:])
myregister1 = Signal(intbv(0)[32:])
myregister2 = Signal(intbv(0)[32:])
myregister3 = Signal(intbv(0)[32:])
def catboard_blinky_host(clock, led, uart_tx, uart_rx):
    """
    The LEDs are controlled from the RPi over the UART
    to the FPGA.
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
    uart_inst = uartlite(glbl, fbustx, fbusrx,
                         serial_in=uart_rx,
                         serial_out=uart_tx)

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
    
    jpeg0 = dwt(flgs0, upd0, lft0, sam0, rht0, lift0, done0, clock)
    l2res0 = lift2res1(lift0,res0)
    sign0 = signed2twoscomplement(res0, z0)

    jpeg1 = dwt(flgs1, upd1, lft1, sam1, rht1, lift1, done1, clock)
    l2res1 = lift2res1(lift1,res1)
    sign1 = signed2twoscomplement(res1, z1)

    jpeg2 = dwt(flgs2, upd2, lft2, sam2, rht2, lift2, done2, clock)
    l2res2 = lift2res1(lift2,res2)
    sign2 = signed2twoscomplement(res2, z2)

    jpeg3 = dwt(flgs3, upd3, lft3, sam3, rht3, lift3, done3, clock)
    l2res3 = lift2res1(lift3,res3)
    sign3 = signed2twoscomplement(res3, z3)

    inst_sig0 = toSig(clock, myregister0,flgs0,lft0,sam0,rht0, upd0) 
    inst_sig1 = toSig(clock, myregister1,flgs1,lft1,sam1,rht1, upd1)
    inst_sig2 = toSig(clock, myregister2,flgs2,lft2,sam2,rht2, upd2) 
    inst_sig3 = toSig(clock, myregister3,flgs3,lft3,sam3,rht3, upd3)
  
    @always_seq(clock.posedge, reset=None) 
    def beh_my_registers():
        if memmap.write:
            if memmap.mem_addr == 0:
                myregister0.next = memmap.write_data
            elif memmap.mem_addr == 4:
                myregister1.next = memmap.write_data
            elif memmap.mem_addr == 8:
                 myregister2.next = memmap.write_data 
            elif memmap.mem_addr == 12:
                 myregister3.next = memmap.write_data        
    return (tick_inst, uart_inst, cmd_inst, 
            beh_led_control, beh_led_read, beh_assign, beh_my_registers,
            jpeg0, l2res0, sign0, jpeg1, l2res1, sign1, 
            jpeg2, l2res2, sign2, jpeg3, l2res3, sign3, 
            inst_sig0, inst_sig1, inst_sig2, inst_sig3)


def build(args):
    brd = get_board('catboard')
    brd.add_port_name('uart_rx', 'bcm14_txd')                           
    brd.add_port_name('uart_tx', 'bcm15_rxd')
    flow = brd.get_flow(top=catboard_blinky_host)
    flow.run()


def program(args):
    subprocess.check_call(["iceprog", "iceriver/icestick.bin"])


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
    catboard_blinky_host(
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

