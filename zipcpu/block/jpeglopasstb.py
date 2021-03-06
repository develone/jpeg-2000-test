from myhdl import *
import argparse

W0 = 31
flgs = Signal(intbv(0)[3:])
lft = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
rht = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
sam = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
clock = Signal(bool(0))
upd = Signal(bool(0))
done = Signal(bool(0))
lift = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))

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
def iwt97(s, width, height):
    ''' Inverse CDF 5/3. '''


    # Interleave:
    temp_bank = [[0]*width for i in range(height)]
    for col in range(width/2):
        for row in range(height):

			temp_bank[col * 2][row] = s[row][col]
			temp_bank[col * 2 + 1][row] =  s[row][col + width/2]
    for row in range(width):
        for col in range(height):
            s[row][col] = temp_bank[row][col]


    for col in range(width): # Do the 1D transform on all cols:
        ''' Perform the inverse 1D transform. '''

        # Inverse update 2.
        for row in range(1, height-1, 2):

			s[row][col] = (s[row][col] - ((int(s[row-1][col]) + int(s[row+1][col]) + 2)>>2))

            #s[row][col] += a4 * (s[row-1][col] + s[row+1][col])
        #s[0][col] += 2 * a4 * s[1][col]

        # Inverse predict 2.
        for row in range(2, height, 2):

			s[row][col] = (s[row][col] + ((int(s[row-1][col])>>1) + (int(s[row+1][col])>>1)))
            #s[row][col] += a3 * (s[row-1][col] + s[row+1][col])
        #s[height-1][col] += 2 * a3 * s[height-2][col]


    return s
	
	
def cliparse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--build", default=False, action='store_true')
    parser.add_argument("--test", default=False, action='store_true')
    parser.add_argument("--convert", default=False, action='store_true')
    args = parser.parse_args()
    return args 

def dwt(flgs,upd,lft,sam,rht,lift,done,clock):
    @always(clock.posedge)
    def rtl ():
        if (upd == 1):
            done.next = 0
            if (flgs == 7):
               lift.next = sam.signed() - ((lft.signed() >> 1) + (rht.signed() >> 1))
            elif (flgs == 5):
               lift.next = sam.signed() + ((lft.signed() >> 1) + (rht.signed() >> 1))
            elif (flgs == 6):
               lift.next = sam.signed() + ((lft.signed() + rht.signed() + 2) >> 2 )
            elif (flgs == 4):
               lift.next = sam.signed() - ((lft.signed() + rht.signed() + 2) >> 2 )
        else:
            done.next = 1
    return rtl

def tb(flgs,upd,lft,sam,rht,lift,done,clock):
	fin = open("c2.bin", "rb")
	import struct
	inp = []

	idx = 0
	for i in range(65536):
		#print(struct.unpack('i', fin.read(4)))
		inp.append(struct.unpack('i', fin.read(4))[0])
		#print inp[i]

	#print x
	w = 8
	h = 8
	m = [[0 for xx in range(w)] for yy in range(h)]
	#print m
	
	for col in range(w):
		for row in range(h):
			m[row][col] = inp[idx]
			idx = idx + 1
		idx= idx + 248
	
	print "row col loops [row][col]"

	print "is this the way C stores in memory?"
	for row in range(h):
		for col in range(w):
			print m[row][col],
		print
	print
	"""
	print "row col loops [col][row]" 
	for row in range(h):
		for col in range(w):
			print m[col][row],
		print
	"""
	print "order in fwt97 which is fwt53"
	print "process down the cols top to bottom"
	print "process across the cols left to right"	
	print "col row loops [row][col] input data "

	for col in range(w):
		for row in range(h):
			print m[row][col],
		print
	print
	

	"""
	print "col row loops [col][row]"
	for col in range(w):
		for row in range(h):
			print m[col][row],
		print 	
	"""
	"""
	going down the col
	with col row loops goes across the 
	col's
	"""
	print
	#fwd dwt 
	for col in range(w):
		for row in range(2, h-2,2):
			#print row,col,m[row-1][col], m[row][col],m[row+1][col]
			m[row][col] = m[row][col] - ((m[row-1][col] + m[row+2][col])>>1)
			#print m[row][col]
	print "col row loops [row][col] hi pass"
	for col in range(w):
		for row in range(h):
			print m[row][col],
		print	
	for col in range(w):
		for row in range(1, h-2,2):
			#print row,col,m[row-1][col], m[row][col],m[row+1][col]
			m[row][col] = m[row][col] - ((m[row-1][col] + m[row+2][col]+2)>>2)
			#print m[row][col]
	
	print "col row loops [row][col] lo pass"
	for col in range(w):
		for row in range(h):
			print m[row][col],
		print
	m = de_interleave(m,w,h)
	print "col row loops [row][col] de_interleave"
	for col in range(w):
		for row in range(h):
			print m[row][col],
		print
	"""	
	for col in range(w):
		for row in range(2, h-2,2):
			#print row,col,m[row-1][col], m[row][col],m[row+1][col]
			m[row][col] = m[row][col] - ((m[row-1][col] + m[row+2][col])>>1)
			#print m[row][col]
	print "col row loops [row][col] hi pass"
	for col in range(w):
		for row in range(h):
			print m[row][col],
		print	
	for col in range(w):
		for row in range(1, h-2,2):
			#print row,col,m[row-1][col], m[row][col],m[row+1][col]
			m[row][col] = m[row][col] - ((m[row-1][col] + m[row+2][col]+2)>>2)
			#print m[row][col]
	
	print "col row loops [row][col] lo pass"
	for col in range(w):
		for row in range(h):
			print m[row][col],
		print
	m = de_interleave(m,w,h)
	print "col row loops [row][col] de_interleave"
	for col in range(w):
		for row in range(h):
			print m[row][col],
		print
	print "pass 1 2 de_interleave pass 1 2 de_interleave"

	
	for col in range(w):
		for row in range(h):
			print m[row][col],
		print
	
	m = iwt97(m,w,h)
	
	print "col row loops inv dwt"
	for col in range(w):
		for row in range(h):
			print m[row][col],
		print
	"""
	
	"""
	for i in range(row):
		for j in range(col):
			print m[i][j],
		print	
	for i in range(row-2,2):
		for j in range(col):
			#m[i+1][j] = m[i+1][j] - ((m[i-1][j] + m[i+2][j])>>1)
			m[i+1][j] = m[i+1][j] + ((m[i-1][j] + m[i+2][j] +2)>>2)
	for i in range(row):
		for j in range(col):
			print m[i][j],
		print	

	"""
	block = [ [0] * 10 ] * 8

	
 	instance_lift = dwt(flgs,upd,lft,sam,rht,lift,done,clock)
        
	@always(delay(10))
	def clkgen():
		clock.next = not clock
	idx = 0
	for col in range(w):
		for row in range(h):
			m[row][col] = inp[idx]
			idx = idx + 1
		idx= idx + 248

	print "Using RTL"
	print "fwd lift becomes the sample inv" 
	print "inv returns the sample of previous"
	print "order in fwt97 which is fwt53"
	print "process down the cols top to bottom"
	print "process across the cols left to right"	
	print "col row loops [row][col] input data "
	print
	for row in range(h):
		for col in range(w):
			print m[row][col],
		print
	print		
	for col in range(w):
		for row in range(h):
			print m[row][col],
		print
	print 
	print "order in fwt97 which is fwt53"
	print "process down the cols top to bottom"
	print "process across the cols left to right"	
	print "col row loops [row][col] input data "
	print "restored m"
	print "lo pass"
	idx = 0
	for col in range(w):
		for row in range(h):
			m[row][col] = inp[idx]
			idx = idx + 1
		idx= idx + 248

	
	
	@instance
	def stimulus():
		for row in range(8):
		
			lft.next = m[row][0]
			yield clock.posedge
			sam.next = m[row][1]
			yield clock.posedge
			rht.next = m[row][2]
			yield clock.posedge
			flgs.next = 6
			yield clock.posedge
			upd.next = 1
			yield clock.posedge
			upd.next = 0
			yield clock.posedge			
			m[row][1] = lift.next
			yield clock.posedge				
			print ('time %d left %d sam %d right %d flgs %d lift %d ' % (now(),  lft, sam, rht, flgs, lift))
		
			lft.next = m[row][0]
			yield clock.posedge
			sam.next = m[row][1]
			yield clock.posedge
			rht.next = m[row][2]
			yield clock.posedge
			flgs.next = 4
			yield clock.posedge
			upd.next = 1
			yield clock.posedge
			upd.next = 0
			yield clock.posedge			
			m[row][1] = lift.next	
			yield clock.posedge			
			print ('time %d left %d sam %d right %d flgs %d lift %d ' % (now(),  lft, sam, rht, flgs, lift))
		
	
			lft.next = m[row][2]
			yield clock.posedge
			sam.next = m[row][3]
			yield clock.posedge
			rht.next = m[row][4]
			yield clock.posedge
			flgs.next = 6
			yield clock.posedge
			upd.next = 1
			yield clock.posedge
			upd.next = 0
			yield clock.posedge			
			m[row][3] = lift.next
			yield clock.posedge				
			print ('time %d left %d sam %d right %d flgs %d lift %d ' % (now(),  lft, sam, rht, flgs, lift))

			lft.next = m[row][2]
			yield clock.posedge
			sam.next = m[row][3]
			yield clock.posedge
			rht.next = m[row][4]
			yield clock.posedge
			flgs.next = 4
			yield clock.posedge
			upd.next = 1
			yield clock.posedge
			upd.next = 0
			yield clock.posedge			
			m[row][3] = lift.next	
			yield clock.posedge			
			print ('time %d left %d sam %d right %d flgs %d lift %d ' % (now(),  lft, sam, rht, flgs, lift))
			lft.next = m[row][4]
			yield clock.posedge
			sam.next = m[row][5]
			yield clock.posedge
			rht.next = m[row][6]
			yield clock.posedge
			flgs.next = 6
			yield clock.posedge
			upd.next = 1
			yield clock.posedge			
			upd.next = 0
			yield clock.posedge
			m[row][5] = lift.next
			yield clock.posedge
			print ('time %d left %d sam %d right %d flgs %d lift %d ' % (now(),  lft, sam, rht, flgs, lift))

			lft.next = m[row][4]
			yield clock.posedge
			sam.next = m[row][5]
			yield clock.posedge
			rht.next = m[row][6]
			yield clock.posedge
			flgs.next = 4
			yield clock.posedge
			upd.next = 1
			yield clock.posedge
			upd.next = 0
			yield clock.posedge
			m[row][5] = lift.next
			yield clock.posedge
			print ('time %d left %d sam %d right %d flgs %d lift %d ' % (now(),  lft, sam, rht, flgs, lift))
   


		raise StopSimulation
		
	return instances()
	
def convert(args):
    toVerilog(dwt,flgs,upd,lft,sam,rht,lift,done,clock)
    #toVHDL(dwt_top,clock)
 
def main():
    args = cliparse()
    if args.test:
       tb_fsm = traceSignals(tb,flgs,upd,lft,sam,rht,lift,done,clock)
       sim = Simulation(tb_fsm)
       sim.run()
      
    if args.convert:
        convert(args)

if __name__ == '__main__':
    main()
