from myhdl import *
#1 3 2 5
#2 4 3 5 
DATA_WIDTH = 262144
d3 = Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))
a2 = Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))
 

x2 = Signal(intbv(156, min = -DATA_WIDTH, max = DATA_WIDTH))
x3 = Signal(intbv(164, min = -DATA_WIDTH, max = DATA_WIDTH)) 
x4 = Signal(intbv(156, min = -DATA_WIDTH, max = DATA_WIDTH))
x5 = Signal(intbv(164, min = -DATA_WIDTH, max = DATA_WIDTH))

 
 
 
print bin(x2), bin(x3), bin(x4), bin(x5)


            
def add_shift(d3,a2,x2,x3,x4,x5):
	t = Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))
	t1 = Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))
	@always_comb
	def eq_logic():
		t = (x2+x4) >> 1
		t = x3 - t	
		t1 = ((x3+x5) >> 2)
		t1 = x4 + t1
	
		d3.next = t
		a2.next = t1
                 
                 
	return eq_logic
        
d_instance = add_shift(d3,a2,x2,x3,x4,x5)


toVerilog(add_shift,d3,a2,x2,x3,x4,x5)
