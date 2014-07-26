from myhdl import *
#25: is for ww[26,18]
 
#din_l = Signal(intbv(0)[25:])


class Add_mul_top(object):

	def __init__(self):
		ww = (20,16)
		self.even_odd = Signal(bool(0))
		self.fwd_inv = Signal(bool(0))
		self.p = Signal(bool(0))
		self.left = Signal(fixbv(0)[ww])
		self.right = Signal(fixbv(0)[ww])
		self.left1 = Signal(fixbv(0)[ww])
		self.right1 = Signal(fixbv(0)[ww])
		self.din_odd = Signal(fixbv(0)[ww])
		self.dout_odd = Signal(fixbv(0)[ww])
		self.we_odd = Signal(bool(0))
		self.addr_odd = Signal(intbv(0)[7:])

		self.din_even = Signal(fixbv(0)[ww])
		self.dout_even = Signal(fixbv(0)[ww])
		self.we_even = Signal(bool(0))
		self.addr_even = Signal(intbv(0)[7:])

		self.din_odd1 = Signal(fixbv(0)[ww])
		self.dout_odd1 = Signal(fixbv(0)[ww])
		self.we_odd1 = Signal(bool(0))
		self.addr_odd1 = Signal(intbv(0)[7:])

		self.din_even1 = Signal(fixbv(0)[ww])
		self.dout_even1 = Signal(fixbv(0)[ww])
		self.we_even1 = Signal(bool(1))
		self.addr_even1 = Signal(intbv(0)[7:])

	def setSig_we_odd(self,val):   
		self.we_odd.next = Signal(bool(val))
		
	def setSig_we_even(self,val):   
		self.we_even.next = Signal(bool(val))
	
 	def setSig_we_odd1(self,val):   
		self.we_odd1.next = Signal(bool(val))
	
 	def setSig_we_even1(self,val):   
		self.we_even1.next = Signal(bool(val))
	
 	def setSig_addr_odd(self,val):   
		self.addr_odd.next = Signal(intbv(val))

 	def setSig_addr_even(self,val):   
		self.addr_even.next = Signal(intbv(val))

	def setSig_addr_odd1(self,val):   
		self.addr_odd1.next = Signal(intbv(val))

	def setSig_addr_even1(self,val):   
		self.addr_even1.next = Signal(intbv(val))

	def setSig_din_odd(self,val):   
		ww = (20,16)
		self.din_odd.next = Signal(fixbv(val)[ww])		

	def setSig_din_odd1(self,val):   
		ww = (20,16)
		self.din_odd1.next = Signal(fixbv(val)[ww])

	def setSig_din_even1(self,val):
		ww = (20,16)
		self.din_even1.next = Signal(fixbv(val)[ww])
	def setSig_left(self,val):   
		ww = (20,16)
		self.left.next = Signal(fixbv(val)[ww])	
	def setSig_right(self,val):   
		ww = (20,16)
		self.right.next = Signal(fixbv(val)[ww])
	def setSig_left1(self,val):   
		ww = (20,16)
		self.left1.next = Signal(fixbv(val)[ww])	
	def setSig_right1(self,val):   
		ww = (20,16)
		self.right1.next = Signal(fixbv(val)[ww])
	def setSig_even_odd(self,val):   
		self.even_odd.next = Signal(bool(val))
	def setSig_fwd_inv(self,val):   
		self.fwd_inv.next = Signal(bool(val))	
	def setSig_p(self,val):   
		self.p.next = Signal(bool(val))									
def add_mul_ram(clk, pix):
	DATA_WIDTH = 524292
	ww = (20,16)
	ca1 = fixbv(-1.586134342, min = -DATA_WIDTH, max = DATA_WIDTH, res=1e-5)
	ra4 = fixbv(-0.4435068522, min = -DATA_WIDTH, max = DATA_WIDTH, res=1e-5)
	ca2 = fixbv(-0.05298011854, min = -DATA_WIDTH, max = DATA_WIDTH, res=1e-5)
	ra3 = fixbv(-0.8829110762, min = -DATA_WIDTH, max = DATA_WIDTH, res=1e-5)
	ca3 = fixbv(0.8829110762, min = -DATA_WIDTH, max = DATA_WIDTH, res=1e-5)		
	ra2 = fixbv(0.05298011854, min = -DATA_WIDTH, max = DATA_WIDTH, res=1e-5)
	ca4 = fixbv(0.4435068522, min = -DATA_WIDTH, max = DATA_WIDTH, res=1e-5)		
	ra1 = fixbv(1.586134342, min = -DATA_WIDTH, max = DATA_WIDTH, res=1e-5)		 
	#ca1 = fixbv(-1.586134342)[ww]
	#ca2 = fixbv(-0.05298011854)[ww]
	#ca3 = fixbv(0.8829110762)[ww]
	#ca4 = fixbv(0.4435068522)[ww]
	#ra1 = fixbv(1.586134342)[ww]
	#ra2 = fixbv(0.05298011854)[ww]
	#ra3 = fixbv(-0.8829110762)[ww]
	#ra4 = fixbv(-0.4435068522)[ww]
	
             
 

	@always(clk.posedge)
	def hdl():
		if not pix.p:
			"""
			p False 1st pass even_odd True fwd_inv True 4 inputs
			left & right are added and mul by ca2  
			left1 & right1 are added and mul by ca2
			results are stored in two ram_even & ram_even1 
			
			p False 1st pass even_odd False fwd_inv True 4 inputs
			left & right are added and mul by ca1  
			left1 & right1 are added and mul by ca1
			results are stored in two ram_odd & ram_odd1 
			
			p False 1st pass even_odd True fwd_inv False 4 inputs
			left & right are added and mul by ra4
			left1 & right1 are added and mul by ra4
			results are stored in two ram_even & ram_even1 
			
			p False 1st pass even_odd False fwd_inv False 4 inputs
			left & right are added and mul by ra3
			left1 & right1 are added and mul by ra3
			results are stored in two ram_odd & ram_odd1 
			"""
			if pix.even_odd: 
				if pix.fwd_inv:
					pix.din_even.next = (pix.left + pix.right)*ca1
					pix.din_even1.next = (pix.left1 + pix.right1)*ca1
				else:
					pix.din_even.next = (pix.left + pix.right)*ra4
					pix.din_even1.next = (pix.left1 + pix.right1)*ra4
 			else:
				if pix.fwd_inv:
					pix.din_odd.next = (pix.left + pix.right)*ca2
					pix.din_odd1.next = (pix.left1 + pix.right1)*ca2
				else:
					pix.din_odd.next = (pix.left + pix.right)*ra3
					pix.din_odd1.next = (pix.left1 + pix.right1)*ra3
		else:
			"""
			p True 1st pass even_odd True fwd_inv True 4 inputs
			left & right are added and mul by ca4 
			left1 & right1 are added and mul by ca4
			results are stored in two ram_even & ram_even1 
			
			p True 1st pass even_odd False fwd_inv True 4 inputs
			left & right are added and mul by ca3
			left1 & right1 are added and mul by ca3
			results are stored in two ram_odd & ram_odd1 
			
			p True 1st pass even_odd True fwd_inv False 4 inputs
			left & right are added and mul by ra2
			left1 & right1 are added and mul by ra2
			results are stored in two ram_even & ram_even1 
			
			p True 1st pass even_odd False fwd_inv False 4 inputs
			left & right are added and mul by ra1
			left1 & right1 are added and mul by ra1
			results are stored in two ram_odd & ram_odd1 
			"""			
 			if pix.even_odd:
				if pix.fwd_inv:
					pix.din_even.next = (pix.left + pix.right)*ca3
					pix.din_even1.next = (pix.left1 + pix.right1)*ca3
				else:
					pix.din_even.next = (pix.left + pix.right)*ra2
					pix.din_even1.next = (pix.left1 + pix.right1)*ra2
					
			else:
				if pix.fwd_inv:
					pix.din_odd.next = (pix.left + pix.right)*ca4
					pix.din_odd1.next = (pix.left1 + pix.right1)*ca4
				else:
					pix.din_odd.next = (pix.left + pix.right)*ra1
					pix.din_odd1.next = (pix.left1 + pix.right1)*ra1			
			
	return hdl
	
def ram_odd(pix, clk, depth = 256):
	"""  Ram model """
	ww = (20,16)
	mem_odd = [Signal(fixbv(0)[ww]) for i in range(256)]    
	@always(clk.posedge)
	def write_odd():
		if pix.we_odd:
			mem_odd[pix.addr_odd].next = pix.din_odd
                
	@always_comb
	def read_odd():
		pix.dout_odd.next = mem_odd[pix.addr_odd]

	return write_odd, read_odd

def ram_even(pix, clk, depth = 256):
	"""  Ram model """
	ww = (20,16)
	mem_even = [Signal(fixbv(0)[ww]) for i in range(256)]
	@always(clk.posedge)
	def write_even():
		if pix.we_even:
			mem_even[pix.addr_even].next = pix.din_even
                
	@always_comb
	def read_even():
		pix.dout_even.next = mem_even[pix.addr_even]

	return write_even, read_even


def ram_odd1(pix, clk, depth = 128):
	"""  Ram model """
	ww = (20,16)
	mem_odd1 = [Signal(fixbv(0)[ww]) for i in range(128)]
	@always(clk.posedge)
	def write_odd1():
		if pix.we_odd1:
			mem_odd1[pix.addr_odd1].next = pix.din_odd1
                
	@always_comb
	def read_odd1():
		pix.dout_odd1.next = mem_odd1[pix.addr_odd1]

	return write_odd1, read_odd1

def ram_even1(pix, clk, depth = 128):
	"""  Ram model """
	ww = (20,16)
	mem_even1 = [Signal(fixbv(0)[ww]) for i in range(128)]
    
	@always(clk.posedge)
	def write_even1():
		if pix.we_even1:
			mem_even1[pix.addr_even1].next = pix.din_even1
                
	@always_comb
	def read_even1():
		pix.dout_even1.next = mem_even1[pix.addr_even1]

	return write_even1, read_even1

def convert():
	ww = (20,16)
	clk = Signal(bool(0))
	pix = Add_mul_top()
	
	
	
 	
	toVerilog(add_mul_ram, clk, pix)
	
	toVerilog(ram_even1, pix, clk)
	toVerilog(ram_odd1, pix, clk)
	toVerilog(ram_odd, pix, clk)
	toVerilog(ram_even, pix, clk)

	 
def testbench():
	ww = (20,16)
 
 
	clk = Signal(bool(0))
	pix = Add_mul_top()


	d_insteven1 = ram_even1(pix, clk)
	d_instodd1 = ram_odd1(pix, clk)
	d_instodd = ram_odd(pix, clk)
	d_insteven = ram_even(pix, clk)

	d_inst3 = add_mul_ram(clk, pix)
	
	@always(delay(10))
	def clkgen():
		clk.next = not clk
	
	@instance
	def stimulus():
		for i in range(3):
			yield clk.posedge
			pix.setSig_p(0)
			pix.setSig_even_odd(0)
			pix.setSig_fwd_inv(1)
			
			pix.setSig_left(100)
			pix.setSig_right(110)
			pix.setSig_left1(104)
			pix.setSig_right1(114)
			
			pix.setSig_we_odd(1)
			pix.setSig_we_odd1(1)
			pix.setSig_addr_odd(1)
			pix.setSig_addr_odd1(3)
			
			
 		for n in (18, 8, 8, 4):
			for i in range(1):
				pix.setSig_even_odd(1)
				pix.setSig_fwd_inv(0)
				pix.setSig_addr_even(2)
				pix.setSig_addr_even1(4)
				pix.setSig_we_even(1)
				pix.setSig_we_even1(1)
 				yield clk.posedge
			for i in range(1):
				pix.setSig_addr_odd(5)
				pix.setSig_addr_odd1(7)
				pix.setSig_addr_even(6)
				pix.setSig_addr_even1(8)

				pix.setSig_p(1) 
				 
				pix.setSig_left(102)
				pix.setSig_right(112)
				pix.setSig_left1(255)
				pix.setSig_right1(255)
				yield clk.posedge
			for i in range(1):
				pix.setSig_addr_odd(9)
				pix.setSig_addr_odd1(11)
				pix.setSig_addr_even(10)
				pix.setSig_addr_even1(12)
				pix.setSig_even_odd(0)	 
				pix.setSig_left(104)
				pix.setSig_right(114)
				pix.setSig_left(108)
				pix.setSig_right(118)

				yield clk.posedge	
			for i in range(2):
				pix.setSig_addr_odd(13)
				pix.setSig_addr_odd1(15)
				pix.setSig_addr_even(14)
				pix.setSig_addr_even1(16)
				pix.setSig_even_odd(0)	 
				pix.setSig_left(106)
				pix.setSig_right(116)
				pix.setSig_left(100)
				pix.setSig_right(101)
				yield clk.posedge
			for i in range(n-1):
			 	yield clk.posedge
		raise StopSimulation
	return d_insteven1, d_instodd1, d_instodd, d_insteven, d_inst3, stimulus, clkgen
 
convert()

tb_fsm = traceSignals(testbench)
sim = Simulation(tb_fsm)
sim.run()
	
