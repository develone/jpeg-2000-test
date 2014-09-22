import os
path = os.path

from myhdl import *

 
#INIT, RD_AND_JPEG_DATA, WR_DATA, INTERLACE, DONE = range(5)
ACTIVE_LOW = bool(0)
FRAME_SIZE = 8
t_State = enum('INIT', 'RD_AND_JPEG_DATA', 'WR_DATA', 'INTERLACE', 'DONE', encoding="one_hot")

def RamCtrl(SOF, state, WR_DATAFlag, clk_fast, reset_n):
    
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
            state.next = t_State.RD_AND_JPEG_DATA
        else:
            index.next = (index + 1) % FRAME_SIZE
            SOF.next = 0
            if state == t_State.INIT:
                index.next = 1
                if WR_DATAFlag:
                    state.next = t_State.RD_AND_JPEG_DATA
            elif state == t_State.RD_AND_JPEG_DATA:
                if index == 0:
                    if WR_DATAFlag:
                        state.next = t_State.WR_DATA
                    else:
                        state.next = t_State.INIT
            elif state == t_State.WR_DATA:
                SOF.next = 0
            elif state == t_State.INTERLACE:
                if index == 0:
                    if not WR_DATAFlag:
                        state.next = t_State.INIT
                SOF.next = (index == FRAME_SIZE-1)
            elif state == t_State.DONE:
                SOF.next = 0
            else:
                raise ValueError("Undefined state")
            
    return FSM


  
def main():

    SOF = Signal(bool(0))
    WR_DATAFlag = Signal(bool(0))
    clk_fast = Signal(bool(0))
    reset_n = Signal(bool(1))
    state = Signal(t_State.INIT)

    toVerilog(RamCtrl, SOF, state, WR_DATAFlag, clk_fast, reset_n)
    toVHDL(RamCtrl, SOF, state, WR_DATAFlag, clk_fast, reset_n)


if __name__ == '__main__':
    main()
