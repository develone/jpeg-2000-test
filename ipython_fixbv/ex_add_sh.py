from myhdl import *
def toTwosComplement(binarySequence):
    convertedSequence = [0] * len(binarySequence)
    carryBit = 1
    # INVERT THE BITS
    for i in range(0, len(binarySequence)):
        if binarySequence[i] == '0':
            convertedSequence[i] = 1
        else:
            convertedSequence[i] = 0

    # ADD BINARY DIGIT 1

    if convertedSequence[-1] == 0: #if last digit is 0, just add the 1 then there's no carry bit so return
            convertedSequence[-1] = 1
            return ''.join(str(x) for x in convertedSequence)

    for bit in range(0, len(binarySequence)):
        if carryBit == 0:
            break
        index = len(binarySequence) - bit - 1
        if convertedSequence[index] == 1:
            convertedSequence[index] = 0
            carryBit = 1
        else:
            convertedSequence[index] = 1
            carryBit = 0

    return ''.join(str(x) for x in convertedSequence)
x = intbv(0, min = -255, max = 255)
y = intbv(0, min = -255, max = 255)
z = intbv(0, min = -255, max = 255)
res = z - ((x) + (y)+2)>>2
print (x), (y), (res)
print hex(z), hex(x), hex(y), hex(res)
print 
t= (0x1ffff)
z = bin(t)
print z, hex(t)
print '-',toTwosComplement(z)
print
   
x = intbv(102, min = -255, max = 255)
y = intbv(104, min = -255, max = 255)
z = intbv(100, min = -255, max = 255)
res = z - ((x>>1) + (y>>1))
print (z),(x), (y), (res)
print hex(z), hex(x), hex(y), hex(res)
print 
t= (0x1fffd)
z = bin(t)
print z, hex(t)
print '-',toTwosComplement(z)
print 
x = intbv(102, min = -255, max = 255)
y = intbv(104, min = -255, max = 255)
z = intbv(100, min = -255, max = 255)
res = z + ((x>>1) + (y>>1))
print (z),(x), (y), (res)
print hex(z), hex(x), hex(y), hex(res)
print 

x = intbv(102, min = -255, max = 255)
y = intbv(104, min = -255, max = 255)
z = intbv(-3, min = -255, max = 255)
res = z + ((x>>1) + (y>>1))
print (z),(x), (y), (res)
print hex(z), hex(x), hex(y), hex(res)
print 
x = intbv(102, min = -255, max = 255)
y = intbv(104, min = -255, max = 255)
z = intbv(-3, min = -255, max = 255)
res = z - ((x) + (y))>>2
print (z),(x), (y), (res)
print hex(z), hex(x), hex(y), hex(res)
print  
t= (0x1ffcb)
z = bin(t)
print z, hex(t)
print '-',toTwosComplement(z)
print 
