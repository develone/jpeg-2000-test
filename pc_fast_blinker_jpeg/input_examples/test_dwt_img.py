from dwt_image import (seq_to_img, de_interleave, lower_upper, rd_img, lsr)
from myhdl import *
import serial
from rhea.utils import CommandPacket
from rhea.utils.command_packet import PACKET_LENGTH

import binascii
'''read the data from the image'''

file_out = open("data_to_fpga.bin","wb")
file_in = open("data_from_fpga.bin","wb")

imgfn = "../../lena_256.png"
im, m, pix = rd_img(imgfn)
#print type(im), type(m), type(pix)
w, h = im.size
 
#print w, h

'''set the baud rate to 115200 on RPi2B'''
def wr2file(pkt):
	ml = []
	for bb in pkt.rawbytes:
		#file_out.write('bb')
		#print bb
		ml.append(bb)
		#print ml
        ba = bytearray(ml)
        file_out.write(ba)
def pkt_get(row,v):
	if (row == 2) or (row ==1):
		pkt = CommandPacket(False, address=0x00, vals=[v])
		wr2file(pkt)
	elif (row == 4) or (row ==3):
		pkt = CommandPacket(False, address=0x04, vals=[v])
		wr2file(pkt)
	elif (row == 6) or (row ==5):
		pkt = CommandPacket(False, address=0x08, vals=[v])
		wr2file(pkt)
	elif (row == 8) or (row ==7):
		pkt = CommandPacket(False, address=0x0C, vals=[v])
		wr2file(pkt)
	elif (row == 10) or (row ==9):
		pkt = CommandPacket(False, address=0x10, vals=[v])
		wr2file(pkt)
	elif (row == 12) or (row ==11):
		pkt = CommandPacket(False, address=0x14, vals=[v])
		wr2file(pkt)
	elif (row == 14) or (row ==13):
		pkt = CommandPacket(False, address=0x18, vals=[v])
		wr2file(pkt)
	elif (row == 16) or (row ==15):
		pkt = CommandPacket(False, address=0x1C, vals=[v])
		wr2file(pkt)

	if (row == 18) or (row ==17):
		pkt = CommandPacket(False, address=0x20, vals=[v])
		wr2file(pkt)
	elif (row == 20) or (row ==19):
		pkt = CommandPacket(False, address=0x24, vals=[v])
		wr2file(pkt)
	elif (row == 22) or (row ==21):
		pkt = CommandPacket(False, address=0x28, vals=[v])
		wr2file(pkt)
	elif (row == 24) or (row ==23):
		pkt = CommandPacket(False, address=0x2C, vals=[v])
		wr2file(pkt)
	elif (row == 26) or (row ==25):
		pkt = CommandPacket(False, address=0x30, vals=[v])
		wr2file(pkt)
	elif (row == 28) or (row ==27):
		pkt = CommandPacket(False, address=0x34, vals=[v])
		wr2file(pkt)
	elif (row == 30) or (row ==29):
		pkt = CommandPacket(False, address=0x38, vals=[v])
		wr2file(pkt)
	elif (row == 32) or (row ==31):
		pkt = CommandPacket(False, address=0x3c, vals=[v])
		wr2file(pkt)
ser = serial.Serial ("/dev/ttyAMA0")    
ser.baudrate = 115200 

col = 0
#send 16 samples
for row in range(2,34, 2):
	flag = 7
	v = lsr(row,col,m,flag)
	print row, v, hex(v)
	pkt_get(row,v)
v = 0
#upd on	
pkt = CommandPacket(False, address=0x40, vals=[v])
wr2file(pkt)
#upd off
pkt = CommandPacket(False, address=0x44, vals=[v])
wr2file(pkt)
#read z1 & z0 @ address 72
pkt = CommandPacket(False, address=0x48, vals=[v])
wr2file(pkt)
#read z3 & z2 @ address 76
pkt = CommandPacket(False, address=0x4C, vals=[v])
wr2file(pkt)
#read z5 & z4 @ address 80
pkt = CommandPacket(False, address=0x50, vals=[v])
wr2file(pkt)
#read z7 & z6 @ address 84
pkt = CommandPacket(False, address=0x54, vals=[v])
wr2file(pkt)
#read z9 & z8 @ address 88
pkt = CommandPacket(False, address=0x58, vals=[v])
wr2file(pkt)
#read z11 & z10 @ address 92
pkt = CommandPacket(False, address=0x5C, vals=[v])
wr2file(pkt)
#read z13 & z12 @ address 96
pkt = CommandPacket(False, address=0x60, vals=[v])
wr2file(pkt)
#read z15 & z14 @ address 100
pkt = CommandPacket(False, address=0x64, vals=[v])
wr2file(pkt)

file_out.close()
file_out = open("data_to_fpga.bin","rb")

reply = []

for j in range(26):
	data = file_out.read(12)
	for i in range(12):
		
		#print (data[i])
		ser.write(data[i])
	reply = ser.read(12)
	file_in.write(reply) 
	print "this is the reply", reply
 
file_out.close()
file_in.close()
'''even samples uploaded
getting ready to read the results
and send the odd samples
'''
file_out = open("data_to_fpga1.bin","wb")
for row in range(1,17, 2):
	flag = 6
	v = lsr(row,col,m,flag)
	print row, v, hex(v)
	pkt_get(row,v)
v = 0	
pkt = CommandPacket(False, address=0x20, vals=[v])
wr2file(pkt)
pkt = CommandPacket(False, address=0x24, vals=[v])
wr2file(pkt)
v = 0
pkt = CommandPacket(False, address=0x40, vals=[v])
wr2file(pkt)
file_out.close()		
file_out = open("data_to_fpga1.bin","rb")	
for j in range(11):
	data = file_out.read(12)
	for i in range(12):
		
		#print (data[i])
		ser.write(data[i])
	reply = ser.read(12)
	file_in.write(reply) 
	print "this is the reply", reply

		

