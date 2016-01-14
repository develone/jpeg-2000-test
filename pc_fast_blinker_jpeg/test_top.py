from myhdl import *
import argparse
from jpeg import dwt
from signed2twoscomplement import signed2twoscomplement
from l2r import lift2res
from sh_reg import ShiftReg, toSig

WIDTH = 31
W0 = 9

clock = Signal(bool(0))
'''
Signals needed for sh_reg
'''
po0 = Signal(intbv(0)[WIDTH:])
si0 = Signal(bool(0))
fB0 = Signal(bool(0))
reset = Signal(bool(1))

po1 = Signal(intbv(0)[WIDTH:])
si1 = Signal(bool(0))
fB1 = Signal(bool(0))

po2 = Signal(intbv(0)[WIDTH:])
si2 = Signal(bool(0))
fB2 = Signal(bool(0))

po3 = Signal(intbv(0)[WIDTH:])
si3 = Signal(bool(0))
fB3 = Signal(bool(0))

po4 = Signal(intbv(0)[WIDTH:])
si4 = Signal(bool(0))
fB4 = Signal(bool(0))
reset = Signal(bool(1))

po5 = Signal(intbv(0)[WIDTH:])
si5 = Signal(bool(0))
fB5 = Signal(bool(0))

po6 = Signal(intbv(0)[WIDTH:])
si6 = Signal(bool(0))
fB6 = Signal(bool(0))

po7 = Signal(intbv(0)[WIDTH:])
si7 = Signal(bool(0))
fB7 = Signal(bool(0))

sig0 = Signal(intbv(0)[WIDTH:])
sig1 = Signal(intbv(0)[WIDTH:])
sig2 = Signal(intbv(0)[WIDTH:])
sig3 = Signal(intbv(0)[WIDTH:])
sig4 = Signal(intbv(0)[WIDTH:])
sig5 = Signal(intbv(0)[WIDTH:])
sig6 = Signal(intbv(0)[WIDTH:])
sig7 = Signal(intbv(0)[WIDTH:])

upd0 = Signal(bool(0))
upd1 = Signal(bool(0))
upd2 = Signal(bool(0))
upd3 = Signal(bool(0))
upd4 = Signal(bool(0))
upd5 = Signal(bool(0))
upd6 = Signal(bool(0))
upd7 = Signal(bool(0))
'''
Signals need to convert signed data 
to unsigned
'''
z0 = Signal(intbv(0)[W0:])
z1 = Signal(intbv(0)[W0:])
z2 = Signal(intbv(0)[W0:])
z3 = Signal(intbv(0)[W0:])
z4 = Signal(intbv(0)[W0:])
z5 = Signal(intbv(0)[W0:])
z6 = Signal(intbv(0)[W0:])
z7 = Signal(intbv(0)[W0:])
done0 = Signal(bool(0))
done1 = Signal(bool(0))
done2 = Signal(bool(0))
done3 = Signal(bool(0))
done4 = Signal(bool(0))
done5 = Signal(bool(0))
done6 = Signal(bool(0))
done7 = Signal(bool(0))
lift0 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
res0 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
res1 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
res2 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
res3 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
res4 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
res5 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
res6 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
res7 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))

flgs0 = Signal(intbv(0)[3:])
lft0 = Signal(intbv(0)[W0:])
rht0 = Signal(intbv(0)[W0:])
sam0 = Signal(intbv(0)[W0:])

flgs1 = Signal(intbv(0)[3:])
lft1 = Signal(intbv(0)[W0:])
rht1 = Signal(intbv(0)[W0:])
sam1 = Signal(intbv(0)[W0:])
lift1 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))

flgs2 = Signal(intbv(0)[3:])
lft2 = Signal(intbv(0)[W0:])
rht2 = Signal(intbv(0)[W0:])
sam2 = Signal(intbv(0)[W0:])
lift2 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))

flgs3 = Signal(intbv(0)[3:])
lft3 = Signal(intbv(0)[W0:])
rht3 = Signal(intbv(0)[W0:])
sam3 = Signal(intbv(0)[W0:])
lift3 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))

flgs4 = Signal(intbv(0)[3:])
lft4= Signal(intbv(0)[W0:])
rht4 = Signal(intbv(0)[W0:])
sam4 = Signal(intbv(0)[W0:])
lift4 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))

flgs5 = Signal(intbv(0)[3:])
lft5= Signal(intbv(0)[W0:])
rht5 = Signal(intbv(0)[W0:])
sam5 = Signal(intbv(0)[W0:])
lift5 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))

flgs6 = Signal(intbv(0)[3:])
lft6= Signal(intbv(0)[W0:])
rht6 = Signal(intbv(0)[W0:])
sam6 = Signal(intbv(0)[W0:])
lift6 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))

flgs7 = Signal(intbv(0)[3:])
lft7= Signal(intbv(0)[W0:])
rht7 = Signal(intbv(0)[W0:])
sam7 = Signal(intbv(0)[W0:])
lift7 = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))

def cliparse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--build", default=False, action='store_true')
    parser.add_argument("--test", default=False, action='store_true')
    parser.add_argument("--convert", default=False, action='store_true')
    args = parser.parse_args()
    return args 

		
def dwt_top(clock):
	instance_0 = dwt(flgs0, upd0, lft0, sam0, rht0, lift0, done0, clock)
	instance_1 = dwt(flgs1, upd1, lft1, sam1, rht1, lift1, done1, clock)
	instance_2 = dwt(flgs2, upd2, lft2, sam2, rht2, lift2, done2, clock)
	instance_3 = dwt(flgs3, upd3, lft3, sam3, rht3, lift3, done3, clock)
	instance_4 = dwt(flgs4, upd4, lft4, sam4, rht4, lift4, done4, clock)
	instance_5 = dwt(flgs5, upd5, lft5, sam5, rht5, lift5, done5, clock)
	instance_6 = dwt(flgs6, upd6, lft6, sam6, rht6, lift6, done6, clock)
	instance_7 = dwt(flgs7, upd7, lft7, sam7, rht7, lift7, done7, clock)
	
	instance_8 = lift2res(lift0,res0, lift1,res1, lift2,res2, lift3,res3, lift4,res4, lift5,res5,lift6,res6,lift7,res7)
        
        instance_9 = ShiftReg(clock, WIDTH, reset, fB0, si0, po0)
        instance_10 = toSig(clock, sig0,flgs0,lft0,sam0,rht0, upd0)
        instance_11 = ShiftReg(clock, WIDTH, reset, fB1, si1, po1)
        instance_12 = toSig(clock, sig1,flgs1,lft1,sam1,rht1, upd1)
        instance_13 = ShiftReg(clock, WIDTH, reset, fB2, si2, po2)
        instance_14 = toSig(clock, sig2,flgs2,lft2,sam2,rht2, upd2)
        instance_15 = ShiftReg(clock, WIDTH, reset, fB3, si3, po3)
        instance_16 = toSig(clock, sig3,flgs3,lft3,sam3,rht3, upd3)  
        instance_17 = ShiftReg(clock, WIDTH, reset, fB4, si4, po4)
        instance_18 = toSig(clock, sig4,flgs4,lft4,sam4,rht4, upd4)
        instance_19 = ShiftReg(clock, WIDTH, reset, fB5, si5, po5)
        instance_20 = toSig(clock, sig5,flgs5,lft5,sam5,rht5, upd5)
        instance_21 = ShiftReg(clock, WIDTH, reset, fB6, si6, po6)
        instance_22 = toSig(clock, sig6,flgs6,lft6,sam6,rht6, upd6)
        instance_23 = ShiftReg(clock, WIDTH, reset, fB7, si7, po7)
        instance_24 = toSig(clock, sig7,flgs7,lft7,sam7,rht7, upd7)  
 
	instance_25 = signed2twoscomplement(res0, z0)
	instance_26 = signed2twoscomplement(res1, z1)
	instance_27 = signed2twoscomplement(res2, z2)
	instance_28 = signed2twoscomplement(res3, z3)
	instance_29 = signed2twoscomplement(res4, z4)
	instance_30 = signed2twoscomplement(res5, z5)
	instance_31 = signed2twoscomplement(res6, z6)
	instance_32 = signed2twoscomplement(res7, z7)
	return instances()	

 
def tb(clock):
        from PIL import Image
        im = Image.open("../lena_256.png")
        pix = im.load()
        m = list(im.getdata())
        #print m.__sizeof__()
        m = [m[i:i+im.size[0]] for i in range(0, len(m), im.size[0])] 
        #print m
        print len(m[0]), len(m[1])

	@always(delay(10))
	def clkgen():
		clock.next = not clock
	instance_0 = dwt(flgs0, upd0, lft0, sam0, rht0, lift0, done0, clock)
	instance_1 = dwt(flgs1, upd1, lft1, sam1, rht1, lift1, done1, clock)
	instance_2 = dwt(flgs2, upd2, lft2, sam2, rht2, lift2, done2, clock)
	instance_3 = dwt(flgs3, upd3, lft3, sam3, rht3, lift3, done3, clock)
	instance_4 = dwt(flgs4, upd4, lft4, sam4, rht4, lift4, done4, clock)
	instance_5 = dwt(flgs5, upd5, lft5, sam5, rht5, lift5, done5, clock)
	instance_6 = dwt(flgs6, upd6, lft6, sam6, rht6, lift6, done6, clock)
	instance_7 = dwt(flgs7, upd7, lft7, sam7, rht7, lift7, done7, clock)
	instance_8 = lift2res(lift0,res0, lift1,res1, lift2,res2, lift3,res3, lift4,res4, lift5,res5,lift6,res6,lift7,res7)
        instance_9 = ShiftReg(clock, WIDTH, reset, fB0, si0, po0)
        instance_10 = toSig(clock, sig0,flgs0,lft0,sam0,rht0, upd0)
        instance_11 = ShiftReg(clock, WIDTH, reset, fB1, si1, po1)
        instance_12 = toSig(clock, sig1,flgs1,lft1,sam1,rht1, upd1)
        instance_13 = ShiftReg(clock, WIDTH, reset, fB2, si2, po2)
        instance_14 = toSig(clock, sig2,flgs2,lft2,sam2,rht2, upd2)
        instance_15 = ShiftReg(clock, WIDTH, reset, fB3, si3, po3)
        instance_16 = toSig(clock, sig3,flgs3,lft3,sam3,rht3, upd3)  
        instance_17 = ShiftReg(clock, WIDTH, reset, fB4, si4, po4)
        instance_18 = toSig(clock, sig4,flgs4,lft4,sam4,rht4, upd4)
        instance_19 = ShiftReg(clock, WIDTH, reset, fB5, si5, po5)
        instance_20 = toSig(clock, sig5,flgs5,lft5,sam5,rht5, upd5)
        instance_21 = ShiftReg(clock, WIDTH, reset, fB6, si6, po6)
        instance_22 = toSig(clock, sig6,flgs6,lft6,sam6,rht6, upd6)
        instance_23 = ShiftReg(clock, WIDTH, reset, fB7, si7, po7)
        instance_24 = toSig(clock, sig7,flgs7,lft7,sam7,rht7, upd7)  
 
	instance_25 = signed2twoscomplement(res0, z0)
	instance_26 = signed2twoscomplement(res1, z1)
	instance_27 = signed2twoscomplement(res2, z2)
	instance_28 = signed2twoscomplement(res3, z3)
	instance_29 = signed2twoscomplement(res4, z4)
	instance_30 = signed2twoscomplement(res5, z5)
	instance_31 = signed2twoscomplement(res6, z6)
	instance_32 = signed2twoscomplement(res7, z7)

	@instance
        def stimulus():
            reset.next = 1
            yield clock.posedge
            print ("reset %d ") % (reset)
            reset.next = 0
            yield clock.posedge
            print ("reset %d ") % (reset)
            reset.next = 1
            yield clock.posedge
            print ("reset %d ") % (reset)
            #************************************0
            fB0.next = 1
            yield clock.posedge
            #fB0.next = 0
            #yield clock.posedge
            si0.next = 1
            yield clock.posedge
            print ("update firstBit %s %d %d ") % (bin(po0,31),fB0,si0) 
            si0.next = 1
            yield clock.posedge
            print ("first flgs firstBit %s %d %d ") % (bin(po0,31),fB0,si0)
            si0.next = 1
            yield clock.posedge
            print ("2nd flg firstBit %s %d %d ") % (bin(po0,31),fB0,si0) 
            '''flgs'''
            si0.next = 1
            yield clock.posedge
            print ("3rd flgs %s %d ") % (bin(po0,31),si0)
 
 
 
            '''end of flgs'''

            ''' starting 27bits'''

            x = m[0][2+1]
            print ("Right %s %d") % (bin(x,9), x)
            for i in range(W0-1,0,-1):
                si0.next = ((x&(1<<i))!=0)
                yield clock.posedge
                print ("31 bits %s %d %d ") % (bin(po0,31),si0,i)
            si0.next = ((x&(1<<0))!=0)
            yield clock.posedge 
            print ("LSB rht %s %d %d ") % (bin(po0,31),si0,i-1)

            x = m[0][2]
            print ("Sam %s %d") % (bin(x,9), x)
            for i in range(W0-1,0,-1):
                si0.next = ((x&(1<<i))!=0)
                yield clock.posedge
                print ("31 bits %s %d %d ") % (bin(po0,31),si0,i)
            si0.next = ((x&(1<<0))!=0)
            yield clock.posedge 
            print ("LSB sam %s %d %d ") % (bin(po0,31),si0,i-1)

            x = m[0][2-1]
            print ("Left %s %d") % (bin(x,9), x)
            for i in range(W0-1,0,-1):
                si0.next = ((x&(1<<i))!=0)
                yield clock.posedge
                print ("31 bits %s %d %d ") % (bin(po0,31),si0,i)
            si0.next = ((x&(1<<0))!=0)
            yield clock.posedge 
            print ("LSB lft %s %d %d ") % (bin(po0,31),si0,i-1)
            yield clock.posedge  
            fB0.next = 0
            yield clock.posedge
 
            print ("fB0 %d ") % (fB0)
            

            

            
            sig0.next = po0
            yield clock.posedge

            for i in range(10):
                yield clock.posedge
            #************************************0
            sig4.next = po0
            yield clock.posedge
            for i in range(10):
                yield clock.posedge            
            #************************************4
            #************************************1             
            reset.next = 1
            yield clock.posedge
            print ("reset %d ") % (reset)
            reset.next = 0
            yield clock.posedge
            print ("reset %d ") % (reset)
            reset.next = 1
            yield clock.posedge
            print ("reset %d ") % (reset)

            fB1.next = 1
            yield clock.posedge
            #fB0.next = 0
            #yield clock.posedge
            si1.next = 1
            yield clock.posedge
            print ("update firstBit %s %d %d ") % (bin(po1,31),fB1,si1) 
            si1.next = 1
            yield clock.posedge
            print ("first flgs firstBit %s %d %d ") % (bin(po1,31),fB1,si1)
            si1.next = 1
            yield clock.posedge
            print ("2nd flg firstBit %s %d %d ") % (bin(po1,31),fB1,si1) 
            '''flgs'''
            si1.next = 1
            yield clock.posedge
            print ("3rd flgs %s %d ") % (bin(po1,31),si1)
 
 
 
            '''end of flgs'''

            ''' starting 27bits'''

            x = m[0][4+1]
            print ("Right %s %d") % (bin(x,9), x)
            for i in range(W0-1,0,-1):
                si1.next = ((x&(1<<i))!=0)
                yield clock.posedge
                print ("31 bits %s %d %d ") % (bin(po1,31),si1,i)
            si1.next = ((x&(1<<0))!=0)
            yield clock.posedge 
            print ("LSB rht %s %d %d ") % (bin(po1,31),si1,i-1)

            x = m[0][4]
            print ("Sam %s %d") % (bin(x,9), x)
            for i in range(W0-1,0,-1):
                si1.next = ((x&(1<<i))!=0)
                yield clock.posedge
                print ("31 bits %s %d %d ") % (bin(po1,31),si1,i)
            si1.next = ((x&(1<<0))!=0)
            yield clock.posedge 
            print ("LSB sam %s %d %d ") % (bin(po1,31),si1,i-1)

            x = m[0][4-1]
            print ("Left %s %d") % (bin(x,9), x)
            for i in range(W0-1,0,-1):
                si1.next = ((x&(1<<i))!=0)
                yield clock.posedge
                print ("31 bits %s %d %d ") % (bin(po1,31),si1,i)
            si1.next = ((x&(1<<0))!=0)
            yield clock.posedge 
            print ("LSB lft %s %d %d ") % (bin(po1,31),si1,i-1)
            yield clock.posedge  
            fB1.next = 0
            yield clock.posedge
 
            print ("fB1 %d ") % (fB1)
            
            sig1.next = po1
            yield clock.posedge
            for i in range(10):
                yield clock.posedge            
            #************************************1
            sig5.next = po1
            yield clock.posedge
            for i in range(10):
                yield clock.posedge 
            #************************************5 
            reset.next = 1
            yield clock.posedge
            print ("reset %d ") % (reset)
            reset.next = 0
            yield clock.posedge
            print ("reset %d ") % (reset)
            reset.next = 1
            yield clock.posedge
            print ("reset %d ") % (reset)

            fB2.next = 1
            yield clock.posedge
            #fB0.next = 0
            #yield clock.posedge
            si2.next = 1
            yield clock.posedge
            print ("update firstBit %s %d %d ") % (bin(po2,31),fB2,si2) 
            si2.next = 1
            yield clock.posedge
            print ("first flgs firstBit %s %d %d ") % (bin(po2,31),fB2,si2)
            si2.next = 1
            yield clock.posedge
            print ("2nd flg firstBit %s %d %d ") % (bin(po2,31),fB0,si0) 
            '''flgs'''
            si2.next = 1
            yield clock.posedge
            print ("3rd flgs %s %d ") % (bin(po2,31),si2)
 
 
 
            '''end of flgs'''

            ''' starting 27bits'''

            x = m[0][6+1]
            print ("Right %s %d") % (bin(x,9), x)
            for i in range(W0-1,0,-1):
                si2.next = ((x&(1<<i))!=0)
                yield clock.posedge
                print ("31 bits %s %d %d ") % (bin(po2,31),si2,i)
            si2.next = ((x&(1<<0))!=0)
            yield clock.posedge 
            print ("LSB rht %s %d %d ") % (bin(po2,31),si2,i-1)
            x = m[0][6]
            print ("Sam %s %d") % (bin(x,9), x)
            for i in range(W0-1,0,-1):
                si2.next = ((x&(1<<i))!=0)
                yield clock.posedge
                print ("31 bits %s %d %d ") % (bin(po2,31),si2,i)
            si2.next = ((x&(1<<0))!=0)
            yield clock.posedge 
            print ("LSB sam %s %d %d ") % (bin(po2,31),si2,i-1)

            x = m[0][4-1]
            print ("Left %s %d") % (bin(x,9), x)
            for i in range(W0-1,0,-1):
                si2.next = ((x&(1<<i))!=0)
                yield clock.posedge
                print ("31 bits %s %d %d ") % (bin(po2,31),si2,i)
            si2.next = ((x&(1<<0))!=0)
            yield clock.posedge 
            print ("LSB lft %s %d %d ") % (bin(po2,31),si2,i-1)
            yield clock.posedge  
            fB2.next = 0
            yield clock.posedge
 
            print ("fB2 %d ") % (fB2)
            sig2.next = po2
            yield clock.posedge
            for i in range(10):
                yield clock.posedge 
            #************************************2
            sig6.next = po2
            yield clock.posedge
            for i in range(10):
                yield clock.posedge 
            #************************************6
            reset.next = 1
            yield clock.posedge
            print ("reset %d ") % (reset)
            reset.next = 0
            yield clock.posedge
            print ("reset %d ") % (reset)
            reset.next = 1
            yield clock.posedge
            print ("reset %d ") % (reset)

            fB3.next = 1
            yield clock.posedge
            #fB0.next = 0
            #yield clock.posedge
            si3.next = 1
            yield clock.posedge
            print ("update firstBit %s %d %d ") % (bin(po3,31),fB3,si3) 
            si3.next = 1
            yield clock.posedge
            print ("first flgs firstBit %s %d %d ") % (bin(po3,31),fB3,si3)
            si3.next = 1
            yield clock.posedge
            print ("2nd flg firstBit %s %d %d ") % (bin(po3,31),fB0,si0) 
            '''flgs'''
            si3.next = 1
            yield clock.posedge
            print ("3rd flgs %s %d ") % (bin(po3,31),si3)
 
 
 
            '''end of flgs'''

            ''' starting 27bits'''

            x = m[0][8+1]
            print ("Right %s %d") % (bin(x,9), x)
            for i in range(W0-1,0,-1):
                si3.next = ((x&(1<<i))!=0)
                yield clock.posedge
                print ("31 bits %s %d %d ") % (bin(po3,31),si3,i)
            si3.next = ((x&(1<<0))!=0)
            yield clock.posedge 
            print ("LSB rht %s %d %d ") % (bin(po3,31),si3,i-1)
            x = m[0][8]
            print ("Sam %s %d") % (bin(x,9), x)
            for i in range(W0-1,0,-1):
                si3.next = ((x&(1<<i))!=0)
                yield clock.posedge
                print ("31 bits %s %d %d ") % (bin(po3,31),si3,i)
            si3.next = ((x&(1<<0))!=0)
            yield clock.posedge 
            print ("LSB sam %s %d %d ") % (bin(po3,31),si3,i-1)

            x = m[0][8-1]
            print ("Left %s %d") % (bin(x,9), x)
            for i in range(W0-1,0,-1):
                si3.next = ((x&(1<<i))!=0)
                yield clock.posedge
                print ("31 bits %s %d %d ") % (bin(po3,31),si3,i)
            si3.next = ((x&(1<<0))!=0)
            yield clock.posedge 
            print ("LSB lft %s %d %d ") % (bin(po3,31),si3,i-1)
            yield clock.posedge  
            fB3.next = 0
            yield clock.posedge
 
            print ("fB3 %d ") % (fB3)            

            
            sig3.next = po3
            yield clock.posedge

            for i in range(10):
                yield clock.posedge
            #************************************3 
            sig7.next = po3
            yield clock.posedge
            for i in range(10):
                yield clock.posedge 
            #************************************7

            for row in range(2,10,2):
                print row-1, row, row+1 
                print m[0][row-1], m[0][row], m[0][row+1]
                print ("%s %s %s") % (bin(m[0][row-1],9),bin(m[0][row],9),bin(m[0][row+1],9))
            
            raise StopSimulation	
	return instances()
 
def convert(args):
    toVerilog(dwt_top,clock)
    #toVHDL(dwt_top,clock)
 
def main():
    args = cliparse()
    if args.test:
       tb_fsm = traceSignals(tb, clock)
       sim = Simulation(tb_fsm)
       sim.run()  
    if args.convert:
        convert(args)

if __name__ == '__main__':
    main()
