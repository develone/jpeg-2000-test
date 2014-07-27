from myhdl import *

from jpeg_utils import Add_shift_top
APB3_DURATION = int(1e9 / 10e6)
class OverrunError(Exception):
    pass

 
				
def add_shift_ram(clk, pix):
	
	########## STATE MACHINE ######
	"""If state is TRANSFER_IN data is written to ram_sam, ram_left, and ram_right.
	If state is TRANSFER_OUT ram_even and ram_odd. 
	If state is Update_Sample on a given sam the addr_left will be set sam - 1 & addr_right will 
	be set sam + 1 updated will be set True
	if sam is even even_odd will be set True if sam is odd even_odd will be set False
	if sam = 255 or 256 state_t is set TRANSFER_OUT which is the end of samples"""
	#@always_seq(pix.pclk.posedge, pix.reset=resetn)
	def state_machine():
		if pix.state == pix.state_t.IDLE:
			pix.state.next = pix.state_t.UPDATE_SAMPLE
		elif pix.state == pix.state_t.UPDATE_SAMPLE:
			if sam % 2 == 0:
				pix.even_odd.next = 1
				pix.addr_even.next = pix.sam
			else:
				pix.even_odd.next = 0
				pix.addr_odd.next = pix.sam
				pix.addr_sam.next = pix.sam
				pix.addr_left.next = pix.sam -1
				pix.addr_right.next = pix.sam + 1
				pix.addr_even.next = pix.sam
				pix.addr_odd.next = pix.sam
				pix.updated.next = 1
				if pix.sam == 256 :
					pix.updated.next = 0
					pix.state.next = pix.state_t.TRANSFER_OUT
		elif pix.sam == 255:
			pix.updated.next = 0
			pix.state.next = pix.state_t.TRANSFER_OUT
		elif pix.state == pix.state_t.TRANSFER_OUT:
			pix.transoutrdy.next = 1
			pix.state.next = pix.state_t.IDLE
		elif pix.state == pix.state_t.TRANSFER_IN:
			pix.updated.next = 1
			pix.state.next = pix.state_t.UPDATE_SAMPLE
			pix.state.next = pix.state_t.IDLE

	 	
	"""  Ram model """
	DATA_WIDTH = 65536	
	mem_right = [Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH)) for i in range(256)] 
	mem_left = [Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH)) for i in range(256)]
	mem_sam = [Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH)) for i in range(256)]
	mem_odd = [Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH)) for i in range(256)]
	mem_even = [Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH)) for i in range(256)]
					
     
	@always(clk.posedge)
	def write_odd():
		if pix.we_odd:
			mem_odd[pix.addr_odd].next = pix.din_odd
                
	@always_comb
	def read_odd():
		pix.dout_odd.next = mem_odd[pix.addr_odd]
	
 	@always(clk.posedge)
	def write_even():
		if pix.we_even:
			mem_even[pix.addr_even].next = pix.din_even
                
	@always_comb
	def read_even():
		pix.dout_even.next = mem_even[pix.addr_even]


 	@always(clk.posedge)
	def write_sam():
		if pix.we_sam:
			mem_sam[pix.addr_sam].next = pix.din_sam
                
	@always_comb
	def read_sam():
		pix.dout_sam.next = mem_sam[pix.addr_sam]

 	@always(clk.posedge)
	def write_left():
		if pix.we_left:
			mem_left[pix.addr_left].next = pix.din_left
                
	@always_comb
	def read_left():
		pix.dout_left.next = mem_left[pix.addr_left]
	 
	@always(clk.posedge)
	def write_right():
		if pix.we_right:
			mem_right[pix.addr_right].next = pix.din_right
                
	@always_comb
	def read_right():
		pix.dout_right.next = mem_right[pix.addr_right]

	
	@always(clk.posedge)
	def hdl():
		
	
		if pix.updated == 1:
			
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
		else:
			pix.noupdate.next = 1
	return hdl, write_sam, read_sam, write_right, read_right, write_left, read_left, write_odd, read_odd
 
			

 
 
def convert():
	clk = Signal(bool(0))
	pix = Add_shift_top(duration=APB3_DURATION)
	toVerilog(add_shift_ram, clk, pix)
 
	signals = (pix.transoutrdy,
		pix.reset,
		pix.penable, 
		pix.psel,
		pix.pwrite,
		pix.full,
		pix.pclk,
		pix.sam,
		pix.updated,
		pix.state_t,
		pix.state,
		pix.noupdate)
	#toVerilog(set_state, *signals )
	
def testbench():
	clk = Signal(bool(0))
	pix = Add_shift_top()

 
	d_inst3 = add_shift_ram(clk, pix)
	
	@always(delay(10))
	def clkgen():
		clk.next = not clk
	
	@instance
	def stimulus():
		for i in range(3):
			yield clk.posedge
			pix.setSig_updated(1)
			pix.setSig_noupdate(0)
			pix.setSig_transoutrdy(0)
			pix.setSig_sam(1)
			
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
				pix.setSig_transoutrdy(1)
				yield clk.posedge			 	
			for i in range(n-1):
			 	yield clk.posedge
		raise StopSimulation
	return   d_inst3, stimulus, clkgen
convert()	
tb_fsm = traceSignals(testbench)
sim = Simulation(tb_fsm)
sim.run()
