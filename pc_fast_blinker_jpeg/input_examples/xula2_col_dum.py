from __future__ import division
from __future__ import print_function


from dwt_image_pix import (seq_to_img, de_interleave, lower_upper, rd_img, lsr)
from myhdl import *
import serial
from rhea.utils import CommandPacket
from rhea.utils.command_packet import PACKET_LENGTH


import binascii
'''read the data from the image'''

file_out = open("col0_to_fpga.bin","wb")
file_in = open("col0_from_fpga.bin","wb")

imgfn = "../../lena_256.png"
im, m, pix = rd_img(imgfn)
#print type(im), type(m), type(pix)
w, h = im.size
 
#print w, h

'''set the baud rate to 115200 on RPi2B'''
def wr2file(pkt, ind):
	ml = []
        #print ("%s " % (pkt))
        #print ("%s " % (binascii.hexlify(pkt)))
	for bb in pkt.rawbytes:
		#file_out.write('bb')
		#print ind
		if (ind >= 8):
			ml.append(bb)
			#print len(ml)
			ba = bytearray(ml)
			#file_out.write(ba)
                print ("%d" % (ind))
		ind = ind + 1
        
	ba = bytearray(ml)
        print ("%s  %d" % (binascii.hexlify(ba), len(ml)))
        file_out.write(ba)
def pkt_get(row,v,i):
        #print v
        pkt = CommandPacket(False, address=0x00, vals=[v])
        i = 0
        wr2file(pkt,i)
        '''
	if (i == 0):
		pkt = CommandPacket(False, address=0x00, vals=[v])
		ind = 0
		wr2file(pkt,ind)
	elif (i == 1):
		pkt = CommandPacket(False, address=0x04, vals=[v])
		ind = 0
		wr2file(pkt,ind)
	elif (i == 2):
		pkt = CommandPacket(False, address=0x08, vals=[v])
		ind = 0
		wr2file(pkt,ind)
	elif (i == 3):
		pkt = CommandPacket(False, address=0x0C, vals=[v])
		ind = 0
		wr2file(pkt,ind)
	elif (i == 4):
		pkt = CommandPacket(False, address=0x10, vals=[v])
		ind = 0
		wr2file(pkt,ind)
	elif (i == 5):
		pkt = CommandPacket(False, address=0x14, vals=[v])
		ind = 0
		wr2file(pkt,ind)
	elif (i == 6):
		pkt = CommandPacket(False, address=0x18, vals=[v])
		ind = 0
		wr2file(pkt,ind)
	elif (i == 7):
		pkt = CommandPacket(False, address=0x1C, vals=[v])
		ind = 0
		wr2file(pkt,ind)

	if (i == 8):
		pkt = CommandPacket(False, address=0x20, vals=[v])
		ind = 0
		wr2file(pkt,ind)
	elif (i == 9):
		pkt = CommandPacket(False, address=0x24, vals=[v])
		ind = 0
		wr2file(pkt,ind)
	elif (i == 10):
		pkt = CommandPacket(False, address=0x28, vals=[v])
		ind = 0
		wr2file(pkt,ind)
	elif (i == 11):
		pkt = CommandPacket(False, address=0x2C, vals=[v])
		ind = 0
		wr2file(pkt,ind)
	elif (i == 12):
		pkt = CommandPacket(False, address=0x30, vals=[v])
		ind = 0
		wr2file(pkt,ind)
	elif (i == 13):
		pkt = CommandPacket(False, address=0x34, vals=[v])
		ind = 0
		wr2file(pkt,ind)
	elif (i == 14):
		pkt = CommandPacket(False, address=0x38, vals=[v])
		ind = 0
		wr2file(pkt,ind)
	elif (i == 15):
		pkt = CommandPacket(False, address=0x3c, vals=[v])
		ind = 0
		wr2file(pkt,ind)
        '''
#ser = serial.Serial ("/dev/ttyAMA0")    
#ser.baudrate = 115200 

index = 0
col = 0
#send 16 samples0
for row in range(1,255, 1):
	flag = 7
	v = lsr(row,col,m,flag)
	print ("%d %d %s" % (row, v, hex(v)))
	pkt_get(row,v,index)
	index = index + 1
	#print ("%d" % (index))
''' 
index = 0
col = 0
#send 16 samples1
for row in range(34,66, 2):
	flag = 7
	v = lsr(row,col,m,flag)
	print row, v, hex(v)
	pkt_get(row,v,index)
	index = index + 1
	#print ("%d" % (index))
index = 0
col = 0
#send 16 samples2
for row in range(66,98, 2):
	flag = 7
	v = lsr(row,col,m,flag)
	print row, v, hex(v)
	pkt_get(row,v,index)
	index = index + 1
	#print ("%d" % (index))	
index = 0
col = 0
#send 16 samples3
for row in range(98,130, 2):
	flag = 7
	v = lsr(row,col,m,flag)
	print row, v, hex(v)
	pkt_get(row,v,index)
	index = index + 1
	#print ("%d" % (index))	
index = 0
col = 0
#send 16 samples4
for row in range(130,162, 2):
	flag = 7
	v = lsr(row,col,m,flag)
	print row, v, hex(v)
	pkt_get(row,v,index)
	index = index + 1
	#print ("%d" % (index))	
index = 0
col = 0
#send 16 samples5
for row in range(162,194, 2):
	flag = 7
	v = lsr(row,col,m,flag)
	print row, v, hex(v)
	pkt_get(row,v,index)
	index = index + 1
	#print ("%d" % (index))	
index = 0
col = 0
#send 16 samples6
for row in range(194,226, 2):
	flag = 7
	v = lsr(row,col,m,flag)
	print row, v, hex(v)
	pkt_get(row,v,index)
	index = index + 1
	#print ("%d" % (index))		
index = 0
col = 0
#send 16 samples7
for row in range(226,254, 2):
	flag = 7
	v = lsr(row,col,m,flag)
	print row, v, hex(v)
	pkt_get(row,v,index)
	index = index + 1
	#print ("%d" % (index))	
'''									
file_out.close()
file_out = open("col0_to_fpga.bin","rb")

 
