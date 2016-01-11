from myhdl import *

from jpeg import dwt
from signed2twoscomplement import signed2twoscomplement
from l2r import lift2res
W0 = 9

clock = Signal(bool(0))
upd = Signal(bool(0))
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
flgs0 = Signal(intbv(0)[3:])
lft0 = Signal(intbv(0)[W0:])
rht0 = Signal(intbv(0)[W0:])
sam0 = Signal(intbv(0)[W0:])
lift0 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
res0 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
res1 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
res2 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
res3 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
res4 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
res5 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
res6 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
res7 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))

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

instance_0 = dwt(clock, upd, flgs0, lft0, sam0, rht0, done0, lift0)
instance_1 = dwt(clock, upd, flgs1, lft1, sam1, rht1, done1, lift1)

instance_2 = dwt(clock, upd, flgs2, lft2, sam2, rht2, done2, lift2)
instance_3 = dwt(clock, upd, flgs3, lft3, sam3, rht3, done3, lift3)


		
def dwt_top(clock):
	instance_0 = dwt(flgs0, upd, lft0, sam0, rht0, lift0, done0, clock)
	instance_1 = dwt(flgs1, upd, lft1, sam1, rht1, lift1, done1, clock)
	instance_2 = dwt(flgs2, upd, lft2, sam2, rht2, lift2, done2, clock)
	instance_3 = dwt(flgs3, upd, lft3, sam3, rht3, lift3, done3, clock)
	instance_4 = dwt(flgs4, upd, lft4, sam4, rht4, lift4, done4, clock)
	instance_5 = dwt(flgs5, upd, lft5, sam5, rht5, lift5, done5, clock)
	instance_6 = dwt(flgs6, upd, lft6, sam6, rht6, lift6, done6, clock)
	instance_7 = dwt(flgs7, upd, lft7, sam7, rht7, lift7, done7, clock)
	
	instance_8 = lift2res(lift0,res0, lift1,res1, lift2,res2, lift3,res3, lift4,res4, lift5,res5,lift6,res6,lift7,res7)
 
	instance_16 = signed2twoscomplement(res0, z0)
	instance_17 = signed2twoscomplement(res1, z1)
	instance_18 = signed2twoscomplement(res2, z2)
	instance_19 = signed2twoscomplement(res3, z3)
	instance_20 = signed2twoscomplement(res4, z4)
	instance_21 = signed2twoscomplement(res5, z5)
	instance_22 = signed2twoscomplement(res6, z6)
	instance_23 = signed2twoscomplement(res7, z7)
	return instances()	

 
def tb(clock):
	@always(delay(10))
	def clkgen():
		clock.next = not clock
	instance_0 = dwt(flgs0, upd, lft0, sam0, rht0, lift0, done0, clock)
	instance_1 = dwt(flgs1, upd, lft1, sam1, rht1, lift1, done1, clock)
	instance_2 = dwt(flgs2, upd, lft2, sam2, rht2, lift2, done2, clock)
	instance_3 = dwt(flgs3, upd, lft3, sam3, rht3, lift3, done3, clock)
	instance_4 = dwt(flgs4, upd, lft4, sam4, rht4, lift4, done4, clock)
	instance_5 = dwt(flgs5, upd, lft5, sam5, rht5, lift5, done5, clock)
	instance_6 = dwt(flgs6, upd, lft6, sam6, rht6, lift6, done6, clock)
	instance_7 = dwt(flgs7, upd, lft7, sam7, rht7, lift7, done7, clock)
	instance_8 = lift2res(lift0,res0, lift1,res1, lift2,res2, lift3,res3, lift4,res4, lift5,res5,lift6,res6,lift7,res7)
 
	instance_16 = signed2twoscomplement(res0, z0)
	instance_17 = signed2twoscomplement(res1, z1)
	instance_18 = signed2twoscomplement(res2, z2)
	instance_19 = signed2twoscomplement(res3, z3)
	instance_20 = signed2twoscomplement(res4, z4)
	instance_21 = signed2twoscomplement(res5, z5)
	instance_22 = signed2twoscomplement(res6, z6)
	instance_23 = signed2twoscomplement(res7, z7)
	@instance
        def stimulus():
	    lft0.next = 164
	    yield clock.posedge
	    sam0.next = 160
	    yield clock.posedge
	    rht0.next = 170
	    yield clock.posedge
	    flgs0.next = 7
	    yield clock.posedge
	    upd.next = 1
	    yield clock.posedge
	    upd.next = 0
	    yield clock.posedge
 
            sam0.next = 505
            yield clock.posedge
            flgs0.next = 5
            yield clock.posedge
            upd.next = 1
            yield clock.posedge
            upd.next = 0
 
	    lft1.next = 164
	    yield clock.posedge
	    sam1.next = 160
	    yield clock.posedge
	    rht1.next = 170
	    yield clock.posedge
	    flgs1.next = 7
	    yield clock.posedge
	    upd.next = 1
	    yield clock.posedge
	    upd.next = 0
            yield clock.posedge
 
            sam1.next = 505
            yield clock.posedge
            flgs1.next = 5
            yield clock.posedge
            upd.next = 1
            yield clock.posedge
            upd.next = 0
            yield clock.posedge 
 
	    lft2.next = 164
	    yield clock.posedge
	    sam2.next = 160
	    yield clock.posedge
	    rht2.next = 170
	    yield clock.posedge
	    flgs2.next = 7
	    yield clock.posedge
	    upd.next = 1
	    yield clock.posedge
	    upd.next = 0
            yield clock.posedge
 
            sam3.next = 505
            yield clock.posedge
            flgs3.next = 5
            yield clock.posedge
            upd.next = 1
            yield clock.posedge
            upd.next = 0
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
	    upd.next = 1
	    yield clock.posedge
	    upd.next = 0
            yield clock.posedge
 
            sam1.next = 505
            yield clock.posedge
            flgs3.next = 5
            yield clock.posedge
            upd.next = 1
            yield clock.posedge
            upd.next = 0
 
            
            
            raise StopSimulation	
	return instances()
'''
toVerilog(dwt_top,clock)
toVHDL(dwt_top,clock)
		
tb_fsm = traceSignals(tb, clock)
sim = Simulation(tb_fsm)
sim.run()	
'''
