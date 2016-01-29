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
    #instance_16 = lift2res1(lift0,res0)
    #instance_70 = signed2twoscomplement(res0, z0)

    #instance_1 = dwt(flgs1, upd1, lft1, sam1, rht1, lift1, done1, clock)
    #instance_17 = lift2res1(lift1,res1)
    #instance_71 = signed2twoscomplement(res1, z1)
 
    @instance
    def stimulus():
        for col in range(256):
            for row in range(2,256,2):
                lft0.next = m[row-1][col]
                yield clock.posedge
                sam0.next = m[row][col]
                yield clock.posedge
                rht0.next = m[row+1][col]
                yield clock.posedge
                flgs0.next = 7
                yield clock.posedge
                upd0.next = 1
                yield clock.posedge
                upd0.next = 0
                yield clock.posedge
                m[row][col] = lift0[W0:]
                #yield clock.posedge
                
                #print ("%d %d %d %d" % (lft0,sam0,rht0,z0))
                #print ("%s %s %s" % (bin(lift0,10),bin(res0,10),bin(z0,9)))
                
                #m[row][col] = z0
                
                #print ("%d %d %d" % (row,col,m[row][col]))
                
                #yield clock.posedge
            for row in range(1,256-1,2):
                lft0.next = m[row-1][col]
                yield clock.posedge
                sam0.next = m[row][col]
                yield clock.posedge
                rht0.next = m[row+1][col]
                yield clock.posedge
                flgs0.next = 6
                yield clock.posedge
                upd0.next = 1
                yield clock.posedge
                upd0.next = 0
                yield clock.posedge
                m[row][col] = lift0[W0:]
                #yield clock.posedge
                
                #print ("%d %d %d %d" % (lft0,sam0,rht0,z0))
                #print ("%s %s %s" % (bin(lift0,10),bin(res0,10),bin(z0,9)))
                
                #m[row][col] = z0
                
                #print ("%d %d %d" % (row,col,m[row][col]))
                
                #yield clock.posedge
        de_interleave(m,256,256)
        seq_to_img(m, pix)
        im.save("test1_256_fwt1pass.png")        
        for col in range(256):
            for row in range(2,256,2):
                lft0.next = m[row-1][col]
                yield clock.posedge
                sam0.next = m[row][col]
                yield clock.posedge
                rht0.next = m[row+1][col]
                yield clock.posedge
                flgs0.next = 7
                yield clock.posedge
                upd0.next = 1
                yield clock.posedge
                upd0.next = 0
                yield clock.posedge
                m[row][col] = lift0[W0:]
                #yield clock.posedge
                
                #print ("%d %d %d %d" % (lft0,sam0,rht0,z0))
                #print ("%s %s %s" % (bin(lift0,10),bin(res0,10),bin(z0,9)))
                
                #m[row][col] = z0
                
                #print ("%d %d %d" % (row,col,m[row][col]))
                
                #yield clock.posedge
            for row in range(1,256-1,2):
                lft0.next = m[row-1][col]
                yield clock.posedge
                sam0.next = m[row][col]
                yield clock.posedge
                rht0.next = m[row+1][col]
                yield clock.posedge
                flgs0.next = 6
                yield clock.posedge
                upd0.next = 1
                yield clock.posedge
                upd0.next = 0
                yield clock.posedge
                m[row][col] = lift0[W0:]
                #yield clock.posedge
                
                #print ("%d %d %d %d" % (lft0,sam0,rht0,z0))
                #print ("%s %s %s" % (bin(lift0,10),bin(res0,10),bin(z0,9)))
                
                #m[row][col] = z0
                
                #print ("%d %d %d" % (row,col,m[row][col]))
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
