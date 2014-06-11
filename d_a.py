from myhdl import *
#jj2000/j2k/wavelet/analysis/AnWTFilterIntLift5x3.java
#    /** The low-pass synthesis filter of the 5x3 wavelet transform */
#    private final static float LPSynthesisFilter[] = 
#    { 0.5f, 1f, 0.5f };
#
#    /** The high-pass synthesis filter of the 5x3 wavelet transform */
#    private final static float HPSynthesisFilter[] =
#    { -0.125f, -0.25f, 0.75f, -0.25f, -0.125f };
#java JJ2KEncoder -v -i ../../lena_256.pgm -o lena_0_125.jpg -rate 0.125
#-rw-r--r-- 1 vidal users  975 Jun  7 07:22 lena_0_125.jpg
#-rw-r--r-- 1 vidal users 2003 Jun  7 07:23 lena_0_25.jpg
#-rw-r--r-- 1 vidal users 4053 Jun  7 07:23 lena_0_5.jpg
#-rw-r--r-- 1 vidal users 6093 Jun  7 07:23 lena_0_75.jpg
#-rw-r--r-- 1 vidal users 8146 Jun  7 07:23 lena_1.jpg
#[vidal@ws009 classes]$ ls -la ../../lena_256.pgm 
#Image index
#0 to 127 and 128 to 256
#0 to 63 and 64 to 128
#0 to 31 and 32 to 64

"""
PGM format example 
P5
# CREATOR: GIMP PNM Filter Version 1.1
256 256 width and height
255 The maximum gray value (Maxval), again in ASCII decimal. 
Must be less than 65536, and more than zero. 
"""
import pylab
import scipy
import scipy.misc as sg_m
import scipy.signal as sg
import numpy as np
def wr_img(sz,img_ar):
	f = open('test.pgm','w')
	f.write(hs0)
	f.write(hs1)
	f.write(hs2)
	f.write(hs3)

	for i in range(sz):
		for j in range(sz):
			f.write(str(img_ar[i,j]))
	f.close()	
def get_col(col_ind,img,wr_img_sz):
	#print col_ind
	for i in range(w_img_sz):
		col[i] = img[i,col_ind]
	return col
		
def get_row(row_id,img,w_img_sz):
	#print row_ind
	for j in range(w_img_sz):
		row[j] = img[row_id,j]
	return row	 

def get_img(f):		
	for i in range(256):
		for j in range(256):
			#print ord(f.read(1))
			img[i,j] =  ord(f.read(1))
			#print i,j	
	return img	
	
LPSynthesisFilter = np.array([ 0.5, 1, 0.5 ])
HPSynthesisFilter = np.array([ -0.125, -0.25, 0.75, -0.25, -0.125 ])
#print type(LPSynthesisFilter)
#print type(HPSynthesisFilter)
#print LPSynthesisFilter
#print HPSynthesisFilter
f = open('lena_256.pgm','r')
#for i in range(4):
#print f.readline()
hs0 = f.readline()
hs1 = f.readline()
hs2 = f.readline()
hs3 = f.readline()
print hs0
print hs1
print hs2
hs2 = '128 128 '
print hs3
ar_size = (256,256)
w_img_sz = 256
#now img is 2-dimensional of type int
#now row is 1-dimensional of type int
#now col is 1-dimensional of type int
#now rowl is 1-dimensional of type int
img = np.zeros(ar_size,dtype=np.int) 
img_odd = np.zeros((128,128),dtype=np.int) 
img_even = np.zeros((128,128),dtype=np.int)
col = np.zeros(w_img_sz,dtype=np.int)
row = np.zeros(256,dtype=np.int)
row_even = np.zeros(128,dtype=np.int)
row_odd = np.zeros(128,dtype=np.int)
col_even = np.zeros(64,dtype=np.int)
col_odd = np.zeros(64,dtype=np.int)
ar_size = (128,128)
D = np.zeros(ar_size,dtype=np.int)
A = np.zeros(ar_size,dtype=np.int)	
#DD & AA are 128 following the downsample
ar_size = (256,256)
DD = np.zeros(ar_size,dtype=np.int)
AA = np.zeros(ar_size,dtype=np.int)
ar_size = (128,128)	
DDD = np.zeros(ar_size,dtype=np.int)
AAA = np.zeros(ar_size,dtype=np.int)
ar_size = (64,64)
DDDD = np.zeros(ar_size,dtype=np.int)
AAAA = np.zeros(ar_size,dtype=np.int)	
	
row_ind = 0
img = get_img(f)
f.close()


t = np.zeros(1,dtype=np.int)


DATA_WIDTH = 262144
d3 = Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))
a2 = Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))
 
x2 = Signal(intbv(164, min = -DATA_WIDTH, max = DATA_WIDTH))
x4 = Signal(intbv(156, min = -DATA_WIDTH, max = DATA_WIDTH))
x3 = Signal(intbv(164, min = -DATA_WIDTH, max = DATA_WIDTH)) 

clk = Signal(bool(0))
 
 
 
#print bin(x2), bin(x3), bin(x4)
#img 256 256 to D 128 128
for i in range(256):
	n = 0
	m = 0
	row_ind = i
	row = get_row(row_ind,img[:],w_img_sz)
	
#spliting into even and odd samples	
	for val in range(row.shape[0]):
		if val %2 == 1:
			#print val, 'odd element',row[val]
			row_odd[0+n] = row[val]
			n = n + 1
			
		if val %2 == 0:
			#print val, 'even element',row[val]
			row_even[0+m] = row[val]
			m  = m + 1	
	#x2,x3,x4 = row_even[2:5]
	#print 'x2 ', x2,'x3 ', x3,'x4 ',x4, 'even'
	#x2,x3,x4 = row_odd[2:5]
	#print 'x2 ', x2,'x3 ', x3,'x4 ',x4, 'odd'
	#print row_even
	#print row_odd
#wr_img(128,D)
for i in range(128): 
	for n in range(123):
		D[n+3,i] = row_odd[n+3] - (0.5*(row_odd[n+2] + row_odd[n+4]) )
		A[n+2,i] = row_even[n+4] + (0.25*(row_even[n+2]) ) + D[n+3,i]
		

#print D.shape
#print A.shape
#print D
#print A
#wr_img(128,A)
#print 0,A[0,:5]
#print 1,A[1,:5]
#print 2,A[2,:5],A[2,123:127]
#print 63,A[63,:5]
#print 125,A[125,:5]
#print 126,A[126,:5]
#print 127,A[127,:5]
#img  to D 256 256

#D output from 1 stage
 

def eq_d(d3,a2,clk,x2,x3,x4):
	t1 = intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH)
	t2 = intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH)	
	t3 = intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH)
	@always(clk.posedge)
	def eq_logic():
		t1 = x2 + x4
		t1 = t1 >> 1
		t2 = x3 - t1
		t1 = x4 >> 2
		t3 = x2 + t1 + t2
		
		d3.next = t2
		a2.next = t3
		 
		 
	return eq_logic
def eq_d_c1(d3,a2,clk,x2,x3,x4):
	t1 = intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH)
	t2 = intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH)	
	t3 = intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH)
	@always(clk.posedge)
	def eq_logic():
		t1 = x2 + x4
		t1 = t1 >> 1
		t2 = x3 - t1
		t1 = x4 >> 2
		t3 = x2 + t1 + t2
		
		d3.next = t2
		a2.next = t3
		 
		 
	return eq_logic	

def eq_d_c2(d3,a2,clk,x2,x3,x4):
	t1 = intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH)
	t2 = intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH)	
	t3 = intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH)
	@always(clk.posedge)
	def eq_logic():
		t1 = x2 + x4
		t1 = t1 >> 1
		t2 = x3 - t1
		t1 = x4 >> 2
		t3 = x2 + t1 + t2
		
		d3.next = t2
		a2.next = t3
		 
		 
	return eq_logic	
d_instance = eq_d(d3,a2,clk,x2,x3,x4)
d_c1_instance = eq_d_c1(d3,a2,clk,x2,x3,x4)
d_c2_instance = eq_d_c2(d3,a2,clk,x2,x3,x4)


toVerilog(eq_d,d3,a2,clk,x2,x3,x4)
toVerilog(eq_d_c1,d3,a2,clk,x2,x3,x4)
toVerilog(eq_d_c2,d3,a2,clk,x2,x3,x4)
