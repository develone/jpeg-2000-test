import myhdl
from myhdl import *
import argparse
from argparse import Namespace
from rhea.system import Reset
reset = Reset(0, active=1, async=False)

'''Include RPi2B interface
This is used in dr_wbdepp.py
also used in my_wbdepp.py
also used in depp.py'''
from rpi2B import *
 
clk  = Signal(bool(0))
a_dstb = Signal(bool(0))
a_astb = Signal(bool(0))
a_write = Signal(bool(0))
a_wait = Signal(bool(0))
a_addr_reg = Signal(intbv(0)[8:])
a_data_reg = Signal(intbv(0)[8:])
a_db = Signal(intbv(0)[8:])
a_astb_sr = Signal(intbv(0)[3:])
a_dstb_sr = Signal(intbv(0)[3:])
def cliparse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--brd", default='xula2_stickit_mb')
    parser.add_argument("--flow", default="ise")
    parser.add_argument("--build", default=False, action='store_true')
    parser.add_argument("--trace", default=False, action='store_true')
    parser.add_argument("--convert", default=False, action='store_true')
 
    args = parser.parse_args()
    return args
def toplevel(i_clk, i_rpi2B,fr_depp,o_rpi2B,to_depp):
    dut_rpi2B_io = rpi2B_io(i_rpi2B,fr_depp,o_rpi2B,to_depp)
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
 
    

    #dut_depp = depp(clk,a_dstb,a_astb,a_write,a_wait,a_addr_reg,to_depp)
 
      
    return myhdl.instances()    
def depp(clk,a_dstb,a_astb,a_write,a_wait,a_addr_reg,a_db):

    @always_comb
    def rtl1():
        a_wait.next = not a_astb or not a_dstb

    @always(clk.posedge)
    def rtl2():
        a_astb_sr.next = concat(a_astb_sr[2:0], a_astb)
        a_dstb_sr.next = concat(a_dstb_sr[2:0], a_dstb)

    @always(clk.posedge)
    def rtl3():
        if (~a_write and a_astb_sr == 4):
            a_addr_reg.next = a_db

    @always(clk.posedge)
    def rtl4():
        if (~a_write and a_dstb_sr == 4):
            a_data_reg.next = a_db

    return myhdl.instances()
def tb(clk,a_dstb,a_astb,a_write,a_wait,a_addr_reg,a_db):
#def tb(clk, i_rpi2B,fr_depp,o_rpi2B,to_depp):
    #dut_rpi2B_io = rpi2B_io(i_rpi2B,fr_depp,o_rpi2B,to_depp )
    dut = depp(clk,a_dstb,a_astb,a_write,a_wait,a_addr_reg,a_db)
    @always(delay(10))
    def clkgen():
        clk.next = not clk

    @instance
    def stimulus():
       yield clk.posedge
       a_astb.next = 1
       yield clk.posedge
       a_dstb.next = 1
       yield clk.posedge
       a_write.next = 1
       yield clk.posedge 		
       yield delay(40)
       '''		
              		
       while(a_wait):
           print "wait for a_wait",a_wait
           
           a_astb.next = 1
           a_dstb.next = 1
           a_write.next = 1
           
           yield clk.posedge                    		
       '''        		
       #i_rpi2B.next = 1
       a_db.next = 1
       yield clk.posedge
       while(a_wait):
           print "wait for a_wait",a_wait
       '''           
       a_write.next = 0
       yield clk.posedge
       '''
       a_astb.next = 0
       yield clk.posedge
       a_write.next = 0
       yield clk.posedge       
       a_astb.next = 1
       yield clk.posedge
       a_write.next = 1
       yield clk.posedge              
       #i_rpi2B.next = 2
       a_db.next = 2
       yield clk.posedge
       while(a_wait):
           print "wait for a_wait",a_wait
       '''           
       a_write.next = 0
       yield clk.posedge
       '''
       a_dstb.next = 0
       yield clk.posedge
       a_write.next = 0
       yield clk.posedge       
       a_dstb.next = 1
       yield clk.posedge
       a_write.next = 1
       yield clk.posedge                      

       raise StopSimulation
          		    
    return myhdl.instances()

 
def convert():
	toVerilog(toplevel,clk, i_rpi2B,fr_depp,o_rpi2B,to_depp)
	toVerilog(depp,clk,a_dstb,a_astb,a_write,a_wait,a_addr_reg,a_db)
 
def main():
    args = cliparse()
    if args.trace:
        #tb_fsm = traceSignals(tb,clk, i_rpi2B,fr_depp,o_rpi2B,to_depp )
        tb_fsm = traceSignals(tb,clk,a_dstb,a_astb,a_write,a_wait,a_addr_reg,a_db)
        sim = Simulation(tb_fsm)
        sim.run()
    if args.build:
	build(args)

    if args.convert: 
	convert()
if __name__ == '__main__':
    main()
