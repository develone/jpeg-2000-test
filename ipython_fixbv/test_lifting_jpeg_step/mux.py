from myhdl import *
W0 = 9
din = Signal(intbv(0)[W0:])
data_in = Signal(intbv(0)[W0:])
z = Signal(intbv(0)[W0:])
muxsel_i = Signal(bool(0))

def mux_data(z, din, data_in, muxsel_i):
	@always_comb
	def muxLogic():
		din.next = z
		
		 
		if (muxsel_i == 1):
			din.next = data_in
			 
	return muxLogic		
def convert():
	toVHDL(mux_data, z, din, data_in, muxsel_i)
	toVerilog(mux_data, z, din, data_in, muxsel_i)
#convert()	
