from myhdl import *

class fifo_upstream_interface(object):
    def __init__(self):
        self.wr_en  = Signal(bool(0))
        self.din    = Signal(intbv(0)[16:])
        #self.wr_clk_fast = Signal(bool(0))
        self.full   = Signal(bool(0)) 
        #self.rst    = Signal(bool(0))

#end class fifo_upstream_interface
    
def fifo_up_if_ex(clk_fast, rst, din, wr_en, full): #rst is asynch, all other
                                               #signals are synchronous
    @always_seq(clk_fast.posedge, reset=rst)
    def fifo_wr():
        if( full==False and wr_en==True):
            din.next = din
        #How to assert full signal???
        #Temporarily tied to 0        
        full.next = False      
    return fifo_wr

#end function fifo_up_if_ex       
                      
