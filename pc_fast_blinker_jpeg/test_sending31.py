from myhdl import *
import argparse
from div_clk import div_4
from para2ser import para2ser
from jpeg_sig import *
 
clock = Signal(bool(0))
ctn1 = Signal(intbv(0)[6:]) 
def cliparse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--build", default=False, action='store_true')
    parser.add_argument("--test", default=False, action='store_true')
    parser.add_argument("--convert", default=False, action='store_true')
    args = parser.parse_args()
    return args
def top_sending(clock,clkInOut,ss0, ld_o):
 

    @always(clkInOut.posedge)
    def rtl1():
        if(ctn1 == 0):
            ld.next = 1
        else:
            ld.next = 0
    
    @always(clkInOut.posedge)
    def rtl():
	if (ctn1 == 38):
            ctn1.next = 0
            
        else:
            ctn1.next = ctn1 + 1
            
               
     
    instance_1 = div_4(clock,clkInOut,ctn)
    instance_2 = para2ser(clkInOut, pp0, ss0, ld,ld_o)
    return instances()
def tb(clock,clkInOut,ctn,pp0,ss0,ld_o):
    @always(clkInOut.posedge)
    def rtl1():
        if(ctn1 == 0):
            ld.next = 1
        else:
            ld.next = 0

    @always(clkInOut.posedge)
    def rtl():
	if (ctn1 == 38):
            ctn1.next = 0
            
        else:
            ctn1.next = ctn1 + 1
    instance_1 = div_4(clock,clkInOut,ctn)
    instance_2 = para2ser(clkInOut, pp0, ss0, ld,ld_o)
    
    @always(delay(10))
    def clkgen():
	clock.next = not clock
    @instance
    def stimulus():
         
        pp0.next = 164 << 27
        yield clock.posedge
        
        pp0.next = pp0 + (511 << 18)
        yield clock.posedge
        
        pp0.next = pp0 + (481 << 9)
        yield clock.posedge
        pp0.next = pp0 + 156
        yield clock.posedge
        ld.next = 1
        yield clkInOut.posedge
 
        ld.next = 0
        yield clkInOut.posedge
        for i in range(6*40):
            yield clock.posedge
             
        raise StopSimulation	
    return instances()

def convert(args):
    toVerilog(top_sending,clock,clkInOut,ss0, ld_o)

def main():
    args = cliparse()
    if args.test:
       tb_fsm = traceSignals(tb,clock,clkInOut,ctn,pp0,ss0,ld_o)
       sim = Simulation(tb_fsm)
       sim.run()  
    if args.convert:
        convert(args)

if __name__ == '__main__':
    main()
 
