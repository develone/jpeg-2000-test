from myhdl import *
import argparse
from jpeg import dwt
from signed2twoscomplement import signed2twoscomplement
from l2r import lift2res1
from sh_reg import ShiftReg, toSig
from para2ser import para2ser
from div_clk import div_4
from jpeg_sig import *
 

clock = Signal(bool(0))
 


def lower_upper(m,width,height):

    temp_bank = [[0]*width for i in range(height)]
    for col in range(width/2,width,1):

        for row in range(height/2,height,1):

            temp_bank[col-width/2][row-height/2] = m[row][col]

    for row in range(width):
        for col in range(height):
            m[row][col] = temp_bank[col][row]

 

def cliparse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--build", default=False, action='store_true')
    parser.add_argument("--test", default=False, action='store_true')
    parser.add_argument("--convert", default=False, action='store_true')
    args = parser.parse_args()
    return args 

        
def dwt_top(
       flgs0, 
       upd0, 
       lft0,
       sam0, 
       rht0, 
        
       done0, 
       clock, 
        
       z0,
       flgs1, 
       upd1, 
       lft1,
       sam1, 
       rht1, 
       
       done1,  
        
       z1,       
       ):
    instance_0 = dwt(flgs0, upd0, lft0, sam0, rht0, lift0, done0, clock)
    instance_16 = lift2res1(lift0,res0)
    instance_70 = signed2twoscomplement(res0, z0)

    instance_1 = dwt(flgs1, upd1, lft1, sam1, rht1, lift1, done1, clock)
    instance_17 = lift2res1(lift1,res1)
    instance_71 = signed2twoscomplement(res1, z1)

    instance_2 = dwt(flgs2, upd2, lft2, sam2, rht2, lift2, done2, clock)
    instance_18 = lift2res1(lift2,res2) 
    instance_72 = signed2twoscomplement(res2, z2)

    instance_3 = dwt(flgs3, upd3, lft3, sam3, rht4, lift3, done3, clock)
    instance_19 = lift2res1(lift3,res3)
    instance_73 = signed2twoscomplement(res3, z3) 
    
    return instances()    

 
def tb(
       flgs0, 
       upd0, 
       lft0,
       sam0, 
       rht0, 
        
       done0, 
       clock, 
        
       z0,
       flgs1, 
       upd1, 
       lft1,
       sam1, 
       rht1, 
        
       done1,  
        
       z1,       
       ):
    def de_interleave(m,height,width):
        # de-interleave
        temp_bank = [[0]*width for i in range(height)]
        for row in range(width):
            for col in range(width):
                # k1 and k2 scale the vals
                # simultaneously transpose the matrix when deinterleaving
                if row % 2 == 0:
    
                    temp_bank[col][row/2] =  m[row][col]
                else:
    
                    temp_bank[col][row/2 + height/2] =  m[row][col]
        # write temp_bank to s:
        for row in range(width):
            for col in range(height):
                m[row][col] = temp_bank[row][col]
    def seq_to_img(m, pix):
        ''' Copy matrix m to pixel buffer pix.
        Assumes m has the same number of rows and cols as pix. '''
        for row in range(len(m)):
            for col in range(len(m[row])):
                pix[col,row] = m[row][col]
    from PIL import Image
    im = Image.open("../lena_256.png")
    pix = im.load()
    m = list(im.getdata())
    #print m.__sizeof__()
    m = [m[i:i+im.size[0]] for i in range(0, len(m), im.size[0])] 
    #print m
    #print len(m[0]), len(m[1])

    @always(delay(10))
    def clkgen():
        clock.next = not clock
    instance_0 = dwt(flgs0, upd0, lft0, sam0, rht0, lift0, done0, clock)
    instance_16 = lift2res1(lift0,res0)
    instance_70 = signed2twoscomplement(res0, z0)

    instance_1 = dwt(flgs1, upd1, lft1, sam1, rht1, lift1, done1, clock)
    instance_17 = lift2res1(lift1,res1)
    instance_71 = signed2twoscomplement(res1, z1)

    instance_2 = dwt(flgs2, upd2, lft2, sam2, rht2, lift2, done2, clock)
    instance_18 = lift2res1(lift2,res2) 
    instance_72 = signed2twoscomplement(res2, z2)

    instance_3 = dwt(flgs3, upd3, lft3, sam3, rht4, lift3, done3, clock)
    instance_19 = lift2res1(lift3,res3)
    instance_73 = signed2twoscomplement(res3, z3) 
    @instance
    def stimulus():
        for col in range(256):
            for row in range(6,256,2):
                '''
                sending from host to FPGA 
                m[row-5][col] m[row-4][col] m[row-3][col] 
                m[row-6][col] m[row-3][col] m[row-2][col]
                flgs0 upd0 flgs1 upd1 flgs2 upd2 flgs3 upd3 
                returning to host from FPGA
                m[row-4][col] m[row-5][col] m[row-2][col] m[row-3][col]
                First pass even odd samples  
                1 2 3  0 1 2
                1
                '''
                lft0.next = m[row-5][col]
                yield clock.posedge
                # 2
                sam0.next = m[row-4][col]
                yield clock.posedge
                # 3
                rht0.next = m[row-3][col]
                yield clock.posedge
                flgs0.next = 7
                yield clock.posedge
                upd0.next = 1
                yield clock.posedge
                upd0.next = 0
                yield clock.posedge
                #this needs to be the rht1
                #1 2 3  0 1 2
                # 2
                m[row-4][col] = lift0[W0:]
                # 2
                rht1.next = z0
                yield clock.posedge
                # 0
                lft1.next = m[row-6][col]
                yield clock.posedge
                # 1
                sam1.next = lft0
                yield clock.posedge
                flgs1.next = 6
                yield clock.posedge
                upd1.next = 1
                yield clock.posedge
                upd1.next = 0
                yield clock.posedge
                #this needs to be the rht2
                # 1
                m[row-5][col] = lift1[W0:]
                
                #3 4 5  2 3 4
                # 5
                rht2.next = z1
                yield clock.posedge
                # 3
                lft2.next = rht0
                #lft2.next = m[row-3][col]
                yield clock.posedge
                # 4
                sam2.next = m[row-2][col]
                yield clock.posedge
 
                flgs2.next = 7
                yield clock.posedge
                upd2.next = 1
                yield clock.posedge
                upd2.next = 0
                yield clock.posedge
                #this needs to be the rht3
                # 4
                m[row-2][col] = lift2[W0:]
                #3 4 5  2 3 4
                # 4
                rht3.next = z2
                yield clock.posedge
                # 2
                lft3.next = z1
                #lft3.next = m[row-4][col] 
                yield clock.posedge
                # 3
                sam3.next = lft2
                yield clock.posedge
                flgs3.next = 6
                yield clock.posedge
                upd3.next = 1
                yield clock.posedge
                upd3.next = 0
                yield clock.posedge
                #this needs to be the rht1
                # 3
                m[row-3][col] = lift3[W0:]
                 
        de_interleave(m,256,256)
        seq_to_img(m, pix)
        im.save("test1_256_fwt1pass.png")        
        for col in range(256):
            for row in range(6,256,2):
                #1 2 3  0 1 2
                # 1
                lft0.next = m[row-5][col]
                yield clock.posedge
                # 2
                sam0.next = m[row-4][col]
                yield clock.posedge
                # 3
                rht0.next = m[row-3][col]
                yield clock.posedge
                flgs0.next = 7
                yield clock.posedge
                upd0.next = 1
                yield clock.posedge
                upd0.next = 0
                yield clock.posedge
                #this needs to be the rht1
                #1 2 3  0 1 2
                # 2
                m[row-4][col] = lift0[W0:]
                # 2
                rht1.next = z0
                yield clock.posedge
                # 0
                lft1.next = m[row-6][col]
                yield clock.posedge
                # 1
                sam1.next = lft0
                yield clock.posedge
                flgs1.next = 6
                yield clock.posedge
                upd1.next = 1
                yield clock.posedge
                upd1.next = 0
                yield clock.posedge
                #this needs to be the rht2
                # 1
                m[row-5][col] = lift1[W0:] 
        de_interleave(m,256,256)
        seq_to_img(m, pix)
        im.save("test1_256_fwt2pass.png")        
                
        raise StopSimulation    
    return instances()
 
def convert(args):
    toVerilog(dwt_top,
       flgs0, 
       upd0, 
       lft0,
       sam0, 
       rht0, 
        
       done0, 
       clock, 
       
       z0,
       flgs1, 
       upd1, 
       lft1,
       sam1, 
       rht1, 
        
       done1,  
        
       z1,       
       )
  
    #toVHDL(dwt_top,clock)
 
def main():
    args = cliparse()
    if args.test:
       tb_fsm = traceSignals(tb,
       flgs0, 
       upd0, 
       lft0,
       sam0, 
       rht0, 
        
       done0, 
       clock, 
       
       z0,
       flgs1, 
       upd1, 
       lft1,
       sam1, 
       rht1, 
        
       done1,  
       
       z1,       
       )
       sim = Simulation(tb_fsm)
       sim.run()  
    if args.convert:
        convert(args)

if __name__ == '__main__':
    main()
