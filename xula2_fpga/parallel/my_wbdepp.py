import myhdl
from myhdl import *
import argparse
from argparse import Namespace

from dr_wbdepp import rpi2B_io

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
    '''
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
    '''
	
    @always(i_clk.posedge)
    def rtl():
        x_dstb_n.next = i_dstb_n
        x_astb_n.next = i_astb_n
        x_write_n.next = i_write_n
        x_depp.next = i_depp
       
    @always(i_clk.posedge)
    def rtl1():        
        r_dstb_n.next = x_dstb_n
        #r_astb_n.next = x_atsb_n
        #r_write_n = x_write_n
        r_depp.next = x_depp
       
    @always(i_clk.posedge)
    def rtl2():        
        #l_dstb_n.next = r_dtsb_n
        l_astb_n.next = r_astb_n
    '''   
    @always(i_clk.posedge)
    def rtl3():
        #r_astb_n.next = x_atsb_n
        r_write_n = x_write_n
        l_dstb_n.next = r_dtsb_n
    '''
    @always(i_clk.posedge)
    def rtl4():
        if( w_write and  astb):
			addr.next = r_depp
        if( w_write and	dstb and addr[8:3]==5):
            if(addr[3:0]):
                o_wb_addr[32:24].next = r_depp
                o_wb_addr[24:16].next = r_depp
                o_wb_addr[16:8].next = r_depp
                o_wb_addr[8:0].next = r_depp
			
			    		       
    return myhdl.instances()
def toplevel(i_clk,i_astb_n,i_dstb_n,i_write_n,i_depp,o_depp,o_wait,o_wb_cyc,o_wb_stb,o_wb_we, \
o_wb_addr,o_wb_data,i_wb_ack,i_wb_stall,i_wb_err,i_wb_data,i_int, \
i_rpi2B,fr_depp,o_rpi2B,to_depp):
    dut_rpi2B_io = rpi2B_io(i_rpi2B,fr_depp,o_rpi2B,to_depp)

    dut_my_wbdepp = my_wbdepp(i_clk,i_astb_n,i_dstb_n,i_write_n,i_depp,o_depp,o_wait,o_wb_cyc,o_wb_stb, \
o_wb_we,o_wb_addr,o_wb_data,i_wb_ack,i_wb_stall,i_wb_err,i_wb_data,i_int)    
    return myhdl.instances()

def tb(i_clk,i_astb_n,i_dstb_n,i_write_n,i_depp,o_depp,o_wait,o_wb_cyc,o_wb_stb,o_wb_we, \
o_wb_addr,o_wb_data,i_wb_ack,i_wb_stall,i_wb_err,i_wb_data,i_int, \
i_rpi2B,fr_depp,o_rpi2B,to_depp):
    dut_rpi2B_io = rpi2B_io(i_rpi2B,fr_depp,o_rpi2B,to_depp)
    dut_my_wbdepp = my_wbdepp(i_clk,i_astb_n,i_dstb_n,i_write_n,i_depp,o_depp,o_wait,o_wb_cyc,o_wb_stb, \
o_wb_we,o_wb_addr,o_wb_data,i_wb_ack,i_wb_stall,i_wb_err,i_wb_data,i_int)

    @always(delay(10))
    def clkgen():
        i_clk.next = not i_clk

    @instance
    def stimulus():
       i_dstb_n.next = 1
       yield i_clk.posedge		
       i_astb_n.next= 1
       yield i_clk.posedge		
       i_write_n.next = 1
       yield i_clk.posedge		
       for i in range(4):
           i_depp.next = i
           yield i_clk.posedge
           i_dstb_n.next = 1
           yield i_clk.posedge
           i_astb_n.next = 1
           yield i_clk.posedge

           i_write_n.next = 1
           yield i_clk.posedge
           i_dstb_n.next = 0
           yield i_clk.posedge

           i_astb_n.next= 0
           yield i_clk.posedge
           i_write_n.next = 0
           yield i_clk.posedge
       raise StopSimulation   		    
    return myhdl.instances()	    
#toVerilog(my_wbdepp,i_clk,i_astb_n,i_dstb_n,i_write_n,i_depp,o_depp,o_wait,o_wb_cyc,o_wb_stb,o_wb_we,o_wb_addr,o_wb_data,i_wb_ack,i_wb_stall,i_wb_err,i_wb_data,i_int)
#toVerilog(rpi2B_io,i_rpi2B,fr_depp,o_rpi2B,to_depp)
def convert():
	toVerilog(toplevel,i_clk,i_astb_n,i_dstb_n,i_write_n,i_depp,o_depp,o_wait,o_wb_cyc, \
o_wb_stb,o_wb_we,o_wb_addr,o_wb_data,i_wb_ack,i_wb_stall,i_wb_err,i_wb_data,i_int, \
i_rpi2B,fr_depp,o_rpi2B,to_depp)
 
def main():
    args = cliparse()
    if args.trace:
        tb_fsm = traceSignals(tb,i_clk,i_astb_n,i_dstb_n,i_write_n,i_depp,o_depp,o_wait,o_wb_cyc, \
        o_wb_stb,o_wb_we,o_wb_addr,o_wb_data,i_wb_ack,i_wb_stall,i_wb_err,i_wb_data,i_int, \
        i_rpi2B,fr_depp,o_rpi2B,to_depp)
        sim = Simulation(tb_fsm)
        sim.run()
    if args.build:
	build(args)

    if args.convert: 
	convert()
if __name__ == '__main__':
    main()
