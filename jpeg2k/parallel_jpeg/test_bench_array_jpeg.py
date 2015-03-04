from myhdl import *
from jpeg_constants import *
from rom import *
from array_jpeg import jp_process
from combine_sam import combine
from PIL import Image
from tounsigned import tounsigned
img = Image.open("lena_rgb_512.png")
pix = img.load()
rgb = list(img.getdata())
w,h = img.size

r = []
g = []
b = []
"""get r g b from rgb"""
for n in range(len(rgb)):
    rr,gg,bb = rgb[n]
    r.append(rr)
    g.append(gg)
    b.append(bb)
"""convert to row col"""
r = [r[i:i+img.size[0]] for i in range(0, len(r), img.size[0])]
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

clk_fast = Signal(bool(0))
res_out_x = Signal(intbv(0, min= -(2**(W0-1)) ,max= (2**(W0-1))))
bits_in = Signal(intbv(0, min= -(2**(W0-1)) ,max= (2**(W0-1))))
v = Signal(intbv(0)[W0:])
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

def tb(clk_fast, res_out_x, left_s_i,sam_s_i, right_s_i, flgs_s_i,
noupdate_s, update_s, left_com_x, sam_com_x, right_com_x,
lft_s_i, sa_s_i, rht_s_i,
combine_rdy_s, nocombine_s, row_ind, col_ind, bits_in, v,
W0=W0, LVL0=LVL0, W1=W1, LVL1=LVL1, W2=W2,
LVL2=LVL2, W3=W3, LVL3=LVL3):

	def tosigned(v, w):
		''' return a signed representation of an 'unsigned' value '''
		if v >> (w-1) & 1:
			# high bit set -> negative
			return -(~v + 1)
		else:
			# positive
			return v
	instance_rom_flgs = rom_flgs(dout_flgs, addr_flgs, ROM_CONTENT)
	instance_combine = combine( left_com_x, sam_com_x, right_com_x,
lft_s_i, sa_s_i, rht_s_i, combine_rdy_s, nocombine_s,
W0=W0, LVL0=LVL0, W1=W1, LVL1=LVL1, W2=W2,
LVL2=LVL2, W3=W3, LVL3=LVL3)
	instance_tounsiged = tounsigned(bits_in, v, w=W0-1)
	instance_dut = jp_process( res_out_x, left_s_i,sam_s_i, right_s_i,
flgs_s_i, noupdate_s, update_s,  W0=W0, LVL0=LVL0, W1=W1, LVL1=LVL1,
W2=W2, LVL2=LVL2, W3=W3, LVL3=LVL3, SIMUL=SIMUL)
	@always(delay(10))
	def clkgen():
		clk_fast.next = not clk_fast

	@instance
	def stimulus():
		for i in range(10):
			#print( "%3d ") % (now())
			row_ind.next = 2
			col_ind.next = 0
			print( "%3d %d %d ") % (now(), row_ind, col_ind  )
			yield clk_fast.posedge

		for col in range(w):
			for row in range(2,h-32, 34):

				lft_s_i.next = (r[row+31][col] << W0*15) + (r[row+29][col] << W0*14) + (r[row+27][col] << W0*13) + (r[row+25][col] << W0*12) + (r[row+23][col] << W0*11) + (r[row+21][col] << W0*10) + (r[row+19][col] << W0*9) + (r[row+17][col] << W0*8) + (r[row+15][col] << W0*7) + (r[row+13][col] << W0*6) + (r[row+11][col] << W0*5) + (r[row+9][col] << W0*4) + (r[row+7][col] << W0*3) + (r[row+5][col] << W0*2) + (r[row+3][col] << W0*1) + (r[row-1][col] )
				sa_s_i.next = (r[row+32][col] << W0*15) + (r[row+30][col] << W0*14) + (r[row+28][col] << W0*13) + (r[row+26][col] << W0*12) + (r[row+24][col] << W0*11) + (r[row+22][col] << W0*10) + (r[row+20][col] << W0*9) + (r[row+18][col] << W0*8) + (r[row+16][col] << W0*7) + (r[row+14][col] << W0*6) + (r[row+12][col] << W0*5) + (r[row+10][col] << W0*4) + (r[row+8][col] << W0*3) + (r[row+6][col] << W0*2) + (r[row+4][col] << W0*1) + (r[row][col] )
				rht_s_i.next = (r[row+33][col] << W0*15) + (r[row+31][col] << W0*14) + (r[row+29][col] << W0*13) + (r[row+27][col] << W0*12) + (r[row+25][col] << W0*11) + (r[row+23][col] << W0*10) + (r[row+21][col] << W0*9) + (r[row+19][col] << W0*8) + (r[row+17][col] << W0*7) + (r[row+15][col] << W0*6) + (r[row+13][col] << W0*5) + (r[row+11][col] << W0*4) + (r[row+9][col] << W0*3) + (r[row+7][col] << W0*2) + (r[row+5][col] << W0*1) + (r[row+1][col] )
				print( "%3d %d %d %s %s %s") % (now(), row, col, hex(lft_s_i), hex(sa_s_i), hex(rht_s_i))
				yield clk_fast.posedge
				combine_rdy_s.next = 1
				yield clk_fast.posedge
				print( "%3d %d %d %s %s %s") % (now(), row, col, hex(left_s_i), hex(sam_s_i), hex(right_s_i))
				left_s_i.next = left_com_x
				sam_s_i.next = sam_com_x
				right_s_i.next = right_com_x
				yield clk_fast.posedge
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
					bits_in.next = res_out_x
					yield clk_fast.posedge
					r[row_ind][col_ind] = v
					#r[row_ind][col_ind] = tounsigned(res_out_x, W0-1)
					print ("%d %d %d %d %d saving even pass 1 res_out_x " ) % (now(), res_out_x, row_ind, col_ind, r[row_ind][col_ind])
					yield clk_fast.posedge

					if (row_ind == 510):
						row_ind.next = 2
						if (col_ind <= 511):
							col_ind.next = col_ind + 1
					else:
						row_ind.next = row_ind + 2

					#print ("%d %d %s" ) % (now(), res_out_x, hex(flgs_s_i))
					#print ("%d %d %d %d %s") % (now(), i, update_s, res_out_x, hex(flgs_s_i) )
					update_s.next = 0
					yield clk_fast.posedge
					update_s.next = 1
					yield clk_fast.posedge
					update_s.next = 0
					yield clk_fast.posedge
		row_ind.next = 1
		col_ind.next = 0
		print( "%3d %d %d ") % (now(), row_ind, col_ind  )

		for col in range(w):
			for row in range(1,h-33, 34):
				print ( "%3d %d %d ") % (now(), w, h  )
				print ("%3d %d %d %d %d %d %d %d %d  %d %d %d %d  %d %d %d %d  ") % (now(),r[row+29][col],r[row+27][col],r[row+25][col],r[row+23][col], r[row+21][col], r[row+19][col], r[row+17][col],r[row+15][col],r[row+13][col],r[row+11][col],r[row+9][col],r[row+7][col], r[row+5][col],r[row+3][col],r[row+1][col],r[row-1][col])
				print ("%3d %d %d %d %d %d %d %d %d  %d %d %d %d  %d %d %d %d  ") % (now(),r[row+30][col],r[row+28][col],r[row+26][col],r[row+24][col], r[row+22][col], r[row+20][col], r[row+18][col],r[row+16][col],r[row+14][col],r[row+12][col],r[row+10][col],r[row+8][col], r[row+6][col],r[row+4][col],r[row+2][col],r[row][col])
				print ("%3d %d %d %d %d %d %d %d %d  %d %d %d %d  %d %d %d %d  ") % (now(),r[row+31][col],r[row+29][col],r[row+27][col],r[row+25][col], r[row+23][col], r[row+21][col], r[row+19][col],r[row+17][col],r[row+15][col],r[row+13][col],r[row+11][col],r[row+9][col], r[row+7][col],r[row+5][col],r[row+3][col],r[row+1][col])
				lft_s_i.next = (r[row+29][col] << W0*15) + (r[row+27][col] << W0*14) + (r[row+25][col] << W0*13) +(r[row+23][col] << W0*12) + (r[row+21][col] << W0*11) + (r[row+19][col] << W0*10) + (r[row+17][col] << W0*9) + (r[row+15][col] << W0*8) + (r[row+13][col] << W0*7) + (r[row+11][col] << W0*6) + (r[row+9][col] << W0*5) + (r[row+7][col] << W0*4) + (r[row+5][col] << W0*3) + (r[row+3][col] << W0*2) + (r[row+1][col] << W0*1) + (r[row-1][col] )
				sa_s_i.next = (r[row+30][col] << W0*15) + (r[row+28][col] << W0*14) + (r[row+26][col] << W0*13) +(r[row+24][col] << W0*12) + (r[row+22][col] << W0*11) + (r[row+20][col] << W0*10) + (r[row+18][col] << W0*9) + (r[row+16][col] << W0*8) + (r[row+14][col] << W0*7) + (r[row+12][col] << W0*6) + (r[row+10][col] << W0*5) + (r[row+8][col] << W0*4) + (r[row+6][col] << W0*3) + (r[row+4][col] << W0*2) + (r[row+2][col] << W0*1) + (r[row][col] )
				#print ("%d %s") % (now(),hex(sa_s_i))
				rht_s_i.next = (r[row+31][col] << W0*15) + (r[row+29][col] << W0*14) + (r[row+27][col] << W0*13) +(r[row+25][col] << W0*12) + (r[row+23][col] << W0*11) + (r[row+21][col] << W0*10) + (r[row+19][col] << W0*9) + (r[row+17][col] << W0*8) + (r[row+15][col] << W0*7) + (r[row+13][col] << W0*6) + (r[row+11][col] << W0*5) + (r[row+9][col] << W0*4) + (r[row+7][col] << W0*3) + (r[row+5][col] << W0*2) + (r[row+3][col] << W0*1) + (r[row+1][col] )
				yield clk_fast.posedge
				combine_rdy_s.next = 1
				yield clk_fast.posedge
				print( "%3d %d %d %s %s %s") % (now(), row, col, hex(left_s_i), hex(sam_s_i), hex(right_s_i))
				left_s_i.next = left_com_x
				sam_s_i.next = sam_com_x
				right_s_i.next = right_com_x
				yield clk_fast.posedge
				combine_rdy_s.next = 0
				yield clk_fast.posedge
				addr_flgs.next = 16
				yield clk_fast.posedge
				for i in range(16):

					flgs_s_i.next = dout_flgs
					yield clk_fast.posedge
					#print( "%3d %s") % (now(), hex(flgs_s_i))
					addr_flgs.next = addr_flgs + 1
					yield clk_fast.posedge
					update_s.next = 1
					yield clk_fast.posedge
					bits_in.next = res_out_x
					yield clk_fast.posedge
					r[row_ind][col_ind] = v
					#row_s.next = row_s + 1
					#r[row_ind][col_ind] = tounsigned(res_out_x, W0-1)
					print ("%d %d %d %d %d saving odd pass 1 res_out_x " ) % (now(), res_out_x, row_ind, col_ind, r[row_ind][col_ind])
					yield clk_fast.posedge

					if (row_ind == 511):
						row_ind.next = 1
						if (col_ind <= 510):
							col_ind.next = col_ind + 1
					else:
						row_ind.next = row_ind + 2

					#print ("%d %d %s" ) % (now(), res_out_x, hex(flgs_s_i))
					#print ("%d %d %d %d %s") % (now(), i, update_s, res_out_x, hex(flgs_s_i) )
					update_s.next = 0
					yield clk_fast.posedge
					update_s.next = 1
					yield clk_fast.posedge
					update_s.next = 0
					yield clk_fast.posedge
		raise StopSimulation
	return instances()
tb(clk_fast, res_out_x, left_s_i,sam_s_i, right_s_i, flgs_s_i,
noupdate_s, update_s, left_com_x, sam_com_x, right_com_x,
lft_s_i, sa_s_i, rht_s_i,
combine_rdy_s, nocombine_s, row_ind, col_ind, bits_in, v,
W0=W0, LVL0=LVL0, W1=W1, LVL1=LVL1, W2=W2,
LVL2=LVL2, W3=W3, LVL3=LVL3)
tb_fsm = traceSignals(
tb, clk_fast, res_out_x, left_s_i,sam_s_i, right_s_i, flgs_s_i,
noupdate_s, update_s, left_com_x, sam_com_x, right_com_x,
lft_s_i, sa_s_i, rht_s_i,
combine_rdy_s, nocombine_s, row_ind, col_ind, bits_in, v)
#print "before fwd dwt", pix[0,0], rgb[0]
r = fwt97_2d(r, 1)
g = fwt97_2d(g, 1)
b = fwt97_2d(b, 1)
rgb = []
for row in range(len(r)):
    for col in range(len(r)):
        rgb.append((r[row][col],g[row][col],b[row][col]))

for row in range(len(r)):
        for col in range(len(r)):
            #pix[row,col] = rgb[col + row*128]
            pix[col,row] = rgb[col + row*len(r)]
#print "after fwd  dwt", pix[0,0], rgb[0]
#print r[1][0]
sim = Simulation(tb_fsm)
sim.run()
