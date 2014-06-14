from myhdl import *
 
DATA_WIDTH = 262144
d3 = Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))
a2 = Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))
 
x2 = Signal(intbv(164, min = -DATA_WIDTH, max = DATA_WIDTH))
x4 = Signal(intbv(156, min = -DATA_WIDTH, max = DATA_WIDTH))
x3 = Signal(intbv(164, min = -DATA_WIDTH, max = DATA_WIDTH)) 


 
 
 
print bin(x2), bin(x3), bin(x4)


            
def add_shift(d3,a2,x2,x3,x4):
        t1 = intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH)
        t2 = intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH)      
        t3 = intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH)
        @always_comb
        def eq_logic():
                t1 = x2 + x4
                t1 = t1 >> 1
                t2 = x3 - t1
                t1 = x4 >> 2
                t3 = x2 + t1 + t2
                
                d3.next = t2
                a2.next = t3
                 
                 
        return eq_logic
        
d_instance = add_shift(d3,a2,x2,x3,x4)


toVerilog(add_shift,d3,a2,x2,x3,x4)
