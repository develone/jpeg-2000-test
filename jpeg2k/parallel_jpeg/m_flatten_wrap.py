from myhdl import *
from flaten import m_flatten
from jpeg_constants import *
matrix = [[Signal(intbv(0)[W0:]) for mcol in range(4)] for mrow in range(4)]
flat = Signal(intbv(0)[LVL2*W2:])
 
x = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
z = Signal(intbv(0)[W0:])
mrow = Signal(intbv(0)[4:])
mcol = Signal(intbv(0)[4:])

def matrix_wrap(matrix, flat, z, x, mrow, mcol,
W0=W0, LVL0=LVL0, W1=W1, LVL1=LVL1, W2=W2,
LVL2=LVL2, W3=W3, LVL3=LVL3):
    mat = m_flatten(matrix, flat)
    return  mat
toVHDL(matrix_wrap, matrix, flat, z, x, mrow, mcol,
W0=W0, LVL0=LVL0, W1=W1, LVL1=LVL1, W2=W2,
LVL2=LVL2, W3=W3, LVL3=LVL3)
toVerilog(matrix_wrap, matrix, flat, z, x, mrow, mcol,
W0=W0, LVL0=LVL0, W1=W1, LVL1=LVL1, W2=W2,
LVL2=LVL2, W3=W3, LVL3=LVL3)