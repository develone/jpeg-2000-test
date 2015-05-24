from myhdl import *
from PIL import Image
im = Image.open("../../lena_256.png")
pix = im.load()
w, h = im.size
m = list(im.getdata())
#print m.__sizeof__()
m = [m[i:i+im.size[0]] for i in range(0, len(m), im.size[0])]
print m[0][0], m[1][0],m[2][0],m[3][0],m[4][0],m[5][0],m[6][0]
print m[248][0],m[249][0], m[250][0],m[251][0],m[252][0],m[253][0],m[254][0]

#print m
W0 = 9
data_in = Signal(intbv(0)[W0:])
'''toLift_Step used for mapping datatodut
from usb hostio
datatodut is an alias of toSub_s
addr_in_toLift_Step used for mapping addr_in_toLift_Step
from usb hostio
addr_in_toLift_Step is an alias of toSub_s
'''
toLift_Step = Signal(intbv(0)[W0:])
we_in = Signal(bool(0))
addr_in = Signal(intbv(0)[8:])
muxsel_i = Signal(bool(0))
read_pc_i = Signal(bool(0))
clk = Signal(bool(0))
'''data from usb hostio'''
pc_data_in = Signal(intbv(0)[2:])
pc_data_rdy = Signal(intbv(0)[2:])

data_pc_in  = Signal(bool(0))

addr_in_toLift_Step = Signal(intbv(0)[8:])

def pc_read(clk,data_in,toLift_Step,addr_in,addr_in_toLift_Step, read_pc_i,muxsel_i, pc_data_in, pc_data_rdy, we_in):
    @always_comb
    def rtl():
        
        if( (read_pc_i == 1) and (muxsel_i == 1)):
            pc_data_in.next = pc_data_rdy
            data_in.next = toLift_Step
            addr_in.next = addr_in_toLift_Step
            we_in.next = 1
        else:
            pc_data_in.next = 0
            data_in.next = 0
            addr_in.next = 0
            we_in.next = 0  
              
    return rtl
    
 
def tb(clk,data_in,toLift_Step,addr_in,addr_in_toLift_Step, read_pc_i,muxsel_i, pc_data_in, pc_data_rdy, we_in):
    instance_pc_read = pc_read(clk,data_in,toLift_Step,addr_in,addr_in_toLift_Step, read_pc_i,muxsel_i, pc_data_in, pc_data_rdy, we_in) 
    @always(delay(10))
    def clkgen():
        clk.next = not clk
    @instance
    def stimulus():
        
        pc_data_rdy.next = 3
        yield clk.posedge
        muxsel_i.next = 0
        yield clk.posedge
        read_pc_i.next = 0
        yield clk.posedge
        addr_in_toLift_Step.next = 0
        yield clk.posedge
        #we_in.next = 1
        #yield clk.posedge        

        muxsel_i.next = 1
        yield clk.posedge
        read_pc_i.next = 1
        yield clk.posedge
        
        for j in range(255):
            k = 0
            #print ("%d %d %d") %(now(), muxsel_i, read_pc_i) 
            #print ("%d wr %d addr %d ") % (now(), we_in, addr_in)
            addr_in_toLift_Step.next = j
            yield clk.posedge
            toLift_Step.next = m[addr_in][k]
            yield clk.posedge
            print ("%d data %d addr %d ") % (now(), data_in, addr_in)
            #print ("%d data %d ") % (now(), toLift_Step)
            
            #yield clk.posedge
            
        for i in range(10):
            muxsel_i.next = 0
            yield clk.posedge
            read_pc_i.next = 0
            yield clk.posedge 
            pc_data_rdy.next = 2
            yield clk.posedge           
        raise StopSimulation
    return instances()
#tb_fsm = traceSignals(tb,clk,data_in,toLift_Step,addr_in,addr_in_toLift_Step, read_pc_i,muxsel_i, pc_data_in, pc_data_rdy, we_in)

#sim = Simulation(tb_fsm)
#sim.run()
#toVHDL(pc_read,clk,data_in,toLift_Step,addr_in,addr_in_toLift_Step, read_pc_i,muxsel_i, pc_data_in, pc_data_rdy, we_in)
 
