
# Need to verify each design is correct, it is easiest 
# to verify each of the converted files (Verilog).  By
# verifying the final result, the design, functionality,
# methodology, etc are all verified.
# 
# Using Python testbenches because Python is a very flexible
# easy language (author knows well).  No need for complicated
# compile (builds) etc.

from __future__ import division
from __future__ import print_function

import os
import argparse
from argparse import Namespace
import math

from myhdl import *
from jpeg_sig import *
clock = Signal(bool(0))
def _prep_cosim(args, **sigs):
    """ prepare the cosimulation environment
    """
    # compile the verilog files with the verilog simulator
    files = ['./dwt_top.v','./tb_dwt_top.v',]
    
    print("compiling ...")
    cmd = "iverilog -o dwt_top %s " % (" ".join(files))
    print("  *%s" %  (cmd))
    os.system(cmd)

    # get the handle to the
    print("cosimulation setup ...")
    cmd = "vvp -m ./myhdl.vpi dwt_top"
    print("  *%s" %  (cmd))
    return Cosimulation(cmd, **sigs)

def de_interleave(m,height,width):
    # de-interleave
    temp_bank = [[0]*width for i in range(height)]
    for row in range(width):
        for col in range(width):
            # k1 and k2 scale the vals
            # simultaneously transpose the matrix when deinterleaving
            if row % 2 == 0:
                temp_bank[col][row//2] =  m[row][col]
            else:
                temp_bank[col][row//2 + height//2] =  m[row][col]
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
w, h = im.size
pix = im.load()
m = list(im.getdata())
m = [m[i:i+im.size[0]] for  i in range(0, len(m), im.size[0])]

def test_dwt_top(args):

    tbdut =  _prep_cosim(args,flgs0=flgs0,upd0=upd0,lft0=lft0,sam0=sam0,rht0=rht0,done0=done0,clock=clock,z0=z0,flgs1=flgs1,upd1=upd1,lft1=lft1,sam1=sam1,rht1=rht1,done1=done1,z1=z1 )

    @always(delay(4))
    def tbclk():
       clock.next = not clock
    
    @instance
    def tbstim():
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
 
                #print ("%8d: %d %d %d %d %d %d" % (now(),row,col,lft0,sam0,rht0,z0))
                m[row][col] = int(z0)
 
            for row in range(1,256-1,2):
                lft1.next = m[row-1][col]
                yield clock.posedge
                # 1
                sam1.next = m[row][col]
                yield clock.posedge
                rht1.next = m[row+1][col]
                yield clock.posedge
                flgs1.next = 6
                yield clock.posedge
                upd1.next = 1
                yield clock.posedge
                upd1.next = 0
                yield clock.posedge
 
                #print ("%8d: %d %d %d %d %d %d" % (now(),row,col,lft1,sam1,rht1,z1))
                m[row][col] = int(z1)
        print ("8%d :%d %d" % (now(),h,w))
        de_interleave(m,h,w)
        seq_to_img(m, pix)
        print("%8d: writing test1_256_fwt1pass.png " % (now()))
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
 
                #print ("%8d: %d %d %d %d %d %d" % (now(),row,col,lft0,sam0,rht0,z0))
                m[row][col] = int(z0)
 
            for row in range(1,256-1,2):
                lft1.next = m[row-1][col]
                yield clock.posedge
                # 1
                sam1.next = m[row][col]
                yield clock.posedge
                rht1.next = m[row+1][col]
                yield clock.posedge
                flgs1.next = 6
                yield clock.posedge
                upd1.next = 1
                yield clock.posedge
                upd1.next = 0
                yield clock.posedge
 
                #print ("%8d: %d %d %d %d %d %d" % (now(),row,col,lft1,sam1,rht1,z1))
                m[row][col] = int(z1)
        print ("8%d :%d %d" % (now(),h,w))
        de_interleave(m,h,w)
        seq_to_img(m, pix)
        print("%8d: writing test1_256_fwt2pass.png " % (now()))
        im.save("test1_256_fwt2pass.png")
      
        raise StopSimulation

    print("start (co)simulation ...")
    Simulation((tbdut, tbstim, tbclk,)).run()


test_dwt_top(Namespace())
 

