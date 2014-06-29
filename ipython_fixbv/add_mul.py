from myhdl import *



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
even_odd = Signal(bool(0)) 
p = Signal(bool(0))
fwd_inv = Signal(bool(0))         


def add_mul(d3,a2,clk,x2,x3,x4,x5,p,even_odd,fwd_inv):
	ca1 = Signal(fixbv(-1.586134342)[ww])
	ca2 = Signal(fixbv(-0.05298011854)[ww])
	ca3 = Signal(fixbv(0.8829110762)[ww])
	ca4 = Signal(fixbv(0.4435068522)[ww])
	ra1 = Signal(fixbv(1.586134342)[ww])
	ra2 = Signal(fixbv(0.05298011854)[ww])
	ra3 = Signal(fixbv(-0.8829110762)[ww])
	ra4 = Signal(fixbv(-0.4435068522)[ww])
	t = Signal(fixbv(0)[ww])
	t1 = Signal(fixbv(0)[ww])
	@always(clk.posedge)
	def rtl():

		if not p:
		
			if even_odd:
				
			
				if fwd_inv:
					 
					t = (x2+x3) * ca1
					d3.next = t
			
				else:
					 
					t1 = (x4+x5) * ra4 				
					a2.next = t1	
			else:
				
				if fwd_inv:
					 
					t1 = (x4+x5) * ca2
					a2.next = t1
					
				else:
					t = (x2+x3) * ra3
					d3.next = t
			
			  

									  					          
		else:
		 
			if even_odd:
						
				if fwd_inv:
					t = (x2+x3) * ca3
					d3.next = t
				else:
					t1 = (x4+x5) * ra2
					a2.next = t1			 
			else: 
				
				if fwd_inv:
					t1 = (x4+x5) * ca4
					a2.next = t1
				else:
					t = (x2+x3) * ra1
					d3.next = t
					                 
    
                 
	return rtl
def convert(ver,both=False):
	
	d_instance = add_mul(d3,a2,clk,x2,x3,x4,x5,p,even_odd,fwd_inv)
		 
	
	if ver:
		toVerilog(add_mul,d3,a2,clk,x2,x3,x4,x5,p,even_odd,fwd_inv)
		if both:
			toVHDL(add_mul,d3,a2,clk,x2,x3,x4,x5,p,even_odd,fwd_inv)		
	else:
		toVHDL(add_mul,d3,a2,clk,x2,x3,x4,x5,p,even_odd,fwd_inv)
#convert(True,True)
#convert(True)
#convert(False)
