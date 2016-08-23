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
	fin = open("img.bin", "rb")
	import struct
	x = []

	idx = 0
	for i in range(65536):
		#print(struct.unpack('i', fin.read(4)))
		x.append(struct.unpack('i', fin.read(4))[0])

	#x = [x[i:256] for i in range(0, len(x), 256)]
	#print x
	row = 256
	col = 256
	m = [ [0] * col ] * row
	block = [ [0] * 10 ] * 8

	
	for row in range(256):
		for col in range(256):
			xx = x[idx]
			#print xx
			m[col][row] = xx
			idx = idx + 1
	
	#print m
	for row in range(8):
		print m[row][0:8]
	
		
	#symmetrical extension
	for row in range(8):
		block[row][0] = m[row][2]
		block[row][1] = m[row][1]
		
	#transfer m to block
 	for row in range(8):
		block[row][2:10]=m[row][0:8]
 
	for row in range(8):
		print block[row][0:10]
	w = 10
	h = 8
	for col in range(w):
		for row in range(1,h-1,2):
			print row, col, block[row-1][col],block[row][col],block[row+1][col]
			block[row][col] = block[row][col] - \
			((block[row-1][col] + block[row+1][col])>>1)
			print block[row][col]
			 
	for row in range(8):
		print block[row][0:10]
			
	instance_lift = dwt(flgs,upd,lft,sam,rht,lift,done,clock)

	@always(delay(10))
	def clkgen():
		clock.next = not clock
	"""
	for i in range(0, 6, 1):
		print x[i]
	"""
	@instance
	def stimulus():
		#2 1 0 
		lft.next = m[0][2]
		yield clock.posedge
		sam.next = m[0][1]
		yield clock.posedge
		rht.next = m[0][0]
		yield clock.posedge
		flgs.next = 7
		yield clock.posedge
		upd.next = 1				
		print ('time %d left %d sam %d right %d flgs %d lift %d ' % (now(),  lft, sam, rht, flgs, lift))
		# 1 2 3
		lft.next = m[0][1]
		yield clock.posedge
		sam.next = m[0][2]
		yield clock.posedge
		rht.next = m[0][3]
		yield clock.posedge
		flgs.next = 7
		yield clock.posedge
		upd.next = 1				
		print ('time %d left %d sam %d right %d flgs %d lift %d ' % (now(),  lft, sam, rht, flgs, lift))
		lft.next = m[0][0]
		yield clock.posedge
		sam.next = m[0][1]
		yield clock.posedge
		rht.next = m[0][2]
		yield clock.posedge
		flgs.next = 7
		yield clock.posedge
		upd.next = 1
		yield clock.posedge
		upd.next = 0
		yield clock.posedge
		print ('time %d left %d sam %d right %d flgs %d lift %d ' % (now(),  lft, sam, rht, flgs, lift))
		sam.next = lift
		yield clock.posedge
		flgs.next = 5
		yield clock.posedge
		upd.next = 1
		yield clock.posedge
		upd.next = 0
		yield clock.posedge 
		print ('time %d left %d sam %d right %d flgs %d lift %d ' % (now(),  lft, sam, rht, flgs, lift))
		yield clock.posedge
		lft.next = 164
		yield clock.posedge
		sam.next = 160
		yield clock.posedge
		rht.next = 170
		yield clock.posedge
		flgs.next = 6
		yield clock.posedge
		upd.next = 1
		yield clock.posedge
		upd.next = 0
		yield clock.posedge
		print ('time %d left %d sam %d right %d flgs %d lift %d ' % (now(),  lft, sam, rht, flgs, lift))
		sam.next = lift
		yield clock.posedge
		flgs.next = 4
		yield clock.posedge
		upd.next = 1
		yield clock.posedge
		upd.next = 0
		yield clock.posedge 
		print ('time %d left %d sam %d right %d flgs %d lift %d ' % (now(),  lft, sam, rht, flgs, lift))
		yield clock.posedge        
        
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
