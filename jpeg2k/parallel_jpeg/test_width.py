from myhdl import *
JPEG_DATA_WIDTH = 1024
dataout = Signal(intbv(0)[9:])
res0_s = Signal(intbv(0, min = -JPEG_DATA_WIDTH, max = JPEG_DATA_WIDTH))
res1_s = Signal(intbv(0, min = -JPEG_DATA_WIDTH, max = JPEG_DATA_WIDTH))
clk_fast = Signal(bool(0))
#488 1E8 1E9 with int
def test_res_back(clk_fast, dataout, res1_s):
    @always(clk_fast.posedge)
    def rtl():
        res1_s.next = dataout
    return rtl
def test_res(clk_fast, dataout, res0_s):
    @always(clk_fast.posedge)
    def rtl():
        dataout.next = (res0_s)
    return rtl
def tb(clk_fast, dataout, res0_s):
    instance_1 = test_res(clk_fast, dataout, res0_s)
    instance_2 = test_res_back(clk_fast, dataout, res1_s)
    @always(delay(10))
    def clkgen():
        clk_fast.next = not clk_fast
    @instance
    def stimulus():
        for i in range(511,0, -1):
            res0_s.next = i
            dataout.next = i
            yield clk_fast.posedge
            print("%3d %d %s %d %s %d %s ") % (now(), i, bin(res0_s,11), res0_s, bin(dataout,9), dataout, bin(res1_s,11))
        for ii in range(0, 511, 1):
            res0_s.next = ii
            yield clk_fast.posedge
            print("%3d %d %s %d %s %d %s") % (now(), ii, bin(res0_s,11), res0_s, bin(dataout,9), dataout, bin(res1_s,11))
        raise StopSimulation
    return instance_1, instance_2, stimulus, clkgen
toVHDL(test_res, clk_fast, dataout, res0_s)
toVHDL(test_res_back, clk_fast, dataout, res1_s)

tb_fsm = traceSignals(tb, clk_fast, dataout, res0_s)
#sim = Simulation(tb, clk_fast, dataout, res0_s)
sim = Simulation(tb_fsm)
sim.run()