from myhdl import *
import argparse

W0 = 31

def cliparse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--build", default=False, action='store_true')
    parser.add_argument("--test", default=False, action='store_true')
    parser.add_argument("--convert", default=False, action='store_true')
    args = parser.parse_args()
    return args 

def ram(dout, din, addr, we, clock, depth=64):
    """  Ram model """
    
    mem = [Signal(intbv(0)[8:]) for i in range(depth)]
    
    @always(clock.posedge)
    def write():
        if we:
            mem[addr].next = din
                
    @always_comb
    def read():
        dout.next = mem[addr]

    return write, read


dout = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
din = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
addr = Signal(intbv(0)[7:])
we = Signal(bool(0))
clock = Signal(bool(0))

def tb(dout,din,addr,we,clock):
	@always(delay(10))
	def clkgen():
		clock.next = not clock
	return instances()
def convert(args):
    #toVerilog.name = 'ram_1'
    toVerilog(ram, dout, din, addr, we, clock)
    #toVHDL(ram, dout, din, addr, we, clock)
    
def main():
    args = cliparse()
    if args.test:
       tb_fsm = traceSignals(tb,dout,din,addr,we,clock)
       sim = Simulation(tb_fsm)
       sim.run()  
    if args.convert:
        convert(args)

if __name__ == '__main__':
    main()
