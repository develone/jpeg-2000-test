from __future__ import division
from __future__ import print_function
'''
reads the file ../lena_256.png
starts 0x800000 
ends 0x8ffff
little endian
0000000 009c 0000 00a4 0000 00a4 0000 00a4 0000
0000020 009c 0000 009c 0000 009c 0000 00a4 0000
0000040 009c 0000 009c 0000 009c 0000 009c 0000
		.
		.
		.
0777720 003c 0000 003c 0000 002c 0000 0034 0000
0777740 003c 0000 002c 0000 0034 0000 0044 0000
0777760 004c 0000 005c 0000 0064 0000 006c 0000

big emdian
0000000 0000 9c00 0000 a400 0000 a400 0000 a400
0000020 0000 9c00 0000 9c00 0000 9c00 0000 a400
0000040 0000 9c00 0000 9c00 0000 9c00 0000 9c00
 		.
		.
		. 
0777720 0000 3c00 0000 3c00 0000 2c00 0000 3400
0777740 0000 3c00 0000 2c00 0000 3400 0000 4400
0777760 0000 4c00 0000 5c00 0000 6400 0000 6c00
1000000
loads the sdram with the data from the file img_to_fpga.bin
dumpsdram jpeg-2000-test/zipcpu/img_to_fpga.bin xx
col 0 0x800000 0x8000ff
col 1 0x800100 0x8001ff
col 2 0x800200 0x8002ff
col 255 0x80ff00 0x80ffff
''' 
from PIL import Image # Part of the standard Python Library

import binascii

def rd_img(imgfn): 
    im = Image.open(imgfn)
    pix = im.load()
    m = list(im.getdata())
    #print m.__sizeof__()
    m = [m[i:i+im.size[0]] for i in range(0, len(m), im.size[0])]
    return im, m, pix
file_out = open("img_to_fpga.bin","wb")

imgfn = "../lena_256.png"
im, m, pix = rd_img(imgfn)
#print type(im), type(m), type(pix)
w, h = im.size

file_out = open("img_to_fpga.bin","wb") 

print ("w = %d h = %d" % (w, h))
memsdram = 0x00800000
for col in range(w):
	for row in range(h):
                pixel = m[row][col]
		print ("col %d row %d pixel %d sdram %s" % (col, row, pixel,hex(memsdram)))
                ml = []
                ml.append(pixel)
                for jj in range(3):
                	ml.append(0)
 		#ml.append(pixel)
		ba = bytearray(ml)
		file_out.write(ba)
                memsdram = memsdram + 1
file_out.close()


