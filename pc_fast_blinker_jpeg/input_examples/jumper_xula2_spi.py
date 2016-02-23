from myhdl import *
#from ice40_primitives import *
import argparse
mosi = Signal(bool(0))
miso = Signal(bool(0))

def cliparse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--build", default=False, action='store_true')
    parser.add_argument("--test", default=False, action='store_true')
    parser.add_argument("--convert", default=False, action='store_true')
    args = parser.parse_args()
    return args 
def spi(mosi, miso):
	@always_comb
	def rtl():
		miso.next = mosi
	return rtl

def tb(mosi, miso):
	@always(delay(10))
	def clkgen():
		clock.next = not clock
	return instances()

def convert(args):
    toVerilog(spi, mosi, miso)

def build(args):
	import rhea.build as build
	from rhea.build.boards import get_board
	#from input_clk import cat_in:


	def run_xula2():
		brd = get_board('xula2')
                brd.device = 'XC6SLX9' 
		#BCM25
		brd.add_port('mosi', 'F2')
		#BCM24
		brd.add_port('miso', 'F1')
		flow = brd.get_flow(top=spi)
		flow.run()
	run_xula2()

'''
rx B16 data sent from xula2 to RPi2B 
tx B15 data sent from RPi2B to xula2

python jumper_xula2.py --build
creates the files
xilinx/xula2.bit
xilinx/xula2.pcf
xsload --usb 0 xula2_jum.bit
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
