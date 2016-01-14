from myhdl import *
import argparse
W0 = 9
flgs = Signal(intbv(0)[3:])
lft = Signal(intbv(0)[W0:])
rht = Signal(intbv(0)[W0:])
sam = Signal(intbv(0)[W0:])
clock = Signal(bool(0))
upd = Signal(bool(0))
done = Signal(bool(0))
lift = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
def cliparse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--build", default=False, action='store_true')
    parser.add_argument("--test", default=False, action='store_true')
    parser.add_argument("--convert", default=False, action='store_true')
    args = parser.parse_args()
    return args 
def dwt(flgs,upd,lft,sam,rht,lift,done,clock):
    @always(clock.posedge)
    def rtl ():
        if (upd == 1):
            done.next = 0
            if (flgs == 7):
               lift.next = sam.signed() - ((lft.signed() >> 1) + (rht.signed() >> 1))
            elif (flgs == 5):
               lift.next = sam.signed() + ((lft.signed() >> 1) + (rht.signed() >> 1))
            elif (flgs == 6):
               lift.next = sam.signed() + ((lft.signed() + rht.signed() + 2) >> 2 )
            elif (flgs == 4):
               lift.next = sam.signed() - ((lft.signed() + rht.signed() + 2) >> 2 )
        else:
            done.next = 1
    return rtl

def tb(flgs,upd,lft,sam,rht,lift,done,clock):
    instance_lift = dwt(flgs,upd,lft,sam,rht,lift,done,clock)

    @always(delay(10))
    def clkgen():
        clock.next = not clock

    @instance
    def stimulus():
	lft.next = 164
	yield clock.posedge
	sam.next = 160
	yield clock.posedge
	rht.next = 170
	yield clock.posedge
	flgs.next = 7
	yield clock.posedge
	upd.next = 1
	yield clock.posedge
	upd.next = 0
        yield clock.posedge
        sam.next = 505
        yield clock.posedge
        flgs.next = 5
        yield clock.posedge
        upd.next = 1
        yield clock.posedge
        upd.next = 0
        yield clock.posedge 
        print ('%d %s %s %s %s %s' % (now(),bin(lft,W0), bin(sam,W0), bin(rht,W0), bin(flgs,3),bin(lift,W0)))
        yield clock.posedge
        
        
        raise StopSimulation
    return instances()
def convert(args):
    toVerilog(dwt,flgs,upd,lft,sam,rht,lift,done,clock)
    #toVHDL(dwt_top,clock)
 
def main():
    args = cliparse()
    if args.test:
       tb_fsm = traceSignals(tb,flgs,upd,lft,sam,rht,lift,done,clock)
       sim = Simulation(tb_fsm)
       sim.run()  
    if args.convert:
        convert(args)

if __name__ == '__main__':
    main()
