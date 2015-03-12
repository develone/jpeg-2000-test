from myhdl import *
from jpeg_constants import *
toVHDL.numeric_ports = False
Sin0 = Signal(intbv(0)[10:])
Sin1 = Signal(intbv(0)[10:])
Sin2 = Signal(intbv(0)[10:])
Sin3 = Signal(intbv(0)[10:])
Sin4 = Signal(intbv(0)[10:])
Sin5 = Signal(intbv(0)[10:])
Sin6 = Signal(intbv(0)[10:])
Sin7 = Signal(intbv(0)[10:])
Sin8 = Signal(intbv(0)[10:])
Sin9 = Signal(intbv(0)[10:])
Sin10 = Signal(intbv(0)[10:])
Sin11 = Signal(intbv(0)[10:])
Sin12 = Signal(intbv(0)[10:])
Sin13 = Signal(intbv(0)[10:])
Sin14 = Signal(intbv(0)[10:])
Sin15 = Signal(intbv(0)[10:])
Sout_s = Signal(intbv(0)[160:])
combine_sig_s = Signal(bool(0))
clk_fast = Signal(bool(0))

def sig2one(Sout_s, clk_fast, combine_sig_s, Sin0, Sin1, Sin2, Sin3, Sin4, Sin5, Sin6, Sin7, Sin8, Sin9, Sin10, Sin11, Sin12, Sin13, Sin14, Sin15):

	@always_seq( clk_fast.posedge, reset = None)
	def combine_logic():
		if (combine_sig_s == 1):
			#Sout_s.next = concat(Sin15, Sin14, Sin13, Sin12, Sin11, Sin10, Sin9, Sin8, Sin7, Sin6, Sin5, Sin4, Sin3, Sin2, Sin1, Sin0)
			Sout_s.next = concat(Sin11,Sin10,Sin9,Sin8,Sin7,Sin6,Sin5,Sin4,Sin3,Sin2,Sin1,Sin0)
		else:
			Sout_s.next = 0
	return combine_logic
def convert():
	toVHDL(sig2one, Sout_s, clk_fast, combine_sig_s, Sin0, Sin1, Sin2, Sin3, Sin4, Sin5, Sin6, Sin7, Sin8, Sin9, Sin10, Sin11, Sin12, Sin13, Sin14, Sin15)
	toVerilog(sig2one,Sout_s, clk_fast, combine_sig_s, Sin0, Sin1, Sin2, Sin3, Sin4, Sin5, Sin6, Sin7, Sin8, Sin9, Sin10, Sin11, Sin12, Sin13, Sin14, Sin15)
def tb(Sout_s, clk_fast, combine_sig_s, Sin0, Sin1, Sin2, Sin3, Sin4, Sin5, Sin6, Sin7, Sin8, Sin9, Sin10, Sin11, Sin12, Sin13, Sin14, Sin15):

	instance_dut = sig2one(Sout_s, clk_fast, combine_sig_s, Sin0, Sin1, Sin2, Sin3, Sin4, Sin5, Sin6, Sin7, Sin8, Sin9, Sin10, Sin11, Sin12, Sin13, Sin14, Sin15)

	@always(delay (10))
	def clkgen():
		clk_fast.next = not clk_fast
	'''
	@instance
	def stimulus():
		for i in range(16):
			print("%3d") % (now())
		raise StopSimulation
	'''
	return instances()
convert()
x = tb(Sout_s, clk_fast, combine_sig_s, Sin0, Sin1, Sin2, Sin3, Sin4, Sin5, Sin6, Sin7, Sin8, Sin9, Sin10, Sin11, Sin12, Sin13, Sin14, Sin15)
print x


#sim = Simulation(tb_fsm)
#sim.run()
