from myhdl import *
from add_mul import *
def top_level(d3,a2,clk,x2,x3,x4,x5,p,even_odd,fwd_inv,n=8):
	""" Function doc """
	d3 = (Signal(fixbv(0)[ww]) for i in range(n))
	a2 = (Signal(fixbv(0)[ww]) for i in range(n))
	x2 = (Signal(fixbv(156)[ww]) for i in range(n))
	x3 = (Signal(fixbv(164)[ww]) for i in range(n))
	x4 = (ignal(fixbv(156)[ww]) for i in range(n))
	x5 = (Signal(fixbv(156)[ww]) for i in range(n))
	clk = Signal(bool(0))
	even_odd = (Signal(bool(0)) for i in range(n)) 
	p = (Signal(bool(0)) for i in range(n))
	fwd_inv = (Signal(bool(0)) for i in range(n))
	
	
	for i in range(n):
		add_mul_inst[i] = add_mul(d3[i],a2[i],clk,x2[i],x3[i],x4[i],x5[i],p[i],even_odd[i],fwd_inv[i])
	return  inst


top_level(d3,a2,clk,x2,x3,x4,x5,p,even_odd,fwd_inv,4)

 

