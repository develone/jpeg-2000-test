from myhdl import *

def ram(dout, din, addr, we, clk_fast, depth=128):
    """  Ram model """
    
    mem = [Signal(intbv(0)[8:]) for i in range(depth)]
    
    @always(clk_fast.posedge)
    def write():
        if we:
            mem[addr].next = din
                
    @always_comb
    def read():
        dout.next = mem[addr]

    return write, read


dout_lf = Signal(intbv(0)[8:])
din_lf = Signal(intbv(0)[8:])
addr_lf = Signal(intbv(0)[2:])
we_lf = Signal(bool(0))

dout_sa = Signal(intbv(0)[8:])
din_sa = Signal(intbv(0)[8:])
addr_sa = Signal(intbv(0)[2:])
we_sa = Signal(bool(0))

dout_rh = Signal(intbv(0)[8:])
din_rh = Signal(intbv(0)[8:])
addr_rh = Signal(intbv(0)[2:])
we_rh = Signal(bool(0))

dout_flgs = Signal(intbv(0)[8:])
din_flgs = Signal(intbv(0)[8:])
addr_flgs = Signal(intbv(0)[2:])
we_flgs = Signal(bool(0))

clk_fast = Signal(bool(0))

def xx():
    toVerilog.name = 'ram_1'
    toVerilog(ram, dout, din, addr, we, clk_fast)
    toVHDL(ram, dout, din, addr, we, clk_fast)
    
if __name__ == '__main__':
    main()
