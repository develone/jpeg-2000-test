from myhdl import *

ww = (24,14)
d3 = Signal(fixbv(0)[ww])
a2 = Signal(fixbv(0)[ww])
x2 = Signal(fixbv(156)[ww])
x3 = Signal(fixbv(164)[ww])
x4 = Signal(fixbv(156)[ww])
x5 = Signal(fixbv(156)[ww])
clk = Signal(bool(0))
even_odd = Signal(bool(0)) 
p = Signal(bool(0))
fwd_inv = Signal(bool(0))
# With 4 instances of add_mul 8 pixels are worked
sig_list = [[d3,a2,clk,x2,x3,x4,x5,p,even_odd,fwd_inv],
[d3,a2,clk,x2,x3,x4,x5,p,even_odd,fwd_inv],
[d3,a2,clk,x2,x3,x4,x5,p,even_odd,fwd_inv],
[d3,a2,clk,x2,x3,x4,x5,p,even_odd,fwd_inv]]
print 'sig_list0 ',sig_list[0]
print
print 'sig_list1 ',sig_list[1]

print 'sig_list2 ',sig_list[2]
print
print 'sig_list3 ',sig_list[3]
print sig_list[0][9]
sig_list[0][9] = True
print sig_list[0][9]

print sig_list[0][3]
sig_list[0][3] = Signal(fixbv(200)[ww])
print sig_list[0][3]
from  add_mul_m import add_mul

def top_level (d3,a2,clk,x2,x3,x4,x5,p,even_odd,fwd_inv,n=8):
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
		inst[i] = add_mul(d3[i],a2[i],clk,x2[i],x3[i],x4[i],x5[i],p[i],even_odd[i],fwd_inv[i])
	return  inst
	
a = top_level(d3,a2,clk,x2,x3,x4,x5,p,even_odd,fwd_inv,4)

 
