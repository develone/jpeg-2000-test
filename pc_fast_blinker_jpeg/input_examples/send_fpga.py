import serial
reply = []
ser = serial.Serial ("/dev/ttyAMA0")    
ser.baudrate = 115200
file_out = open("data_to_fpga.bin","rb")
file_in = open("data_from_fpga.bin","wb") 
for j in range(105060):
	data = file_out.read(12)
	for i in range(12):
		
		#print (data[i])
		ser.write(data[i])
	reply = ser.read(12)

	print "this is the reply", reply
