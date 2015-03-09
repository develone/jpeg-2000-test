from myhdl import *
from jpeg_constants import *
from rom import *
from array_jpeg import jp_process
from combine_sam import combine
from PIL import Image
#img = Image.open("lena_rgb_512.png")
img = Image.open("lena_256.png")
pix = img.load()
if (img.mode == "RGB"):
	rgb = list(img.getdata())
else:
	'''mode is L'''
	r = list(img.getdata())
w,h = img.size

results = []

if (img.mode == "RGB"):
	r = []
	g = []
	b = []
	"""get r g b from rgb"""
	for n in range(len(rgb)):
		rr, gg, bb = rgb[n]
		r.append(rr)
		g.append(gg)
		b.append(bb)
"""convert to row col"""
r = [r[i:i+img.size[0]] for i in range(0, len(r), img.size[0])]
if (img.mode == "RGB"):
	g = [g[i:i+img.size[0]] for i in range(0, len(g), img.size[0])]
	b = [b[i:i+img.size[0]] for i in range(0, len(b), img.size[0])]
def upper_lower(s, width, height):

	temp_bank = [[0]*width for i in range(height)]
	for col in range(width/2):

		for row in range(height/2):

			temp_bank[col+width/2][row+height/2] = s[row][col]

	for row in range(width):
		for col in range(height):
			s[row][col] = temp_bank[col][row]
	return s
def lower_upper(s, width, height):

	temp_bank = [[0]*width for i in range(height)]
	for col in range(width/2,width,1):

		for row in range(height/2,height,1):

			temp_bank[col-width/2][row-height/2] = s[row][col]

	for row in range(width):
		for col in range(height):
			s[row][col] = temp_bank[col][row]
	return s
def de_interleave(s,height,width):
	# de-interleave
	temp_bank = [[0]*width for i in range(height)]
	for row in range(width):
		for col in range(width):
            # k1 and k2 scale the vals
            # simultaneously transpose the matrix when deinterleaving
			if row % 2 == 0:

				temp_bank[col][row/2] =  s[row][col]
			else:

				temp_bank[col][row/2 + height/2] =  s[row][col]
    # write temp_bank to s:
	for row in range(width):
		for col in range(height):
			s[row][col] = temp_bank[row][col]
	return s

def fwt97_2d(m, nlevels=1):
    ''' Perform the CDF 9/7 transform on a 2D matrix signal m.
    nlevel is the desired number of times to recursively transform the
    signal.

    w = len(m[0])
    h = len(m)
    for i in range(nlevels):
        m = fwt97(m, w, h) # cols
        m = fwt97(m, w, h) # rows
        lower_upper(m, w, h)
        w /= 2
        h /= 2
	'''
    return m
def fwt97(s, width, height):
    ''' Forward Cohen-Daubechies-Feauveau 5 tap / 3 tap wavelet transform
    performed on all columns of the 2D n*n matrix signal s via lifting.
    The returned result is s, the modified input matrix.
    The highpass and lowpass results are stored on the left half and right
    half of s respectively, after the matrix is transposed. '''



    for col in range(width): # Do the 1D transform on all cols:
        ''' Core 1D lifting process in this loop. '''
        ''' Lifting is done on the cols. '''
        # Predict 1. y1

        for row in range(2, height-32, 34):
			if (row == 2):
				if (col == 0):
					#dummy statement
					#col == 0
					print row, col, s[row][col]


            #s[row][col] += a1 * (s[row-1][col] + s[row+1][col])


        # Update 1. y0

        for row in range(1, height-33, 34):
			if (row == 1):
				if (col == 0):
					#dummy statement
					#col = 0
					print row, col, s[row][col]


    s = de_interleave(s,height,width)
    return s
def seq_to_img(m, pix):
    ''' Copy matrix m to pixel buffer pix.
    Assumes m has the same number of rows and cols as pix. '''
    for row in range(len(m)):
        for col in range(len(m[row])):
            pix[col,row] = m[row][col]

clk_fast = Signal(bool(0))
res_out_x = Signal(intbv(0, min= -(2**(W0-1)) ,max= (2**(W0-1))))
bits_in = Signal(intbv(0, min= -(2**(W0-1)) ,max= (2**(W0-1))))
bits_in2unsigned = Signal(intbv(0)[W0:])
v = Signal(intbv(0)[W0:])
vv = Signal(intbv(0, min= -(2**(W0-1)) ,max= (2**(W0-1))))
update_s = Signal(bool(0))
noupdate_s = Signal(bool(0))
row_s = Signal(intbv(0)[8:])
col_s = Signal(intbv(0)[8:])
left_s_i = Signal(intbv(0)[LVL2*W2:])
sam_s_i = Signal(intbv(0)[LVL2*W2:])
right_s_i = Signal(intbv(0)[LVL2*W2:])
flgs_s_i = Signal(intbv(0)[LVL3*W3:])

left_com_x = Signal(intbv(0)[LVL2*W2:])
sam_com_x = Signal(intbv(0)[LVL2*W2:])
right_com_x = Signal(intbv(0)[LVL2*W2:])
lft_s_i = Signal(intbv(0)[LVL2*W2:])
sa_s_i = Signal(intbv(0)[LVL2*W2:])
rht_s_i = Signal(intbv(0)[LVL2*W2:])
a0 = Signal(intbv(0)[LVL2*W2:])
a1 = Signal(intbv(0)[LVL2*W2:])
a2 = Signal(intbv(0)[LVL2*W2:])
y0 = Signal(intbv(0)[LVL2*W2:])
y1 = Signal(intbv(0)[LVL2*W2:])
y2 = Signal(intbv(0)[LVL2*W2:])
combine_rdy_s = Signal(bool(0))
nocombine_s = Signal(bool(0))
row_ind = Signal(intbv(0)[9:])
col_ind = Signal(intbv(0)[9:])
DO_SIGNED_UNSIGNED = bool(1)

def tounsigned( v , w):
	''' return an unsigned value to represent a possibly 'signed' value'''
	if DO_SIGNED_UNSIGNED:
		if v >= 0:
			return v
		else:
			'''remember, v is negative'''
			return 2**w + v
	else:
		return v
def tosigned(v, w):
	''' return a signed representation of a 'two's complement' value '''
	if v >> (w-1) & 1:
		'''high bit set -> negative'''
		return -(2**w - v)
	else:
		'''positive'''
		return v

def tb(clk_fast, res_out_x, left_s_i,sam_s_i, right_s_i, flgs_s_i,
noupdate_s, update_s, left_com_x, sam_com_x, right_com_x,
lft_s_i, sa_s_i, rht_s_i,
combine_rdy_s, nocombine_s, row_ind, col_ind, a0, a1, a2,
y0, y1, y2,
W0=W0, LVL0=LVL0, W1=W1, LVL1=LVL1, W2=W2,
LVL2=LVL2, W3=W3, LVL3=LVL3):


	instance_rom_flgs = rom_flgs(dout_flgs, addr_flgs, ROM_CONTENT)
	instance_combine = combine( left_com_x, sam_com_x, right_com_x,
lft_s_i, sa_s_i, rht_s_i, combine_rdy_s, nocombine_s,
W0=W0, LVL0=LVL0, W1=W1, LVL1=LVL1, W2=W2,
LVL2=LVL2, W3=W3, LVL3=LVL3)

	instance_dut = jp_process( res_out_x, left_s_i,sam_s_i, right_s_i,
flgs_s_i, noupdate_s, update_s,  W0=W0, LVL0=LVL0, W1=W1, LVL1=LVL1,
W2=W2, LVL2=LVL2, W3=W3, LVL3=LVL3, SIMUL=SIMUL)
	@always(delay(10))
	def clkgen():
		clk_fast.next = not clk_fast
	DO_SIGNED_UNSIGNED = 1
	@instance
	def stimulus():

		for i in range(10):
			#print( "%3d ") % (now())
			row_ind.next = 2
			col_ind.next = 0
			#print( "%3d %d %d ") % (now(), row_ind, col_ind  )
			yield clk_fast.posedge

		for col in range(w):
			for row in range(2,h-32, 34):

				print bin(tounsigned((r[row+31][col] << W0*15), 10) | tounsigned((r[row+29][col] << W0*14), 10) | tounsigned((r[row+27][col] << W0*13), 10) | tounsigned((r[row+25][col] << W0*12), 10) | tounsigned((r[row+23][col] << W0*11), 10) | tounsigned((r[row+21][col] << W0*10), 10) | tounsigned((r[row+19][col] << W0*9), 10) | tounsigned((r[row+17][col] << W0*8), 10) | tounsigned((r[row+15][col] << W0*7), 10) | tounsigned((r[row+13][col] << W0*6), 10) | tounsigned((r[row+11][col] << W0*5), 10) | tounsigned((r[row+9][col] << W0*4), 10) | tounsigned((r[row+7][col] << W0*3), 10) | tounsigned((r[row+5][col] << W0*2), 10) | tounsigned((r[row+3][col] << W0*1), 10) | tounsigned((r[row-1][col]),10))
				print bin(tounsigned((r[row+32][col] << W0*15), 10) | tounsigned((r[row+30][col] << W0*14), 10) | tounsigned((r[row+28][col] << W0*13), 10) | tounsigned((r[row+26][col] << W0*12), 10) | tounsigned((r[row+24][col] << W0*11), 10) | tounsigned((r[row+22][col] << W0*10), 10) | tounsigned((r[row+20][col] << W0*9), 10) | tounsigned((r[row+18][col] << W0*8), 10) | tounsigned((r[row+16][col] << W0*7), 10) | tounsigned((r[row+14][col] << W0*6), 10) | tounsigned((r[row+12][col] << W0*5), 10) | tounsigned((r[row+10][col] << W0*4), 10) | tounsigned((r[row+8][col] << W0*3), 10) | tounsigned((r[row+6][col] << W0*2), 10) | tounsigned((r[row+4][col] << W0*1), 10) | tounsigned((r[row][col]), 10))
				print bin(tounsigned((r[row+33][col] << W0*15), 10) | tounsigned((r[row+31][col] << W0*14), 10) | tounsigned((r[row+29][col] << W0*13), 10) | tounsigned((r[row+27][col] << W0*12), 10) | tounsigned((r[row+25][col] << W0*11), 10) | tounsigned((r[row+23][col] << W0*10), 10) | tounsigned((r[row+21][col] << W0*9), 10) | tounsigned((r[row+19][col] << W0*8), 10) | tounsigned((r[row+17][col] << W0*7), 10) | tounsigned((r[row+15][col] << W0*6), 10) | tounsigned((r[row+13][col] << W0*5), 10) | tounsigned((r[row+11][col] << W0*4), 10) | tounsigned((r[row+9][col] << W0*3), 10) | tounsigned((r[row+7][col] << W0*2), 10) | tounsigned((r[row+5][col] << W0*1), 10) | tounsigned((r[row+1][col]), 10))
				lft_s_i.next = tounsigned((r[row+31][col] << W0*15), 10) | tounsigned((r[row+29][col] << W0*14), 10) | tounsigned((r[row+27][col] << W0*13), 10) | tounsigned((r[row+25][col] << W0*12), 10) | tounsigned((r[row+23][col] << W0*11), 10) | tounsigned((r[row+21][col] << W0*10), 10) | tounsigned((r[row+19][col] << W0*9), 10) | tounsigned((r[row+17][col] << W0*8), 10) | tounsigned((r[row+15][col] << W0*7), 10) | tounsigned((r[row+13][col] << W0*6), 10) | tounsigned((r[row+11][col] << W0*5), 10) | tounsigned((r[row+9][col] << W0*4), 10) | tounsigned((r[row+7][col] << W0*3), 10) | tounsigned((r[row+5][col] << W0*2), 10) | tounsigned((r[row+3][col] << W0*1), 10) | tounsigned((r[row-1][col]), 10)
				sa_s_i.next = tounsigned((r[row+32][col] << W0*15), 10) | tounsigned((r[row+30][col] << W0*14), 10) | tounsigned((r[row+28][col] << W0*13), 10) | tounsigned((r[row+26][col] << W0*12), 10) | tounsigned((r[row+24][col] << W0*11), 10) | tounsigned((r[row+22][col] << W0*10), 10) | tounsigned((r[row+20][col] << W0*9), 10) | tounsigned((r[row+18][col] << W0*8), 10) | tounsigned((r[row+16][col] << W0*7), 10) | tounsigned((r[row+14][col] << W0*6), 10) | tounsigned((r[row+12][col] << W0*5), 10) | tounsigned((r[row+10][col] << W0*4), 10) | tounsigned((r[row+8][col] << W0*3), 10) | tounsigned((r[row+6][col] << W0*2), 10) | tounsigned((r[row+4][col] << W0*1), 10) | tounsigned((r[row][col]), 10)
				rht_s_i.next = tounsigned((r[row+33][col] << W0*15), 10) | tounsigned((r[row+31][col] << W0*14), 10) | tounsigned((r[row+29][col] << W0*13), 10) | tounsigned((r[row+27][col] << W0*12), 10) | tounsigned((r[row+25][col] << W0*11), 10) | tounsigned((r[row+23][col] << W0*10), 10) | tounsigned((r[row+21][col] << W0*9), 10) | tounsigned((r[row+19][col] << W0*8), 10) | tounsigned((r[row+17][col] << W0*7), 10) | tounsigned((r[row+15][col] << W0*6), 10) | tounsigned((r[row+13][col] << W0*5), 10) | tounsigned((r[row+11][col] << W0*4), 10) | tounsigned((r[row+9][col] << W0*3), 10) | tounsigned((r[row+7][col] << W0*2), 10) | tounsigned((r[row+5][col] << W0*1), 10) | tounsigned((r[row+1][col]), 10)
				yield clk_fast.posedge
				'''
				y0.next = lft_s_i
				y1.next = sa_s_i
				y2.next = rht_s_i
				'''
				yield clk_fast.posedge
				#print( "%3d %d %d %s %s %s") % (now(), row, col, hex(lft_s_i), hex(sa_s_i), hex(rht_s_i))
				yield clk_fast.posedge
				combine_rdy_s.next = 1
				yield clk_fast.posedge

				left_s_i.next = left_com_x
				sam_s_i.next = sam_com_x
				right_s_i.next = right_com_x
				yield clk_fast.posedge
				#print( "%3d %d %d %s %s %s") % (now(), row, col, hex(left_s_i), hex(sam_s_i), hex(right_s_i))
				combine_rdy_s.next = 0
				yield clk_fast.posedge
				addr_flgs.next = 0
				yield clk_fast.posedge
				for i in range(16):

					flgs_s_i.next = dout_flgs
					yield clk_fast.posedge
					#print( "%3d %s") % (now(), hex(flgs_s_i))
					addr_flgs.next = addr_flgs + 1
					yield clk_fast.posedge
					update_s.next = 1
					yield clk_fast.posedge
					r[row_ind][col_ind] = res_out_x
					results.append(int(res_out_x))

					yield clk_fast.posedge

					yield clk_fast.posedge

					yield clk_fast.posedge


					#print ("%d %d %d %d %d saving even pass 1 res_out_x " ) % (now(), res_out_x, row_ind, col_ind, r[row_ind][col_ind])
					yield clk_fast.posedge

					if (row_ind == w - 2):
						row_ind.next = 2
						if (col_ind <= h - 1):
							col_ind.next = col_ind + 1
					else:
						row_ind.next = row_ind + 2

					yield clk_fast.posedge
					update_s.next = 0
					yield clk_fast.posedge
					update_s.next = 1
					yield clk_fast.posedge
					update_s.next = 0
					yield clk_fast.posedge
		row_ind.next = 1
		col_ind.next = 0
		yield clk_fast.posedge
		#print( "%3d %d %d ") % (now(), row_ind, col_ind  )

		for col in range(w):
			for row in range(1,h-33, 34):
				print bin(tounsigned((r[row+29][col] << W0*15), 10) | tounsigned((r[row+27][col] << W0*14), 10) | tounsigned((r[row+25][col] << W0*13), 10) | tounsigned((r[row+23][col] << W0*12), 10) | tounsigned((r[row+21][col] << W0*11), 10) | tounsigned((r[row+19][col] << W0*10), 10) | tounsigned((r[row+17][col] << W0*9), 10) | tounsigned((r[row+15][col] << W0*8), 10) | tounsigned((r[row+13][col] << W0*7), 10) | tounsigned((r[row+11][col] << W0*6), 10) | tounsigned((r[row+9][col] << W0*5), 10) | tounsigned((r[row+7][col] << W0*4), 10) | tounsigned((r[row+5][col] << W0*3), 10) | tounsigned((r[row+3][col] << W0*2), 10) | tounsigned((r[row+1][col] << W0*1), 10) | tounsigned((r[row-1][col]), 10 ))
				print bin(tounsigned((r[row+30][col] << W0*15), 10) | tounsigned((r[row+28][col] << W0*14), 10) | tounsigned((r[row+26][col] << W0*13), 10) | tounsigned((r[row+24][col] << W0*12), 10) | tounsigned((r[row+22][col] << W0*11), 10) | tounsigned((r[row+20][col] << W0*10), 10) | tounsigned((r[row+18][col] << W0*9), 10) | tounsigned((r[row+16][col] << W0*8), 10) | tounsigned((r[row+14][col] << W0*7), 10) | tounsigned((r[row+12][col] << W0*6), 10) | tounsigned((r[row+10][col] << W0*5), 10) | tounsigned((r[row+8][col] << W0*4), 10) | tounsigned((r[row+6][col] << W0*3), 10) | tounsigned((r[row+4][col] << W0*2), 10) | tounsigned((r[row+2][col] << W0*1), 10) | tounsigned((r[row][col]), 10 ))
				print bin(tounsigned((r[row+31][col] << W0*15), 10) | tounsigned((r[row+29][col] << W0*14), 10) | tounsigned((r[row+27][col] << W0*13), 10) | tounsigned((r[row+25][col] << W0*12), 10) | tounsigned((r[row+23][col] << W0*11), 10) | tounsigned((r[row+21][col] << W0*10), 10) | tounsigned((r[row+19][col] << W0*9), 10) | tounsigned((r[row+17][col] << W0*8), 10) | tounsigned((r[row+15][col] << W0*7), 10) | tounsigned((r[row+13][col] << W0*6), 10) | tounsigned((r[row+11][col] << W0*5), 10) | tounsigned((r[row+9][col] << W0*4), 10) | tounsigned((r[row+7][col] << W0*3), 10) | tounsigned((r[row+5][col] << W0*2), 10) | tounsigned((r[row+3][col] << W0*1), 10) | tounsigned((r[row+1][col]), 10 ))

				lft_s_i.next = tounsigned((r[row+29][col] << W0*15), 10) | tounsigned((r[row+27][col] << W0*14), 10) | tounsigned((r[row+25][col] << W0*13), 10) | tounsigned((r[row+23][col] << W0*12), 10) | tounsigned((r[row+21][col] << W0*11), 10) | tounsigned((r[row+19][col] << W0*10), 10) | tounsigned((r[row+17][col] << W0*9), 10) | tounsigned((r[row+15][col] << W0*8), 10) | tounsigned((r[row+13][col] << W0*7), 10) | tounsigned((r[row+11][col] << W0*6), 10) | tounsigned((r[row+9][col] << W0*5), 10) | tounsigned((r[row+7][col] << W0*4), 10) | tounsigned((r[row+5][col] << W0*3), 10) | tounsigned((r[row+3][col] << W0*2), 10) | tounsigned((r[row+1][col] << W0*1), 10) | tounsigned((r[row-1][col]), 10)
				sa_s_i.next = tounsigned((r[row+30][col] << W0*15), 10) | tounsigned((r[row+28][col] << W0*14), 10) | tounsigned((r[row+26][col] << W0*13), 10) | tounsigned((r[row+24][col] << W0*12), 10) | tounsigned((r[row+22][col] << W0*11), 10) | tounsigned((r[row+20][col] << W0*10), 10) | tounsigned((r[row+18][col] << W0*9), 10) | tounsigned((r[row+16][col] << W0*8), 10) | tounsigned((r[row+14][col] << W0*7), 10) | tounsigned((r[row+12][col] << W0*6), 10) | tounsigned((r[row+10][col] << W0*5), 10) | tounsigned((r[row+8][col] << W0*4), 10) | tounsigned((r[row+6][col] << W0*3), 10) | tounsigned((r[row+4][col] << W0*2), 10) | tounsigned((r[row+2][col] << W0*1), 10) | tounsigned((r[row][col]), 10)
				rht_s_i.next = tounsigned((r[row+31][col] << W0*15), 10) | tounsigned((r[row+29][col] << W0*14), 10) | tounsigned((r[row+27][col] << W0*13), 10) | tounsigned((r[row+25][col] << W0*12), 10) | tounsigned((r[row+23][col] << W0*11), 10) | tounsigned((r[row+21][col] << W0*10), 10) | tounsigned((r[row+19][col] << W0*9), 10) | tounsigned((r[row+17][col] << W0*8), 10) | tounsigned((r[row+15][col] << W0*7), 10) | tounsigned((r[row+13][col] << W0*6), 10) | tounsigned((r[row+11][col] << W0*5), 10) | tounsigned((r[row+9][col] << W0*4), 10) | tounsigned((r[row+7][col] << W0*3), 10) | tounsigned((r[row+5][col] << W0*2), 10) | tounsigned((r[row+3][col] << W0*1), 10) | tounsigned((r[row+1][col]), 10)
				yield clk_fast.posedge
				'''
				y0.next = lft_s_i
				y1.next = sa_s_i
				y2.next = rht_s_i
				yield clk_fast.posedge
				'''
				#print( "%3d %d %d %s %s %s") % (now(), row, col, hex(lft_s_i), hex(sa_s_i), hex(rht_s_i))
				combine_rdy_s.next = 1
				yield clk_fast.posedge


				left_s_i.next = left_com_x
				sam_s_i.next = sam_com_x
				right_s_i.next = right_com_x
				yield clk_fast.posedge
				#print( "%3d %d %d %s %s %s") % (now(), row, col, hex(left_s_i), hex(sam_s_i), hex(right_s_i))
				combine_rdy_s.next = 0
				yield clk_fast.posedge
				addr_flgs.next = 16
				yield clk_fast.posedge
				for i in range(16):

					flgs_s_i.next = dout_flgs
					yield clk_fast.posedge

					addr_flgs.next = addr_flgs + 1
					yield clk_fast.posedge
					update_s.next = 1
					yield clk_fast.posedge
					r[row_ind][col_ind] = res_out_x
					results.append(int(res_out_x))
					yield clk_fast.posedge
					#print ("%d %d %d %d %d saving odd pass 1 res_out_x " ) % (now(), res_out_x, row_ind, col_ind, r[row_ind][col_ind])


					if (row_ind == w - 1):
						row_ind.next = 1
						if (col_ind <= h - 2 ):
							col_ind.next = col_ind + 1
					else:
						row_ind.next = row_ind + 2

					yield clk_fast.posedge
					update_s.next = 0
					yield clk_fast.posedge
					update_s.next = 1
					yield clk_fast.posedge
					update_s.next = 0
					yield clk_fast.posedge
		temp_bank = [[0]*w for i in range(h)]
		for row in range(w):
			for col in range(w):

				if row % 2 == 0:

					temp_bank[col][row/2] =  r[row][col]
				else:

					temp_bank[col][row/2 + h/2] =  r[row][col]
		for i in range(10):
			#print( "%3d ") % (now())
			row_ind.next = 2
			col_ind.next = 0
			#print( "%3d %d %d ") % (now(), row_ind, col_ind  )
			yield clk_fast.posedge
		for row in range(w):
			for col in range(h):
				r[row][col] = temp_bank[row][col]
 		for i in range(10):
			#print( "%3d ") % (now())
			row_ind.next = 2
			col_ind.next = 0
			#print( "%3d %d %d ") % (now(), row_ind, col_ind  )
			yield clk_fast.posedge

		for col in range(w):
			for row in range(2,h-32, 34):
				print bin(tounsigned((r[row+31][col] << W0*15), 10) | tounsigned((r[row+29][col] << W0*14), 10) | tounsigned((r[row+27][col] << W0*13), 10) | tounsigned((r[row+25][col] << W0*12), 10) | tounsigned((r[row+23][col] << W0*11), 10) | tounsigned((r[row+21][col] << W0*10), 10) | tounsigned((r[row+19][col] << W0*9), 10) | tounsigned((r[row+17][col] << W0*8), 10) | tounsigned((r[row+15][col] << W0*7), 10) | tounsigned((r[row+13][col] << W0*6), 10) | tounsigned((r[row+11][col] << W0*5), 10) | tounsigned((r[row+9][col] << W0*4), 10) | tounsigned((r[row+7][col] << W0*3), 10) | tounsigned((r[row+5][col] << W0*2), 10) | tounsigned((r[row+3][col] << W0*1), 10) | tounsigned((r[row-1][col]),10))
				print bin(tounsigned((r[row+32][col] << W0*15), 10) | tounsigned((r[row+30][col] << W0*14), 10) | tounsigned((r[row+28][col] << W0*13), 10) | tounsigned((r[row+26][col] << W0*12), 10) | tounsigned((r[row+24][col] << W0*11), 10) | tounsigned((r[row+22][col] << W0*10), 10) | tounsigned((r[row+20][col] << W0*9), 10) | tounsigned((r[row+18][col] << W0*8), 10) | tounsigned((r[row+16][col] << W0*7), 10) | tounsigned((r[row+14][col] << W0*6), 10) | tounsigned((r[row+12][col] << W0*5), 10) | tounsigned((r[row+10][col] << W0*4), 10) | tounsigned((r[row+8][col] << W0*3), 10) | tounsigned((r[row+6][col] << W0*2), 10) | tounsigned((r[row+4][col] << W0*1), 10) | tounsigned((r[row][col]), 10))
				print bin(tounsigned((r[row+33][col] << W0*15), 10) | tounsigned((r[row+31][col] << W0*14), 10) | tounsigned((r[row+29][col] << W0*13), 10) | tounsigned((r[row+27][col] << W0*12), 10) | tounsigned((r[row+25][col] << W0*11), 10) | tounsigned((r[row+23][col] << W0*10), 10) | tounsigned((r[row+21][col] << W0*9), 10) | tounsigned((r[row+19][col] << W0*8), 10) | tounsigned((r[row+17][col] << W0*7), 10) | tounsigned((r[row+15][col] << W0*6), 10) | tounsigned((r[row+13][col] << W0*5), 10) | tounsigned((r[row+11][col] << W0*4), 10) | tounsigned((r[row+9][col] << W0*3), 10) | tounsigned((r[row+7][col] << W0*2), 10) | tounsigned((r[row+5][col] << W0*1), 10) | tounsigned((r[row+1][col]), 10))
				lft_s_i.next = tounsigned((r[row+31][col] << W0*15), 10) | tounsigned((r[row+29][col] << W0*14), 10) | tounsigned((r[row+27][col] << W0*13), 10) | tounsigned((r[row+25][col] << W0*12), 10) | tounsigned((r[row+23][col] << W0*11), 10) | tounsigned((r[row+21][col] << W0*10), 10) | tounsigned((r[row+19][col] << W0*9), 10) | tounsigned((r[row+17][col] << W0*8), 10) | tounsigned((r[row+15][col] << W0*7), 10) | tounsigned((r[row+13][col] << W0*6), 10) | tounsigned((r[row+11][col] << W0*5), 10) | tounsigned((r[row+9][col] << W0*4), 10) | tounsigned((r[row+7][col] << W0*3), 10) | tounsigned((r[row+5][col] << W0*2), 10) | tounsigned((r[row+3][col] << W0*1), 10) | tounsigned((r[row-1][col]),10)
				sa_s_i.next = tounsigned((r[row+32][col] << W0*15), 10) | tounsigned((r[row+30][col] << W0*14), 10) | tounsigned((r[row+28][col] << W0*13), 10) | tounsigned((r[row+26][col] << W0*12), 10) | tounsigned((r[row+24][col] << W0*11), 10) | tounsigned((r[row+22][col] << W0*10), 10) | tounsigned((r[row+20][col] << W0*9), 10) | tounsigned((r[row+18][col] << W0*8), 10) | tounsigned((r[row+16][col] << W0*7), 10) | tounsigned((r[row+14][col] << W0*6), 10) | tounsigned((r[row+12][col] << W0*5), 10) | tounsigned((r[row+10][col] << W0*4), 10) | tounsigned((r[row+8][col] << W0*3), 10) | tounsigned((r[row+6][col] << W0*2), 10) | tounsigned((r[row+4][col] << W0*1), 10) | tounsigned((r[row][col]), 10)
				rht_s_i.next = tounsigned((r[row+33][col] << W0*15), 10) | tounsigned((r[row+31][col] << W0*14), 10) | tounsigned((r[row+29][col] << W0*13), 10) | tounsigned((r[row+27][col] << W0*12), 10) | tounsigned((r[row+25][col] << W0*11), 10) | tounsigned((r[row+23][col] << W0*10), 10) | tounsigned((r[row+21][col] << W0*9), 10) | tounsigned((r[row+19][col] << W0*8), 10) | tounsigned((r[row+17][col] << W0*7), 10) | tounsigned((r[row+15][col] << W0*6), 10) | tounsigned((r[row+13][col] << W0*5), 10) | tounsigned((r[row+11][col] << W0*4), 10) | tounsigned((r[row+9][col] << W0*3), 10) | tounsigned((r[row+7][col] << W0*2), 10) | tounsigned((r[row+5][col] << W0*1), 10) | tounsigned((r[row+1][col]), 10)
				yield clk_fast.posedge
				'''
				y0.next = lft_s_i
				y1.next = sa_s_i
				y2.next = rht_s_i
				yield clk_fast.posedge
				'''
				#print( "%3d %d %d %s %s %s") % (now(), row, col, hex(lft_s_i), hex(sa_s_i), hex(rht_s_i))
				yield clk_fast.posedge
				combine_rdy_s.next = 1
				yield clk_fast.posedge

				left_s_i.next = left_com_x
				sam_s_i.next = sam_com_x
				right_s_i.next = right_com_x
				yield clk_fast.posedge
				#print( "%3d %d %d %s %s %s") % (now(), row, col, hex(left_s_i), hex(sam_s_i), hex(right_s_i))
				combine_rdy_s.next = 0
				yield clk_fast.posedge
				addr_flgs.next = 0
				yield clk_fast.posedge
				for i in range(16):

					flgs_s_i.next = dout_flgs
					yield clk_fast.posedge
					#print( "%3d %s") % (now(), hex(flgs_s_i))
					addr_flgs.next = addr_flgs + 1
					yield clk_fast.posedge
					update_s.next = 1
					yield clk_fast.posedge
					r[row_ind][col_ind] = res_out_x
					results.append(int(res_out_x))

					yield clk_fast.posedge

					yield clk_fast.posedge

					yield clk_fast.posedge


					#print ("%d %d %d %d %d saving even pass 1 res_out_x " ) % (now(), res_out_x, row_ind, col_ind, r[row_ind][col_ind])
					yield clk_fast.posedge

					if (row_ind == w - 2):
						row_ind.next = 2
						if (col_ind <= h - 1):
							col_ind.next = col_ind + 1
					else:
						row_ind.next = row_ind + 2

					yield clk_fast.posedge
					update_s.next = 0
					yield clk_fast.posedge
					update_s.next = 1
					yield clk_fast.posedge
					update_s.next = 0
					yield clk_fast.posedge
		row_ind.next = 1
		col_ind.next = 0
		yield clk_fast.posedge
		#print( "%3d %d %d ") % (now(), row_ind, col_ind  )

		for col in range(w):
			for row in range(1,h-33, 34):
				print bin(tounsigned((r[row+29][col] << W0*15), 10) | tounsigned((r[row+27][col] << W0*14), 10) | tounsigned((r[row+25][col] << W0*13), 10) | tounsigned((r[row+23][col] << W0*12), 10) | tounsigned((r[row+21][col] << W0*11), 10) | tounsigned((r[row+19][col] << W0*10), 10) | tounsigned((r[row+17][col] << W0*9), 10) | tounsigned((r[row+15][col] << W0*8), 10) | tounsigned((r[row+13][col] << W0*7), 10) | tounsigned((r[row+11][col] << W0*6), 10) | tounsigned((r[row+9][col] << W0*5), 10) | tounsigned((r[row+7][col] << W0*4), 10) | tounsigned((r[row+5][col] << W0*3), 10) | tounsigned((r[row+3][col] << W0*2), 10) | tounsigned((r[row+1][col] << W0*1), 10) | tounsigned((r[row-1][col]), 10 ))
				print bin(tounsigned((r[row+30][col] << W0*15), 10) | tounsigned((r[row+28][col] << W0*14), 10) | tounsigned((r[row+26][col] << W0*13), 10) | tounsigned((r[row+24][col] << W0*12), 10) | tounsigned((r[row+22][col] << W0*11), 10) | tounsigned((r[row+20][col] << W0*10), 10) | tounsigned((r[row+18][col] << W0*9), 10) | tounsigned((r[row+16][col] << W0*8), 10) | tounsigned((r[row+14][col] << W0*7), 10) | tounsigned((r[row+12][col] << W0*6), 10) | tounsigned((r[row+10][col] << W0*5), 10) | tounsigned((r[row+8][col] << W0*4), 10) | tounsigned((r[row+6][col] << W0*3), 10) | tounsigned((r[row+4][col] << W0*2), 10) | tounsigned((r[row+2][col] << W0*1), 10) | tounsigned((r[row][col]), 10 ))
				print bin(tounsigned((r[row+31][col] << W0*15), 10) | tounsigned((r[row+29][col] << W0*14), 10) | tounsigned((r[row+27][col] << W0*13), 10) | tounsigned((r[row+25][col] << W0*12), 10) | tounsigned((r[row+23][col] << W0*11), 10) | tounsigned((r[row+21][col] << W0*10), 10) | tounsigned((r[row+19][col] << W0*9), 10) | tounsigned((r[row+17][col] << W0*8), 10) | tounsigned((r[row+15][col] << W0*7), 10) | tounsigned((r[row+13][col] << W0*6), 10) | tounsigned((r[row+11][col] << W0*5), 10) | tounsigned((r[row+9][col] << W0*4), 10) | tounsigned((r[row+7][col] << W0*3), 10) | tounsigned((r[row+5][col] << W0*2), 10) | tounsigned((r[row+3][col] << W0*1), 10) | tounsigned((r[row+1][col]), 10 ))


				lft_s_i.next = tounsigned((r[row+29][col] << W0*15), 10) | tounsigned((r[row+27][col] << W0*14), 10) | tounsigned((r[row+25][col] << W0*13), 10) | tounsigned((r[row+23][col] << W0*12), 10) | tounsigned((r[row+21][col] << W0*11), 10) | tounsigned((r[row+19][col] << W0*10), 10) | tounsigned((r[row+17][col] << W0*9), 10) | tounsigned((r[row+15][col] << W0*8), 10) | tounsigned((r[row+13][col] << W0*7), 10) | tounsigned((r[row+11][col] << W0*6), 10) | tounsigned((r[row+9][col] << W0*5), 10) | tounsigned((r[row+7][col] << W0*4), 10) | tounsigned((r[row+5][col] << W0*3), 10) | tounsigned((r[row+3][col] << W0*2), 10) | tounsigned((r[row+1][col] << W0*1), 10) | tounsigned((r[row-1][col]), 10 )
				sa_s_i.next = tounsigned((r[row+30][col] << W0*15), 10) | tounsigned((r[row+28][col] << W0*14), 10) | tounsigned((r[row+26][col] << W0*13), 10) | tounsigned((r[row+24][col] << W0*12), 10) | tounsigned((r[row+22][col] << W0*11), 10) | tounsigned((r[row+20][col] << W0*10), 10) | tounsigned((r[row+18][col] << W0*9), 10) | tounsigned((r[row+16][col] << W0*8), 10) | tounsigned((r[row+14][col] << W0*7), 10) | tounsigned((r[row+12][col] << W0*6), 10) | tounsigned((r[row+10][col] << W0*5), 10) | tounsigned((r[row+8][col] << W0*4), 10) | tounsigned((r[row+6][col] << W0*3), 10) | tounsigned((r[row+4][col] << W0*2), 10) | tounsigned((r[row+2][col] << W0*1), 10) | tounsigned((r[row][col]), 10 )
				rht_s_i.next = tounsigned((r[row+31][col] << W0*15), 10) | tounsigned((r[row+29][col] << W0*14), 10) | tounsigned((r[row+27][col] << W0*13), 10) | tounsigned((r[row+25][col] << W0*12), 10) | tounsigned((r[row+23][col] << W0*11), 10) | tounsigned((r[row+21][col] << W0*10), 10) | tounsigned((r[row+19][col] << W0*9), 10) | tounsigned((r[row+17][col] << W0*8), 10) | tounsigned((r[row+15][col] << W0*7), 10) | tounsigned((r[row+13][col] << W0*6), 10) | tounsigned((r[row+11][col] << W0*5), 10) | tounsigned((r[row+9][col] << W0*4), 10) | tounsigned((r[row+7][col] << W0*3), 10) | tounsigned((r[row+5][col] << W0*2), 10) | tounsigned((r[row+3][col] << W0*1), 10) | tounsigned((r[row+1][col]), 10 )
				yield clk_fast.posedge
				'''
				y0.next = lft_s_i
				y1.next = sa_s_i
				y2.next = rht_s_i
				yield clk_fast.posedge
				'''
				#print( "%3d %d %d %s %s %s") % (now(), row, col, hex(lft_s_i), hex(sa_s_i), hex(rht_s_i))
				combine_rdy_s.next = 1
				yield clk_fast.posedge


				left_s_i.next = left_com_x
				sam_s_i.next = sam_com_x
				right_s_i.next = right_com_x
				yield clk_fast.posedge
				#print( "%3d %d %d %s %s %s") % (now(), row, col, hex(left_s_i), hex(sam_s_i), hex(right_s_i))
				combine_rdy_s.next = 0
				yield clk_fast.posedge
				addr_flgs.next = 16
				yield clk_fast.posedge
				for i in range(16):

					flgs_s_i.next = dout_flgs
					yield clk_fast.posedge

					addr_flgs.next = addr_flgs + 1
					yield clk_fast.posedge
					update_s.next = 1
					yield clk_fast.posedge
					r[row_ind][col_ind] = res_out_x
					results.append(int(res_out_x))
					yield clk_fast.posedge
					#print ("%d %d %d %d %d saving odd pass 1 res_out_x " ) % (now(), res_out_x, row_ind, col_ind, r[row_ind][col_ind])


					if (row_ind == w - 1):
						row_ind.next = 1
						if (col_ind <= h - 2 ):
							col_ind.next = col_ind + 1
					else:
						row_ind.next = row_ind + 2

					yield clk_fast.posedge
					update_s.next = 0
					yield clk_fast.posedge
					update_s.next = 1
					yield clk_fast.posedge
					update_s.next = 0
					yield clk_fast.posedge
		temp_bank = [[0]*w for i in range(h)]
		for row in range(w):
			for col in range(w):

				if row % 2 == 0:

					temp_bank[col][row/2] =  r[row][col]
				else:

					temp_bank[col][row/2 + h/2] =  r[row][col]

		for row in range(w):
			for col in range(h):
				r[row][col] = temp_bank[row][col]
 		raise StopSimulation
	return instances()
tb(clk_fast, res_out_x, left_s_i,sam_s_i, right_s_i, flgs_s_i,
noupdate_s, update_s, left_com_x, sam_com_x, right_com_x,
lft_s_i, sa_s_i, rht_s_i, a0, a1, a2, y0, y1, y2,
combine_rdy_s, nocombine_s, row_ind, col_ind,
W0=W0, LVL0=LVL0, W1=W1, LVL1=LVL1, W2=W2,
LVL2=LVL2, W3=W3, LVL3=LVL3)
tb_fsm = traceSignals(
tb, clk_fast, res_out_x, left_s_i,sam_s_i, right_s_i, flgs_s_i,
noupdate_s, update_s, left_com_x, sam_com_x, right_com_x,
lft_s_i, sa_s_i, rht_s_i, a0, a1, a2, y0, y1, y2,
combine_rdy_s, nocombine_s, row_ind, col_ind)

sim = Simulation(tb_fsm)
sim.run()

if (img.mode == "RGB"):
	rgb = []
	for row in range(len(r)):
		for col in range(len(r)):
			#rgb.append((r[row][col],g[row][col],b[row][col]))
			rgb.append((r[row][col]))



	for row in range(len(r)):
		for col in range(len(r)):
			pix[col,row] = rgb[col + row*len(r)]
else:

	seq_to_img(r, pix)
img.save("simulation.png")

print "writing results"
for i in range(len(results)):

	print(results[i])

