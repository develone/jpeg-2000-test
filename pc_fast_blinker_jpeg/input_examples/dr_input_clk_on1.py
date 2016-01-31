import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pi_in = 19
GPIO.setup(pi_in, GPIO.OUT)

GPIO.output(pi_in,True)
