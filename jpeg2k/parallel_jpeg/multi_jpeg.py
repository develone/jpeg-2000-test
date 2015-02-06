from myhdl import *
from jpeg_constants import *
JPEG_DATA_WIDTH = 1024
SIG_IN_WIDTH = 32
JPEG_RAM_ADDR = 23
JPEG_RES_RAM_ADDR = 9
ROW_NUM = 8
ACTIVE_LOW = bool(0)
NO = bool(0)
YES = bool(1)
#force std_logic_vectors
#toVHDL.numeric_ports = False
clk_fast = Signal(bool(0))
sig0_in_x = Signal(intbv(0)[SIG_IN_WIDTH:])
noupdate0_s = Signal(bool(0))
res0_s = Signal(intbv(0, min = -JPEG_DATA_WIDTH, max = JPEG_DATA_WIDTH))

sig1_in_x = Signal(intbv(0)[SIG_IN_WIDTH:])
noupdate1_s = Signal(bool(0))
res1_s = Signal(intbv(0, min = -JPEG_DATA_WIDTH, max = JPEG_DATA_WIDTH))

sig2_in_x = Signal(intbv(0)[SIG_IN_WIDTH:])
noupdate2_s = Signal(bool(0))
res2_s = Signal(intbv(0, min = -JPEG_DATA_WIDTH, max = JPEG_DATA_WIDTH))

sig3_in_x = Signal(intbv(0)[SIG_IN_WIDTH:])
noupdate3_s = Signal(bool(0))
res3_s = Signal(intbv(0, min = -JPEG_DATA_WIDTH, max = JPEG_DATA_WIDTH))

sig4_in_x = Signal(intbv(0)[SIG_IN_WIDTH:])
noupdate4_s = Signal(bool(0))
res4_s = Signal(intbv(0, min = -JPEG_DATA_WIDTH, max = JPEG_DATA_WIDTH))

sig5_in_x = Signal(intbv(0)[SIG_IN_WIDTH:])
noupdate5_s = Signal(bool(0))
res5_s = Signal(intbv(0, min = -JPEG_DATA_WIDTH, max = JPEG_DATA_WIDTH))

sig6_in_x = Signal(intbv(0)[SIG_IN_WIDTH:])
noupdate6_s = Signal(bool(0))
res6_s = Signal(intbv(0, min = -JPEG_DATA_WIDTH, max = JPEG_DATA_WIDTH))

sig7_in_x = Signal(intbv(0)[SIG_IN_WIDTH:])
noupdate7_s = Signal(bool(0))
res7_s = Signal(intbv(0, min = -JPEG_DATA_WIDTH, max = JPEG_DATA_WIDTH))

sig8_in_x = Signal(intbv(0)[SIG_IN_WIDTH:])
noupdate8_s = Signal(bool(0))
res8_s = Signal(intbv(0, min = -JPEG_DATA_WIDTH, max = JPEG_DATA_WIDTH))

sig9_in_x = Signal(intbv(0)[SIG_IN_WIDTH:])
noupdate9_s = Signal(bool(0))
res9_s = Signal(intbv(0, min = -JPEG_DATA_WIDTH, max = JPEG_DATA_WIDTH))

sig10_in_x = Signal(intbv(0)[SIG_IN_WIDTH:])
noupdate10_s = Signal(bool(0))
res10_s = Signal(intbv(0, min = -JPEG_DATA_WIDTH, max = JPEG_DATA_WIDTH))

sig11_in_x = Signal(intbv(0)[SIG_IN_WIDTH:])
noupdate11_s = Signal(bool(0))
res11_s = Signal(intbv(0, min = -JPEG_DATA_WIDTH, max = JPEG_DATA_WIDTH))

sig12_in_x = Signal(intbv(0)[SIG_IN_WIDTH:])
noupdate12_s = Signal(bool(0))
res12_s = Signal(intbv(0, min = -JPEG_DATA_WIDTH, max = JPEG_DATA_WIDTH))

sig13_in_x = Signal(intbv(0)[SIG_IN_WIDTH:])
noupdate13_s = Signal(bool(0))
res13_s = Signal(intbv(0, min = -JPEG_DATA_WIDTH, max = JPEG_DATA_WIDTH))

sig14_in_x = Signal(intbv(0)[SIG_IN_WIDTH:])
noupdate14_s = Signal(bool(0))
res14_s = Signal(intbv(0, min = -JPEG_DATA_WIDTH, max = JPEG_DATA_WIDTH))

sig15_in_x = Signal(intbv(0)[SIG_IN_WIDTH:])
noupdate15_s = Signal(bool(0))
res15_s = Signal(intbv(0, min = -JPEG_DATA_WIDTH, max = JPEG_DATA_WIDTH))

def jpeg_process(clk_fast, sig_in_x,  noupdate_s, res_s):
    left_s = Signal(intbv(0, min = -JPEG_DATA_WIDTH, max = JPEG_DATA_WIDTH))
    sam_s = Signal(intbv(0, min = -JPEG_DATA_WIDTH, max = JPEG_DATA_WIDTH))
    right_s = Signal(intbv(0, min = -JPEG_DATA_WIDTH, max = JPEG_DATA_WIDTH))
    left_s = sig_in_x(9,0)
    sam_s = sig_in_x(18,9)
    right_s = sig_in_x(27,18)
    even_odd_s = sig_in_x(27)
    fwd_inv_s = sig_in_x(28)
    updated_s = sig_in_x(29)
    dum_s = sig_in_x(30)
    dum1_s = sig_in_x(31) 
    @always(clk_fast.posedge)
    def jpeg():
        if updated_s:
            noupdate_s.next = 0
            if even_odd_s:
                if  fwd_inv_s:
                    res_s.next =  sam_s - ((left_s >> 1) + (right_s >> 1))
                else:
                    res_s.next =  sam_s + ((left_s >> 1) + (right_s >> 1))
            else:
                if fwd_inv_s:
                    res_s.next =  sam_s + (((left_s) +  (right_s) + 2)>>2)
                else:
                    res_s.next =  sam_s - (((left_s) +  (right_s) + 2)>>2)
        else:
            noupdate_s.next = 1
    return jpeg
def multi_jpeg(clk_fast, sig0_in_x, noupdate0_s, res0_s,
               sig1_in_x, noupdate1_s, res1_s,
               sig2_in_x, noupdate2_s, res2_s,
               sig3_in_x, noupdate3_s, res3_s,
               sig4_in_x, noupdate4_s, res4_s,
               sig5_in_x, noupdate5_s, res5_s,
               sig6_in_x, noupdate6_s, res6_s,
               sig7_in_x, noupdate7_s, res7_s,
               sig8_in_x, noupdate8_s, res8_s,
               sig9_in_x, noupdate9_s, res9_s,
               sig10_in_x, noupdate10_s, res10_s,
               sig11_in_x, noupdate11_s, res11_s,
               sig12_in_x, noupdate12_s, res12_s,
               sig13_in_x, noupdate13_s, res13_s,
               sig14_in_x, noupdate14_s, res14_s,
               sig15_in_x, noupdate15_s, res15_s
               ):
    instance_0 = jpeg_process( clk_fast, sig0_in_x,  noupdate0_s, res0_s)
    instance_1 = jpeg_process( clk_fast, sig1_in_x,  noupdate1_s, res1_s)
    instance_2 = jpeg_process( clk_fast, sig2_in_x,  noupdate2_s, res2_s)
    instance_3 = jpeg_process( clk_fast, sig3_in_x,  noupdate3_s, res3_s)
    instance_4 = jpeg_process( clk_fast, sig4_in_x,  noupdate4_s, res4_s)
    instance_5 = jpeg_process( clk_fast, sig5_in_x,  noupdate5_s, res5_s)
    instance_6 = jpeg_process( clk_fast, sig6_in_x,  noupdate6_s, res6_s)
    instance_7 = jpeg_process( clk_fast, sig7_in_x,  noupdate7_s, res7_s)
    
    instance_8 = jpeg_process( clk_fast, sig8_in_x,  noupdate8_s, res8_s)
    instance_9 = jpeg_process( clk_fast, sig9_in_x,  noupdate9_s, res9_s)
    instance_10 = jpeg_process( clk_fast, sig10_in_x,  noupdate10_s, res10_s)
    instance_11 = jpeg_process( clk_fast, sig11_in_x,  noupdate11_s, res11_s)
    instance_12 = jpeg_process( clk_fast, sig12_in_x,  noupdate12_s, res12_s)
    instance_13 = jpeg_process( clk_fast, sig13_in_x,  noupdate13_s, res13_s)
    instance_14 = jpeg_process( clk_fast, sig14_in_x,  noupdate14_s, res14_s)
    instance_15 = jpeg_process( clk_fast, sig15_in_x,  noupdate15_s, res15_s)
    return instance_0, instance_1, instance_2, instance_3, instance_4, instance_5, instance_6, instance_7, instance_8, instance_9, instance_10, instance_11, instance_12, instance_13, instance_14, instance_15
"""
toVHDL(multi_jpeg, clk_fast, sig0_in_x, noupdate0_s, res0_s,
               sig1_in_x, noupdate1_s, res1_s,
               sig2_in_x, noupdate2_s, res2_s,
               sig3_in_x, noupdate3_s, res3_s,
               sig4_in_x, noupdate4_s, res4_s,
               sig5_in_x, noupdate5_s, res5_s,
               sig6_in_x, noupdate6_s, res6_s,
               sig7_in_x, noupdate7_s, res7_s,
               sig8_in_x, noupdate8_s, res8_s,
               sig9_in_x, noupdate9_s, res9_s,
               sig10_in_x, noupdate10_s, res10_s,
               sig11_in_x, noupdate11_s, res11_s,
               sig12_in_x, noupdate12_s, res12_s,
               sig13_in_x, noupdate13_s, res13_s,
               sig14_in_x, noupdate14_s, res14_s,
               sig15_in_x, noupdate15_s, res15_s)
"""