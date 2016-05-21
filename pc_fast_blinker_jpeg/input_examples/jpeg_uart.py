from rhea.utils import CommandPacket
from rhea.utils.command_packet import PACKET_LENGTH
import binascii
import serial
from PIL import Image

def rd_img(imgfn): 
    im = Image.open(imgfn)
    pix = im.load()
    m = list(im.getdata())
    #print m.__sizeof__()
    m = [m[i:i+im.size[0]] for i in range(0, len(m), im.size[0])]
    return im, m, pix
imgfn = "../../lena_256.png"
im, m, pix = rd_img(imgfn)
w, h = im.size
'''set the baud rate to 115200 on RPi2B'''

ser = serial.Serial ("/dev/ttyAMA0")    
ser.baudrate = 115200
file_out = open("data_to_fpga.bin","wb")
#file_in = open("data_from_fpga.bin","wb") 
def wr2file(pkt):
    ml = []
    for bb in pkt.rawbytes:
	    ml.append(bb)
    print ml
    ba = bytearray(ml)
    file_out.write(ba) 

'''
first 16 addresses are the sending to lifting steps
next 2 address are you set upd on/off
next 8 addres returns the 16 lift steps
'''
addr = [0,4,8,12,16,20,24,28,32,36,40,44,48,52,56,60,64,68,72,76,80,84,88,92,96,100]
ez = [2,34,66,98,130,162,194,226]
oz = [1,33,65,97,129,161,193,225]
last_set = 0
def get_results(last_set):
	print 'last_set in get results',last_set
        if (last_set == 15):
           end = 25
        else:
           end = 26
	v = 0
	for r in range(16,end,1):
	    print 'results_addr',addr[r]
	    pkt = CommandPacket(False, address=addr[r], vals=[v])
            wr2file(pkt)

def lsr(row,col,m,flag):
    x0 = m[row-1][col] << 18
    x1 = m[row][col] << 9
    x2 = m[row+1][col]
    f = flag << 27
    
    print ("%d %s %s %s" % (row, hex(m[row-1][col]), hex(m[row][col]), hex(m[row+1][col])))
    return (f+x0+x1+x2) 
def jpeg():
    for cc in range(255):
        col = cc
        print 'col ',cc
        #file_out = open("data_to_fpga.bin","wb")
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
        		print addr[addr_index]
        		pkt = CommandPacket(False, address=addr[addr_index], vals=[v])
                        wr2file(pkt)
        		addr_index+=1
        		saved_row.append(row)
        		print row, v, hex(v),addr_index 
        	print saved_row
        	last_set = len(saved_row)  
                print 'last_set',last_set
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
        		print addr[addr_index]
        		pkt = CommandPacket(False, address=addr[addr_index], vals=[v])
                        wr2file(pkt)
        		addr_index+=1
        		saved_row.append(row)
        		print row, v, hex(v),addr_index 
        	print saved_row
        	last_set = len(saved_row)  
                print 'last_set',last_set
        	get_results(last_set)
        
reply = []
jpeg()
file_out.close()
'''
file_out = open("data_to_fpga.bin","rb")
file_in = open("data_from_fpga.bin","wb")

for j in range(105060):
	data = file_out.read(12)
	for i in range(12):
		
		#print (data[i])
		ser.write(data[i])
	reply = ser.read(12)
        #file_in.write(reply) 
	print "this is the reply", reply
'''
