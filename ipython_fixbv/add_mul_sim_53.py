from myhdl import *
import math
 


class Add_mul_top(object):
	
	def __init__(self):
		DATA_WIDTH = 4194304 
		self.even_odd = (bool(0))
		self.fwd_inv = (bool(0))
		self.p = (bool(0))
		self.left = 0
		self.right = 0
		self.sam = 0
 
		self.din_odd = 0
 

		self.din_even = 0
 
 

 

 

 	def setSig_left(self,val): 
		DATA_WIDTH = 4194304  
		self.left = 0	
	
	def setSig_right(self,val): 
		DATA_WIDTH = 4194304  
		self.right = 0
	def setSig_sam(self,val): 
		DATA_WIDTH = 4194304  
		self.sam = 0	
		
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
				"""p False even_odd True fwd_inv True #1"""
				pix.din_even = pix.sam - math.floor(((pix.left>>1) + (pix.right>>1)))
			else:
				"""p False even_odd True fwd_inv False #1"""
				pix.din_even = pix.sam + math.floor(((pix.left>>1) + (pix.right>>1)))
				
				 
		else:
			if pix.fwd_inv:
				"""p False even_odd False fwd_inv True #2"""
				pix.din_odd = pix.sam + math.floor(((pix.left + pix.right + 2)>>2))
				 
			else:
				"""p False even_odd False fwd_inv False #2"""
				pix.din_odd = pix.sam - math.floor(((pix.left + pix.right + 2)>>2))
		
				 
	else:
 
 		if pix.even_odd:
			if pix.fwd_inv:
				"""p True even_odd True fwd_inv True #3"""
				pix.din_even = pix.sam - math.floor(((pix.left>>1) + (pix.right>>1)))
				 
			else:
				"""p True even_odd True fwd_inv False #3"""
				pix.din_even = pix.sam + math.floor(((pix.left>>1) + (pix.right>>1)))
					
		else:
			if pix.fwd_inv:
				"""p True even_odd False fwd_inv True #4"""
				pix.din_odd = pix.sam + math.floor(((pix.left + pix.right + 2)>>2))
				 
			else:
				"""p True even_odd False fwd_inv False #4"""
				pix.din_odd = pix.sam - math.floor(((pix.left + pix.right + 2)>>2))	 		
			
	
	return pix.din_even, pix.din_odd 
	
	

