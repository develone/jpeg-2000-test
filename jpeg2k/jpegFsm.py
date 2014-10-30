from myhdl import *

 
 
RAM_ADDR = 9
ROM_ADDR = 12
ACTIVE_LOW = bool(0)
t_State = enum('ODD_SA', 'EVEN_SA', 'TRAN_RAM', encoding="one_hot")
state_r = Signal(t_State.ODD_SA)
clk_fast = Signal(bool(0))
jp_flgs = Signal(intbv(0)[4:])
addr_res = Signal(intbv(0)[RAM_ADDR:])
offset = Signal(intbv(0)[ROM_ADDR:])
offset_r = Signal(intbv(0)[ROM_ADDR:])
reset_fsm_r = Signal(bool(1))
rdy = Signal(bool(0)) 
reset_n = Signal(bool(1))
sig_in = Signal(intbv(0)[52:])
sig_out = Signal(intbv(0)[52:])

offset_i = Signal(intbv(0)[ROM_ADDR:])
offset_o = Signal(intbv(0)[ROM_ADDR:])
def jpegFsm( state_r, reset_fsm_r, addr_res,  offset, offset_r,  jp_flgs, reset_n, rdy ):
    #addr_rom = addr_rom
    addr_res = addr_res
    #offset_x = offset_r
    
    jp_flgs = jp_flgs
    state_x = state_r
 
    @always_comb
    def FSM():

         
        if reset_fsm_r == ACTIVE_LOW:
            """The start up value for reset_n is 1 |__
            Need to added after 70 ns to the line below
            which will total 80 ns 
            cut after 70 ns and paste in the line below  """
             
            addr_res.next = offset_r + 1
            reset_n.next = 0
            state_x.next = t_State.ODD_SA
 
        else:
 
            if state_r == t_State.ODD_SA:
                rdy.next = 1
                jp_flgs.next = 6
                
                offset.next = offset_r
                """ The start up value for reset_n is 1 |__
                Need to added after 70 ns to the line below
                which will total 80 ns
                rdy needs to go hi 30 ns after reset_n goes lo
                rdy needs go lo 10 ns before reset_n goes hi
                cut after 70 ns and paste in the line below """
                reset_n.next = 1
                """The start up value for rdy is 0 __|
                rdy needs to go hi 10 ns after reset_n goes lo
                rdy needs go lo 10 ns before reset_n goes hi
                cut after 60 ns and paste in the line below """
                rdy.next = 0
                
                state_x.next = t_State.ODD_SA
            elif state_r == t_State.EVEN_SA:
                jp_flgs.next = 7
                #offset.next = 1
                state_x.next = t_State.ODD_SA

            elif state_r == t_State.TRAN_RAM:
                 
                state_x.next = t_State.ODD_SA
            else:
                raise ValueError("Undefined state")
    return FSM
 
#toVHDL(jpegFsm, state_r, reset_fsm_r,  addr_res, offset, offset_r,  jp_flgs, reset_n, rdy )
#toVerilog(jpegFsm, state_r, reset_fsm_r, addr_res, offset, offset_r,  jp_flgs, reset_n, rdy )
def jprow(clk_fast,  offset_o,  offset_i  ):
        
        @always(clk_fast.posedge)
        def row_logic():
            row = 0
            if row <= 64 :             
                offset_o.next =  offset_i + 2
            else:
                row = 0
            #reset_fsm_o.next 
            #sig_o.next = sig_i
        return row_logic
toVHDL(jprow, clk_fast, offset_o,  offset_i )  
toVerilog(jprow, clk_fast, offset_o,  offset_i )            