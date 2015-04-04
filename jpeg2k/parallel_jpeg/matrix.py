from myhdl import *
from jpeg_constants import *
def matrix(mrow, mcol, x, flat_s_i):
    flat_i = [flat_s_i((i+1)*9, i*9) for i in range(0, 16) ]
    @always_comb
    def matrix_logic():
        if (mrow == 3 and mcol == 3):
            x.next = flat_i[0]
        elif (mrow == 3 and mcol == 2):
            x.next = flat_i[1]
        elif (mrow == 3 and mcol == 1):
            x.next = flat_i[2]
        elif (mrow == 3 and mcol == 0):
            x.next = flat_i[3]
        elif (mrow == 2 and mcol == 3):
            x.next = flat_i[4]
        elif (mrow == 2 and mcol == 2):
            x.next = flat_i[5]
        elif (mrow == 2 and mcol == 1):
            x.next = flat_i[6]
        elif (mrow == 2 and mcol == 0):
            x.next = flat_i[7]
        elif (mrow == 1 and mcol == 3):
            x.next = flat_i[8]
        elif (mrow == 1 and mcol == 2):
            x.next = flat_i[9]
        elif (mrow == 1 and mcol == 1):
            x.next = flat_i[10]
        elif (mrow == 1 and mcol == 0):
            x.next = flat_i[11]
        elif (mrow == 0 and mcol == 3):
            x.next = flat_i[12]
        elif (mrow == 0 and mcol == 2):
            x.next = flat_i[13]
        elif (mrow == 0 and mcol == 1):
            x.next = flat_i[14]
        elif (mrow == 0 and mcol == 0):
            x.next = flat_i[15]
    return matrix_logic
def convert():
    x = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
    mrow = Signal(intbv(0)[4:])
    mcol = Signal(intbv(0)[4:])
    flat_s_i = Signal(intbv(0)[LVL2*W2:])
    toVerilog(matrix, mrow, mcol, x, flat_s_i)
    toVHDL(matrix, mrow, mcol, x, flat_s_i)

#convert()
