from myhdl import *
DATA_WIDTH = 32768
JPEG_RAM_ADDR = 9
ACTIVE_LOW = bool(0)
rst = Signal(bool(0))
rst_file_in = Signal(bool(1))
eog = Signal(bool(0))
y = Signal(intbv(0)[16:])
clk_fast = Signal(bool(0))
wr_s = Signal(bool(0))
y = Signal(intbv(0)[16:])
dataToRam_r = Signal(intbv(0)[16:])
sel = Signal(bool(0))
addr_r = Signal(intbv(0)[JPEG_RAM_ADDR:])
addr_r1 = Signal(intbv(0)[JPEG_RAM_ADDR:])
addr_r2 = Signal(intbv(0)[JPEG_RAM_ADDR:])

sig_in = Signal(intbv(0)[52:])
noupdate_s = Signal(bool(0))
res_s = Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))

jp_lf = Signal(intbv(0)[16:])
jp_sa = Signal(intbv(0)[16:])
jp_rh = Signal(intbv(0)[16:])
jp_flgs = Signal(intbv(0)[4:])
dataFromRam_s = Signal(intbv(0)[16:])
din_res = Signal(intbv(0)[16:])
dout_res = Signal(intbv(0)[16:])
offset = Signal(intbv(0)[JPEG_RAM_ADDR:])
reset_n = Signal(bool(1))
we_res = Signal(bool(1))
addr_not_reached = Signal(bool(1))

rdy = Signal(bool(0))
reset_fsm_r = Signal(bool(1))
addr_rom = Signal(intbv(0)[JPEG_RAM_ADDR:])
addr_rom_r = Signal(intbv(0)[JPEG_RAM_ADDR:])
offset = Signal(intbv(0)[JPEG_RAM_ADDR:])
offset_r = Signal(intbv(0)[JPEG_RAM_ADDR:])
t_State = enum('INIT', 'ODD_SA', 'EVEN_SA', 'TR_RES', 'TR_INIT', 'TRAN_RAM', encoding="one_hot")
state_r = Signal(t_State.ODD_SA)
state_x = Signal(t_State.ODD_SA)
addr_res = Signal(intbv(0)[JPEG_RAM_ADDR:])
addr_res_r = Signal(intbv(0)[JPEG_RAM_ADDR:])

reset_n = Signal(bool(1))

def read_file_sdram(clk_fast, rst, eog, wr_s, rst_file_in, addr_r, dataToRam_r, y):
	@always(clk_fast.negedge)
	def file_rd():
		if (rst_file_in == 0):
			rst.next = 1
			addr_r.next = 0
			wr_s.next = 1
		else:
			if (rst == 1):
				rst.next = 0
			elif (eog == 0):
				if (addr_r <= 256):
					dataToRam_r.next = y
					addr_r.next = addr_r + 1
			else:
				wr_s.next = 0
	return file_rd
def mux2(addr_r, addr_r1, addr_r2, sel):
    @always_comb
    def muxLogic():
        addr_r.next = addr_r1
        if (sel == 1):
            addr_r.next = addr_r2
    return muxLogic

def jpegFsm( state_r, state_x, reset_fsm_r, addr_res, addr_res_r, offset, offset_r,  jp_flgs, reset_n, rdy,  noupdate_s, addr_not_reached ):
	offset.next = offset_r
	addr_res.next = addr_res_r
	state_x.next = state_r
	@always_comb
	def Fsm():
		state_x.next = state_r
		if reset_fsm_r == ACTIVE_LOW:
			offset.next = offset_r
			addr_res.next = addr_res_r
			state_x.next = t_State.INIT
		else:
			if state_r == t_State.INIT:
				reset_n.next = 1
				rdy.next = 0
				offset.next = 0
				addr_res.next = 0
				state_x.next = t_State.EVEN_SA
			elif state_r == t_State.ODD_SA:
				rdy.next = 1
				reset_n.next = 0
				jp_flgs.next = 6
				offset.next = offset_r
				if (offset_r <= 250):
					if ((noupdate_s != 1) and (addr_not_reached)):
						offset.next = offset_r + 2
						addr_res.next = addr_res_r + 2
						rdy.next = 1
						reset_n.next = 1
				else:
					"""Setting up for next state"""
					reset_n.next = 1
					rdy.next = 1
					offset.next = 1
					addr_res.next = 2
					state_x.next = t_State.INIT
			elif state_r == t_State.EVEN_SA:
				rdy.next = 1
				reset_n.next = 0
				jp_flgs.next = 7
				offset.next = offset_r
				if (offset_r <= 252):
					if ((noupdate_s != 1) and (addr_not_reached)):
						offset.next = offset_r + 2
						addr_res.next = addr_res_r + 2
						rdy.next = 1
						reset_n.next = 1
				else:
					"""Need to setup for next state"""
					rdy.next = 1
					reset_n.next = 1
					rdy.next = 0
					offset.next = 0
					addr_res.next = 0
					#addr_rom.next = 0
					state_x.next = t_State.TR_RES
			elif state_r == t_State.TR_RES:
				offset.next = offset_r
				addr_res.next = 0
				state_x.next = t_State.TR_INIT
			elif state_r == t_State.TR_INIT:
				reset_n.next = 1
				rdy.next = 0
				offset.next = 0
				addr_res.next = 0
				 
				state_x.next = t_State.ODD_SA
			elif state_r == t_State.TRAN_RAM:
				state_x.next = t_State.INIT
			else:
				raise ValueError("Undefined state")
	return Fsm
def jpegfsmupdate(clk_fast, offset, offset_r, state_r, state_x, addr_res, addr_res_r):
	@always(clk_fast.posedge)
	def fsmupdate():
		offset_r.next = offset
		state_r.next = state_x
		addr_res_r.next = addr_res
	return fsmupdate
def jpeg_process(clk_fast, sig_in,  noupdate_s, res_s):
    left_s = sig_in(16,0)
    sam_s = sig_in(32,16)
    right_s = sig_in(48,32)
    even_odd_s = sig_in(48)
    fwd_inv_s = sig_in(49)
    updated_s = sig_in(50)
    dum_s = sig_in(52)
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
                    res_s.next =  sam_s + ((left_s +  right_s + 2)>>2)
                else:
                    res_s.next =  sam_s - ((left_s +  right_s + 2)>>2)
        else:
            noupdate_s.next = 1
    return jpeg
def jpegsdram_rd(clk_fast, offset, dataFromRam_s, jp_lf, jp_sa, jp_rh, jp_flgs, reset_n, addr_r, addr_not_reached):
    even = jp_flgs(0)
    @always(clk_fast.posedge)
    def sdram_rd():
        
        
        if (reset_n):
            jp_lf.next = 0
            jp_sa.next = 0
            jp_rh.next = 0
            addr_not_reached.next = 0
            #if jp_flgs 6 odd jp_flgs 7 even_odd
            if (even  == 1):           
                addr_r.next = 1 + offset
            else:
                addr_r.next = 0 + offset
        else:
            if (even):
                    if (addr_r == (1 + offset) ):
                        jp_lf.next = dataFromRam_s
                        addr_r.next = addr_r + 1
                    else:
                        if (addr_r == (2 + offset)):
                            jp_sa.next = dataFromRam_s
                            addr_r.next = addr_r + 1
                        else:
                            if (addr_r == (3 + offset)):
                                jp_rh.next = dataFromRam_s
                                addr_not_reached.next = 1
            else:
                if (addr_r == (0 + offset)):
                    jp_lf.next = dataFromRam_s
                    addr_r.next = addr_r + 1
                else:
                    if (addr_r == (1 + offset)):
                        jp_sa.next = dataFromRam_s
                        addr_r.next = addr_r + 1
                    else:
                        if (addr_r == (2 + offset)):
                            jp_rh.next = dataFromRam_s
                            addr_not_reached.next = 1
    return sdram_rd
def jpegram2sig(jp_lf, jp_sa ,jp_rh, jp_flgs, rdy, addr_not_reached,  sig_in):
    """Combines 3 16 bit plus 4 flags into single value """
    @always_comb
    def ram2sig():
        if rdy:
            if addr_not_reached:
                sig_in.next = concat(jp_flgs, jp_rh, jp_sa, jp_lf)
            else:
                sig_in.next = 0
        else:
            sig_in.next = 0
    return ram2sig
#def test_instances(clk_fast, rst, eog, wr_s, rst_file_in, addr_r, dataToRam_r, y, addr_r1, addr_r2, sel, sig_in, noupdate_s, res_s, offset, dataFromRam_s, jp_lf, jp_sa, jp_rh, jp_flgs, reset_n, addr_not_reached, rdy, state_r, state_x, reset_fsm_r, addr_res, addr_res_r, offset_r, addr_rom, addr_rom_r):
def ramres(dout_res, din_res, addr_res, we_res, clk_fast, depth=256):
    """  Ram model """
    
    mem = [Signal(intbv(0)[16:]) for i in range(depth)]
    
    @always(clk_fast.posedge)
    def write():
        if we_res:
            mem[addr_res].next = din_res
                
    @always_comb
    def read():
        dout_res.next = mem[addr_res]

    return write, read
def jpeg_top(clk_fast, rst, eog, wr_s, rst_file_in, addr_r, dataToRam_r, y, addr_r1, addr_r2, sel, sig_in, noupdate_s, res_s, offset, dataFromRam_s, jp_lf, jp_sa, jp_rh, jp_flgs, reset_n, addr_not_reached, rdy, state_r, state_x, reset_fsm_r, addr_res, addr_res_r, offset_r, dout_res, din_res, we_res):
    instance_1 = read_file_sdram(clk_fast, rst, eog, wr_s, rst_file_in, addr_r1, dataToRam_r, y)
    instance_2 = mux2(addr_r, addr_r1, addr_r2, sel)
    instance_3 = jpeg_process(clk_fast, sig_in,  noupdate_s, res_s)
    instance_4 = jpegsdram_rd(clk_fast, offset, dataFromRam_s, jp_lf, jp_sa, jp_rh, jp_flgs, reset_n, addr_r2, addr_not_reached)
    instance_5 = jpegram2sig(jp_lf, jp_sa ,jp_rh, jp_flgs, rdy, addr_not_reached,  sig_in)
    instance_6 = jpegFsm(state_r, state_x, reset_fsm_r, addr_res, addr_res_r, offset, offset_r,  jp_flgs, reset_n, rdy,  noupdate_s, addr_not_reached )
    instance_7 = jpegfsmupdate(clk_fast, offset, offset_r, state_r, state_x, addr_res, addr_res_r )
    instance_8 = ramres(dout_res, din_res, addr_res, we_res, clk_fast, depth=256)
    return instance_1, instance_2, instance_3, instance_4, instance_5, instance_6, instance_7, instance_8

#toVHDL(read_file_sdram, clk_fast, rst, eog, wr_s, rst_file_in, addr_r, dataToRam_r, y)
#toVHDL(mux2, addr_r, addr_r1, addr_r2, sel)
#toVHDL(jpeg_process, clk_fast, sig_in,  noupdate_s, res_s)
#toVHDL(jpegsdram_rd, clk_fast, offset, dataFromRam_s, jp_lf, jp_sa, jp_rh, jp_flgs, reset_n, addr_r, addr_not_reached)
#toVHDL(jpegram2sig, jp_lf, jp_sa ,jp_rh, jp_flgs, rdy, addr_not_reached,  sig_in)
#toVHDL(jpegfsmupdate, clk_fast, offset, offset_r, state_r, state_x, addr_res, addr_res_r )
#toVHDL(jpegFsm, state_r, state_x, reset_fsm_r, addr_res, addr_res_r, offset, offset_r,  jp_flgs, reset_n, rdy,  noupdate_s, addr_not_reached )
toVHDL(jpeg_top, clk_fast, rst, eog, wr_s, rst_file_in, addr_r, dataToRam_r, y, addr_r1, addr_r2, sel, sig_in,  noupdate_s, res_s, offset, dataFromRam_s, jp_lf, jp_sa, jp_rh, jp_flgs, reset_n, addr_not_reached, rdy, state_r, state_x, reset_fsm_r, addr_res, addr_res_r, offset_r, dout_res, din_res, we_res)