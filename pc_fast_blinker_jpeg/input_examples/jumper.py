from myhdl import *
#from ice40_primitives import *
import argparse
tx = Signal(bool(0))
rx = Signal(bool(0))

def cliparse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--build", default=False, action='store_true')
    parser.add_argument("--test", default=False, action='store_true')
    parser.add_argument("--convert", default=False, action='store_true')
    args = parser.parse_args()
    return args 
def tx_rx(tx,rx):
	@always_comb
	def rtl():
		rx.next = tx
	return rtl

def tb(tx,rx):
	@always(delay(10))
	def clkgen():
		clock.next = not clock
	return instances()

def convert(args):
    toVerilog(tx_rx,tx,rx)

def build(args):
	import rhea.build as build
	from rhea.build.boards import get_board
	#from input_clk import cat_in:


	def run_catboard():
		brd = get_board('catboard')
		#BCM15
		brd.add_port('rx', 'T14')
		#BCM14
		brd.add_port('tx', 'T15')
		flow = brd.get_flow(top=tx_rx)
		flow.run()
	run_catboard()

'''
rx T14 data sent from CAT-Board to RPi2B 
tx T15 data sent from RPi2B to CAT-Board

python jumper.py --build
creates the files
iceriver/catboard.bin
iceriver/catboard.pcf
sudo config_cat iceriver/catboard.bin
'''

def main():
    args = cliparse()
    if args.test:
       tb_fsm = traceSignals(tb,tx,rx)
       sim = Simulation(tb_fsm)
       sim.run()  
    if args.convert:
        convert(args)
    if args.build:
		build(args)
if __name__ == '__main__':
    main() 
