from myhdl import *
m = [156.0, 156.0, 156.0, 156.0, 164.0, 164.0, 164.0, 164.0, 164.0, 164.0, 164.0, 164.0, 156.0, 156.0, 164.0, 164.0, 156.0, 156.0, 164.0, 164.0, 148.0, 148.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 164.0, 164.0, 164.0, 164.0, 164.0, 164.0, 172.0, 172.0, 172.0, 172.0, 172.0, 172.0, 172.0, 172.0, 172.0, 172.0, 164.0, 164.0, 148.0, 148.0, 156.0, 156.0, 124.0, 124.0, 116.0, 116.0, 92.0, 92.0, 92.0, 92.0, 84.0, 84.0, 108.0, 108.0, 108.0, 108.0, 100.0, 100.0, 100.0, 100.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 100.0, 100.0, 108.0, 108.0, 108.0, 108.0, 116.0, 116.0, 116.0, 116.0, 124.0, 124.0, 116.0, 116.0, 124.0, 124.0, 124.0, 124.0, 116.0, 116.0, 116.0, 116.0, 124.0, 124.0, 124.0, 124.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 124.0, 124.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 124.0, 124.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 132.0, 132.0, 140.0, 140.0, 124.0, 124.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 140.0, 140.0, 132.0, 132.0, 140.0, 140.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 140.0, 140.0, 132.0, 132.0, 132.0, 132.0, 140.0, 140.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 140.0, 140.0, 132.0, 132.0, 140.0, 140.0, 132.0, 132.0, 132.0, 132.0, 124.0, 124.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 140.0, 140.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 124.0, 124.0, 132.0, 132.0, 140.0, 140.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 124.0, 124.0, 132.0, 132.0, 140.0, 140.0, 132.0, 132.0, 132.0, 132.0, 124.0, 124.0, 132.0, 132.0, 124.0, 124.0, 140.0, 140.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 124.0, 124.0, 140.0, 140.0, 132.0, 132.0, 124.0, 124.0, 124.0, 124.0, 132.0, 132.0, 124.0, 124.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 124.0, 124.0, 132.0, 132.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 116.0, 116.0, 124.0, 124.0, 116.0, 116.0, 108.0, 108.0, 116.0, 116.0, 100.0, 100.0, 100.0, 100.0, 116.0, 116.0, 124.0, 124.0, 132.0, 132.0, 140.0, 140.0, 148.0, 148.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 164.0, 164.0, 164.0, 164.0, 156.0, 156.0, 148.0, 148.0, 156.0, 156.0, 156.0, 156.0, 148.0, 148.0, 148.0, 148.0, 156.0, 156.0, 156.0, 156.0, 148.0, 148.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 148.0, 148.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 164.0, 164.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 188.0, 188.0, 204.0, 204.0, 212.0, 212.0, 212.0, 212.0, 220.0, 220.0, 220.0, 220.0, 220.0, 220.0, 212.0, 212.0, 196.0, 196.0, 148.0, 148.0, 108.0, 108.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 116.0, 116.0, 124.0, 124.0, 116.0, 116.0, 116.0, 116.0, 132.0, 132.0, 124.0, 124.0, 116.0, 116.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 116.0, 116.0, 124.0, 124.0, 132.0, 132.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 116.0, 116.0, 132.0, 132.0, 132.0, 132.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 132.0, 132.0, 132.0, 132.0, 116.0, 116.0, 116.0, 116.0, 116.0, 116.0, 116.0, 116.0, 124.0, 124.0, 132.0, 132.0, 164.0, 164.0, 172.0, 172.0, 156.0, 156.0]
DATA_WIDTH = 32768

left = (intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))
right = (intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))
sam = (intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))
res = (intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))

left_s = Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))
right_s = Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))
sam_s = Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))
res_s = Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))

updated_s = Signal(bool(0))
even_odd_s = Signal(bool(0))
fwd_inv_s = Signal(bool(0))
clk_fast = Signal(bool(0))
noupdate_s = Signal(bool(0))
leftDelDut_s = Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))
signalDelayed_s = Signal(bool(0))
updated_jpeg_s = Signal(bool(0))
flag = 0
def step1(sam,left,right,flag):
	if flag == 1:
		res =  sam - ((left >> 1) + (right >> 1))
	else:
		res =  sam - ((left >> 1) + (right >> 1))
	return res

def step2(sam,left,right,flag):
	if flag == 1:
		res =  sam + ((left) + (right ))>>2
	else:
		res =  sam - ((left) + (right ))>>2
	return res
def test_jpeg():
	for i in range(2,128-1,2):
		sam = int(m[i])
		left = int(m[i - 1])
		right = int(m[i + 1])
		flag = 1
		print i, flag, sam, left, right, step1(sam,left,right,flag)
		flag = 0
		print i, flag, sam, left, right, step1(sam,left,right,flag)
		flag = 1
		print i, flag, sam, left, right, step2(sam,left,right,flag)
		flag = 0
		print i, flag, sam, left, right, step2(sam,left,right,flag)
	for i in range(1,128,2):
		sam = int(m[i])
		left = int(m[i - 1])
		right = int(m[i + 1])
		flag = 1
		print i, flag, sam, left, right, step1(sam,left,right,flag)
		flag = 0
		print i, flag, sam, left, right, step1(sam,left,right,flag)
		flag = 1
		print i, flag, sam, left, right, step2(sam,left,right,flag)
		flag = 0
		print i, flag, sam, left, right, step2(sam,left,right,flag)

def jpeg(clk_fast, left_s, right_s, sam_s, res_s, updated_jpeg_s, even_odd_s , fwd_inv_s, updated_s, noupdate_s, signalDelayed_s):
	@always(clk_fast.posedge)
	def hdl():
		if updated_s:
			if even_odd_s:
				if  fwd_inv_s:
					if signalDelayed_s:
						res_s.next =  sam_s - ((leftDelDut_s >> 1) + (right_s >> 1))
					else:
						res_s.next =  sam_s - ((left_s >> 1) + (right_s >> 1))
				else:
					if signalDelayed_s:
						res_s.next =  sam_s + ((leftDelDut_s >> 1) + (right_s >> 1))
					else:
						res_s.next =  sam_s + ((left_s >> 1) + (right_s >> 1))
			else:
				if fwd_inv_s:
					if signalDelayed_s:
						res_s.next =  sam_s + ((leftDelDut_s +  right_s + 2)>>2)
					else:
						res_s.next =  sam_s + ((left_s +  right_s + 2)>>2)
				else:
					if signalDelayed_s:
						res_s.next =  sam_s - ((leftDelDut_s +  right_s + 2)>>2)
					else:
						res_s.next =  sam_s - ((left_s +  right_s + 2)>>2)
			updated_jpeg_s.next = 1
		else:
			noupdate_s.next = 1

	return hdl
def testbench():
	i_inst = jpeg( clk_fast, left_s, right_s, sam_s, res_s,updated_jpeg_s,  even_odd_s , fwd_inv_s, updated_s, noupdate_s, signalDelayed_s)

	@always(delay(10))
	def clkgen():
		clk_fast.next = not clk_fast

	@instance
	def stimulus():

		for i in range(1):
			updated_s.next = 1
			even_odd_s.next = 1
			fwd_inv_s.next = 1

			yield clk_fast.posedge
		for i in range(1,128,2):
			sam_s.next = int(m[i])
			left_s.next = int(m[i - 1])
			right_s.next = int(m[i + 1])
			if i == 45:
				even_odd_s.next = 0
			if i == 65:
				fwd_inv_s.next = 0
			if i == 73:
				updated_s.next = 0
			yield clk_fast.posedge
		raise StopSimulation
	return   i_inst, stimulus, clkgen
def convert():
	toVerilog(jpeg, clk_fast, left_s, right_s, sam_s, res_s, updated_jpeg_s, even_odd_s , fwd_inv_s, updated_s, noupdate_s, signalDelayed_s)
	toVHDL(jpeg, clk_fast, left_s, right_s, sam_s, res_s, updated_jpeg_s, even_odd_s , fwd_inv_s, updated_s, noupdate_s, signalDelayed_s)
convert()
tb_fsm = traceSignals(testbench)
sim = Simulation(tb_fsm)
sim.run()
#test_jpeg()
