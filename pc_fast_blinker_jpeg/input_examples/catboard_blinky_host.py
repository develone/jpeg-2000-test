
import argparse
import subprocess

from myhdl import *

from rhea.cores.uart import uartlite
from rhea.cores.memmap import command_bridge
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

upd4 = Signal(bool(0))
upd5 = Signal(bool(0))
z4 = Signal(intbv(0)[W0:])
z5 = Signal(intbv(0)[W0:])
done4 = Signal(bool(0))
done5 = Signal(bool(0))
res4 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
res5 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
flgs4 = Signal(intbv(0)[3:])
flgs5 = Signal(intbv(0)[3:])
lft4 = Signal(intbv(0)[W0:])
lft5 = Signal(intbv(0)[W0:])
sam4 = Signal(intbv(0)[W0:])
sam5 = Signal(intbv(0)[W0:])
rht4 = Signal(intbv(0)[W0:])
rht5 = Signal(intbv(0)[W0:])
lift4 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
lift5 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))

upd6 = Signal(bool(0))
upd7 = Signal(bool(0))
z6 = Signal(intbv(0)[W0:])
z7 = Signal(intbv(0)[W0:])
done6 = Signal(bool(0))
done7 = Signal(bool(0))
res6 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
res7 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
flgs6 = Signal(intbv(0)[3:])
flgs7 = Signal(intbv(0)[3:])
lft6 = Signal(intbv(0)[W0:])
lft7 = Signal(intbv(0)[W0:])
sam6 = Signal(intbv(0)[W0:])
sam7 = Signal(intbv(0)[W0:])
rht6 = Signal(intbv(0)[W0:])
rht7 = Signal(intbv(0)[W0:])
lift6 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
lift7 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))


myregister0 = Signal(intbv(0)[32:])
myregister1 = Signal(intbv(0)[32:])
myregister2 = Signal(intbv(0)[32:])
myregister3 = Signal(intbv(0)[32:])
myregister4 = Signal(intbv(0)[32:])
myregister5 = Signal(intbv(0)[32:])
myregister6 = Signal(intbv(0)[32:])
myregister7 = Signal(intbv(0)[32:])
 
data_to_host0 = Signal(intbv(0)[32:])
data_to_host1 = Signal(intbv(0)[32:])
data_to_host2 = Signal(intbv(0)[32:])
data_to_host3 = Signal(intbv(0)[32:])
def catboard_blinky_host(clock, reset, led, uart_tx, uart_rx):
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
    cmd_inst = command_bridge(glbl, fbusrx, fbustx, memmap)

 

    @always_seq(clock.posedge, reset=None)
    def beh_led_control():
        memmap.done.next = not (memmap.write or memmap.read)
        if memmap.write and memmap.mem_addr == 0x40:
            ledreg.next = memmap.write_data
 
    @always_comb
    def set_data():
       
        data_to_host0.next = z1 << 16 | z0
        data_to_host1.next = z3 << 16 | z2
        data_to_host2.next = z5 << 16 | z4
        data_to_host3.next = z7 << 16 | z6
   
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

    jpeg4 = dwt(flgs4, upd4, lft4, sam4, rht4, lift4, done4, clock)
    l2res4 = lift2res1(lift4,res4)
    sign4 = signed2twoscomplement(res4, z4)

    jpeg5 = dwt(flgs5, upd5, lft5, sam5, rht5, lift5, done5, clock)
    l2res5 = lift2res1(lift5,res5)
    sign5 = signed2twoscomplement(res5, z5)

    jpeg6 = dwt(flgs6, upd6, lft6, sam6, rht6, lift6, done6, clock)
    l2res6 = lift2res1(lift6,res6)
    sign6 = signed2twoscomplement(res6, z6)

    jpeg7 = dwt(flgs7, upd7, lft7, sam7, rht7, lift7, done7, clock)
    l2res7 = lift2res1(lift7,res7)
    sign7 = signed2twoscomplement(res7, z7)
    
    inst_sig0 = toSig(clock, myregister0,flgs0,lft0,sam0,rht0) 
    inst_sig1 = toSig(clock, myregister1,flgs1,lft1,sam1,rht1)
    inst_sig2 = toSig(clock, myregister2,flgs2,lft2,sam2,rht2) 
    inst_sig3 = toSig(clock, myregister3,flgs3,lft3,sam3,rht3)
    
    inst_sig4 = toSig(clock, myregister4,flgs4,lft4,sam4,rht4) 
    inst_sig5 = toSig(clock, myregister5,flgs5,lft5,sam5,rht5)
    inst_sig6 = toSig(clock, myregister6,flgs6,lft6,sam6,rht6) 
    inst_sig7 = toSig(clock, myregister7,flgs7,lft7,sam7,rht7) 

    @always_seq(clock.posedge, reset=None) 
    def beh_my_ret_reg():
        if memmap.read:
            if (memmap.mem_addr == 36):
                memmap.read_data.next = data_to_host0
            if (memmap.mem_addr == 40):
                memmap.read_data.next = data_to_host1 
            if (memmap.mem_addr == 44):
                memmap.read_data.next = data_to_host2
            if (memmap.mem_addr == 48):
                memmap.read_data.next = data_to_host3  
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
            if memmap.mem_addr == 16:
                myregister4.next = memmap.write_data
            elif memmap.mem_addr == 20:
                myregister5.next = memmap.write_data
            elif memmap.mem_addr == 24:
                 myregister6.next = memmap.write_data 
            elif memmap.mem_addr == 28:
                 myregister7.next = memmap.write_data 
            elif memmap.mem_addr == 32:
                 upd0.next = 1    
                 upd1.next = 1 
                 upd2.next = 1
                 upd3.next = 1
                 upd4.next = 1    
                 upd5.next = 1 
                 upd6.next = 1
                 upd7.next = 1
            elif memmap.mem_addr == 36:
                 upd0.next = 0    
                 upd1.next = 0 
                 upd2.next = 0
                 upd3.next = 0
                 upd4.next = 0    
                 upd5.next = 0 
                 upd6.next = 0
                 upd7.next = 0 
    
 
        
    return instances()


def build(args):
    brd = get_board('catboard')
    brd.add_port_name('uart_rx', 'bcm14_txd')                           
    brd.add_port_name('uart_tx', 'bcm15_rxd')
    brd.add_reset('reset', active=0, async=True, pins=('N11',))
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

