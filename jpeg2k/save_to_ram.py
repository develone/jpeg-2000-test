from myhdl import *
DATA_WIDTH = 32768
RAM_ADDR = 9
def save_to_ram(clk_fast, dout_res_o, res_i, we_s_o, reset_sav_i, addr_res_o, incRes_i, odd_i):
    @always(clk_fast.posedge)
    def xx():
        if (reset_sav_i == 1):
            we_s_o.next = 0
            if (odd_i == 1):
                addr_res_o.next = 1
            else:
                addr_res_o.next = 2
        elif (incRes_i == 1):
            we_s_o.next = 0
            addr_res_o.next = addr_res_o + 2
            
        else:    
            we_s_o.next = 1
            dout_res_o.next = res_i
        
            
    return xx
clk_fast = Signal(bool(0))
odd_i = Signal(bool(0))
incRes_i = Signal(bool(0))
we_s_o = Signal(bool(0))
reset_sav_i = Signal(bool(0))
dout_res_o = Signal(intbv(0)[16:])
res_i = Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))
addr_res_o = Signal(intbv(0)[RAM_ADDR:]) 
toVerilog(save_to_ram, clk_fast, dout_res_o, res_i, we_s_o, reset_sav_i, addr_res_o, incRes_i, odd_i)
toVHDL(save_to_ram, clk_fast, dout_res_o, res_i, we_s_o, reset_sav_i, addr_res_o, incRes_i, odd_i)