'''
sudo /home/pi/PIGPIO/pigpiod
21 20 19 18 17 16 15 14 13 12 11 10  9  8  7  6  5  4  3  2  1  0
 b  b  b  b  b  b  R  T  n  n  n  n  W  A u2 u1 u0 p2 p1 p0  m  m


mm defines the SPI mode.

WARNING: modes 1 and 3 do not appear to work on the auxiliary device.

Mode POL PHA
 0    0   0
 1    0   1
 2    1   0
 3    1   1


px is 0 if CEx is active low (default) and 1 for active high.

ux is 0 if the CEx GPIO is reserved for SPI (default) and 1 otherwise.

A is 0 for the standard SPI device, 1 for the auxiliary SPI.

W is 0 if the device is not 3-wire, 1 if the device is 3-wire. Standard SPI device only.

nnnn defines the number of bytes (0-15) to write before switching the MOSI line to MISO to read data. This field is ignored if W is not set. Standard SPI device only.

T is 1 if the least significant bit is transmitted on MOSI first, the default (0) shifts the most significant bit out first. Auxiliary SPI device only.

R is 1 if the least significant bit is received on MISO first, the default (0) receives the 
most significant bit first. Auxiliary SPI device only.

bbbbbb defines the word size in bits (0-32). The default (0) sets 8 bits per word. Auxiliary SPI device only.

'''

import pigpio
from myhdl import bin,intbv
pi1 = pigpio.pi()
print  pi1

flgs = intbv(0)[22:]
flgs = 0

clk = 
print "flgs",bin(flgs)
h = pi1.spi_open(1,25000,flgs)

print "handle",h
pi1.spi_write(h, b'\x02\xc0\x80\x01\x02\x03')
#pi1.spi_write(h,"abc")
(b, d) = pi1.spi_read(h,6)
print b, d[0], d[1],d[2],d[3], d[4],d[5]

pi1.spi_close(h)
