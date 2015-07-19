from myhdl import *
from signed2twoscomplement import signed2twoscomplement
from mux import mux_data
from ram import ram
from lift_step import lift_step
from odd_even_fsm import *
#, SOF, state, syncFlag,

from pc_read import pc_read

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
we_in = Signal(bool(0))
we_1 = Signal(bool(0))
addr_1 = Signal(intbv(0)[8:])
addr_in = Signal(intbv(0)[8:])
 
toLift_Step = Signal(intbv(0)[W0:])
data_in = Signal(intbv(0)[W0:])

pc_data_in = Signal(intbv(0)[2:])
pc_data_rdy = Signal(intbv(0)[2:])

datactn_in = Signal(intbv(0)[8:])
datactn = Signal(intbv(0)[8:])
z = Signal(intbv(0)[W0:])
muxsel_i = Signal(bool(0))
muxaddrsel = Signal(intbv(0)[2:])

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
rst_fsm = Signal(bool(1))

addr_left = Signal(intbv(0)[8:])
addr_sam = Signal(intbv(0)[8:])
addr_rht = Signal(intbv(0)[8:])
state = Signal(t_State.INIT)

def top_lift_step(clk, dout, din,  data_in, toLift_Step, z,we_1, we, we_in,  addr, addr_in, muxsel_i, x, res_o, left_i, right_i, sam_i,flgs_i, update_i, update_o, rst_fsm, datactn_in, datactn, pc_data_in, pc_data_rdy , muxaddrsel, addr_left, addr_sam, addr_rht ):
	'''toLift_Step used for mapping datatodut from usb hostio
	datatodut is an alias of toSub_s
	datactn used for mapping datactn from usb hostio
	datactn is an alias of toSub_s'''
	instance_lift_step = lift_step(left_i, sam_i, right_i, flgs_i, update_i, clk, res_o, update_o)
	instance_ram = ram(dout, din, addr, we, clk)
	instance_mux_data =  mux_data(z, din, data_in, we_1, we, we_in, addr, addr_in, muxsel_i, muxaddrsel, addr_left, addr_sam, addr_rht)
	instance_Odd_Even_Fsm = Odd_Even_Fsm( state, clk, rst_fsm, addr_left, muxsel_i, addr_sam, addr_rht, muxaddrsel, we_1, dout, left_i, sam_i, right_i )
	instance_signed2twoscomplement = signed2twoscomplement(clk, x, z)
	
	
	instance_pc_read = pc_read(clk, data_in, toLift_Step, we_in, addr_in, muxsel_i, datactn_in, datactn, pc_data_in, pc_data_rdy  )
	return instances()

def tb(clk, dout, din, data_in, toLift_Step, z, we_1, we, we_in, addr_1, addr, addr_in, muxsel_i, x, res_o, left_i, right_i, sam_i, flgs_i, update_i, update_o, rst_fsm, datactn_in, datactn, pc_data_in, pc_data_rdy):
	instance_lift_step = lift_step(left_i, sam_i, right_i, flgs_i, update_i, clk, res_o, update_o)
	instance_ram = ram(dout, din, addr, we, clk) 
	instance_mux_data =  mux_data(z, din, data_in, we_1, we, we_in,  addr, addr_in, muxsel_i, muxaddrsel, addr_left, addr_sam, addr_rht)
	instance_signed2twoscomplement = signed2twoscomplement(clk, x, z)
	 
	 
	instance_pc_read = pc_read(clk, data_in, toLift_Step, we_in, addr_in, muxsel_i, datactn_in, datactn, pc_data_in, pc_data_rdy  )
	
	@always(delay(10))
	def clkgen():
		clk.next = not clk
	
	@instance
	def stimulus():
		dummy = 100000
		muxsel_i.next = 0
		
		while(muxsel_i == 0):
			print( "%d wait for data ") % (now() )
			yield clk.posedge
			dummy = dummy - 1
			if ( dummy == 0):
				muxsel_i.next = 1
				yield clk.posedge
				
		i = 0
		j = 0
		print( "%d at start ") % (now() )
		while(muxsel_i == 1):
			toLift_Step.next = m[j][i]
			yield clk.posedge
			print( "%d addr %d, data %d") % (now(), addr_in , data_in)
			#yield clk.posedge
			j = j + 1
		print ("%d pc_read done") % (now())
		we_1.next = 0
		flgs_i.next = 7
		yield clk.posedge		
		for i in range(w):
			for j in range(1, h-1,2):
				we_1.next = 0
				yield clk.posedge
				flgs_i.next = 7
				yield clk.posedge
				addr_1.next = j - 1
				yield clk.posedge
				left_i.next = dout
				yield clk.posedge
				addr_1.next = j + 1
				yield clk.posedge
				right_i.next = dout
				yield clk.posedge
				addr_1.next = j 
				yield clk.posedge
				sam_i.next = dout
				yield clk.posedge
				we_1.next = 1
				yield clk.posedge
				print( "time %d ") % (now())
				print( "left %d sam %d right %d") % (left_i, sam_i, right_i)
				update_i.next = 1
				yield clk.posedge
				update_i.next = 0
				yield clk.posedge
				x.next = res_o[W0:]
				yield clk.posedge
				#m[j][i] = z
				print( "time %d") % (now())
				print( "j %d i %d z %d") % (j, i, z)
				yield clk.posedge
		flgs_i.next = 6
		for i in range(w):
			for j in range(2, h, 2):
				addr_1.next = j	
				yield clk.posedge
				left_i.next = m[j - 1][i]
				yield clk.posedge
				right_i.next = m[j + 1][i]
				yield clk.posedge
				sam_i.next = m[j][i]
				yield clk.posedge
				print( "time %d ") % (now())
				print( "left %d sam %d right %d") % (left_i, sam_i, right_i)
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
tb_fsm = traceSignals( tb,clk, dout, din, data_in, toLift_Step, z, we_1, we, we_in, addr_1, addr, addr_in, muxsel_i, x, res_o, left_i, right_i, sam_i, flgs_i, update_i, update_o, rst_fsm, datactn_in, datactn, pc_data_in, pc_data_rdy)
sim = Simulation(tb_fsm)
sim.run()
#toVHDL(top_lift_step, clk, dout, din, data_in, toLift_Step, z, we_1, we, we_in, addr, addr_in, muxsel_i, x, res_o, left_i, right_i, sam_i, flgs_i, update_i, update_o, rst_fsm, datactn_in, datactn, pc_data_in, pc_data_rdy, muxaddrsel, addr_left, addr_sam, addr_rht) 
