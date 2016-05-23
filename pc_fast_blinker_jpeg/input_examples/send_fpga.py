import serial
import binascii
reply = []
ser = serial.Serial ("/dev/ttyAMA0")    
ser.baudrate = 115200
file_out = open("samples.bin","rb")
file_out1 = open("results.bin","rb")
file_in = open("data_from_fpga.bin","wb") 
for j in range(1):
    for l in range(16):
        data = file_out.read(12)
        for i in range(12):
            ser.write(data[i])
            #print i
        reply = ser.read(12)
        #print "this is the sample", reply
    for l in range(2):
        data = file_out1.read(12)
        for i in range(12):
            ser.write(data[i])
            #print i
        reply = ser.read(12)
        #print "this is on/off", reply
    for l in range(8):
        data = file_out1.read(12)
        for i in range(12):
            ser.write(data[i])
            #print i
        reply = ser.read(8)
        print "this is first part of reply", reply
        reply = ser.read(2)
        x = binascii.b2a_hex(reply)
        print x
        reply = ser.read(2)
        x = binascii.b2a_hex(reply)
        print x
        
 
