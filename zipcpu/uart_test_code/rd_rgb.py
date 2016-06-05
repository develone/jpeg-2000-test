import serial
import time
ser = serial.Serial ("/dev/ttyAMA0")    
ser.baudrate = 1000000
     
file = open("rgb.bin", "rb")
reply=[]
print "waiting for hello, world!"

reply = ser.read(14)
print reply
start_time = time.time()        
print "sending data"
for i in range(65536):
    data = file.read(3)
    #print data 
    ser.write(data) 
end_time = time.time()
print "transfer time", end_time-start_time, "sec"
reply=[]
print "waiting for Data rdy     !"
reply = ser.read(14)
print reply
 
