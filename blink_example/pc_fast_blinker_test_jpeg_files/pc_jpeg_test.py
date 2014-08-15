
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

print '''
##################################################################
# This program tests the interface between the host PC and the FPGA 
# on the XuLA board that has been programmed to act as a jpeg_lifting .
##################################################################
'''

USB_ID = 0  # USB port index for the XuLA board connected to the host PC.
JPEG_ID = 4  # This is the identifier for the jpeg in the FPGA.

# Create a jpeg intfc obj with three 17-bit inputs and one 17-bit output.
jpeg = XsDut(USB_ID, JPEG_ID, [17, 17, 17], [17])
flags = 3
# Test the subtractor by iterating through some random inputs.
for i in range(0, 100):
    sam = randint(0, 511)  # Get a random, positive byte...
    left = randint(0, 511)  # Get a random, positive byte...
    right = randint(0, 511)  # Get a random, positive byte...
    
    lift = jpeg.Exec(right, left, sam)  # Use the jpeg in FPGA.
    loc_lift = sam - ((left>>1) + (right>>1))
    print '%5d %5d %5d %5d %5d ' % (sam, left, right, loc_lift, lift.int)
    if loc_lift != lift.int:
	print 'ERROR %5d  %5d' % (loc_lift, lift.int)
    else:
	print 'results are the same between the local and FPGA'
