
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
from jpeg_sig import *
 
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

 

    @always(clock.posedge)
    def beh_led_control():
        memmap.done.next = not (memmap.write or memmap.read)
        if memmap.write and memmap.mem_addr == 0x80:
            ledreg.next = memmap.write_data
 
    @always_comb
    def set_data():
       
        data_to_host0.next = z1 << 16 | z0
        data_to_host1.next = z3 << 16 | z2
        data_to_host2.next = z5 << 16 | z4
        data_to_host3.next = z7 << 16 | z6
        data_to_host4.next = z9 << 16 | z8
        data_to_host5.next = z11 << 16 | z10
        data_to_host6.next = z13 << 16 | z12
        data_to_host7.next = z14 << 16 | z14                 
    # blink one of the LEDs
    tone = Signal(intbv(0)[8:])

    @always(clock.posedge)
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

    jpeg8 = dwt(flgs8, upd8, lft8, sam8, rht8, lift8, done8, clock)
    l2res8 = lift2res1(lift8,res8)
    sign8 = signed2twoscomplement(res8, z8)

    jpeg9 = dwt(flgs9, upd9, lft9, sam9, rht9, lift9, done9, clock)
    l2res9 = lift2res1(lift9,res9)
    sign9 = signed2twoscomplement(res9, z9)

    jpeg10= dwt(flgs10, upd10, lft10, sam10, rht10, lift10, done10, clock)
    l2res10= lift2res1(lift10,res10)
    sign10= signed2twoscomplement(res10, z10)

    jpeg11 = dwt(flgs11, upd11, lft11, sam11, rht11, lift11, done11, clock)
    l2res11 = lift2res1(lift11,res11)
    sign11 = signed2twoscomplement(res11, z11)

    jpeg12 = dwt(flgs12, upd12, lft12, sam12, rht12, lift12, done12, clock)
    l2res12 = lift2res1(lift12,res12)
    sign12 = signed2twoscomplement(res12, z12)

    jpeg13 = dwt(flgs13, upd13, lft13, sam13, rht13, lift13, done13, clock)
    l2res13 = lift2res1(lift13,res13)
    sign13 = signed2twoscomplement(res13, z13)

    jpeg14 = dwt(flgs14, upd14, lft14, sam14, rht14, lift14, done14, clock)
    l2res14 = lift2res1(lift14,res14)
    sign14 = signed2twoscomplement(res14, z14)

    jpeg15 = dwt(flgs15, upd15, lft15, sam15, rht15, lift15, done15, clock)
    l2res15 = lift2res1(lift15,res15)
    sign15 = signed2twoscomplement(res15, z15)
    
 

    inst_sig8 = toSig(clock, myregister8,flgs8,lft8,sam8,rht8) 
    inst_sig9 = toSig(clock, myregister9,flgs9,lft9,sam9,rht9)
    inst_sig10 = toSig(clock, myregister10,flgs10,lft10,sam10,rht10) 
    inst_sig11 = toSig(clock, myregister11,flgs11,lft11,sam11,rht11)
    
    inst_sig12 = toSig(clock, myregister12,flgs12,lft12,sam12,rht12) 
    inst_sig13 = toSig(clock, myregister13,flgs13,lft13,sam13,rht13)
    inst_sig14 = toSig(clock, myregister14,flgs14,lft14,sam14,rht14) 
    inst_sig15 = toSig(clock,myregister15,flgs15,lft15,sam15,rht15) 
    @always(clock.posedge) 
    def beh_my_ret_reg():
        if memmap.read:
            if (memmap.mem_addr == 70):
                memmap.read_data.next = data_to_host0
            if (memmap.mem_addr == 74):
                memmap.read_data.next = data_to_host1 
            if (memmap.mem_addr == 78):
                memmap.read_data.next = data_to_host2
            if (memmap.mem_addr == 82):
                memmap.read_data.next = data_to_host3 
            if (memmap.mem_addr == 86):
                memmap.read_data.next = data_to_host4
            if (memmap.mem_addr == 90):
                memmap.read_data.next = data_to_host5 
            if (memmap.mem_addr == 94):
                memmap.read_data.next = data_to_host6
            if (memmap.mem_addr == 98):
                memmap.read_data.next = data_to_host7 
    @always(clock.posedge) 
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
            if memmap.mem_addr == 32:
                myregister8.next = memmap.write_data
            elif memmap.mem_addr == 36:
                myregister9.next = memmap.write_data
            elif memmap.mem_addr == 40:
                 myregister10.next = memmap.write_data 
            elif memmap.mem_addr == 44:
                 myregister11.next = memmap.write_data 
            if memmap.mem_addr == 48:
                myregister12.next = memmap.write_data
            elif memmap.mem_addr == 52:
                myregister13.next = memmap.write_data
            elif memmap.mem_addr == 56:
                 myregister14.next = memmap.write_data 
            elif memmap.mem_addr == 60:
                 myregister15.next = memmap.write_data                 
            elif memmap.mem_addr == 64:
                 upd0.next = 1    
                 upd1.next = 1 
                 upd2.next = 1
                 upd3.next = 1
                 upd4.next = 1    
                 upd5.next = 1 
                 upd6.next = 1
                 upd7.next = 1
                 upd8.next = 1    
                 upd9.next = 1 
                 upd10.next = 1
                 upd11.next = 1
                 upd12.next = 1    
                 upd13.next = 1 
                 upd14.next = 1
                 upd15.next = 1         
            elif memmap.mem_addr == 36:
                 upd0.next = 0    
                 upd1.next = 0 
                 upd2.next = 0
                 upd3.next = 0
                 upd4.next = 0    
                 upd5.next = 0 
                 upd6.next = 0
                 upd7.next = 0 
                 upd8.next = 0    
                 upd9.next = 0 
                 upd10.next = 0
                 upd11.next = 0
                 upd12.next = 0    
                 upd13.next = 0 
                 upd14.next = 0
                 upd15.next = 0           
 
        
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

