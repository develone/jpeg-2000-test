from myhdl import *
import argparse
from jpeg import dwt
from signed2twoscomplement import signed2twoscomplement
from l2r import lift2res1
from sh_reg import ShiftReg, toSig
from para2ser import para2ser
from div_clk import div_4
from jpeg_sig import *
 

clock = Signal(bool(0))
 
 

def cliparse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--build", default=False, action='store_true')
    parser.add_argument("--test", default=False, action='store_true')
    parser.add_argument("--convert", default=False, action='store_true')
    args = parser.parse_args()
    return args 

		
def dwt_top(flgs0, upd0, lft0, sam0, rht0, lift0, done0, clock, res0, z0):
	instance_0 = dwt(flgs0, upd0, lft0, sam0, rht0, lift0, done0, clock)
	instance_16 = lift2res1(lift0,res0)
	instance_70 = signed2twoscomplement(res0, z0)
	
	return instances()	

 
def tb(flgs0, upd0, lft0, sam0, rht0, lift0, done0, clock, res0, z0):
        from PIL import Image
        im = Image.open("../lena_256.png")
        pix = im.load()
        m = list(im.getdata())
        #print m.__sizeof__()
        m = [m[i:i+im.size[0]] for i in range(0, len(m), im.size[0])] 
        #print m
        #print len(m[0]), len(m[1])

	@always(delay(10))
	def clkgen():
		clock.next = not clock
	instance_0 = dwt(flgs0, upd0, lft0, sam0, rht0, lift0, done0, clock)
        instance_16 = lift2res1(lift0,res0)

 
	instance_70 = signed2twoscomplement(res0, z0)
 
	@instance
        def stimulus():
            for col in range(256):
                for row in range(0,256,2):
                    lft0.next = m[row-1][col]
                    yield clock.posedge
                    sam0.next = m[row][col]
                    yield clock.posedge
                    rht0.next = m[row+1][col]
                    yield clock.posedge
                    flgs0.next = 7
                    yield clock.posedge
                    upd0.next = 1
                    yield clock.posedge
                    upd0.next = 0
                    yield clock.posedge
                    #print ("%s %s %s" % (bin(lft0,9),bin(sam0,9),bin(rht0,9)))
                    #print ("%s %d %s" % (bin(flgs0,3),done0,bin(lift0,10)))
                    #res0.next = lift0[W0:]
                    yield clock.posedge
                    #print ("%s %d" % (bin(z0,9),z0))
                    m[row][col] = z0
            for col in range(256):
                for row in range(1,256-1,2):
                    lft0.next = m[row-1][col]
                    yield clock.posedge
                    sam0.next = m[row][col]
                    yield clock.posedge
                    rht0.next = m[row+1][col]
                    yield clock.posedge
                    flgs0.next = 7
                    yield clock.posedge
                    upd0.next = 1
                    yield clock.posedge
                    upd0.next = 0
                    yield clock.posedge
                    #print ("%s %s %s" % (bin(lft0,9),bin(sam0,9),bin(rht0,9)))
                    #print ("%s %d %s" % (bin(flgs0,3),done0,bin(lift0,10)))
                    #res0.next = lift0[W0:]
                    yield clock.posedge
                    #print ("%s %d" % (bin(z0,9),z0))
                    m[row][col] = z0                    
            raise StopSimulation	
	return instances()
 
def convert(args):
    toVerilog(dwt_top,flgs0, upd0, lft0, sam0, rht0, lift0, done0, clock, res0, z0)
    #toVHDL(dwt_top,clock)
 
def main():
    args = cliparse()
    if args.test:
	   tb_fsm = traceSignals(tb,flgs0, upd0, lft0, sam0, rht0, lift0, done0, clock, res0, z0)
	   sim = Simulation(tb_fsm)
	   sim.run()  
    if args.convert:
        convert(args)

if __name__ == '__main__':
    main()
