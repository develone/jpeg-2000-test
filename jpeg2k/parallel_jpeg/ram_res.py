from myhdl import *
from jpeg_constants import *
def ram_res(dout_res, din_res, addr_res, we_res, clk_fast, depth=512):
    """  Ram model """

    mem = [Signal(intbv(0)[W0:]) for i in range(depth)]

    @always(clk_fast.posedge)
    def write():
        if we_res:
            mem[addr_res].next = din_res

    @always_comb
    def read():
        dout_res.next = mem[addr_res]

    return write, read


dout_res = Signal(intbv(0)[W0:])
#dout_v = Signal(intbv(0)[LVL2*W2:])
din_res = Signal(intbv(0)[W0:])
addr_res = Signal(intbv(0)[10:])
we_res = Signal(bool(0))
clk_fast = Signal(bool(0))

def main():
    #toVerilog.name = 'ram_1'
    toVerilog(ram_res, dout_res, din_res, addr_res, we_res, clk_fast)
    toVHDL(ram_res, dout_res, din_res, addr_res, we_res, clk_fast)

if __name__ == '__main__':
    main()
