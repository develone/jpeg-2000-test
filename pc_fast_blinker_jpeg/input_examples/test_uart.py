from rhea.utils import CommandPacket
from rhea.utils.command_packet import PACKET_LENGTH
import binascii
import serial
import time
#print "Start : %s" % time.ctime()

ser = serial.Serial ("/dev/ttyAMA0")    
ser.baudrate = 115200
reply = []
file = open("wr.bin","wb")
file.write("\xde\x02\x00\x00\x00\x80\x04\xca\x00\x00\x00\xff")
file.close
file = open("wr.bin", "rb")
data = file.read(12)
x = binascii.b2a_hex(data)
print x
for i in range(12):
	ser.write(data[i])
reply = ser.read(12)
x = binascii.b2a_hex(reply)
print x
time.sleep( 5 )
file = open("wr.bin","wb")
file.write("\xde\x02\x00\x00\x00\x80\x04\xca\x00\x00\x00\x00")
file.close
file = open("wr.bin", "rb")
data = file.read(12)
x = binascii.b2a_hex(data)
print x
for i in range(12):
	ser.write(data[i])
reply = ser.read(12)
x = binascii.b2a_hex(reply)
print x
start_time = time.ctime()

'''sample 1 0xa4 0xa4 0xa4 0 '0x3a', '0x91', '0x48', '0xa4' '''
'''***************************************************************'''
print 'sample 1'
file = open("wr.bin","wb")
file.write("\xde\x02\x00\x00\x00\x00\x04\xca\x3a\x91\x48\xa4")
file.close
file = open("wr.bin","rb")
data = file.read(12)
x = binascii.b2a_hex(data)
print x
for i in range(12):
	ser.write(data[i])
reply = ser.read(12)
x = binascii.b2a_hex(reply)
print x
 
 
'''***************************************************************'''
'''sample 2 0xa4 0x9c 0x9c -4 '0x3a', '0x91', '0x38', '0x9c' '''
'''sample 2'''
'''***************************************************************'''
print 'sample 2'
file = open("wr.bin","wb")
file.write("\xde\x02\x00\x00\x00\x04\x04\xca\x3a\x91\x38\x9c")
file.close
file = open("wr.bin","rb")
data = file.read(12)
x = binascii.b2a_hex(data)
print x
for i in range(12):
	ser.write(data[i])
reply = ser.read(12)
x = binascii.b2a_hex(reply)
print x

file = open("wr.bin","wb")	
file.write("\xde\x02\x00\x00\x00\x40\x04\xca\x00\x00\x00\x00")
file.close
file = open("wr.bin","rb")
data = file.read(12)
x = binascii.b2a_hex(data)
print x
for i in range(12):
	ser.write(data[i])
reply = ser.read(12)
x = binascii.b2a_hex(reply)
print x

file = open("wr.bin","wb")
file.write("\xde\x02\x00\x00\x00\x44\x04\xca\x00\x00\x00\x00")
file.close
file = open("wr.bin","rb")
data = file.read(12)
x = binascii.b2a_hex(data)
print x
for i in range(12):
	ser.write(data[i])
reply = ser.read(12)
x = binascii.b2a_hex(reply)
print x

file = open("wr.bin","wb")
file.write("\xde\x02\x00\x00\x00\x48\x04\xca\x00\x00\x00\x00")
file.close
file = open("wr.bin","rb")
data = file.read(12)
x = binascii.b2a_hex(data)
print x

for i in range(12):
	ser.write(data[i])
reply = ser.read(12)
x = binascii.b2a_hex(reply)
print x

'''sample 15 0xa4 0xa4 0xa4 0 '0x3a', '0x91', '0x48', '0xa4' '''
'''***************************************************************'''
print 'sample 15'
file = open("wr.bin","wb")
file.write("\xde\x02\x00\x00\x00\x38\x04\xca\x3a\x91\x48\xa4")
file.close
file = open("wr.bin","rb")
data = file.read(12)
x = binascii.b2a_hex(data)
print x
for i in range(12):
	ser.write(data[i])
reply = ser.read(12)
x = binascii.b2a_hex(reply)
print x 
'''***************************************************************'''

'''sample 16'''
'''***************************************************************'''
print 'sample 16'
file = open("wr.bin","wb")
file.write("\xde\x02\x00\x00\x00\x3c\x04\xca\x3a\x91\x58\xa4")
file.close
file = open("wr.bin","rb")
data = file.read(12)
x = binascii.b2a_hex(data)
print x
for i in range(12):
	ser.write(data[i])
reply = ser.read(12)
x = binascii.b2a_hex(reply)
print x

file = open("wr.bin","wb")	
file.write("\xde\x02\x00\x00\x00\x40\x04\xca\x00\x00\x00\x00")
file.close
file = open("wr.bin","rb")
data = file.read(12)
x = binascii.b2a_hex(data)
print x
for i in range(12):
	ser.write(data[i])
reply = ser.read(12)
x = binascii.b2a_hex(reply)
print x

file = open("wr.bin","wb")
file.write("\xde\x02\x00\x00\x00\x44\x04\xca\x00\x00\x00\x00")
file.close
file = open("wr.bin","rb")
data = file.read(12)
x = binascii.b2a_hex(data)
print x
for i in range(12):
	ser.write(data[i])
reply = ser.read(12)
x = binascii.b2a_hex(reply)
print x

file = open("wr.bin","wb")
file.write("\xde\x02\x00\x00\x00\x64\x04\xca\x00\x00\x00\x00")
file.close
file = open("wr.bin","rb")
data = file.read(12)
x = binascii.b2a_hex(data)
print x
for i in range(12):
	ser.write(data[i])
reply = ser.read(12)
x = binascii.b2a_hex(reply)
print x

'''***************************************************************'''



end_time = time.ctime()

print start_time, end_time
