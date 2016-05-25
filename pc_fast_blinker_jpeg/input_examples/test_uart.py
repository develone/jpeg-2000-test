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

'''sample 0'''
'''***************************************************************'''
print 'sample 0'
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
 

'''sample 1'''
'''***************************************************************'''
print 'sample 1'
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

'''sample 2'''
'''***************************************************************'''
print 'sample 2'
file = open("wr.bin","wb")
file.write("\xde\x02\x00\x00\x00\x08\x04\xca\x3a\x71\x38\xa4")
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

'''sample 3'''
'''***************************************************************'''
print 'sample 3'
file = open("wr.bin","wb")
file.write("\xde\x02\x00\x00\x00\x0C\x04\xca\x3a\x91\x38\x9c")
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

'''sample 4'''
'''***************************************************************'''
print 'sample 4'
file = open("wr.bin","wb")
file.write("\xde\x02\x00\x00\x00\x10\x04\xca\x3a\x71\x38\x9c")
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

'''sample 5'''
'''***************************************************************'''
print 'sample 5'
file = open("wr.bin","wb")
file.write("\xde\x02\x00\x00\x00\x14\x04\xca\x3a\x71\x38\x9c")
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

'''sample 6'''
'''***************************************************************'''
print 'sample 6'
file = open("wr.bin","wb")
file.write("\xde\x02\x00\x00\x00\x18\x04\xca\x3a\x71\x38\x9C")
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
 

'''sample 7'''
'''***************************************************************'''
print 'sample 7'
file = open("wr.bin","wb")
file.write("\xde\x02\x00\x00\x00\x1C\x04\xca\x3a\x71\x38\x9c")
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

'''sample 8'''
'''***************************************************************'''
print 'sample 8'
file = open("wr.bin","wb")
file.write("\xde\x02\x00\x00\x00\x20\x04\xca\x3a\x71\x38\x9c")
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

'''sample 9'''
'''***************************************************************'''
print 'sample 9'
file = open("wr.bin","wb")
file.write("\xde\x02\x00\x00\x00\x24\x04\xca\x3a\x71\x48\xa4")
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





'''sample 10'''
'''***************************************************************'''
print 'sample 10'
file = open("wr.bin","wb")
file.write("\xde\x02\x00\x00\x00\x28\x04\xca\x3a\x91\x48\xa4")
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


'''sample 11'''
'''***************************************************************'''
print 'sample 11'
file = open("wr.bin","wb")
file.write("\xde\x02\x00\x00\x00\x2c\x04\xca\x3a\x91\x48\xa4")
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

'''sample 12'''
'''***************************************************************'''
print 'sample 12'
file = open("wr.bin","wb")
file.write("\xde\x02\x00\x00\x00\x30\x04\xca\x3a\x91\x48\x9c")
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

'''sample 13'''
'''***************************************************************'''
print 'sample 13'
file = open("wr.bin","wb")
file.write("\xde\x02\x00\x00\x00\x34\x04\xca\x3a\x71\x48\xa4")
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

'''sample 14'''
'''***************************************************************'''
print 'sample 14'
file = open("wr.bin","wb")
file.write("\xde\x02\x00\x00\x00\x38\x04\xca\x3a\x91\x38\xa4")
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

'''sample 15'''
'''***************************************************************'''
print 'sample 15'
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

print 'upd on/off'

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
print 'reading results 0 & 1  01fc 0000 '
file = open("wr.bin","wb")
file.write("\xde\x02\x00\x00\x00\x48\x04\xca\x00\x00\x00\x00")
file.close
file = open("wr.bin","rb")
data = file.read(12)
x = binascii.b2a_hex(data)
print x
for i in range(12):
	ser.write(data[i])
reply = ser.read(8)
x = binascii.b2a_hex(reply)
print x
reply = ser.read(2)
x = binascii.b2a_hex(reply)
print x
reply = ser.read(2)
x = binascii.b2a_hex(reply)
print x
print 'reading results 0 & 1  01fc 0000 '
file = open("wr.bin","wb")
file.write("\xde\x02\x00\x00\x00\x48\x04\xca\x00\x00\x00\x00")
file.close
file = open("wr.bin","rb")
data = file.read(12)
x = binascii.b2a_hex(data)
print x
for i in range(12):
	ser.write(data[i])
reply = ser.read(8)
x = binascii.b2a_hex(reply)
print x
reply = ser.read(2)
x = binascii.b2a_hex(reply)
print x
reply = ser.read(2)
x = binascii.b2a_hex(reply)
print x
print 'reading results 2 & 3 01fc 01fc'
file = open("wr.bin","wb")
file.write("\xde\x02\x00\x00\x00\x4C\x04\xca\x00\x00\x00\x00")
file.close
file = open("wr.bin","rb")
data = file.read(12)
x = binascii.b2a_hex(data)
print x
for i in range(12):
	ser.write(data[i])
reply = ser.read(8)
x = binascii.b2a_hex(reply)
print x
reply = ser.read(2)
x = binascii.b2a_hex(reply)
print x
reply = ser.read(2)
x = binascii.b2a_hex(reply)
print x
print 'reading results 2 & 3 01fc 01fc'
file = open("wr.bin","wb")
file.write("\xde\x02\x00\x00\x00\x4C\x04\xca\x00\x00\x00\x00")
file.close
file = open("wr.bin","rb")
data = file.read(12)
x = binascii.b2a_hex(data)
print x
for i in range(12):
	ser.write(data[i])
reply = ser.read(8)
x = binascii.b2a_hex(reply)
print x
reply = ser.read(2)
x = binascii.b2a_hex(reply)
print x
reply = ser.read(2)
x = binascii.b2a_hex(reply)
print x
print 'reading results 4 & 5 0000 0000'
file = open("wr.bin","wb")
file.write("\xde\x02\x00\x00\x00\x50\x04\xca\x00\x00\x00\x00")
file.close
file = open("wr.bin","rb")
data = file.read(12)
x = binascii.b2a_hex(data)
print x

file.close
file = open("wr.bin","rb")
for i in range(12):
	ser.write(data[i])
reply = ser.read(8)
x = binascii.b2a_hex(reply)
print x
reply = ser.read(2)
x = binascii.b2a_hex(reply)
print x
reply = ser.read(2)
x = binascii.b2a_hex(reply)
print x

print 'reading results 4 & 5 0000 0000'
file = open("wr.bin","wb")
file.write("\xde\x02\x00\x00\x00\x50\x04\xca\x00\x00\x00\x00")
file.close
file = open("wr.bin","rb")
data = file.read(12)
x = binascii.b2a_hex(data)
print x

file.close
file = open("wr.bin","rb")
for i in range(12):
	ser.write(data[i])
reply = ser.read(8)
x = binascii.b2a_hex(reply)
print x
reply = ser.read(2)
x = binascii.b2a_hex(reply)
print x
reply = ser.read(2)
x = binascii.b2a_hex(reply)
print x 
 
print 'reading results 6 & 7 0000 0000 '
file = open("wr.bin","wb")
file.write("\xde\x02\x00\x00\x00\x54\x04\xca\x00\x00\x00\x00")
file.close
file = open("wr.bin","rb")
data = file.read(12)
x = binascii.b2a_hex(data)
print x
for i in range(12):
	ser.write(data[i])
reply = ser.read(8)
x = binascii.b2a_hex(reply)
print x
reply = ser.read(2)
x = binascii.b2a_hex(reply)
print x
reply = ser.read(2)
x = binascii.b2a_hex(reply)
print x

print 'reading results 6 & 7 0000 0000 '
file = open("wr.bin","wb")
file.write("\xde\x02\x00\x00\x00\x54\x04\xca\x00\x00\x00\x00")
file.close
file = open("wr.bin","rb")
data = file.read(12)
x = binascii.b2a_hex(data)
print x
for i in range(12):
	ser.write(data[i])
reply = ser.read(8)
x = binascii.b2a_hex(reply)
print x
reply = ser.read(2)
x = binascii.b2a_hex(reply)
print x
reply = ser.read(2)
x = binascii.b2a_hex(reply)
print x
print 'reading results 8 & 9 0004 0000'
file = open("wr.bin","wb")
file.write("\xde\x02\x00\x00\x00\x58\x04\xca\x00\x00\x00\x00")
file.close
file = open("wr.bin","rb")
data = file.read(12)
x = binascii.b2a_hex(data)
print x
for i in range(12):
	ser.write(data[i])
reply = ser.read(8)
x = binascii.b2a_hex(reply)
print x
reply = ser.read(2)
x = binascii.b2a_hex(reply)
print x
reply = ser.read(2)
x = binascii.b2a_hex(reply)
print x

print 'reading results 8 & 9 0004 0000'
file = open("wr.bin","wb")
file.write("\xde\x02\x00\x00\x00\x58\x04\xca\x00\x00\x00\x00")
file.close
file = open("wr.bin","rb")
data = file.read(12)
x = binascii.b2a_hex(data)
print x
for i in range(12):
	ser.write(data[i])
reply = ser.read(8)
x = binascii.b2a_hex(reply)
print x
reply = ser.read(2)
x = binascii.b2a_hex(reply)
print x
reply = ser.read(2)
x = binascii.b2a_hex(reply)
print x

print 'reading results 10 & 11 0000 0000 '
file = open("wr.bin","wb")
file.write("\xde\x02\x00\x00\x00\x5C\x04\xca\x00\x00\x00\x00")
file.close
file = open("wr.bin","rb")
data = file.read(12)
x = binascii.b2a_hex(data)
print x
for i in range(12):
	ser.write(data[i])
reply = ser.read(8)
x = binascii.b2a_hex(reply)
print x
reply = ser.read(2)
x = binascii.b2a_hex(reply)
print x
reply = ser.read(2)
x = binascii.b2a_hex(reply)
print x

print 'reading results 10 & 11 0000 0000 '
file = open("wr.bin","wb")
file.write("\xde\x02\x00\x00\x00\x5C\x04\xca\x00\x00\x00\x00")
file.close
file = open("wr.bin","rb")
data = file.read(12)
x = binascii.b2a_hex(data)
print x
for i in range(12):
	ser.write(data[i])
reply = ser.read(8)
x = binascii.b2a_hex(reply)
print x
reply = ser.read(2)
x = binascii.b2a_hex(reply)
print x
reply = ser.read(2)
x = binascii.b2a_hex(reply)
print x

print 'reading results 12 & 13 0004 0004'
file = open("wr.bin","wb")
file.write("\xde\x02\x00\x00\x00\x60\x04\xca\x00\x00\x00\x00")
file.close
file = open("wr.bin","rb")
data = file.read(12)
x = binascii.b2a_hex(data)
print x
for i in range(12):
	ser.write(data[i])
reply = ser.read(8)
x = binascii.b2a_hex(reply)
print x
reply = ser.read(2)
x = binascii.b2a_hex(reply)
print x
reply = ser.read(2)
x = binascii.b2a_hex(reply)
print x

print 'reading results 12 & 13 0004 0004'
file = open("wr.bin","wb")
file.write("\xde\x02\x00\x00\x00\x60\x04\xca\x00\x00\x00\x00")
file.close
file = open("wr.bin","rb")
data = file.read(12)
x = binascii.b2a_hex(data)
print x
for i in range(12):
	ser.write(data[i])
reply = ser.read(8)
x = binascii.b2a_hex(reply)
print x
reply = ser.read(2)
x = binascii.b2a_hex(reply)
print x
reply = ser.read(2)
x = binascii.b2a_hex(reply)
print x

print 'reading results 14 & 15 0008 01F8'
file = open("wr.bin","wb")
file.write("\xde\x02\x00\x00\x00\x64\x04\xca\x00\x00\x00\x00")
file.close
file = open("wr.bin","rb")
data = file.read(12)
x = binascii.b2a_hex(data)
print x
for i in range(12):
	ser.write(data[i])
reply = ser.read(8)
x = binascii.b2a_hex(reply)
print x
reply = ser.read(2)
x = binascii.b2a_hex(reply)
print x
reply = ser.read(2)
x = binascii.b2a_hex(reply)
print x
print 'reading results 14 & 15 0008 01F8'
file = open("wr.bin","wb")
file.write("\xde\x02\x00\x00\x00\x64\x04\xca\x00\x00\x00\x00")
file.close
file = open("wr.bin","rb")
data = file.read(12)
x = binascii.b2a_hex(data)
print x
for i in range(12):
	ser.write(data[i])
reply = ser.read(8)
x = binascii.b2a_hex(reply)
print x
reply = ser.read(2)
x = binascii.b2a_hex(reply)
print x
reply = ser.read(2)
x = binascii.b2a_hex(reply)
print x
'''***************************************************************'''



end_time = time.ctime()

print start_time, end_time
