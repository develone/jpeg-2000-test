from myhdl import *

 


class Add_shift_top(object):
	
	def __init__(self):
		DATA_WIDTH = 65536
		self.even_odd = Signal(bool(0))
		self.fwd_inv = Signal(bool(0))
		 
		self.din_sam = Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))
		self.dout_sam = Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))
		self.din_left = Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))
		self.dout_left = Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))
		self.din_right = Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))
		self.dout_right = Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))
		self.din_odd = Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))
		self.dout_odd = Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))
		self.din_even = Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))
		self.dout_even = Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))

		self.we_odd = Signal(bool(0))
		self.addr_odd = Signal(intbv(0)[8:])

		self.we_sam = Signal(bool(0))
		self.addr_sam = Signal(intbv(0)[8:])

		self.we_even = Signal(bool(0))
		self.addr_even = Signal(intbv(0)[8:])

 		self.we_left = Signal(bool(0))
		self.addr_left = Signal(intbv(0)[8:])

		self.we_right = Signal(bool(0))
		self.addr_right = Signal(intbv(0)[8:])
 
	def setSig_we_odd(self,val):   
		self.we_odd.next = (bool(val))
		
	def setSig_we_even(self,val):   
		self.we_even.next = (bool(val))
	
	def setSig_we_left(self,val):   
		self.we_left.next = (bool(val))
		
	def setSig_we_sam(self,val):   
		self.we_sam.next = (bool(val))  
 
	def setSig_we_right(self,val):   
		self.we_right.next = (bool(val))  
	
 	def setSig_addr_sam(self,val):   
		self.addr_sam.next = Signal(intbv(val))

 	def setSig_addr_left(self,val):   
		self.addr_left.next = Signal(intbv(val))

 	def setSig_addr_right(self,val):   
		self.addr_right.next = Signal(intbv(val))

	def  setSig_addr_even(self,val):   
		self.addr_even.next = Signal(intbv(val))

	def  setSig_addr_odd(self,val):   
		self.addr_odd.next = Signal(intbv(val))
 

	def setSig_din_odd(self,val):   
		DATA_WIDTH = 65536
		self.din_odd.next = Signal(intbv(val, min = -DATA_WIDTH, max = DATA_WIDTH))
			
	def setSig_din_sam(self,val):   
		DATA_WIDTH = 65536
		self.din_sam.next = Signal(intbv(val, min = -DATA_WIDTH, max = DATA_WIDTH))

	def setSig_din_left(self,val):   
		DATA_WIDTH = 65536
		self.din_left.next = Signal(intbv(val, min = -DATA_WIDTH, max = DATA_WIDTH))

	def setSig_din_right(self,val):   
		DATA_WIDTH = 65536
		self.din_right.next = Signal(intbv(val, min = -DATA_WIDTH, max = DATA_WIDTH))				 									

	def setSig_even_odd(self,val):   
		self.even_odd.next = (bool(val))

	def setSig_fwd_inv(self,val):   
		self.fwd_inv.next = (bool(val))	

def add_shift_ram(clk, pix):
 
	
             
 
	 
	
	@always(clk.posedge)
	def hdl():
		if pix.even_odd: 
			if pix.fwd_inv:
				pix.din_even.next = pix.dout_sam - ((pix.dout_left >> 1) + (pix.dout_right >> 1))
			else:
				pix.din_even.next = pix.dout_sam + ((pix.dout_left >> 1) + (pix.dout_right >> 1))
		else:
			if pix.fwd_inv:
				pix.din_odd.next = pix.dout_sam + (pix.dout_left + pix.dout_right + 2)>>2
			else:
				pix.din_odd.next = pix.dout_sam - (pix.dout_left + pix.dout_right + 2)>>2
	return hdl
	
def ram_odd(pix, clk, depth = 256):
	"""  Ram model """
	DATA_WIDTH = 65536	
	mem_odd = [Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH)) for i in range(256)]    
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
	DATA_WIDTH = 65536 
	mem_even = [Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH)) for i in range(256)]
	@always(clk.posedge)
	def write_even():
		if pix.we_even:
			mem_even[pix.addr_even].next = pix.din_even
                
	@always_comb
	def read_even():
		pix.dout_even.next = mem_even[pix.addr_even]

	return write_even, read_even
def ram_left(pix, clk, depth = 256):
	"""  Ram model """
	DATA_WIDTH = 65536 
	mem_left = [Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH)) for i in range(256)]
	@always(clk.posedge)
	def write_left():
		if pix.we_left:
			mem_left[pix.addr_left].next = pix.din_left
                
	@always_comb
	def read_left():
		pix.dout_left.next = mem_left[pix.addr_left]

	return write_left, read_left	
def ram_right(pix, clk, depth = 256):
	"""  Ram model """
	DATA_WIDTH = 65536 
	mem_right = [Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH)) for i in range(256)]
	@always(clk.posedge)
	def write_right():
		if pix.we_right:
			mem_right[pix.addr_right].next = pix.din_right
                
	@always_comb
	def read_right():
		pix.dout_right.next = mem_right[pix.addr_right]

	return write_right, read_right
def ram_sam(pix, clk, depth = 256):
	"""  Ram model """
	DATA_WIDTH = 65536 
	mem_sam = [Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH)) for i in range(256)]
	@always(clk.posedge)
	def write_sam():
		if pix.we_sam:
			mem_sam[pix.addr_sam].next = pix.din_sam
                
	@always_comb
	def read_sam():
		pix.dout_sam.next = mem_sam[pix.addr_sam]

	return write_sam, read_sam
def convert():
	clk = Signal(bool(0))
	pix = Add_shift_top()
	toVerilog(add_shift_ram, clk, pix)
	toVerilog(ram_odd, pix, clk)
	toVerilog(ram_even, pix, clk)
	toVerilog(ram_left, pix, clk)
	toVerilog(ram_right, pix, clk)
	toVerilog(ram_sam, pix, clk)

def testbench():
	clk = Signal(bool(0))
	pix = Add_shift_top()

 	d_instodd = ram_odd(pix, clk)
	d_insteven = ram_even(pix, clk)
 	d_instright = ram_right(pix, clk)
	d_instleft = ram_left(pix, clk)
	d_instsam = ram_sam(pix,clk)
	d_inst3 = add_shift_ram(clk, pix)
	
	@always(delay(10))
	def clkgen():
		clk.next = not clk
	
	@instance
	def stimulus():
		for i in range(3):
			yield clk.posedge
			pix.setSig_we_sam(1)
			pix.setSig_addr_sam(0) 
			pix.setSig_din_sam(100)
			pix.setSig_we_left(1)
			pix.setSig_addr_left(0) 
			pix.setSig_din_left(102)
			pix.setSig_we_right(1)
			pix.setSig_addr_right(0) 
			pix.setSig_din_right(104)
			pix.setSig_even_odd(1)
			pix.setSig_fwd_inv(1)
			
			pix.setSig_we_even(1)
			pix.setSig_addr_even(0)
			 
 		for n in (18, 8, 8, 4):
			for i in range(1):
				pix.we_sam = (1)
				pix.setSig_addr_sam(0) 
				pix.setSig_din_sam(-3) 
				pix.setSig_fwd_inv(0)
				pix.setSig_we_even(1)
				pix.setSig_addr_even(1) 
			 	yield clk.posedge
			for i in range(1):
			 	pix.setSig_addr_even(0)
				pix.setSig_we_odd(1)
				pix.setSig_addr_odd(0)
				yield clk.posedge
			for i in range(1):
				pix.setSig_even_odd(0)
				pix.setSig_fwd_inv(0)  
				yield clk.posedge	
			for i in range(1):
		
				pix.setSig_din_sam(-53) 
			 	yield clk.posedge
			for i in range(1):
				pix.setSig_fwd_inv(1)
			 	 
			 
			 	yield clk.posedge
			for i in range(1):
				 
 			 	yield clk.posedge	
			for i in range(1):
				 
				yield clk.posedge			 	
			for i in range(n-1):
			 	yield clk.posedge
		raise StopSimulation
	return  d_instleft, d_instright, d_instsam, d_instodd, d_insteven, d_inst3, stimulus, clkgen
convert()	
tb_fsm = traceSignals(testbench)
sim = Simulation(tb_fsm)
sim.run()
