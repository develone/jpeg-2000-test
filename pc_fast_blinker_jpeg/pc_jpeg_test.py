
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
# on the XuLA board that has been programmed to act as a LIFT_STEP.
##################################################################
'''
def jpeg_test(lft,sa,rht,flgs):
	lift = 0
	if (flgs == 7):
		lift = (int(sa) - ( (int(lft >> 1)) + (int(rht >> 1)) ))
	elif (flgs == 6):
		lift = (int(sa) + ((int(lft) + int(rht) + 2) >> 2))
	elif (flgs == 5):
		lift = (int(sa) + ( (int(lft >> 1)) + (int(rht >> 1)) ))
	elif (flgs == 4):
		lift = (int(sa) - ((int(lft) + int(rht) + 2) >> 2))
	print '%4d \n' % (lift) 
USB_ID = 0  # USB port index for the XuLA board connected to the host PC.
LIFT_STEP_ID = 4  # This is the identifier for the subtractor in the FPGA.
# Create a lift_step intfc obj with 3 8-bit & 1 3-bit inputs and one 8-bit output.
lift_step = XsDut(USB_ID, LIFT_STEP_ID, [8, 8, 8, 3], [8])

# Test lift_step by iterating through some random inputs.
'''
for i in range(0, 256):
    lft = randint(0, 255)  # Get a random, positive byte..
    rht = randint(0, 255)  # Get a random, positive byte..
    sa = randint(0, 255)  # Get a random, positive byte..
    if (i <= 64):
        flgs = 7
    elif ( i <= 128):
	flgs = 6
    elif (i <= 192):
	flgs = 5
    elif (i <= 256):
	flgs = 4
    jpeg_test(lft,sa, rht,flgs)
    
    jpeg = lift_step.Exec(lft, sa, rht, flgs)  # Use the lift_step in FPGA.
    print '%3d %3d %3d %3d %4d %s \n' % (lft, sa, rht, flgs, jpeg.int, jpeg)
''' 
lft = 68

sa = 218

rht = 163
flgs = 7
jpeg = lift_step.Exec(lft, sa, rht, flgs)  # Use the lift_step in FPGA.
print '%3d %3d %3d %3d %s \n' % (lft, sa, rht, flgs, jpeg)
lft = 164

sa = 250

rht = 160
flgs = 5
jpeg = lift_step.Exec(lft, sa, rht, flgs)  # Use the lift_step in FPGA.
print '%3d %3d %3d %3d %s \n' % (lft, sa, rht, flgs, jpeg)
lft = 164

sa = 250

rht = 160
flgs = 6
jpeg = lift_step.Exec(lft, sa, rht, flgs)  # Use the lift_step in FPGA.
print '%3d %3d %3d %3d %s \n' % (lft, sa, rht, flgs, jpeg)
