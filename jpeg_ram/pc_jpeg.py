from myhdl import *
left = intbv(167)[16:]
right = intbv(173)[16:]
sam = intbv(170)[16:]
result = sam - ((left +  right)>>1)
print result

result = sam + ((left +  right + 2)>>2)
print result
result = sam + ((left +  right)>>1)

print result

result = sam - ((left +  right + 2)>>2)
print result