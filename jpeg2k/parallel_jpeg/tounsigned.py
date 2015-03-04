from myhdl import *
from jpeg_constants import *
bits_in = Signal(intbv(0, min= -(2**(W0-1)) ,max= (2**(W0-1))))
v = Signal(intbv(0)[W0:])

def tounsigned(bits_in, v, w=9):
	''' return an unsigned value to represent a possibly 'signed' value'''
	@always_comb
	def unsigned_logic():
		if bits_in >= 0:
			v.next = bits_in
		else:
			v.next = 2**w + bits_in

	return unsigned_logic
toVHDL(tounsigned, bits_in, v, w=W0)
toVerilog(tounsigned, bits_in, v, w=W0)
