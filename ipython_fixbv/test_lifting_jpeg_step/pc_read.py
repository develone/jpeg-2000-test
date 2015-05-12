from myhdl import *

W0 = 9
data_in = Signal(intbv(0)[W0:])
'''toLift_Step used for mapping datatodut
from usb hostio
datatodut is an alias of toSub_s
datactn used for mapping datactn
from usb hostio
datactn is an alias of toSub_s
'''
toLift_Step = Signal(intbv(0)[W0:])
we_in = Signal(bool(0))
addr_in = Signal(intbv(0)[8:])
muxsel_i = Signal(bool(0))
clk = Signal(bool(0))
'''data from usb hostio'''
pc_data_rdy  = Signal(bool(0))
data_pc_in  = Signal(bool(0))
datactn_in = Signal(intbv(0)[8:])
datactn = Signal(intbv(0)[8:])
status_i = Signal(intbv(0)[2:])

def pc_read(clk, data_in, toLift_Step, we_in, addr_in, muxsel_i,datactn_in, datactn ):
    @always(clk.posedge)
    def readlogic():
        if( muxsel_i == 1):
            if (addr_in <= 256):
                we_in.next = 1
                data_in.next = toLift_Step
                datactn_in.next = datactn 
                addr_in.next = addr_in + 1
                 
    return readlogic
def detect_data_from_pc(status_i, datapush):
    @always_comb
    def rtl():
        if (datapush == 0):
            status_i.next = 3
        else:
            status_i.next = 0
    return rtl
def tb(clk, data_in, toLift_Step, we_in, addr_in, muxsel_i, datactn_in, datactn ):
    instance_pc_read = pc_read(clk, data_in, toLift_Step, we_in, addr_in, muxsel_i, datactn_in, datactn  )
    @always(delay(10))
    def clkgen():
        clk.next = not clk
    @instance
    def stimulus():
        for i in range(10):
            print( "%3d ") % (now())
            yield clk.posedge
        muxsel_i.next = 0
        yield clk.posedge
        
        addr_in.next = 0
        yield clk.posedge
        we_in.next = 1
        yield clk.posedge        

        muxsel_i.next = 1
        yield clk.posedge
        for i in range(255):
            yield clk.posedge
        raise StopSimulation
    return instances()
#tb_fsm = traceSignals( tb, clk, data_in, toLift_Step, we_in, addr_in, muxsel_i, datactn_in, datactn  )
#sim = Simulation(tb_fsm)
#sim.run()
toVHDL(pc_read, clk, data_in, toLift_Step, we_in, addr_in, muxsel_i,datactn_in, datactn ) 
