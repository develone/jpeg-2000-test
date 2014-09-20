
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
even_odd = 1 
fwd_inv = 1
jpeg = XsDut(USB_ID, JPEG_ID, [14, 1, 1], [16, 16, 16, 16, 16, 16, 16, 1])

# Test the subtractor by iterating through some random inputs.

#sam = randint(0, 511)  # Get a random, positive byte...
#left = randint(0, 511)  # Get a random, positive byte...
#right = randint(0, 511)  # Get a random, positive byte...
left = 163
sam = 163
right = 163
sam_addr = 125
def loc_jpeg():
    if even_odd:
        if fwd_inv:
            loc_lift = sam - ((left>>1) + (right>>1))
        else:
            loc_lift = sam + ((left>>1) + (right>>1))
    else:
        if fwd_inv:
            loc_lift = sam + ( (left + right + 2)>>2)
        else:
            loc_lift = sam - ( (left + right + 2)>>2)
    return loc_lift
loc_lift = loc_jpeg()
lift, sum, left_r, sam_r, right_r, addr_sam, addr_jpeg, noupdate = jpeg.Exec(sam_addr, even_odd, fwd_inv )  # Use the jpeg in FPGA.
#print '%5d %1d %1d %5d %5d %5d %5d %5d %5d %5d'  % (sam_addr, even_odd, fwd_inv, loc_lift, lift.int, sum.int, left_r.int, sam_r.int, right_r.int, addr_sam.int, addr_jpeg.int)
#print '%5d %1d %1d %5d %5d %5d %5d %5d %5d %5d'  % (sam_addr, even_odd, fwd_inv, loc_lift, lift.int, sum.int, left_r.int, sam_r.int, right_r.int, addr_sam.int, addr_jpeg.int)
print sam_addr, even_odd, fwd_inv, loc_lift, lift.int, sum.int, left_r, sam_r, right_r, addr_sam, addr_jpeg, noupdate

even_odd = 1 
fwd_inv = 0
loc_lift = loc_jpeg()
lift, sum, left_r, sam_r, right_r, addr_sam, addr_jpeg, noupdate = jpeg.Exec(sam_addr, even_odd, fwd_inv )  # Use the jpeg in FPGA.
#print '%5d %1d %1d %5d %5d %5d %5d %5d %5d %5d'  % (sam_addr, even_odd, fwd_inv, loc_lift, lift.int, sum.int, left_r.int, sam_r.int, right_r.int, addr_sam.int, addr_jpeg.int)
#print '%5d %1d %1d %5d %5d %5d %5d %5d %5d %5d'  % (sam_addr, even_odd, fwd_inv, loc_lift, lift.int, sum.int, left_r.int, sam_r.int, right_r.int, addr_sam.int, addr_jpeg.int)
print sam_addr, even_odd, fwd_inv, loc_lift, lift.int, sum.int, left_r, sam_r, right_r, addr_sam, addr_jpeg, noupdate

even_odd = 0 
fwd_inv = 0
loc_lift = loc_jpeg()
lift, sum, left_r, sam_r, right_r, addr_sam, addr_jpeg, noupdate = jpeg.Exec(sam_addr, even_odd, fwd_inv )  # Use the jpeg in FPGA.
#print '%5d %1d %1d %5d %5d %5d %5d %5d %5d %5d'  % (sam_addr, even_odd, fwd_inv, loc_lift, lift.int, sum.int, left_r.int, sam_r.int, right_r.int, addr_sam.int, addr_jpeg.int)
#print '%5d %1d %1d %5d %5d %5d %5d %5d %5d %5d'  % (sam_addr, even_odd, fwd_inv, loc_lift, lift.int, sum.int, left_r.int, sam_r.int, right_r.int, addr_sam.int, addr_jpeg.int)
print sam_addr, even_odd, fwd_inv, loc_lift, lift.int, sum.int, left_r, sam_r, right_r, addr_sam, addr_jpeg, noupdate

even_odd = 0 
fwd_inv = 1
loc_lift = loc_jpeg()
lift, sum, left_r, sam_r, right_r, addr_sam, addr_jpeg, noupdate = jpeg.Exec(sam_addr, even_odd, fwd_inv )  # Use the jpeg in FPGA.
#print '%5d %1d %1d %5d %5d %5d %5d %5d %5d %5d'  % (sam_addr, even_odd, fwd_inv, loc_lift, lift.int, sum.int, left_r.int, sam_r.int, right_r.int, addr_sam.int, addr_jpeg.int)
#print '%5d %1d %1d %5d %5d %5d %5d %5d %5d %5d'  % (sam_addr, even_odd, fwd_inv, loc_lift, lift.int, sum.int, left_r.int, sam_r.int, right_r.int, addr_sam.int, addr_jpeg.int)
print sam_addr, even_odd, fwd_inv, loc_lift, lift.int, sum.int, left_r, sam_r, right_r, addr_sam, addr_jpeg, noupdate