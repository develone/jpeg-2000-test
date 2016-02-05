from myhdl import *


import argparse
from rhea.cores.memmap import memmap_command_bridge
from rhea.cores.misc import glbl_timer_ticks
from rhea.system import Barebone
from rhea.system import FIFOBus
from rhea.system import Global, Clock, Reset

clock = Signal(bool(0))
clkInOut = Signal(bool(0))
pi_in = Signal(bool(0))
cat_out = Signal(bool(0))
pi_in1 = Signal(bool(0))
cat_out1 = Signal(bool(0))
pi_in2 = Signal(bool(0))
cat_out2 = Signal(bool(0))
pi_in3 = Signal(bool(0))
cat_out3 = Signal(bool(0))
clock=Clock(0, frequency=50e6)
glbl = Global(clock, None)  
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

def tb(pi_in,cat_out):
	@always(delay(10))
	def clkgen():
		clock.next = not clock
	return instances()

def convert(args):
    toVerilog(cat_top,clock,pi_in,cat_out,pi_in1,cat_out1,pi_in2,cat_out2,pi_in3,cat_out3)

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
	#from input_clk import cat_in:


	def run_xula():
		brd = get_board('xula2')
                brd.device = 'XC6SLX9'
                
		#LED1
                #CHAN0
                #brd.add_port('cat_out', 'R7', pullup=True)
                brd.add_port('cat_out', 'R7')
		#brd.add_port('cat_out', 'A9')
		#LED2
                #CHAN22
                brd.add_port('cat_out1', 'H1', pullup=True)
		#brd.add_port('cat_out1', 'B8')
		#LED3
                #CHAN23
                brd.add_port('cat_out2', 'H2', pullup=True)
		#brd.add_port('cat_out2', 'A7')
		#LED4
                #CHAN19
                brd.add_port('cat_out3', 'M1', pullup=True)
		#brd.add_port('cat_out3', 'B7')
		#BCM23
		brd.add_port('pi_in', 'P9')
		#BCM19
		brd.add_port('pi_in1', 'T3')
		#BCM24
		brd.add_port('pi_in2', 'T9')
		#BCM20
		brd.add_port('pi_in3', 'R3')
		flow = brd.get_flow(top=cat_top)
		flow.run()
                info = flow.get_utilization()
                pprint(info)
	run_xula()
def cat_top(clock,pi_in,cat_out,pi_in1,cat_out1,pi_in2,cat_out2,pi_in3,cat_out3):
    
    instance_1 = cat_in(pi_in,cat_out)
    instance_2 = cat_in(pi_in1,cat_out1)
    instance_3 = cat_in(pi_in2,cat_out2)
    instance_4 = cat_in(pi_in3,cat_out3)
    # create the timer tick instance
    tick_inst = glbl_timer_ticks(glbl, include_seconds=True)
    # create the interfaces to the UART
    fbustx = FIFOBus(width=8, size=4)
    fbusrx = FIFOBus(width=8, size=4)
    # create the memmap (CSR) interface
    memmap = Barebone(glbl, data_width=32, address_width=32)
    # create the packet command instance
    cmd_inst = memmap_command_bridge(glbl, fbusrx, fbustx, memmap)

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
       tb_fsm = traceSignals(tb,pi_in,cat_out)
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
