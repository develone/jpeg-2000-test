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
def interleave(s, width, height):
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
    
def prowcol (s,w,h):
	for row in range(h):
		for col in range(w):
			print s[row][col],
		print
	print
def pcolrow (s,w,h):
	for col in range(w):
		for row in range(h):
			print s[row][col],
		print
	print
			
def tb(flgs,upd,lft,sam,rht,lift,done,clock):
	fin = open("c2.bin", "rb")
	import struct
	inp = []

	idx = 0
	for i in range(65536):
		#print(struct.unpack('i', fin.read(4)))
		inp.append(struct.unpack('i', fin.read(4))[0])
		#print inp[i]

	w = 12
	h = 12
	bl = [[0 for xx in range(w)] for yy in range(h)]
	w = 8
	h = 8
	m = [[0 for xx in range(w)] for yy in range(h)]

	
	for col in range(w):
		for row in range(h):
			m[row][col] = inp[idx]
			idx = idx + 1
		idx= idx + 248
	"""
	copy m row 1 to row 0 of bl
	copy m row 1 to row 1 of bl
	symmetrical extension
	"""
	
	for col in range(6):
		for row in range(2):
			bl[row][col] = m[row+1][col]
			bl[row+1][col] = m[row+2][col]
	bl[0][6] = m[1][6]
	bl[1][6] = m[2][6]
	bl[0][7] = m[1][7]
	bl[1][7] = m[2][7]
	
	for col in range(8):
		for row in range(8):
			bl[row+2][col] = m[row][col]
	
	for col in range(6):
		for row in range(5,6,1):
			#bl[row+6][col] = m[row][col]
			bl[row+5][col] = m[row+1][col]
	
	bl[10][7] = m[5][7]
	bl[10][6] = m[5][6]
	
	for col in range(8):
		bl[11][col] = m[5][col]
			
	print "row col loops [row][col]"
	prowcol(m,8,8)
	w = 12
	h = 12
	print "row col loops [row][col]"
	prowcol(bl,w,h)	


	

	print "order in fwt97 "
	print "process down the cols top to bottom"
	print "process across the cols left to right"	
	print "col row loops [row][col] input data "

 
	pcolrow(bl,w,h)
	
	print "fwd dwt pass 1" 
	for col in range(w):
		for row in range(2, h-2,2):
			 
			bl[row][col] = bl[row][col] - ((bl[row-1][col] + bl[row+2][col])>>1)
			 
	print "col row loops [row][col] pass 1 hi pass"
	prowcol(bl,w,h)
 	
	for col in range(w):
		for row in range(1, h-1,2):
			 
			bl[row][col] = bl[row][col] - ((bl[row-1][col] + bl[row+2][col]+2)>>2)
			 
	
	print "col row loops [row][col] pass 1 lo pass"
	prowcol(bl,w,h)
 
	bl = de_interleave(bl,w,h)
	print "col row loops [row][col] pass1 de_interleave"
	prowcol(bl,w,h)
	
	print "fwd dwt pass 2"
	for col in range(w):
		for row in range(2, h-2,2):
			 
			bl[row][col] = bl[row][col] - ((bl[row-1][col] + bl[row+2][col])>>1)
			 
	print "col row loops [row][col] pass 2 hi pass"
	prowcol(bl,w,h)
 	
	for col in range(w):
		for row in range(1, h-1,2):
			 
			bl[row][col] = bl[row][col] - ((bl[row-1][col] + bl[row+2][col]+2)>>2)
			 
	
	print "col row loops [row][col] pass2 lo pass"
	prowcol(bl,w,h)
 
	bl = de_interleave(bl,w,h)
	print "col row loops [row][col] pass 2 de_interleave"
	prowcol(bl,w,h)
	
	bl = interleave(bl,w,h)
	print "col row loops [row][col] interleave fwd dwt"
	prowcol(bl,w,h)
 
	"""
 	instance_lift = dwt(flgs,upd,lft,sam,rht,lift,done,clock)
        
	@always(delay(10))
	def clkgen():
		clock.next = not clock
	idx = 0
	w = 8
	h = 8
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


	
	
	@instance
	def stimulus():
		for row in range(8):
		
			lft.next = m[row][1]
			yield clock.posedge
			sam.next = m[row][2]
			yield clock.posedge
			rht.next = m[row][3]
			yield clock.posedge
			flgs.next = 7
			yield clock.posedge
			upd.next = 1
			yield clock.posedge
			upd.next = 0
			yield clock.posedge			
			m[row][2] = lift.next
			yield clock.posedge				
			print ('time %d left %d sam %d right %d flgs %d lift %d ' % (now(),  lft, sam, rht, flgs, lift))
		
			lft.next = m[row][1]
			yield clock.posedge
			sam.next = m[row][2]
			yield clock.posedge
			rht.next = m[row][3]
			yield clock.posedge
			flgs.next = 5
			yield clock.posedge
			upd.next = 1
			yield clock.posedge
			upd.next = 0
			yield clock.posedge			
			m[row][2] = lift.next	
			yield clock.posedge			
			print ('time %d left %d sam %d right %d flgs %d lift %d ' % (now(),  lft, sam, rht, flgs, lift))
		
	
			lft.next = m[row][3]
			yield clock.posedge
			sam.next = m[row][4]
			yield clock.posedge
			rht.next = m[row][5]
			yield clock.posedge
			flgs.next = 7
			yield clock.posedge
			upd.next = 1
			yield clock.posedge
			upd.next = 0
			yield clock.posedge			
			m[row][4] = lift.next
			yield clock.posedge				
			print ('time %d left %d sam %d right %d flgs %d lift %d ' % (now(),  lft, sam, rht, flgs, lift))

			lft.next = m[row][3]
			yield clock.posedge
			sam.next = m[row][4]
			yield clock.posedge
			rht.next = m[row][5]
			yield clock.posedge
			flgs.next = 5
			yield clock.posedge
			upd.next = 1
			yield clock.posedge
			upd.next = 0
			yield clock.posedge			
			m[row][4] = lift.next	
			yield clock.posedge			
			print ('time %d left %d sam %d right %d flgs %d lift %d ' % (now(),  lft, sam, rht, flgs, lift))
			lft.next = m[row][5]
			yield clock.posedge
			sam.next = m[row][6]
			yield clock.posedge
			rht.next = m[row][7]
			yield clock.posedge
			flgs.next = 7
			yield clock.posedge
			upd.next = 1
			yield clock.posedge			
			upd.next = 0
			yield clock.posedge
			m[row][6] = lift.next
			yield clock.posedge
			print ('time %d left %d sam %d right %d flgs %d lift %d ' % (now(),  lft, sam, rht, flgs, lift))

			lft.next = m[row][5]
			yield clock.posedge
			sam.next = m[row][6]
			yield clock.posedge
			rht.next = m[row][7]
			yield clock.posedge
			flgs.next = 5
			yield clock.posedge
			upd.next = 1
			yield clock.posedge
			upd.next = 0
			yield clock.posedge
			m[row][6] = lift.next
			yield clock.posedge
			print ('time %d left %d sam %d right %d flgs %d lift %d ' % (now(),  lft, sam, rht, flgs, lift))
 


		raise StopSimulation
	"""	
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
