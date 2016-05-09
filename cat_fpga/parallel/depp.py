import myhdl
from myhdl import *
import argparse
from argparse import Namespace

from pprint import pprint 

from rhea.system import Reset
from rhea.build.boards import get_board

reset = Reset(0, active=1, async=False)

'''Currently using to_rpi2B & fr_rpi2B'''
 
fr_rpi2B = Signal(intbv(0)[8:]) 
to_rpi2B = Signal(intbv(0)[8:]) 
clock  = Signal(bool(0))
a_dstb = Signal(bool(0))
a_astb = Signal(bool(0))
a_write = Signal(bool(0))
a_wait = Signal(bool(0))
a_addr_reg = Signal(intbv(0)[8:])
a_data_reg = Signal(intbv(0)[8:])
a_db = Signal(intbv(0)[8:])
a_astb_sr = Signal(intbv(0)[3:])
a_dstb_sr = Signal(intbv(0)[3:])

def build(args):
    '''
	GPIO FOR XULA2-LX9
	16 GPIO FOR INPUT OR OUTPUT
	CH0 R7  CH1 R15 CH2 R16 CH3 M15 CH4 M16 CH5 K15 CH6  K16 CH7 J16
	CH8 J14 CH9 F15 CH10 F16 CH11 C16 CH12 C15 CH13 B16 CH14 B15 CH22 H1
	CH23 H2 CH24 F1 CH25 F2 CH26 E1
	CH27 E2 CH28 C1 CH29 B1 B30 B2 CH31 A2  
    '''
    brd = get_board(args.brd)
    brd.device = 'XC6SLX9'
    brd.add_port_name('fr_rpi2B', 'pm2', slice(0, 8))
    brd.add_port_name('to_rpi2B', 'pm2', slice(0, 8))
    brd.add_port('a_astb', 'A2')
    brd.add_port('a_dstb', 'B2')
    brd.add_port('a_write', 'B1')
    brd.add_port('a_wait', 'C1')
    print(("%s %s") % (brd, brd.device))
    flow = brd.get_flow(para_rpi2B)
    flow.run()
    info = flow.get_utilization()
    pprint(info)	
	
def cliparse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--brd", default='xula2_stickit_mb')
    parser.add_argument("--flow", default="ise")
    parser.add_argument("--build", default=False, action='store_true')
    parser.add_argument("--trace", default=False, action='store_true')
    parser.add_argument("--convert", default=False, action='store_true')
 
    args = parser.parse_args()
    return args
def para_rpi2B( clock, to_rpi2B,fr_rpi2B,a_dstb,a_astb,a_write,a_wait):
 
    reset_dly_cnt = Signal(intbv(0)[5:])
    @always( clock.posedge)
    def reset_tst():
        '''
        For the first 4 clocks the reset is forced to lo
        for clock 6 to 31 the reset is set hi
        then the reset is lo
        '''
        if (reset_dly_cnt < 10):
            reset_dly_cnt.next = reset_dly_cnt + 1
            if (reset_dly_cnt <= 4):
                reset.next = 0
            if (reset_dly_cnt >= 5):
                reset.next = 1
                #i_int.next = 1
        else:
            reset.next = 0
 
    

    dut_depp = depp(clock,a_dstb,a_astb,a_write,a_wait,a_addr_reg,fr_rpi2B)
 
      
    return myhdl.instances()    
def depp(clock,a_dstb,a_astb,a_write,a_wait,a_addr_reg,a_db):

    @always_comb
    def rtl1():
        a_wait.next = not a_astb or not a_dstb

    @always(clock.posedge)
    def rtl2():
        a_astb_sr.next = concat(a_astb_sr[2:0], a_astb)
        a_dstb_sr.next = concat(a_dstb_sr[2:0], a_dstb)

    @always(clock.posedge)
    def rtl3():
        if (~a_write and a_astb_sr == 4):
            a_addr_reg.next = a_db

    @always(clock.posedge)
    def rtl4():
        if (~a_write and a_dstb_sr == 4):
            a_data_reg.next = a_db

    return myhdl.instances()
 
def tb(clock, to_rpi2B,fr_rpi2B,a_dstb,a_astb,a_write,a_wait):
 
    dut = para_rpi2B( clock, to_rpi2B,fr_rpi2B,a_dstb,a_astb,a_write,a_wait)
    @always(delay(10))
    def clockgen():
        clock.next = not clock

    @instance
    def stimulus():
       yield delay(200)  	
       yield clock.posedge
       a_astb.next = 1
       yield clock.posedge
       a_dstb.next = 1
       yield clock.posedge
       a_write.next = 1
       yield clock.posedge 		
       yield delay(100)
       	
              		
       while(a_wait):
           print "wait for a_wait",a_wait
           '''
           a_astb.next = 1
           a_dstb.next = 1
           a_write.next = 1
           
           yield clock.posedge                    		
           '''        		
       fr_rpi2B.next = 1
       #a_db.next = 1
       yield clock.posedge
       while(a_wait):
           print "wait for a_wait",a_wait
       '''           
       a_write.next = 0
       yield clock.posedge
       '''
       a_astb.next = 0
       yield clock.posedge
       a_write.next = 0
       yield clock.posedge       
       a_astb.next = 1
       yield clock.posedge
       a_write.next = 1
       yield clock.posedge              
       fr_rpi2B.next = 2
       #a_db.next = 2
       yield clock.posedge
       while(a_wait):
           print "wait for a_wait",a_wait
       '''           
       a_write.next = 0
       yield clock.posedge
       '''
       a_dstb.next = 0
       yield clock.posedge
       a_write.next = 0
       yield clock.posedge       
       a_dstb.next = 1
       yield clock.posedge
       a_write.next = 1
       yield clock.posedge
       yield delay(200)  	                             

       raise StopSimulation
          		    
    return myhdl.instances()

 
def convert():
	toVerilog(para_rpi2B,clock, to_rpi2B,fr_rpi2B,a_dstb,a_astb,a_write,a_wait)
	toVerilog(depp,clock,a_dstb,a_astb,a_write,a_wait,a_addr_reg,a_db)
 
def main():
    args = cliparse()
    if args.trace:
        tb_fsm = traceSignals(tb,clock, to_rpi2B,fr_rpi2B,a_dstb,a_astb,a_write,a_wait )
         
         
        sim = Simulation(tb_fsm)
        sim.run()
    if args.build:
	    build(args)

    if args.convert: 
	convert()
if __name__ == '__main__':
    main()
