from myhdl import *
from jpeg_constants import *
def matrix(mrow, mcol, x, elements_s_i):
    element_s = [elements_s_i((i+1)*9, i*9) for i in range(0, 16) ]
    @always_comb
    def matrix_logic():
        if (mrow == 3 and mcol == 3):
            x.next = element_s[0]
        elif (mrow == 3 and mcol == 2):
            x.next = element_s[1]
        elif (mrow == 3 and mcol == 1):
            x.next = element_s[2]
        elif (mrow == 3 and mcol == 0):
            x.next = element_s[3]
        elif (mrow == 2 and mcol == 3):
            x.next = element_s[4]
        elif (mrow == 2 and mcol == 2):
            x.next = element_s[5]
        elif (mrow == 2 and mcol == 1):
            x.next = element_s[6]
        elif (mrow == 2 and mcol == 0):
            x.next = element_s[7]
        elif (mrow == 1 and mcol == 3):
            x.next = element_s[8]
        elif (mrow == 1 and mcol == 2):
            x.next = element_s[9]
        elif (mrow == 1 and mcol == 1):
            x.next = element_s[10]
        elif (mrow == 1 and mcol == 0):
            x.next = element_s[11]
        elif (mrow == 0 and mcol == 3):
            x.next = element_s[12]
        elif (mrow == 0 and mcol == 2):
            x.next = element_s[13]
        elif (mrow == 0 and mcol == 1):
            x.next = element_s[14]
        elif (mrow == 0 and mcol == 0):
            x.next = element_s[15]
    return matrix_logic
def convert():
    x = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
    mrow = Signal(intbv(0)[4:])
    mcol = Signal(intbv(0)[4:])
    elements_s_i = Signal(intbv(0)[LVL2*W2:])
    dut = toVerilog(matrix, mrow, mcol, x, elements_s_i)
convert()
