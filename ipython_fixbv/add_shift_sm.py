from myhdl import *

from jpeg_utils import Add_shift_top
APB3_DURATION = int(1e9 / 10e6)
SYSCLK_DURATION = int(1e9 / 20e6)
class OverrunError(Exception):
    pass

 
				
def jpeg_sm(resetn, pix):

	
	########## STATE MACHINE ######
	"""If state is TRANSFER_IN data is written to ram_sam, ram_left, and ram_right.
	If state is TRANSFER_OUT ram_even and ram_odd. 
	If state is Update_Sample on a given sam the addr_left will be set sam - 1 & addr_right will 
	be set sam + 1 updated will be set True
	if sam is even even_odd will be set True if sam is odd even_odd will be set False
	if sam = 255 or 256 state_t is set TRANSFER_OUT which is the end of samples"""
	@always_seq(pix.pclk.posedge, reset=resetn)
	def state_machine():
		if pix.state == pix.state_t.IDLE:
			pix.state.next = pix.state_t.UPDATE_SAMPLE
		elif pix.state == pix.state_t.UPDATE_SAMPLE:
			if pix.sam % 2 == 0:
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

	 	
 
	return state_machine
 
			

 
 
def convert():
	clk = Signal(bool(0))
	#pix = Add_shift_top(duration=APB3_DURATION)
	pix = Add_shift_top()
	#toVerilog(add_shift_ram, clk, pix)
 
	signals = (pix.presetn,
		)
		
	toVerilog(jpeg_sm, pix.presetn, pix )

def tb(pix):
	clk = Signal(bool(0))
	#pix = Add_shift_top()
	signals = (pix.presetn,
		pix.pclk,
		pix.state_t,
        pix.state,
		pix.even_odd,
		pix.addr_even,
		pix.addr_sam,
		pix.addr_left,
		pix.addr_right,
		pix.addr_odd,
		pix.updated,
		pix.transoutrdy,
		pix.sam)
	return jpeg_sm(pix.presetn, pix)
		
def testbench():
	clk = Signal(bool(0))
	pix = Add_shift_top()
	signals = (pix.presetn,
		pix.pclk,
		pix.state_t,
        pix.state,
		pix.even_odd,
		pix.addr_even,
		pix.addr_sam,
		pix.addr_left,
		pix.addr_right,
		pix.addr_odd,
		pix.updated,
		pix.transoutrdy,
		pix.sam)
 
	#d_inst3 = add_shift_ram(clk, pix)
	d_sm = jpeg_sm(pix.presetn, pix)
	@always(delay(10))
	def clkgen():
		clk.next = not clk
		
	@always(delay(10))	
	def clkgen1():
		pix.pclk.next = not pix.pclk	
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
				pix.setSig_state_update_sample()
				pix.state.next = pix.state_t.UPDATE_SAMPLE
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
	return   d_sm, stimulus, clkgen, clkgen1
#convert()	
#tb_fsm = traceSignals(testbench)
#sim = Simulation(tb_fsm)
#sim.run()
