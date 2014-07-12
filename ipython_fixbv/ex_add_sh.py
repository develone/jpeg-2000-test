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
    
x = intbv(100, min = -255, max = 255)
y = intbv(110, min = -255, max = 255)
res = y - ((x >> 1) + (y >> 1))
print (x), (y), (res)
print hex(x), hex(y), hex(res)
print
x = intbv(202, min = -255, max = 255)
y = intbv(182, min = -255, max = 255)
res = y - ((x >> 1) + (y >> 1))
print (x), (y), (res)
print hex(x), hex(y), hex(res)
t= (0x1f6)
z = bin(t)
print z, hex(t)
print '-',toTwosComplement(z)
print
x = intbv(200, min = -255, max = 255)
y = intbv(174, min = -255, max = 255)
res = y - ((x >> 1) + (y >> 1))
print (x), (y), (res)
print hex(x), hex(y), hex(res)
t= (0x1f3)
z = bin(t)
print z, hex(t)
print '-',toTwosComplement(z)
print
x = intbv(204, min = -255, max = 255)
y = intbv(194, min = -255, max = 255)
res = y - ((x >> 1) + (y >> 1))
print (x), (y), (res)
print hex(x), hex(y), hex(res)
t= (0x1fb)
z = bin(t)
print z, hex(t)
print '-',toTwosComplement(z)
print

x = intbv(106, min = -255, max = 255)
y = intbv(126, min = -255, max = 255)
res = y - ((x >> 1) + (y >> 1))
print (x), (y), (res)
print hex(x), hex(y), hex(res)
print
x = intbv(136, min = -255, max = 255)
y = intbv(106, min = -255, max = 255)
res = y - ((x >> 1) + (y >> 1))
print (x), (y), (res)
print hex(x), hex(y), hex(res)
t= (0x1f1)
z = bin(t)
print z, hex(t)
print '-',toTwosComplement(z)
print
x = intbv(100, min = -255, max = 255)
y = intbv(96, min = -255, max = 255)
res = ((x) + (y) + 2)>>2
print hex(x), hex(y), hex(res)
