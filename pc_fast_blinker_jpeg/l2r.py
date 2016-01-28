from myhdl import *
W0 = 9
lift0 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
res0 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
lift1 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
res1 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
lift2 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
res2 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
lift3 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
res3 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
lift4 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
res4 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
lift5 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
res5 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
lift6 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
res6 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
lift7 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
res7 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))

def lift2res(lift0, res0, lift1, res1, lift2, res2, lift3, res3, lift4, res4, lift5, res5,lift6, res6,lift7, res7 ):
	
	@always_comb
	def rtl():
		res0.next = lift0[W0:]
		res1.next = lift1[W0:]
		res2.next = lift2[W0:]
		res3.next = lift3[W0:]
		res4.next = lift4[W0:]
		res5.next = lift5[W0:]
		res6.next = lift6[W0:]
		res7.next = lift7[W0:]		
	return rtl
def lift2res1(lift0, res0 ):
	
	@always_comb
	def rtl():
		res0.next = lift0[W0:]
	return rtl
