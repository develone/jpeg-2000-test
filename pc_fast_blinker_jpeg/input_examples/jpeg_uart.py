from rhea.utils import CommandPacket
from rhea.utils.command_packet import PACKET_LENGTH
import binascii
import serial
from PIL import Image
def seq_to_img(m, pix):
    ''' Copy matrix m to pixel buffer pix.
    Assumes m has the same number of rows and cols as pix. '''
    for row in range(len(m)):
        for col in range(len(m[row])):
            pix[col,row] = m[row][col]

def de_interleave(m,h,w):
	# de-interleave
	temp_bank = [[0]*w for i in range(h)]
	for row in range(w):
		for col in range(h):
            # k1 and k2 scale the vals
            # simultaneously transpose the matrix when deinterleaving
			if row % 2 == 0:

				temp_bank[col][row//2] =  m[row][col]
			else:

				temp_bank[col][row//2 + h//2] =  m[row][col]
    # write temp_bank to s:
	for row in range(w):
		for col in range(h):
			m[row][col] = temp_bank[row][col]
	return m
'''reads image [row][col]'''
def rd_img(imgfn): 
    im = Image.open(imgfn)
    pix = im.load()
    m = list(im.getdata())
    #print m.__sizeof__()
    m = [m[i:i+im.size[0]] for i in range(0, len(m), im.size[0])]
    return im, m, pix
'''converts string '01fc' to -4'''
def convert_9bit(xx):
	y = int(xx,16)
	if (y > 255):
	   y = y - 512
	return y
''' '''
def get_results(last_set,row,col,sam):
	#print 'last_set in get results',last_set
	#print row,col
        if (last_set == 15):
           end = 25
        else:
           end = 26
	v = 0
	
	for r in range(16,end,1):
	    print 'results_addr',addr[r],row,col,sam
	    pkt = CommandPacket(False, address=addr[r], vals=[v])
            #wr2file(pkt,file_out1,row,col,r)
            ml = []
            for bb in pkt.rawbytes:
	            ml.append(bb)
            ba = bytearray(ml)
            x = binascii.b2a_hex(ba)
            print x
            if (r == 16 or r==17):
		ser.write(ba)
		reply = ser.read(12)
		ser.write(ba)
		reply = ser.read(12)
		x = binascii.b2a_hex(reply)
		print x
            if (r == 18):
                print sam[0],sam[1]
                ser.write(ba)
                reply = ser.read(12)
                ser.write(ba)
                reply = ser.read(8)
                x = binascii.b2a_hex(reply)
                reply = ser.read(2)
                x = binascii.b2a_hex(reply)
                m[sam[0]][col]=convert_9bit(x)
                print sam[0],m[sam[0]][col]
                print 'reply',x,convert_9bit(x) 
                #print 'reply',x
                reply = ser.read(2)
                x = binascii.b2a_hex(reply)
                m[sam[1]][col]=convert_9bit(x)
                print sam[1],m[sam[1]][col]
                print 'reply',x,convert_9bit(x)
            elif (r == 19):
                print sam[2],sam[3]
                ser.write(ba)
                reply = ser.read(12)
                ser.write(ba)
                reply = ser.read(8)
                x = binascii.b2a_hex(reply)
                reply = ser.read(2)
                x = binascii.b2a_hex(reply)
                m[sam[2]][col]=convert_9bit(x)
                print sam[2],m[sam[2]][col]                
                print 'reply',x,convert_9bit(x) 
                #print 'reply',x
                reply = ser.read(2)
                x = binascii.b2a_hex(reply)
                m[sam[3]][col]=convert_9bit(x)
                print sam[3],m[sam[3]][col]                
                print 'reply',x,convert_9bit(x)
            elif (r == 20):
                print sam[4],sam[5]
                ser.write(ba)
                reply = ser.read(12)
                ser.write(ba)
                reply = ser.read(8)
                x = binascii.b2a_hex(reply)
                reply = ser.read(2)
                x = binascii.b2a_hex(reply)
                m[sam[4]][col]=convert_9bit(x)
                print sam[4],m[sam[4]][col]                
                print 'reply',x,convert_9bit(x) 
                #print 'reply',x
                reply = ser.read(2)
                x = binascii.b2a_hex(reply)
                m[sam[5]][col]=convert_9bit(x)
                print sam[5],m[sam[5]][col]                
                print 'reply',x,convert_9bit(x)
            elif (r == 21):
                print sam[6],sam[7]
                ser.write(ba)
                reply = ser.read(12)
                ser.write(ba)
                reply = ser.read(8)
                x = binascii.b2a_hex(reply)
                reply = ser.read(2)
                x = binascii.b2a_hex(reply)
                m[sam[6]][col]=convert_9bit(x)
                print sam[6],m[sam[6]][col]                
                print 'reply',x,convert_9bit(x) 
                #print 'reply',x
                reply = ser.read(2)
                x = binascii.b2a_hex(reply)
                m[sam[7]][col]=convert_9bit(x)
                print sam[7],m[sam[7]][col]                
                print 'reply',x,convert_9bit(x)
            elif (r == 22):
                print sam[8],sam[9]
                ser.write(ba)
                reply = ser.read(12)
                ser.write(ba)
                reply = ser.read(8)
                x = binascii.b2a_hex(reply)
                reply = ser.read(2)
                x = binascii.b2a_hex(reply)
                m[sam[8]][col]=convert_9bit(x)
                print sam[8],m[sam[8]][col]                
                print 'reply',x,convert_9bit(x) 
                #print 'reply',x
                reply = ser.read(2)
                x = binascii.b2a_hex(reply)
                m[sam[9]][col]=convert_9bit(x)
                print sam[9],m[sam[9]][col]                
                print 'reply',x,convert_9bit(x)
            elif (r == 23):
                print sam[10],sam[11]
                ser.write(ba)
                reply = ser.read(12)
                ser.write(ba)
                reply = ser.read(8)
                x = binascii.b2a_hex(reply)
                reply = ser.read(2)
                x = binascii.b2a_hex(reply)
                m[sam[10]][col]=convert_9bit(x)
                print sam[10],m[sam[10]][col]                
                print 'reply',x,convert_9bit(x) 
                #print 'reply',x
                reply = ser.read(2)
                x = binascii.b2a_hex(reply)
                m[sam[11]][col]=convert_9bit(x)
                print sam[11],m[sam[11]][col]                
                print 'reply',x,convert_9bit(x)
            elif (r == 24):
                print sam[12],sam[13]
                ser.write(ba)
                reply = ser.read(12)
                ser.write(ba)
                reply = ser.read(8)
                x = binascii.b2a_hex(reply)
                reply = ser.read(2)
                x = binascii.b2a_hex(reply)
                m[sam[12]][col]=convert_9bit(x)
                print sam[12],m[sam[12]][col]                
                print 'reply',x,convert_9bit(x) 
                #print 'reply',x
                reply = ser.read(2)
                x = binascii.b2a_hex(reply)
                m[sam[13]][col]=convert_9bit(x)
                print sam[13],m[sam[13]][col]                
                print 'reply',x,convert_9bit(x)
            elif (r == 25):
                print sam[14],sam[15]
                ser.write(ba)
                reply = ser.read(12)
                ser.write(ba)
                reply = ser.read(8)
                x = binascii.b2a_hex(reply)
                reply = ser.read(2)
                x = binascii.b2a_hex(reply)
                m[sam[14]][col]=convert_9bit(x)
                print sam[14],m[sam[14]][col]                
                print 'reply',x,convert_9bit(x) 
                #print 'reply',x
                reply = ser.read(2)
                x = binascii.b2a_hex(reply)
                m[sam[15]][col]=convert_9bit(x)
                print sam[15],m[sam[15]][col]                
                print 'reply',x,convert_9bit(x)
        
	
       
            

def wr2file(pkt,fout,row,col):
    ml = []
    ml_hex = []
    for bb in pkt.rawbytes:
	    ml.append(bb)
	    ml_hex.append(hex(bb))
    print ml_hex
    ba = bytearray(ml)
    if(fout == file_out):
        file_out.write(ba)
        
        ser.write(ba)
        reply = ser.read(12)
        x = binascii.b2a_hex(reply)
        print 'reply',x
    else:
        print row,col
        
        file_out1.write(ba)
        ser.write(ba)
        reply = ser.read(12)
        x = binascii.b2a_hex(reply)
        ser.write(ba)
        reply = ser.read(8)
        x = binascii.b2a_hex(reply)
      
        reply = ser.read(2)
        x = binascii.b2a_hex(reply)
        print 'reply',convert_9bit(x) 
        #print 'reply',x
        reply = ser.read(2)
        x = binascii.b2a_hex(reply)
        print 'reply',convert_9bit(x)
        #print 'reply',x
        
        
	
       
			
'''row col m flag
['0xde', '0x2', '0x0', '0x0', '0x0', '0x2c', '0x4', '0xca', '0x38', '0xf0', '0x68', '0x3c']
0x38f0683c
'''	    
def lsr(row,col,m,flag):
    x0 = m[row-1][col] << 18
    x1 = m[row][col] << 9
    x2 = m[row+1][col]
    f = flag << 27
    '''
    if(flag==7):
	print 'lift',m[row][col] - ( (m[row-1][col] + m[row+1][col])>>1 )
    else:
	print 'lift',m[row][col] + ( (m[row-1][col] + m[row+1][col] + 2)>>2 )
    print ("%d %s %s %s" % (row, hex(m[row-1][col]), hex(m[row][col]), hex(m[row+1][col])))
    '''
    return (f+x0+x1+x2)
     
def jpeg():
    for cc in range(255):
        col = cc
        print 'col ',cc
         
        for i in range(8):
        	addr_index=0
        	saved_row = []
        	if (i<7):
        		zzz = ez[i] + 32
        	else:
        		zzz = ez[i] + 30
        	sam = []		
        	for row in range(ez[i],zzz,2):
			sam.append(row)
        		flag = 7
        		v = lsr(row,col,m,flag)
        		#print addr[addr_index]
        		
        		pkt = CommandPacket(False, address=addr[addr_index], vals=[v])
                        wr2file(pkt,file_out,row,col)
        		addr_index+=1
        		saved_row.append(row)
        		#print row,col, v, hex(v),addr_index 
        	#print saved_row
        	last_set = len(saved_row)  
                #print 'last_set',last_set
                print sam    
        	get_results(last_set,row,col,sam)
        
        for i in range(8):
        	addr_index=0
        	saved_row = []
        	if (i<7):
        		zzz = oz[i] + 32
        	else:
        		zzz = oz[i] + 30
        	sam = []		
        	for row in range(oz[i],zzz,2):
			sam.append(row)
        		flag = 6
        		v = lsr(row,col,m,flag)
        		#print addr[addr_index]
        		
        		pkt = CommandPacket(False, address=addr[addr_index], vals=[v])
                        wr2file(pkt,file_out,row,col)
        		addr_index+=1
        		saved_row.append(row)
        		#print row, v, hex(v),addr_index 
        	#print saved_row
        	last_set = len(saved_row)  
                #print 'last_set',last_set
                print sam    
        	get_results(last_set,row,col,sam)
 

addr = [0,4,8,12,16,20,24,28,32,36,40,44,48,52,56,60,64,68,72,76,80,84,88,92,96,100]
ez = [2,34,66,98,130,162,194,226]
oz = [1,33,65,97,129,161,193,225]

imgfn = "../../lena_256.png"
im, m, pix = rd_img(imgfn)
w, h = im.size
ser = serial.Serial ("/dev/ttyAMA0")    
ser.baudrate = 115200 
file_out = open("samples.bin","wb")
file_out1 = open("results.bin","wb")


last_set = 0        
reply = []
jpeg()
file_out.close()
file_out1.close()
de_interleave(m,h,w)
seq_to_img(m, pix) 
im.save("test1_256_fwt.png") 
