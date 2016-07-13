import serial
import time
import binascii
import pigpio
import os

pi = pigpio.pi()
zipcpu14 = 2
print "signal from zipcpu",pi.read(zipcpu14)
ser = serial.Serial ("/dev/ttyAMA0")    
ser.baudrate = 1000000
     
#file = open("rgb.bin", "rb")
reply=[]
print "waiting for hello, world!"

while(not pi.read(zipcpu14)):
	pi.read(zipcpu14)
print "signal from zipcpu",pi.read(zipcpu14)
reply = ser.read(15)
#print reply

start_time = time.time()        
print "sending data"
os.system("dd if=rgb.bin of=/dev/ttyAMA0 bs=196608")
    
end_time = time.time()
print "transfer time", end_time-start_time, "sec"
#file.close()
start_time = time.time()
reply=[]
print "waiting for Data rdy     !"
reply = ser.read(262144)
end_time = time.time()
print "transfer time", end_time-start_time, "sec"
print len(reply) 
file = open("r_dwt_zip.bin", "wb")
file.write(reply)
file.close()
start_time = time.time()
reply=[]
print "waiting for Data rdy     !"
reply = ser.read(262144)
end_time = time.time()
print "transfer time", end_time-start_time, "sec"
print len(reply) 
file = open("g_dwt_zip.bin", "wb")
file.write(reply)
file.close()
start_time = time.time()
reply=[]
print "waiting for Data rdy     !"
reply = ser.read(262144)
end_time = time.time()
print "transfer time", end_time-start_time, "sec"
print len(reply) 
file = open("b_dwt_zip.bin", "wb")
file.write(reply)
file.close()
