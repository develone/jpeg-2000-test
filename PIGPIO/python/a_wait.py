import pigpio

pi = pigpio.pi()
def to_rpi2B():
    '''
    to_rpi2B 
    data from FPGA to rpi2B
    output [7:0] to_rpi2B; 
    '''
    v = 0
    b0 = 11
    b1 = 10
    b2 = 27
    b3 = 4
    b4 = 19
    b5 = 22
    b6 = 17
    b7 = 3
    v7 = pi.read(b7)*128
    v6 = pi.read(b6)*64
    v5 = pi.read(b5)*32
    v4 = pi.read(b4)*16
    v3 = pi.read(b3)*8
    v2 = pi.read(b2)*4
    v1 = pi.read(b1)*2
    v0 = pi.read(b0)
    v = v7 + v6 +v5 + v4 + v3 + v2 + v1 + v0
    print 'to_rpi2B',v
    
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
to_rpi2B()
GPIO=15 
v = pi.read(GPIO)
print v
a_astb_lo_hi()
a_dstb_lo_hi()
GPIO=15 
v = pi.read(GPIO)
print v
ck_a_wait()
