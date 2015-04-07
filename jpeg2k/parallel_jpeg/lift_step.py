 
from myhdl import *
import  random
from signed2twoscomplement import signed2twoscomplement
from jpeg_constants import *
def top(clk, x, z, n=16):
   res_o = [Signal(intbv(0, min=-(2**(W0)), max=(2**(W0)))) for i in range(n)]
   left_i = [Signal(intbv(0)[W0:]) for i in range(n)]
   sam_i = [Signal(intbv(0)[W0:]) for i in range(n)]
   right_i = [Signal(intbv(0)[W0:]) for i in range(n)]
   flgs_i = [Signal(intbv(0)[W3:]) for i in range(n)]
   update_i = [Signal(bool(0)) for i in range(n)]
   update_o = [Signal(bool(0)) for i in range(n)]
   jpeg_instance = [None for i in range(n)]
   instance_signed2twoscomplement = signed2twoscomplement(x, z)
   '''
   print left_i
   print sam_i
   print right_i
   print flgs_i
   
   print jpeg_instance
   '''
   for i in range(n):
       jpeg_instance[i] = lift_step(left_i[i], sam_i[i], right_i[i], flgs_i[i], update_i[i], clk, res_o[i], update_o[i])
   #print jpeg_instance
   return jpeg_instance, instance_signed2twoscomplement

def lift_step(left_i, sam_i, right_i, flgs_i, update_i, clk, res_o, update_o):
    @always(clk.posedge)
    def rtl ():
        if (update_i == 1):
            update_o.next = 0
            if (flgs_i == 7):
                res_o.next = sam_i.signed() - ( (left_i.signed() >> 1) + (right_i.signed() >> 1) )
            elif (flgs_i == 5):
                res_o.next = sam_i.signed() + ( (left_i.signed() >> 1) + (right_i.signed() >> 1) )
            elif (flgs_i == 6):
                res_o.next = sam_i.signed() + ( (left_i.signed() + right_i.signed() + 2) >> 2 )
            elif (flgs_i == 4):
                res_o.next = sam_i.signed() - ( (left_i.signed() + right_i.signed() + 2) >> 2 )
        else:
            update_o.next = 1
    return rtl    
		
x = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
z = Signal(intbv(0)[W0:]) 

res_o = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
left_i = Signal(intbv(0)[W0:])
right_i = Signal(intbv(0)[W0:])
sam_i = Signal(intbv(0)[W0:])
flgs_i = Signal(intbv(0)[5:])
clk = Signal(bool(0))
update_i = Signal(bool(0))
update_o = Signal(bool(0))

def test_lift_step():
    instance_signed2twoscomplement = signed2twoscomplement(x, z)
    instance_jpeg = lift_step(left_i, sam_i, right_i, flgs_i, update_i, clk, res_o, update_o)
    @always(delay(10))
    def clkgen():
        clk.next = not clk
    @instance
    def stimulus():
        for i in range(10):
            l = random.randrange(0,256)
            s = random.randrange(0,256)
            r = random.randrange(0,256)
            left_i.next = l
            yield clk.posedge
            sam_i.next = s
            yield clk.posedge
            right_i.next = r
            yield clk.posedge
            flgs_i.next = 7
            yield clk.posedge
            update_i.next = 1
            yield clk.posedge
            x.next = res_o[W0:]
            yield clk.posedge
            print left_i, sam_i, right_i, flgs_i, update_i, res_o, x, z, update_o
            update_i.next = 0
            yield clk.posedge
            flgs_i.next = 5
            yield clk.posedge
            update_i.next = 1
            yield clk.posedge
            x.next = res_o[W0:]
            yield clk.posedge
            print left_i, sam_i, right_i, flgs_i, update_i, res_o, x, z, update_o
            update_i.next = 0
            yield clk.posedge
            flgs_i.next = 6
            yield clk.posedge
            update_i.next = 1
            yield clk.posedge
            x.next = res_o[W0:]
            yield clk.posedge
            print left_i, sam_i, right_i, flgs_i, update_i, res_o, x, z, update_o
            update_i.next = 0
            yield clk.posedge
            flgs_i.next = 4
            yield clk.posedge
            update_i.next = 1
            yield clk.posedge
            x.next = res_o[W0:]
            yield clk.posedge
            print left_i, sam_i, right_i, flgs_i, update_i, res_o, x, z, update_o
            update_i.next = 0
            yield clk.posedge 
        raise StopSimulation
    return  instance_jpeg, instance_signed2twoscomplement, clkgen, stimulus 
def convert():
    toVHDL(lift_step,left_i, sam_i, right_i, flgs_i, update_i, clk, res_o, update_o)
#convert() 
#tb_fsm = traceSignals(test_lift_step)
#sim = Simulation(tb_fsm)
#sim.run()
jpeg_instance, instance_signed2twoscomplement = top(clk, x, z)
print  jpeg_instance
print
print instance_signed2twoscomplement
toVHDL(top, clk, x, z)

