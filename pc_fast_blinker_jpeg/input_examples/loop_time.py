import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pi_in = 23
ctn = 0
ctn_on = 0
ctn_off = 0
flag = 0
delay = 10
time_stop = 0
test_ctn = 1000000
GPIO.setup(pi_in, GPIO.OUT)
time_start = time.time()
while flag == 0:
	if (ctn <= test_ctn):
		GPIO.output(pi_in,True)
		ctn = ctn + 1
		ctn_on = ctn_on + 1
	else:
		flag = 1
		time_stop = time.time()
	GPIO.output(pi_in,False)
	ctn_off = ctn_off + 1
    
	    
time_loop = time_stop - time_start
print time_start, time_stop
print ctn_on, ctn_off
print time_loop
	
