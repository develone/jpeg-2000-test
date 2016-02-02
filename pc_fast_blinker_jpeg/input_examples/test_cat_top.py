
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
WIDTH_OUT = 36
WIDTH = 31
W0 = 9
clock = Signal(bool(0))
clkInOut = Signal(bool(0))
pi_in = Signal(bool(0))
cat_out = Signal(bool(0))
pi_in1 = Signal(bool(0))
cat_out1 = Signal(bool(0))
pi_in2 = Signal(bool(0))
cat_out2 = Signal(bool(0))
pi_in3 = Signal(bool(0))
cat_out3 = Signal(bool(0))

ctn1 = Signal(intbv(0)[6:])
ctn2 = Signal(intbv(0)[6:])

ld_o = Signal(bool(0))
pp0 = Signal(intbv(0)[WIDTH_OUT:])
ld = Signal(bool(0)) 
ss0 = Signal(bool(0))


#ctn = Signal(intbv(0)[3:]) 
def _prep_cosim(args, **sigs):
    """ prepare the cosimulation environment
    """
    # compile the verilog files with the verilog simulator
    files = ['./cat_top.v','./tb_cat_top.v',]
    
    print("compiling ...")
    cmd = "iverilog -o cat_top %s " % (" ".join(files))
    print("  *%s" %  (cmd))
    os.system(cmd)

    # get the handle to the
    print("cosimulation setup ...")
    cmd = "vvp -m ./myhdl.vpi cat_top"
    return Cosimulation(cmd, **sigs)


def test_cat_top(args):
 

    tbdut =  _prep_cosim(args,clock=clock,pi_in=pi_in,cat_out=cat_out,pi_in1=pi_in1,cat_out1=cat_out1,pi_in2=pi_in2,cat_out2=cat_out2,pi_in3=pi_in3,cat_out3=cat_out3,clkInOut=clkInOut,ss0=ss0,ld_o=ld_o)

    @always(delay(10))
    def tbclk():
       clock.next = not clock
    
    @instance
    def tbstim():
 
		for i in range(900):
			yield clock.posedge
			print ("%8d:  %d  %d  %d  %d  %d  %d  %d  %d" % (now(),pi_in,cat_out,clkInOut,ld_o,ss0,clock,ctn1,ctn2))
			pi_in.next = 1
			print ("%8d:  %d  %d  %d  %d  %d  %d  %d  %d" % (now(),pi_in,cat_out,clkInOut,ld_o,ss0,clock,ctn1,ctn2))
			yield clock.posedge
			print ("%8d:  %d  %d  %d  %d  %d  %d  %d  %d" % (now(),pi_in,cat_out,clkInOut,ld_o,ss0,clock,ctn1,ctn2))
			pi_in.next = 0
			print ("%8d:  %d  %d  %d  %d  %d  %d  %d  %d" % (now(),pi_in,cat_out,clkInOut,ld_o,ss0,clock,ctn1,ctn2))
			yield clock.posedge
			print ("%8d:  %d  %d  %d  %d  %d  %d  %d  %d" % (now(),pi_in,cat_out,clkInOut,ld_o,ss0,clock,ctn1,ctn2))
	     
		raise StopSimulation

    print("start (co)simulation ...")
    Simulation((tbdut, tbstim, tbclk,)).run()


if __name__ == '__main__':
    test_cat_top(Namespace())
