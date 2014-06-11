from myhdl import *

import pylab
import scipy
import scipy.misc as sg_m
import scipy.signal as sg
import numpy as np

import  wavelet97lift
def wr_img(sz,img_ar):
 
	f = open('test.pgm','w')
	f.write(hs0)
	f.write(hs1)
	f.write(hs2)
	f.write(hs3) 
	for i in range(sz):
		for j in range(sz):
			ele = str(img_ar[i,j])
			f.write(ele)
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
ar_size = (256,256)	
img = np.zeros(ar_size,dtype=np.int) 
s = np.zeros(ar_size,dtype=np.float) 	
f = open('../lena_256.pgm','r')
hs0 = f.readline()
hs1 = f.readline()
hs2 = f.readline()
hs3 = f.readline()
print hs0
print hs1
print hs2

print hs3
img = get_img(f)
f.close()
for i in range(img.shape[0]):
	for j in range(img.shape[1]):
		s[i,j] = float(img[i,j])	
print s
width, height= s.shape
#fwt97(s, width, height)
#s = wavelet97lift.fwt97(s, width, height)
s = wavelet97lift.fwt97_2d(s)
print s
print s.shape
wr_img(256,s)
#wavelet97lift.seq_to_img(s, pix)
#im.save("test1_256.png")
