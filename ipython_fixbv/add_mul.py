from myhdl import *


DATA_WIDTH = 262144
# 9/7 Coefficients:
#a1 = -1.586134342
#a2 = -0.05298011854
#a3 = 0.8829110762
#a4 = 0.4435068522

d3 = Signal(fixbv(0, min = -DATA_WIDTH, max = DATA_WIDTH, res=1e-5))
a2 = Signal(fixbv(0, min = -DATA_WIDTH, max = DATA_WIDTH, res=1e-5))
 
x2 = Signal(fixbv(156, min = -DATA_WIDTH, max = DATA_WIDTH))
x3 = Signal(fixbv(164, min = -DATA_WIDTH, max = DATA_WIDTH)) 
#from prev operation
x4 = Signal(fixbv(156, min = -DATA_WIDTH, max = DATA_WIDTH))
x5 = Signal(fixbv(156, min = -DATA_WIDTH, max = DATA_WIDTH))
clk = Signal(bool(0))
odd_even = Signal(bool(0)) 
p = Signal(bool(0))           
def add_mul(d3,a2,clk,x2,x3,x4,x5,p,odd_even):


	t = fixbv(0, min = -DATA_WIDTH, max = DATA_WIDTH,res=1e-5)
	t1 = fixbv(0, min = -DATA_WIDTH, max = DATA_WIDTH,res=1e-5)
	@always(clk.posedge)
	def rtl():
		if not p:
		
			if odd_even:
				ca1 = fixbv(-1.586134342, min = -DATA_WIDTH, max = DATA_WIDTH, res=1e-5)
				t = (x2+x3) * ca1
			else:
				ca2 = fixbv(-0.05298011854, min = -DATA_WIDTH, max = DATA_WIDTH, res=1e-5)
				t1 = (x4+x5) * ca2					          
		else:
		 
			if odd_even:
				ca3 = fixbv(0.8829110762, min = -DATA_WIDTH, max = DATA_WIDTH, res=1e-5)
				t = (x2+x3) * ca3
			else: 
				ca4 = fixbv(0.4435068522, min = -DATA_WIDTH, max = DATA_WIDTH, res=1e-5)
				t1 = (x4+x5) * ca4                 
	d3.next = t
	a2.next = t1  
                 
                 
	return rtl
        
d_instance = add_mul(d3,a2,clk,x2,x3,x4,x5,p,odd_even)


toVerilog(add_mul,d3,a2,clk,x2,x3,x4,x5,p,odd_even)
toVHDL(add_mul,d3,a2,clk,x2,x3,x4,x5,p,odd_even)
