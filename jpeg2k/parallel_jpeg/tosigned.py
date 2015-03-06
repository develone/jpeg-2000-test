from myhdl import *
from jpeg_constants import *

bits_in2unsigned = Signal(intbv(0)[W0:])
vv = Signal(intbv(0, min= -(2**(W0-1)) ,max= (2**(W0-1))))
def tosigned(bits_in2unsigned, vv, w=10):
	''' return a signed representation of an 'unsigned' value '''
	@always_comb
	def tosigned_logic():
		if ((bits_in2unsigned >> (w-1)) & 1):
			# high bit set -> negative
			vv.next = (~bits_in2unsigned + 1)
		else:
			# positive
			vv.next = bits_in2unsigned
	return tosigned_logic
toVHDL(tosigned, bits_in2unsigned, vv, w=W0-1)
toVerilog(tosigned, bits_in2unsigned, vv, w=W0-1)
