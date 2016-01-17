from myhdl import *
import argparse
from jpeg import dwt
from signed2twoscomplement import signed2twoscomplement
from l2r import lift2res
from sh_reg import ShiftReg, toSig
from para2ser import para2ser
from jpeg_sig import *
WIDTH_OUT = 36
WIDTH = 31
W0 = 9

clock = Signal(bool(0))
 
 

pp0 = Signal(intbv(0)[WIDTH_OUT:])
ld = Signal(bool(0)) 
ss0 = Signal(bool(0))
def cliparse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--build", default=False, action='store_true')
    parser.add_argument("--test", default=False, action='store_true')
    parser.add_argument("--convert", default=False, action='store_true')
    args = parser.parse_args()
    return args 

		
def dwt_top(clock,si0,fB0,si1,fB1,si2,fB2,si3,fB3,reset,pp0,ss0,ld):
	instance_0 = dwt(flgs0, upd0, lft0, sam0, rht0, lift0, done0, clock)
	instance_1 = dwt(flgs1, upd1, lft1, sam1, rht1, lift1, done1, clock)
	instance_2 = dwt(flgs2, upd2, lft2, sam2, rht2, lift2, done2, clock)
	instance_3 = dwt(flgs3, upd3, lft3, sam3, rht3, lift3, done3, clock)
	instance_4 = dwt(flgs4, upd4, lft4, sam4, rht4, lift4, done4, clock)
	instance_5 = dwt(flgs5, upd5, lft5, sam5, rht5, lift5, done5, clock)
	instance_6 = dwt(flgs6, upd6, lft6, sam6, rht6, lift6, done6, clock)
	instance_7 = dwt(flgs7, upd7, lft7, sam7, rht7, lift7, done7, clock)
	instance_8 = dwt(flgs8, upd8, lft8, sam8, rht8, lift8, done8, clock)
	instance_9 = dwt(flgs9, upd9, lft9, sam9, rht9, lift9, done9, clock)
	instance_10 = dwt(flgs10, upd10, lft10, sam10, rht10, lift10, done10, clock)
	instance_11 = dwt(flgs11, upd11, lft11, sam11, rht11, lift11, done11, clock)
	instance_12 = dwt(flgs12, upd12, lft12, sam12, rht12, lift12, done12, clock)
	instance_13 = dwt(flgs13, upd13, lft13, sam13, rht13, lift13, done13, clock)
	instance_14 = dwt(flgs14, upd14, lft14, sam14, rht14, lift14, done14, clock)
	instance_15 = dwt(flgs15, upd15, lft15, sam15, rht15, lift15, done15, clock)	
	instance_16 = lift2res(lift0,res0, lift1,res1, lift2,res2, lift3,res3, lift4,res4, lift5,res5,lift6,res6,lift7,res7)
	instance_17 = lift2res(lift8,res8, lift9,res9, lift10,res10, lift11,res11, lift12,res12, lift13,res13,lift14,res14,lift15,res15)
        
        instance_30 = ShiftReg(clock, WIDTH, reset, fB0, si0, po0)
        instance_31 = toSig(clock, sig0,flgs0,lft0,sam0,rht0, upd0)
        instance_32 = ShiftReg(clock, WIDTH, reset, fB1, si1, po1)
        instance_33 = toSig(clock, sig1,flgs1,lft1,sam1,rht1, upd1)
        instance_34 = ShiftReg(clock, WIDTH, reset, fB2, si2, po2)
        instance_35 = toSig(clock, sig2,flgs2,lft2,sam2,rht2, upd2)
        instance_36 = ShiftReg(clock, WIDTH, reset, fB3, si3, po3)
        instance_37 = toSig(clock, sig3,flgs3,lft3,sam3,rht3, upd3)  
        instance_38 = ShiftReg(clock, WIDTH, reset, fB4, si4, po4)
        instance_39 = toSig(clock, sig4,flgs4,lft4,sam4,rht4, upd4)
        instance_40 = ShiftReg(clock, WIDTH, reset, fB5, si5, po5)
        instance_41 = toSig(clock, sig5,flgs5,lft5,sam5,rht5, upd5)
        instance_42 = ShiftReg(clock, WIDTH, reset, fB6, si6, po6)
        instance_43 = toSig(clock, sig6,flgs6,lft6,sam6,rht6, upd6)
        instance_44 = ShiftReg(clock, WIDTH, reset, fB7, si7, po7)
        instance_45 = toSig(clock, sig7,flgs7,lft7,sam7,rht7, upd7)
  
        instance_50 = ShiftReg(clock, WIDTH, reset, fB8, si8, po8)
        instance_51 = toSig(clock, sig8,flgs8,lft8,sam8,rht8, upd8)
        instance_52 = ShiftReg(clock, WIDTH, reset, fB9, si9, po9)
        instance_53 = toSig(clock, sig9,flgs9,lft9,sam9,rht9, upd9)
        instance_54 = ShiftReg(clock, WIDTH, reset, fB10, si10, po10)
        instance_55 = toSig(clock, sig10,flgs10,lft10,sam10,rht10, upd10)
        instance_56 = ShiftReg(clock, WIDTH, reset, fB11, si11, po11)
        instance_57 = toSig(clock, sig11,flgs11,lft11,sam11,rht11, upd11)  
        instance_58 = ShiftReg(clock, WIDTH, reset, fB12, si12, po12)
        instance_59 = toSig(clock, sig12,flgs12,lft12,sam12,rht12, upd12)
        instance_60 = ShiftReg(clock, WIDTH, reset, fB13, si13, po13)
        instance_61 = toSig(clock, sig13,flgs13,lft13,sam13,rht13, upd13)
        instance_62 = ShiftReg(clock, WIDTH, reset, fB14, si14, po14)
        instance_63 = toSig(clock, sig14,flgs14,lft14,sam14,rht14, upd14)
        instance_64 = ShiftReg(clock, WIDTH, reset, fB15, si15, po15)
        instance_65 = toSig(clock, sig15,flgs15,lft15,sam15,rht15, upd15) 

 
	instance_70 = signed2twoscomplement(res0, z0)
	instance_71 = signed2twoscomplement(res1, z1)
	instance_72 = signed2twoscomplement(res2, z2)
	instance_73 = signed2twoscomplement(res3, z3)
	instance_74 = signed2twoscomplement(res4, z4)
	instance_75 = signed2twoscomplement(res5, z5)
	instance_76 = signed2twoscomplement(res6, z6)
	instance_77 = signed2twoscomplement(res7, z7)
	instance_78 = signed2twoscomplement(res8, z8)
	instance_79 = signed2twoscomplement(res9, z9)
	instance_80 = signed2twoscomplement(res10, z10)
	instance_81 = signed2twoscomplement(res11, z11)
	instance_82 = signed2twoscomplement(res12, z12)
	instance_83 = signed2twoscomplement(res13, z13)
	instance_84 = signed2twoscomplement(res14, z14)
	instance_85 = signed2twoscomplement(res15, z15)

        instance_90 = para2ser(clock, pp0, ss0, ld)
	return instances()	

 
def tb(clock,si0,fB0,si1,fB1,si2,fB2,si3,fB3,reset,pp0,ss0,ld):
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
	instance_8 = dwt(flgs8, upd8, lft8, sam8, rht8, lift8, done8, clock)
	instance_9 = dwt(flgs9, upd9, lft9, sam9, rht9, lift9, done9, clock)
	instance_10 = dwt(flgs10, upd10, lft10, sam10, rht10, lift10, done10, clock)
	instance_11 = dwt(flgs11, upd11, lft11, sam11, rht11, lift11, done11, clock)
	instance_12 = dwt(flgs12, upd12, lft12, sam12, rht12, lift12, done12, clock)
	instance_13 = dwt(flgs13, upd13, lft13, sam13, rht13, lift13, done13, clock)
	instance_14 = dwt(flgs14, upd14, lft14, sam14, rht14, lift14, done14, clock)
	instance_15 = dwt(flgs15, upd15, lft15, sam15, rht15, lift15, done15, clock)	
	instance_16 = lift2res(lift0,res0, lift1,res1, lift2,res2, lift3,res3, lift4,res4, lift5,res5,lift6,res6,lift7,res7)
	instance_17 = lift2res(lift8,res8, lift9,res9, lift10,res10, lift11,res11, lift12,res12, lift13,res13,lift14,res14,lift15,res15)
        
        instance_30 = ShiftReg(clock, WIDTH, reset, fB0, si0, po0)
        instance_31 = toSig(clock, sig0,flgs0,lft0,sam0,rht0, upd0)
        instance_32 = ShiftReg(clock, WIDTH, reset, fB1, si1, po1)
        instance_33 = toSig(clock, sig1,flgs1,lft1,sam1,rht1, upd1)
        instance_34 = ShiftReg(clock, WIDTH, reset, fB2, si2, po2)
        instance_35 = toSig(clock, sig2,flgs2,lft2,sam2,rht2, upd2)
        instance_36 = ShiftReg(clock, WIDTH, reset, fB3, si3, po3)
        instance_37 = toSig(clock, sig3,flgs3,lft3,sam3,rht3, upd3)  
        instance_38 = ShiftReg(clock, WIDTH, reset, fB4, si4, po4)
        instance_39 = toSig(clock, sig4,flgs4,lft4,sam4,rht4, upd4)
        instance_40 = ShiftReg(clock, WIDTH, reset, fB5, si5, po5)
        instance_41 = toSig(clock, sig5,flgs5,lft5,sam5,rht5, upd5)
        instance_42 = ShiftReg(clock, WIDTH, reset, fB6, si6, po6)
        instance_43 = toSig(clock, sig6,flgs6,lft6,sam6,rht6, upd6)
        instance_44 = ShiftReg(clock, WIDTH, reset, fB7, si7, po7)
        instance_45 = toSig(clock, sig7,flgs7,lft7,sam7,rht7, upd7)
  
        instance_50 = ShiftReg(clock, WIDTH, reset, fB8, si8, po8)
        instance_51 = toSig(clock, sig8,flgs8,lft8,sam8,rht8, upd8)
        instance_52 = ShiftReg(clock, WIDTH, reset, fB9, si9, po9)
        instance_53 = toSig(clock, sig9,flgs9,lft9,sam9,rht9, upd9)
        instance_54 = ShiftReg(clock, WIDTH, reset, fB10, si10, po10)
        instance_55 = toSig(clock, sig10,flgs10,lft10,sam10,rht10, upd10)
        instance_56 = ShiftReg(clock, WIDTH, reset, fB11, si11, po11)
        instance_57 = toSig(clock, sig11,flgs11,lft11,sam11,rht11, upd11)  
        instance_58 = ShiftReg(clock, WIDTH, reset, fB12, si12, po12)
        instance_59 = toSig(clock, sig12,flgs12,lft12,sam12,rht12, upd12)
        instance_60 = ShiftReg(clock, WIDTH, reset, fB13, si13, po13)
        instance_61 = toSig(clock, sig13,flgs13,lft13,sam13,rht13, upd13)
        instance_62 = ShiftReg(clock, WIDTH, reset, fB14, si14, po14)
        instance_63 = toSig(clock, sig14,flgs14,lft14,sam14,rht14, upd14)
        instance_64 = ShiftReg(clock, WIDTH, reset, fB15, si15, po15)
        instance_65 = toSig(clock, sig15,flgs15,lft15,sam15,rht15, upd15) 

 
	instance_70 = signed2twoscomplement(res0, z0)
	instance_71 = signed2twoscomplement(res1, z1)
	instance_72 = signed2twoscomplement(res2, z2)
	instance_73 = signed2twoscomplement(res3, z3)
	instance_74 = signed2twoscomplement(res4, z4)
	instance_75 = signed2twoscomplement(res5, z5)
	instance_76 = signed2twoscomplement(res6, z6)
	instance_77 = signed2twoscomplement(res7, z7)
	instance_78 = signed2twoscomplement(res8, z8)
	instance_79 = signed2twoscomplement(res9, z9)
	instance_80 = signed2twoscomplement(res10, z10)
	instance_81 = signed2twoscomplement(res11, z11)
	instance_82 = signed2twoscomplement(res12, z12)
	instance_83 = signed2twoscomplement(res13, z13)
	instance_84 = signed2twoscomplement(res14, z14)
	instance_85 = signed2twoscomplement(res15, z15)

        instance_90 = para2ser(clock, pp0, ss0, ld)

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
            pp0.next = z0 << 27
            yield clock.posedge
        
            pp0.next = pp0 + (z1 << 18)
            yield clock.posedge
        
            pp0.next = pp0 + (z2 << 9)
            yield clock.posedge
            pp0.next = pp0 + z3
            yield clock.posedge
        
            ld.next = 1
            yield clock.posedge
 
            ld.next = 0
            yield clock.posedge

            for j in range(40):
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
    toVerilog(dwt_top,clock,si0,fB0,si1,fB1,si2,fB2,si3,fB3,reset,pp0,ss0,ld)
    #toVHDL(dwt_top,clock)
 
def main():
    args = cliparse()
    if args.test:
       tb_fsm = traceSignals(tb,clock,si0,fB0,si1,fB1,si2,fB2,si3,fB3,reset,pp0,ss0,ld)
       sim = Simulation(tb_fsm)
       sim.run()  
    if args.convert:
        convert(args)

if __name__ == '__main__':
    main()
