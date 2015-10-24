from myhdl import *
from lift import *
from signed2twoscomplement import *

W0 = 9
flags_i = Signal(intbv(0)[3:])
z = Signal(intbv(0)[W0:])
left_i = Signal(intbv(0)[W0:])
right_i = Signal(intbv(0)[W0:])
sam_i = Signal(intbv(0)[W0:])
clk_i = Signal(bool(0))
update_i = Signal(bool(0))
update_o = Signal(bool(0))
res_o = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
t = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))

def tb(clk_i, res_o,z,update_o,left_i,sam_i,right_i,flags_i,update_i,t):
    @always(delay(10))
    def clkgen():
        clk_i.next = not clk_i

    instance_lift_step = lift_step(flags_i,update_i,left_i,sam_i,right_i,res_o,update_o,clk_i)
    instance_signed2twoscomplement = signed2twoscomplement(clk_i, t, z)

    @instance
    def stimulus():
	left_i.next = 68
        yield clk_i.posedge
	sam_i.next = 218
        yield clk_i.posedge
	right_i.next = 163
        yield clk_i.posedge
	flags_i.next = 7
        yield clk_i.posedge
	update_i.next = 1
        yield clk_i.posedge
	update_i.next = 0
        yield clk_i.posedge 
        t.next = res_o[W0:]
        yield clk_i.posedge
        
	print ('%d %s %s %s %s %s' % (now(),bin(left_i,W0), bin(sam_i,W0), bin(right_i,W0), bin(flags_i,2),bin(res_o,W0+1)))
        yield clk_i.posedge

	left_i.next = 68
        yield clk_i.posedge
	sam_i.next = 231
        yield clk_i.posedge
	right_i.next = 163
        yield clk_i.posedge
	flags_i.next = 5
        yield clk_i.posedge
	update_i.next = 1
        yield clk_i.posedge
	update_i.next = 0
        yield clk_i.posedge 
        t.next = res_o[W0:]
        yield clk_i.posedge
        
	print ('%d %s %s %s %s %s' % (now(),bin(left_i,W0), bin(sam_i,W0), bin(right_i,W0), bin(flags_i,2),bin(res_o,W0+1)))
        yield clk_i.posedge        
 
	left_i.next = 164
        yield clk_i.posedge
	sam_i.next = 250
        yield clk_i.posedge
	right_i.next = 160
        yield clk_i.posedge
	flags_i.next = 6
        yield clk_i.posedge
	update_i.next = 1
        yield clk_i.posedge
	update_i.next = 0
        yield clk_i.posedge 
        t.next = res_o[W0:]
        yield clk_i.posedge
        
	print ('%d %s %s %s %s %s' % (now(),bin(left_i,W0), bin(sam_i,W0), bin(right_i,W0), bin(flags_i,2),bin(res_o,W0+1)))

	left_i.next = 164
        yield clk_i.posedge
	sam_i.next = 203
        yield clk_i.posedge
	right_i.next = 160
        yield clk_i.posedge
	flags_i.next = 4
        yield clk_i.posedge
	update_i.next = 1
        yield clk_i.posedge
	update_i.next = 0
        yield clk_i.posedge 
        t.next = res_o[W0:]
        yield clk_i.posedge
        
	print ('%d %s %s %s %s %s' % (now(),bin(left_i,W0), bin(sam_i,W0), bin(right_i,W0), bin(flags_i,2),bin(res_o,W0+1)))
        yield clk_i.posedge
        yield clk_i.posedge       
        raise StopSimulation
    return instances()

def main():
   tb_fsm = traceSignals(tb,clk_i, res_o,z,update_o,left_i,sam_i,right_i,flags_i,update_i,t)
   sim = Simulation(tb_fsm)
   sim.run()

if __name__ == '__main__':
    main() 
