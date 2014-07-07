from myhdl import *
#25: is for ww[26,18]
 
#din_l = Signal(intbv(0)[25:])


class Add_mul_top(object):

	def __init__(self):
		ww = (26,18)
		self.din_odd = Signal(fixbv(0)[ww])
		self.dout_odd = Signal(fixbv(0)[ww])
		self.we_odd = Signal(bool(0))
		self.addr_odd = Signal(intbv(0)[7:])

		self.din_l = Signal(fixbv(0)[ww])
		self.dout_l = Signal(fixbv(0)[ww])
		self.we_l = Signal(bool(0))
		self.addr_l = Signal(intbv(0)[7:])

		self.din_r = Signal(fixbv(0)[ww])
		self.dout_r = Signal(fixbv(0)[ww])
		self.we_r = Signal(bool(0))
		self.addr_r = Signal(intbv(0)[7:])

	def setSig_we_odd(self,val):   
		self.we_odd.next = Signal(bool(val))
	
 	def setSig_we_l(self,val):   
		self.we_l.next = Signal(bool(val))
	
 	def setSig_we_r(self,val):   
		self.we_r.next = Signal(bool(val))
	
 	def setSig_addr_odd(self,val):   
		self.addr_odd.next = Signal(intbv(val))

	def setSig_addr_l(self,val):   
		self.addr_l.next = Signal(intbv(val))

	def setSig_addr_r(self,val):   
		self.addr_r.next = Signal(intbv(val))

	def setSig_din_l(self,val):   
		ww = (26,18)
		self.din_l.next = Signal(fixbv(val)[ww])

	def setSig_din_r(self,val):
		ww = (26,18)
		self.din_r.next = Signal(fixbv(val))
		
def mult_mul_add(clk, pix):
	ww = (26,18)
 
	ca1 = fixbv(-1.586134342)[ww]
	ca2 = fixbv(-0.05298011854)[ww]
	ca3 = fixbv(0.8829110762)[ww]
	ca4 = fixbv(0.4435068522)[ww]
	ra1 = fixbv(1.586134342)[ww]
	ra2 = fixbv(0.05298011854)[ww]
	ra3 = fixbv(-0.8829110762)[ww]
	ra4 = fixbv(-0.4435068522)[ww]
	
             
 


	@always(clk.posedge)
	def hdl():
		pix.dout_odd.next = (pix.dout_l + pix.dout_r)*ca1
	 
	return hdl
	
def ram_odd(pix, clk, depth = 128):
	"""  Ram model """
	ww = (26,18)
	mem_odd = [Signal(fixbv(0)[ww]) for i in range(128)]    
	@always(clk.posedge)
	def write_odd():
		if pix.we_odd:
			mem_odd[pix.addr_odd].next = pix.din_odd
                
	@always_comb
	def read_odd():
		pix.dout_odd.next = mem_odd[pix.addr_odd]

	return write_odd, read_odd


def ram_l(pix, clk, depth = 128):
	"""  Ram model """
	ww = (26,18)
	mem_l = [Signal(fixbv(0)[ww]) for i in range(128)]
	@always(clk.posedge)
	def write_l():
		if pix.we_l:
			mem_l[pix.addr_l].next = pix.din_l
                
	@always_comb
	def read_l():
		pix.dout_l.next = mem_l[pix.addr_l]

	return write_l, read_l

def ram_r(pix, clk, depth = 128):
	"""  Ram model """
	ww = (26,18)
	mem_r = [Signal(fixbv(0)[ww]) for i in range(128)]
    
	@always(clk.posedge)
	def write_r():
		if pix.we_r:
			mem_r[pix.addr_r].next = pix.din_r
                
	@always_comb
	def read_r():
		pix.dout_r.next = mem_r[pix.addr_r]

	return write_r, read_r

def convert():
	ww = (26,18)
	clk = Signal(bool(0))
	pix = Add_mul_top()
	
	
	
 	
	toVerilog(mult_mul_add, clk, pix)
	
	toVerilog(ram_r, pix, clk)
	toVerilog(ram_l, pix, clk)
	toVerilog(ram_odd, pix, clk)


	 
def testbench():
	ww = (26,0)
 
 
	clk = Signal(bool(0))
	pix = Add_mul_top()
	pix.setSig_addr_l(0)
	pix.setSig_addr_r(2)
	pix.setSig_addr_odd(1)
	pix.setSig_we_l(1)
	pix.setSig_we_r(1)
	pix.setSig_we_odd(1)

	pix.setSig_din_l(100)

	pix.setSig_din_r(110)

	d_inst = ram_r(pix, clk)
	d_inst1 = ram_l(pix, clk)
	d_inst2 = ram_odd(pix, clk)
	d_inst3 = mult_mul_add(clk, pix)
	
	@always(delay(10))
	def clkgen():
		clk.next = not clk
	
	@instance
	def stimulus():
		for i in range(3):
			yield clk.posedge
		for n in (18, 8, 8, 4):
			for i in range(2):
				yield clk.posedge
			for i in range(n-1):
				yield clk.posedge 
		raise StopSimulation
	return d_inst, d_inst1, d_inst2, d_inst3, stimulus, clkgen
 
convert()

tb_fsm = traceSignals(testbench)
sim = Simulation(tb_fsm)
sim.run()
	
