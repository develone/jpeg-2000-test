from myhdl import *

class fifo_downstream_interface(object):
    def __init__(self):
        self.rd_en  = Signal(bool(0))
        self.dout    = Signal(intbv(0)[16:])
        self.empty   = Signal(bool(0)) 

#end class fifo_downstream_interface
    
def fifo_down_if_ex(clk_fast, rst, dout, rd_en, empty): #rst is asynch, all other
                                               #signals are synchronous
    @always_seq(clk_fast.posedge, reset=rst)
    def fifo_rd():
        if( empty ==False and rd_en==True):
            dout.next = dout
        #How to assert empty signal???
        #Temporarily tied to 0        
        empty.next = False      
    return fifo_rd

#end function fifo_down_if_ex       
                      
