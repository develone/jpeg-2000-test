from myhdl import *
m = [156.0, 156.0, 156.0, 156.0, 164.0, 164.0, 164.0, 164.0, 164.0, 164.0, 164.0, 164.0, 156.0, 156.0, 164.0, 164.0, 156.0, 156.0, 164.0, 164.0, 148.0, 148.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 164.0, 164.0, 164.0, 164.0, 164.0, 164.0, 172.0, 172.0, 172.0, 172.0, 172.0, 172.0, 172.0, 172.0, 172.0, 172.0, 164.0, 164.0, 148.0, 148.0, 156.0, 156.0, 124.0, 124.0, 116.0, 116.0, 92.0, 92.0, 92.0, 92.0, 84.0, 84.0, 108.0, 108.0, 108.0, 108.0, 100.0, 100.0, 100.0, 100.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 100.0, 100.0, 108.0, 108.0, 108.0, 108.0, 116.0, 116.0, 116.0, 116.0, 124.0, 124.0, 116.0, 116.0, 124.0, 124.0, 124.0, 124.0, 116.0, 116.0, 116.0, 116.0, 124.0, 124.0, 124.0, 124.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 124.0, 124.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 124.0, 124.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 132.0, 132.0, 140.0, 140.0, 124.0, 124.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 140.0, 140.0, 132.0, 132.0, 140.0, 140.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 140.0, 140.0, 132.0, 132.0, 132.0, 132.0, 140.0, 140.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 140.0, 140.0, 132.0, 132.0, 140.0, 140.0, 132.0, 132.0, 132.0, 132.0, 124.0, 124.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 140.0, 140.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 124.0, 124.0, 132.0, 132.0, 140.0, 140.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 124.0, 124.0, 132.0, 132.0, 140.0, 140.0, 132.0, 132.0, 132.0, 132.0, 124.0, 124.0, 132.0, 132.0, 124.0, 124.0, 140.0, 140.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 124.0, 124.0, 140.0, 140.0, 132.0, 132.0, 124.0, 124.0, 124.0, 124.0, 132.0, 132.0, 124.0, 124.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 132.0, 124.0, 124.0, 132.0, 132.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 116.0, 116.0, 124.0, 124.0, 116.0, 116.0, 108.0, 108.0, 116.0, 116.0, 100.0, 100.0, 100.0, 100.0, 116.0, 116.0, 124.0, 124.0, 132.0, 132.0, 140.0, 140.0, 148.0, 148.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 164.0, 164.0, 164.0, 164.0, 156.0, 156.0, 148.0, 148.0, 156.0, 156.0, 156.0, 156.0, 148.0, 148.0, 148.0, 148.0, 156.0, 156.0, 156.0, 156.0, 148.0, 148.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 148.0, 148.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 164.0, 164.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 188.0, 188.0, 204.0, 204.0, 212.0, 212.0, 212.0, 212.0, 220.0, 220.0, 220.0, 220.0, 220.0, 220.0, 212.0, 212.0, 196.0, 196.0, 148.0, 148.0, 108.0, 108.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 116.0, 116.0, 124.0, 124.0, 116.0, 116.0, 116.0, 116.0, 132.0, 132.0, 124.0, 124.0, 116.0, 116.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 116.0, 116.0, 124.0, 124.0, 132.0, 132.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 116.0, 116.0, 132.0, 132.0, 132.0, 132.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 132.0, 132.0, 132.0, 132.0, 116.0, 116.0, 116.0, 116.0, 116.0, 116.0, 116.0, 116.0, 124.0, 124.0, 132.0, 132.0, 164.0, 164.0, 172.0, 172.0, 156.0, 156.0]
DATA_WIDTH = 32768
RAM_ADDR = 9
dout = Signal(intbv(0)[16:])
dout_v = Signal(intbv(0)[8:])
din = Signal(intbv(0)[16:])
addr = Signal(intbv(0)[RAM_ADDR:])
reset_jpeg = Signal(bool(0))
odd = Signal(bool(0))
we = Signal(bool(0))
we_lf = Signal(bool(0))
we_sam = Signal(bool(0))
we_rht = Signal(bool(0))
we_res = Signal(bool(0))
dout_lf = Signal(intbv(0)[16:])
dout_sam = Signal(intbv(0)[16:])
dout_rht = Signal(intbv(0)[16:])
dout_res = Signal(intbv(0)[16:])

addr_lf = Signal(intbv(0)[RAM_ADDR:])
addr_sam = Signal(intbv(0)[RAM_ADDR:])
addr_rht = Signal(intbv(0)[RAM_ADDR:])
addr_res = Signal(intbv(0)[RAM_ADDR:])

#clk = Signal(bool(0))
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

odd_i = Signal(bool(0))
incRes_i = Signal(bool(0))
we_s_o = Signal(bool(0))
reset_sav_i = Signal(bool(0))
dout_res_o = Signal(intbv(0)[16:])
res_i = Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))
addr_res_o = Signal(intbv(0)[RAM_ADDR:]) 
 
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
def save_to_ram(clk_fast, dout_res_o, res_i, we_s_o, reset_sav_i, addr_res_o, incRes_i, odd_i):
    @always(clk_fast.posedge)
    def xx():
        if (reset_sav_i == 1):
            we_s_o.next = 0
            if (odd_i == 1):
                addr_res_o.next = 1
            else:
                addr_res_o.next = 2
        elif (incRes_i == 1):
            we_s_o.next = 0
            addr_res_o.next = addr_res_o + 2
            
        else:    
            we_s_o.next = 1
            dout_res_o.next = res_i
        
            
    return xx		
def approx(clk_fast, even_odd_s, left_s, sam_s, right_s, we_lf, we_sam, we_rht, we_res, addr_lf, addr_sam, addr_rht, addr_res, dout_lf, dout_sam, dout_rht, odd, reset_jpeg, updated_s):

	@always(clk_fast.posedge)
	def xx():
		if reset_jpeg:
			updated_s.next = 0
			we_lf.next = 0
			we_sam.next = 0
			we_rht.next = 0
			we_res.next = 1
			if odd:
				addr_lf.next = 1
				addr_sam.next = 1
				addr_rht.next = 1
				addr_res.next = 1
				even_odd_s.next = 0
			else:
				addr_lf.next = 2
				addr_sam.next = 2
				addr_rht.next = 2
				addr_res.next = 2
				even_odd_s.next = 1
		else:
			if (addr_res <= 64):
				left_s.next = dout_lf
				sam_s.next = dout_sam
				right_s.next = dout_rht
				updated_s.next = 1
				if (updated_s == 0):
					addr_lf.next = addr_lf + 2
					addr_sam.next = addr_sam + 2
					addr_rht.next = addr_rht + 2
					addr_res.next = addr_res + 2





 
    
	return xx
	

	
	
def ram(dout, din, addr, we, clk_fast, depth=256):
    """  Ram model """
    
    mem = [Signal(intbv(0)[16:]) for i in range(depth)]
    
    @always(clk_fast.posedge)
    def write():
        if we:
            mem[addr].next = din
                
    @always_comb
    def read():
        dout.next = mem[addr]

    return write, read




def jpeg(clk_fast, left_s, right_s, sam_s, res_s, even_odd_s , fwd_inv_s, updated_s, noupdate_s):
	@always(clk_fast.posedge)
	def hdl():
		if updated_s:
			noupdate_s.next = 0
			if even_odd_s:
				if  fwd_inv_s:
					res_s.next =  sam_s - ((left_s >> 1) + (right_s >> 1))
				else:
					res_s.next =  sam_s + ((left_s >> 1) + (right_s >> 1))
			else:
				if fwd_inv_s:
					res_s.next =  sam_s + ((left_s +  right_s + 2)>>2)
				else:
					res_s.next =  sam_s - ((left_s +  right_s + 2)>>2)
		else:
			noupdate_s.next = 1

	return hdl
def testbench():
	i_inst = jpeg( clk_fast, left_s, right_s, sam_s, res_s, even_odd_s , fwd_inv_s, updated_s, noupdate_s)

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
	toVerilog(jpeg, clk_fast, left_s, right_s, sam_s, res_s, even_odd_s , fwd_inv_s, updated_s, noupdate_s)
	toVHDL(jpeg, clk_fast, left_s, right_s, sam_s, res_s, even_odd_s , fwd_inv_s, updated_s, noupdate_s)
	toVerilog(ram, dout, din, addr, we, clk_fast)
	toVHDL(ram, dout, din, addr, we, clk_fast)
	#toVerilog(approx, clk_fast, even_odd_s, left_s, sam_s, right_s, we_lf, we_sam, we_rht, we_res, addr_lf, addr_sam, addr_rht, addr_res,  dout_lf, dout_sam, dout_rht, odd, reset_jpeg, updated_s)
	#toVHDL(approx, clk_fast, even_odd_s, left_s, sam_s, right_s, we_lf, we_sam, we_rht, we_res, addr_lf, addr_sam, addr_rht, addr_res,  dout_lf, dout_sam, dout_rht, odd, reset_jpeg, updated_s)
	toVerilog(save_to_ram, clk_fast, dout_res_o, res_i, we_s_o, reset_sav_i, addr_res_o, incRes_i, odd_i)
	toVHDL(save_to_ram, clk_fast, dout_res_o, res_i, we_s_o, reset_sav_i, addr_res_o, incRes_i, odd_i)
#convert()
tb_fsm = traceSignals(testbench)
sim = Simulation(tb_fsm)
sim.run()
#test_jpeg()
