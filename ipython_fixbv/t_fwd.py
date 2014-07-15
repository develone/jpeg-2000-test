from myhdl import *
from add_mul_sim_53 import *
m = [156.0, 156.0, 164.0, 164.0, 164.0, 164.0, 156.0, 164.0, 156.0, 164.0, 148.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 164.0, 164.0, 164.0, 172.0, 172.0, 172.0, 172.0, 172.0, 164.0, 148.0, 156.0, 124.0, 116.0, 92.0, 92.0, 84.0, 108.0, 108.0, 100.0, 100.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 108.0, 100.0, 108.0, 108.0, 116.0, 116.0, 124.0, 116.0, 124.0, 124.0, 116.0, 116.0, 124.0, 124.0, 132.0, 132.0, 132.0, 124.0, 132.0, 132.0, 132.0, 132.0, 124.0, 132.0, 132.0, 132.0, 124.0, 124.0, 124.0, 132.0, 140.0, 124.0, 132.0, 132.0, 132.0, 132.0, 132.0, 140.0, 132.0, 140.0, 132.0, 132.0, 132.0, 132.0, 140.0, 132.0, 132.0, 140.0, 132.0, 132.0, 132.0, 132.0, 132.0, 140.0, 132.0, 140.0, 132.0, 132.0, 124.0, 132.0, 132.0, 132.0, 132.0, 132.0, 140.0, 132.0, 132.0, 132.0, 132.0, 124.0, 132.0, 140.0, 132.0, 132.0, 132.0, 132.0, 132.0, 124.0, 132.0, 140.0, 132.0, 132.0, 124.0, 132.0, 124.0, 140.0, 132.0, 132.0, 132.0, 124.0, 140.0, 132.0, 124.0, 124.0, 132.0, 124.0, 132.0, 132.0, 132.0, 132.0, 124.0, 132.0, 124.0, 124.0, 124.0, 116.0, 124.0, 116.0, 108.0, 116.0, 100.0, 100.0, 116.0, 124.0, 132.0, 140.0, 148.0, 156.0, 156.0, 156.0, 164.0, 164.0, 156.0, 148.0, 156.0, 156.0, 148.0, 148.0, 156.0, 156.0, 148.0, 156.0, 156.0, 156.0, 148.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 156.0, 164.0, 156.0, 156.0, 156.0, 156.0, 188.0, 204.0, 212.0, 212.0, 220.0, 220.0, 220.0, 212.0, 196.0, 148.0, 108.0, 100.0, 100.0, 100.0, 116.0, 124.0, 116.0, 116.0, 132.0, 124.0, 116.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 124.0, 116.0, 124.0, 132.0, 124.0, 124.0, 124.0, 124.0, 124.0, 116.0, 132.0, 132.0, 124.0, 124.0, 124.0, 132.0, 132.0, 116.0, 116.0, 116.0, 116.0, 124.0, 132.0, 164.0, 172.0, 156.0]
#print len(m)
mm = m
#print m[:]
pix = Add_mul_top()
#1
pix.setSig_p(0)
pix.setSig_even_odd(1)
pix.setSig_fwd_inv(1)

"""odd samples"""
"""p False even_odd True fwd_inv True #1"""
for i in range(1,255,2):

	pix.setSig_left(int(m[i-1]))
	pix.setSig_right(int(m[i+1]))
	pix.setSig_sam(int(m[i]))
	even,odd = add_mul_ram(pix)
	m[i] = float(even)
#print m[:]

#2
pix.setSig_p(0)
pix.setSig_even_odd(0)
pix.setSig_fwd_inv(1)
for i in range(2,256,2):

	pix.setSig_left(int(m[i-1]))
	pix.setSig_right(int(m[i+1]))
	pix.setSig_sam(int(m[i]))
	even,odd = add_mul_ram(pix)
	m[i] = float(odd)
#print m[:]
#3

pix.setSig_p(1)
pix.setSig_even_odd(1)
pix.setSig_fwd_inv(1)
for i in range(1,255,2):

	pix.setSig_left(int(m[i-1]))
	pix.setSig_right(int(m[i+1]))
	pix.setSig_sam(int(m[i]))
	even,odd = add_mul_ram(pix)
	m[i] = float(even)
#print m[:]
#4
pix.setSig_p(1)
pix.setSig_even_odd(0)
pix.setSig_fwd_inv(1)
for i in range(2,256,2):

	pix.setSig_left(int(m[i-1]))
	pix.setSig_right(int(m[i+1]))
	pix.setSig_sam(int(m[i]))
	even,odd = add_mul_ram(pix)
	m[i] = float(odd)
#print m[:]
#44
pix.setSig_p(1)
pix.setSig_even_odd(0)
pix.setSig_fwd_inv(0)
for i in range(2,256,2):

	pix.setSig_left(int(m[i-1]))
	pix.setSig_right(int(m[i+1]))
	pix.setSig_sam(int(m[i]))
	even,odd = add_mul_ram(pix)
	m[i] = float(odd)
#print m[:]

#33
pix.setSig_p(1)
pix.setSig_even_odd(1)
pix.setSig_fwd_inv(0)
for i in range(1,255,2):

	pix.setSig_left(int(m[i-1]))
	pix.setSig_right(int(m[i+1]))
	pix.setSig_sam(int(m[i]))
	even,odd = add_mul_ram(pix)
	m[i] = float(even)
#print m[:]

 
#22
pix.setSig_p(0)
pix.setSig_even_odd(0)
pix.setSig_fwd_inv(0)
for i in range(2,256,2):

	pix.setSig_left(int(m[i-1]))
	pix.setSig_right(int(m[i+1]))
	pix.setSig_sam(int(m[i]))
	even,odd = add_mul_ram(pix)
	m[i] = float(odd)
#print m[:]

#11

pix.setSig_p(0)
pix.setSig_even_odd(1)
pix.setSig_fwd_inv(0)

"""odd samples"""
"""p False even_odd True fwd_inv True #1"""
for i in range(1,255,2):

	pix.setSig_left(int(m[i-1]))
	pix.setSig_right(int(m[i+1]))
	pix.setSig_sam(int(m[i]))
	even,odd = add_mul_ram(pix)
	m[i] = float(even)
#print m[:] 
#156.0, 156.0, 164.0, 164.0, 164.0, 164.0, 156.0
#156.0, -4.0, 164.0, 0.0, 164.0, 4.0, 156.0, 8.0 #1 chg 1 3 5
#156.0, -4.0, 163.0, 0.0, 165.0, 4.0, 159.0, 8.0 #2 chg 2 4 6
#156.0, -163.0, 163.0, -163.0, 165.0, -157.0, 159.0, -151.0 #3 1 3 5
#156.0, -163.0, 82.0, -163.0, 85.0, -157.0, 82.0, -151.0 #4 2 4 6

for i in range(256):
	d = mm[i] -m[i]
	assert d == 0
