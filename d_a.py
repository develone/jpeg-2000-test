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
import scipy.signal as sg
import numpy as np
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
for i in range(4):
	#print f.readline()
	f.readline()

ar_size = (256,256)
w_img_sz = 256
#now img is 2-dimensional of type int
#now row is 1-dimensional of type int
#now col is 1-dimensional of type int
#now rowl is 1-dimensional of type int
img = np.zeros(ar_size,dtype=np.int) 
col = np.zeros(w_img_sz,dtype=np.int)
row = np.zeros(w_img_sz,dtype=np.int)
D = np.zeros(w_img_sz,dtype=np.int)
A = np.zeros(w_img_sz,dtype=np.int)	
row_ind = 0
img = get_img(f)
row = get_row(row_ind,img[:],w_img_sz)
print row[0:15]

DATA_WIDTH = 262144
d3 = Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))
a2 = Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))
 
x2 = Signal(intbv(164, min = -DATA_WIDTH, max = DATA_WIDTH))
x4 = Signal(intbv(156, min = -DATA_WIDTH, max = DATA_WIDTH))
x3 = Signal(intbv(164, min = -DATA_WIDTH, max = DATA_WIDTH)) 

clk = Signal(bool(0))
 
 
 
print bin(x2), bin(x3), bin(x4)
for n in range(30):
	
    D[n+3] = row[n+3] - ((row[n+2] + row[n+4]) >> 1)
    A[n+2] = row[n+4] + ((row[n+2]) >> 2) + D[n+3]
    print n,hex(row[n+3]), hex(row[n+2]), hex(row[n+4]), hex(D[n+3])
    print n,row[n+3], row[n+2], row[n+4], D[n+3]
    print n,hex(row[n+2]), hex(row[n+4]), hex(A[n+2])
    print n,row[n+2], row[n+4], A[n+2]
            
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
