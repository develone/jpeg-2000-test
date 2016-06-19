import serial
import time
import binascii
import pigpio

pi = pigpio.pi()
zipcpu14 = 2
print "signal from zipcpu",pi.read(zipcpu14)
ser = serial.Serial ("/dev/ttyAMA0")    
ser.baudrate = 1000000
     
file = open("rgb.bin", "rb")
reply=[]
print "waiting for hello, world!"

while(not pi.read(zipcpu14)):
	pi.read(zipcpu14)
print "signal from zipcpu",pi.read(zipcpu14)
#reply = ser.read(14)
#print reply

start_time = time.time()        
print "sending data"
for i in range(65536):
    data = file.read(3)
    #if(i == 0):
    #x = binascii.b2a_hex(data)
    #print x 
    ser.write(data) 
end_time = time.time()
print "transfer time", end_time-start_time, "sec"
file.close()
start_time = time.time()
reply=[]
print "waiting for Data rdy     !"
reply = ser.read(65536)
end_time = time.time()
print "transfer time", end_time-start_time, "sec"
print len(reply) 
file = open("rgb_dwt_zip.bin", "wb")
file.write(reply)
file.close()
