from myhdl import *
from jpeg_constants import *
from rom import *
from array_jpeg import jp_process
from combine_sam import combine
from sig2one import sig2one
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

combine_rdy_s = Signal(bool(0))
nocombine_s = Signal(bool(0))
row_ind = Signal(intbv(0)[9:])
col_ind = Signal(intbv(0)[9:])

Sinl_in0 = Signal(intbv(0)[10:])
Sinl_in1 = Signal(intbv(0)[10:])
Sinl_in2 = Signal(intbv(0)[10:])
Sinl_in3 = Signal(intbv(0)[10:])
Sinl_in4 = Signal(intbv(0)[10:])
Sinl_in5 = Signal(intbv(0)[10:])
Sinl_in6 = Signal(intbv(0)[10:])
Sinl_in7 = Signal(intbv(0)[10:])
Sinl_in8 = Signal(intbv(0)[10:])
Sinl_in9 = Signal(intbv(0)[10:])
Sinl_in10 = Signal(intbv(0)[10:])
Sinl_in11 = Signal(intbv(0)[10:])
Sinl_in12 = Signal(intbv(0)[10:])
Sinl_in13 = Signal(intbv(0)[10:])
Sinl_in14 = Signal(intbv(0)[10:])
Sinl_in15 = Signal(intbv(0)[10:])
Sout_s = Signal(intbv(0)[160:])
combinel_sig_s = Signal(bool(0))

Sinsa_in0 = Signal(intbv(0)[10:])
Sinsa_in1 = Signal(intbv(0)[10:])
Sinsa_in2 = Signal(intbv(0)[10:])
Sinsa_in3 = Signal(intbv(0)[10:])
Sinsa_in4 = Signal(intbv(0)[10:])
Sinsa_in5 = Signal(intbv(0)[10:])
Sinsa_in6 = Signal(intbv(0)[10:])
Sinsa_in7 = Signal(intbv(0)[10:])
Sinsa_in8 = Signal(intbv(0)[10:])
Sinsa_in9 = Signal(intbv(0)[10:])
Sinsa_in10 = Signal(intbv(0)[10:])
Sinsa_in11 = Signal(intbv(0)[10:])
Sinsa_in12 = Signal(intbv(0)[10:])
Sinsa_in13 = Signal(intbv(0)[10:])
Sinsa_in14 = Signal(intbv(0)[10:])
Sinsa_in15 = Signal(intbv(0)[10:])
Sout_s = Signal(intbv(0)[160:])
combinesa_sig_s = Signal(bool(0))

Sinrt_in0 = Signal(intbv(0)[10:])
Sinrt_in1 = Signal(intbv(0)[10:])
Sinrt_in2 = Signal(intbv(0)[10:])
Sinrt_in3 = Signal(intbv(0)[10:])
Sinrt_in4 = Signal(intbv(0)[10:])
Sinrt_in5 = Signal(intbv(0)[10:])
Sinrt_in6 = Signal(intbv(0)[10:])
Sinrt_in7 = Signal(intbv(0)[10:])
Sinrt_in8 = Signal(intbv(0)[10:])
Sinrt_in9 = Signal(intbv(0)[10:])
Sinrt_in10 = Signal(intbv(0)[10:])
Sinrt_in11 = Signal(intbv(0)[10:])
Sinrt_in12 = Signal(intbv(0)[10:])
Sinrt_in13 = Signal(intbv(0)[10:])
Sinrt_in14 = Signal(intbv(0)[10:])
Sinrt_in15 = Signal(intbv(0)[10:])
Sout_s = Signal(intbv(0)[160:])
combinert_sig_s = Signal(bool(0))

def tb(clk_fast, res_out_x, left_s_i,sam_s_i, right_s_i, flgs_s_i,
noupdate_s, update_s, left_com_x, sam_com_x, right_com_x,
lft_s_i, sa_s_i, rht_s_i,combine_rdy_s, nocombine_s, row_ind,
col_ind, sig2one, Sout_s, combinel_sig_s, Sinl_in0, Sinl_in1, Sinl_in2, Sinl_in3, Sinl_in4,
Sinl_in5, Sinl_in6, Sinl_in7, Sinl_in8, Sinl_in9, Sinl_in10, Sinl_in11, Sinl_in12, Sinl_in13, Sinl_in14, Sinl_in15,
combinesa_sig_s, Sinsa_in0, Sinsa_in1, Sinsa_in2, Sinsa_in3, Sinsa_in4,
Sinsa_in5, Sinsa_in6, Sinsa_in7, Sinsa_in8, Sinsa_in9, Sinsa_in10, Sinsa_in11, Sinsa_in12, Sinsa_in13, Sinsa_in14, Sinsa_in15,
combinert_sig_s, Sinrt_in0, Sinrt_in1, Sinrt_in2, Sinrt_in3, Sinrt_in4,
Sinrt_in5, Sinrt_in6, Sinrt_in7, Sinrt_in8, Sinrt_in9, Sinrt_in10, Sinrt_in11, Sinrt_in12, Sinrt_in13, Sinrt_in14, Sinrt_in15,
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
	instance_sig2_lf = sig2one(lft_s_i, clk_fast, combinel_sig_s, Sinl_in0, Sinl_in1, Sinl_in2, Sinl_in3, Sinl_in4, Sinl_in5, Sinl_in6, Sinl_in7, Sinl_in8, Sinl_in9, Sinl_in10, Sinl_in11, Sinl_in12, Sinl_in13, Sinl_in14, Sinl_in15)
	instance_sig2_sa = sig2one(sa_s_i, clk_fast, combinesa_sig_s, Sinsa_in0, Sinsa_in1, Sinsa_in2, Sinsa_in3, Sinsa_in4, Sinsa_in5, Sinsa_in6, Sinsa_in7, Sinsa_in8, Sinsa_in9, Sinsa_in10, Sinsa_in11, Sinsa_in12, Sinsa_in13, Sinsa_in14, Sinsa_in15)
	instance_sig2_rh = sig2one(rht_s_i, clk_fast, combinert_sig_s, Sinrt_in0, Sinrt_in1, Sinrt_in2, Sinrt_in3, Sinrt_in4, Sinrt_in5, Sinrt_in6, Sinrt_in7, Sinrt_in8, Sinrt_in9, Sinrt_in10, Sinrt_in11, Sinrt_in12, Sinrt_in13, Sinrt_in14, Sinrt_in15)
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
				Sinl_in0.next = r[row-1][col]
				Sinl_in1.next = r[row+3][col]
				Sinl_in2.next = r[row+5][col]
				Sinl_in3.next = r[row+7][col]
				Sinl_in4.next = r[row+9][col]
				Sinl_in5.next = r[row+11][col]
				Sinl_in6.next = r[row+13][col]
				Sinl_in7.next = r[row+15][col]
				Sinl_in8.next = r[row+17][col]
				Sinl_in9.next = r[row+19][col]
				Sinl_in10.next = r[row+21][col]
				Sinl_in11.next = r[row+23][col]
				Sinl_in12.next = r[row+25][col]
				Sinl_in13.next = r[row+27][col]
				Sinl_in14.next = r[row+29][col]
				Sinl_in15.next = r[row+31][col]
				yield clk_fast.posedge
				combinel_sig_s.next = 1
				yield clk_fast.posedge

				lft_s_i.next = Sout_s
				yield clk_fast.posedge
				yield clk_fast.posedge
				print (" %d %s %s") % (now(), bin(Sout_s,160), bin(lft_s_i,160))
				yield clk_fast.posedge
				#combinel_sig_s.next = 0
				Sinsa_in0.next = r[row][col]
				Sinsa_in1.next = r[row+4][col]
				Sinsa_in2.next = r[row+6][col]
				Sinsa_in3.next = r[row+8][col]
				Sinsa_in4.next = r[row+10][col]
				Sinsa_in5.next = r[row+12][col]
				Sinsa_in6.next = r[row+14][col]
				Sinsa_in7.next = r[row+16][col]
				Sinsa_in8.next = r[row+18][col]
				Sinsa_in9.next = r[row+20][col]
				Sinsa_in10.next = r[row+22][col]
				Sinsa_in11.next = r[row+24][col]
				Sinsa_in12.next = r[row+26][col]
				Sinsa_in13.next = r[row+28][col]
				Sinsa_in14.next = r[row+30][col]
				Sinsa_in15.next = r[row+32][col]
				yield clk_fast.posedge
				combinesa_sig_s.next = 1
				yield clk_fast.posedge
				sa_s_i.next = (Sout_s)
				yield clk_fast.posedge
				print (" %d %s %s") % (now(), bin(Sout_s,160), bin(sa_s_i,160))
				#combinesa_sig_s.next = 0

				Sinrt_in0.next = r[row+1][col]
				Sinrt_in1.next = r[row+5][col]
				Sinrt_in2.next = r[row+7][col]
				Sinrt_in3.next = r[row+7][col]
				Sinrt_in4.next = r[row+11][col]
				Sinrt_in5.next = r[row+13][col]
				Sinrt_in6.next = r[row+15][col]
				Sinrt_in7.next = r[row+17][col]
				Sinrt_in8.next = r[row+19][col]
				Sinrt_in9.next = r[row+21][col]
				Sinrt_in10.next = r[row+23][col]
				Sinrt_in11.next = r[row+25][col]
				Sinrt_in12.next = r[row+27][col]
				Sinrt_in13.next = r[row+29][col]
				Sinrt_in14.next = r[row+31][col]
				Sinrt_in15.next = r[row+33][col]
				yield clk_fast.posedge
				combinert_sig_s.next = 1
				yield clk_fast.posedge
				rht_s_i.next = (Sout_s)
				yield clk_fast.posedge
				print (" %d %s %s") % (now(), bin(Sout_s,160), bin(rht_s_i,160))
				#combinert_sig_s.next = 0
				yield clk_fast.posedge

				print( "%3d %d %d %s %s %s") % (now(), row, col, hex(lft_s_i), hex(sa_s_i), hex(rht_s_i))
				yield clk_fast.posedge

				combine_rdy_s.next = 1
				yield clk_fast.posedge

				left_s_i.next = left_com_x
				sam_s_i.next = sam_com_x
				right_s_i.next = right_com_x
				yield clk_fast.posedge
				print( "%3d %d %d %s %s %s") % (now(), row, col, hex(left_s_i), hex(sam_s_i), hex(right_s_i))
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
				Sinl_in0.next = r[row-1][col]
				Sinl_in1.next = r[row+3][col]
				Sinl_in2.next = r[row+5][col]
				Sinl_in3.next = r[row+7][col]
				Sinl_in4.next = r[row+9][col]
				Sinl_in5.next = r[row+11][col]
				Sinl_in6.next = r[row+13][col]
				Sinl_in7.next = r[row+15][col]
				Sinl_in8.next = r[row+17][col]
				Sinl_in9.next = r[row+19][col]
				Sinl_in10.next = r[row+21][col]
				Sinl_in11.next = r[row+23][col]
				Sinl_in12.next = r[row+25][col]
				Sinl_in13.next = r[row+27][col]
				Sinl_in14.next = r[row+29][col]
				Sinl_in15.next = r[row+31][col]
				yield clk_fast.posedge
				combinel_sig_s.next = 1
				yield clk_fast.posedge

				lft_s_i.next = Sout_s
				yield clk_fast.posedge
				yield clk_fast.posedge
				print (" %d %s %s") % (now(), bin(Sout_s,160), bin(lft_s_i,160))
				yield clk_fast.posedge
				#combinel_sig_s.next = 0
				Sinsa_in0.next = r[row][col]
				Sinsa_in1.next = r[row+4][col]
				Sinsa_in2.next = r[row+6][col]
				Sinsa_in3.next = r[row+8][col]
				Sinsa_in4.next = r[row+10][col]
				Sinsa_in5.next = r[row+12][col]
				Sinsa_in6.next = r[row+14][col]
				Sinsa_in7.next = r[row+16][col]
				Sinsa_in8.next = r[row+18][col]
				Sinsa_in9.next = r[row+20][col]
				Sinsa_in10.next = r[row+22][col]
				Sinsa_in11.next = r[row+24][col]
				Sinsa_in12.next = r[row+26][col]
				Sinsa_in13.next = r[row+28][col]
				Sinsa_in14.next = r[row+30][col]
				Sinsa_in15.next = r[row+32][col]
				yield clk_fast.posedge
				combinesa_sig_s.next = 1
				yield clk_fast.posedge
				sa_s_i.next = (Sout_s)
				yield clk_fast.posedge
				print (" %d %s %s") % (now(), bin(Sout_s,160), bin(sa_s_i,160))
				#combinesa_sig_s.next = 0

				Sinrt_in0.next = r[row+1][col]
				Sinrt_in1.next = r[row+5][col]
				Sinrt_in2.next = r[row+7][col]
				Sinrt_in3.next = r[row+7][col]
				Sinrt_in4.next = r[row+11][col]
				Sinrt_in5.next = r[row+13][col]
				Sinrt_in6.next = r[row+15][col]
				Sinrt_in7.next = r[row+17][col]
				Sinrt_in8.next = r[row+19][col]
				Sinrt_in9.next = r[row+21][col]
				Sinrt_in10.next = r[row+23][col]
				Sinrt_in11.next = r[row+25][col]
				Sinrt_in12.next = r[row+27][col]
				Sinrt_in13.next = r[row+29][col]
				Sinrt_in14.next = r[row+31][col]
				Sinrt_in15.next = r[row+33][col]
				yield clk_fast.posedge
				combinert_sig_s.next = 1
				yield clk_fast.posedge
				rht_s_i.next = (Sout_s)
				yield clk_fast.posedge
				print (" %d %s %s") % (now(), bin(Sout_s,160), bin(rht_s_i,160))
				#combinert_sig_s.next = 0
				yield clk_fast.posedge

				print( "%3d %d %d %s %s %s") % (now(), row, col, hex(lft_s_i), hex(sa_s_i), hex(rht_s_i))
				yield clk_fast.posedge

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
				Sinl_in0.next = r[row-1][col]
				Sinl_in1.next = r[row+3][col]
				Sinl_in2.next = r[row+5][col]
				Sinl_in3.next = r[row+7][col]
				Sinl_in4.next = r[row+9][col]
				Sinl_in5.next = r[row+11][col]
				Sinl_in6.next = r[row+13][col]
				Sinl_in7.next = r[row+15][col]
				Sinl_in8.next = r[row+17][col]
				Sinl_in9.next = r[row+19][col]
				Sinl_in10.next = r[row+21][col]
				Sinl_in11.next = r[row+23][col]
				Sinl_in12.next = r[row+25][col]
				Sinl_in13.next = r[row+27][col]
				Sinl_in14.next = r[row+29][col]
				Sinl_in15.next = r[row+31][col]
				yield clk_fast.posedge
				combinel_sig_s.next = 1
				yield clk_fast.posedge

				lft_s_i.next = Sout_s
				yield clk_fast.posedge
				yield clk_fast.posedge
				print (" %d %s %s") % (now(), bin(Sout_s,160), bin(lft_s_i,160))
				yield clk_fast.posedge
				#combinel_sig_s.next = 0
				Sinsa_in0.next = r[row][col]
				Sinsa_in1.next = r[row+4][col]
				Sinsa_in2.next = r[row+6][col]
				Sinsa_in3.next = r[row+8][col]
				Sinsa_in4.next = r[row+10][col]
				Sinsa_in5.next = r[row+12][col]
				Sinsa_in6.next = r[row+14][col]
				Sinsa_in7.next = r[row+16][col]
				Sinsa_in8.next = r[row+18][col]
				Sinsa_in9.next = r[row+20][col]
				Sinsa_in10.next = r[row+22][col]
				Sinsa_in11.next = r[row+24][col]
				Sinsa_in12.next = r[row+26][col]
				Sinsa_in13.next = r[row+28][col]
				Sinsa_in14.next = r[row+30][col]
				Sinsa_in15.next = r[row+32][col]
				yield clk_fast.posedge
				combinesa_sig_s.next = 1
				yield clk_fast.posedge
				sa_s_i.next = (Sout_s)
				yield clk_fast.posedge
				print (" %d %s %s") % (now(), bin(Sout_s,160), bin(sa_s_i,160))
				#combinesa_sig_s.next = 0

				Sinrt_in0.next = r[row+1][col]
				Sinrt_in1.next = r[row+5][col]
				Sinrt_in2.next = r[row+7][col]
				Sinrt_in3.next = r[row+7][col]
				Sinrt_in4.next = r[row+11][col]
				Sinrt_in5.next = r[row+13][col]
				Sinrt_in6.next = r[row+15][col]
				Sinrt_in7.next = r[row+17][col]
				Sinrt_in8.next = r[row+19][col]
				Sinrt_in9.next = r[row+21][col]
				Sinrt_in10.next = r[row+23][col]
				Sinrt_in11.next = r[row+25][col]
				Sinrt_in12.next = r[row+27][col]
				Sinrt_in13.next = r[row+29][col]
				Sinrt_in14.next = r[row+31][col]
				Sinrt_in15.next = r[row+33][col]
				yield clk_fast.posedge
				combinert_sig_s.next = 1
				yield clk_fast.posedge
				rht_s_i.next = (Sout_s)
				yield clk_fast.posedge
				print (" %d %s %s") % (now(), bin(Sout_s,160), bin(rht_s_i,160))
				#combinert_sig_s.next = 0
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
				Sinl_in0.next = r[row-1][col]
				Sinl_in1.next = r[row+3][col]
				Sinl_in2.next = r[row+5][col]
				Sinl_in3.next = r[row+7][col]
				Sinl_in4.next = r[row+9][col]
				Sinl_in5.next = r[row+11][col]
				Sinl_in6.next = r[row+13][col]
				Sinl_in7.next = r[row+15][col]
				Sinl_in8.next = r[row+17][col]
				Sinl_in9.next = r[row+19][col]
				Sinl_in10.next = r[row+21][col]
				Sinl_in11.next = r[row+23][col]
				Sinl_in12.next = r[row+25][col]
				Sinl_in13.next = r[row+27][col]
				Sinl_in14.next = r[row+29][col]
				Sinl_in15.next = r[row+31][col]
				yield clk_fast.posedge
				combinel_sig_s.next = 1
				yield clk_fast.posedge

				lft_s_i.next = Sout_s
				yield clk_fast.posedge
				yield clk_fast.posedge
				print (" %d %s %s") % (now(), bin(Sout_s,160), bin(lft_s_i,160))
				yield clk_fast.posedge
				#combinel_sig_s.next = 0
				Sinsa_in0.next = r[row][col]
				Sinsa_in1.next = r[row+4][col]
				Sinsa_in2.next = r[row+6][col]
				Sinsa_in3.next = r[row+8][col]
				Sinsa_in4.next = r[row+10][col]
				Sinsa_in5.next = r[row+12][col]
				Sinsa_in6.next = r[row+14][col]
				Sinsa_in7.next = r[row+16][col]
				Sinsa_in8.next = r[row+18][col]
				Sinsa_in9.next = r[row+20][col]
				Sinsa_in10.next = r[row+22][col]
				Sinsa_in11.next = r[row+24][col]
				Sinsa_in12.next = r[row+26][col]
				Sinsa_in13.next = r[row+28][col]
				Sinsa_in14.next = r[row+30][col]
				Sinsa_in15.next = r[row+32][col]
				yield clk_fast.posedge
				combinesa_sig_s.next = 1
				yield clk_fast.posedge
				sa_s_i.next = (Sout_s)
				yield clk_fast.posedge
				print (" %d %s %s") % (now(), bin(Sout_s,160), bin(sa_s_i,160))
				#combinesa_sig_s.next = 0

				Sinrt_in0.next = r[row+1][col]
				Sinrt_in1.next = r[row+5][col]
				Sinrt_in2.next = r[row+7][col]
				Sinrt_in3.next = r[row+7][col]
				Sinrt_in4.next = r[row+11][col]
				Sinrt_in5.next = r[row+13][col]
				Sinrt_in6.next = r[row+15][col]
				Sinrt_in7.next = r[row+17][col]
				Sinrt_in8.next = r[row+19][col]
				Sinrt_in9.next = r[row+21][col]
				Sinrt_in10.next = r[row+23][col]
				Sinrt_in11.next = r[row+25][col]
				Sinrt_in12.next = r[row+27][col]
				Sinrt_in13.next = r[row+29][col]
				Sinrt_in14.next = r[row+31][col]
				Sinrt_in15.next = r[row+33][col]
				yield clk_fast.posedge
				combinert_sig_s.next = 1
				yield clk_fast.posedge
				rht_s_i.next = (Sout_s)
				yield clk_fast.posedge
				print (" %d %s %s") % (now(), bin(Sout_s,160), bin(rht_s_i,160))
				#combinert_sig_s.next = 0
				yield clk_fast.posedge

				print( "%3d %d %d %s %s %s") % (now(), row, col, hex(lft_s_i), hex(sa_s_i), hex(rht_s_i))
				yield clk_fast.posedge

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
lft_s_i, sa_s_i, rht_s_i, combine_rdy_s, nocombine_s, row_ind, col_ind,
sig2one, Sout_s, combinel_sig_s, Sinl_in0, Sinl_in1, Sinl_in2, Sinl_in3, Sinl_in4, Sinl_in5, Sinl_in6,
Sinl_in7, Sinl_in8, Sinl_in9, Sinl_in10, Sinl_in11, Sinl_in12, Sinl_in13, Sinl_in14, Sinl_in15,
combinesa_sig_s, Sinsa_in0, Sinsa_in1, Sinsa_in2, Sinsa_in3, Sinsa_in4,
Sinsa_in5, Sinsa_in6, Sinsa_in7, Sinsa_in8, Sinsa_in9, Sinsa_in10, Sinsa_in11, Sinsa_in12, Sinsa_in13, Sinsa_in14, Sinsa_in15,
combinert_sig_s, Sinrt_in0, Sinrt_in1, Sinrt_in2, Sinrt_in3, Sinrt_in4,
Sinrt_in5, Sinrt_in6, Sinrt_in7, Sinrt_in8, Sinrt_in9, Sinrt_in10, Sinrt_in11, Sinrt_in12, Sinrt_in13, Sinrt_in14, Sinrt_in15,
W0=W0, LVL0=LVL0, W1=W1, LVL1=LVL1, W2=W2,
LVL2=LVL2, W3=W3, LVL3=LVL3)
tb_fsm = traceSignals(
tb, clk_fast, res_out_x, left_s_i,sam_s_i, right_s_i, flgs_s_i,
noupdate_s, update_s, left_com_x, sam_com_x, right_com_x,
lft_s_i, sa_s_i, rht_s_i, combine_rdy_s, nocombine_s, row_ind, col_ind,
sig2one, Sout_s, combinel_sig_s, Sinl_in0, Sinl_in1, Sinl_in2, Sinl_in3, Sinl_in4, Sinl_in5, Sinl_in6,
Sinl_in7, Sinl_in8, Sinl_in9, Sinl_in10, Sinl_in11, Sinl_in12, Sinl_in13, Sinl_in14, Sinl_in15,
combinesa_sig_s, Sinsa_in0, Sinsa_in1, Sinsa_in2, Sinsa_in3, Sinsa_in4,
Sinsa_in5, Sinsa_in6, Sinsa_in7, Sinsa_in8, Sinsa_in9, Sinsa_in10, Sinsa_in11, Sinsa_in12, Sinsa_in13, Sinsa_in14, Sinsa_in15,
combinert_sig_s, Sinrt_in0, Sinrt_in1, Sinrt_in2, Sinrt_in3, Sinrt_in4,
Sinrt_in5, Sinrt_in6, Sinrt_in7, Sinrt_in8, Sinrt_in9, Sinrt_in10, Sinrt_in11, Sinrt_in12, Sinrt_in13, Sinrt_in14, Sinrt_in15,)

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

