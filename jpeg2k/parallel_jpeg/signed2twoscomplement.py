from myhdl import *
from jpeg_constants import *
#W0 = 9
bits_in_sig = Signal(intbv(0, min= -(2**(W0)) ,max= (2**(W0))))
vv = Signal(intbv(0)[W0:])

def signed2twoscomplement(bits_in_sig, vv):
	''' return '''
	@always_comb
	def unsigned_logic():
		vv.next = bits_in_sig

	return unsigned_logic
def convert():
	toVHDL(signed2twoscomplement, bits_in_sig, vv)
	toVerilog(signed2twoscomplement, bits_in_sig, vv)

#convert()
