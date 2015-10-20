from myhdl import *
flags_i = Signal(intbv(0)[3:])
left_i = Signal(intbv(0)[8:])
right_i = Signal(intbv(0)[8:])
sam_i = Signal(intbv(0)[8:])
clk_i = Signal(bool(0))
update_i = Signal(bool(0))
update_o = Signal(bool(0))
res_o = Signal(intbv(0, min=-(2**(8)), max=(2**(8))))
def lift_step(flags_i,update_i,left_i,sam_i,right_i,res_o,update_o,clk_i):
    @always(clk_i.posedge)
    def rtl ():
        if (update_i == 1):
            update_o.next = 0
            if (flags_i == 7):
               res_o.next = sam_i - ((left_i.signed() >> 1) + (right_i.signed() >> 1))
            elif (flags_i == 6):
               res_o.next = sam_i.signed() + ( (left_i.signed() + right_i.signed() + 2) >> 2 )
            elif (flags_i == 5):
               res_o.next = sam_i + ((left_i.signed() >> 1) + (right_i.signed() >> 1))
            elif (flags_i == 4):
               res_o.next = sam_i.signed() - ( (left_i.signed() + right_i.signed() + 2) >> 2 )
        else:
            update_o.next = 1
    return rtl
toVHDL(lift_step,flags_i,update_i,left_i,sam_i,right_i,res_o,update_o,clk_i)
toVerilog(lift_step,flags_i,update_i,left_i,sam_i,right_i,res_o,update_o,clk_i)
