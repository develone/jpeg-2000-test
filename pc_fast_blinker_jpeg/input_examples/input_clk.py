from myhdl import *
from ice40_primitives import *
import argparse
pi_in = Signal(bool(0))
cat_out = Signal(bool(0))

def cliparse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--build", default=False, action='store_true')
    parser.add_argument("--test", default=False, action='store_true')
    parser.add_argument("--convert", default=False, action='store_true')
    args = parser.parse_args()
    return args 
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
    toVerilog(cat_in,pi_in,cat_out)

def build(args):
	import rhea.build as build
	from rhea.build.boards import get_board
	#from input_clk import cat_in:


	def run_catboard():
		brd = get_board('catboard')
		#LED0
		brd.add_port('cat_out', 'A9')
		#BCM23
		brd.add_port('pi_in', 'P9')
		flow = brd.get_flow(top=cat_in)
		flow.run()
	run_catboard()

'''
LED1	A9  
LED2 	B8
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
if __name__ == '__main__':
    main() 
