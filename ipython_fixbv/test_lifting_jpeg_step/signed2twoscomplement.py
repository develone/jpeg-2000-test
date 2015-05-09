from myhdl import *
W0 = 9

x = Signal(intbv(0, min= -(2**(W0)) ,max= (2**(W0))))
z = Signal(intbv(0)[W0:])
clk = Signal(bool(0))
def signed2twoscomplement(clk, x, z):
	
	@always(clk.posedge)
	def unsigned_logic():
		z.next = x

	return unsigned_logic
def convert():
	toVHDL(signed2twoscomplement, clk, x, z)
	toVerilog(signed2twoscomplement, clk, x, z)

#convert()
