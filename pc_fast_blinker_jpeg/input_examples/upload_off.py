import serial
file = open("led_off.bin", "rb")
data = file.read(12)
ser = serial.Serial ("/dev/ttyAMA0")    
ser.baudrate = 115200                      

print data
ser.write(data) 
 
file.close

