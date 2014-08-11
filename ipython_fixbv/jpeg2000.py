from myhdl import *
m = [156.0, 156.0, 156.0, 156.0, 164.0, 164.0, 164.0, 164.0, 164.0, 164.0, 164.0, 164.0, 156.0, 156.0, 164.0, 164.0, 156.0, 156.0, 164.0, 164.0, 148.0, 148.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 164.0, 164.0, 164.0, 164.0, 164.0, 164.0, 172.0, 172.0, 172.0, 172.0, 172.0, 172.0, 172.0, 172.0, 172.0, 172.0, 164.0, 164.0, 148.0, 148.0, 156.0, 156.0, 124.0, 124.0, 116.0, 116.0, 92.0, 92.0, 92.0, 92.0, 84.0, 84.0, 108.0, 108.0, 108.0, 108.0, 100.0, 100.0, 100.0, 100.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 100.0, 100.0, 108.0, 108.0, 108.0, 108.0, 116.0, 116.0, 116.0, 116.0, 124.0, 124.0, 116.0, 116.0, 124.0, 124.0, 124.0, 124.0, 116.0, 116.0, 116.0, 116.0, 124.0, 124.0, 124.0, 124.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 124.0, 124.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 124.0, 124.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 132.0, 132.0, 140.0, 140.0, 124.0, 124.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 140.0, 140.0, 132.0, 132.0, 140.0, 140.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 140.0, 140.0, 132.0, 132.0, 132.0, 132.0, 140.0, 140.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 140.0, 140.0, 132.0, 132.0, 140.0, 140.0, 132.0, 132.0, 132.0, 132.0, 124.0, 124.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 140.0, 140.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 124.0, 124.0, 132.0, 132.0, 140.0, 140.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 124.0, 124.0, 132.0, 132.0, 140.0, 140.0, 132.0, 132.0, 132.0, 132.0, 124.0, 124.0, 132.0, 132.0, 124.0, 124.0, 140.0, 140.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 124.0, 124.0, 140.0, 140.0, 132.0, 132.0, 124.0, 124.0, 124.0, 124.0, 132.0, 132.0, 124.0, 124.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 124.0, 124.0, 132.0, 132.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 116.0, 116.0, 124.0, 124.0, 116.0, 116.0, 108.0, 108.0, 116.0, 116.0, 100.0, 100.0, 100.0, 100.0, 116.0, 116.0, 124.0, 124.0, 132.0, 132.0, 140.0, 140.0, 148.0, 148.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 164.0, 164.0, 164.0, 164.0, 156.0, 156.0, 148.0, 148.0, 156.0, 156.0, 156.0, 156.0, 148.0, 148.0, 148.0, 148.0, 156.0, 156.0, 156.0, 156.0, 148.0, 148.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 148.0, 148.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 164.0, 164.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 188.0, 188.0, 204.0, 204.0, 212.0, 212.0, 212.0, 212.0, 220.0, 220.0, 220.0, 220.0, 220.0, 220.0, 212.0, 212.0, 196.0, 196.0, 148.0, 148.0, 108.0, 108.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 116.0, 116.0, 124.0, 124.0, 116.0, 116.0, 116.0, 116.0, 132.0, 132.0, 124.0, 124.0, 116.0, 116.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 116.0, 116.0, 124.0, 124.0, 132.0, 132.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 116.0, 116.0, 132.0, 132.0, 132.0, 132.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 132.0, 132.0, 132.0, 132.0, 116.0, 116.0, 116.0, 116.0, 116.0, 116.0, 116.0, 116.0, 124.0, 124.0, 132.0, 132.0, 164.0, 164.0, 172.0, 172.0, 156.0, 156.0]
DATA_WIDTH = 131072

left = (intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))
right = (intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))
sam = (intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))
res = (intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))

left_i = Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))
right_i = Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))
sam_i = Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))
res_o = Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))

updated_i = Signal(bool(0))
even_odd_i = Signal(bool(0))
fwd_inv_i = Signal(bool(0))
clk_i = Signal(bool(0))
noupdate_o = Signal(bool(0))
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
			
def jpeg(clk_i, left_i, right_i, sam_i, updated_i, even_odd_i, fwd_inv_i, noupdate_o, res_o):
	@always(clk_i.posedge)
	def hdl():
		if  updated_i == 1:
			if even_odd_i:
				if  fwd_inv_i:
					 res_o.next =  sam_i - ((left_i >> 1) + (right_i >> 1))
				else:
					 res_o.next =  sam_i + ((left_i >> 1) + ( right_i >> 1))
			else:
				if fwd_inv_i:
					 res_o.next =  sam_i + (left_i +  right_i + 2)>>2
				else:
					 res_o.next =  sam_i - (left_i +  right_i + 2)>>2
		else:
			noupdate_o.next = 1
	return hdl
def testbench():
	i_inst = jpeg( clk_i, left_i, right_i, sam_i, updated_i, even_odd_i, fwd_inv_i, noupdate_o, res_o)

	@always(delay(10))
	def clkgen():
		clk_i.next = not clk_i
	
	@instance
	def stimulus():	
	
		for i in range(1):
			updated_i.next = 1
			even_odd_i.next = 1
			fwd_inv_i.next = 1
			
			yield clk_i.posedge
		for i in range(1,128,2):
			sam_i.next = int(m[i])
			left_i.next = int(m[i - 1])
			right_i.next = int(m[i + 1])
			if i == 45:
				even_odd_i.next = 0
			if i == 65:
				fwd_inv_i.next = 0
			if i == 73:
				updated_i.next = 0	
			yield clk_i.posedge	
		raise StopSimulation
	return   i_inst, stimulus, clkgen
def convert():			
	toVerilog(jpeg, clk_i, left_i, right_i, sam_i, updated_i, even_odd_i, fwd_inv_i, noupdate_o, res_o)
	toVHDL(jpeg, clk_i, left_i, right_i, sam_i, updated_i, even_odd_i, fwd_inv_i, noupdate_o, res_o)
#convert()
tb_fsm = traceSignals(testbench)
sim = Simulation(tb_fsm)
sim.run()
#test_jpeg()
