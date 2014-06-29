from myhdl import *


def add_mul(d3,a2,clk,x2,x3,x4,x5,p,even_odd,fwd_inv):
	
	@always(clk.posedge)
	def rtl():

		if not p:
		
			if even_odd:			
				if fwd_inv:
					ca1 = fixbv(-1.586134342)[24,14]
					t = fixbv(0)[24,14]
	
					t = (x2+x3) * ca1
					d3.next = t			
				else:
					ra4 = fixbv(-0.4435068522)[24,14]
					t1 = fixbv(0)[24,14]
					 
					t1 = (x4+x5) * ra4 				
					a2.next = t1	
			else:				
				if fwd_inv:
					ca2 = fixbv(-0.05298011854)[24,14]
					t1 = fixbv(0)[24,14]
					 
					t1 = (x4+x5) * ca2
					a2.next = t1
					
				else:
					ra3 = fixbv(-0.8829110762)[24,14]
					t = fixbv(0)[24,14]
					
					t = (x2+x3) * ra3
					d3.next = t							  					          
		else:
			if even_odd:
				if fwd_inv:
					ca3 = fixbv(0.8829110762)[24,14]
					t = fixbv(0)[24,14]
					
					t = (x2+x3) * ca3
					d3.next = t
				else:
					ra2 = fixbv(0.05298011854)[24,14]
					t1 = fixbv(0)[24,14]
					t1 = (x4+x5) * ra2
					a2.next = t1			 
			else: 
				if fwd_inv:
					ca4 = fixbv(0.4435068522)[24,14]
					t1 = fixbv(0)[24,14]
					t1 = (x4+x5) * ca4
					a2.next = t1
				else:
					ra1 = fixbv(1.586134342)[24,14]
					t = fixbv(0)[24,14]
					
					t = (x2+x3) * ra1
					d3.next = t
					                 
		print hex(d3), d3,  hex(a2), a2 
                 
	return rtl
 
        
