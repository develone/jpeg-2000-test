from myhdl import *
m = [156.0, 156.0, 156.0, 156.0, 164.0, 164.0, 164.0, 164.0, 164.0, 164.0, 164.0, 164.0, 156.0, 156.0, 164.0, 164.0, 156.0, 156.0, 164.0, 164.0, 148.0, 148.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 164.0, 164.0, 164.0, 164.0, 164.0, 164.0, 172.0, 172.0, 172.0, 172.0, 172.0, 172.0, 172.0, 172.0, 172.0, 172.0, 164.0, 164.0, 148.0, 148.0, 156.0, 156.0, 124.0, 124.0, 116.0, 116.0, 92.0, 92.0, 92.0, 92.0, 84.0, 84.0, 108.0, 108.0, 108.0, 108.0, 100.0, 100.0, 100.0, 100.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 100.0, 100.0, 108.0, 108.0, 108.0, 108.0, 116.0, 116.0, 116.0, 116.0, 124.0, 124.0, 116.0, 116.0, 124.0, 124.0, 124.0, 124.0, 116.0, 116.0, 116.0, 116.0, 124.0, 124.0, 124.0, 124.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 124.0, 124.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 124.0, 124.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 132.0, 132.0, 140.0, 140.0, 124.0, 124.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 140.0, 140.0, 132.0, 132.0, 140.0, 140.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 140.0, 140.0, 132.0, 132.0, 132.0, 132.0, 140.0, 140.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 140.0, 140.0, 132.0, 132.0, 140.0, 140.0, 132.0, 132.0, 132.0, 132.0, 124.0, 124.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 140.0, 140.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 124.0, 124.0, 132.0, 132.0, 140.0, 140.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 124.0, 124.0, 132.0, 132.0, 140.0, 140.0, 132.0, 132.0, 132.0, 132.0, 124.0, 124.0, 132.0, 132.0, 124.0, 124.0, 140.0, 140.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 124.0, 124.0, 140.0, 140.0, 132.0, 132.0, 124.0, 124.0, 124.0, 124.0, 132.0, 132.0, 124.0, 124.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 124.0, 124.0, 132.0, 132.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 116.0, 116.0, 124.0, 124.0, 116.0, 116.0, 108.0, 108.0, 116.0, 116.0, 100.0, 100.0, 100.0, 100.0, 116.0, 116.0, 124.0, 124.0, 132.0, 132.0, 140.0, 140.0, 148.0, 148.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 164.0, 164.0, 164.0, 164.0, 156.0, 156.0, 148.0, 148.0, 156.0, 156.0, 156.0, 156.0, 148.0, 148.0, 148.0, 148.0, 156.0, 156.0, 156.0, 156.0, 148.0, 148.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 148.0, 148.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 164.0, 164.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 188.0, 188.0, 204.0, 204.0, 212.0, 212.0, 212.0, 212.0, 220.0, 220.0, 220.0, 220.0, 220.0, 220.0, 212.0, 212.0, 196.0, 196.0, 148.0, 148.0, 108.0, 108.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 116.0, 116.0, 124.0, 124.0, 116.0, 116.0, 116.0, 116.0, 132.0, 132.0, 124.0, 124.0, 116.0, 116.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 116.0, 116.0, 124.0, 124.0, 132.0, 132.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 116.0, 116.0, 132.0, 132.0, 132.0, 132.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 132.0, 132.0, 132.0, 132.0, 116.0, 116.0, 116.0, 116.0, 116.0, 116.0, 116.0, 116.0, 124.0, 124.0, 132.0, 132.0, 164.0, 164.0, 172.0, 172.0, 156.0, 156.0]
from jpeg_utils import Add_shift_top
APB3_DURATION = int(1e9 / 10e6)
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
		if resetn == 0:
			pix.updated.next = 0
			pix.even_odd.next = 0
			pix.addr_left.next = 0
			pix.addr_right.next = 0
			pix.addr_sam.next = 0
			pix.addr_res.next = 0
			pix.we_res.next = 0
			pix.we_sam.next = 0
			pix.we_left.next = 0
			pix.we_right.next = 0
			pix.transoutrdy.next = 0
			pix.transinrdy.next = 0
			pix.state.next = pix.state_t.UPDATE_SAMPLE
		else:
			#pix.state.next = pix.state_t.UPDATE_SAMPLE
			if pix.state == pix.state_t.IDLE:
				if pix.state == pix.state_t.UPDATE_SAMPLE:
					pix.state.next = pix.state_t.UPDATE_SAMPLE
				if pix.state == pix.state_t.TRANSFER_IN:
					pix.state.next = pix.state_t.TRANSFER_IN
				if pix.state == pix.state_t.TRANSFER_OUT:
					pix.state.next = pix.state_t.TRANSFER_OUT
			elif pix.state == pix.state_t.UPDATE_SAMPLE:
				pix.even_odd.next = 0
				pix.we_left.next = 0
				pix.we_right.next = 0
				pix.we_sam.next = 0
				pix.updated.next = 1
				pix.we_res.next = 1
				if pix.sam % 2 == 0:
					pix.even_odd.next = 1
					pix.addr_res.next = pix.sam
					pix.addr_sam.next = pix.sam
					if pix.sam != 0:
						pix.addr_left.next = pix.sam -1
					pix.addr_right.next = pix.sam + 1


				else:
					pix.even_odd.next = 0
					pix.addr_res.next = pix.sam
					pix.addr_sam.next = pix.sam
					pix.addr_left.next = pix.sam -1
					if pix.sam <= 253:

						pix.addr_right.next = pix.sam + 1
					pix.addr_res.next = pix.sam

					if pix.sam == 255 :
						pix.even_odd.next = 0
						pix.we_res.next = 0
						pix.updated.next = 0
						pix.state.next = pix.state_t.TRANSFER_OUT
					elif pix.sam == 254:
						pix.even_odd.next = 0
						pix.updated.next = 0
						pix.state.next = pix.state_t.TRANSFER_OUT
			elif pix.state == pix.state_t.TRANSFER_OUT:
				pix.we_res.next = 0
				pix.updated.next = 0

				if pix.addr_sam == 255:
					pix.transoutrdy.next = 1
					pix.state.next = pix.state_t.IDLE
				else:
					pix.addr_sam.next =  1 + pix.addr_sam
			elif pix.state == pix.state_t.TRANSFER_IN:
				pix.we_sam.next = 1
				pix.we_left.next = 1
				pix.we_right.next = 1


				pix.we_res.next = 0
				pix.updated.next = 0
				pix.transinrdy.next = 0
				if pix.addr_sam == 255:
					pix.we_sam.next = 0
					pix.we_left.next = 0
					pix.we_right.next = 0

					pix.transinrdy.next = 1
					pix.state.next = pix.state_t.IDLE
				else:
					pix.addr_sam.next = pix.sam
					pix.addr_left.next = pix.sam
					pix.addr_right.next = pix.sam


	return state_machine

def add_shift_ram(clk, pix):

	"""  Ram model """
	DATA_WIDTH = 65536
	mem_right = [Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH)) for i in range(256)]
	mem_left = [Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH)) for i in range(256)]
	mem_sam = [Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH)) for i in range(256)]
	mem_res = [Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH)) for i in range(256)]



	@always(clk.posedge)
	def write_res():
		if pix.we_res:
			mem_res[pix.addr_res].next = pix.din_res

	@always_comb
	def read_res():
		pix.dout_res.next = mem_res[pix.addr_res]

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
					pix.din_res.next = pix.dout_sam - ((pix.dout_left >> 1) + (pix.dout_right >> 1))
				else:
					pix.din_res.next = pix.dout_sam + ((pix.dout_left >> 1) + (pix.dout_right >> 1))
			else:
				if pix.fwd_inv:
					pix.din_res.next = pix.dout_sam + (pix.dout_left + pix.dout_right + 2)>>2
				else:
					pix.din_res.next = pix.dout_sam - (pix.dout_left + pix.dout_right + 2)>>2
		else:
			pix.noupdate.next = 1
	return hdl, write_sam, read_sam, write_right, read_right, write_left, read_left, write_res, read_res





def convert():
	clk = Signal(bool(0))
	#pix = Add_shift_top(duration=APB3_DURATION)
	pix = Add_shift_top()
	toVerilog(add_shift_ram, clk, pix)
 	toVerilog(jpeg_sm, pix.presetn, pix )

def testbench():
	clk = Signal(bool(0))
	pix = Add_shift_top()


	d_inst3 = add_shift_ram(clk, pix)
	d_sm = jpeg_sm(pix.presetn, pix)

	@always(delay(10))
	def clkgen():
		clk.next = not clk

	@always(delay(10))
	def clkgen1():
		pix.pclk.next = not pix.pclk

	@instance
	def stimulus():
		for i in range(1):
			pix.setSig_presetn(0)
			print("%8d  %s" % (now(), pix))
			yield clk.posedge
		for i in range(1):

			yield clk.posedge
		for i in range(1):


			yield clk.posedge
		for i in range(1):
			yield clk.posedge
		for i in range(1):
			pix.setSig_presetn(1)



			#setting samples 1 2 3





			yield clk.posedge

		for i in range(1):
			pix.setSig_sam(0)
			yield clk.posedge
		for i  in range(2):

			pix.setSig_state_transfer_in()
			print("%8d  %s" % (now(), pix))
			yield clk.posedge

		for i  in range(255):
			#print m[i]
			pix.setSig_din_left(int(m[i]))
			pix.setSig_din_right(int(m[i]))
			pix.setSig_din_sam(int(m[i]))
			pix.setSig_sam(i)

			yield clk.posedge
		for i  in range(1):
			pix.setSig_fwd_inv(1)
			yield clk.posedge
		for i  in range(1):
			pix.setSig_state_update_sample()
			yield clk.posedge

		for i  in range(1):
			pix.setSig_sam(2)
			yield clk.posedge
		for i  in range(1):
			pix.setSig_state_update_sample()
			yield clk.posedge
		for i  in range(2,255,2):
			pix.setSig_sam(i)
			yield clk.posedge
		for i  in range(1,255-1,2):
			pix.setSig_sam(i)
			yield clk.posedge
		for i  in range(1):
			pix.setSig_fwd_inv(0)
		for i  in range(255):
			pix.setSig_addr_sam(0)
			pix.setSig_state_transfer_out()
			print("%8d  %s" % (now(), pix))
			yield clk.posedge
		raise StopSimulation
	return   d_inst3, d_sm, stimulus, clkgen, clkgen1
#convert()
tb_fsm = traceSignals(testbench)
sim = Simulation(tb_fsm)
sim.run()
