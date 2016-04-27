import myhdl
from myhdl import *
import os
import argparse
from argparse import Namespace
'''
tb_dut = _prep_cosimi_clk=i_clk,i_astb_n=i_astb_n,i_dstb_n=i_dstb_n,
i_write_n=i_write_n,i_depp=i_depp,o_depp=o_depp,o_wait=o_wait,
o_wb_cyc=o_wb_cyc,o_wb_stb=o_wb_stb=o_wb_stb,o_wb_addr=o_wb_addr,
o_wb_data=o_wb_data,i_wb_ack=i_wb_ack,i_wb_stall=i_wb_stall,
i_wb_err=i_wb_err,i_wb_data=i_wb_data,i_int=i_int)
'''
i_clk  = Signal(bool(0))
reset = Signal(bool(0))
reset_dly_cnt = Signal(intbv(0)[5:]) 
#DEPP interface
i_astb_n = Signal(bool(0))
i_dstb_n = Signal(bool(0))
i_write_n = Signal(bool(0))
o_depp = Signal(intbv(0)[8:])
i_depp = Signal(intbv(0)[8:])
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
def wbdepp(i_clk,i_astb_n, i_dstb_n, i_write_n,i_depp, o_depp, o_wait,o_wb_cyc, o_wb_stb, o_wb_we, o_wb_addr, o_wb_data,i_wb_ack,i_wb_stall, i_wb_err, i_wb_data, i_int):
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
                x_dstb_n.next = 1
                r_dstb_n.next = 1
                l_dstb_n.next = 1
                x_astb_n.next = 1
                r_astb_n.next = 1
                l_astb_n.next = 1
                o_wb_cyc.next = 1
                o_wb_stb.next = 1
                #addr.next = 0  				
        else:
            reset.next = 0

    @always(i_clk.posedge)
    def rtl():
        if ((w_write)and(astb)):
			addr.next = r_depp
        #if ((w_write)and(dstb)and(addr[7:3]==5'h00)):
    @always(i_clk.posedge)
    def rtl():
		'''
		{ x_dstb_n, x_astb_n, x_write_n, x_depp }
			<= { i_dstb_n, i_astb_n, i_write_n, i_depp };
		{ r_dstb_n, r_astb_n, r_write_n, r_depp }
			<= { x_dstb_n, x_astb_n, x_write_n, x_depp };
		{ l_dstb_n, l_astb_n } <= { r_dstb_n, r_astb_n };
		x_dstb_n.next = i_dstb_n
		x_astb_n.next = i_astb_n
		x_write_n.next = i_write_n
		x_depp.next =  i_depp                 
		'''
        	
    return myhdl.instances()
def tb_cosim(args,i_clk,i_astb_n, i_dstb_n, i_write_n,i_depp, o_depp, o_wait,
	o_wb_cyc, o_wb_stb, o_wb_we, o_wb_addr, o_wb_data,
	i_wb_ack, i_wb_stall, i_wb_err, i_wb_data, i_int):
    
    tb_dut = _prep_cosim(args,i_clk=i_clk,i_astb_n=i_astb_n,i_dstb_n=i_dstb_n, \
    i_write_n=i_write_n,i_depp=i_depp,o_depp=o_depp,o_wait=o_wait, \
    o_wb_cyc=o_wb_cyc,o_wb_stb=o_wb_stb,o_wb_we=o_wb_we,o_wb_addr=o_wb_addr, \
    o_wb_data=o_wb_data,i_wb_ack=i_wb_ack,i_wb_stall=i_wb_stall, \
    i_wb_err=i_wb_err,i_wb_data=i_wb_data,i_int=i_int)
    
     
    
    @always(delay(10))
    def clkgen():
        i_clk.next = not i_clk
    @instance
    def tbstim():
       for i in range(100):
           yield i_clk.posedge
       r_depp.next = 208
       yield i_clk.posedge
       w_write.next = 1
       yield i_clk.posedge
       yield i_clk.posedge
       astb.next = 1
       yield i_clk.posedge
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
    parser.add_argument("--build", default=False, action='store_true')
    parser.add_argument("--trace", default=False, action='store_true')
    parser.add_argument("--convert", default=False, action='store_true')
    parser.add_argument("--cosim", default=False, action='store_true')
    parser.add_argument("--cosimtrace", default=False, action='store_true')
    args = parser.parse_args()
    return args    
def _prep_cosim(args, **sigs):
    """ prepare the cosimulation environment
    """
    print ("  *%s" %  (sigs))   
    print("compiling ...")
    cmd = "iverilog -o ifdeppsimple tb/wbdeppsimple.v tb/tb_wbdeppsimple.v"
    print("  %s" %  (cmd))
    os.system(cmd)
    # get the handle to the
    print("cosimulation setup ...")
    cmd = "vvp -m ./myhdl.vpi ifdeppsimple"
    print("  %s" %  (cmd))
    cosim = Cosimulation(cmd, **sigs)
    print("  %s" %  (cosim))
    return cosim
def convert():        
    toVerilog(wbdepp,i_clk,i_astb_n, i_dstb_n, i_write_n,i_depp, o_depp, o_wait, o_wb_cyc, o_wb_stb, o_wb_we, o_wb_addr, o_wb_data, i_wb_ack, i_wb_stall, i_wb_err, i_wb_data, i_int) 

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

    if args.convert: 
		convert()
    if args.cosim:
        test_prep = test_cosim_prep(args,i_clk,i_astb_n, i_dstb_n, i_write_n,i_depp, o_depp, o_wait, o_wb_cyc, o_wb_stb, o_wb_we, o_wb_addr, o_wb_data, i_wb_ack, i_wb_stall, i_wb_err, i_wb_data, i_int)
    if  args.cosimtrace:
		tb_cosim(args,i_clk,i_astb_n, i_dstb_n, i_write_n,i_depp, o_depp, o_wait,o_wb_cyc, o_wb_stb, o_wb_we, o_wb_addr, o_wb_data,i_wb_ack, i_wb_stall, i_wb_err, i_wb_data, i_int)        
if __name__ == '__main__':
    main()
