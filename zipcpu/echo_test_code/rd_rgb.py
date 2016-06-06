import serial
import time
import binascii
ser = serial.Serial ("/dev/ttyAMA0")    
ser.baudrate = 1000000
     
file = open("rgb.bin", "rb")
reply=[]
 
start_time = time.time()        
print "sending data"
for i in range(3):
    data = file.read(1)
    #if(i == 0):
    x = binascii.b2a_hex(data)
    #print x 
    ser.write(x)
    ser.read(1) 
end_time = time.time()
print "transfer time", end_time-start_time, "sec"
'''
reply=[]
print "waiting for Data rdy     !"
reply = ser.read(14)
print reply
''' 
