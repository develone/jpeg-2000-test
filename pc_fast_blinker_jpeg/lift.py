from myhdl import *
W0 = 8
flags_i = Signal(intbv(0)[3:])
left_i = Signal(intbv(0)[W0:])
right_i = Signal(intbv(0)[W0:])
sam_i = Signal(intbv(0)[W0:])
clk_i = Signal(bool(0))
update_i = Signal(bool(0))
update_o = Signal(bool(0))
res_o = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
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
#toVHDL(lift_step,flags_i,update_i,left_i,sam_i,right_i,res_o,update_o,clk_i)
#toVerilog(lift_step,flags_i,update_i,left_i,sam_i,right_i,res_o,update_o,clk_i)
def tb(flags_i,update_i,left_i,sam_i,right_i,res_o,update_o,clk_i):
    instance_lift = lift_step(flags_i,update_i,left_i,sam_i,right_i,res_o,update_o,clk_i)

    @always(delay(10))
    def clkgen():
        clk_i.next = not clk_i

    @instance
    def stimulus():
	left_i.next = 164
        yield clk_i.posedge
	sam_i.next = 160
        yield clk_i.posedge
	right_i.next = 170
        yield clk_i.posedge
	flags_i.next = 7
        yield clk_i.posedge
	update_i.next = 1
        yield clk_i.posedge
        yield clk_i.posedge 
	print ('%d %s %s %s %s %s' % (now(),bin(left_i,W0), bin(sam_i,W0), bin(right_i,W0), bin(flags_i,3),bin(res_o,9)))
        yield clk_i.posedge
        
        
        raise StopSimulation
    return instances()
def main():
    
    toVHDL(lift_step,flags_i,update_i,left_i,sam_i,right_i,res_o,update_o,clk_i)
    toVerilog(lift_step,flags_i,update_i,left_i,sam_i,right_i,res_o,update_o,clk_i)
    '''
    tb_fsm = traceSignals(tb,flags_i,update_i,left_i,sam_i,right_i,res_o,update_o,clk_i)
    sim = Simulation(tb_fsm)
    sim.run()
    '''
if __name__ == '__main__':
    main()    
