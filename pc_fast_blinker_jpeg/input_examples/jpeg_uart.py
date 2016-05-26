from rhea.utils import CommandPacket
from rhea.utils.command_packet import PACKET_LENGTH
import binascii
import serial
from PIL import Image
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
def get_results(last_set):
	#print 'last_set in get results',last_set
        if (last_set == 15):
           end = 25
        else:
           end = 26
	v = 0
	for r in range(16,end,1):
	    #print 'results_addr',addr[r]
	    pkt = CommandPacket(False, address=addr[r], vals=[v])
            wr2file(pkt,file_out1)

def wr2file(pkt,fout):
	
    ml = []
    ml_hex = []
    for bb in pkt.rawbytes:
	    ml.append(bb)
	    ml_hex.append(hex(bb))
    #print ml_hex
    ba = bytearray(ml)
    if(fout == file_out):
        file_out.write(ba)
        
        ser.write(ba)
        reply = ser.read(12)
        x = binascii.b2a_hex(reply)
        #print 'reply',x
    else:
        file_out1.write(ba)
        ser.write(ba)
        reply = ser.read(12)
        x = binascii.b2a_hex(reply)
        ser.write(ba)
        reply = ser.read(8)
        x = binascii.b2a_hex(reply)
        #print 'reply',x
        reply = ser.read(2)
        x = binascii.b2a_hex(reply)
        print 'reply',x
        reply = ser.read(2)
        x = binascii.b2a_hex(reply)
        print 'reply',x
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
        	for row in range(ez[i],zzz,2):
        		flag = 7
        		v = lsr(row,col,m,flag)
        		#print addr[addr_index]
        		pkt = CommandPacket(False, address=addr[addr_index], vals=[v])
                        wr2file(pkt,file_out)
        		addr_index+=1
        		saved_row.append(row)
        		#print row, v, hex(v),addr_index 
        	#print saved_row
        	last_set = len(saved_row)  
                #print 'last_set',last_set
        	get_results(last_set)
        
        for i in range(8):
        	addr_index=0
        	saved_row = []
        	if (i<7):
        		zzz = oz[i] + 32
        	else:
        		zzz = oz[i] + 30	
        	for row in range(oz[i],zzz,2):
        		flag = 7
        		v = lsr(row,col,m,flag)
        		#print addr[addr_index]
        		pkt = CommandPacket(False, address=addr[addr_index], vals=[v])
                        wr2file(pkt,file_out)
        		addr_index+=1
        		saved_row.append(row)
        		#print row, v, hex(v),addr_index 
        	#print saved_row
        	last_set = len(saved_row)  
                #print 'last_set',last_set
        	get_results(last_set)
 

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
 
