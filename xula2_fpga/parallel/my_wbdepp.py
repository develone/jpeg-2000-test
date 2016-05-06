import myhdl
from myhdl import *
import argparse
from argparse import Namespace
from rhea.system import Reset
reset = Reset(0, active=1, async=False)
#from dr_wbdepp import rpi2B_io

i_rpi2B = Signal(intbv(0)[8:])
o_rpi2B = Signal(intbv(0)[8:])
i_clk  = Signal(bool(0))
#DEPP interface
i_astb_n = Signal(bool(0))
i_dstb_n = Signal(bool(0))
i_write_n = Signal(bool(0))
o_depp = Signal(intbv(0)[8:])
i_depp = Signal(intbv(0)[8:])
fr_depp = Signal(intbv(0)[8:])
to_depp = Signal(intbv(0)[8:])
o_wait = Signal(bool(0))

#Wishbone master interface
o_wb_cyc = Signal(bool(0))
o_wb_stb = Signal(bool(0))
o_wb_we = Signal(bool(0))
o_wb_addr = Signal(intbv(0)[32:])
o_wb_data = Signal(intbv(0)[32:])
i_wb_ack = Signal(bool(0))
i_wb_stall = Signal(bool(0))
i_wb_err = Signal(bool(0))
i_wb_data = Signal(intbv(0)[32:])
i_int = Signal(bool(0))

#Synchronize the incoming signals
x_dstb_n = Signal(bool(0))
x_astb_n = Signal(bool(0))
x_write_n = Signal(bool(0))
r_dstb_n = Signal(bool(0))
r_astb_n = Signal(bool(0))
r_write_n = Signal(bool(0))
l_dstb_n = Signal(bool(0))
l_astb_n = Signal(bool(0))

r_depp = Signal(intbv(0)[8:])
x_depp = Signal(intbv(0)[8:])
astb = Signal(bool(0))
dstb = Signal(bool(0))
w_write = Signal(bool(0))
addr = Signal(intbv(0)[8:])
def rpi2B_io(i_clk,i_rpi2B,fr_depp,o_rpi2B,to_depp):
 


		
 
    @always(i_clk.posedge)
    def rtl1():
        to_depp[1:0].next = i_rpi2B[1:0]
        to_depp[2:1].next = i_rpi2B[2:1]
        to_depp[3:2].next = i_rpi2B[3:2]
        to_depp[4:3].next = i_rpi2B[4:3]
        to_depp[5:4].next = i_rpi2B[5:4]
        to_depp[6:5].next = i_rpi2B[6:5]
        to_depp[7:6].next = i_rpi2B[7:6]
        to_depp[8:7].next = i_rpi2B[8:7]
    @always(i_clk.posedge)
    def rtl2():
        o_rpi2B[1:0].next = fr_depp[1:0]
        o_rpi2B[2:1].next = fr_depp[2:1]
        o_rpi2B[3:2].next = fr_depp[3:2]
        o_rpi2B[4:3].next = fr_depp[4:3]
        o_rpi2B[5:4].next = fr_depp[5:4]
        o_rpi2B[6:5].next = fr_depp[6:5]
        o_rpi2B[7:6].next = fr_depp[7:6]
        o_rpi2B[8:7].next = fr_depp[8:7]

				        	
    return myhdl.instances()
def cliparse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--brd", default='xula2_stickit_mb')
    parser.add_argument("--flow", default="ise")
    parser.add_argument("--build", default=False, action='store_true')
    parser.add_argument("--trace", default=False, action='store_true')
    parser.add_argument("--convert", default=False, action='store_true')
 
    args = parser.parse_args()
    return args    

def my_wbdepp(i_clk,i_astb_n,i_dstb_n,i_write_n,i_depp,o_depp,o_wait,o_wb_cyc,o_wb_stb, \
o_wb_we,o_wb_addr,o_wb_data,i_wb_ack,i_wb_stall,i_wb_err,i_wb_data,i_int):
	
    @always(i_clk.posedge)
    def rtl():
        x_dstb_n.next = i_dstb_n
        x_astb_n.next = i_astb_n
        x_write_n.next = i_write_n
        x_depp.next = i_depp
       
    @always(i_clk.posedge)
    def rtl1():        
        r_dstb_n.next = x_dstb_n
        r_astb_n.next = x_astb_n
        r_write_n.next = x_write_n
        r_depp.next = x_depp
      
    @always(i_clk.posedge)
    def rtl2():        
        l_dstb_n.next = r_dstb_n
        l_astb_n.next = r_astb_n
    @always_comb
    def rtl4():
		astb.next = (not r_astb_n)and(l_astb_n)
		
    @always_comb
    def rtl5():
		dstb.next = (not r_dstb_n)and(l_dstb_n)

    @always_comb
    def rtl6():
		w_write.next = (not r_write_n)
				 
    @always(i_clk.posedge)
    def rtl3():
        if( w_write and  astb):
            addr.next = r_depp
        if( w_write and	dstb and (addr[8:3]==5)):
            if(addr[3:0]==0):
                o_wb_addr[32:24].next = r_depp
	    elif(addr[3:0]==1):	
                o_wb_addr[24:16].next = r_depp
            elif(addr[3:0]==2):	    
                o_wb_addr[16:8].next = r_depp
            elif(addr[3:0]==3):	
                o_wb_addr[8:0].next = r_depp
            elif(addr[3:0]==4):	
                o_wb_data[32:24].next = r_depp
            elif(addr[3:0]==5):    
                o_wb_data[24:16].next = r_depp
            elif(addr[3:0]==6):    
                o_wb_data[16:8].next = r_depp
            else:    
                o_wb_data[8:0].next = r_depp
 
    			    		       
    return myhdl.instances()
def toplevel(i_clk, i_rpi2B,fr_depp,o_rpi2B,to_depp):
    dut_rpi2B_io = rpi2B_io(i_clk,i_rpi2B,fr_depp,o_rpi2B,to_depp)
    reset_dly_cnt = Signal(intbv(0)[5:])
    @always(i_clk.posedge)
    def reset_tst():
        '''
        For the first 4 clocks the reset is forced to lo
        for clock 6 to 31 the reset is set hi
        then the reset is lo
        '''
        if (reset_dly_cnt < 31):
            reset_dly_cnt.next = reset_dly_cnt + 1
            if (reset_dly_cnt <= 4):
                reset.next = 0
            if (reset_dly_cnt >= 5):
                reset.next = 1
                #i_int.next = 1
        else:
            reset.next = 0
 
    

    dut_my_wbdepp = my_wbdepp(i_clk,i_astb_n,i_dstb_n,i_write_n,to_depp,\
    fr_depp,o_wait,o_wb_cyc,o_wb_stb, \
    o_wb_we,o_wb_addr,o_wb_data,i_wb_ack,i_wb_stall,i_wb_err,i_wb_data,i_int)    
    return myhdl.instances()

def tb(i_clk, i_rpi2B,fr_depp,o_rpi2B,to_depp ):
    #dut_rpi2B_io = toplevel(i_clk,i_rpi2B,fr_depp,o_rpi2B,to_depp)
    dut_my_wbdepp = my_wbdepp(i_clk,i_astb_n,i_dstb_n,i_write_n,i_depp, \
    o_depp,o_wait,o_wb_cyc,o_wb_stb,o_wb_we,o_wb_addr,o_wb_data,i_wb_ack, \
    i_wb_stall,i_wb_err,i_wb_data,i_int)

    @always(delay(10))
    def clkgen():
        i_clk.next = not i_clk

    @instance
    def stimulus():
       yield delay(1000)	
       yield i_clk.posedge
       i_write_n.next = 1
       yield i_clk.posedge
       i_dstb_n.next = 1
       yield i_clk.posedge
       i_astb_n.next = 1
       yield i_clk.posedge
       
       '''writing addres 01020304 1st byte'''
       
       i_depp.next = 1
       yield i_clk.posedge
       i_write_n.next = 0
       yield i_clk.posedge
       i_astb_n.next = 0
       yield i_clk.posedge
       i_write_n.next = 1
       yield i_clk.posedge
       i_astb_n.next = 1
       yield i_clk.posedge

       while(o_wait):
           print "wait for o_wait",o_wait
           yield i_clk.posedge
       i_depp.next = 2
       i_write_n.next = 0
       yield i_clk.posedge
       i_astb_n.next = 0
       yield i_clk.posedge
       i_write_n.next = 1
       yield i_clk.posedge
       i_astb_n.next = 1
       yield i_clk.posedge

       while(o_wait):
           print "wait for o_wait",o_wait
           yield i_clk.posedge
       i_depp.next = 2
       i_write_n.next = 0
       yield i_clk.posedge
       i_astb_n.next = 0
       yield i_clk.posedge
       i_write_n.next = 1
       yield i_clk.posedge
       i_astb_n.next = 1
       yield i_clk.posedge

       while(o_wait):
           print "wait for o_wait",o_wait
           yield i_clk.posedge
       i_depp.next = 3
       i_write_n.next = 0
       yield i_clk.posedge
       i_astb_n.next = 0
       yield i_clk.posedge
       i_write_n.next = 1
       yield i_clk.posedge
       i_astb_n.next = 1
       yield i_clk.posedge

       while(o_wait):
           print "wait for o_wait",o_wait
           yield i_clk.posedge
       i_depp.next = 4
       i_write_n.next = 0
       yield i_clk.posedge
       i_astb_n.next = 0
       yield i_clk.posedge
       i_write_n.next = 1
       yield i_clk.posedge
       i_astb_n.next = 1
       yield i_clk.posedge

       raise StopSimulation   		    
    return myhdl.instances()	    
#toVerilog(my_wbdepp,i_clk,i_astb_n,i_dstb_n,i_write_n,i_depp,o_depp,o_wait,o_wb_cyc,o_wb_stb,o_wb_we,o_wb_addr,o_wb_data,i_wb_ack,i_wb_stall,i_wb_err,i_wb_data,i_int)
#toVerilog(rpi2B_io,i_rpi2B,fr_depp,o_rpi2B,to_depp)
def convert():
	toVerilog(toplevel,i_clk,i_rpi2B,fr_depp,o_rpi2B,to_depp)
 
def main():
    args = cliparse()
    if args.trace:
        tb_fsm = traceSignals(tb,i_clk,i_rpi2B,fr_depp,o_rpi2B,to_depp )
        sim = Simulation(tb_fsm)
        sim.run()
    if args.build:
	build(args)

    if args.convert: 
	convert()
if __name__ == '__main__':
    main()
