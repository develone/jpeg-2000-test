from myhdl import *
from add_mul_sim import add_mul_sim
x2 = fixbv(164)
x3 = fixbv(156)
x4 = fixbv(0)
x5 = fixbv(0)
d3 = fixbv(0)
a2 = fixbv(0)
p = bool(0)
odd_even = bool(1)
d_instance = add_mul_sim(d3,a2,x2,x3,x4,x5,p,odd_even)
print d_instance[0]

d3 = fixbv(0)
a2 = fixbv(0)
x2 = fixbv(0)
x3 = fixbv(0)
x4 = fixbv(164)
x5 = fixbv(156)
p = bool(0)
odd_even = bool(0)
d_instance = add_mul_sim(d3,a2,x2,x3,x4,x5,p,odd_even)
print d_instance[1]

x2 = fixbv(146)
x3 = fixbv(200)
x4 = fixbv(0)
x5 = fixbv(0)
p = bool(1)
odd_even = bool(1)
d_instance = add_mul_sim(d3,a2,x2,x3,x4,x5,p,odd_even)
print d_instance[0]
x4 = fixbv(146)
x5 = fixbv(200)
p = bool(1)
odd_even = bool(0)
d_instance = add_mul_sim(d3,a2,x2,x3,x4,x5,p,odd_even)
print d_instance[1]
