from myhdl import *
for i in range(-127,128,1):
	x = intbv(i)[8:]
	print i, bin(x,8), x, x.signed()
