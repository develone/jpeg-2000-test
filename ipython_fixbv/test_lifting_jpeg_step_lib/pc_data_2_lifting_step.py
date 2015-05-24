
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
W0 = 9
from xstools.xsdutio import *  # Import funcs/classes for PC <=> FPGA link.
import random  # Import some random number generator routines.
import time
from PIL import Image
from myhdl import *
x0 = intbv(-2, min = -256, max = 256)

datactn = intbv(0)[8:]
datapush = intbv(3)[2:]
print bin(datapush), bin(datactn,8)

fifo_rd = bool(0)
print
print '''
##################################################################
# This program tests the interface between the host PC and the FPGA 
# on the XuLA board that has been programmed to act as a fifo.
##################################################################
'''
im = Image.open("../../lena_256.png")
pix = im.load()
w, h = im.size
m = list(im.getdata())
m = [m[i:i+im.size[0]] for i in range(0, len(m), im.size[0])]

USB_ID = 0  # USB port index for the XuLA board connected to the host PC.
FIFO_ID = 4  # This is the identifier for the fifo in the FPGA.

# Create a fifo intfc obj with two 8-bit inputs and one 8-bit output.
#c = XsBitArray('0b111111110111111110')
#print c
#print repr(c.to_usb())

fifo = XsDut(USB_ID, FIFO_ID, [ 9, 2, 8, 1, 1], [9, 2])
#help(fifo)
'''
for i in range(255):
    t = random.randrange(-2**(W0-1),2**(W0-1)) 
    #print t
    x0 = intbv(t, min = -256, max = 256)
    datactn = intbv(i)[8:]
    print datactn
    print x0, bin(x0,9) 
    datasent, status = FIFO.Exec(x0, datapush, datactn )  # Use the fifo in FPGA.
    
    print datasent.int, datasent,status
'''
for i in range(1):
    #time.sleep(5)
    for j in range(256):
        print i,j
        x0 = m[j][i]
        print x0, bin(x0,9)
        if j == 0:
            fifo_wr = bool(0)
        else:
            fifo_wr = bool(1)
        datasent,status = fifo.Exec(x0, datapush, datactn, fifo_wr, fifo_rd )  # Use the fifo in FPGA.
        print datasent.int, datasent, status, fifo_wr, fifo_rd





 
