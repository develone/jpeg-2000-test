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
start_time = time.ctime()
'''sample 1'''
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

file = open("wr.bin","wb")	
file.write("\xde\x02\x00\x00\x00\x40\x04\xca\x00\x00\x00\x00")
file.close
file = open("wr.bin","rb")
data = file.read(12)
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

 
'''***************************************************************'''

'''sample 2'''
'''***************************************************************'''
print 'sample 2'
file = open("wr.bin","wb")
file.write("\xde\x02\x00\x00\x00\x04\x04\xca\x3a\x91\x48\xa4")
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
file.write("\xde\x02\x00\x00\x00\x4C\x04\xca\x00\x00\x00\x00")
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
file.write("\xde\x02\x00\x00\x00\x80\x04\xca\x00\x00\x00\x00")
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
end_time = time.ctime()

print start_time, end_time
