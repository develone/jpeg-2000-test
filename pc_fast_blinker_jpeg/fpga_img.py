from PIL import Image # Part of the standard Python Library
import time
im = Image.open("../lena_64.png")
pix = im.load()
m = list(im.getdata())
#print m.__sizeof__()
m = [m[i:i+im.size[0]] for i in range(0, len(m), im.size[0])]
#print m.__sizeof__()
#print len(m[0]), len(m[1])
width = len(m[0])
#width = 1
#height = 16
height = len(m)
'''
.1
Wed 11 Nov 02:49:53 UTC 2015
Wed 11 Nov 03:05:31 UTC 2015
.075
Wed 11 Nov 03:19:36 UTC 2015
Wed 11 Nov 03:31:55 UTC 2015
0.085
Wed 11 Nov 03:40:18 UTC 2015
Wed 11 Nov 03:53:57 UTC 2015
'''
 

def de_interleave(m,height,width):
	# de-interleave
	temp_bank = [[0]*width for i in range(height)]
	for row in range(width):
		for col in range(width):
            # k1 and k2 scale the vals
            # simultaneously transpose the matrix when deinterleaving
			if row % 2 == 0:

				temp_bank[col][row/2] =  m[row][col]
			else:

				temp_bank[col][row/2 + height/2] =  m[row][col]
    # write temp_bank to s:
	for row in range(width):
		for col in range(height):
			m[row][col] = temp_bank[row][col]


def lower_upper(m,width,height):

	temp_bank = [[0]*width for i in range(height)]
	for col in range(width/2,width,1):

		for row in range(height/2,height,1):

			temp_bank[col-width/2][row-height/2] = m[row][col]

	for row in range(width):
		for col in range(height):
			m[row][col] = temp_bank[col][row]

def seq_to_img(m, pix):
    ''' Copy matrix m to pixel buffer pix.
    Assumes m has the same number of rows and cols as pix. '''
    for row in range(len(m)):
        for col in range(len(m[row])):
            pix[col,row] = m[row][col]
            
def even_odd(m,width,height):
    for col in range(width): # Do the 1D transform on all cols:
        flgs = 7
        for row in range(2, height, 2):
            lft =  m[row-1][col]	  
            sa =  m[row][col]   
            rht =  m[row+1][col]   
            jpeg = lift_step.Exec(lft,sa,rht,flgs)
            time.sleep (110.0 / 1000.0) 
            if (jpeg.int < 0):
                m[row][col] = 512 + jpeg.int
            else:
                m[row][col] = jpeg.int
            #print 'row col flgs left sam right result'        
            #print '%3d %3d  %3d  %3d  %3d  %3d' % (row,col,lft,sa,rht,jpeg.int)
        flgs = 6
        for row in range(1, height-1, 2):
            lft = m[row-1][col]
            sa = m[row][col]
            rht =  m[row+1][col] 
            jpeg = lift_step.Exec(lft,sa,rht,flgs)
            time.sleep (110.0 / 1000.0) 
            if (jpeg.int < 0):
                m[row][col] = 512 + jpeg.int
            else:
                m[row][col] = jpeg.int
            #print 'row col flgs left sam right result'        
            #print '%3d %3d  %3d  %3d  %3d  %3d ' % (row,col,lft,sa,rht,jpeg.int)
             

# /***********************************************************************************
# *   This program is free software; you can redistribute it and/or
# *   modify it under the terms of the GNU General Public License
# *   as published by the Free Software Foundation; either version 2
# *   of the License, or (at your option) any later version.
# *
# *   This program is distributed in the hope that it will be useful,
# *   but WITHOUT ANY WARRANTY; without even the implied warranty of
# *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# *   GNU General Public License for more details.
# *
# *   You should have received a copy of the GNU General Public License
# *   along with this program; if not, write to the Free Software
# *   Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA
# *   02111-1307, USA.
# *
# *   (c)2011 - X Engineering Software Systems Corp. (www.xess.com)
# ***********************************************************************************/

from xstools.xsdutio import *  # Import funcs/classes for PC <=> FPGA link.
from random import *  # Import some random number generator routines.

#print '''
##################################################################
# This program tests the interface between the host PC and the FPGA 
# on the XuLA board that has been programmed to act as a LIFT_STEP.
##################################################################
#'''

USB_ID = 0  # USB port index for the XuLA board connected to the host PC.
LIFT_STEP_ID = 4  # This is the identifier for the subtractor in the FPGA.
# Create a lift_step intfc obj with 3 9-bit & 1 3-bit inputs and one 9-bit output.
lift_step = XsDut(USB_ID, LIFT_STEP_ID, [9, 9, 9, 3], [9])

# Test lift_step by iterating through some random inputs.
even_odd(m,width,height)
de_interleave(m,height,width)
#even_odd(m,width,height)
#de_interleave(m,height,width)
#lower_upper(m,width,height)
seq_to_img(m, pix)

im.save("test1_64_fwt.png")

even_odd(m,width,height)
de_interleave(m,height,width)
lower_upper(m,width,height)
seq_to_img(m, pix)
im.save("test2_64_fwt.png")
