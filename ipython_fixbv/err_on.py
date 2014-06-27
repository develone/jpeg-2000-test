from myhdl import *
from add_mul_sim import *
x2 = fixbv(0)
x3 = fixbv(0)
p = bool(0)
w = (20,10)
even_odd=bool(0)
x4 = fixbv(-351.750000)[w]
x5 = fixbv(-356.375000)[w]
d3 = fixbv(0)
a2 = fixbv(0)
d_instance = add_mul_sim(d3,a2,x2,x3,x4,x5,p,even_odd)
print d_instance[0],d_instance[1]
