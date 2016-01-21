from myhdl import *
import argparse
clock = Signal(bool(0))
clkInOut = Signal(bool(0))
ctn = Signal(intbv(0)[3:])
def cliparse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--build", default=False, action='store_true')
    parser.add_argument("--test", default=False, action='store_true')
    parser.add_argument("--convert", default=False, action='store_true')
    args = parser.parse_args()
    return args 

def div_4(clock,clkInOut,ctn):
    
    @always(clock.posedge)
    def rtl():
	if (ctn == 3):
            ctn.next = 0
            clkInOut.next = 1
        else:
            ctn.next = ctn + 1
            if (ctn == 1):
                clkInOut.next = 0
    return rtl

def tb(clock,clkInOut,ctn):
    instance_1 = div_4(clock,clkInOut,ctn)
    @always(delay(10))
    def clkgen():
	clock.next = not clock
    @instance
    def stimulus():
        ctn.next = 0
        yield clock.posedge
        for i in range(4*30):
            yield clock.posedge
        raise StopSimulation	
    return instances()

def convert(args):
    toVerilog(div_4,clock,clkInOut,ctn)

def main():
    args = cliparse()
    if args.test:
       tb_fsm = traceSignals(tb,clock,clkInOut,ctn)
       sim = Simulation(tb_fsm)
       sim.run()  
    if args.convert:
        convert(args)

if __name__ == '__main__':
    main()
 
