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

x4 = fixbv(-351.750000)
print repr(x4)
z = bin(x4)
print len(z)
sign_bit_x4 = x4 >> len(z)
print sign_bit_x4
print '   origbinary  ',z

y = toTwosComplement( z)
    
print 'TwosComplement ',y
print x4._W._fwl
print x4._W._iwl



x5 =  fixbv(-356.375000)
print repr(x5)
z = bin(x5)
print len(z)
sign_bit_x5 = x5 >> len(z)
print sign_bit_x5
print '   origbinary  ',z

y = toTwosComplement( z)

print 'TwosComplement ',y
print x5._W._fwl
print x5._W._iwl
#print xx + x5
 
