import serial
file = open("led_on.bin", "rb")
data = file.read(12)
ser = serial.Serial ("/dev/ttyAMA0")    
ser.baudrate = 115200                      

#print data
ser.write(data) 
reply = ser.read(12) 
print "this is the reply", reply 
file.close
