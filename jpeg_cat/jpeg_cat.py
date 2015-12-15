 
from myhdl import *
 

def jpeg_cat(left_i, sam_i, right_i, flgs_i, update_i, res_o, update_o, clk):
    @always(clk.posedge)
    def rtl ():
        if (update_i == 1):
            update_o.next = 0
            if (flgs_i == 7):
                res_o.next = sam_i - ( (left_i >> 1) + (right_i >> 1) )
            elif (flgs_i == 5):
                res_o.next = sam_i + ( (left_i >> 1) + (right_i >> 1) )
            elif (flgs_i == 6):
                res_o.next = sam_i + ( (left_i + right_i + 2) >> 2 )
            elif (flgs_i == 4):
                res_o.next = sam_i - ( (left_i + right_i + 2) >> 2 )
        else:
            update_o.next = 1
    return rtl    

def jpeg_signals():
    W0 = 9		
    res_o = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
    left_i = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
    right_i = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
    sam_i = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
    flgs_i = Signal(intbv(0)[4:])
    update_i = Signal(bool(0))
    update_o = Signal(bool(0))
    clk = Signal(bool(0))
    return  left_i, right_i, sam_i, flgs_i, update_i, res_o, update_o, clk

def tb(jpeg_cat,left_i, sam_i, right_i, flgs_i, update_i, res_o, update_o, clk):
    instance_jpeg_cat = jpeg_cat(left_i, sam_i, right_i, flgs_i, update_i, res_o, update_o, clk)

    @always(delay(10))
    def clkgen():
        clk.next = not clk

    @instance
    def stimulus():
        update_i.next = 0
        yield clk.posedge
        flgs_i.next = 7
        left_i.next = 164
        right_i.next = 158
        sam_i.next = 160
        yield clk.posedge
        update_i.next = 1
        yield clk.posedge
        update_i.next = 0
        yield clk.posedge
        flgs_i.next = 5
        left_i.next = 164
        right_i.next = 158
        sam_i.next = -1
        yield clk.posedge
        update_i.next = 1
        yield clk.posedge
        update_i.next = 0
        yield clk.posedge

        flgs_i.next = 6
        left_i.next = 164
        right_i.next = 158
        sam_i.next = 160
        yield clk.posedge
        update_i.next = 1
        yield clk.posedge
        update_i.next = 0
        yield clk.posedge
        flgs_i.next = 4
        left_i.next = 164
        right_i.next = 158
        sam_i.next = 241
        yield clk.posedge
        update_i.next = 1
        yield clk.posedge
        update_i.next = 0
        yield clk.posedge
        raise StopSimulation
    return instances()

def convert():
    left_i, sam_i, right_i, flgs_i, update_i, res_o, update_o, clk = jpeg_signals()
    toVerilog(jpeg_cat, left_i, sam_i, right_i, flgs_i, update_i, res_o, update_o, clk) 
'''
convert()
'''
'''
left_i, right_i, sam_i, flgs_i, update_i, res_o, update_o, clk = jpeg_signals()
tb_fsm = traceSignals(tb, jpeg_cat, left_i, sam_i, right_i, flgs_i, update_i, res_o, update_o, clk) 
sim = Simulation(tb_fsm)
sim.run()
''' 

