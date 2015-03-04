from myhdl import *
W0 = 10
bits_in = Signal(intbv(0, min= -(2**(W0-1)) ,max= (2**(W0-1))))
v = Signal(intbv(0)[W0:])
def tosigned(bits_in, v, w=10-1):
	''' return a signed representation of an 'unsigned' value '''
	@always_comb
	def tosigned_logic():
		if (bits_in >> (w-1) & 1):
			# high bit set -> negative
			v.next = -(~bits_in + 1)
		else:
			# positive
			v.next = bits_in
	return tosigned_logic
toVHDL(tosigned, bits_in, v, w=W0)
toVerilog(tosigned, bits_in, v, w=W0)
