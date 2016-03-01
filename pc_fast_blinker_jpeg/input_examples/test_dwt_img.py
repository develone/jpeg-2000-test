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
def pkt_get(row,v,i):
	if (i == 0):
		pkt = CommandPacket(False, address=0x00, vals=[v])
		wr2file(pkt)
	elif (i == 1):
		pkt = CommandPacket(False, address=0x04, vals=[v])
		wr2file(pkt)
	elif (i == 2):
		pkt = CommandPacket(False, address=0x08, vals=[v])
		wr2file(pkt)
	elif (i == 3):
		pkt = CommandPacket(False, address=0x0C, vals=[v])
		wr2file(pkt)
	elif (i == 4):
		pkt = CommandPacket(False, address=0x10, vals=[v])
		wr2file(pkt)
	elif (i == 5):
		pkt = CommandPacket(False, address=0x14, vals=[v])
		wr2file(pkt)
	elif (i == 6):
		pkt = CommandPacket(False, address=0x18, vals=[v])
		wr2file(pkt)
	elif (i == 7):
		pkt = CommandPacket(False, address=0x1C, vals=[v])
		wr2file(pkt)

	if (i == 8):
		pkt = CommandPacket(False, address=0x20, vals=[v])
		wr2file(pkt)
	elif (i == 9):
		pkt = CommandPacket(False, address=0x24, vals=[v])
		wr2file(pkt)
	elif (i == 10):
		pkt = CommandPacket(False, address=0x28, vals=[v])
		wr2file(pkt)
	elif (i == 11):
		pkt = CommandPacket(False, address=0x2C, vals=[v])
		wr2file(pkt)
	elif (i == 12):
		pkt = CommandPacket(False, address=0x30, vals=[v])
		wr2file(pkt)
	elif (i == 13):
		pkt = CommandPacket(False, address=0x34, vals=[v])
		wr2file(pkt)
	elif (i == 14):
		pkt = CommandPacket(False, address=0x38, vals=[v])
		wr2file(pkt)
	elif (i == 15):
		pkt = CommandPacket(False, address=0x3c, vals=[v])
		wr2file(pkt)
ser = serial.Serial ("/dev/ttyAMA0")    
ser.baudrate = 115200 

index = 0
col = 0
#send 16 samples
for row in range(2,34, 2):
	flag = 7
	v = lsr(row,col,m,flag)
	print row, v, hex(v)
	pkt_get(row,v,index)
	index = index + 1
	print ("%d" % (index))
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
#read z15 & z14 @ address 100
pkt = CommandPacket(False, address=0x64, vals=[v])
wr2file(pkt)

index = 0
col = 0
#send 16 samples
for row in range(34,66, 2):
	flag = 7
	v = lsr(row,col,m,flag)
	print row, v, hex(v)
	pkt_get(row,v,index)
	index = index + 1
	print ("%d" % (index))
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
#read z15 & z14 @ address 100
pkt = CommandPacket(False, address=0x64, vals=[v])
wr2file(pkt)

index = 0
col = 0
#send 16 samples
for row in range(66,98, 2):
	flag = 7
	v = lsr(row,col,m,flag)
	print row, v, hex(v)
	pkt_get(row,v,index)
	index = index + 1
	print ("%d" % (index))
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
#read z15 & z14 @ address 100
pkt = CommandPacket(False, address=0x64, vals=[v])
wr2file(pkt)

index = 0
col = 0
#send 16 samples
for row in range(96,128, 2):
	flag = 7
	v = lsr(row,col,m,flag)
	print row, v, hex(v)
	pkt_get(row,v,index)
	index = index + 1
	print ("%d" % (index))
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
#read z15 & z14 @ address 100
pkt = CommandPacket(False, address=0x64, vals=[v])
wr2file(pkt)


file_out.close()
file_out = open("data_to_fpga.bin","rb")

reply = []

for j in range(108):
	data = file_out.read(12)
	for i in range(12):
		
		#print (data[i])
		ser.write(data[i])
	reply = ser.read(12)
	file_in.write(reply) 
	print "this is the reply", reply
 
file_out.close()
file_in.close()
