from myhdl import *
from ram_for_test import *
#from jpeg_constants import *
CONTENT = [
163, 160, 155,
155, 157, 170]
W0 = 8
LVL0 = 2
W1 = 8
LVL1 = 2
W2 = 8
LVL2 = 2
W3 = 5
LVL3 = 2
SIMUL = 1
from array_jpeg import jp_process
clk_fast = Signal(bool(0))
res_out_x = Signal(intbv(0, min= -128 ,max= 128))
update_s = Signal(bool(0))
noupdate_s = Signal(bool(0))

left_s_i = Signal(intbv(0)[LVL2*W2:])
sam_s_i = Signal(intbv(0)[LVL2*W2:])
right_s_i = Signal(intbv(0)[LVL2*W2:])
flgs_s_i = Signal(intbv(0)[LVL3*W3:])
#dut = toVerilog(jp_process, res_out_x, left_s_i,sam_s_i, right_s_i, flgs_s_i, noupdate_s, update_s,  W0=W0, LVL0=LVL0, W1=W1, LVL1=LVL1, W2=W2, LVL2=LVL2, W3=W3, LVL3=LVL3)
#dut = jp_process( res_out_x, left_s_i,sam_s_i, right_s_i, flgs_s_i, noupdate_s, update_s,  W0=W0, LVL0=LVL0, W1=W1, LVL1=LVL1, W2=W2, LVL2=LVL2, W3=W3, LVL3=LVL3)
def tb(clk_fast, res_out_x, left_s_i,sam_s_i, right_s_i, flgs_s_i, noupdate_s, update_s,  W0=W0, LVL0=LVL0, W1=W1, LVL1=LVL1, W2=W2, LVL2=LVL2, W3=W3, LVL3=LVL3):
    instance_ram_lf = ram(dout_lf, din_lf, addr_lf, we_lf, clk_fast)
    instance_ram_sa = ram(dout_sa, din_sa, addr_sa, we_sa, clk_fast)
    instance_ram_rh = ram(dout_rh, din_rh, addr_rh, we_rh, clk_fast)
    instance_ram_flgs = ram(dout_flgs, din_flgs, addr_flgs, we_flgs, clk_fast)
    instance_dut = jp_process( res_out_x, left_s_i,sam_s_i, right_s_i, flgs_s_i, noupdate_s, update_s,  W0=W0, LVL0=LVL0, W1=W1, LVL1=LVL1, W2=W2, LVL2=LVL2, W3=W3, LVL3=LVL3, SIMUL=SIMUL)
    @always(delay(10))
    def clkgen():
        clk_fast.next = not clk_fast
    
    @instance
    def stimulus():
        for i in range(10):
            print("%3d  ") % (now())
            yield clk_fast.posedge
            we_lf.next = 1
            yield clk_fast.posedge
            we_sa.next = 1
            yield clk_fast.posedge
            we_rh.next = 1
            yield clk_fast.posedge
            addr_lf.next = 0
            addr_sa.next = 0
            addr_rh.next = 0
            yield clk_fast.posedge
            for i in range(2):
                din_lf.next = CONTENT[i]
                din_sa.next = CONTENT[i + 1]
                din_rh.next = CONTENT[i + 2]
                addr_lf.next = addr_lf + 1
                addr_sa.next = addr_lf + 1
                addr_rh.next = addr_lf + 1
                yield clk_fast.posedge
            we_lf.next = 0
            we_sa.next = 0
            we_rh.next = 0
            yield clk_fast.posedge
            for i in range(2):
                left_s_i.next = dout_lf << 8
        raise StopSimulation
    
    
    return instances()
    
tb(clk_fast, res_out_x, left_s_i,sam_s_i, right_s_i, flgs_s_i, noupdate_s, update_s,  W0=W0, LVL0=LVL0, W1=W1, LVL1=LVL1, W2=W2, LVL2=LVL2, W3=W3, LVL3=LVL3)
#print dir(tb)
#print tb

tb_fsm = traceSignals(tb, clk_fast, res_out_x, left_s_i,sam_s_i, right_s_i, flgs_s_i, noupdate_s, update_s)
#print tb_fsm
sim = Simulation(tb(clk_fast, res_out_x, left_s_i,sam_s_i, right_s_i, flgs_s_i, noupdate_s, update_s))
sim = Simulation(tb_fsm)
sim.run()