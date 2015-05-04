from myhdl import *
#from myhdl._fixbv import FixedPointFormat as fpf
ww = (32,9)
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
print bin(x, wL)
y = fixbv(0.5)[ww]

z = x * y
z1 = fixbv(z)[ww]
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
