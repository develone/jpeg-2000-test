import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
clk = 15
ctn1 = 0
ss0 = 26
ctn2 = 0
ld_o = 27
ctn3 = 0
loop = 0
#With pull up
#GPIO.setup(clk, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(clk, GPIO.IN)
GPIO.setup(ss0, GPIO.IN)
GPIO.setup(ld_o, GPIO.IN)
while True:
	'''
	if (GPIO.input(clk) == True):
		ctn1 = ctn1 + 1
	else:
		if (GPIO.input(ss0) == True):
			ctn2 = ctn2 + 1
		else:
			if (GPIO.input(ss0) == True):
				ctn3 = ctn3 + 1
	
	print ctn1, ctn2, ctn3,GPIO.input(clk),GPIO.input(ld_o),GPIO.input(ss0)
	'''
	loop = loop + 1
	print loop,GPIO.input(clk),GPIO.input(ss0),GPIO.input(ld_o)
		
 
