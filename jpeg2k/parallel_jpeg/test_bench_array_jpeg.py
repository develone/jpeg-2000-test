from myhdl import *
from flaten import m_flatten
from jpeg_constants import *
from rom import *
from array_jpeg import jp_process
from combine_sam import combine
#from sig2one import sig2one
from PIL import Image
toVHDL.numeric_ports = False
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
res_out_x = Signal(intbv(0, min= -(2**(W0)) ,max= (2**(W0))))

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

matrix_lf = [[Signal(intbv(0)[W0:]) for mcol in range(4)] for mrow in range(4)]
matrix_sa = [[Signal(intbv(0)[W0:]) for mcol in range(4)] for mrow in range(4)]
matrix_rt = [[Signal(intbv(0)[W0:]) for mcol in range(4)] for mrow in range(4)]
flat_lf = Signal(intbv(0)[LVL2*W2:])
flat_sa = Signal(intbv(0)[LVL2*W2:])
flat_rt = Signal(intbv(0)[LVL2*W2:])
x = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
z = Signal(intbv(0)[W0:])
mrow = Signal(intbv(0)[4:])
mcol = Signal(intbv(0)[4:])

def tb(clk_fast, res_out_x, left_s_i,sam_s_i, right_s_i, flgs_s_i,
noupdate_s, update_s, left_com_x, sam_com_x, right_com_x,
lft_s_i, sa_s_i, rht_s_i,combine_rdy_s, nocombine_s, row_ind,
col_ind,
matrix_lf, flat_lf, matrix_sa, flat_sa, matrix_rt, flat_rt, z, x, mrow, mcol,
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
	'''
	instance_sig2_lf = sig2one(lft_s_i, clk_fast, combinel_sig_s, Sinl_in0, Sinl_in1, Sinl_in2, Sinl_in3, Sinl_in4, Sinl_in5, Sinl_in6, Sinl_in7, Sinl_in8, Sinl_in9, Sinl_in10, Sinl_in11, Sinl_in12, Sinl_in13, Sinl_in14, Sinl_in15)
	instance_sig2_sa = sig2one(sa_s_i, clk_fast, combinesa_sig_s, Sinsa_in0, Sinsa_in1, Sinsa_in2, Sinsa_in3, Sinsa_in4, Sinsa_in5, Sinsa_in6, Sinsa_in7, Sinsa_in8, Sinsa_in9, Sinsa_in10, Sinsa_in11, Sinsa_in12, Sinsa_in13, Sinsa_in14, Sinsa_in15)
	instance_sig2_rh = sig2one(rht_s_i, clk_fast, combinert_sig_s, Sinrt_in0, Sinrt_in1, Sinrt_in2, Sinrt_in3, Sinrt_in4, Sinrt_in5, Sinrt_in6, Sinrt_in7, Sinrt_in8, Sinrt_in9, Sinrt_in10, Sinrt_in11, Sinrt_in12, Sinrt_in13, Sinrt_in14, Sinrt_in15)
	'''
	instance_mat_lf = m_flatten(matrix_lf, flat_lf)
	instance_mat_sa = m_flatten(matrix_sa, flat_sa)
	instance_mat_rt = m_flatten(matrix_rt, flat_rt)
	@always(delay(10))
	def clkgen():
		clk_fast.next = not clk_fast

	@instance
	def stimulus():

		for i in range(10):
			#print( "%3d ") % (now())
			row_ind.next = 2
			col_ind.next = 0
			#print( "%3d %d %d ") % (now(), row_ind, col_ind  )
			yield clk_fast.posedge
		for col in range(w):
			col_ind.next = col
			yield clk_fast.posedge
			for row in range(2,h-32, 32):
				'''mrow mcol  pass1 even lf
				   3 3    3 2      3 1    3 0       2 3       2 2       2 1         2 0      1 3         1 2         1 1       1 0          0 3       0 2       0 1       00
				(1 2 3) (3 4 5) (5 6 7) (7 8 9) (9 10 11) (11 12 13) (13 14 15) (15 16 17) (17 18 19) (19 20 21) (21 22 23) (23 24 25) (25 26 28) (27 28 29) (29 30 31) (31 32 33)'''
				for mmrow in range(3,-1,-1):
					mrow.next = mmrow
					yield clk_fast.posedge
					for mmcol in range(3,-1,-1):
						mcol.next = mmcol
						yield clk_fast.posedge
						if (mrow == 3 and mcol == 3):
							x.next = r[row-1][col]
						elif (mrow == 3 and mcol == 2):
							x.next = r[row+1][col]
						elif (mrow == 3 and mcol == 1):
							x.next = r[row+3][col]
						elif (mrow == 3 and mcol == 0):
							x.next = r[row+5][col]
						elif (mrow == 2 and mcol == 3):
							x.next = r[row+7][col]
						elif (mrow == 2 and mcol == 2):
							x.next = r[row+9][col]
						elif (mrow == 2 and mcol == 1):
							x.next = r[row+11][col]
						elif (mrow == 2 and mcol == 0):
							x.next = r[row+13][col]
						elif (mrow == 1 and mcol == 3):
							x.next = r[row+15][col]
						elif (mrow == 1 and mcol == 2):
							x.next = r[row+17][col]
						elif (mrow == 1 and mcol == 1):
							x.next = r[row+19][col]
						elif (mrow == 1 and mcol == 0):
							x.next = r[row+21][col]
						elif (mrow == 0 and mcol == 3):
							x.next = r[row+23][col]
						elif (mrow == 0 and mcol == 2):
							x.next = r[row+25][col]
						elif (mrow == 0 and mcol == 1):
							x.next = r[row+27][col]
						elif (mrow == 0 and mcol == 0):
							x.next = r[row+29][col]
						yield clk_fast.posedge
						print (" %d %s %d %d %d") % (now(),bin(x,W0), x, mrow, mcol)
						yield clk_fast.posedge
						z.next = x[W0:]
						yield clk_fast.posedge
						matrix_lf[mrow][mcol].next = z
						yield clk_fast.posedge
						#print (" %d %s") % (now(),bin(flat_lf,W0*LVL0))

				#raise StopSimulation

				lft_s_i.next = flat_lf
				yield clk_fast.posedge
				print ("left %d %s %s") % (now(), hex(flat_lf), hex(lft_s_i))
				yield clk_fast.posedge
				#combinel_sig_s.next = 0
				'''mrow mcol pass1 even sa
				   3 3    3 2      3 1    3 0       2 3       2 2       2 1         2 0      1 3         1 2         1 1       1 0          0 3       0 2       0 1       00
				(1 2 3) (3 4 5) (5 6 7) (7 8 9) (9 10 11) (11 12 13) (13 14 15) (15 16 17) (17 18 19) (19 20 21) (21 22 23) (23 24 25) (25 26 28) (27 28 29) (29 30 31) (31 32 33)'''
				for mmrow in range(3,-1,-1):
					mrow.next = mmrow
					yield clk_fast.posedge
					for mmcol in range(3,-1,-1):
						mcol.next = mmcol
						yield clk_fast.posedge
						if (mrow == 3 and mcol == 3):
							x.next = r[row][col]
						elif (mrow == 3 and mcol == 2):
							x.next = r[row+2][col]
						elif (mrow == 3 and mcol == 1):
							x.next = r[row+4][col]
						elif (mrow == 3 and mcol == 0):
							x.next = r[row+6][col]
						elif (mrow == 2 and mcol == 3):
							x.next = r[row+8][col]
						elif (mrow == 2 and mcol == 2):
							x.next = r[row+10][col]
						elif (mrow == 2 and mcol == 1):
							x.next = r[row+12][col]
						elif (mrow == 2 and mcol == 0):
							x.next = r[row+14][col]
						elif (mrow == 1 and mcol == 3):
							x.next = r[row+16][col]
						elif (mrow == 1 and mcol == 2):
							x.next = r[row+18][col]
						elif (mrow == 1 and mcol == 1):
							x.next = r[row+20][col]
						elif (mrow == 1 and mcol == 0):
							x.next = r[row+22][col]
						elif (mrow == 0 and mcol == 3):
							x.next = r[row+24][col]
						elif (mrow == 0 and mcol == 2):
							x.next = r[row+26][col]
						elif (mrow == 0 and mcol == 1):
							x.next = r[row+28][col]
						elif (mrow == 0 and mcol == 0):
							x.next = r[row+30][col]
						yield clk_fast.posedge
						print (" %d %s %d %d %d") % (now(),bin(x,W0), x, mrow, mcol)
						z.next = x[W0:]
						yield clk_fast.posedge
						matrix_sa[mrow][mcol].next = z
						yield clk_fast.posedge
						#print (" %d %s") % (now(),bin(flat_sa,W0*LVL0))

				sa_s_i.next = flat_sa
				yield clk_fast.posedge
				print ("sam  %d %s %s") % (now(), hex(flat_sa), hex(sa_s_i))
				#combinesa_sig_s.next = 0
				'''mrow mcol pass1 even rt
				   3 3    3 2      3 1    3 0       2 3       2 2       2 1         2 0      1 3         1 2         1 1       1 0          0 3       0 2       0 1       00
				(1 2 3) (3 4 5) (5 6 7) (7 8 9) (9 10 11) (11 12 13) (13 14 15) (15 16 17) (17 18 19) (19 20 21) (21 22 23) (23 24 25) (25 26 28) (27 28 29) (29 30 31) (31 32 33)'''
				for mmrow in range(3,-1,-1):
					mrow.next = mmrow
					yield clk_fast.posedge
					for mmcol in range(3,-1,-1):
						mcol.next = mmcol
						yield clk_fast.posedge
						if (mrow == 3 and mcol == 3):
							x.next = r[row+1][col]
						elif (mrow == 3 and mcol == 2):
							x.next = r[row+3][col]
						elif (mrow == 3 and mcol == 1):
							x.next = r[row+5][col]
						elif (mrow == 3 and mcol == 0):
							x.next = r[row+7][col]
						elif (mrow == 2 and mcol == 3):
							x.next = r[row+9][col]
						elif (mrow == 2 and mcol == 2):
							x.next = r[row+11][col]
						elif (mrow == 2 and mcol == 1):
							x.next = r[row+13][col]
						elif (mrow == 2 and mcol == 0):
							x.next = r[row+15][col]
						elif (mrow == 1 and mcol == 3):
							x.next = r[row+17][col]
						elif (mrow == 1 and mcol == 2):
							x.next = r[row+19][col]
						elif (mrow == 1 and mcol == 1):
							x.next = r[row+21][col]
						elif (mrow == 1 and mcol == 0):
							x.next = r[row+23][col]
						elif (mrow == 0 and mcol == 3):
							x.next = r[row+25][col]
						elif (mrow == 0 and mcol == 2):
							x.next = r[row+27][col]
						elif (mrow == 0 and mcol == 1):
							x.next = r[row+29][col]
						elif (mrow == 0 and mcol == 0):
							x.next = r[row+31][col]
						yield clk_fast.posedge
						print (" %d %s %d %d %d") % (now(),bin(x,W0), x, mrow, mcol)
						z.next = x[W0:]
						yield clk_fast.posedge
						matrix_rt[mrow][mcol].next = z
						yield clk_fast.posedge
						#print (" %d %s") % (now(),bin(flat_rt,W0*LVL0))

				rht_s_i.next = (flat_rt)
				yield clk_fast.posedge
				print ("right %d %s %s") % (now(), hex(flat_rt), hex(rht_s_i))
				#combinert_sig_s.next = 0
				yield clk_fast.posedge

				print( "left sam right %3d %d %d %s %s %s") % (now(), row, col, hex(lft_s_i), hex(sa_s_i), hex(rht_s_i))
				yield clk_fast.posedge

				combine_rdy_s.next = 1
				yield clk_fast.posedge

				left_s_i.next = left_com_x
				sam_s_i.next = sam_com_x
				right_s_i.next = right_com_x
				yield clk_fast.posedge
				print( "left sam right %3d %d %d %s %s %s") % (now(), row, col, hex(left_s_i), hex(sam_s_i), hex(right_s_i))
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
					print ("%d %d %d %d %d %d %d odd pass 1 res_out_x " ) % (now(), res_out_x, r[row_ind][col_ind], row_ind, col_ind, row, col)
					results.append(int(r[row_ind][col_ind]))
					if (row_ind == 224):
						row_ind.next = 2
						yield clk_fast.posedge

					else:
						row_ind.next = row_ind + 2
						yield clk_fast.posedge

					update_s.next = 0
					yield clk_fast.posedge
					update_s.next = 1
					yield clk_fast.posedge
					update_s.next = 0
					yield clk_fast.posedge

		#raise StopSimulation
		row_ind.next = 1
		#col_ind.next = 0
		yield clk_fast.posedge
		for col in range(w):
			col_ind.next = col
			yield clk_fast.posedge
			for row in range(1,h-33, 32):
				'''mrow mcol pass1 odd lf
				   3 3    3 2      3 1    3 0       2 3       2 2       2 1         2 0      1 3         1 2         1 1       1 0          0 3       0 2       0 1       00
				(0 1 2 ) (2 3 4 ) (4 5 6) (6 7 8) (8 9 10) (10 11 12) (12 13 14) (14 15 16) (16 17 18) (18 19 20) (20 21 22) (22 23 24) (24 25 26) (26 27 28) (28 29 30) (30 31 32)'''
				for mmrow in range(3,-1,-1):
					mrow.next = mmrow
					yield clk_fast.posedge
					for mmcol in range(3,-1,-1):
						mcol.next = mmcol
						yield clk_fast.posedge
						if (mrow == 3 and mcol == 3):
							x.next = r[row-1][col]
						elif (mrow == 3 and mcol == 2):
							x.next = r[row+1][col]
						elif (mrow == 3 and mcol == 1):
							x.next = r[row+3][col]
						elif (mrow == 3 and mcol == 0):
							x.next = r[row+5][col]
						elif (mrow == 2 and mcol == 3):
							x.next = r[row+7][col]
						elif (mrow == 2 and mcol == 2):
							x.next = r[row+9][col]
						elif (mrow == 2 and mcol == 1):
							x.next = r[row+11][col]
						elif (mrow == 2 and mcol == 0):
							x.next = r[row+13][col]
						elif (mrow == 1 and mcol == 3):
							x.next = r[row+15][col]
						elif (mrow == 1 and mcol == 2):
							x.next = r[row+17][col]
						elif (mrow == 1 and mcol == 1):
							x.next = r[row+19][col]
						elif (mrow == 1 and mcol == 0):
							x.next = r[row+21][col]
						elif (mrow == 0 and mcol == 3):
							x.next = r[row+23][col]
						elif (mrow == 0 and mcol == 2):
							x.next = r[row+25][col]
						elif (mrow == 0 and mcol == 1):
							x.next = r[row+27][col]
						elif (mrow == 0 and mcol == 0):
							x.next = r[row+29][col]
						yield clk_fast.posedge
						print (" %d %s %d %d %d") % (now(),bin(x,W0), x, mrow, mcol)
						z.next = x[W0:]
						yield clk_fast.posedge
						matrix_lf[mrow][mcol].next = z
						yield clk_fast.posedge
						#print (" %d %s") % (now(),bin(flat_lf,W0*LVL0))

				lft_s_i.next = flat_lf
				yield clk_fast.posedge
				print ("left %d %s %s") % (now(), hex(flat_lf), hex(lft_s_i))
				yield clk_fast.posedge
				#combinel_sig_s.next = 0
				'''mrow mcol pass1 odd sa
				   3 3    3 2      3 1    3 0       2 3       2 2       2 1         2 0      1 3         1 2         1 1       1 0          0 3       0 2       0 1       00
				(0 1 2 ) (2 3 4 ) (4 5 6) (6 7 8) (8 9 10) (10 11 12) (12 13 14) (14 15 16) (16 17 18) (18 19 20) (20 21 22) (22 23 24) (24 25 26) (26 27 28) (28 29 30) (30 31 32)'''
				for mmrow in range(3,-1,-1):
					mrow.next = mmrow
					yield clk_fast.posedge
					for mmcol in range(3,-1,-1):
						mcol.next = mmcol
						yield clk_fast.posedge
						if (mrow == 3 and mcol == 3):
							x.next = r[row][col]
							yield clk_fast.posedge
						elif (mrow == 3 and mcol == 2):
							x.next = r[row+2][col]
						elif (mrow == 3 and mcol == 1):
							x.next = r[row+4][col]
						elif (mrow == 3 and mcol == 0):
							x.next = r[row+6][col]
						elif (mrow == 2 and mcol == 3):
							x.next = r[row+8][col]
						elif (mrow == 2 and mcol == 2):
							x.next = r[row+10][col]
						elif (mrow == 2 and mcol == 1):
							x.next = r[row+12][col]
						elif (mrow == 2 and mcol == 0):
							x.next = r[row+14][col]
						elif (mrow == 1 and mcol == 3):
							x.next = r[row+16][col]
						elif (mrow == 1 and mcol == 2):
							x.next = r[row+18][col]
						elif (mrow == 1 and mcol == 1):
							x.next = r[row+20][col]
						elif (mrow == 1 and mcol == 0):
							x.next = r[row+22][col]
						elif (mrow == 0 and mcol == 3):
							x.next = r[row+24][col]
						elif (mrow == 0 and mcol == 2):
							x.next = r[row+26][col]
						elif (mrow == 0 and mcol == 1):
							x.next = r[row+28][col]
						elif (mrow == 0 and mcol == 0):
							x.next = r[row+30][col]
						yield clk_fast.posedge
						print (" %d %s %d %d %d") % (now(),bin(x,W0), x, mrow, mcol)
						z.next = x[W0:]
						yield clk_fast.posedge
						matrix_sa[mrow][mcol].next = z
						yield clk_fast.posedge
						#print (" %d %s") % (now(),bin(flat_lf,W0*LVL0))


				sa_s_i.next = flat_sa
				yield clk_fast.posedge
				print ("sam %d %s %s") % (now(), hex(flat_sa), hex(sa_s_i))
				#combinesa_sig_s.next = 0
				'''mrow mcol pass1 odd rt
				   3 3    3 2      3 1    3 0       2 3       2 2       2 1         2 0      1 3         1 2         1 1       1 0          0 3       0 2       0 1       00
				(0 1 2 ) (2 3 4 ) (4 5 6) (6 7 8) (8 9 10) (10 11 12) (12 13 14) (14 15 16) (16 17 18) (18 19 20) (20 21 22) (22 23 24) (24 25 26) (26 27 28) (28 29 30) (30 31 32)'''
				for mmrow in range(3,-1,-1):
					mrow.next = mmrow
					yield clk_fast.posedge
					for mmcol in range(3,-1,-1):
						mcol.next = mmcol
						yield clk_fast.posedge
						if (mrow == 3 and mcol == 3):
							x.next = r[row+1][col]
							yield clk_fast.posedge
						elif (mrow == 3 and mcol == 2):
							x.next = r[row+3][col]
						elif (mrow == 3 and mcol == 1):
							x.next = r[row+5][col]
						elif (mrow == 3 and mcol == 0):
							x.next = r[row+7][col]
						elif (mrow == 2 and mcol == 3):
							x.next = r[row+9][col]
						elif (mrow == 2 and mcol == 2):
							x.next = r[row+11][col]
						elif (mrow == 2 and mcol == 1):
							x.next = r[row+13][col]
						elif (mrow == 2 and mcol == 0):
							x.next = r[row+15][col]
						elif (mrow == 1 and mcol == 3):
							x.next = r[row+17][col]
						elif (mrow == 1 and mcol == 2):
							x.next = r[row+19][col]
						elif (mrow == 1 and mcol == 1):
							x.next = r[row+21][col]
						elif (mrow == 1 and mcol == 0):
							x.next = r[row+23][col]
						elif (mrow == 0 and mcol == 3):
							x.next = r[row+25][col]
						elif (mrow == 0 and mcol == 2):
							x.next = r[row+27][col]
						elif (mrow == 0 and mcol == 1):
							x.next = r[row+29][col]
						elif (mrow == 0 and mcol == 0):
							x.next = r[row+31][col]
						yield clk_fast.posedge
						print (" %d %s %d %d %d") % (now(),bin(x,W0), x, mrow, mcol)
						z.next = x[W0:]
						yield clk_fast.posedge
						matrix_rt[mrow][mcol].next = z
						yield clk_fast.posedge
						#print (" %d %s") % (now(),bin(flat_rt,W0*LVL0))


				rht_s_i.next = flat_rt
				yield clk_fast.posedge
				print ("right %d %s %s") % (now(), hex(flat_rt), hex(rht_s_i))


				print( "%3d %d %d %s %s %s") % (now(), row, col, hex(lft_s_i), hex(sa_s_i), hex(rht_s_i))
				yield clk_fast.posedge

				#print( "%3d %d %d %s %s %s") % (now(), row, col, hex(lft_s_i), hex(sa_s_i), hex(rht_s_i))
				combine_rdy_s.next = 1
				yield clk_fast.posedge


				left_s_i.next = left_com_x
				sam_s_i.next = sam_com_x
				right_s_i.next = right_com_x
				yield clk_fast.posedge
				print( "left sam right %3d %d %d %s %s %s") % (now(), row, col, hex(left_s_i), hex(sam_s_i), hex(right_s_i))
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
					print ("%d %d %d %d %d %d %d odd pass 1 res_out_x " ) % (now(), res_out_x, r[row_ind][col_ind], row_ind, col_ind, row, col)
					results.append(int(r[row_ind][col_ind]))
					yield clk_fast.posedge
					if (row_ind == w - 1):
						row_ind.next = 1
						yield clk_fast.posedge
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
		for mmrow in range(w):
			for mmcol in range(w):

				if mmrow % 2 == 0:

					temp_bank[mmcol][mrow/2] =  r[mmrow][mmcol]
				else:

					temp_bank[mmcol][mmrow/2 + h/2] =  r[mmrow][mmcol]

		#raise StopSimulation
		'''this is pass2'''

		raise StopSimulation

 	return instances()
tb(clk_fast, res_out_x, left_s_i,sam_s_i, right_s_i, flgs_s_i,
noupdate_s, update_s, left_com_x, sam_com_x, right_com_x,
lft_s_i, sa_s_i, rht_s_i, combine_rdy_s, nocombine_s, row_ind, col_ind,

matrix_lf, flat_lf, matrix_sa, flat_sa, matrix_rt, flat_rt, z, x, mrow, mcol,
W0=W0, LVL0=LVL0, W1=W1, LVL1=LVL1, W2=W2,
LVL2=LVL2, W3=W3, LVL3=LVL3)
tb_fsm = traceSignals(
tb, clk_fast, res_out_x, left_s_i,sam_s_i, right_s_i, flgs_s_i,
noupdate_s, update_s, left_com_x, sam_com_x, right_com_x,
lft_s_i, sa_s_i, rht_s_i, combine_rdy_s, nocombine_s, row_ind, col_ind,

matrix_lf, flat_lf, matrix_sa, flat_sa, matrix_rt, flat_rt, z, x, mrow, mcol)

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

