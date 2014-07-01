from myhdl import *




DATA_WIDTH =  262144
# 9/7 Coefficients:
#a1 = -1.586134342
#a2 = -0.05298011854
#a3 = 0.8829110762
#a4 = 0.4435068522


         
def add_mul(d3,a2,clk,x2,x3,x4,x5,p,even_odd,fwd_inv):
		 
	@always(clk.posedge)
	def rtl():

		if not p:
		
			if even_odd:			
				if fwd_inv:
					ca1 = fixbv(-1.586134342)[ww]
					t = fixbv(0)[ww]
	
					t = (x2+x3) * ca1
					d3.next = t			
				else:
					ra4 = fixbv(-0.4435068522)[ww]
					t1 = fixbv(0)[ww]
					 
					t1 = (x4+x5) * ra4 				
					a2.next = t1	
			else:				
				if fwd_inv:
					ca2 = fixbv(-0.05298011854)[ww]
					t1 = fixbv(0)[ww]
					 
					t1 = (x4+x5) * ca2
					a2.next = t1
					
				else:
					ra3 = fixbv(-0.8829110762)[ww]
					t = fixbv(0)[ww]
					
					t = (x2+x3) * ra3
					d3.next = t							  					          
		else:
			if even_odd:
				if fwd_inv:
					ca3 = fixbv(0.8829110762)[ww]
					t = fixbv(0)[ww]
					
					t = (x2+x3) * ca3
					d3.next = t
				else:
					ra2 = fixbv(0.05298011854)[ww]
					t1 = fixbv(0)[ww]
					t1 = (x4+x5) * ra2
					a2.next = t1			 
			else: 
				if fwd_inv:
					ca4 = fixbv(0.4435068522)[ww]
					t1 = fixbv(0)[ww]
					t1 = (x4+x5) * ca4
					a2.next = t1
				else:
					ra1 = fixbv(1.586134342)[ww]
					t = fixbv(0)[ww]
					
					t = (x2+x3) * ra1
					d3.next = t
					                 
		print hex(d3), d3,  hex(a2), a2 
                 
	return rtl
        
def testbench():
	p = Signal(bool(0))
	even_odd = Signal(bool(0))
	fwd_inv = Signal(bool(0))
	clk = Signal(bool(0))

	d3 = Signal(fixbv(0)[ww])
	a2 = Signal(fixbv(0)[ww])
 
	x2 = Signal(fixbv(156)[ww])
	x3 = Signal(fixbv(164)[ww]) 
	#from prev operation
	x4 = Signal(fixbv(156)[ww])
	x5 = Signal(fixbv(156)[ww])	 
	
	d_instance = add_mul(d3,a2,clk,x2,x3,x4,x5,p,even_odd,fwd_inv)
	print d_instance 
	print type(d_instance)
	@always(delay(10))
	def clkgen():
		clk.next = not clk
	
	@instance
	def stimulus():
		for i in range(3):
			yield clk.posedge
		for n in (12, 8, 8, 4):
			even_odd.next = 1
			fwd_inv.next = 1
			p.next = 1
			x2.next = 80
			x3.next = 100
			x4.next = 200
			x5.next = 132
			for i in range(5):
				yield clk.posedge
			even_odd.next = 0


			x4.next = 210
			x5.next = 142

			for i in range(3):
				yield clk.posedge
			fwd_inv.next = 0
			for i in range(2):
				yield clk.posedge
			p.next = 0
			x2.next = 90
			x3.next = 110
			for i in range(n-1):
				yield clk.posedge
		raise StopSimulation
	return d_instance, clkgen, stimulus


#toVerilog(add_mul,d3,a2,clk,x2,x3,x4,x5,p,even_odd,fwd_inv)
#toVHDL(add_mul,d3,a2,clk,x2,x3,x4,x5,p,even_odd,fwd_inv)
ww = (26,18)
tb_fsm = traceSignals(testbench)
sim = Simulation(tb_fsm)
sim.run()
