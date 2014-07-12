from myhdl import *

 


class Add_shift_top(object):
	
	def __init__(self):
		 
		self.even_odd = Signal(bool(0))
		self.fwd_inv = Signal(bool(0))
		self.p = Signal(bool(0))
		self.left = Signal(intbv(0)[9:])
		self.right = Signal(intbv(0)[9:])
	 
		self.din_odd = Signal(intbv(0, min = -255, max = 255))
		self.dout_odd = Signal(intbv(0, min = -255, max = 255))
		self.we_odd = Signal(bool(0))
		self.addr_odd = Signal(intbv(0)[7:])

		self.din_even = Signal(intbv(0, min = -255, max = 255))
		self.dout_even = Signal(intbv(0, min = -255, max = 255))
		self.we_even = Signal(bool(0))
		self.addr_even = Signal(intbv(0)[7:])

 
	def setSig_we_odd(self,val):   
		self.we_odd.next = (bool(val))
		
	def setSig_we_even(self,val):   
		self.we_even.next = (bool(val))
	
  
 
	
 	def setSig_addr_odd(self,val):   
		self.addr_odd.next = (intbv(val))

 	def setSig_addr_even(self,val):   
		self.addr_even.next = (intbv(val))

 

	def setSig_din_odd(self,val):   
		
		self.din_odd.next = (intbv(val)[9:])		

 
	def setSig_left(self,val):   
		
		self.left.next = (intbv(val)[9:])	
	def setSig_right(self,val):   
		
		self.right.next = (intbv(val)[9:])
 
	def setSig_even_odd(self,val):   
		self.even_odd.next = (bool(val))
	def setSig_fwd_inv(self,val):   
		self.fwd_inv.next = (bool(val))	
	def setSig_p(self,val):   
		self.p.next = (bool(val))									
def add_shift_ram(clk, pix):
 
	
             
 
	 
	
	@always(clk.posedge)
	def hdl():
		if not pix.p:
 
			if pix.even_odd: 
				if pix.fwd_inv:
					pix.din_even.next = pix.right - ((pix.left >> 1) + (pix.right >> 1))
				else:
					pix.din_odd.next = (pix.left + pix.right + 2)>>2
				 
			else:
				if pix.fwd_inv:
					pix.din_odd.next = (pix.left + pix.right + 2)>>2
				 
				else:
					pix.din_even.next = pix.right - ((pix.left >> 1) + (pix.right >> 1))
				 
		else:
 
			if pix.even_odd:
				if pix.fwd_inv:
					pix.din_even.next = pix.right - ((pix.left >> 1) + (pix.right >> 1))
				 
				else:
					pix.din_odd.next = (pix.left + pix.right + 2)>>2
				 
					
			else:
				if pix.fwd_inv:
					pix.din_odd.next = (pix.left + pix.right + 2)>>2
				 
				else:
					pix.din_even.next = pix.right - ((pix.left >> 1) + (pix.right >> 1))	 		
			
	
	return hdl
	
def ram_odd(pix, clk, depth = 128):
	"""  Ram model """
	 
	mem_odd = [Signal(intbv(0, min = -255, max = 255)) for i in range(128)]    
	@always(clk.posedge)
	def write_odd():
		if pix.we_odd:
			mem_odd[pix.addr_odd].next = pix.din_odd
                
	@always_comb
	def read_odd():
		pix.dout_odd.next = mem_odd[pix.addr_odd]

	return write_odd, read_odd

def ram_even(pix, clk, depth = 128):
	"""  Ram model """
	 
	mem_even = [Signal(intbv(0, min = -255, max = 255)) for i in range(128)]
	@always(clk.posedge)
	def write_even():
		if pix.we_even:
			mem_even[pix.addr_even].next = pix.din_even
                
	@always_comb
	def read_even():
		pix.dout_even.next = mem_even[pix.addr_even]

	return write_even, read_even
def convert():
	clk = Signal(bool(0))
	pix = Add_shift_top()
	toVerilog(add_shift_ram, clk, pix)
	toVerilog(ram_odd, pix, clk)
	toVerilog(ram_even, pix, clk)
	

def testbench():

 
 
	clk = Signal(bool(0))
	pix = Add_shift_top()


 	d_instodd = ram_odd(pix, clk)
	d_insteven = ram_even(pix, clk)

	d_inst3 = add_shift_ram(clk, pix)
	
	@always(delay(10))
	def clkgen():
		clk.next = not clk
	
	@instance
	def stimulus():
		for i in range(3):
			yield clk.posedge
			pix.setSig_p(0)
			pix.setSig_even_odd(1)
			pix.setSig_fwd_inv(1)
			pix.setSig_left(100)
			pix.setSig_right(110)
			pix.setSig_we_even(1)
			pix.setSig_addr_even(0)
			 

 		for n in (18, 8, 8, 4):
			for i in range(1):
				pix.setSig_left(202)
				pix.setSig_right(182)
				 
			 	yield clk.posedge
			for i in range(1):
			 	pix.setSig_addr_even(1)
				pix.setSig_left(200)
				pix.setSig_right(174)
 
				yield clk.posedge
			for i in range(1):
				pix.setSig_addr_even(2)
				pix.setSig_left(204)
				pix.setSig_right(194)
			 
				yield clk.posedge	
			for i in range(1):
		
			 	pix.setSig_addr_even(3)	 
				pix.setSig_left(106)
				pix.setSig_right(126)
			 	yield clk.posedge
			for i in range(1):
		
			 	pix.setSig_addr_even(4)	 
				pix.setSig_left(136)
				pix.setSig_right(106)
			 	yield clk.posedge
			for i in range(1):
				pix.setSig_addr_even(5)	 
 			 	yield clk.posedge	
			for i in range(1):
				pix.setSig_left(100)
				pix.setSig_right(96)
				pix.setSig_even_odd(0)
				pix.setSig_we_even(0)
				pix.setSig_we_odd(1)
				pix.setSig_addr_odd(0)
				yield clk.posedge			 	
			for i in range(n-1):
			 	yield clk.posedge
		raise StopSimulation
	return  d_instodd, d_insteven, d_inst3, stimulus, clkgen
convert()	
tb_fsm = traceSignals(testbench)
sim = Simulation(tb_fsm)
sim.run()
