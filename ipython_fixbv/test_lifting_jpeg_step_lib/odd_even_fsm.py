import os
path = os.path

from myhdl import *
from lift_step import lift_step
from signed2twoscomplement import signed2twoscomplement
from mux import mux_data
from ram import ram

from rd_pc import pc_read

from PIL import Image
W0 = 9
im = Image.open("../../lena_256.png")
pix = im.load()
w, h = im.size
m = list(im.getdata())
#print m.__sizeof__()
m = [m[i:i+im.size[0]] for i in range(0, len(m), im.size[0])]
#print m
print m[0][0], m[1][0],m[2][0],m[3][0],m[4][0],m[5][0],m[6][0]
print m[248][0],m[249][0], m[250][0],m[251][0],m[252][0],m[253][0],m[254][0]
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

 
z = Signal(intbv(0)[W0:])
read_pc_i = Signal(bool(0))
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
do_first = Signal(bool(0))
end_of_col = Signal(bool(0))
'''data from usb hostio'''
pc_data_in = Signal(intbv(0)[2:])
pc_data_rdy = Signal(intbv(0)[2:])

data_pc_in  = Signal(bool(0))

addr_in_toLift_Step = Signal(intbv(0)[8:])

t_State = enum('INIT', 'ODD_L', 'ODD_S', 'ODD_R', 'RD_RAM_LF', 'RD_RAM_SA', 'RD_RAM_RT', 'LIFT', 'LIFT_EXE', 'LIFT_RD', 'LIFT_WR', 'LIFT_DEL1', 'LIFT_DEL2', 'LIFT_DEL3', 'EVEN_L', 'EVEN_S', 'EVEN_R',   'DONE', encoding="one_hot")
state = Signal(t_State.INIT)

# INIT, READ_DATA, DONE = range(3)

ACTIVE_LOW = bool(0)



 

def Odd_Even_Fsm(state, clk, rst_fsm, addr_left, muxsel_i, addr_sam, addr_rht, muxaddrsel, we_1, dout, left_i, sam_i, right_i, do_first, x, z, flgs_i, update_i, res_o, update_o, end_of_col  ):
    @always(clk.posedge, rst_fsm.negedge)
    def FSM():
        if rst_fsm == ACTIVE_LOW:
            addr_left.next = 0
            addr_sam.next = 1
            addr_rht.next = 2
            do_first.next = 0
            flgs_i.next = 7
            end_of_col.next = 0 
            state.next = t_State.INIT
        else:
            if state == t_State.INIT:
                
                state.next = t_State.ODD_L
            elif state == t_State.ODD_L:
                if (muxsel_i == 0):
                    if ((addr_left < 254) ):
                        if (addr_left == 0) and (do_first == 0):
                            ''' do_first goes hi to execute first location'''
                            #do_first.next = 1
                            addr_left.next = 0
                            muxaddrsel.next = 0
                            we_1.next = 0
                            state.next = t_State.RD_RAM_LF

                        else:
			    
			    addr_left.next = addr_left + 2
                            muxaddrsel.next = 0
                            we_1.next = 0
                            state.next = t_State.RD_RAM_LF
                    
            elif state == t_State.ODD_S:
                    if (addr_sam < 254) :
                        if (addr_sam == 1)and (do_first == 0):
                            addr_sam.next = 1
                            muxaddrsel.next = 1
                            we_1.next = 0
                            state.next = t_State.RD_RAM_SA
                        else:
                            addr_sam.next = addr_sam + 2
                            muxaddrsel.next = 1
                            we_1.next = 0
                            state.next = t_State.RD_RAM_SA
            elif state == t_State.ODD_R:
                if (muxsel_i == 0):
                     if (addr_rht < 254):
                        if (addr_rht == 2)and (do_first == 0):
                            do_first.next = 1
                            addr_rht.next = 2
                            muxaddrsel.next = 2
                            we_1.next = 0
                            state.next = t_State.RD_RAM_RT
                        else:
                            addr_rht.next = addr_rht + 2
                            muxaddrsel.next = 2
                            we_1.next = 0
                            state.next = t_State.RD_RAM_RT
                     else:
                        addr_left.next = 1
                        addr_sam.next = 2
                        addr_rht.next = 3
                        do_first.next = 0
                        flgs_i.next = 6 
                        state.next = t_State.EVEN_L 
            elif state == t_State.EVEN_L:
                if (muxsel_i == 0):
                    if ((addr_left < 254)):
                        if (addr_left == 1)and (do_first == 0):

                            ''' do_first goes hi to execute first location'''
                            #do_first.next = 1
                            addr_left.next = 1
                            muxaddrsel.next = 0
                            we_1.next = 0
                            state.next = t_State.RD_RAM_LF

                        else:
			    
			    addr_left.next = addr_left + 2
                            muxaddrsel.next = 0
                            we_1.next = 0
                            state.next = t_State.RD_RAM_LF
 
            elif state == t_State.EVEN_S:
                    if (addr_sam < 254):
                        if (addr_sam == 2)and (do_first == 0):
                            addr_sam.next = 2
                            muxaddrsel.next = 1
                            we_1.next = 0
                            state.next = t_State.RD_RAM_SA
                        else:
                            addr_sam.next = addr_sam + 2
                            muxaddrsel.next = 1
                            we_1.next = 0
                            state.next = t_State.RD_RAM_SA
                    else:
                        addr_left.next = 1
                        addr_sam.next = 2
                        addr_rht.next = 3 
                        state.next = t_State.DONE 
            elif state == t_State.EVEN_R:

                if (muxsel_i == 0):
                     if (addr_rht < 254):
                        if (addr_rht == 3)and (do_first == 0):
                            do_first.next = 1
                            addr_rht.next = 3
                            muxaddrsel.next = 2
                            we_1.next = 0
                            state.next = t_State.RD_RAM_RT
                        else:
                            addr_rht.next = addr_rht + 2
                            muxaddrsel.next = 2
                            we_1.next = 0
                            state.next = t_State.RD_RAM_RT
                     else:
                        addr_left.next = 1
                        addr_sam.next = 2
                        addr_rht.next = 3 
                        state.next = t_State.DONE 
            elif state == t_State.DONE:
                end_of_col.next = 1 
                state.next = t_State.DONE
            elif state == t_State.RD_RAM_LF:
                left_i.next = dout
                if (flgs_i == 6):
                    state.next = t_State.EVEN_S
                else:
                    state.next = t_State.ODD_S
            elif state == t_State.RD_RAM_SA:
                sam_i.next = dout
                if (flgs_i == 6):
                    state.next = t_State.EVEN_R
                else:
                    state.next = t_State.ODD_R
            elif state == t_State.RD_RAM_RT:
                right_i.next = dout
                
                    
                state.next = t_State.LIFT
 
            elif state == t_State.LIFT:
                '''setting addr to sam'''
                #flgs_i.next = 7
                update_i.next = 1
                we_1.next = 1 
                muxaddrsel.next = 1 
               
                state.next = t_State.LIFT_EXE
            elif state == t_State.LIFT_EXE:
                
		muxaddrsel.next = 1       
                state.next = t_State.LIFT_RD
            elif state == t_State.LIFT_RD:
                muxaddrsel.next = 1
		x.next = res_o[W0:]       
                state.next = t_State.LIFT_WR
            elif state == t_State.LIFT_WR:
                muxaddrsel.next = 1
                #addr_sam.next = addr_sam + 1
		update_i.next = 0
                #we_1.next = 0        
                state.next = t_State.LIFT_DEL1
            elif state == t_State.LIFT_DEL1:
                muxaddrsel.next = 1
                #addr_sam.next = addr_sam + 1
		#update_i.next = 0
                #we_1.next = 0        
                state.next = t_State.LIFT_DEL2
            elif state == t_State.LIFT_DEL2:
                muxaddrsel.next = 1
                #addr_sam.next = addr_sam + 1
		#update_i.next = 0
                #we_1.next = 0
      
                state.next = t_State.LIFT_DEL3
            elif state == t_State.LIFT_DEL3:
                muxaddrsel.next = 1
                #addr_sam.next = addr_sam + 1
		#update_i.next = 0
                we_1.next = 0        
                state.next = t_State.ODD_L

            else:
                raise ValueError("Undefined state")
            
    return FSM
def top_odd_even(state, clk, rst_fsm, addr_left, muxsel_i, addr_sam, addr_rht, muxaddrsel, we_1, dout, left_i, sam_i, right_i, do_first, x, z, flgs_i, update_i, res_o, update_o, end_of_col ):

    instance_Odd_Even_Fsm = Odd_Even_Fsm (state, clk, rst_fsm, addr_left, muxsel_i, addr_sam, addr_rht, muxaddrsel, we_1, dout, left_i, sam_i, right_i, do_first, x, z, flgs_i, update_i, res_o, update_o, end_of_col, data_in, toLift_Step, addr_in, addr_in_toLift_Step, we_in)
    instance_ram = ram(dout, din, addr, we, clk)
    instance_mux_data =  mux_data(z, din, data_in, we_1, we, we_in, addr, addr_in, muxsel_i, muxaddrsel, addr_left, addr_sam, addr_rht)
    instance_signed2twoscomplement = signed2twoscomplement(clk, x, z)
    instance_lift_step = lift_step(left_i, sam_i, right_i, flgs_i, update_i, clk, res_o, update_o)
    instance_pd_read = pc_read(clk, data_in, toLift_Step, we_in, addr_in, muxsel_i, datactn_in, datactn, pc_data_in, pc_data_rdy ) 
    return instances()

def tb(state, clk, rst_fsm, addr_left, muxsel_i, addr_sam, addr_rht, muxaddrsel, we_1, dout, left_i, sam_i, right_i, do_first, x, z, flgs_i, update_i, res_o, update_o, end_of_col, read_pc_i, data_in, toLift_Step, addr_in, addr_in_toLift_Step, we_in):

    instance_Odd_Even_Fsm = Odd_Even_Fsm (state, clk, rst_fsm, addr_left, muxsel_i, addr_sam, addr_rht, muxaddrsel, we_1, dout, left_i, sam_i, right_i, do_first, x, z, flgs_i, update_i, res_o, update_o, end_of_col)

    instance_ram = ram(dout, din, addr, we, clk)

    instance_mux_data =  mux_data(z, din, data_in, we_1, we, we_in, addr, addr_in, muxsel_i, muxaddrsel, addr_left, addr_sam, addr_rht)

    instance_signed2twoscomplement = signed2twoscomplement(clk, x, z)

    instance_lift_step = lift_step(left_i, sam_i, right_i, flgs_i, update_i, clk, res_o, update_o)

    instance_pc_read = pc_read(clk,data_in,toLift_Step,addr_in,addr_in_toLift_Step, read_pc_i,muxsel_i, pc_data_in, pc_data_rdy, we_in)

    @always(delay(10))
    def clkgen():
        clk.next = not clk

    @instance
    def stimulus():
        rst_fsm.next = 0
        yield clk.posedge
        pc_data_rdy.next = 3
        yield clk.posedge
        muxsel_i.next = 1
        yield clk.posedge
        read_pc_i.next = 1
        yield clk.posedge
        k = 0
        for j in range(256):
            #addr_in.next = j
            #yield clk.posedge
            addr_in_toLift_Step.next = j
	    toLift_Step.next = m[addr_in][k]
            yield clk.posedge
        for i in range(4):

            pc_data_rdy.next = 2
            yield clk.posedge
            muxsel_i.next = 0
            yield clk.posedge
            read_pc_i.next = 0
            yield clk.posedge         
            rst_fsm.next = 1
            yield clk.posedge
            print ("%d muxsel_i %d rst_fsm %d") % (now(), muxsel_i, rst_fsm)
        
        for i in range(10000):
            print ("time %d flgs %d left %d sam %d right %d ") % (now(), flgs_i, left_i, sam_i, right_i)
            print ("time %d addr %d din %d we %d ") % (now(), addr, din, we)   
            yield clk.posedge
        print ("%d ") % (now())
        raise StopSimulation
    return instances()

def main():

    '''    
    toVerilog(Odd_Even_Fsm, state, clk, rst_fsm, addr_left, muxsel_i, addr_sam, addr_rht, muxaddrsel, we_1, dout, left_i, sam_i, right_i, do_first, x, z, flgs_i, update_i, res_o, update_o, end_of_col)
    toVHDL(Odd_Even_Fsm, state, clk, rst_fsm, addr_left, muxsel_i, addr_sam, addr_rht, muxaddrsel, we_1, dout, left_i, sam_i, right_i, do_first, x, z, flgs_i, update_i, res_o, update_o, end_of_col)
    
    toVHDL(top_odd_even,state, clk, rst_fsm, addr_left, muxsel_i, addr_sam, addr_rht, muxaddrsel, we_1, dout, left_i, sam_i, right_i, do_first, x, z, flgs_i, update_i, res_o, update_o, end_of_col)
    '''
    tb_fsm = traceSignals(tb,state, clk, rst_fsm, addr_left, muxsel_i, addr_sam, addr_rht, muxaddrsel, we_1, dout, left_i, sam_i, right_i, do_first, x, z, flgs_i, update_i, res_o, update_o, end_of_col, read_pc_i, data_in, toLift_Step, addr_in, addr_in_toLift_Step, we_in)
    sim = Simulation(tb_fsm)
    sim.run()
    
    

if __name__ == '__main__':
    main()
