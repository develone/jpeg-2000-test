import serial
import time
import binascii
ser = serial.Serial ("/dev/ttyAMA0")    
ser.baudrate = 1000000
data ="abcdefghijklmnopqrst"
#sudo stty -F /dev/ttyAMA0 1000000 -ixon -crtscts
while(1):
    for i in range(19):
	   print data[i]
	   x = binascii.b2a_hex(data[i])
	   print x
	   ser.write(x)
	   reply = []
	   reply = ser.read(1)
	   y = binascii.b2a_hex(reply)
	   if (y == x):
		   print x,y
