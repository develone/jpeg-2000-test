from myhdl import *
from jpeg_utils import Add_shift_top
 

x = Add_shift_top()
@instance
def tbstim():
	print("%8d  %s" % (now(), x))
	x.setSig_state_update_sample()
	yield delay(1)
	print("%8d  %s" % (now(), x))
	x.setSig_state_transfer_out()
	yield delay(1)
	print("%8d  %s" % (now(), x))
	x.setSig_state_transfer_in()
	yield delay(1)
	print("%8d  %s" % (now(), x))
	raise StopSimulation

Simulation(tbstim).run()
