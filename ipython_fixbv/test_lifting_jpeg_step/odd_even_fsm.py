import os
path = os.path

from myhdl import *
from signed2twoscomplement import signed2twoscomplement
from mux import mux_data
from ram import ram
from lift_step import lift_step
W0 = 9
dout = Signal(intbv(0)[W0:])
din = Signal(intbv(0)[W0:])
addr = Signal(intbv(0)[8:])

we = Signal(bool(0))
clk = Signal(bool(0))
we_in = Signal(bool(0))
we_1 = Signal(bool(0))
addr_in = Signal(intbv(0)[8:])
 
toLift_Step = Signal(intbv(0)[W0:])
data_in = Signal(intbv(0)[W0:])

pc_data_in = Signal(intbv(0)[2:])
pc_data_rdy = Signal(intbv(0)[2:])

datactn_in = Signal(intbv(0)[8:])
datactn = Signal(intbv(0)[8:])
z = Signal(intbv(0)[W0:])
muxsel_i = Signal(bool(0))
muxaddrsel = Signal(intbv(0)[2:])

x = Signal(intbv(0, min= -(2**(W0)) ,max= (2**(W0))))
res_o = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
left_i = Signal(intbv(0)[W0:])
right_i = Signal(intbv(0)[W0:])
sam_i = Signal(intbv(0)[W0:])
flgs_i = Signal(intbv(0)[4:])

update_i = Signal(bool(0))
update_o = Signal(bool(0))

SOF = Signal(bool(0))
syncFlag = Signal(bool(0))
rst_fsm = Signal(bool(1))

addr_left = Signal(intbv(0)[8:])
addr_sam = Signal(intbv(0)[8:])
addr_rht = Signal(intbv(0)[8:])
t_State = enum('INIT', 'ODD', 'EVEN', 'RD_RAM_LF', 'RD_RAM_SA', 'RD_RAM_RT', 'DONE', encoding="one_hot")
state = Signal(t_State.INIT)

# INIT, READ_DATA, DONE = range(3)

ACTIVE_LOW = bool(0)



 

def Odd_Even_Fsm(state, clk, rst_fsm, addr_left, muxsel_i, addr_sam, addr_rht, muxaddrsel, we_1, dout, left_i, sam_i, right_i  ):
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
                        muxaddrsel.next = 0
                        we_1.next = 0
                        state.next = t_State.RD_RAM_LF
                    if (addr_rht < 254):
                        addr_rht.next = addr_rht + 2
                        muxaddrsel.next = 2
                        we_1.next = 0
                        state.next = t_State.RD_RAM_RT                        
                    if (addr_sam <= 252):
                        addr_sam.next = addr_sam + 2
                        muxaddrsel.next = 1
                        we_1.next = 0
                        state.next = t_State.RD_RAM_SA                        
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
            elif state == t_State.RD_RAM_LF:
                left_i.next = dout
                state.next = t_State.ODD
            elif state == t_State.RD_RAM_SA:
                sam_i.next = dout
                state.next = t_State.ODD
            elif state == t_State.RD_RAM_RT:
                right_i.next = dout
                state.next = t_State.ODD
                
            else:
                raise ValueError("Undefined state")
            
    return FSM

def tb(state, clk, rst_fsm, addr_left, muxsel_i, addr_sam, addr_rht, muxaddrsel, we_1, dout, left_i, sam_i, right_i):
    instance_lift_step = lift_step(left_i, sam_i, right_i, flgs_i, update_i, clk, res_o, update_o)
    instance_Odd_Even_Fsm = Odd_Even_Fsm (state, clk, rst_fsm, addr_left, muxsel_i, addr_sam, addr_rht, muxaddrsel, we_1, dout, left_i, sam_i, right_i)
    instance_ram = ram(dout, din, addr, we, clk)
    instance_mux_data =  mux_data(z, din, data_in, we_1, we, we_in, addr, addr_in, muxsel_i, muxaddrsel, addr_left, addr_sam, addr_rht)

    @always(delay(10))
    def clkgen():
        clk.next = not clk
    @instance
    def stimulus():
        muxsel_i.next = 0
        rst_fsm.next = 0
        yield clk.posedge
        for i in range(4):
            yield clk.posedge
        rst_fsm.next = 1
        yield clk.posedge
        for i in range(4):
            yield clk.posedge
        print ("%d muxsel_i %d rst_fsm %d") % (now(), muxsel_i, rst_fsm)
        
        for i in range(10000):
 
            yield clk.posedge
        print ("%d ") % (now())
        raise StopSimulation
    return instances()

def main():
    '''
    W0 = 9
    addr_left = Signal(intbv(0)[8:])
    addr_1 = Signal(intbv(0)[8:])
    addr_sam = Signal(intbv(0)[8:])
 
    addr_rht = Signal(intbv(0)[8:])
    muxsel_i = Signal(bool(0))
    muxaddrsel = Signal(intbv(0)[2:])
    clk = Signal(bool(0))
    we_1 = Signal(bool(0))
    dout = Signal(intbv(0)[W0:])
    rst_fsm = Signal(bool(1))
    state = Signal(t_State.INIT)
    we_1 = Signal(bool(0))
    x = Signal(intbv(0, min= -(2**(W0)) ,max= (2**(W0))))
    res_o = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
    left_i = Signal(intbv(0)[W0:])
    right_i = Signal(intbv(0)[W0:])
    sam_i = Signal(intbv(0)[W0:])
    flgs_i = Signal(intbv(0)[4:])

    update_i = Signal(bool(0))
    '''
    '''
    toVerilog(Odd_Even_Fsm, state, clk, rst_fsm, addr_left, muxsel_i, addr_sam, addr_rht, muxaddrsel, we_1, dout, left_i, sam_i, right_i)
    toVHDL(Odd_Even_Fsm, state, clk, rst_fsm, addr_left, muxsel_i, addr_sam, addr_rht, muxaddrsel, we_1, dout, left_i, sam_i, right_i)
    '''
    tb_fsm = traceSignals(tb,state, clk, rst_fsm, addr_left, muxsel_i, addr_sam, addr_rht, muxaddrsel, we_1, dout, left_i, sam_i, right_i)
    sim = Simulation(tb_fsm)
    sim.run()
     

if __name__ == '__main__':
    main()
