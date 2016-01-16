from myhdl import *
import argparse
 
WIDTH_OUT = 36

 
 
pp0 = Signal(intbv(0)[WIDTH_OUT:])
 
ss0 = Signal(bool(0))
clk = Signal(bool(0))
ld = Signal(bool(0))
def cliparse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--build", default=False, action='store_true')
    parser.add_argument("--test", default=False, action='store_true')
    parser.add_argument("--convert", default=False, action='store_true')
    args = parser.parse_args()
    return args 

def para2ser(clk, pp0, ss0, ld):
 
    t = Signal(bool(0))
    temp = Signal(intbv(0)[WIDTH_OUT:])
    @always(clk.posedge)
    def logic():

        if (ld == 1):
          temp.next = pp0
        else:
          t.next = temp[35]
          temp.next = concat(temp[35:0], "0")

        ss0.next = t
        
    return logic
  
def tb(clk, pp0, ss0, ld):
    instance_1 = para2ser(clk, pp0, ss0, ld)
     
    @always(delay(10))
    def clkgen():
        clk.next = not clk
    @instance
    def stimulus():
        for i in range(10):
            yield clk.posedge
        pp0.next = 481 << 27
        yield clk.posedge
        
        pp0.next = pp0 + (507 << 18)
        yield clk.posedge
        
        pp0.next = pp0 + (160 << 9)
        yield clk.posedge
        pp0.next = pp0 + 164
        yield clk.posedge
        
        ld.next = 1
        yield clk.posedge
 
        ld.next = 0
        yield clk.posedge

        for j in range(40):
            yield clk.posedge  
        for i in range(100):
             
            pp0.next = 34359738368 + i
            yield clk.posedge
            ld.next = 1
            yield clk.posedge
 
            ld.next = 0
            yield clk.posedge
 
 
            print ("%d") % (ss0 )
            for j in range(40):
               yield clk.posedge
                
                 
 
   
        raise StopSimulation
    
    return instances()
def convert(args): 
    #toVHDL(para2ser,clk, pp0, ss0, ld)
    toVerilog(para2ser,clk, pp0, ss0, ld)    
 
 
def main():
    args = cliparse()
    if args.test:
       tb_fsm = traceSignals(tb,clk, pp0, ss0, ld)
       sim = Simulation(tb_fsm)
       sim.run()  
    if args.convert:
        convert(args)

if __name__ == '__main__':
    main()   
