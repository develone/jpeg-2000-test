from myhdl import *
from jpeg_constants import *
#toVHDL.numeric_ports = False
def jp_process( res_out_x, left_s_i, sam_s_i, right_s_i,flgs_s_i, noupdate_s, update_s, W0=3, LVL0=4, W1=3, LVL1=4, W2=3, LVL2=4,  W3=3, LVL3=4, SIMUL=0 ):

    print W0, LVL0, W1, LVL1, W2, LVL2, W3, LVL3, SIMUL

    #sig_in_x = [sig_in_x_i((i+1)*W0, i*W0) for i in range(0, LVL0) ]
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
        update_s needs to be 1
        for the res_out_x to be valid
        noupdate_s goes lo when a
        res_out_x valid
        fwd dwt even flgs_s eq 7
        inv dwt even flgs_s eq 5
        fwd dwt odd flgs_s eq 6
        inv dwt odd flgs_s eq 4
        """
        if (update_s):
            noupdate_s.next = NO
            for i in range(LVL0):
                if (flgs_s[i] == 7):
                    res_out_x.next = sam_s[i].signed() - ( (left_s[i].signed() >> 1) + ( (right_s[i].signed() >> 1)))

                elif (flgs_s[i] == 5):
                    res_out_x.next = sam_s[i].signed() + ( (left_s[i].signed() >> 1) + ( (right_s[i].signed() >> 1)))

                elif (flgs_s[i] == 6):
                    res_out_x.next = sam_s[i].signed() + ((left_s[i].signed()  + right_s[i].signed() + 2 ) >> 2)

                elif (flgs_s[i] == 4):
                    res_out_x.next = sam_s[i].signed() - ((left_s[i].signed()  + right_s[i].signed() + 2 ) >> 2)
        else:
            noupdate_s.next = YES
    if (SIMUL == 0):
        return instances()
    else:
        print "In simulation mode"
        return jpeg_logic
def convert():
    if (SIMUL == 0):
        res_out_x = Signal(intbv(0, min= -(2**(W0-1)) ,max= (2**(W0-1))))
        update_s = Signal(bool(0))
        noupdate_s = Signal(bool(0))
        """ W0, LVL0, W1, LVL1, W2, LVL2, W3, and LVL3
        Required  by jp_process
        these are used to set the size of the
        arrays"""

        #sig_in_x_i = Signal(intbv(0)[LVL0*W0:])
        left_s_i = Signal(intbv(0)[LVL2*W2:])
        sam_s_i = Signal(intbv(0)[LVL2*W2:])
        right_s_i = Signal(intbv(0)[LVL2*W2:])
        flgs_s_i = Signal(intbv(0)[LVL3*W3:])

        dut = toVerilog(jp_process, res_out_x, left_s_i,sam_s_i, right_s_i, flgs_s_i, noupdate_s, update_s,  W0=W0, LVL0=LVL0, W1=W1, LVL1=LVL1, W2=W2, LVL2=LVL2, W3=W3, LVL3=LVL3, SIMUL=SIMUL)
        dut = toVHDL(jp_process, res_out_x, left_s_i,sam_s_i, right_s_i, flgs_s_i, noupdate_s, update_s,  W0=W0, LVL0=LVL0, W1=W1, LVL1=LVL1, W2=W2, LVL2=LVL2, W3=W3, LVL3=LVL3, SIMUL=SIMUL)
    else:
        print "In simulation mode"


#convert()


