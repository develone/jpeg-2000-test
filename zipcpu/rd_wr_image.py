from __future__ import division
from __future__ import print_function

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

for col in range(w):
	for row in range(h):
                pixel = m[row][col]
		print ("col %d row %d pixel %d " % (col, row, pixel))
                ml = []
                for jj in range(3):
                	ml.append(0)
 		ml.append(pixel)
		ba = bytearray(ml)
		file_out.write(ba)
file_out.close()


