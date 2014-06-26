from myhdl import *
def add_mul_sim(d3,a2,x2,x3,x4,x5,p,odd_even,fwd_res):

	t = fixbv(0, min = -DATA_WIDTH, max = DATA_WIDTH,res=1e-5)
	t1 = fixbv(0, min = -DATA_WIDTH, max = DATA_WIDTH,res=1e-5)
	
	
	if not p:
		
		if odd_even:
			#print 'p = ',p,'odd_even = ',odd_even,'x2 = ',x2,'x3 = ',x3
			ca1 = fixbv(-1.586134342, min = -DATA_WIDTH, max = DATA_WIDTH, res=1e-5)
			ra4 = fixbv(-0.4435068522, min = -DATA_WIDTH, max = DATA_WIDTH, res=1e-5)
			
			if fwd_res:
				t = (x2+x3) * ca1
			else:
				t1 = (x4+x5) * ra4 
		else:
			#print 'p = ',p,'odd_even = ',odd_even,'x4 = ',x4,'x5 = ',x5
			ca2 = fixbv(-0.05298011854, min = -DATA_WIDTH, max = DATA_WIDTH, res=1e-5)
			ra3 = fixbv(-0.8829110762, min = -DATA_WIDTH, max = DATA_WIDTH, res=1e-5)
			if fwd_res:
				t1 = (x4+x5) * ca2
			else:
				t = (x2+x3) * ra3
		d3 = t
		a2 = t1                 
	else:
		 
		if odd_even:
			#print 'p = ',p,'odd_even = ',odd_even,'x2 = ',x2,'x3 = ',x3
			ca3 = fixbv(0.8829110762, min = -DATA_WIDTH, max = DATA_WIDTH, res=1e-5)		
			ra2 = fixbv(0.05298011854, min = -DATA_WIDTH, max = DATA_WIDTH, res=1e-5)		
			if fwd_res:
				t = (x2+x3) * ca3
			else:
				t1 = (x4+x5) * ra2
		else:
			#print 'p = ',p,'odd_even = ',odd_even,'x4 = ',x4,'x5 = ',x5 
			ca4 = fixbv(0.4435068522, min = -DATA_WIDTH, max = DATA_WIDTH, res=1e-5)		
			ra1 = fixbv(1.586134342, min = -DATA_WIDTH, max = DATA_WIDTH, res=1e-5)
			if fwd_res:
				t1 = (x4+x5) * ca4
			else:
				t = (x2+x3) * ra1
		d3 = t
		a2 = t1                 

	                 
	#print d3,a2
	return d3,a2
DATA_WIDTH = 262144
# 9/7 Coefficients:
#a1 = -1.586134342
#a2 = -0.05298011854
#a3 = 0.8829110762
#a4 = 0.4435068522

#d3 = fixbv(0, min = -DATA_WIDTH, max = DATA_WIDTH, res=1e-5)
#a2 = fixbv(0, min = -DATA_WIDTH, max = DATA_WIDTH, res=1e-5)
 

#x2 = fixbv(186, min = -DATA_WIDTH, max = DATA_WIDTH)
#x3 = fixbv(194, min = -DATA_WIDTH, max = DATA_WIDTH) 
#from prev operation
#x4 = fixbv(156, min = -DATA_WIDTH, max = DATA_WIDTH)
#x5 = fixbv(156, min = -DATA_WIDTH, max = DATA_WIDTH)

#odd_even = bool(0) 

#p = bool(0)        

#print p, odd_even, x1,x2,x3,x4,x5        
#d_instance = add_mul_sim(d3,a2,x2,x3,x4,x5,p,odd_even)
#print d_instance

 
