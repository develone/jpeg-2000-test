from myhdl import *
#from myhdl._fixbv import FixedPointFormat as fpf
ww = (32,9)
x_sig = Signal(intbv(0)[ww[0]:])
y_sig = Signal(intbv(0)[ww[0]:])
sum_sig = Signal(intbv(0)[ww[0]:])
prod_sig = Signal(intbv(0)[2*ww[0]:])
clk = Signal(bool(0))
do_add = Signal(bool(0))
do_mul = Signal(bool(0))
wL = ww[0]
wI = (wL - ww[1]) - 1
wF = wL - wI
print  wL, wI, wF
x = fixbv(3.141592)[ww]
#ww = (32,12)  32 19 13
# 2109876543210 1234567890123456789
# 0000000000011 0010010000111111011
# siiiiiiiiiiii.fffffffffffffffffff

#ww = (32,9) frac 32 22 10
# 9876543210 1234567890123456789012
# 0000000011 0010010000111111011000 
# siiiiiiiii.ffffffffffffffffffffff

#ww = (32,8) frac 32 23 9
# 876543210 12345678901234567890123
# 000000011 00100100001111110110000 
# siiiiiiii.fffffffffffffffffffffff
#print bin(x, wL)
y = fixbv(0.5)[ww]

z = x * y
z1 = fixbv(z)[ww]
'''
print float(x), int(x), repr(x)
print float(y), int(y), repr(y)
print float(z), int(z), repr(z)
print float(z1), int(z1), repr(z1)
print

z = x + y
z1 = fixbv(z)[ww]
print float(x), int(x), repr(x)
print float(y), int(y), repr(y)
print float(z), int(z), repr(z)
print float(z1), int(z1), repr(z1) 
print

z = x - y
z1 = fixbv(z)[ww]
print float(x), int(x), repr(x)
print float(y), int(y), repr(y)
print float(z), int(z), repr(z)
print float(z1), int(z1), repr(z1) 
print

z = y - x
z1 = fixbv(z)[ww]
print float(x), int(x), repr(x)
print float(y), int(y), repr(y)
print float(z), int(z), repr(z)
print float(z1), int(z1), repr(z1)
''' 
def fixbv_add(clk, do_add, x_sig, y_sig, sum_sig):
	@always(clk.posedge)
	def add_rtl():
		if (do_add == 1):
			sum_sig.next = x_sig + y_sig
		else:
			sum_sig.next = 0
	return add_rtl

def fixbv_mul(clk, do_prod, x_sig, y_sig, prod_sig):
	@always(clk.posedge)
	def add_rtl():
		if (do_mul == 1):
			prod_sig.next = x_sig * y_sig
		else:
			prod_sig.next = 0
	return add_rtl
toVHDL(fixbv_add, clk, do_add, x_sig, y_sig, sum_sig)
toVerilog(fixbv_add, clk, do_add, x_sig, y_sig, sum_sig)
toVHDL(fixbv_mul, clk, do_mul, x_sig, y_sig, prod_sig)
toVerilog(fixbv_mul, clk, do_mul, x_sig, y_sig, prod_sig)
def tb():
        dut_fixbv_add = fixbv_add(clk, do_add, x_sig, y_sig, sum_sig)
	dut_fixbv_mul = fixbv_mul(clk, do_mul, x_sig, y_sig, prod_sig)
	@always(delay(10))
    	def clkgen():
        	clk.next = not clk
	@instance
   	def stimulus():

        	for i in range(10):
        	    print( "%3d ") % (now())
         	    yield clk.posedge
		    x_sig.next = 13176792
		    yield clk.posedge
		    y_sig.next = 2097152
		    yield clk.posedge
		    do_add.next = 1
		    yield clk.posedge 
		    do_add.next = 0
		    yield clk.posedge
		    do_mul.next = 1
		    yield clk.posedge 
		    do_mul.next = 0
		    yield clk.posedge   
		raise StopSimulation
	return clkgen, stimulus, dut_fixbv_add, dut_fixbv_mul
z = x + y
z1 = fixbv(z)[ww]
print float(x), int(x), repr(x), hex(x)
print float(y), int(y), repr(y), hex(y)
print float(z), int(z), repr(z), hex(z)

z = x * y
z1 = fixbv(z)[ww]
print float(x), int(x), repr(x), hex(x)
print float(y), int(y), repr(y), hex(y)
print float(z), int(z), repr(z), hex(z)
print float(z1), int(z1), repr(z1), hex(z1)

tb_fsm = traceSignals(tb)
sim = Simulation(tb_fsm)
sim.run()
