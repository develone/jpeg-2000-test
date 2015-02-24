from myhdl import *
from rom import *
from array_jpeg import jp_process
from merge_sam import merge
CONTENT = [
668288, 672388, 668288]

W0 = 8
LVL0 = 16
W1 = 8
LVL1 = 16
W2 = 8
LVL2 = 16
W3 = 5
LVL3 = 16
SIMUL = 1

clk_fast = Signal(bool(0))
res_out_x = Signal(intbv(0, min= -(2**(W0+1)) ,max= (2**(W0+1))))
update_s = Signal(bool(0))
noupdate_s = Signal(bool(0))

left_s_i = Signal(intbv(0)[LVL2*W2:])
sam_s_i = Signal(intbv(0)[LVL2*W2:])
right_s_i = Signal(intbv(0)[LVL2*W2:])
flgs_s_i = Signal(intbv(0)[LVL3*W3:])

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
			print( "%3d ") % (now())

			yield clk_fast.posedge
		for i in range(2):
			#10	9	8	8	7	6	6	5	4	4	3	2	2	1	0
			lft_s_i.next = (160 << W0*15) + (163 << W0*14)+(156 << W0*13) + (157 << W0*12) + (160 << W0*11)+(163 << W0*10) + (156 << W0*9)+(160 << W0*8) +(159 << W0*7) + (144 << W0*6) + (157 <<  W0*5) + (163 << W0*4) + (161 << W0*3) + (159 << W0*2) + (157 << W0) + 158
			sa_s_i.next = (158 << W0*15) + (159 << W0*14)+(160 << W0*13) + (161 << W0*12) + (162 << W0*11)+(163 << W0*10) + (164 << W0*9)+(165 << W0*8) +(166 << W0*7) + (165 << W0*6) + (164 <<  W0*5) + (163 << W0*4) + (162 << W0*3) + (161 << W0*2) + (160 << W0) + 159
			rht_s_i.next = (157 << W0*15) + (160 << W0*14)+(163 << W0*13) + (156 << W0*12) + (157 << W0*11)+(160 << W0*10) + (163 << W0*9)+(156 << W0*8) +(160 << W0*7) + (159 << W0*6) + (144 <<  W0*5) + (157 << W0*4) + (163 << W0*3) + (161 << W0*2) + (159 << W0) + 157

 			yield clk_fast.posedge
			merge_rdy_s.next = 1
			yield clk_fast.posedge

 		for i in range(2):
			print( "%3d %s %s %s") % (now(), hex(left_s_i), hex(sam_s_i), hex(right_s_i))
			left_s_i.next = left_com_x
			sam_s_i.next = sam_com_x
			right_s_i.next = right_com_x
 			yield clk_fast.posedge
		addr_flgs.next = 0
		for i in range(26):

			flgs_s_i.next = dout_flgs
			yield clk_fast.posedge
			#print( "%3d %s") % (now(), hex(flgs_s_i))
			addr_flgs.next = addr_flgs + 1
			yield clk_fast.posedge
			update_s.next = 1
			yield clk_fast.posedge
			print ("%d %d %s") % (now(), res_out_x.signed(), bin(flgs_s_i) )
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
