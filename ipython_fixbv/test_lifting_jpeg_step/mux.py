from myhdl import *
W0 = 9
we = Signal(bool(0))
we_in = Signal(bool(0))
addr = Signal(intbv(0)[8:])
addr_in = Signal(intbv(0)[8:])
we_1 = Signal(bool(0))
addr_1 = Signal(intbv(0)[8:])
din = Signal(intbv(0)[W0:])
data_in = Signal(intbv(0)[W0:])
z = Signal(intbv(0)[W0:])
muxsel_i = Signal(bool(0))

def mux_data(z, din, data_in, we_1, we, we_in, addr_1, addr, addr_in, muxsel_i):
	@always_comb
	def muxLogic():
		'''If  muxsel_i eq 0 ram  writing disabled to pc_read'''
		din.next = z
		we.next = we_1
		addr.next = addr_1
		 
		if (muxsel_i == 1):
			din.next = data_in
			we.next =  we_in
			addr.next = addr_in
	return muxLogic		
def convert():
	toVHDL(mux_data, z, din, data_in, we_1, we, we_in, addr_1, addr, addr_in, muxsel_i)
	toVerilog(mux_data, z, din, data_in, we_1, we, we_in, addr_1, addr, addr_in, muxsel_i)
#convert()	
