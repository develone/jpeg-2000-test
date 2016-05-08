import myhdl
from myhdl import Signal,always_comb,intbv

i_rpi2B = Signal(intbv(0)[8:])
o_rpi2B = Signal(intbv(0)[8:])

fr_depp = Signal(intbv(0)[8:])
to_depp = Signal(intbv(0)[8:])

def rpi2B_io(i_rpi2B,fr_depp,o_rpi2B,to_depp):		
 
    @always_comb
    def rtl1():
        to_depp[1:0].next = i_rpi2B[1:0]
        to_depp[2:1].next = i_rpi2B[2:1]
        to_depp[3:2].next = i_rpi2B[3:2]
        to_depp[4:3].next = i_rpi2B[4:3]
        to_depp[5:4].next = i_rpi2B[5:4]
        to_depp[6:5].next = i_rpi2B[6:5]
        to_depp[7:6].next = i_rpi2B[7:6]
        to_depp[8:7].next = i_rpi2B[8:7]
    @always_comb
    def rtl2():
        o_rpi2B[1:0].next = fr_depp[1:0]
        o_rpi2B[2:1].next = fr_depp[2:1]
        o_rpi2B[3:2].next = fr_depp[3:2]
        o_rpi2B[4:3].next = fr_depp[4:3]
        o_rpi2B[5:4].next = fr_depp[5:4]
        o_rpi2B[6:5].next = fr_depp[6:5]
        o_rpi2B[7:6].next = fr_depp[7:6]
        o_rpi2B[8:7].next = fr_depp[8:7]

				        	
    return myhdl.instances()
