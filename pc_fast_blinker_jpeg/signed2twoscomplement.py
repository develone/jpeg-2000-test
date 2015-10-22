from myhdl import *
import random
'''unsigned data width signed is W0 + 1'''
W0 = 8

  
res_o = Signal(intbv(0, min= -(2**(W0)) ,max= (2**(W0))))
z = Signal(intbv(0)[W0:])
clk = Signal(bool(0))
def signed2twoscomplement(clk, res_o, z):
	
	@always(clk.posedge)
	def unsigned_logic():
		z.next = res_o

	return unsigned_logic
def convert():
	toVHDL(signed2twoscomplement, clk, res_o, z)
	toVerilog(signed2twoscomplement, clk, res_o, z)
def tb(clk, res_o, z):
    instance_1 = signed2twoscomplement(clk, res_o, z)
    @always(delay(10))
    def clkgen():
        clk.next = not clk
    @instance
    def stimulus():
        for i in range(0,2**(W0),1):
             
            res_o.next = i
            yield clk.posedge
            print ("%d %d %d %s %s ") % (res_o, z.signed(), z, bin(res_o,W0), bin(z, W0))
            print ("%d %d %d %s %s ") % (res_o, z.signed(), z, hex(res_o), hex(z))
            if( z.signed() < 0):
				print ("%d ") % (((2**W0)+z.signed()) + 1)
        raise StopSimulation
    return instances()
'''
tb_fsm = traceSignals(tb,clk, res_o, z)
sim = Simulation(tb_fsm)
sim.run()

convert()
'''
