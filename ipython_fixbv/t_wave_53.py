import waveletsim_53 as dwt
from  intelhex import *
from struct import *
def convert_intelhex_to_list():
	"""Converts the 16bit to list m[row][col]
	this is the procedure that will be needed in the FPGA"""

	ih_lena = IntelHex()
	ih_lena.loadhex('lena.hex')
	pydict = ih_lena.todict()
 	i = 0
	x = 0
	for row in range(0, len(m[0])):
		for col in range(0, len(m[1])):
			#if col == 0:
				#print col, row , i
			"""creating a short int from the first & 2nd bytes"""
			x = pydict[i] + pydict[i + 1]
			m[row][col] = x
			i +=  1*2
def convert_list_to_bin():
	fmt = '>H'
	f = open('tmp_level.bin','wb')
	for row in range(0, len(m)):
		for col in range(0, len(m[0])):
			f.write(pack(fmt,m[row][col]))
	f.close()

im = dwt.Image.open("../lena_512.png")
pix = im.load()
m = list(im.getdata())
#print len(m)
m = [m[i:i+im.size[0]] for i in range(0, len(m), im.size[0])]
#print len(m[0]), len(m[1])
"""Converts the 16bit to list m[row][col] this is the procedure that will be needed in the FPGA"""
convert_intelhex_to_list()
m = dwt.fwt97_2d(m, 1)
# Convert the list of lists matrix to an image.
dwt.seq_to_img(m, pix)
convert_list_to_bin()
# Save the transformed image.
im.save("test1_512_fwt.png")
w, h = im.size
m = dwt.upper_lower(m, w, h)
mm = dwt.iwt97_2d(m, 1)
dwt.seq_to_img(mm, pix)
im.save("test1_512_iwt.png")

