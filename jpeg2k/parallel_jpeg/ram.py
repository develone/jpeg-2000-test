from myhdl import *
from jpeg_constants import *
def ram(dout, din, addr, we, clk_fast, depth=512):
    """  Ram model """

    mem = [Signal(intbv(0)[LVL2*W2:]) for i in range(depth)]

    @always(clk_fast.posedge)
    def write():
        if we:
            mem[addr].next = din

    @always_comb
    def read():
        dout.next = mem[addr]

    return write, read


dout = Signal(intbv(0)[LVL2*W2:])
#dout_v = Signal(intbv(0)[LVL2*W2:])
din = Signal(intbv(0)[LVL2*W2:])
addr = Signal(intbv(0)[10:])
we = Signal(bool(0))
clk_fast = Signal(bool(0))

def main():
    #toVerilog.name = 'ram_1'
    toVerilog(ram, dout, din, addr, we, clk_fast)
    toVHDL(ram, dout, din, addr, we, clk_fast)

if __name__ == '__main__':
    main()
