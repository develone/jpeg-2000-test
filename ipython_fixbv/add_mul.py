from myhdl import *


DATA_WIDTH =  262144
# 9/7 Coefficients:
#a1 = -1.586134342
#a2 = -0.05298011854
#a3 = 0.8829110762
#a4 = 0.4435068522
ww = (24,14)
d3 = Signal(fixbv(0)[ww])
a2 = Signal(fixbv(0)[ww])
 
x2 = Signal(fixbv(156)[ww])
x3 = Signal(fixbv(164)[ww]) 
#from prev operation
x4 = Signal(fixbv(156)[ww])
x5 = Signal(fixbv(156)[ww])
clk = Signal(bool(0))
odd_even = Signal(bool(0)) 
p = Signal(bool(0))
fwd_res = Signal(bool(0))         
def add_mul(d3,a2,clk,x2,x3,x4,x5,p,odd_even,fwd_res):


	t = fixbv(0)
	t1 = fixbv(0)
	@always(clk.posedge)
	def rtl():
		if not p:
		
			if odd_even:
				ca1 = fixbv(-1.586134342,min = -DATA_WIDTH, max= DATA_WIDTH,res=1e-5)
				ra4 = fixbv(-0.4435068522, min = -DATA_WIDTH, max = DATA_WIDTH, res=1e-5)
			
				if fwd_res:
					t = (x2+x3) * ca1
				else:
					t1 = (x4+x5) * ra4 				
				
			else:
				ca2 = fixbv(-0.05298011854,min = -DATA_WIDTH, max= DATA_WIDTH,res=1e-5)
				ra3 = fixbv(-0.8829110762, min = -DATA_WIDTH, max = DATA_WIDTH, res=1e-5)
				if fwd_res:
					t1 = (x4+x5) * ca2
				else:
					t = (x2+x3) * ra3				  					          
		else:
		 
			if odd_even:
				ca3 = fixbv(0.8829110762,min = -DATA_WIDTH, max= DATA_WIDTH,res=1e-5)
				ra2 = fixbv(0.05298011854, min = -DATA_WIDTH, max = DATA_WIDTH, res=1e-5)		
				if fwd_res:
					t = (x2+x3) * ca3
				else:
					t1 = (x4+x5) * ra2				 
			else: 
				ca4 = fixbv(0.4435068522, min = -DATA_WIDTH, max = DATA_WIDTH, res=1e-5)		
				ra1 = fixbv(1.586134342, min = -DATA_WIDTH, max = DATA_WIDTH, res=1e-5)
				if fwd_res:
					t1 = (x4+x5) * ca4
				else:
					t = (x2+x3) * ra1                  
	d3.next = t
	a2.next = t1  
                 
                 
	return rtl
        
d_instance = add_mul(d3,a2,clk,x2,x3,x4,x5,p,odd_even,fwd_res)


toVerilog(add_mul,d3,a2,clk,x2,x3,x4,x5,p,odd_even,fwd_res)
toVHDL(add_mul,d3,a2,clk,x2,x3,x4,x5,p,odd_even,fwd_res)
