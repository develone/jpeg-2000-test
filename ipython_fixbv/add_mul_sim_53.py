from myhdl import *

 


class Add_mul_top(object):
	
	def __init__(self):
		 
		self.even_odd = (bool(0))
		self.fwd_inv = (bool(0))
		self.p = (bool(0))
		self.left = (intbv(0)[9:])
		self.right = (intbv(0)[9:])
 
		self.din_odd = (intbv(0)[9:])
		self.dout_odd = (intbv(0)[9:])
		self.we_odd = (bool(0))
		self.addr_odd = (intbv(0)[7:])

		self.din_even = (intbv(0)[9:])
		self.dout_even = (intbv(0)[9:])
		self.we_even = (bool(0))
		self.addr_even = (intbv(0)[7:])

 

	def setSig_we_odd(self,val):   
		self.we_odd = (bool(val))
		
	def setSig_we_even(self,val):   
		self.we_even = (bool(val))
	
 	def setSig_we_odd1(self,val):   
		self.we_odd1 = (bool(val))
	
 	def setSig_we_even1(self,val):   
		self.we_even1 = (bool(val))
	
 	def setSig_addr_odd(self,val):   
		self.addr_odd = (intbv(val))

 	def setSig_addr_even(self,val):   
		self.addr_even = (intbv(val))

 
	def setSig_din_odd(self,val):   
		
		self.din_odd = (intbv(val)[9:])		

 	def setSig_left(self,val):   
		self.left = (intbv(val)[9:])	
	
	def setSig_right(self,val):   
		self.right = (intbv(val)[9:])
		
 	def setSig_even_odd(self,val):   
		self.even_odd = (bool(val))
		
	def setSig_fwd_inv(self,val):   
		self.fwd_inv = (bool(val))	
	def setSig_p(self,val):   
		self.p = (bool(val))									
def add_mul_ram( pix):
 
	
             
 
	 
	

	if not pix.p:
 
		if pix.even_odd: 
			if pix.fwd_inv:
				pix.din_even = pix.right - (pix.left>>1 + pix.right>>1)
			else:
				pix.din_even = pix.left + (pix.left + pix.right + 2)>>2
				 
		else:
			if pix.fwd_inv:
				pix.din_odd = pix.left + (pix.left + pix.right + 2)>>2
				 
			else:
				pix.din_odd = pix.right - (pix.left>>1 + pix.right>>1)
				 
	else:
 
 		if pix.even_odd:
			if pix.fwd_inv:
				pix.din_even = pix.right - (pix.left>>1 + pix.right>>1)
				 
			else:
				pix.din_even = pix.left + (pix.left + pix.right + 2)>>2
				 
					
		else:
			if pix.fwd_inv:
				pix.din_odd = pix.left + (pix.left + pix.right + 2)>>2
				 
			else:
				pix.din_odd = pix.right - (pix.left>>1 + pix.right>>1)	 		
			
	
	return pix.din_even, pix.din_odd 
	
	

