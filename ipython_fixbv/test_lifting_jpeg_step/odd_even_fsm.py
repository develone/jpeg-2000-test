import os
path = os.path

from myhdl import *

# INIT, READ_DATA, DONE = range(3)

ACTIVE_LOW = bool(0)

t_State = enum('INIT', 'ODD', 'EVEN', 'DONE', encoding="one_hot")

 

def Odd_Even_Fsm(state, clk, rst_fsm, addr_left, muxsel_i, addr_sam, addr_rht):
    @always(clk.posedge, rst_fsm.negedge)
    def FSM():
        if rst_fsm == ACTIVE_LOW:
            addr_left.next = 0
            addr_sam.next = 1
            addr_rht.next = 2 
            state.next = t_State.INIT
        else:
            if state == t_State.INIT:
                
                state.next = t_State.ODD
            elif state == t_State.ODD:
                if (muxsel_i == 0):
                    if (addr_left < 254):
                        addr_left.next = addr_left + 2
                    if (addr_rht < 254):
                        addr_rht.next = addr_rht + 2
                    if (addr_sam <= 252):
                        addr_sam.next = addr_sam + 2
                    else:
                        addr_left.next = 1
                        addr_sam.next = 2
                        addr_rht.next = 3 
                        state.next = t_State.EVEN
            elif state == t_State.EVEN:
                if (muxsel_i == 0):
                    if (addr_left < 253):
                        addr_left.next = addr_left + 2
                    if (addr_rht <= 254):
                        addr_rht.next = addr_rht + 2
                    if (addr_sam < 254):
                        addr_sam.next = addr_sam + 2
                    else:
                        state.next = t_State.DONE

            elif state == t_State.DONE:
                 
                state.next = t_State.DONE
            
            else:
                raise ValueError("Undefined state")
            
    return FSM

def tb(state, clk, rst_fsm, addr_left, muxsel_i, addr_sam, addr_rht):
    instance_1 = Odd_Even_Fsm (state, clk, rst_fsm, addr_left, muxsel_i, addr_sam, addr_rht)
    @always(delay(10))
    def clkgen():
        clk.next = not clk
    @instance
    def stimulus():
        muxsel_i.next = 0
        yield clk.posedge
        rst_fsm.next = 1
        yield clk.posedge
        print ("%d muxsetl_i %d rst_fsm %d") % (now(), muxsel_i, rst_fsm)
        for i in range(4):
            yield clk.posedge
        for i in range(10000):
 
            yield clk.posedge
        print ("%d ") % (now())
        raise StopSimulation
    return instances()

def main():

    addr_left = Signal(intbv(0)[8:])
    addr_1 = Signal(intbv(0)[8:])
    addr_sam = Signal(intbv(0)[8:])
 
    addr_rht = Signal(intbv(0)[8:])
    muxsel_i = Signal(bool(0))
    clk = Signal(bool(0))
    we_1 = Signal(bool(0))
    rst_fsm = Signal(bool(1))
    state = Signal(t_State.INIT)
    
    toVerilog(Odd_Even_Fsm, state, clk, rst_fsm, addr_left, muxsel_i, addr_sam, addr_rht )
    toVHDL(Odd_Even_Fsm, state, clk, rst_fsm, addr_left, muxsel_i, addr_sam, addr_rht )
    '''
    tb_fsm = traceSignals(tb,state, clk, rst_fsm, addr_left, muxsel_i, addr_sam, addr_rht)
    sim = Simulation(tb_fsm)
    sim.run()
    ''' 

if __name__ == '__main__':
    main()
