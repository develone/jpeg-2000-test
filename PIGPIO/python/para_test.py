import pigpio

pi = pigpio.pi() 

#CH14 a_dstb
GPIO=14
pi.set_pull_up_down(GPIO, pigpio.PUD_UP)
v = pi.read(GPIO)
print 'CH14 B15','BCM14','a_dstb',v

#CH31 a_astb
GPIO=2
pi.set_pull_up_down(GPIO, pigpio.PUD_UP)
v = pi.read(GPIO)
print 'CH31 A2','BCM2','a_astb',v

#CH22 a_write
GPIO=5
pi.set_pull_up_down(GPIO, pigpio.PUD_UP)
v = pi.read(GPIO)
print 'CH22 H1','BCM5','a_write',v

#CH13 a_wait
GPIO=15
pi.set_pull_up_down(GPIO, pigpio.PUD_UP)
v = pi.read(GPIO)
print 'CH13 B16','BCM15','a_wait',v
print 

# data to FPGA 
#CH6 fr_rpi2B<0>" LOC = "K16" 
GPIO=12
pi.set_pull_up_down(GPIO, pigpio.PUD_UP)
v = pi.read(GPIO)
print 'CH6 K16','BCM12','fr_rpi2B<0>',v

#CH2 fr_rpi2B<1>" LOC = "R16" 
GPIO=19
pi.set_pull_up_down(GPIO, pigpio.PUD_UP)
v = pi.read(GPIO)
print 'CH2 R16','BCM19','fr_rpi2B<1>',v

#CH4 fr_rpi2B<2>" LOC = "M16" 
GPIO=13
pi.set_pull_up_down(GPIO, pigpio.PUD_UP)
v = pi.read(GPIO)
print 'CH4 M16','BCM13','fr_rpi2B<2>',v

#CH5 fr_rpi2B<3>" LOC = "K15" 
GPIO=6
pi.set_pull_up_down(GPIO, pigpio.PUD_UP)
v = pi.read(GPIO)
print 'CH5 K15','BCM6','fr_rpi2B<3>',v

#CH12 fr_rpi2B<4>" LOC = "C15" 
GPIO=18
pi.set_pull_up_down(GPIO, pigpio.PUD_UP)
v = pi.read(GPIO)
print 'CH12 C15','BCM18','fr_rpi2B<4>',v

#CH1 fr_rpi2B<5>" LOC = "R15" 
GPIO=20
pi.set_pull_up_down(GPIO, pigpio.PUD_UP)
v = pi.read(GPIO)
print 'CH1 R15','BCM20','fr_rpi2B<5>',v

#CH3 fr_rpi2B<6>" LOC = "M15" 
GPIO=16
pi.set_pull_up_down(GPIO, pigpio.PUD_UP)
v = pi.read(GPIO)
print 'CH3 M15','BCM16','fr_rpi2B<6>',v

#CH7 fr_rpi2B<7>" LOC = "J16" 
GPIO=7
pi.set_pull_up_down(GPIO, pigpio.PUD_UP)
v = pi.read(GPIO)
print 'CH7 J16','BCM7','fr_rpi2B<7>',v
print 

# data from FPGA 
#CH23 to_rpi2B<0>" LOC = "H2" 
GPIO=11
pi.set_pull_up_down(GPIO, pigpio.PUD_UP)
v = pi.read(GPIO)
print 'CH23 H2','BCM11','to_rpi2B<0>',v

#CH25 to_rpi2B<1>" LOC = "F2" 
GPIO=10
pi.set_pull_up_down(GPIO, pigpio.PUD_UP)
v = pi.read(GPIO)
print 'CH25 F2','BCM10','to_rpi2B<1>',v

#CH27 to_rpi2B<2>" LOC = "E2" 
GPIO=27
pi.set_pull_up_down(GPIO, pigpio.PUD_UP)
v = pi.read(GPIO)
print 'CH27 E2','BCM27','to_rpi2B<2>',v

#CH29 to_rpi2B<3>" LOC = "B1" 
GPIO=4
pi.set_pull_up_down(GPIO, pigpio.PUD_UP)
v = pi.read(GPIO)
print 'CH29 B1','BCM4','to_rpi2B<3>',v

#CH24 to_rpi2B<4>" LOC = "F1" 
GPIO=19
pi.set_pull_up_down(GPIO, pigpio.PUD_UP)
v = pi.read(GPIO)
print 'CH24 F1','BCM19','to_rpi2B<4>',v

#CH26 to_rpi2B<5>" LOC = "E1" 
GPIO=22
pi.set_pull_up_down(GPIO, pigpio.PUD_UP)
v = pi.read(GPIO)
print 'CH26 E1','BCM22','to_rpi2B<5>',v

#CH28 to_rpi2B<6>" LOC = "C1" 
GPIO=17
pi.set_pull_up_down(GPIO, pigpio.PUD_UP)
v = pi.read(GPIO)
print 'CH28 C1','BCM17','to_rpi2B<6>',v

#CH30 to_rpi2B<7>" LOC = "B2" 
GPIO=3
pi.set_pull_up_down(GPIO, pigpio.PUD_UP)
v = pi.read(GPIO)
print 'CH30 B2','BCM3','to_rpi2B<7>',v



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

def fr_rpi2B(to_fpga):
    b0 = 12
    b1 = 19
    b2 = 13
    b3 = 6
    b4 = 18
    b5 = 20
    b6 = 16
    b7 = 16
to_rpi2B()

