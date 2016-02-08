from myhdl import *


import argparse
from rhea.cores.memmap import memmap_command_bridge
from rhea.cores.misc import glbl_timer_ticks
from rhea.system import Barebone
from rhea.system import FIFOBus
from rhea.system import Global, Clock, Reset
from rhea.cores.uart import uartlite
from jpeg import dwt
from jpeg_sig import *
from signed2twoscomplement import signed2twoscomplement
from l2r import lift2res1
 
'''
xula2 frequency = 12e6
catboard frequency = 100e6
'''
clock=Clock(0, frequency=100e6)
glbl = Global(clock, None) 

pi_in = Signal(bool(0))
cat_out = Signal(bool(0))
pi_in1 = Signal(bool(0))
cat_out1 = Signal(bool(0))
pi_in2 = Signal(bool(0))
cat_out2 = Signal(bool(0))
pi_in3 = Signal(bool(0))
cat_out3 = Signal(bool(0))


 
def cliparse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--xbuild", default=False, action='store_true')
    parser.add_argument("--build", default=False, action='store_true')
    parser.add_argument("--test", default=False, action='store_true')
    parser.add_argument("--convert", default=False, action='store_true')
     
    args = parser.parse_args()
    return args 

def pi_in2clkInOut(cat_out,clkInOut):
        @always_comb
        def rtl():
            '''The signal pi_in which drives cat_out is going to be used as 
            the clkInOut for transfers between the RPi2B and the FPGA
            '''
            clkInOut.next = cat_out
        return rtl

def cat_in(pi_in,cat_out):
	@always_comb
	def rtl():
		cat_out.next = pi_in
	return rtl

def tb(clock,pi_in,cat_out,pi_in1,cat_out1,pi_in2,cat_out2,pi_in3,cat_out3):
    @always(delay(10))
    def clkgen():
        clock.next = not clock

 
    # create the timer tick instance
    tick_inst = glbl_timer_ticks(glbl, include_seconds=True)
    # create the interfaces to the UART
    fbustx = FIFOBus(width=8, size=4)
    fbusrx = FIFOBus(width=8, size=4)
    fbustx1 = FIFOBus(width=8, size=4)
    fbusrx1 = FIFOBus(width=8, size=4)
    fbustx2 = FIFOBus(width=8, size=4)
    fbusrx2 = FIFOBus(width=8, size=4)
    fbustx3 = FIFOBus(width=8, size=4)
    fbusrx3 = FIFOBus(width=8, size=4)
    # create the memmap (CSR) interface
    memmap = Barebone(glbl, data_width=32, address_width=32)
    memmap1 = Barebone(glbl, data_width=32, address_width=32)
    memmap2 = Barebone(glbl, data_width=32, address_width=32)
    memmap3 = Barebone(glbl, data_width=32, address_width=32)
    # create the packet command instance
    cmd_inst = memmap_command_bridge(glbl, fbusrx, fbustx, memmap)
    cmd_inst1 = memmap_command_bridge(glbl, fbusrx1, fbustx1, memmap1)
    cmd_inst2 = memmap_command_bridge(glbl, fbusrx2, fbustx2, memmap2)
    cmd_inst3 = memmap_command_bridge(glbl, fbusrx3, fbustx3, memmap3)
    # create the UART instance.
    uart_inst = uartlite(glbl, fbustx, fbusrx, pi_in, cat_out)
    uart_inst1 = uartlite(glbl, fbustx1, fbusrx1, pi_in1, cat_out1)
    uart_inst2 = uartlite(glbl, fbustx2, fbusrx2, pi_in2, cat_out2)
    uart_inst3 = uartlite(glbl, fbustx3, fbusrx3, pi_in3, cat_out3)

    jpeg_inst_0 = dwt(flgs0, upd0, lft0, sam0, rht0, lift0, done0, clock)
    l2res_inst_1 = lift2res1(lift0,res0)
    sign_inst_2 = signed2twoscomplement(res0, z0)

    jpeg_inst_3 = dwt(flgs1, upd1, lft1, sam1, rht1, lift1, done1, clock)
    l2res_inst_4 = lift2res1(lift1,res1)
    signed_inst_5 = signed2twoscomplement(res1, z1)

    jpeg_inst_6 = dwt(flgs2, upd2, lft2, sam2, rht2, lift2, done2, clock)
    l2res_inst_7 = lift2res1(lift2,res2) 
    signed_inst_8 = signed2twoscomplement(res2, z2)

    jpeg_inst_9 = dwt(flgs3, upd3, lft3, sam3, rht4, lift3, done3, clock)
    l2res_inst_10 = lift2res1(lift3,res3)
    signed_inst_11 = signed2twoscomplement(res3, z3) 

    @instance
    def tbstim():
        for i in range(2000):
            pi_in.next = 1
            yield clock.posedge
            pi_in.next = 0
            yield clock.posedge
        raise StopSimulation
    return instances()

def convert(args):
    toVerilog(cat_top,clock,pi_in,cat_out,pi_in1,cat_out1,pi_in2,cat_out2,pi_in3,cat_out3)
    #toVHDL(cat_top,clock,pi_in,cat_out,pi_in1,cat_out1,pi_in2,cat_out2,pi_in3,cat_out3)

def build(args):
	import rhea.build as build
	from rhea.build.boards import get_board
	 


	def run_catboard():
		brd = get_board('catboard')
		#LED1
		brd.add_port('cat_out', 'A9')
		#LED2
		brd.add_port('cat_out1', 'B8')
		#LED3
		brd.add_port('cat_out2', 'A7')
		#LED4
		brd.add_port('cat_out3', 'B7')
		#BCM23
		brd.add_port('pi_in', 'P9')
		#BCM19
		brd.add_port('pi_in1', 'T3')
		#BCM24
		brd.add_port('pi_in2', 'T9')
		#BCM20
		brd.add_port('pi_in3', 'R3')
 
                #BCM26
                brd.add_port('ss0', 'T2')
                #BCM27
                brd.add_port('ld_o', 'R10')
		flow = brd.get_flow(top=cat_top)
		flow.run()
	run_catboard()
def xbuild(args):

        from pprint import pprint 
	import rhea.build as build
	from rhea.build.boards import get_board
	 


	def run_xula():
		brd = get_board('xula2')
                brd.device = 'XC6SLX9'
   
		
                #BCM14 BCM27 BCM11 BCM17 BCM15 BCM19 BCM24 BCM25 
                #BCM14/CHAN14
                brd.add_port('cat_out', 'B15')
                #BCM27/CHAN27
                brd.add_port('cat_out1', 'E2')
                #BCM11/CHAN23
                brd.add_port('cat_out2', 'H2')
                #BCM17/CHAN28
                brd.add_port('cat_out3', 'C1')
		#brd.add_port('cat_out3', 'B7')
		#BCM15/CHAN13
		brd.add_port('pi_in', 'B16')
		#BCM19/CHAN2
		brd.add_port('pi_in1', 'R16')
		#BCM24/CHAN10
		brd.add_port('pi_in2', 'F16')
		#BCM25/CHAN9
		brd.add_port('pi_in3', 'F15')
		flow = brd.get_flow(top=cat_top)
		flow.run()
                info = flow.get_utilization()
                pprint(info)
	run_xula()
def cat_top(clock,pi_in,cat_out,pi_in1,cat_out1,pi_in2,cat_out2,pi_in3,cat_out3):
    
 
    # create the timer tick instance
    tick_inst = glbl_timer_ticks(glbl, include_seconds=True)
    # create the interfaces to the UART
    fbustx = FIFOBus(width=8, size=4)
    fbusrx = FIFOBus(width=8, size=4)
    fbustx1 = FIFOBus(width=8, size=4)
    fbusrx1 = FIFOBus(width=8, size=4)
    fbustx2 = FIFOBus(width=8, size=4)
    fbusrx2 = FIFOBus(width=8, size=4)
    fbustx3 = FIFOBus(width=8, size=4)
    fbusrx3 = FIFOBus(width=8, size=4)
    # create the memmap (CSR) interface
    memmap = Barebone(glbl, data_width=32, address_width=32)
    memmap1 = Barebone(glbl, data_width=32, address_width=32)
    memmap2 = Barebone(glbl, data_width=32, address_width=32)
    memmap3 = Barebone(glbl, data_width=32, address_width=32)
    # create the packet command instance
    cmd_inst = memmap_command_bridge(glbl, fbusrx, fbustx, memmap)
    cmd_inst1 = memmap_command_bridge(glbl, fbusrx1, fbustx1, memmap1)
    cmd_inst2 = memmap_command_bridge(glbl, fbusrx2, fbustx2, memmap2)
    cmd_inst3 = memmap_command_bridge(glbl, fbusrx3, fbustx3, memmap3)
    # create the UART instance.
    uart_inst = uartlite(glbl, fbustx, fbusrx, pi_in, cat_out)
    uart_inst1 = uartlite(glbl, fbustx1, fbusrx1, pi_in1, cat_out1)
    uart_inst2 = uartlite(glbl, fbustx2, fbusrx2, pi_in2, cat_out2)
    uart_inst3 = uartlite(glbl, fbustx3, fbusrx3, pi_in3, cat_out3)

    jpeg_inst_0 = dwt(flgs0, upd0, lft0, sam0, rht0, lift0, done0, clock)
    l2res_inst_1 = lift2res1(lift0,res0)
    sign_inst_2 = signed2twoscomplement(res0, z0)

    jpeg_inst_3 = dwt(flgs1, upd1, lft1, sam1, rht1, lift1, done1, clock)
    l2res_inst_4 = lift2res1(lift1,res1)
    signed_inst_5 = signed2twoscomplement(res1, z1)

    jpeg_inst_6 = dwt(flgs2, upd2, lft2, sam2, rht2, lift2, done2, clock)
    l2res_inst_7 = lift2res1(lift2,res2) 
    signed_inst_8 = signed2twoscomplement(res2, z2)

    jpeg_inst_9 = dwt(flgs3, upd3, lft3, sam3, rht4, lift3, done3, clock)
    l2res_inst_10 = lift2res1(lift3,res3)
    signed_inst_11 = signed2twoscomplement(res3, z3) 
    return instances()
'''
LED1	A9  
LED2 	B9
LED3	A7
LED4	B7
python input_clk.py --build
creates the files
iceriver/catboard.bin
iceriver/catboard.pcf

sudo config_cat iceriver/catboard.bin
python dr_input_clk_on.py  turns on led
python dr_input_clk_off.py turns off led
'''

def main():
    args = cliparse()
 

    if args.test:
       tb_fsm = traceSignals(tb,clock,pi_in,cat_out,pi_in1,cat_out1,pi_in2,cat_out2,pi_in3,cat_out3)
       sim = Simulation(tb_fsm)
       sim.run()  
    if args.convert:
        convert(args)
    if args.build:                 
		build(args)
    if args.xbuild:
        xbuild(args)
if __name__ == '__main__':
    main() 
