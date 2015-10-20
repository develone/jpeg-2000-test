
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

USB_ID = 0  # USB port index for the XuLA board connected to the host PC.
LIFT_STEP_ID = 4  # This is the identifier for the subtractor in the FPGA.

# Create a lift_step intfc obj with 3 8-bit & 1 4-bit inputs and one 8-bit output.
lift_step = XsDut(USB_ID, LIFT_STEP_ID, [8, 8, 8, 3], [9])

# Test lift_step by iterating through some random inputs.
for i in range(0, 256):
    lft = randint(0, 255)  # Get a random, positive byte..
    rht = randint(0, 255)  # Get a random, positive byte..
    sa = randint(0, 255)  # Get a random, positive byte..
    flgs = 7
     
    jpeg = lift_step.Exec(lft, rht, sa, flgs)  # Use the lift_step in FPGA.
    print '%3d %3d %3d %3d %4d \n' % (lft, rht, sa, flgs, jpeg.int)
 
