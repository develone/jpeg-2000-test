#testbench for fifo_up_if

from myhdl import *
import fifo_down_if
import fifo_up_if

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
def test():
    clk_fast = Signal(bool(0))
    rst = ResetSignal(0,active=1,async=True) #Xilinx spec didn't mention
                                             #specifically about reset
                                             #polarity
                                             
    up_interface = fifo_up_if.fifo_upstream_interface() #defining signals for the fifo
                                             #upstream interface
    def _test():
        #instantiating dut
        dut = fifo_up_if.fifo_up_if_ex(clk_fast,
                            rst,
                            up_interface.din,
                            up_interface.wr_en,
                            up_interface.full
                            )
                        
        @always(delay(5))
        def clk_fast_driver():
            clk_fast.next = not clk_fast
        
        
        @instance
        def tb_stim():
            rst.next = rst.active
            yield delay(20)
            rst.next = not rst.active
            yield delay(20)
            yield clk_fast.posedge
            
            for i in range(50):
                up_interface.wr_en.next = True
                up_interface.din.next = i
                yield clk_fast.posedge
                up_interface.wr_en.next = False
                yield clk_fast.posedge    
	    
	    raise StopSimulation	
        
        return dut, clk_fast_driver, tb_stim

    #Simulation(traceSignals(_test)).run()
clk_fast = Signal(bool(0))
rst = ResetSignal(0,active=1,async=True)
up_interface = fifo_up_if.fifo_upstream_interface()
dn_interface = fifo_down_if.fifo_downstream_interface()

#up_interface = fifo_upstream_interface()
#dn_interface = fifo_downstream_interface()
#toVerilog(fifo_up_if.fifo_up_if_ex,clk_fast,rst,up_interface.din,up_interface.wr_en,up_interface.full)
                                                              
#toVHDL(fifo_up_if.fifo_up_if_ex,clk_fast,rst,up_interface.din,up_interface.wr_en,up_interface.full)        
#toVHDL(fifo_down_if.fifo_down_if_ex,clk_fast, rst, dn_interface.dout, dn_interface.rd_en, dn_interface.empty)                                
    
#def fifos(clk_fast,rst,up_interface.din,up_interface_wr.en,up_interface.full, dn_interface.dout, dn_interface.rd_en
 #         , dn_interface.empty):
 #   instance_13 = fifo_up_if_ex(clk_fast,rst,up_interface.din,up_interface_wr.en,up_interface.full)
 #   instance_14 = fifo_down_if_ex(clk_fast, rst, dn_interface.dout, dn_interface.rd_en, dn_interface.empty)
 #   return instance_13, instance_14
#toVHDL(fifos, clk_fast, up_interface.din,up_interface.wr_en,up_interface.full, dn_interface.dout, dn_interface.rd_en, dn_interface.empty)
instance_13 = fifo_up_if_ex(clk_fast,rst,up_interface.din,up_interface.wr_en,up_interface.full)        
instance_14 = fifo_down_if_ex(clk_fast, rst, dn_interface.dout, dn_interface.rd_en, dn_interface.empty)
#print instance_13, instance_14
def fifos():
    #print instance_13, instance_14
    instance_13 = fifo_up_if_ex(clk_fast,rst,up_interface.din,up_interface.wr_en,up_interface.full)        
    instance_14 = fifo_down_if_ex(clk_fast, rst, dn_interface.dout, dn_interface.rd_en, dn_interface.empty)
    print instance_13, instance_14
    return instance_13, instance_14
#inst_pr(instance_13, instance_14)
#toVHDL(fifo_up_if_ex, clk_fast,rst,up_interface.din,up_interface.wr_en,up_interface.full)
#toVHDL(fifo_down_if_ex,clk_fast, rst, dn_interface.dout, dn_interface.rd_en, dn_interface.empty)
#toVHDL(fifos)  
#toVHDL(clk_fast,rst,up_interface.din,up_interface.wr_en,up_interface.full)        
#toVerilog(fifo_down_if_ex,clk_fast, rst, dn_interface.dout, dn_interface.rd_en, dn_interface.empty)   
#if __name__ == "__main__":
#    test()
                
        