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
x2 = fixbv(100)[ww]
x3 = fixbv(110)[ww]

ca1 = fixbv(-1.586134342)[ww]
ca2 = fixbv(-0.05298011854)[ww]
ca3 = fixbv(0.8829110762)[ww]
ca4 = fixbv(0.4435068522)[ww]
d3 = (x2 + x3) * ca3
print d3  
print hex(x2),hex(x3),hex(d3)

#z = bin(d3)
#print z
#print toTwosComplement(z)

x2 = fixbv(101)[ww]
x3 = fixbv(111)[ww] 

d3 = (x2 + x3) * ca3
print d3  
print hex(x2),hex(x3),hex(d3)

#z = bin(d3)
#print z
#print toTwosComplement(z)

x2 = fixbv(102)[ww]
x3 = fixbv(112)[ww] 

d3 = (x2 + x3) * ca1
print d3  
print hex(x2),hex(x3),hex(d3)

z = bin(d3)
print z
print toTwosComplement(z)

x4 = fixbv(122)[ww]
x5 = fixbv(132)[ww] 

a2 = (x4 + x5) * ca4
print a2  
print hex(x4),hex(x5),hex(a2)

 


