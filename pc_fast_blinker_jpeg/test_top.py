from myhdl import *

from jpeg import dwt
from signed2twoscomplement import signed2twoscomplement
from l2r import lift2res
from sh_reg import ShiftReg, toSig

WIDTH = 31
W0 = 9

clock = Signal(bool(0))
'''
Signals needed for sh_reg
'''
po0 = Signal(intbv(0)[WIDTH:])
si0 = Signal(bool(0))
fB0 = Signal(bool(0))
reset = Signal(bool(1))

po1 = Signal(intbv(0)[WIDTH:])
si1 = Signal(bool(0))
fB1 = Signal(bool(0))

po2 = Signal(intbv(0)[WIDTH:])
si2 = Signal(bool(0))
fB2 = Signal(bool(0))

po3 = Signal(intbv(0)[WIDTH:])
si3 = Signal(bool(0))
fB3 = Signal(bool(0))

po4 = Signal(intbv(0)[WIDTH:])
si4 = Signal(bool(0))
fB4 = Signal(bool(0))
reset = Signal(bool(1))

po5 = Signal(intbv(0)[WIDTH:])
si5 = Signal(bool(0))
fB5 = Signal(bool(0))

po6 = Signal(intbv(0)[WIDTH:])
si6 = Signal(bool(0))
fB6 = Signal(bool(0))

po7 = Signal(intbv(0)[WIDTH:])
si7 = Signal(bool(0))
fB7 = Signal(bool(0))

sig0 = Signal(intbv(0)[WIDTH:])
sig1 = Signal(intbv(0)[WIDTH:])
sig2 = Signal(intbv(0)[WIDTH:])
sig3 = Signal(intbv(0)[WIDTH:])
sig4 = Signal(intbv(0)[WIDTH:])
sig5 = Signal(intbv(0)[WIDTH:])
sig6 = Signal(intbv(0)[WIDTH:])
sig7 = Signal(intbv(0)[WIDTH:])

upd0 = Signal(bool(0))
upd1 = Signal(bool(0))
upd2 = Signal(bool(0))
upd3 = Signal(bool(0))
upd4 = Signal(bool(0))
upd5 = Signal(bool(0))
upd6 = Signal(bool(0))
upd7 = Signal(bool(0))
'''
Signals need to convert signed data 
to unsigned
'''
z0 = Signal(intbv(0)[W0:])
z1 = Signal(intbv(0)[W0:])
z2 = Signal(intbv(0)[W0:])
z3 = Signal(intbv(0)[W0:])
z4 = Signal(intbv(0)[W0:])
z5 = Signal(intbv(0)[W0:])
z6 = Signal(intbv(0)[W0:])
z7 = Signal(intbv(0)[W0:])
done0 = Signal(bool(0))
done1 = Signal(bool(0))
done2 = Signal(bool(0))
done3 = Signal(bool(0))
done4 = Signal(bool(0))
done5 = Signal(bool(0))
done6 = Signal(bool(0))
done7 = Signal(bool(0))
lift0 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
res0 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
res1 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
res2 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
res3 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
res4 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
res5 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
res6 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
res7 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))

flgs0 = Signal(intbv(0)[3:])
lft0 = Signal(intbv(0)[W0:])
rht0 = Signal(intbv(0)[W0:])
sam0 = Signal(intbv(0)[W0:])

flgs1 = Signal(intbv(0)[3:])
lft1 = Signal(intbv(0)[W0:])
rht1 = Signal(intbv(0)[W0:])
sam1 = Signal(intbv(0)[W0:])
lift1 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))

flgs2 = Signal(intbv(0)[3:])
lft2 = Signal(intbv(0)[W0:])
rht2 = Signal(intbv(0)[W0:])
sam2 = Signal(intbv(0)[W0:])
lift2 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))

flgs3 = Signal(intbv(0)[3:])
lft3 = Signal(intbv(0)[W0:])
rht3 = Signal(intbv(0)[W0:])
sam3 = Signal(intbv(0)[W0:])
lift3 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))

flgs4 = Signal(intbv(0)[3:])
lft4= Signal(intbv(0)[W0:])
rht4 = Signal(intbv(0)[W0:])
sam4 = Signal(intbv(0)[W0:])
lift4 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))

flgs5 = Signal(intbv(0)[3:])
lft5= Signal(intbv(0)[W0:])
rht5 = Signal(intbv(0)[W0:])
sam5 = Signal(intbv(0)[W0:])
lift5 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))

flgs6 = Signal(intbv(0)[3:])
lft6= Signal(intbv(0)[W0:])
rht6 = Signal(intbv(0)[W0:])
sam6 = Signal(intbv(0)[W0:])
lift6 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))

flgs7 = Signal(intbv(0)[3:])
lft7= Signal(intbv(0)[W0:])
rht7 = Signal(intbv(0)[W0:])
sam7 = Signal(intbv(0)[W0:])
lift7 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))

 

		
def dwt_top(clock):
	instance_0 = dwt(flgs0, upd0, lft0, sam0, rht0, lift0, done0, clock)
	instance_1 = dwt(flgs1, upd1, lft1, sam1, rht1, lift1, done1, clock)
	instance_2 = dwt(flgs2, upd2, lft2, sam2, rht2, lift2, done2, clock)
	instance_3 = dwt(flgs3, upd3, lft3, sam3, rht3, lift3, done3, clock)
	instance_4 = dwt(flgs4, upd0, lft4, sam4, rht4, lift4, done4, clock)
	instance_5 = dwt(flgs5, upd1, lft5, sam5, rht5, lift5, done5, clock)
	instance_6 = dwt(flgs6, upd2, lft6, sam6, rht6, lift6, done6, clock)
	instance_7 = dwt(flgs7, upd3, lft7, sam7, rht7, lift7, done7, clock)
	
	instance_8 = lift2res(lift0,res0, lift1,res1, lift2,res2, lift3,res3, lift4,res4, lift5,res5,lift6,res6,lift7,res7)
        
        instance_9 = ShiftReg(clock, WIDTH, reset, fB0, si0, po0)
        instance_10 = toSig(clock, sig0,flgs0,lft0,sam0,rht0, upd0)
        instance_11 = ShiftReg(clock, WIDTH, reset, fB1, si1, po1)
        instance_12 = toSig(clock, sig1,flgs1,lft1,sam1,rht1, upd1)
        instance_13 = ShiftReg(clock, WIDTH, reset, fB2, si2, po2)
        instance_14 = toSig(clock, sig2,flgs2,lft2,sam2,rht2, upd2)
        instance_15 = ShiftReg(clock, WIDTH, reset, fB3, si3, po3)
        instance_16 = toSig(clock, sig3,flgs3,lft3,sam3,rht3, upd3)  
        instance_17 = ShiftReg(clock, WIDTH, reset, fB4, si4, po4)
        instance_18 = toSig(clock, sig4,flgs4,lft4,sam4,rht4, upd4)
        instance_19 = ShiftReg(clock, WIDTH, reset, fB5, si5, po5)
        instance_20 = toSig(clock, sig5,flgs5,lft5,sam5,rht5, upd5)
        instance_21 = ShiftReg(clock, WIDTH, reset, fB6, si6, po6)
        instance_22 = toSig(clock, sig6,flgs6,lft6,sam6,rht6, upd6)
        instance_23 = ShiftReg(clock, WIDTH, reset, fB7, si7, po7)
        instance_24 = toSig(clock, sig7,flgs7,lft7,sam7,rht7, upd7)  
 
	instance_25 = signed2twoscomplement(res0, z0)
	instance_26 = signed2twoscomplement(res1, z1)
	instance_27 = signed2twoscomplement(res2, z2)
	instance_28 = signed2twoscomplement(res3, z3)
	instance_29 = signed2twoscomplement(res4, z4)
	instance_30 = signed2twoscomplement(res5, z5)
	instance_31 = signed2twoscomplement(res6, z6)
	instance_32 = signed2twoscomplement(res7, z7)
	return instances()	

 
def tb(clock):
	@always(delay(10))
	def clkgen():
		clock.next = not clock
	instance_0 = dwt(flgs0, upd0, lft0, sam0, rht0, lift0, done0, clock)
	instance_1 = dwt(flgs1, upd1, lft1, sam1, rht1, lift1, done1, clock)
	instance_2 = dwt(flgs2, upd2, lft2, sam2, rht2, lift2, done2, clock)
	instance_3 = dwt(flgs3, upd3, lft3, sam3, rht3, lift3, done3, clock)
	instance_4 = dwt(flgs4, upd0, lft4, sam4, rht4, lift4, done4, clock)
	instance_5 = dwt(flgs5, upd1, lft5, sam5, rht5, lift5, done5, clock)
	instance_6 = dwt(flgs6, upd2, lft6, sam6, rht6, lift6, done6, clock)
	instance_7 = dwt(flgs7, upd3, lft7, sam7, rht7, lift7, done7, clock)
	instance_8 = lift2res(lift0,res0, lift1,res1, lift2,res2, lift3,res3, lift4,res4, lift5,res5,lift6,res6,lift7,res7)
        instance_9 = ShiftReg(clock, WIDTH, reset, fB0, si0, po0)
        instance_10 = toSig(clock, sig0,flgs0,lft0,sam0,rht0, upd0)
        instance_11 = ShiftReg(clock, WIDTH, reset, fB1, si1, po1)
        instance_12 = toSig(clock, sig1,flgs1,lft1,sam1,rht1, upd1)
        instance_13 = ShiftReg(clock, WIDTH, reset, fB2, si2, po2)
        instance_14 = toSig(clock, sig2,flgs2,lft2,sam2,rht2, upd2)
        instance_15 = ShiftReg(clock, WIDTH, reset, fB3, si3, po3)
        instance_16 = toSig(clock, sig3,flgs3,lft3,sam3,rht3, upd3)  
        instance_17 = ShiftReg(clock, WIDTH, reset, fB4, si4, po4)
        instance_18 = toSig(clock, sig4,flgs4,lft4,sam4,rht4, upd4)
        instance_19 = ShiftReg(clock, WIDTH, reset, fB5, si5, po5)
        instance_20 = toSig(clock, sig5,flgs5,lft5,sam5,rht5, upd5)
        instance_21 = ShiftReg(clock, WIDTH, reset, fB6, si6, po6)
        instance_22 = toSig(clock, sig6,flgs6,lft6,sam6,rht6, upd6)
        instance_23 = ShiftReg(clock, WIDTH, reset, fB7, si7, po7)
        instance_24 = toSig(clock, sig7,flgs7,lft7,sam7,rht7, upd7)  
 
	instance_25 = signed2twoscomplement(res0, z0)
	instance_26 = signed2twoscomplement(res1, z1)
	instance_27 = signed2twoscomplement(res2, z2)
	instance_28 = signed2twoscomplement(res3, z3)
	instance_29 = signed2twoscomplement(res4, z4)
	instance_30 = signed2twoscomplement(res5, z5)
	instance_31 = signed2twoscomplement(res6, z6)
	instance_32 = signed2twoscomplement(res7, z7)

	@instance
        def stimulus():
            reset.next = 1
            yield clock.posedge
            print ("reset %d ") % (reset)
            reset.next = 0
            yield clock.posedge
            print ("reset %d ") % (reset)
            reset.next = 1
            yield clock.posedge
            print ("reset %d ") % (reset)
            fB0.next = 1
            yield clock.posedge
            print ("fB0 %d ") % (fB0)
            si0.next = 1
            yield clock.posedge
            print ("31 bits %s %d ") % (bin(po0,31),si0)
            si0.next = 1
            yield clock.posedge
            print ("31 bits %s %d ") % (bin(po0,31),si0)
            si0.next = 1
            yield clock.posedge
            print ("31 bits %s %d ") % (bin(po0,31),si0)
            si0.next = 1
            yield clock.posedge
            print ("31 bits %s %d ") % (bin(po0,31),si0)
            print ("fB0 %d ") % (fB0)
            si0.next = 1
            yield clock.posedge
            print ("31 bits %s %d ") % (bin(po0,31),si0)
            si0.next = 1
            yield clock.posedge
            print ("31 bits %s %d ") % (bin(po0,31),si0)
            si0.next = 1
            yield clock.posedge
            print ("31 bits %s %d ") % (bin(po0,31),si0)
            si0.next = 1
            yield clock.posedge
            print ("31 bits %s %d ") % (bin(po0,31),si0)
            si0.next = 1
            yield clock.posedge
            print ("31 bits %s %d ") % (bin(po0,31),si0)
            si0.next = 1
            yield clock.posedge
            print ("31 bits %s %d ") % (bin(po0,31),si0)
            si0.next = 0
            yield clock.posedge
            print ("31 bits %s %d ") % (bin(po0,31),si0)
            si0.next = 1
            yield clock.posedge
            print ("31 bits %s %d ") % (bin(po0,31),si0)
            si0.next = 0
            yield clock.posedge
            print ("31 bits %s %d ") % (bin(po0,31),si0)
            si0.next = 1
            yield clock.posedge
            print ("31 bits %s %d ") % (bin(po0,31),si0)
            si0.next = 1
            yield clock.posedge
            print ("31 bits %s %d ") % (bin(po0,31),si0)
            si0.next = 1
            yield clock.posedge
            print ("31 bits %s %d ") % (bin(po0,31),si0)
            si0.next = 0
            yield clock.posedge
            print ("31 bits %s %d ") % (bin(po0,31),si0)
            si0.next = 1
            yield clock.posedge
            print ("31 bits %s %d ") % (bin(po0,31),si0)
            si0.next = 0
            yield clock.posedge
            print ("31 bits %s %d ") % (bin(po0,31),si0)
            si0.next = 1
            yield clock.posedge
            print ("31 bits %s %d ") % (bin(po0,31),si0)
            si0.next = 0
            yield clock.posedge
            print ("31 bits %s %d ") % (bin(po0,31),si0)
            si0.next = 1
            yield clock.posedge
            print ("31 bits %s %d ") % (bin(po0,31),si0)
            si0.next = 0
            yield clock.posedge
            print ("31 bits %s %d ") % (bin(po0,31),si0)
            si0.next = 1
            yield clock.posedge
            print ("31 bits %s %d ") % (bin(po0,31),si0)
            si0.next = 0
            yield clock.posedge
            print ("31 bits %s %d ") % (bin(po0,31),si0)
            si0.next = 1
            yield clock.posedge
            print ("31 bits %s %d ") % (bin(po0,31),si0)
            si0.next = 0
            yield clock.posedge
            print ("31 bits %s %d ") % (bin(po0,31),si0)
            si0.next = 1
            yield clock.posedge
            print ("31 bits %s %d ") % (bin(po0,31),si0)
            si0.next = 0
            yield clock.posedge
            print ("31 bits %s %d ") % (bin(po0,31),si0)
            si0.next = 1
            yield clock.posedge
            print ("31 bits %s %d ") % (bin(po0,31),si0)
            si0.next = 0
            yield clock.posedge
            print ("31 bits %s %d ") % (bin(po0,31),si0)
            si0.next = 1
            yield clock.posedge
            print ("31 bits %s %d ") % (bin(po0,31),si0)
            si0.next = 0
            yield clock.posedge
            print ("31 bits %s %d ") % (bin(po0,31),si0)
            
            si0.next = 1
            yield clock.posedge
            print ("31 bits %s %d ") % (bin(po0,31),si0)
            si0.next = 0
            yield clock.posedge
            print ("31 bits %s %d ") % (bin(po0,31),si0)
            si0.next = 1
            yield clock.posedge
            print ("31 bits %s %d ") % (bin(po0,31),si0)
            sig0.next = po0
            yield clock.posedge
            sig1.next = po0
            yield clock.posedge
            sig2.next = po0
            yield clock.posedge
            sig3.next = po0
            yield clock.posedge
            sig4.next = po0
            yield clock.posedge
            sig5.next = po0
            yield clock.posedge
            sig6.next = po0
            yield clock.posedge
            sig7.next = po0
            yield clock.posedge
            for i in range(10):
                yield clock.posedge
            
	    lft0.next = 164
	    yield clock.posedge
	    sam0.next = 160
	    yield clock.posedge
	    rht0.next = 170
	    yield clock.posedge
	    flgs0.next = 7
	    yield clock.posedge
	    upd0.next = 1
	    yield clock.posedge
	    upd0.next = 0
	    yield clock.posedge
 
            sam0.next = 505
            yield clock.posedge
            flgs0.next = 5
            yield clock.posedge
            upd0.next = 1
            yield clock.posedge
            upd0.next = 0
 
	    lft1.next = 164
	    yield clock.posedge
	    sam1.next = 160
	    yield clock.posedge
	    rht1.next = 170
	    yield clock.posedge
	    flgs1.next = 7
	    yield clock.posedge
	    upd1.next = 1
	    yield clock.posedge
	    upd1.next = 0
            yield clock.posedge
 
            sam1.next = 505
            yield clock.posedge
            flgs1.next = 5
            yield clock.posedge
            upd1.next = 1
            yield clock.posedge
            upd1.next = 0
            yield clock.posedge 
 
	    lft2.next = 164
	    yield clock.posedge
	    sam2.next = 160
	    yield clock.posedge
	    rht2.next = 170
	    yield clock.posedge
	    flgs2.next = 7
	    yield clock.posedge
	    upd2.next = 1
	    yield clock.posedge
	    upd2.next = 0
            yield clock.posedge
 
            sam3.next = 505
            yield clock.posedge
            flgs3.next = 5
            yield clock.posedge
            upd3.next = 1
            yield clock.posedge
            upd3.next = 0
            yield clock.posedge 
 
            yield clock.posedge
	    lft3.next = 164
	    yield clock.posedge
	    sam3.next = 160
	    yield clock.posedge
	    rht3.next = 170
	    yield clock.posedge
	    flgs3.next = 7
	    yield clock.posedge
	    upd3.next = 1
	    yield clock.posedge
	    upd3.next = 0
            yield clock.posedge
 
            sam1.next = 505
            yield clock.posedge
            flgs3.next = 5
            yield clock.posedge
            upd3.next = 1
            yield clock.posedge
            upd3.next = 0
 
            
            
            raise StopSimulation	
	return instances()
'''
toVerilog(dwt_top,clock)

toVHDL(dwt_top,clock)
'''		
tb_fsm = traceSignals(tb, clock)
sim = Simulation(tb_fsm)
sim.run()	

