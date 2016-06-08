import binascii
file = open("rgb.bin", "rb")
for i in range(65536*3):
    d0 = file.read(1)
    x = binascii.b2a_hex(d0)
    
    d1 = file.read(1)
    y = binascii.b2a_hex(d1)
    d2 = file.read(1)
    z = binascii.b2a_hex(d2)     
    print hex(i),x,y,z
