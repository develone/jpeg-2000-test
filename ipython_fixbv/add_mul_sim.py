from myhdl import *
def add_mul_sim(d3,a2,x2,x3,x4,x5,p,odd_even):


	t = fixbv(0, min = -DATA_WIDTH, max = DATA_WIDTH,res=1e-5)
	t1 = fixbv(0, min = -DATA_WIDTH, max = DATA_WIDTH,res=1e-5)
	
	
	if not p:
		
		if odd_even:
			ca1 = fixbv(-1.586134342, min = -DATA_WIDTH, max = DATA_WIDTH, res=1e-5)
			t = (x2+x3) * ca1
		else: 
			ca2 = fixbv(-0.05298011854, min = -DATA_WIDTH, max = DATA_WIDTH, res=1e-5)
			t1 = (x4+x5) * ca2					
		d3 = t
		a2 = t1                 
	else:
		 
		if odd_even:
			ca3 = fixbv(0.8829110762, min = -DATA_WIDTH, max = DATA_WIDTH, res=1e-5)
			t = (x2+x3) * ca3
		else: 
			ca4 = fixbv(0.4435068522, min = -DATA_WIDTH, max = DATA_WIDTH, res=1e-5)
			t1 = (x4+x5) * ca4                 
 		d3 = t
		a2 = t1                 
                
	return t,t1
DATA_WIDTH = 262144
# 9/7 Coefficients:
#a1 = -1.586134342
#a2 = -0.05298011854
#a3 = 0.8829110762
#a4 = 0.4435068522

d3 = fixbv(0, min = -DATA_WIDTH, max = DATA_WIDTH, res=1e-5)
a2 = fixbv(0, min = -DATA_WIDTH, max = DATA_WIDTH, res=1e-5)
 

x2 = fixbv(186, min = -DATA_WIDTH, max = DATA_WIDTH)
x3 = fixbv(194, min = -DATA_WIDTH, max = DATA_WIDTH) 
#from prev operation
x4 = fixbv(156, min = -DATA_WIDTH, max = DATA_WIDTH)
x5 = fixbv(156, min = -DATA_WIDTH, max = DATA_WIDTH)

odd_even = bool(0) 

p = bool(0)        

#print p, odd_even, x1,x2,x3,x4,x5        
d_instance = add_mul_sim(d3,a2,x2,x3,x4,x5,p,odd_even)
print d_instance

 
