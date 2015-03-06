from myhdl import *
W0 = 10
r = (intbv(0, min= -(2**(W0-1)) ,max= (2**(W0-1))))
def tounsigned( v , w):
    ''' return an unsigned value to represent a possibly 'signed' value'''
    if v >= 0:
        return v
    else :
        return 2**w + v  # remember, v is negative


def tosigned(v, w):
    ''' return a signed representation of an 'unsigned' value '''
    if v >> (w-1) & 1:
        # high bit set -> negative
        return -(~v + 1)
    else:
        # positive
        return v
for r in range(-511,511,1):

	print "calling tounsigned", r

	y = tounsigned(r,W0-1)
	print y, bin(y,10), r,bin(r,10)

	print "calling tosigned", r
	z = tosigned(r,W0)
	print z, bin(z,10), bin(r,10)

	print "calling tosigned", y
	z = tosigned(y,W0)
	print z, bin(z,10), bin(y,10)

	print
