import waveletsim_53 as dwt
from  intelhex import *
from struct import *
import copy
def convert_intelhex_to_list():
	"""Converts the 16bit to list m[row][col]
	this is the procedure that will be needed in the FPGA"""

	ih_lena = IntelHex()
	ih_lena.loadhex('lena256.hex')
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
			#print row, col, m[row][col], bin(m[row][col])
			f.write(pack(fmt,m[row][col]))
	f.close()

im = dwt.Image.open("../lena_256.png")
pix = im.load()
m = list(im.getdata())

#print m.__sizeof__()
m = [m[i:i+im.size[0]] for i in range(0, len(m), im.size[0])]
m_orig = copy.deepcopy(m)
#m_orig[0][0]=300
#print m_orig[0][0], m[0][0]
#print len(m_orig[0]), len(m_orig[1])
#print m.__sizeof__()
#print len(m[0]), len(m[1])
"""Converts the 16bit to list m[row][col] this is the procedure that will be needed in the FPGA"""
#convert_intelhex_to_list()
#print m[0][0].__sizeof__()
m = dwt.fwt97_2d(m, 1)
# Convert the list of lists matrix to an image.
dwt.seq_to_img(m, pix)
#convert_list_to_bin()
# Save the transformed image.
im.save("test1_256_fwt.png")
w, h = im.size
m = dwt.upper_lower(m, w, h)
mm = copy.deepcopy(m)
mm = dwt.iwt97_2d(mm, 1)
dwt.seq_to_img(mm, pix)
mm_1lvl = copy.deepcopy(mm)

im.save("test1_256_iwt.png")

for i in range(256):
	for j in range(256):
		diff = m_orig[j][i] - mm_1lvl[j][i]
		if (diff != 0): 
			print "i", i,"j",j,"diff", diff,"orig", m_orig[j][i] , "fwd/inv",mm_1lvl[j][i]

