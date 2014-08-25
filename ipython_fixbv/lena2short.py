"""writing lena as 16 bit data for transfer to RAM XulA2-LX9
The tmp.bin can be written to lena.hex with the command
/bin/bin2hex.py tmp.bin lena.hex
“xsload.exe -usb 0 -ram m:\lena.hex”  where m: is the Samba_Extra on 192.168.0.69
“xsload.exe -usb 0 -u 0x0 0x7FFFF -ram m:\ttt.hex”  where m: is the Samba_Extra on 192.168.0.69
Using PIL to read the file ../lena_512.png"""

import waveletsim_53 as dwt
from array import array
a = array('h')


im = dwt.Image.open("../lena_512.png")
pix = im.load()
m = list(im.getdata())
m = [m[i:i+im.size[0]] for i in range(0, len(m), im.size[0])]
# Cast every item in the list to a float:
for row in range(0, len(m)):
        for col in range(0, len(m[0])):
                a.append(m[row][col])

print len(a)

f = open('tmp.bin','wb')
f.write(a)
f.close()
