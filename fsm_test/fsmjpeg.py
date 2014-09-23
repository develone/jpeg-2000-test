import os
path = os.path

from myhdl import *

 
#INIT, RD_AND_JPEG_DATA, WR_DATA, INTERLACE, DONE = range(5)
ACTIVE_LOW = bool(0)
FRAME_SIZE = 8
t_State = enum('INIT', 'RD_AND_JPEG_DATA', 'WR_DATA', 'INTERLACE', 'DONE', encoding="one_hot")

def RamCtrl(SOF, state, WR_DATAFlag, clk_fast, reset_n, addrsam_r, addrjpeg_r, rd_r, wr_r):
    
    """ Framing control FSM.

    SOF -- start-of-frame output bit
    state -- RamState output
    WR_DATAFlag -- WR_DATA pattern found indication input
    clk_fast -- clock input
    reset_n -- active low reset
    
    """
    
    index = Signal(intbv(0)[8:]) # position in frame

    @always(clk_fast.posedge, reset_n.negedge)
    def FSM():
        if reset_n == ACTIVE_LOW:
            SOF.next = 0
            index.next = 0
            addrsam_r.next = 1
            addrjpeg_r.next = 8192 + 1
            rd_r.next = 0
            wr_r.next = 0
            state.next = t_State.INIT
        else:
            index.next = (index + 1) % FRAME_SIZE
            SOF.next = 0
            if state == t_State.INIT:
                addrsam_r.next = 1
                addrjpeg_r.next = 8192 + 1
                rd_r.next = 0
                wr_r.next = 0
                state.next = t_State.RD_AND_JPEG_DATA
            elif state == t_State.RD_AND_JPEG_DATA:
                rd_r.next = 1
                if (addrsam_r <= 21):
                    addrsam_r.next = addrsam_r + 2
                else:
                    addrsam_r.next = 1
                    state.next = t_State.WR_DATA
            elif state == t_State.WR_DATA:
                rd_r.next = 0
                wr_r.next = 1
                SOF.next = 1
                if addrjpeg_r <= (8192 + 21):
                    addrjpeg_r.next = addrjpeg_r + 2
                else:
                    wr_r.next = 0
                    addrjpeg_r.next = (8192 + 1)
                    state.next = t_State.INTERLACE
            elif state == t_State.INTERLACE:
                
                if (addrsam_r <= 21):
                    rd_r.next = 1
                    addrsam_r.next = addrsam_r + 2
                    rd_r.next = 0
                    wr_r.next = 1
                    addrjpeg_r.next = addrjpeg_r + 2
                    wr_r.next = 0
                else:
                    addrsam_r.next = 1
                    addrjpeg_r.next = (8192 + 1)
                    state.next = t_State.INIT
            elif state == t_State.DONE:
                SOF.next = 0
            else:
                raise ValueError("Undefined state")
        #addrjpeg_r.next <= addrjpeg_r
        #addrsam_r.next <= addrsam_r
            
    return FSM


  
def main():

    SOF = Signal(bool(0))
    WR_DATAFlag = Signal(bool(0))
    clk_fast = Signal(bool(0))
    reset_n = Signal(bool(1))
    state = Signal(t_State.INIT)
    addrsam_r = Signal(intbv(0, min = 0, max = 8388608))
    addrjpeg_r = Signal(intbv(0, min = 0, max = 8388608))
    rd_r = Signal(bool(0))
    wr_r = Signal(bool(0))
    toVerilog(RamCtrl, SOF, state, WR_DATAFlag, clk_fast, reset_n, addrsam_r, addrjpeg_r, rd_r, wr_r)
    toVHDL(RamCtrl, SOF, state, WR_DATAFlag, clk_fast, reset_n, addrsam_r, addrjpeg_r, rd_r, wr_r)


if __name__ == '__main__':
    main()
