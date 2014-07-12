from myhdl import *

 


class Add_mul_top(object):
	
	def __init__(self):
		 
		self.even_odd = (bool(0))
		self.fwd_inv = (bool(0))
		self.p = (bool(0))
		self.left = (intbv(0)[10:])
		self.right = (intbv(0)[10:])
		self.left1 = (intbv(0)[10:])
		self.right1 = (intbv(0)[10:])
		self.din_odd = (intbv(0)[10:])
		self.dout_odd = (intbv(0)[10:])
		self.we_odd = (bool(0))
		self.addr_odd = (intbv(0)[7:])

		self.din_even = (intbv(0)[10:])
		self.dout_even = (intbv(0)[10:])
		self.we_even = (bool(0))
		self.addr_even = (intbv(0)[7:])

		self.din_odd1 = (intbv(0)[10:])
		self.dout_odd1 = (intbv(0)[10:])
		self.we_odd1 = (bool(0))
		self.addr_odd1 = (intbv(0)[7:])

		self.din_even1 = (intbv(0)[10:])
		self.dout_even1 = (intbv(0)[10:])
		self.we_even1 = (bool(1))
		self.addr_even1 = (intbv(0)[7:])

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

	def setSig_addr_odd1(self,val):   
		self.addr_odd1 = (intbv(val))

	def setSig_addr_even1(self,val):   
		self.addr_even1 = (intbv(val))

	def setSig_din_odd(self,val):   
		
		self.din_odd = (intbv(val)[10:])		

	def setSig_din_odd1(self,val):   
		
		self.din_odd1 = (intbv(val)[10:])

	def setSig_din_even1(self,val):
		
		self.din_even1 = (intbv(val)[10:])
	def setSig_left(self,val):   
		
		self.left = (intbv(val)[10:])	
	def setSig_right(self,val):   
		
		self.right = (intbv(val)[10:])
	def setSig_left1(self,val):   
		
		self.left1 = (intbv(val)[10:])	
	def setSig_right1(self,val):   
		
		self.right1 = (intbv(val)[10:])
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
				pix.din_even = pix.right - (pix.left/2 + pix.right/2)
		 else:
				pix.din_odd = (pix.left + pix.right + 2)/4
				 
		else:
			if pix.fwd_inv:
				pix.din_odd = (pix.left + pix.right + 2)/4
				 
			else:
				pix.din_even = pix.right - (pix.left/2 + pix.right/2)
				 
	else:
 
 		if pix.even_odd:
			if pix.fwd_inv:
				pix.din_even = pix.right - (pix.left/2 + pix.right/2)
				 
			else:
				pix.din_odd = (pix.left + pix.right + 2)/4
				 
					
		else:
			if pix.fwd_inv:
				pix.din_odd = (pix.left + pix.right + 2)/4
				 
			else:
				pix.din_even = pix.right - (pix.left/2 + pix.right/2)	 		
			
	
	return pix.din_even, pix.din_odd 
	
	

