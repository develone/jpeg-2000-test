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
pc_data_in = Signal(intbv(0)[2:])
pc_data_rdy = Signal(intbv(0)[2:])

data_pc_in  = Signal(bool(0))
datactn_in = Signal(intbv(0)[8:])
datactn = Signal(intbv(0)[8:])


def pc_read(clk, data_in, toLift_Step, we_in, addr_in, muxsel_i,datactn_in, datactn, pc_data_in, pc_data_rdy ):
    @always(clk.posedge)
    def readlogic():
        if( muxsel_i == 1):
            if (addr_in <= 254):
                we_in.next = 1
                data_in.next = toLift_Step
                datactn_in.next = datactn 
                addr_in.next = addr_in + 1
    @always_comb
    def rtl():
        pc_data_in.next = pc_data_rdy
    @always(clk.posedge)
    def rtl1():
        if(muxsel_i == 0):
            if (pc_data_in.next == 3):
                muxsel_i.next = 1
            else:
                if (pc_data_in.next == 2):
                    muxsel_i.next = 0
                    
    return readlogic, rtl, rtl1
 
def tb(clk, data_in, toLift_Step, we_in, addr_in, muxsel_i, datactn_in, datactn ):
    instance_pc_read = pc_read(clk, data_in, toLift_Step, we_in, addr_in, muxsel_i,datactn_in, datactn, pc_data_in, pc_data_rdy   )
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
        for i in range(100):
            print ("%d wr %d addr %d ") % (now(), we_in, addr_in)
            yield clk.posedge
            toLift_Step.next = i
            yield clk.posedge
            print ("%d data %d addr %d ") % (now(), data_in, addr_in)
        raise StopSimulation
    return instances()
tb_fsm = traceSignals( tb, clk, data_in, toLift_Step, we_in, addr_in, muxsel_i, datactn_in, datactn  )
sim = Simulation(tb_fsm)
sim.run()
#toVHDL(pc_read, clk, data_in, toLift_Step, we_in, addr_in, muxsel_i, datactn_in, datactn, pc_data_in, pc_data_rdy ) 
