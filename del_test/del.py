from myhdl import *
DATA_WIDTH = 32768
left_s = Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))
res_s = Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))
delay_s = Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))
clk_fast = Signal(bool(0))
def del_test(clk_fast, left_s, delay_s, res_s):
    @always(clk_fast.posedge)
    def hdl():
        res_s.next = left_s + 1
    return hdl
toVerilog(del_test, clk_fast, left_s, delay_s, res_s)
toVHDL(del_test, clk_fast, left_s, delay_s, res_s)