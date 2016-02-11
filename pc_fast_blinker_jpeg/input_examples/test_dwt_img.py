from dwt_image import (seq_to_img, de_interleave, lower_upper, rd_img, lsr)
from myhdl import *
import serial
from rhea.utils import CommandPacket
from rhea.utils.command_packet import PACKET_LENGTH
'''read the data from the image'''

imgfn = "../../lena_256.png"
im, m, pix = rd_img(imgfn)
#print type(im), type(m), type(pix)
w, h = im.size
 
#print w, h

'''set the baud rate to 115200 on RPi2B'''

ser = serial.Serial ("/dev/ttyAMA0")    
ser.baudrate = 115200 


'''passing the row, col, and flag to lsr lsr(row,col,m,flag)
provides a 32 bit value '''
row = 1
col = 0
flag = 6
print m[row-1][col], m[row][col], m[row+1][col]
x3 = lsr(row,col,m,flag) 
print hex(x3), x3
print bin(x3,32)

pkt = CommandPacket(False, address=0x04, vals=[x3])
print pkt.rawbytes[0], pkt.rawbytes[6], pkt.rawbytes[7]
for bb in pkt.rawbytes:
    print bin(bb,8)
    ser.write(bb)
reply = ser.read(12) 
print "this is the reply", reply
