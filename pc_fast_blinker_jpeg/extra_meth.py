from myhdl import *
import argparse
#from div_clk import div_4
#from para2ser import para2ser
from jpeg_sig import *
 
clock = Signal(bool(0))
ctn1 = Signal(intbv(0)[6:])
ctn2 = Signal(intbv(0)[6:])
def meth1(): 
    @always(clkInOut.posedge)
    def rtl3():
	if (ctn2 == 36):
            ctn2.next = 0
            
        else:
            ctn2.next = ctn2 + 1
    return rtl3
def meth2():
    @always(clkInOut.posedge)
    def rtl2():
        if(ctn2 == 0):
            pp0.next = (170 << 27) + (170 << 18) + (170 << 9) + 120
        else:
            pp0.next = 0 

    return rtl2
def meth3():
    @always(clkInOut.posedge)
    def rtl1():
        if(ctn1 == 0):
            ld.next = 1
        else:
            ld.next = 0
    return rtl1
def meth4():
    @always(clkInOut.posedge)
    def rtl():
	if (ctn1 == 38):
            ctn1.next = 0
            
        else:
            ctn1.next = ctn1 + 1
    return rtl
'''
toVerilog(meth1)
toVerilog(meth2)
toVerilog(meth3)
toVerilog(meth4)
'''

