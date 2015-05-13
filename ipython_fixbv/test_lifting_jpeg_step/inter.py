from myhdl import *
#toVHDL.numeric_ports = False
pc_data_in = Signal(intbv(0)[2:])
pc_data_rdy = Signal(intbv(0)[2:])

def inter(pc_data_in, pc_data_rdy):
    @always_comb
    def rtl():
        pc_data_in.next = pc_data_rdy
    return rtl
toVHDL(inter, pc_data_in, pc_data_rdy)