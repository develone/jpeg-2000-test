from myhdl import *
from rom import *

CONTENT = [
668288, 672388, 668288]

W0 = 10
LVL0 = 16
W1 = W0
LVL1 = 16
W2 = 10
LVL2 = 16
W3 = 5
LVL3 = 16
SIMUL = 1
from array_jpeg import jp_process
clk_fast = Signal(bool(0))
res_out_x = Signal(intbv(0, min= -2048 ,max= 2048))
update_s = Signal(bool(0))
noupdate_s = Signal(bool(0))

left_s_i = Signal(intbv(0)[LVL2*W2:])
sam_s_i = Signal(intbv(0)[LVL2*W2:])
right_s_i = Signal(intbv(0)[LVL2*W2:])
flgs_s_i = Signal(intbv(0)[LVL3*W3:])
from merge_sam import merge
left_com_x = Signal(intbv(0)[LVL2*W2:])
sam_com_x = Signal(intbv(0)[LVL2*W2:])
right_com_x = Signal(intbv(0)[LVL2*W2:])
lft_s_i = Signal(intbv(0)[LVL2*W2:])
sa_s_i = Signal(intbv(0)[LVL2*W2:])
rht_s_i = Signal(intbv(0)[LVL2*W2:])
merge_rdy_s = Signal(bool(0))
nomerge_s = Signal(bool(0))


def tb(clk_fast, res_out_x, left_s_i,sam_s_i, right_s_i, flgs_s_i,
noupdate_s, update_s, left_com_x, sam_com_x, right_com_x,
lft_s_i, sa_s_i, rht_s_i,
merge_rdy_s, nomerge_s,
W0=W0, LVL0=LVL0, W1=W1, LVL1=LVL1, W2=W2,
LVL2=LVL2, W3=W3, LVL3=LVL3):

	instance_rom_flgs = rom_flgs(dout_flgs, addr_flgs, ROM_CONTENT)
	instance_merge = merge( left_com_x, sam_com_x, right_com_x,
lft_s_i, sa_s_i, rht_s_i, merge_rdy_s, nomerge_s,
W0=W0, LVL0=LVL0, W1=W1, LVL1=LVL1, W2=W2,
LVL2=LVL2, W3=W3, LVL3=LVL3)
	instance_dut = jp_process( res_out_x, left_s_i,sam_s_i, right_s_i,
flgs_s_i, noupdate_s, update_s,  W0=W0, LVL0=LVL0, W1=W1, LVL1=LVL1,
W2=W2, LVL2=LVL2, W3=W3, LVL3=LVL3, SIMUL=SIMUL)
	@always(delay(10))
	def clkgen():
		clk_fast.next = not clk_fast

	@instance
	def stimulus():
		for i in range(10):
			print("%3d  ") % (now())

			yield clk_fast.posedge
		for i in range(2):

			lft_s_i.next = (157<< 150) + (160 << 140)+(163<<130) + (156 << 120) + (157<<110) + (160 << 100)+(163<<90)+(156 << 80) +(160 << 70) + (163<<60)+(156 << 50) + (157<<40) + (160 << 30)+(163<<20)+(156 << 10) + 157
			sa_s_i.next = (157<< 150) + (160 << 140)+(163<<130) + (156 << 120) + (157<<110) + (160 << 100)+(163<<90)+(156 << 80) +(160 << 70) + (163<<60)+(156 << 50) + (157<<40) + (160 << 30)+(163<<20)+(156 << 10) + 157
			rht_s_i.next = (157<< 150) + (160 << 140)+(163<<130) + (156 << 120) + (157<<110) + (160 << 100)+(163<<90)+(156 << 80) +( 160 << 70) + (163<<60)+(156 << 50) + (157<<40) + (160 << 30)+(163<<20)+(156 << 10) + 157

 			yield clk_fast.posedge
			merge_rdy_s.next = 1
			yield clk_fast.posedge

 		for i in range(2):

			left_s_i.next = left_com_x
			sam_s_i.next = sam_com_x
			right_s_i.next = right_com_x
 			yield clk_fast.posedge
		addr_flgs.next = 0
		for i in range(26):
			flgs_s_i.next = dout_flgs
			yield clk_fast.posedge
			addr_flgs.next = addr_flgs + 1
			yield clk_fast.posedge
			update_s.next = 1
			yield clk_fast.posedge
			update_s.next = 0
			yield clk_fast.posedge
			update_s.next = 1
			yield clk_fast.posedge
			update_s.next = 0
			yield clk_fast.posedge
		raise StopSimulation
	return instances()
tb(clk_fast, res_out_x, left_s_i,sam_s_i, right_s_i, flgs_s_i,
noupdate_s, update_s, left_com_x, sam_com_x, right_com_x,
lft_s_i, sa_s_i, rht_s_i,
merge_rdy_s, nomerge_s,
W0=W0, LVL0=LVL0, W1=W1, LVL1=LVL1, W2=W2,
LVL2=LVL2, W3=W3, LVL3=LVL3)
tb_fsm = traceSignals(
tb, clk_fast, res_out_x, left_s_i,sam_s_i, right_s_i, flgs_s_i,
noupdate_s, update_s, left_com_x, sam_com_x, right_com_x,
lft_s_i, sa_s_i, rht_s_i,
merge_rdy_s, nomerge_s)
sim = Simulation(tb_fsm)
sim.run()
