import pigpio
from myhdl import bin

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
    b4 = 9
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
'''
NET "to_rpi2B<0>" LOC = "H2" ; BCM11
NET "to_rpi2B<1>" LOC = "F2" ; BCM10
NET "to_rpi2B<2>" LOC = "E2" ; BCM27
NET "to_rpi2B<3>" LOC = "B1" ; BCM4
NET "to_rpi2B<4>" LOC = "F1" ; BCM9
NET "to_rpi2B<5>" LOC = "E1" ; BCM22
NET "to_rpi2B<6>" LOC = "C1" ; BCM17
NET "to_rpi2B<7>" LOC = "B2" ; BCM3
'''

def fr_rpi2B(to_fpga):
    b0 = 12
    b1 = 19
    b2 = 13
    b3 = 6
    b4 = 18
    b5 = 20
    b6 = 16
    b7 = 7 
    bits = [b0,b1,b2,b3,b4,b5,b6,b7]
    ones = []
    #print bin(to_fpga,8)
    for i in range(8):
		x = to_fpga & 2**i
		if (x == 0):
                   ones.append(0)
                else:
                   ones.append(1)
		#print i, x, bits[i]
    #print ones, bits
    for i in range(8):
       GPIO = bits[i]
       #print GPIO, ones[i]
       pi.write(GPIO,ones[i])
       yy = pi.read(GPIO)
       #print i, yy, GPIO 
'''
NET "fr_rpi2B<0>" LOC = "K16" ; BCM12
NET "fr_rpi2B<1>" LOC = "R16" ; BCM19
NET "fr_rpi2B<2>" LOC = "M16" ; BCM13
NET "fr_rpi2B<3>" LOC = "K15" ; BCM6 
NET "fr_rpi2B<4>" LOC = "C15" ; BCM18
NET "fr_rpi2B<5>" LOC = "R15" ; BCM20
NET "fr_rpi2B<6>" LOC = "M15" ; BCM16
NET "fr_rpi2B<7>" LOC = "J16" ; BCM7
'''      
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

def pullup_a_write():
    #CH33 a_write
    GPIO=5
    pi.set_pull_up_down(GPIO, pigpio.PUD_UP)
    v = pi.read(GPIO)
    print 'CH22 H1','BCM5','a_write',v
    
def a_write_lo_hi():
    GPIO=5
    pi.write(GPIO,0)
    v = pi.read(GPIO)
    print 'CH22 H1','BCM5','a_write',v   	
    pi.write(GPIO,1)
    v = pi.read(GPIO)
    print 'CH22 H1','BCM5','a_write',v   	


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
pullup_a_write()
to_rpi2B()
GPIO=15 
v = pi.read(GPIO)
print v
for jj in range(128):
    print 'fr_rpi2B',jj
	fr_rpi2B(jj)
	a_astb_lo_hi()
	a_write_lo_hi()
	GPIO = 15
	v = pi.read(GPIO)
	print 'a_wait', v
for jj in range(128):
    print 'fr_rpi2B',jj
	fr_rpi2B(jj)
	a_dstb_lo_hi()
	a_write_lo_hi()
	GPIO = 15
	v = pi.read(GPIO)
	print 'a_wait', v
        to_rpi2B()
