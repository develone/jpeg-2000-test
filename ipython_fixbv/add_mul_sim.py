from myhdl import *

 


class Add_mul_top(object):

	def __init__(self):
		ww = (31,10)
		self.even_odd = (bool(0))
		self.fwd_inv = (bool(0))
		self.p = (bool(0))
		self.left = (fixbv(0)[ww])
		self.right = (fixbv(0)[ww])
 
		self.din_odd = (fixbv(0)[ww])
		self.dout_odd = (fixbv(0)[ww])
		self.we_odd = (bool(0))
		self.addr_odd = (intbv(0)[7:])

		self.din_even = (fixbv(0)[ww])
		self.dout_even = (fixbv(0)[ww])
		self.we_even = (bool(0))
		self.addr_even = (intbv(0)[7:])

 

  
 

	def setSig_we_odd(self,val):   
		self.we_odd = (bool(val))
		
	def setSig_we_even(self,val):   
		self.we_even = (bool(val))
	
 
	
 	def setSig_addr_odd(self,val):   
		self.addr_odd = (intbv(val))

 	def setSig_addr_even(self,val):   
		self.addr_even = (intbv(val))

	def setSig_addr_odd1(self,val):   
		self.addr_odd1 = (intbv(val))

 

	def setSig_din_odd(self,val):   
		ww = (31,10)
		self.din_odd = (fixbv(val)[ww])		

 

 
	def setSig_left(self,val):   
		ww = (31,10)
		self.left = (fixbv(val)[ww])	
	def setSig_right(self,val):   
		ww = (31,10)
		self.right = (fixbv(val)[ww])
 
	def setSig_even_odd(self,val):   
		self.even_odd = (bool(val))
	def setSig_fwd_inv(self,val):   
		self.fwd_inv = (bool(val))	
	def setSig_p(self,val):   
		self.p = (bool(val))									
def add_mul_ram( pix):
	#DATA_WIDTH = 262144
	ww = (31,10)
        '''
	ca1 = fixbv(-1.586134342, min = -DATA_WIDTH, max = DATA_WIDTH, res=1e-5)
	ra4 = fixbv(-0.4435068522, min = -DATA_WIDTH, max = DATA_WIDTH, res=1e-5)
	ca2 = fixbv(-0.05298011854, min = -DATA_WIDTH, max = DATA_WIDTH, res=1e-5)
	ra3 = fixbv(-0.8829110762, min = -DATA_WIDTH, max = DATA_WIDTH, res=1e-5)
	ca3 = fixbv(0.8829110762, min = -DATA_WIDTH, max = DATA_WIDTH, res=1e-5)		
	ra2 = fixbv(0.05298011854, min = -DATA_WIDTH, max = DATA_WIDTH, res=1e-5)
	ca4 = fixbv(0.4435068522, min = -DATA_WIDTH, max = DATA_WIDTH, res=1e-5)		
	ra1 = fixbv(1.586134342, min = -DATA_WIDTH, max = DATA_WIDTH, res=1e-5)
        '''		
	ca1 = fixbv(-1.586134342)[ww]
        ra4 = fixbv(-0.4435068522)[ww]
	ca2 = fixbv(-0.05298011854)[ww]
        ra3 = fixbv(-0.8829110762)[ww]
        ca3 = fixbv(0.8829110762)[ww]
        ra2 = fixbv(0.05298011854)[ww]
	ca4 = fixbv(0.4435068522)[ww]
	ra1 = fixbv(1.586134342)[ww]
	
	
	
	

	 
	

	if not pix.p:
 
		if pix.even_odd: 
			if pix.fwd_inv:
				pix.din_even = (pix.left + pix.right)*ca2
				 				 
			else:
				pix.din_even = (pix.left + pix.right)*ra4
			 
		else:
			if pix.fwd_inv:
				pix.din_odd = (pix.left + pix.right)*ca1
			 
			else:
				pix.din_odd = (pix.left + pix.right)*ra3
				 
	else:
 
 		if pix.even_odd:
			if pix.fwd_inv:
				pix.din_even = (pix.left + pix.right)*ca4
			 
			else:
				pix.din_even = (pix.left + pix.right)*ra2
				 
					
		else:
			if pix.fwd_inv:
				pix.din_odd = (pix.left + pix.right)*ca3
				 
			else:
				pix.din_odd = (pix.left + pix.right)*ra1
		 	
			
	
	return pix.din_even, pix.din_odd 
	
	

