import pigpio

pi = pigpio.pi()
def pullup_a_astb():
    #CH31 a_dstb
    GPIO=2
    pi.set_pull_up_down(GPIO, pigpio.PUD_UP)
    v = pi.read(GPIO)
    print 'CH31 A2','BCM2','a_astb',v

def a_astb_lo():
    GPIO=2
    pi.write(GPIO,0)
    v = pi.read(GPIO)
    print 'CH31 A2','BCM2','a_astb',v   	

def a_astb_lo_hi():
    GPIO=2
    pi.write(GPIO,0)
    v = pi.read(GPIO)
    print 'CH31 A2','BCM2','a_astb',v   	
    pi.write(GPIO,1)
    v = pi.read(GPIO)
    print 'CH31 A2','BCM2','a_astb',v   	

def pullup_a_dstb():
    #CH14 a_dstb
    GPIO=14
    pi.set_pull_up_down(GPIO, pigpio.PUD_UP)
    v = pi.read(GPIO)
    print 'CH14 B15','BCM14','a_dstb',v

def a_dstb_lo():
    GPIO=14
    pi.write(GPIO,0)
    v = pi.read(GPIO)
    print 'CH14 B15','BCM14','a_dstb',v   	

def a_dstb_lo_hi():
    GPIO=14
    pi.write(GPIO,0)
    v = pi.read(GPIO)
    print 'CH14 B15','BCM14','a_dstb',v   	
    pi.write(GPIO,1)
    v = pi.read(GPIO)
    print 'CH14 B15','BCM14','a_dstb',v   	

def ck_a_wait():
    GPIO=15
    v = pi.read(GPIO)
    while(v == 1):
        v = pi.read(GPIO)
    print 'a_wait goes lo'

pullup_a_astb()
pullup_a_dstb()
  
a_astb_lo_hi()
a_dstb_lo_hi()

print 'reset the FPGA'
print 'xstest -u 0 -b xula2-lx9'
print 'reload the program'
print 'xsload --usb 0 --fpga xula2_wait.bit'

ck_a_wait()
print 'testing making a_wait go hi' 
pullup_a_astb()
pullup_a_dstb()
GPIO=15 
v = pi.read(GPIO)
print v
a_astb_lo_hi()
a_dstb_lo_hi()
GPIO=15 
v = pi.read(GPIO)
print v
ck_a_wait()
