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
#wavelet97lift needs to be 1 level below
#PYTHONPATH /home/vidal/lib/python:./python_dwt:
import  wavelet97lift

 
def convert_hdl():
	d_instance = eq_d(d3,a2,clk,x2,x3,x4)
	d_c1_instance = eq_d_c1(d3,a2,clk,x2,x3,x4)
	d_c2_instance = eq_d_c2(d3,a2,clk,x2,x3,x4)

	toVerilog(eq_d,d3,a2,clk,x2,x3,x4)
	toVerilog(eq_d_c1,d3,a2,clk,x2,x3,x4)
	toVerilog(eq_d_c2,d3,a2,clk,x2,x3,x4)
		
LPSynthesisFilter = np.array([ 0.5, 1, 0.5 ])
HPSynthesisFilter = np.array([ -0.125, -0.25, 0.75, -0.25, -0.125 ])
 
 

 

DATA_WIDTH = 262144
d3 = Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))
a2 = Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))
 
x2 = Signal(intbv(164, min = -DATA_WIDTH, max = DATA_WIDTH))
x4 = Signal(intbv(156, min = -DATA_WIDTH, max = DATA_WIDTH))
x3 = Signal(intbv(164, min = -DATA_WIDTH, max = DATA_WIDTH)) 

clk = Signal(bool(0))
 
 
 
  

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
def fwt97_2d_int(m, nlevels=1):
    ''' Perform the CDF 9/7 transform on a 2D matrix signal m.
    nlevel is the desired number of times to recursively transform the 
    signal. When flag is 0 processing done on rows '''
    
    w = len(m[0])
    h = len(m)
    flag = 0
    for i in range(nlevels):
        m = fwt97_int(m, w, h,flag)
         
        #flag = 1
        #m = fwt97_int(m, w, h,flag) 
        
        #w /= 2
        #h /= 2
    
    return m

def fwt97_int(s, width, height,flag):
	if flag == 0:   
		for col in range(width): # Do the 1D transform on all cols:
			''' Core 1D lifting process in this loop. '''
			''' Lifting is done on the rows. '''
			# Predict 1. y1
			# odd pass 1
			# i starts at 1 and increments by 2 until (height -1)
			# for a height of 128 i goes 1, 3, 5...125
			# for a height of 256 i goes 1, 3, 5...253
			# for a height of 512 i goes 1, 3, 5...509
			for row in range(1, height-3, 2):
				#details coefficients  
				s[row+2][col] += s[row+2][col] + (-0.5 * ((s[row+1][col] + s[row+4][col]))) 
				 
				#s[height-1][col] += 2 * a1 * s[height-2][col] # Symmetric extension
				# this is working on sample at the end
				#  for height 256 works on sample 255 using 2*a1* sample 254
		
			# Update 1. y0
			# even pass1
			# i starts at 1 and increments by 2 until (height -1)
			# for a height of 128 i goes 2, 4, 6...126
			# for a height of 256 i goes 2, 4, 6...254
			# for a height of 512 i goes 2, 4, 6...510

			for row in range(2, height-2, 2):
				#approximations coefficients. 
				s[row+2][col] += s[row+2][col] + .25* (s[row+1][col] + s[row+3][col])
				#s[0][col] +=  2 * a2 * s[1][col] # Symmetric extension
				# this is working on sample at the beginning
				# for for height 256 works on sample 0 using 2*a2* sample 1
	else:
		for row in range(height): # Do the 1D transform on all cols:
			''' Core 1D lifting process in this loop. '''
			''' Lifting is done on the cols. '''
			# Predict 1. y1
			# odd pass 1
			# i starts at 1 and increments by 2 until (height -1)
			# for a height of 128 i goes 1, 3, 5...125
			# for a height of 256 i goes 1, 3, 5...253
			# for a height of 512 i goes 1, 3, 5...509
			for col in range(1, height-3, 2):
				#details coefficients 
				s[row][col+2] += s[row][col+2] + (-0.5 * ((s[row][col+1] + s[row][col+4])))  
				#s[height-1][col] += 2 * a1 * s[height-2][col] # Symmetric extension
				# this is working on sample at the end
				#  for height 256 works on sample 255 using 2*a1* sample 254
		
			# Update 1. y0
			# even pass1
			# i starts at 1 and increments by 2 until (height -1)
			# for a height of 128 i goes 2, 4, 6...126
			# for a height of 256 i goes 2, 4, 6...254
			# for a height of 512 i goes 2, 4, 6...510

			for col in range(2, height-2, 2):
				#approximations coefficients.
				s[row][col+2] += s[row][col+2] + .25* (s[row][col+1] + s[row][col+3])
				#s[0][col] +=  2 * a2 * s[1][col] # Symmetric extension
				# this is working on sample at the beginning
				# for for height 256 works on sample 0 using 2*a2* sample 1
	temp_bank = [[0]*width for i in range(height)]
	for row in range(height):
		for col in range(width):
             
			if row % 2 == 1: # odd
                 
				temp_bank[col][row/2] = s[row][col]
			else:            # even
					 
				temp_bank[col][row/2 + height/2] = s[row][col]
	# write temp_bank to s:
	for row in range(width):
		for col in range(height):
			s[col][row] = temp_bank[row][col]
	return s
def iwt97_2d(m, nlevels=1):
    ''' Inverse CDF 9/7 transform on a 2D matrix signal m.
        nlevels must be the same as the nlevels used to perform the fwt.
    '''
    
    w = len(m[0])
    h = len(m)

    # Find starting size of m:
    for i in range(nlevels-1):
        h /= 2
        w /= 2
        
    for i in range(nlevels):
        m = iwt97(m, w, h) # rows
        m = iwt97(m, w, h) # cols
        h *= 2
        w *= 2
    
    return m
def iwt97(s, width, height):
    ''' Inverse CDF 9/7. '''
    
    # 9/7 inverse coefficients:
    a1 = 1.586134342
    a2 = 0.05298011854
    a3 = -0.8829110762
    a4 = -0.4435068522
    
    # Inverse scale coeffs:
    k1 = 1.230174104914
    k2 = 1.6257861322319229
    
    # Interleave:
    temp_bank = [[0]*width for i in range(height)]
    for col in range(width/2):
        for row in range(height):
            # k1 and k2 scale the vals
            # simultaneously transpose the matrix when interleaving
            temp_bank[col * 2][row] = k1 * s[row][col]
            temp_bank[col * 2 + 1][row] = k2 * s[row][col + width/2]
                
    # write temp_bank to s:
    for row in range(width):
        for col in range(height):
            s[row][col] = temp_bank[row][col]

                
    for col in range(width): # Do the 1D transform on all cols:
        ''' Perform the inverse 1D transform. '''
        
        # Inverse update 2.
        for row in range(2, height, 2):
            s[row][col] += a4 * (s[row-1][col] + s[row+1][col])
        s[0][col] += 2 * a4 * s[1][col]
        
        # Inverse predict 2.
        for row in range(1, height-1, 2):
            s[row][col] += a3 * (s[row-1][col] + s[row+1][col])
        s[height-1][col] += 2 * a3 * s[height-2][col]

        # Inverse update 1.
        for row in range(2, height, 2):
            s[row][col] += a2 * (s[row-1][col] + s[row+1][col])
        s[0][col] +=  2 * a2 * s[1][col] # Symmetric extension
        
        # Inverse predict 1.
        for row in range(1, height-1, 2):
            s[row][col] += a1 * (s[row-1][col] + s[row+1][col])   
        s[height-1][col] += 2 * a1 * s[height-2][col] # Symmetric extension
                
    return s
def seq_to_img(m, pix):
    ''' Copy matrix m to pixel buffer pix.
    Assumes m has the same number of rows and cols as pix. '''
    for row in range(len(m)):
        for col in range(len(m[row])):
            pix[col,row] = m[row][col]
                
#im is an instance provided by PIL
#im is 2-d im[0] & im[1] are the sizes
#Using PIL to read image
#im = wavelet97lift.Image.open("python_dwt/test1_512.png")
im = wavelet97lift.Image.open("lena_256.png")
#print im.mode, im.format
# Create an image buffer object for fast access.
pix = im.load()


#m is a list 
# Convert the 2d image to a 1d sequence:
m = list(im.getdata())

#m is a list 
# Convert the 2d image to a 1d sequence:
m = [m[i:i+im.size[0]] for i in range(0, len(m), im.size[0])]
 

# Cast every item in the list to a float:
#for row in range(0, len(m)):
#	for col in range(0, len(m[0])):
#		m[row][col] = float(m[row][col])
		
# Perform a forward CDF 9/7 transform on the image:
m = fwt97_2d_int(m, 1)	
    	 
#pix[col,row] = m[row][col]	
seq_to_img(m, pix) # Convert the list of lists matrix to an image.		
im.save("fwt.png") # Save the inverse transformation.
  		
#m = iwt97_2d(m, 1)		
#seq_to_img(m, pix) # Convert the inverse list of lists matrix to an image.
#im.save("lena_256_iwt.png") # Save the inverse transformation.
    		
		
		
		
		
		
		
		
		
		
