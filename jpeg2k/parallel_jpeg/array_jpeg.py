from myhdl import *
 
def jp_process(sig_in_x_i, res_out_x, left_s_i, sam_s_i, right_s_i,flgs_s_i, W0=3, LVL0=4, W1=3, LVL1=4, W2=3, LVL2=4,  W3=3, LVL3=4 ):
    print W0, LVL0, W1, LVL1, W2, LVL2, W3, LVL3
 
    sig_in_x = [sig_in_x_i((i+1)*W0, i*W0) for i in range(0, LVL0) ]
    #res_out_x = [res_out_x_i((i+1)*W1, i*W1) for i in range(0, LVL1) ]
    left_s = [left_s_i((i+1)*W2, i*W2) for i in range(0, LVL2) ]
    sam_s = [sam_s_i((i+1)*W2, i*W2) for i in range(0, LVL2) ]
    right_s = [right_s_i((i+1)*W2, i*W2) for i in range(0, LVL2) ]
    flgs_s = [flgs_s_i((i+1)*W3, i*W3) for i in range(0, LVL3) ]

    print "left_s_i", type(left_s_i)
    print "sam_s_i", type(sam_s_i)
    print "right_s_i", type(right_s_i)
    print "flgs_s_i", type(flgs_s_i)
    @always_comb
    def jpeg_logic():
        """
        fwd dwt even flgs_s eq 7
        inv dwt even flgs_s eq 5
        fwd dwt odd flgs_s eq 6
        inv dwt odd flgs_s eq 4
        """
        if (flgs_s[LVL0-1] == 7):
            res_out_x.next = sam_s[LVL0-1] - ( (left_s[LVL0-1] >> 1) + ( (right_s[LVL0-1] >> 1)))
        
        elif (flgs_s[LVL0-1] == 5):
            res_out_x.next = sam_s[LVL0-1] + ( (left_s[LVL0-1] >> 1) + ( (right_s[LVL0-1] >> 1)))
        
        elif (flgs_s[LVL0-1] == 6):
            res_out_x.next = sam_s[LVL0-1] + (( (left_s[LVL0-1] ) + ( (right_s[LVL0-1] ))) >> 2 )
        
        elif (flgs_s[LVL0-1] == 4):
            res_out_x.next = sam_s[LVL0-1] - (( (left_s[LVL0-1] ) + ( (right_s[LVL0-1] ))) >> 2 )
        
    return instances()
 
def convert():
    W0 = 8
    LVL0 = 16
    W1 = 8
    LVL1 = 16
    W2 = 8
    LVL2 = 16
    W3 = 5
    LVL3 = 16

    sig_in_x_i = Signal(intbv(0)[LVL0*W0:])
    res_out_x = Signal(intbv(0, min= -256 ,max= 256))
    left_s_i = Signal(intbv(0)[LVL2*W2:])
    sam_s_i = Signal(intbv(0)[LVL2*W2:])
    right_s_i = Signal(intbv(0)[LVL2*W2:])
    flgs_s_i = Signal(intbv(0)[LVL3*W3:])
    dut = toVerilog(jp_process, sig_in_x_i, res_out_x, left_s_i,sam_s_i, right_s_i, flgs_s_i, W0=W0, LVL0=LVL0, W1=W1, LVL1=LVL1, W2=W2, LVL2=LVL2, W3=W3, LVL3=LVL3)
    dut = toVHDL(jp_process, sig_in_x_i, res_out_x, left_s_i,sam_s_i, right_s_i, flgs_s_i, W0=W0, LVL0=LVL0, W1=W1, LVL1=LVL1, W2=W2, LVL2=LVL2, W3=W3, LVL3=LVL3) 
 

convert()


