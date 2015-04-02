from myhdl import *
from jpeg_constants import *

x = Signal(intbv(0, min= -(2**(W0)) ,max= (2**(W0))))
z = Signal(intbv(0)[W0:])

def signed2twoscomplement(x, z):
	''' return '''
	@always_comb
	def unsigned_logic():
		z.next = x

	return unsigned_logic
def convert():
	toVHDL(signed2twoscomplement, x, z)
	toVerilog(signed2twoscomplement, x, z)

#convert()
