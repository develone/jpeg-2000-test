from myhdl import *
import  random
#from myhdl._fixbv import FixedPointFormat as fpf



def disp_fix(x_i):
        iW = x_i._W
	print float(x_i), int(x_i), repr(x_i), hex(x_i), bin(x_i, iW[0])

x = (fixbv(3.1415926535897932, min = -2**10, max=2**10, res=1e-6))
#disp_fix(x)
y = (fixbv(510.5, min = -2**10, max=2**10, res=1e-6))
#disp_fix(y)
iW = x._W

ww = (x._nrbits,iW[1])
 
x = fixbv(3.141592)[ww]
y = fixbv(510.5)[ww] 
  
x_sig = Signal(intbv(0, min = -2**(x._nrbits-1), max = 2**(x._nrbits-1) ))
y_sig = Signal(intbv(0, min = -2**(x._nrbits-1), max = 2**(x._nrbits-1) ))

sum_sig = Signal(intbv(0)[ww[0]+1:])
sub_sig = Signal(intbv(0, min = -2**(x._nrbits), max = 2**(x._nrbits) ))
 

prod_sig = Signal(intbv(0)[2*ww[0]:])
clk = Signal(bool(0))
do_add = Signal(bool(0))
do_mul = Signal(bool(0))
do_sub = Signal(bool(0))

done_add = Signal(bool(0))
done_sub = Signal(bool(0))
done_mul = Signal(bool(0)) 
 
def fixbv_sub(clk, do_sub, x_sig, y_sig, sub_sig, done_sub):
	@always(clk.posedge)
	def sub_rtl():
		if (do_sub == 1):
                        done_sub.next = 0
			sub_sig.next = x_sig - y_sig
		else:
			done_sub.next = 1
			sub_sig.next = 0
	return sub_rtl

def fixbv_add(clk, do_add, x_sig, y_sig, sum_sig, done_add):
	@always(clk.posedge)
	def add_rtl():
		if (do_add == 1):
                        done_add.next = 0
			sum_sig.next = x_sig + y_sig
		else:
			done_add.next = 1
			sum_sig.next = 0
	return add_rtl

 
def fixbv_mul(clk, do_mul, x_sig, y_sig, prod_sig, done_mul):
	@always(clk.posedge)
	def add_rtl():
		if (do_mul == 1):
			done_mul.next = 0
			prod_sig.next = x_sig * y_sig
		else:
			done_mul.next = 1
			prod_sig.next = 0
	return add_rtl
toVHDL(fixbv_add, clk, do_add, x_sig, y_sig, sum_sig, done_add)
toVerilog(fixbv_add, clk, do_add, x_sig, y_sig, sum_sig, done_add)

toVHDL(fixbv_sub, clk, do_sub, x_sig, y_sig, sub_sig, done_sub)
toVerilog(fixbv_sub, clk, do_sub, x_sig, y_sig, sub_sig, done_sub)

toVHDL(fixbv_mul, clk, do_mul, x_sig, y_sig, prod_sig, done_mul)
toVerilog(fixbv_mul, clk, do_mul, x_sig, y_sig, prod_sig, done_mul)


def tb():
        dut_fixbv_add = fixbv_add(clk, do_add, x_sig, y_sig, sum_sig, done_add)
	dut_fixbv_sub = fixbv_sub( clk, do_sub, x_sig, y_sig, sub_sig, done_sub)
	dut_fixbv_mul = fixbv_mul(clk, do_mul, x_sig, y_sig, prod_sig, done_mul)
 
	@always(delay(10))
    	def clkgen():
        	clk.next = not clk
	@instance
   	def stimulus():

        	for i in range(10):
        	    print( "%3d ") % (now())
         	    yield clk.posedge
		    x_sig.next = int(x)
		    yield clk.posedge
		    y_sig.next = int(y)
		    yield clk.posedge
		    do_add.next = 1
		    yield clk.posedge 
		    do_add.next = 0
		    yield clk.posedge
                    
                    do_sub.next = 1
		    yield clk.posedge 
		    do_sub.next = 0
		    yield clk.posedge

		    do_mul.next = 1
		    yield clk.posedge 
		    do_mul.next = 0
		    yield clk.posedge
                      
		raise StopSimulation
	return clkgen, stimulus, dut_fixbv_add, dut_fixbv_sub, dut_fixbv_mul
print 'x + y'
z = x + y
disp_fix(x)
disp_fix(y)
disp_fix(z)
#z1 = fixbv(z)[ww]
z = x - y
print 'x - y'
disp_fix(z)
 
print 'x * y'
z = x * y
disp_fix(z)
#z1 = fixbv(z)[ww]
 

tb_fsm = traceSignals(tb)
sim = Simulation(tb_fsm)
sim.run()
