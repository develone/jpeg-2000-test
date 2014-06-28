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
import add_mul_m
def top_level (sig_list):
	""" Function doc """
	instance_0 = add_mul(sig_list[0])
	instance_1 = add_mul(sig_list[1])
	instance_2 = add_mul(sig_list[2])
	instance_3 = add_mul(sig_list[3])
	
