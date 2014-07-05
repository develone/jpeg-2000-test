#http://dev.myhdl.org/
from myhdl import *
#d3 d3
#a2 a2
 
#x2 x2,x2_1,x2_2,x2_3
#x3 x3,x3_1,x3_2,x3_3
#from prev operation
#x4 x4,x4_1,x4_2,x4_3
#x5 x5,x5_1,x5_2,x5_3
def set_ctl():
	
	""" Configuring single signals """
	fwd_inv = Signal(bool(False))
	even_odd = Signal(bool(False))
	p = Signal(bool(False))
	clk = Signal(bool(False))
	return fwd_inv, even_odd,p,clk

class Mult_sig_top(object):
	
	def __init__(self):
		ww = (26,18)
		self.x2 = Signal(fixbv(0)[ww])
		self.x3 = Signal(fixbv(0)[ww])
		self.x4 = Signal(fixbv(0)[ww])
		self.x5 = Signal(fixbv(0)[ww])
		
		self.x2_1 = Signal(fixbv(0)[ww])
		self.x3_1 = Signal(fixbv(0)[ww])
		self.x4_1 = Signal(fixbv(0)[ww])
		self.x5_1 = Signal(fixbv(0)[ww])
		
		self.x2_2 = Signal(fixbv(0)[ww])
		self.x3_2 = Signal(fixbv(0)[ww])
		self.x4_2 = Signal(fixbv(0)[ww])
		self.x5_2 = Signal(fixbv(0)[ww])

		self.x2_3 = Signal(fixbv(0)[ww])
		self.x3_3 = Signal(fixbv(0)[ww])
		self.x4_3 = Signal(fixbv(0)[ww])
		self.x5_3 = Signal(fixbv(0)[ww])

		self.d3 = Signal(fixbv(0)[ww])
		self.a2 = Signal(fixbv(0)[ww])
		self.d3_1 = Signal(fixbv(0)[ww])
		self.a2_1 = Signal(fixbv(0)[ww])
		self.d3_2 = Signal(fixbv(0)[ww])
		self.a2_2 = Signal(fixbv(0)[ww])
		self.d3_3 = Signal(fixbv(0)[ww])
		self.a2_3 = Signal(fixbv(0)[ww])
		
	"""Display variables x2,x3,x4,x5,d3, and a1"""
	
	def disSig_x2(self):
		print "Signal x2: ", self.x2
	def disSig_x4(self):
		print "Signal x4: ", self.x4
	def disSig_d3(self):
		print "Signal d3: ", self.d3
	def disSig_x3(self):
		print "Signal x3: ", self.x3
	def disSig_x5(self):
		print "Signal x5: ", self.x5
	def disSig_a2(self):
		print "Signal a2: ", self.a2	
				
	"""Set variables x2,x3,x4,x5"""
	
	def setSig_x2(self,val): 
		ww = (26,18)   
		self.x2.next = Signal(fixbv(val)[ww]) 
	def setSig_x3(self,val):
		ww = (26,18)    
		self.x3.next = Signal(fixbv(val)[ww])
	def setSig_x4(self,val): 
		ww = (26,18)   
		self.x4.next = Signal(fixbv(val)[ww]) 
	def setSig_x5(self,val):
		ww = (26,18)    
		self.x5.next = Signal(fixbv(val)[ww])		     

	def setSig_x2_1(self,val): 
		ww = (26,18)   
		self.x2_1.next = Signal(fixbv(val)[ww]) 
	def setSig_x3_1(self,val):
		ww = (26,18)    
		self.x3_1.next = Signal(fixbv(val)[ww])
	def setSig_x4_1(self,val): 
		ww = (26,18)   
		self.x4_1.next = Signal(fixbv(val)[ww]) 
	def setSig_x5_1(self,val):
		ww = (26,18)    
		self.x5_1.next = Signal(fixbv(val)[ww])
	
	def setSig_x2_2(self,val): 
		ww = (26,18)   
		self.x2_2.next = Signal(fixbv(val)[ww]) 
	def setSig_x3_2(self,val):
		ww = (26,18)    
		self.x3_2.next = Signal(fixbv(val)[ww])
	def setSig_x4_2(self,val): 
		ww = (26,18)   
		self.x4_2.next = Signal(fixbv(val)[ww]) 
	def setSig_x5_2(self,val):
		ww = (26,18)    
		self.x5_2.next = Signal(fixbv(val)[ww])
	
	def setSig_x2_3(self,val): 
		ww = (26,18)   
		self.x2_3.next = Signal(fixbv(val)[ww]) 
	def setSig_x3_3(self,val):
		ww = (26,18)    
		self.x3_3.next = Signal(fixbv(val)[ww])
	def setSig_x4_3(self,val): 
		ww = (26,18)   
		self.x4_3.next = Signal(fixbv(val)[ww]) 
	def setSig_x5_3(self,val):
		ww = (26,18)    
		self.x5_3.next = Signal(fixbv(val)[ww])
					
	"""Get variables d3,d3_1,d3_2,d3_3
	Get variables a2,a2_1,a2_2,a2_3"""
    
	def get_d3(self):
		return self.d3
	def get_d3_1(self):
		return self.d3_1			     
	def get_d3_2(self):
		return self.d3_2
	def get_d3_3(self):
		return self.d3_3
	def get_a2(self):
		return self.a2
	def get_a2_1(self):
		return self.a2_1			     
	def get_a2_2(self):
		return self.a2_2
	def get_a2_3(self):
		return self.a2_3
		
def mult_mul_add(clk, p, even_odd, fwd_inv, pix):
	ww = (26,18)
	ca1 = fixbv(-1.586134342)[ww]
	ca2 = fixbv(-0.05298011854)[ww]
	ca3 = fixbv(0.8829110762)[ww]
	ca4 = fixbv(0.4435068522)[ww]
	ra1 = fixbv(1.586134342)[ww]
	ra2 = fixbv(0.05298011854)[ww]
	ra3 = fixbv(-0.8829110762)[ww]
	ra4 = fixbv(-0.4435068522)[ww]
	@always(clk.posedge)
	def hdl():
		
		
		if not p:
			if even_odd:
				
				if fwd_inv:
					"""p false 1st pass even_odd True fwd_inv True (x2+x3) * ca1 """
					pix.d3.next = (pix.x2 + pix.x3)*ca1
					pix.d3_1.next = (pix.x2_1 + pix.x3_1)*ca1
					pix.d3_2.next = (pix.x2_2 + pix.x3_2)*ca1
					pix.d3_3.next = (pix.x2_2 + pix.x3_2)*ca1
				else:
					"""p false 1st pass even_odd True fwd_inv False (x4+x5) * ra4 """	
					pix.a2.next = (pix.x4 + pix.x5)*ra4
					pix.a2_1.next = (pix.x4_1 + pix.x5_1)*ra4
					pix.a2_2.next = (pix.x4_2 + pix.x5_2)*ra4
					pix.a2_3.next = (pix.x4_3 + pix.x5_3)*ra4
			else:
					
				if fwd_inv:
					"""p false 1st pass even_odd false fwd_inv True (x4+x5) * ca2 """
					pix.a2.next = (pix.x4 + pix.x5)*ca2
					pix.a2_1.next = (pix.x4_1 + pix.x5_1)*ca2
					pix.a2_2.next = (pix.x4_2 + pix.x5_2)*ca2
					pix.a2_3.next = (pix.x4_3 + pix.x5_3)*ca2
				else:
					"""p false 1st pass even_odd false fwd_inv False (x2+x3) * ra3 """
					pix.d3.next = (pix.x2 + pix.x3)*ra3	 
					pix.d3_1.next = (pix.x2_1 + pix.x3_1)*ra3	 
					pix.d3_2.next = (pix.x2_2 + pix.x3_2)*ra3	 
					pix.d3_3.next = (pix.x2_2 + pix.x3_3)*ra3	 
		else:
			if even_odd:
				if fwd_inv:
					"""p True 2nd pass even_odd True fwd_inv True (x2+x3) * ca3 """
					pix.d3.next = (pix.x2 + pix.x3)*ca3
					pix.d3_1.next = (pix.x2_1 + pix.x3_1)*ca3
					pix.d3_2.next = (pix.x2_2 + pix.x3_2)*ca3
					pix.d3_3.next = (pix.x2_3 + pix.x3_3)*ca3
				else:
					"""p True 2nd pass even_odd True fwd_inv False (x4+x5) * ra2 """
					pix.a2.next = (pix.x4 + pix.x5)*ra2
					pix.a2_1.next = (pix.x4_1 + pix.x5_1)*ra2
					pix.a2_2.next = (pix.x4_2 + pix.x5_2)*ra2
					pix.a2_3.next = (pix.x4_3 + pix.x5_3)*ra2

			else:
		
				if fwd_inv:
					"""p True 2nd pass even_odd False fwd_inv True (x4+x5) * ca4 """
					pix.a2.next = (pix.x4 + pix.x5)*ca4
					pix.a2_1.next = (pix.x4_1 + pix.x5_1)*ca4
					pix.a2_2.next = (pix.x4_2 + pix.x5_2)*ca4
					pix.a2_3.next = (pix.x4_3 + pix.x5_3)*ca4
				else:
					"""p True 2nd pass even_odd False fwd_inv False (x2+x3) * ra1 """
					pix.d3.next = (pix.x2 + pix.x3)*ra1
					pix.d3_1.next = (pix.x2_1 + pix.x3_1)*ra1
					pix.d3_2.next = (pix.x2_2 + pix.x3_2)*ra1
					pix.d3_3.next = (pix.x2_3 + pix.x3_3)*ra1
	
	return hdl

def testbench():
	fwd_inv, even_odd, p, clk = set_ctl()
	pix = Mult_sig_top()
	
	d_instance = mult_mul_add( clk, p,even_odd, fwd_inv, pix)
   
	
	
	
	@always(delay(10))
	def clkgen():
		clk.next = not clk
	
	@instance
	def stimulus():
		for i in range(3):
			yield clk.posedge
		for n in (18, 8, 8, 4):
			even_odd.next = True
			fwd_inv.next = True
			p.next = True
			pix.setSig_x2(100)
			pix.setSig_x3(110)
			pix.setSig_x4(120)
			pix.setSig_x5(130)

			pix.setSig_x2_1(100)
			pix.setSig_x3_1(110)
			pix.setSig_x4_1(120)
			pix.setSig_x5_1(130)

			pix.setSig_x2_2(100)
			pix.setSig_x3_2(110)
			pix.setSig_x4_2(120)
			pix.setSig_x5_2(130)
			
			pix.setSig_x2_3(100)
			pix.setSig_x3_3(110)
			pix.setSig_x4_3(120)
			pix.setSig_x5_3(130)
  			
    
			for i in range(2):
				yield clk.posedge
				
				pix.setSig_x2(101)
				pix.setSig_x3(111)
				pix.setSig_x4(121)
				pix.setSig_x5(131)
				
				pix.setSig_x2_1(101)
				pix.setSig_x3_1(111)
				pix.setSig_x4_1(121)
				pix.setSig_x5_1(131)

				
  
			for i in range(3):
				yield clk.posedge
				even_odd.next = False
				pix.setSig_x2(102)
				pix.setSig_x3(112)
				pix.setSig_x4(122)
				pix.setSig_x5(132)
				
				pix.setSig_x2_1(102)
				pix.setSig_x3_1(112)
				pix.setSig_x4_1(122)
				pix.setSig_x5_1(132)

 
			fwd_inv.next = False
			for i in range(2):
				yield clk.posedge
				p.next = False
	 
			for i in range(n-1):
				yield clk.posedge
		raise StopSimulation
	return d_instance, clkgen, stimulus



def convert(ver,both=False):
	fwd_inv, even_odd, p, clk = set_ctl()
	pix = Mult_sig_top()
	pix.disSig_x2()
	pix.disSig_x3()
	pix.disSig_x4()
	pix.disSig_x5()
	pix.disSig_d3()
	pix.disSig_a2()

	pix.setSig_x2(140)
	pix.disSig_x2()
	pix.setSig_x3(120)
	pix.disSig_x3()

	pix.setSig_x4(160)
	pix.disSig_x4()
	pix.setSig_x5(130)
	pix.disSig_x5()
	
	if ver:
		toVerilog(mult_mul_add, clk, p, even_odd,fwd_inv, pix)
		if both:
			toVHDL(mult_mul_add, clk, p,even_odd, fwd_inv, pix)
		else:
			toVHDL(mult_mul_add, clk, p,even_odd, fwd_inv, pix)
fwd_inv, even_odd, p, clk = set_ctl()


convert(1,1)


tb_fsm = traceSignals(testbench)
sim = Simulation(tb_fsm)
sim.run()
