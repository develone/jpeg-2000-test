from myhdl import *

 


class Add_Mul_Sim(object):

	def __init__(self):
		ww = (31,10)
		self.even_odd = (bool(0))
		self.fwd_inv = (bool(0))
		self.p = (bool(0))
		self.left = (fixbv(0)[ww])
		self.right = (fixbv(0)[ww])
 		self._even = (fixbv(0)[ww])
                self._odd = (fixbv(0)[ww])
 		self.ca1 = fixbv(-1.586134342)[ww]
        	self.ra4 = fixbv(-0.4435068522)[ww]
		self.ca2 = fixbv(-0.05298011854)[ww]
        	self.ra3 = fixbv(-0.8829110762)[ww]
        	self.ca3 = fixbv(0.8829110762)[ww]
        	self.ra2 = fixbv(0.05298011854)[ww]
		self.ca4 = fixbv(0.4435068522)[ww]
		self.ra1 = fixbv(1.586134342)[ww]
 
	def setSig__odd(self,val):   
		ww = (31,10)
		self._odd = (fixbv(val)[ww])
		
	def get__odd(self):
		return self._odd

	def setSig__even(self,val):   
		ww = (31,10)
		self._even = (fixbv(val)[ww])
		
	def get__even(self):
		return self._even
 
	def setSig_left(self,val):   
		ww = (31,10)
		self.left = (fixbv(val)[ww])
        
	def get_left(self):
		return self.left
	
	def setSig_right(self,val):   
		ww = (31,10)
		self.right = (fixbv(val)[ww])

	def get_right(self):
		return self.right
 
	def setSig_even_odd(self,val):   
		self.even_odd = (bool(val))

	def setSig_fwd_inv(self,val):   
		self.fwd_inv = (bool(val))
	
	def setSig_p(self,val):   
		self.p = (bool(val))

	def add_mul(self):
 
		if not self.p:
 
			if self.even_odd: 
				if self.fwd_inv:
					self._even = (self.left + self.right)*self.ca2
                        	else:
					self._even = (self.left + self.right)*self.ra4			 
			else:
				if self.fwd_inv:
					self._odd = (self.left + self.right)*self.ca1
				else:
					self._odd = (self.left + self.right)*self.ra3
				 
		else:
 
 			if self.even_odd:
				if self.fwd_inv:
					self._even = (self.left + self.right)*self.ca4
				else:
					self._even = (self.left + self.right)*self.ra2
				 
			else:
				if self.fwd_inv:
					self._odd = (self.left + self.right)*self.ca3
				 
				else:
					self._odd = (self.left + self.right)*self.ra1
		 	
        	return self._even, self._odd 
 
