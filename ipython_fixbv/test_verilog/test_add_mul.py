

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
res1 = (0)
x2 = (80)
x3 = (120)
x4 = (164)
x5 = (164)
ca3 = 115724
ca2 = -6945
ca1 = -207898
ra4 = -58132
ra2 = 6944
ra3 = -115725
ra1 = 207897
ca4 = 58131
 
 

res1 = (x4 + x5) * ca2
print hex(x4),hex(x5),hex(res1),bin(res1)
#0xa4 0xa4 -0x22c248 -0b1000101100001001001000
#The bin(res1) was put in the function below an ran again
    
print toTwosComplement('1000101100001001001000')
# -  D      3   D   B    8
#0111010011110110111000
