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
ww = (26,18)

 
 
ca1 = fixbv(-1.586134342)[ww]
ca2 = fixbv(-0.05298011854)[ww]
ca3 = fixbv(0.8829110762)[ww]
ca4 = fixbv(0.4435068522)[ww]
ra2 = fixbv(0.05298011854)[ww]

x2 = fixbv(100.0)[ww]
x3 = fixbv(110.0)[ww]
d3 = (x2 + x3) * ca1

print (x2),(x3)
print hex(x2),hex(x3),hex(d3)

x = 0x3a42000
print 'simulation results', hex(x)
z = bin(x)
print z
print '2s complement of simulation results', toTwosComplement(z)

print



print
x2 = fixbv(104.0)[ww]
x3 = fixbv(114.0)[ww]
d3 = (x2 + x3) * ca1

z = bin(d3)
print z 
print toTwosComplement(z)
 

z = bin(d3)
  
print (x2),(x3)
print hex(x2),hex(x3),hex(d3)

x = 0x3a0a000
print 'simulations', hex(x)
z = bin(x)
print z
print '2s complement of simulation results', toTwosComplement(z)

x2 = fixbv(100.0)[ww]
x3 = fixbv(110.0)[ww]
d3 = (x2 + x3) * ca1

