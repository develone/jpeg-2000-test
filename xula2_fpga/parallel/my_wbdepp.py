import myhdl
from myhdl import *
import argparse
from argparse import Namespace
from rhea.system import Reset
reset = Reset(0, active=1, async=False)

'''Include RPi2B interface'''
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

r_data = Signal(intbv(0)[32:])
r_int = Signal(bool(0))
r_err = Signal(bool(0))
w_wait = Signal(bool(0))
def cliparse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--brd", default='xula2_stickit_mb')
    parser.add_argument("--flow", default="ise")
    parser.add_argument("--build", default=False, action='store_true')
    parser.add_argument("--trace", default=False, action='store_true')
    parser.add_argument("--convert", default=False, action='store_true')
 
    args = parser.parse_args()
    return args    

def my_wbdepp(i_clk,i_astb_n,i_dstb_n,i_write_n,to_depp,fr_depp,o_wait,o_wb_cyc,o_wb_stb, \
o_wb_we,o_wb_addr,o_wb_data,i_wb_ack,i_wb_stall,i_wb_err,i_wb_data,i_int):
	
    @always(i_clk.posedge)
    def delayed1():
        x_dstb_n.next = i_dstb_n
        x_astb_n.next = i_astb_n
        x_write_n.next = i_write_n
        x_depp.next = i_depp
       
    @always(i_clk.posedge)
    def delay2():        
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
    def rtl7():
		dstb.next = (not r_dstb_n)and(l_dstb_n)

    @always_comb
    def rtl6():
		w_write.next = (not r_write_n)
				 
    @always(i_clk.posedge)
    def rtl5():
        '''ast depends on not r_astb_n and l_astb_n 
        
        addr depends on (w_write and astb)
        r_depp --> addr
        
        o_wb_addr & o_wb_data 32 bits are set when 
        (w_write and dstb and addr upper 5 bits are 0)
        
        When the lsb bit 3 to 0 of addr 
        000	r_depp --> o_wb_addr 31-24
        001 r_depp --> o_wb_addr 23-16
        010 r_depp --> o_wb_addr 15-8
        011 r_depp --> o_wb_addr 7-0
        
        When the lsb bit 7 to 4 of addr 
        100	r_depp --> o_wb_data 31-24
        101 r_depp --> o_wb_data 23-16
        110 r_depp --> o_wb_data 15-8
        111 r_depp --> o_wb_data 7-0
         '''
        if( w_write and  astb):
            addr.next = r_depp
        if( w_write and	dstb and (addr[8:3]==0)):
            if(addr[3:0]==0):
                o_wb_addr[32:24].next = r_depp
            if(addr[3:0]==1):	
                o_wb_addr[24:16].next = r_depp
            if(addr[3:0]==2):	    
                o_wb_addr[16:8].next = r_depp
            if(addr[3:0]==3):	
                o_wb_addr[8:0].next = r_depp
            if(addr[3:0]==4):	
                o_wb_data[32:24].next = r_depp
            if(addr[3:0]==5):    
                o_wb_data[24:16].next = r_depp
            if(addr[3:0]==6):    
                o_wb_data[16:8].next = r_depp
            else:    
                o_wb_data[8:0].next = r_depp
        '''if(o_wb_cyc and (i_wb_ack and not o_wb_we)):
				r_data.next = i_wb_data '''   
    @always(i_clk.posedge)
    def addr_data():
        if(addr[4]):
            o_depp.next = concat(o_wb_cyc , r_int , r_err)
        if( w_write and	dstb and (addr[8:3]==0)):
            if(addr[3:0]==0):
                o_depp.next = o_wb_addr[32:24]
	    if(addr[3:0]==1):	
                o_depp.next = o_wb_addr[24:16]
            if(addr[3:0]==2):	    
                o_depp.next = o_wb_addr[16:8]
            if(addr[3:0]==3):	
                o_depp.next = o_wb_addr[8:0]
            if(addr[3:0]==4):	
                o_depp.next = r_data[32:24]
            if(addr[3:0]==5):    
                o_depp.next = r_data[24:16]
            if(addr[3:0]==6):    
                o_depp.next = r_data[16:8]
            else:    
                o_depp.next = r_data[ 8: 0]
                
               
        r_int.next = (i_int)   or ( r_int and ( ~dstb or w_write or ~addr[4] ) )
        #r_err.next = ~(i_wb_err)or((r_err)and((~dstb)or(w_write)or(~addr[4])))
        
    
    @always_comb
    def wait():
	w_wait.next = not (x_dstb_n and x_astb_n and r_dstb_n and r_astb_n and l_dstb_n and l_astb_n)
    @always_comb
    def out_wait():
        o_wait.next = w_wait 
        
    '''
    These following lines need to commnted 
    out to convert 
    
    @always(i_clk.posedge)
       
    def int_values():
	if(reset == 1):
            x_dstb_n.next = 1
            r_dstb_n.next = 1
            l_dstb_n.next = 1
            x_astb_n.next = 1
            r_astb_n.next = 1
            l_astb_n.next = 1'''
         
    return myhdl.instances()
def toplevel(i_clk, i_rpi2B,fr_depp,o_rpi2B,to_depp):
    dut_rpi2B_io = rpi2B_io(i_rpi2B,o_depp,o_rpi2B,to_depp)
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
    top = toplevel(i_clk, i_rpi2B,fr_depp,o_rpi2B,to_depp )
    '''
    dut_rpi2B_io = rpi2B_io(i_rpi2B,fr_depp,o_rpi2B,to_depp)
    dut_my_wbdepp = my_wbdepp(i_clk,i_astb_n,i_dstb_n,i_write_n,to_depp, \
    fr_depp,o_wait,o_wb_cyc,o_wb_stb,o_wb_we,o_wb_addr,o_wb_data,i_wb_ack, \
    i_wb_stall,i_wb_err,i_wb_data,i_int)'''

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
       l_dstb_n.next = 1
       yield i_clk.posedge
       r_dstb_n.next = 1
       yield i_clk.posedge
       ''' 
       Expected boolean value, got -2 (<type 'int'>)
       i_int.next = 1
       yield i_clk.posedge
       i_int.next = 0
       yield i_clk.posedge
       ''' 
       i_astb_n.next = 1
       yield i_clk.posedge
       
       '''writing addres 01020304 1st byte'''
       
       i_depp.next = 1
       yield i_clk.posedge
       #i_rpi2B.next = 1
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
       i_depp.next = 0
       yield i_clk.posedge
       #i_rpi2B.next = 2
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
       yield i_clk.posedge
       #i_rpi2B.next = 3
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
       #i_depp.next = 0
       yield i_clk.posedge
       i_rpi2B.next = 4
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
       i_depp.next = 4
       yield i_clk.posedge
       #i_rpi2B.next = 4
       yield i_clk.posedge       
       
       i_write_n.next = 0
       yield i_clk.posedge
       i_astb_n.next = 0
       yield i_clk.posedge
       i_write_n.next = 1
       yield i_clk.posedge
       i_astb_n.next = 1
       yield i_clk.posedge
       
       yield delay(50)

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
