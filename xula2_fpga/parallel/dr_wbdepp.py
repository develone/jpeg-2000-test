import myhdl
from myhdl import *
import os
import argparse
from argparse import Namespace
from rhea.build.boards import get_board
from pprint import pprint
'''
tb_dut = _prep_cosimi_clk=i_clk,i_astb_n=i_astb_n,i_dstb_n=i_dstb_n,
i_write_n=i_write_n,i_depp=i_depp,o_depp=o_depp,o_wait=o_wait,
o_wb_cyc=o_wb_cyc,o_wb_stb=o_wb_stb=o_wb_stb,o_wb_addr=o_wb_addr,
o_wb_data=o_wb_data,i_wb_ack=i_wb_ack,i_wb_stall=i_wb_stall,
i_wb_err=i_wb_err,i_wb_data=i_wb_data,i_int=i_int)
'''
i_b0 = Signal(bool(0))
i_b1 = Signal(bool(0))
i_b2 = Signal(bool(0))
i_b3 = Signal(bool(0))
i_b4 = Signal(bool(0))
i_b5 = Signal(bool(0))
i_b6 = Signal(bool(0))
i_b7 = Signal(bool(0))

o_b0 = Signal(bool(0))
o_b1 = Signal(bool(0))
o_b2 = Signal(bool(0))
o_b3 = Signal(bool(0))
o_b4 = Signal(bool(0))
o_b5 = Signal(bool(0))
o_b6 = Signal(bool(0))
o_b7 = Signal(bool(0))
i_clk  = Signal(bool(0))
reset = Signal(bool(0))
reset_dly_cnt = Signal(intbv(0)[5:]) 
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
#memdev Signals 
i_wb_cyc = Signal(bool(0))
i_wb_stb = Signal(bool(0))
i_wb_we = Signal(bool(0))
def rpi2B_io(i_b0,i_b1,i_b2,i_b3,i_b4,i_b5,i_b6,i_b7,fr_depp,o_b0,o_b1,o_b2,o_b3,o_b4,o_b5,o_b6,o_b7,to_depp):
 


		
 
    @always_comb
    def rtl1():
        to_depp[1:0].next = i_b0
        to_depp[2:1].next = i_b1
        to_depp[3:2].next = i_b2
        to_depp[4:3].next = i_b3
        to_depp[5:4].next = i_b4
        to_depp[6:5].next = i_b5
        to_depp[7:6].next = i_b6
        to_depp[8:7].next = i_b7
    @always_comb
    def rtl2():
        o_b0.next = fr_depp[1:0]
        o_b1.next = fr_depp[2:1]
        o_b2.next = fr_depp[3:2]
        o_b3.next = fr_depp[4:3]
        o_b4.next = fr_depp[5:4]
        o_b5.next = fr_depp[6:5]
        o_b6.next = fr_depp[7:6]
        o_b7.next = fr_depp[8:7]

				        	
    return myhdl.instances()
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
	print(("%s %s") % (brd, brd.device))
	
def tb_cosim(args,i_clk,i_astb_n, i_dstb_n, i_write_n,i_depp, o_depp, o_wait,
	o_wb_cyc, o_wb_stb, o_wb_we, o_wb_addr, o_wb_data,
	i_wb_ack, i_wb_stall, i_wb_err, i_wb_data, i_int):
    #tb_dut_dr = dr_wbdepp(i_clk,i_b0,i_b1,i_b2,i_b3,i_b4,i_b5,i_b6,i_b7,fr_depp,o_b0,o_b1,o_b2,o_b3,o_b4,o_b5,o_b6,o_b7,to_depp)
    
    tb_dut = _prep_cosim(args,i_clk=i_clk,i_astb_n=i_astb_n,i_dstb_n=i_dstb_n, \
    i_write_n=i_write_n,i_depp=i_depp,o_depp=o_depp,o_wait=o_wait, \
    o_wb_cyc=o_wb_cyc,o_wb_stb=o_wb_stb,o_wb_we=o_wb_we,o_wb_addr=o_wb_addr, \
    o_wb_data=o_wb_data,i_wb_ack=i_wb_ack,i_wb_stall=i_wb_stall, \
    i_wb_err=i_wb_err,i_wb_data=i_wb_data,i_int=i_int, \
    fr_depp=fr_depp,o_b0=o_b0,o_b1=o_b1,o_b2=o_b2,o_b3=o_b3,o_b4=o_b4, \
    o_b5=o_b5,o_b6=o_b6,o_b7=o_b7,i_b0=i_b0,i_b1=i_b1,i_b2=i_b2,i_b3=i_b3,i_b4=i_b4, \
    i_b5=i_b5,i_b6=i_b6,i_b7=i_b7,to_depp=to_depp,i_wb_cyc=i_wb_cyc,i_wb_stb=i_wb_stb, \
    i_wb_we=i_wb_we)
    
     
    
    @always(delay(10))
    def clkgen():
        i_clk.next = not i_clk
    @instance
    def tbstim():

       yield i_clk.posedge		
       for i in range(100):
           yield i_clk.posedge
       for i in range(256):
           
           fr_depp.next = i
           yield i_clk.posedge
       for i in range(100):
           yield i_clk.posedge
       i_b1.next = 1
       yield i_clk.posedge
       i_b1.next = 0
       yield i_clk.posedge
       
       i_b2.next = 1
       yield i_clk.posedge
       i_b2.next = 0
       yield i_clk.posedge
       i_b3.next = 1
       yield i_clk.posedge                      
       i_b0.next = 1
       yield i_clk.posedge
       i_b0.next = 0
       yield i_clk.posedge
       
       i_b4.next = 1
       yield i_clk.posedge
       i_b4.next = 0
       yield i_clk.posedge
       
       i_b5.next = 1
       yield i_clk.posedge
       i_b5.next = 0
       yield i_clk.posedge
       i_b6.next = 1
       yield i_clk.posedge                      
       i_b6.next = 0
       yield i_clk.posedge
       i_b0.next = 0
       yield i_clk.posedge
       i_b7.next = 1
       yield i_clk.posedge
       i_b7.next = 0
       yield i_clk.posedge
       i_b3.next = 0
       yield i_clk.posedge
       for i in range(100):
           yield i_clk.posedge                     
       '''writing addres 03000508'''
       i_depp.next = 03
       yield i_clk.posedge
              
       i_int.next = 1
       yield i_clk.posedge
       i_write_n.next = 1
       yield i_clk.posedge
       i_dstb_n.next = 1
       yield i_clk.posedge
       i_astb_n.next = 1
       yield i_clk.posedge
       i_write_n.next = 0
       yield i_clk.posedge
       i_astb_n.next = 0
       yield i_clk.posedge
       i_depp.next = 0

       yield i_clk.posedge
       i_wb_ack.next = 1
       yield i_clk.posedge
       i_dstb_n.next = 0 
       yield i_clk.posedge
       i_write_n.next = 1
       yield i_clk.posedge
       i_dstb_n.next = 1
       yield i_clk.posedge
       i_astb_n.next = 1 
       yield i_clk.posedge
       i_write_n.next = 0
       yield i_clk.posedge
       i_astb_n.next = 0
       yield i_clk.posedge
       i_dstb_n.next = 0 
       yield i_clk.posedge
       for i in range(5):
		   yield i_clk.posedge
       i_depp.next = 5
       yield i_clk.posedge

       i_write_n.next = 1
       yield i_clk.posedge
       i_dstb_n.next = 1
       yield i_clk.posedge
       i_astb_n.next = 1 
       yield i_clk.posedge
       i_write_n.next = 0
       yield i_clk.posedge
       i_astb_n.next = 0
       yield i_clk.posedge
       i_dstb_n.next = 0 
       yield i_clk.posedge
       i_depp.next = 8
       yield i_clk.posedge

       i_write_n.next = 1
       yield i_clk.posedge
       i_dstb_n.next = 1
       yield i_clk.posedge
       i_astb_n.next = 1 
       yield i_clk.posedge
       i_write_n.next = 0
       yield i_clk.posedge
       i_astb_n.next = 0
       yield i_clk.posedge
       i_dstb_n.next = 0 
       yield i_clk.posedge
       i_depp.next = 164
       yield i_clk.posedge

       i_write_n.next = 1
       yield i_clk.posedge
       i_dstb_n.next = 1
       yield i_clk.posedge
       i_astb_n.next = 1 
       yield i_clk.posedge
       i_write_n.next = 0
       yield i_clk.posedge
       i_astb_n.next = 0
       yield i_clk.posedge
       i_dstb_n.next = 0 
       yield i_clk.posedge
       i_dstb_n.next = 1
       yield i_clk.posedge
       i_astb_n.next = 1
       yield i_clk.posedge
       i_depp.next = 200
       yield i_clk.posedge
       i_write_n.next = 0
       yield i_clk.posedge
       yield i_clk.posedge
       i_astb_n.next = 0
       for i in range(5):
		   yield i_clk.posedge	   
       for i in range(256):
           i_depp.next = i
           yield i_clk.posedge
           i_write_n.next = 0
           yield i_clk.posedge
           i_astb_n.next = 0
           yield i_clk.posedge
           i_dstb_n.next = 0 
           yield i_clk.posedge
           i_dstb_n.next = 1
           yield i_clk.posedge
           i_astb_n.next = 1
           yield i_clk.posedge                          
           i_write_n.next = 1
           yield i_clk.posedge
       raise StopSimulation
    print("back from prep cosim")
    print("start (co)simulation ...")
    Simulation((tb_dut, clkgen, tbstim)).run()    
def tb(args,i_clk,i_astb_n, i_dstb_n, i_write_n,i_depp, o_depp, o_wait,
	o_wb_cyc, o_wb_stb, o_wb_we, o_wb_addr, o_wb_data,
	i_wb_ack, i_wb_stall, i_wb_err, i_wb_data, i_int):
    '''
    tb_dut = _prep_cosim(args,i_clk=i_clk,i_astb_n=i_astb_n,i_dstb_n=i_dstb_n, \
    i_write_n=i_write_n,i_depp=i_depp,o_depp=o_depp,o_wait=o_wait, \
    o_wb_cyc=o_wb_cyc,o_wb_stb=o_wb_stb,o_wb_addr=o_wb_addr, \
    o_wb_data=o_wb_data,i_wb_ack=i_wb_ack,i_wb_stall=i_wb_stall, \
    i_wb_err=i_wb_err,i_wb_data=i_wb_data,i_int=i_int)
    '''
    inst_wbdepp = wbdepp(i_clk,i_astb_n, i_dstb_n, i_write_n,i_depp, o_depp, o_wait, o_wb_cyc, o_wb_stb, o_wb_we, o_wb_addr, o_wb_data, i_wb_ack, i_wb_stall, i_wb_err, i_wb_data, i_int)
    
    @always(delay(10))
    def clkgen():
        i_clk.next = not i_clk
    @instance
    def tbstim():
       for i in range(100):
           yield i_clk.posedge

       i_b3.next = 0
       yield i_clk.posedge                
       for i in range(256):
	   o_depp.next = i
           yield i_clk.posedge
       i_b3.next = 1
       r_depp.next = 208
       yield i_clk.posedge
       w_write.next = 1
       yield i_clk.posedge
       yield i_clk.posedge
       astb.next = 1
       yield i_clk.posedge
       yield i_clk.posedge

       raise StopSimulation
    return myhdl.instances()
def cliparse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--brd", default='xula2_stickit_mb')
    parser.add_argument("--flow", default="ise")
    parser.add_argument("--build", default=False, action='store_true')
    parser.add_argument("--trace", default=False, action='store_true')
    parser.add_argument("--convert_rpi2B_io", default=False, action='store_true')
    parser.add_argument("--cosim", default=False, action='store_true')
    parser.add_argument("--cosimtrace", default=False, action='store_true')
    args = parser.parse_args()
    return args    
def _prep_cosim(args, **sigs):
    """ prepare the cosimulation environment
    """
    print ("  *%s" %  (sigs))   
    print("compiling ...")
    cmd = "iverilog -o ifdeppsimple tb/wbdeppsimple.v tb/tb_wbdeppsimple.v rpi2B_io.v tb/memdev.v "
    print("  %s" %  (cmd))
    os.system(cmd)
    # get the handle to the
    print("cosimulation setup ...")
    cmd = "vvp -m ./myhdl.vpi ifdeppsimple"
    print("  %s" %  (cmd))
    cosim = Cosimulation(cmd, **sigs)
    print("  %s" %  (cosim))
    return cosim
def convert_rpi2B_io():        
    toVerilog(rpi2B_io,i_b0,i_b1,i_b2,i_b3,i_b4,i_b5,i_b6,i_b7,fr_depp,o_b0,o_b1,o_b2,o_b3,o_b4,o_b5,o_b6,o_b7,to_depp) 

def test_cosim_prep(args,i_clk,i_astb_n, i_dstb_n, i_write_n,i_depp, o_depp, o_wait,
	o_wb_cyc, o_wb_stb, o_wb_we, o_wb_addr, o_wb_data,
	i_wb_ack, i_wb_stall, i_wb_err, i_wb_data, i_int):
    tb_dut = _prep_cosim(args,i_clk=i_clk,i_astb_n=i_astb_n,i_dstb_n=i_dstb_n, \
    i_write_n=i_write_n,i_depp=i_depp,o_depp=o_depp,o_wait=o_wait, \
    o_wb_cyc=o_wb_cyc,o_wb_stb=o_wb_stb,o_wb_addr=o_wb_addr, \
    o_wb_data=o_wb_data,i_wb_ack=i_wb_ack,i_wb_stall=i_wb_stall, \
    i_wb_err=i_wb_err,i_wb_data=i_wb_data,i_int=i_int)
    		
def main():
    args = cliparse()
    if args.trace:
		tb_fsm = traceSignals(tb,args,i_clk,i_astb_n, i_dstb_n, i_write_n,i_depp, o_depp, o_wait, o_wb_cyc, o_wb_stb, o_wb_we, o_wb_addr, o_wb_data, i_wb_ack, i_wb_stall, i_wb_err, i_wb_data, i_int)
		sim = Simulation(tb_fsm)
		sim.run()
    if args.build:
	build(args)

    if args.convert_rpi2B_io: 
	convert_rpi2B_io()
    if args.cosim:
        test_prep = test_cosim_prep(args,i_clk,i_astb_n, i_dstb_n, i_write_n,i_depp, o_depp, o_wait, o_wb_cyc, o_wb_stb, o_wb_we, o_wb_addr, o_wb_data, i_wb_ack, i_wb_stall, i_wb_err, i_wb_data, i_int)
    if  args.cosimtrace:
		tb_cosim(args,i_clk,i_astb_n, i_dstb_n, i_write_n,i_depp, o_depp, o_wait,o_wb_cyc, o_wb_stb, o_wb_we, o_wb_addr, o_wb_data,i_wb_ack, i_wb_stall, i_wb_err, i_wb_data, i_int)        
if __name__ == '__main__':
    main()
