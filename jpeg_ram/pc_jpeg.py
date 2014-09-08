from myhdl import *
left = intbv(166)[16:]
right = intbv(172)[16:]
sam = intbv(169)[16:]
result = sam + ((left +  right + 2)>>2)
print result
result = sam - ((left +  right)>>1)

print result