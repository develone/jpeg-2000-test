from myhdl import *
from signed2twoscomplement import signed2twoscomplement
from mux import mux_data
from ram import ram
from lift_step import lift_step
from fsm3 import *
from PIL import Image
W0 = 9
im = Image.open("../../lena_256.png")
pix = im.load()
w, h = im.size
m = list(im.getdata())
#print m.__sizeof__()
m = [m[i:i+im.size[0]] for i in range(0, len(m), im.size[0])]
#print m

dout = Signal(intbv(0)[W0:])
din = Signal(intbv(0)[W0:])
addr = Signal(intbv(0)[8:])
we = Signal(bool(0))
clk = Signal(bool(0))

data_in = Signal(intbv(0)[W0:])
z = Signal(intbv(0)[W0:])
muxsel_i = Signal(bool(0))

x = Signal(intbv(0, min= -(2**(W0)) ,max= (2**(W0))))
res_o = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
left_i = Signal(intbv(0)[W0:])
right_i = Signal(intbv(0)[W0:])
sam_i = Signal(intbv(0)[W0:])
flgs_i = Signal(intbv(0)[4:])

update_i = Signal(bool(0))
update_o = Signal(bool(0))

SOF = Signal(bool(0))
syncFlag = Signal(bool(0))
reset_n = Signal(bool(1))
state = Signal(t_State.SEARCH)

def top_lift_step(clk, dout, din, addr, we, data_in, z,
 muxsel_i, x, res_o, left_i, right_i, sam_i,
 flgs_i, update_i, update_o, SOF, state, syncFlag, reset_n  ):
	instance_lift_step = lift_step(left_i, sam_i, right_i, flgs_i, update_i, clk, res_o, update_o)
	instance_ram = ram(dout, din, addr, we, clk)
	instance_mux_data =  mux_data(z, din, data_in, muxsel_i)
	instance_signed2twoscomplement = signed2twoscomplement(clk, x, z)
	instance_fsm = FramerCtrl(SOF, state, syncFlag, clk, reset_n) 
	return instances()
def tb(clk, dout, din, addr, we, data_in, z, muxsel_i, x, res_o, left_i, right_i, sam_i, flgs_i, update_i, update_o, SOF, state, syncFlag, reset_n  ):
	instance_lift_step = lift_step(left_i, sam_i, right_i, flgs_i, update_i, clk, res_o, update_o)
	instance_ram = ram(dout, din, addr, we, clk)
	instance_mux_data =  mux_data(z, din, data_in, muxsel_i)
	instance_signed2twoscomplement = signed2twoscomplement(clk, x, z)
	instance_fsm = FramerCtrl(SOF, state, syncFlag, clk, reset_n)
	@always(delay(10))
     	def clkgen():
        	clk.next = not clk

    	@instance
   	def stimulus():

		for i in range(10):
			print( "%3d ") % (now())
 		
			yield clk.posedge
		addr.next = 1
				
		muxsel_i.next = 0
		yield clk.posedge
		
		yield clk.posedge
		for i in range(3):
 			for i in (4, 8, 8, 12):
				syncFlag.next = 1
				yield clk.posedge
				syncFlag.next = 0
				yield clk.posedge
		we.next = 1
		yield clk.posedge
		muxsel_i.next = 1
		i = 0
		for j in range(256):
			 
			addr.next = j
			yield clk.posedge
			data_in.next = m[j][i]
			yield clk.posedge
			print( "%3d %d, %d") % (now(), j , din)
		muxsel_i.next = 1
		yield clk.posedge
		we.next = 0
		yield clk.posedge
		flgs_i.next = 7
		yield clk.posedge		
		for i in range(w):
			for j in range(1, h-1,2):
				we.next = 0
				yield clk.posedge
				flgs_i.next = 7
				yield clk.posedge
				addr.next = j - 1
				yield clk.posedge
				left_i.next = dout
				yield clk.posedge
				addr.next = j + 1
				yield clk.posedge
				right_i.next = dout
				yield clk.posedge
				addr.next = j 
				yield clk.posedge
				sam_i.next = dout
				yield clk.posedge
    				we.next = 1
				yield clk.posedge
				print( "%3d %d %d %d") % (now(),left_i, sam_i, right_i)
				update_i.next = 1
				yield clk.posedge
				update_i.next = 0
				yield clk.posedge
				x.next = res_o[W0:]
				yield clk.posedge
				#m[j][i] = z
				print( "%3d %d %d %d") % (now(), j, i, z)
				yield clk.posedge
		flgs_i.next = 6
		for i in range(w):
			for j in range(2, h, 2):
				addr.next = j	
				yield clk.posedge
				left_i.next = m[j - 1][i]
				yield clk.posedge
				right_i.next = m[j + 1][i]
				yield clk.posedge
				sam_i.next = m[j][i]
				yield clk.posedge
				print( "%3d %d %d %d") % (now(),left_i, sam_i, right_i)
				update_i.next = 1
				yield clk.posedge
				update_i.next = 0
				yield clk.posedge
				x.next = res_o[W0:]
				yield clk.posedge
				m[j][i] = z
				yield clk.posedge
 
		raise StopSimulation
				
	return instances()
tb_fsm = traceSignals( tb, clk, dout, din, addr, we, data_in, z,
 muxsel_i, x, res_o, left_i, right_i, sam_i,
 flgs_i, update_i, update_o, SOF, state, syncFlag, reset_n  )

sim = Simulation(tb_fsm)
sim.run()
 
'''
toVHDL(top_lift_step, clk, dout, din, addr, we, data_in, z,
 muxsel_i, x, res_o, left_i, right_i, sam_i,
 flgs_i, update_i, update_o, SOF, state, syncFlag, reset_n   ) 
'''
