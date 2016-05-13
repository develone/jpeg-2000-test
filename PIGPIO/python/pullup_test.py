import pigpio

pi = pigpio.pi() 

#CH2
GPIO=19
pi.set_pull_up_down(GPIO, pigpio.PUD_UP)
v = pi.read(GPIO)
print 'ch2',v

#CH3
GPIO=16
pi.set_pull_up_down(GPIO, pigpio.PUD_UP)
v = pi.read(GPIO)
print 'ch3',v

#CH4
GPIO=13
pi.set_pull_up_down(GPIO, pigpio.PUD_UP)
v = pi.read(GPIO)
print 'ch4',v

#CH5
GPIO=6
pi.set_pull_up_down(GPIO, pigpio.PUD_UP)
v = pi.read(GPIO)
print 'ch5',v

#CH6
GPIO=12
pi.set_pull_up_down(GPIO, pigpio.PUD_UP)
v = pi.read(GPIO)
print 'ch6',v

#CH7
GPIO=7
pi.set_pull_up_down(GPIO, pigpio.PUD_UP)
v = pi.read(GPIO)
print 'ch7',v

#CH31
GPIO=2
pi.set_pull_up_down(GPIO, pigpio.PUD_UP)
v = pi.read(GPIO)
print 'ch31',v

#CH30
GPIO=3
pi.set_pull_up_down(GPIO, pigpio.PUD_UP)
v = pi.read(GPIO)
print 'ch30',v

#CH29
GPIO=4
pi.set_pull_up_down(GPIO, pigpio.PUD_UP)
v = pi.read(GPIO)
print 'ch29',v

#CH28
GPIO=17
pi.set_pull_up_down(GPIO, pigpio.PUD_UP)
v = pi.read(GPIO)
print 'ch28',v

#CH27
GPIO=27
pi.set_pull_up_down(GPIO, pigpio.PUD_UP)
v = pi.read(GPIO)
print 'ch27',v

#CH26
GPIO=22
pi.set_pull_up_down(GPIO, pigpio.PUD_UP)
v = pi.read(GPIO)
print 'ch26',v
