from myhdl import *
import argparse
ACTIVE_LOW = 0

WIDTH = 31
W0 = 9
po = Signal(intbv(0)[WIDTH:])
si = Signal(bool(0))
fB = Signal(bool(0))
clk = Signal(bool(0))
reset = Signal(bool(1))

upd_o = Signal(bool(0))
sig = Signal(intbv(0)[WIDTH:])
flgs_o = Signal(intbv(0)[3:])
lft_o = Signal(intbv(0)[W0:])
rht_o = Signal(intbv(0)[W0:])
sam_o = Signal(intbv(0)[W0:])

def cliparse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--convert", default=False, action='store_true')
    parser.add_argument("--test", default=False, action='store_true')
    args = parser.parse_args()
    return args
def ShiftReg(clk, WIDTH, reset, fB, si, po):

   reg = Signal(intbv(0)[WIDTH:])

   @always(clk.posedge, reset.negedge)
   def SRProcess():

       if reset == ACTIVE_LOW:
           reg.next = 0
           po.next = 0
       else:
           reg.next[WIDTH:1] = reg[WIDTH-1:]
           reg.next[0] = si
           if fB: # pulse indicating first input bit of a word
               po.next = reg

   return instances()
def toSig(clk, sig,flgs_o,lft_o,sam_o,rht_o, upd_o):
    lft_s = sig(9,0)
    sam_s = sig(18,9)
    rht_s = sig(27,18)
    flgs_s = sig(30,27)
    upd_s = sig(31,30)
    @always_comb
    def rtl():
        flgs_o.next = flgs_s
        rht_o.next = rht_s
        sam_o.next = sam_s
        lft_o.next = lft_s
        upd_o.next = upd_s
    return rtl
 
def tb(clk, WIDTH, reset, fB, si, po, sig,flgs_o,lft_o,sam_o,rht_o,upd_o):
    instance_1 = ShiftReg(clk, WIDTH, reset, fB, si, po)
    instance_2 = toSig(clk, sig,flgs_o,lft_o,sam_o,rht_o,upd_o)
    @always(delay(10))
    def clkgen():
        clk.next = not clk

    @instance
    def stimulus():
        reset.next = 1
        yield clk.posedge
        print ("reset %d ") % (reset)
        reset.next = 0
        yield clk.posedge
        print ("reset %d ") % (reset)
        reset.next = 1
        yield clk.posedge
        print ("reset %d ") % (reset)
        fB.next = 1
        yield clk.posedge
        print ("fB %d ") % (fB)
        si.next = 1
        yield clk.posedge
        print ("31 bits %s %d ") % (bin(po,31),si)
        si.next = 1
        yield clk.posedge
        print ("31 bits %s %d ") % (bin(po,31),si)
        si.next = 1
        yield clk.posedge
        print ("31 bits %s %d ") % (bin(po,31),si)
        si.next = 1
        yield clk.posedge
        print ("31 bits %s %d ") % (bin(po,31),si)
        print ("fB %d ") % (fB)
        si.next = 1
        yield clk.posedge
        print ("31 bits %s %d ") % (bin(po,31),si)
        si.next = 1
        yield clk.posedge
        print ("31 bits %s %d ") % (bin(po,31),si)
        si.next = 1
        yield clk.posedge
        print ("31 bits %s %d ") % (bin(po,31),si)
        si.next = 1
        yield clk.posedge
        print ("31 bits %s %d ") % (bin(po,31),si)
        si.next = 1
        yield clk.posedge
        print ("31 bits %s %d ") % (bin(po,31),si)
        si.next = 1
        yield clk.posedge
        print ("31 bits %s %d ") % (bin(po,31),si)
        si.next = 0
        yield clk.posedge
        print ("31 bits %s %d ") % (bin(po,31),si)
        si.next = 1
        yield clk.posedge
        print ("31 bits %s %d ") % (bin(po,31),si)
        si.next = 0
        yield clk.posedge
        print ("31 bits %s %d ") % (bin(po,31),si)
        si.next = 1
        yield clk.posedge
        print ("31 bits %s %d ") % (bin(po,31),si)
        si.next = 1
        yield clk.posedge
        print ("31 bits %s %d ") % (bin(po,31),si)
        si.next = 1
        yield clk.posedge
        print ("31 bits %s %d ") % (bin(po,31),si)
        si.next = 0
        yield clk.posedge
        print ("31 bits %s %d ") % (bin(po,31),si)
        si.next = 1
        yield clk.posedge
        print ("31 bits %s %d ") % (bin(po,31),si)
        si.next = 0
        yield clk.posedge
        print ("31 bits %s %d ") % (bin(po,31),si)
        si.next = 1
        yield clk.posedge
        print ("31 bits %s %d ") % (bin(po,31),si)
        si.next = 0
        yield clk.posedge
        print ("31 bits %s %d ") % (bin(po,31),si)
        si.next = 1
        yield clk.posedge
        print ("31 bits %s %d ") % (bin(po,31),si)
        si.next = 0
        yield clk.posedge
        print ("31 bits %s %d ") % (bin(po,31),si)
        si.next = 1
        yield clk.posedge
        print ("31 bits %s %d ") % (bin(po,31),si)
        si.next = 0
        yield clk.posedge
        print ("31 bits %s %d ") % (bin(po,31),si)
        si.next = 1
        yield clk.posedge
        print ("31 bits %s %d ") % (bin(po,31),si)
        si.next = 0
        yield clk.posedge
        print ("31 bits %s %d ") % (bin(po,31),si)
        si.next = 1
        yield clk.posedge
        print ("31 bits %s %d ") % (bin(po,31),si)
        si.next = 0
        yield clk.posedge
        print ("31 bits %s %d ") % (bin(po,31),si)
        si.next = 1
        yield clk.posedge
        print ("31 bits %s %d ") % (bin(po,31),si)
        si.next = 0
        yield clk.posedge
        print ("31 bits %s %d ") % (bin(po,31),si)
        si.next = 1
        yield clk.posedge
        print ("31 bits %s %d ") % (bin(po,31),si)
        si.next = 0
        yield clk.posedge
        print ("31 bits %s %d ") % (bin(po,31),si)
        
        si.next = 1
        yield clk.posedge
        print ("31 bits %s %d ") % (bin(po,31),si)
        si.next = 0
        yield clk.posedge
        print ("31 bits %s %d ") % (bin(po,31),si)
        si.next = 1
        yield clk.posedge
        print ("31 bits %s %d ") % (bin(po,31),si)
        sig.next = po
        yield clk.posedge
        
        for i in range(10):
            yield clk.posedge
        raise StopSimulation
    return instances() 
 
def convert(args):
    toVerilog.name = "shift_reg"
    SHIFT_REG_0 = toVerilog(ShiftReg, clk, WIDTH, reset, fB, si, po)
    toVerilog(toSig, clk, sig,flgs_o,lft_o,sam_o,rht_o,upd_o)
    #toVHDL(dwt_top,clock)
 
def main():
    args = cliparse()
    if args.test:
       tb_fsm = traceSignals(tb, clk, WIDTH, reset, fB, si, po, sig,flgs_o,lft_o,sam_o,rht_o,upd_o)
       sim = Simulation(tb_fsm)
       sim.run()  
    if args.convert:
        convert(args)

if __name__ == '__main__':
    main()


