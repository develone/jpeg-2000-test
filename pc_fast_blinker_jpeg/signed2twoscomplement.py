from myhdl import *
import argparse
import random
'''unsigned data width signed is W0 + 1'''
W0 = 9
clk = Signal(bool(0))
t = Signal(intbv(0, min= -(2**(W0)) ,max= (2**(W0))))  
res_o = Signal(intbv(0, min= -(2**(W0)) ,max= (2**(W0))))
z = Signal(intbv(0)[W0:])

def cliparse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--convert", default=False, action='store_true')
    parser.add_argument("--test", default=False, action='store_true')
    args = parser.parse_args()
    return args

def signed2twoscomplement(res_o, z):
	
	@always_comb
	def unsigned_logic():
		z.next = res_o	
	return unsigned_logic
	    

def tb(clk, res_o, z):
    instance_1 = signed2twoscomplement(res_o, z)
    @always(delay(10))
    def clkgen():
        clk.next = not clk
    @instance
    def stimulus():
        for i in range(-2**(W0),2**(W0),1):
            t.next = i
            yield clk.posedge
            res_o.next = t[W0:]
            yield clk.posedge
            print ("i = %4d 9 bits %s 8 bits %s ") % (i, bin(t,W0+1),bin(t,W0+1)) 
            print ("res_o = %d z.signed() = %d z = %d 9 bits %s 8 bits %s ") % (res_o, z.signed(), z, bin(res_o,W0+1), bin(z, W0))
        raise StopSimulation
    return instances()

def convert(args):
	#toVHDL(signed2twoscomplement, res_o, z)
	toVerilog(signed2twoscomplement, res_o, z) 
 
 
def main():
    args = cliparse()
    if args.test:
       tb_fsm = traceSignals(tb, clk, res_o, z)
       sim = Simulation(tb_fsm)
       sim.run()
    if args.convert:
        convert(args)

if __name__ == '__main__':
    main()
