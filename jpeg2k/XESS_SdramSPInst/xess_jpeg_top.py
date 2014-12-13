from myhdl import *

import fifo_down_if
import fifo_up_if

class fifo_upstream_interface(object):
    def __init__(self):
        self.wr_en  = Signal(bool(0))
        self.din    = Signal(intbv(0)[16:])
        #self.wr_clk_fast = Signal(bool(0))
        self.full   = Signal(bool(0)) 
        #self.rst    = Signal(bool(0))

#end class fifo_upstream_interface
    
def fifo_up_if_ex(clk_fast, rst, din, wr_en, full): #rst is asynch, all other
                                               #signals are synchronous
    @always_seq(clk_fast.posedge, reset=rst)
    def fifo_wr():
        if( full==False and wr_en==True):
            din.next = din
        #How to assert full signal???
        #Temporarily tied to 0        
        full.next = False      
    return fifo_wr
class fifo_downstream_interface(object):
    def __init__(self):
        self.rd_en  = Signal(bool(0))
        self.dout    = Signal(intbv(0)[16:])
        self.empty   = Signal(bool(0)) 

#end class fifo_downstream_interface
    
def fifo_down_if_ex(clk_fast, rst, dout, rd_en, empty): #rst is asynch, all other
                                               #signals are synchronous
    @always_seq(clk_fast.posedge, reset=rst)
    def fifo_rd():
        if( empty ==False and rd_en==True):
            dout.next = dout
        #How to assert empty signal???
        #Temporarily tied to 0        
        empty.next = False      
    return fifo_rd
def test():
    clk_fast = Signal(bool(0))
    rst = ResetSignal(0,active=1,async=True) #Xilinx spec didn't mention
                                             #specifically about reset
                                             #polarity
                                             
    up_interface = fifo_up_if.fifo_upstream_interface() #defining signals for the fifo
                                             #upstream interface
    def _test():
        #instantiating dut
        dut = fifo_up_if.fifo_up_if_ex(clk_fast,
                            rst,
                            up_interface.din,
                            up_interface.wr_en,
                            up_interface.full
                            )
                        
        @always(delay(5))
        def clk_fast_driver():
            clk_fast.next = not clk_fast
        
        
        @instance
        def tb_stim():
            rst.next = rst.active
            yield delay(20)
            rst.next = not rst.active
            yield delay(20)
            yield clk_fast.posedge
            
            for i in range(50):
                up_interface.wr_en.next = True
                up_interface.din.next = i
                yield clk_fast.posedge
                up_interface.wr_en.next = False
                yield clk_fast.posedge    
	    
	    raise StopSimulation	
        
        return dut, clk_fast_driver, tb_stim

    #Simulation(traceSignals(_test)).run()
clk_fast = Signal(bool(0))
rst = ResetSignal(0,active=1,async=True)
up_interface = fifo_up_if.fifo_upstream_interface()
dn_interface = fifo_down_if.fifo_downstream_interface()


def fifos():
   
    #print instance_13, instance_14
    instance_13 = fifo_up_if_ex(clk_fast,rst,up_interface.din,up_interface.wr_en,up_interface.full)        
    instance_14 = fifo_down_if_ex(clk_fast, rst, dn_interface.dout, dn_interface.rd_en, dn_interface.empty)
    print instance_13, instance_14
    return instance_13, instance_14
 
#toVHDL(fifos)
def xx(up_interface, dn_interface, clk_fast, rst ):
    #print "in xx"
    #print up_interface, dn_interface
    #print dn_interface.dout, dn_interface.rd_en, dn_interface.empty
    #toVHDL(fifo_up_if_ex, clk_fast,rst,up_interface.din,up_interface.wr_en,up_interface.full)
    instance_14 = fifo_down_if_ex(clk_fast, rst, dn_interface.dout, dn_interface.rd_en, dn_interface.empty)
    instance_13 = fifo_up_if_ex(clk_fast,rst,up_interface.din,up_interface.wr_en,up_interface.full)
    #toVHDL(fifo_down_if_ex, clk_fast, rst, dn_interface.dout, dn_interface.rd_en, dn_interface.empty)
    return instance_13, instance_14
#xx(up_interface, dn_interface, clk_fast, rst)
#toVHDL(xx, clk_fast, rst, dn_interface.dout, dn_interface.rd_en, dn_interface.empty)
reset_dly_c = 10
DATA_WIDTH = 32768
JPEG_RAM_ADDR = 23
JPEG_RES_RAM_ADDR = 9
ROW_NUM = 4
ACTIVE_LOW = bool(0)
NO = bool(0)
YES = bool(1)
#rst = Signal(bool(0))
rst_file_in = Signal(bool(1))
eog = Signal(bool(0))
y = Signal(intbv(0)[16:])
#clk_fast = Signal(bool(0))
rd_s = Signal(bool(0))
wr_s = Signal(bool(0))
wr_s1 = Signal(bool(0))
wr_s2 = Signal(bool(0))
y = Signal(intbv(0)[16:])
dataToRam_r = Signal(intbv(0)[16:])
dataToRam_x = Signal(intbv(0)[16:])
dataFromRam_s = Signal(intbv(0)[16:])
dataFromRam_r = Signal(intbv(0)[16:])
dataFromRam_r1 = Signal(intbv(0)[16:])
dataFromRam_r2 = Signal(intbv(0)[16:])
dataFromRam_x = Signal(intbv(0)[16:])
 
sum_r = Signal(intbv(0)[16:])
sum_x = Signal(intbv(0)[16:])
dataToRam_r1 = Signal(intbv(0)[16:])
dataToRam_r2 = Signal(intbv(0)[16:])
muxsel = Signal(bool(0))
muxsel_r = Signal(bool(0))
muxsel_x = Signal(bool(0))
#muxsel_r = Signal(intbv(0)[3:])
sel = Signal(bool(0))
sel_row = Signal(bool(0))
sel_r = Signal(bool(0))
sel_tr = Signal(bool(0))
sel_row_r = Signal(bool(0))
col = Signal(intbv(0)[ROW_NUM:])
col_r = Signal(intbv(0)[ROW_NUM:])

index_r = Signal(intbv(0)[JPEG_RAM_ADDR:])
index = Signal(intbv(0)[JPEG_RAM_ADDR:])
addr_r = Signal(intbv(0)[JPEG_RAM_ADDR:])
addr_x = Signal(intbv(0)[JPEG_RAM_ADDR:])
addr_r1 = Signal(intbv(0)[JPEG_RAM_ADDR:])
addr_r2 = Signal(intbv(0)[JPEG_RAM_ADDR:])
addr_r3 = Signal(intbv(0)[JPEG_RAM_ADDR:])
addr_r4 = Signal(intbv(0)[JPEG_RAM_ADDR:])
sig_in = Signal(intbv(0)[52:])
sig_in1 = Signal(intbv(0)[52:])
sig_in2 = Signal(intbv(0)[52:])
noupdate_s = Signal(bool(0))
res_s = Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))

jp_lf = Signal(intbv(0)[16:])
jp_sa = Signal(intbv(0)[16:])
jp_rh = Signal(intbv(0)[16:])
jp_flgs = Signal(intbv(0)[4:])
jp_row_lf = Signal(intbv(0)[16:])
jp_row_sa = Signal(intbv(0)[16:])
jp_row_rh = Signal(intbv(0)[16:])
jp_row_flgs = Signal(intbv(0)[4:])
dataFromRam_s = Signal(intbv(0)[16:])
din_res_r = Signal(intbv(0)[16:])
dout_res_r = Signal(intbv(0)[16:])
dout_res_r1 = Signal(intbv(0)[16:])
dout_res_r2 = Signal(intbv(0)[16:])
din_res_x = Signal(intbv(0)[16:])
dout_res_x = Signal(intbv(0)[16:])
offset = Signal(intbv(0)[JPEG_RAM_ADDR:])
reset_col = Signal(bool(1))
reset_col_r = Signal(bool(1))
reset_row = Signal(bool(1))
reset_row_r = Signal(bool(1))
we_res = Signal(bool(1))
addr_not_reached = Signal(bool(1))
addr_not_reached1 = Signal(bool(1))
addr_not_reached2 = Signal(bool(1))
rdy = Signal(bool(0))
reset_ctn = Signal(intbv(0)[4:])
reset_fsm_r = Signal(bool(1))
pass1_done = Signal(bool(1))
pass1_done_r = Signal(bool(1))
addr_rom = Signal(intbv(0)[JPEG_RAM_ADDR:])
addr_rom_r = Signal(intbv(0)[JPEG_RAM_ADDR:])
offset = Signal(intbv(0)[JPEG_RAM_ADDR:])
offset_r = Signal(intbv(0)[JPEG_RAM_ADDR:])
#t_State = enum('INIT', 'ODD_SA', 'EVEN_SA','ODD_SA_COL', 'EVEN_SA_COL', 'TR_RES', 'TR_INIT', 'TRAN_RAM', 'DONE_PASS1', encoding="one_hot")
#t_State = enum('INIT', 'WRITE_DATA', 'READ_AND_SUM_DATA', 'DONE', encoding="one_hot")
t_State = enum('INIT', 'WRITE', 'READ_AND_SUM_DATA', 'CK_SDRAM_RD', 'CK_SDRAM_WR', 'ODD_SAMPLES', 'EVEN_SAMPLES', 'WR_DATA', 'INTERLACE', 'DONE', encoding="one_hot")
#print t_State, t_State.INIT
state_r = Signal(t_State.INIT)
state_x = Signal(t_State.INIT)
state = Signal(t_State.INIT)
even_odd_r = Signal(bool(0))
even_odd_x = Signal(bool(0))
#print  t_State.INIT, t_State.READ_AND_SUM_DATA, state_r, state_x
done_s = Signal(bool(0))
addr_res_x = Signal(intbv(0)[JPEG_RES_RAM_ADDR:])
addr_res_r = Signal(intbv(0)[JPEG_RES_RAM_ADDR:])
addr_res1 = Signal(intbv(0)[JPEG_RAM_ADDR:])
addr_res2 = Signal(intbv(0)[JPEG_RAM_ADDR:])
reset_col = Signal(bool(1))
def resetFsm(clk_fast, reset_fsm_r, reset_ctn):
    @always(clk_fast.posedge)
    def rtl():
        reset_fsm_r.next = YES
        if (reset_ctn < reset_dly_c):
            reset_fsm_r.next = NO
            reset_ctn.next = reset_ctn + 1
    return rtl
def trram2sdram(wr_s, dout_res, addr_res, addr_r, dataToRam_r):
	@always(clk_fast.negedge)
	def trram():
		
		
		if (addr_r <= 256):
			wr_s.next = 1
			dataToRam_r.next = dout_res
			addr_r.next = addr_r + 1
			addr_res.next = addr_res + 1
		else:
			wr_s.next = 0
		
	return trram
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
def muxaddr(addr_r, addr_r1, addr_r2, muxsel_r, dataFromRam_r, dataFromRam_r1, dataFromRam_r2, dout_res_r, dout_res_r1, dout_res_r2):
	@always_comb
	def muxLogic():
		addr_r.next = addr_r1
		dataFromRam_r.next = dataFromRam_r1
		dout_res_r.next = dout_res_r1
		if (muxsel_r == 1):
			addr_r.next = addr_r2
			dataFromRam_r.next = dataFromRam_r2
			dout_res_r.next = dout_res_r2
	return muxLogic		
		
def mux2(addr_r, addr_r1, addr_r2, addr_r3, addr_r4, muxsel, addr_not_reached, addr_not_reached1, addr_not_reached2, sig_in, sig_in1, sig_in2, wr_s, wr_s1, wr_s2, addr_res, addr_res1, addr_res2, dataToRam_r, dataToRam_r1, dataToRam_r2):
	@always_comb
	def muxLogic():
		addr_r.next = addr_r1
		addr_not_reached.next = addr_not_reached1
		sig_in.next = sig_in1
		wr_s.next = wr_s1
		addr_res.next = addr_res1
		dataToRam_r.next = dataToRam_r1
		if (muxsel == 0):
			addr_r.next = addr_r2
		elif (muxsel == 1):
			addr_r.next = addr_r3
			addr_not_reached.next = addr_not_reached2
			sig_in.next = sig_in2
		elif (muxsel == 2):
			wr_s.next = wr_s2
			addr_res.next = addr_res2
			addr_r.next = addr_r4
			dataToRam_r.next = dataToRam_r2
	return muxLogic

def RamCtrl(addr_r, addr_x, state_r, state_x, dataToRam_r, dataToRam_x, dataFromRam_r, dataFromRam_x, dataFromRam_s, done_s, wr_s, rd_s, sum_r, sum_x, din_res_r, din_res_x, dout_res_r, dout_res_x, addr_res_r, addr_res_x, we_res, muxsel_r, muxsel_x, rst):
    
    @always_comb
    def FSM():
        muxsel_x.next = muxsel_r
        din_res_x.next = din_res_r
        dout_res_x.next = dout_res_r
        addr_res_x.next = addr_res_r
        addr_x.next = addr_r
        state_x.next = state_r
        sum_x.next = sum_r
        wr_s.next = NO
        rd_s.next = NO
        dataToRam_x.next = dataToRam_r
        dataFromRam_x.next = dataFromRam_r
        if state_r == t_State.INIT:
            #up_interface.wr_en.next = YES
            rst.next = YES
            addr_x.next = 131072
            dataToRam_x.next = 1
            addr_res_x.next = 0
            muxsel_x.next = 0
            state_x.next = t_State.WRITE
        elif state_r == t_State.WRITE:
            if (done_s == NO):
                rst.next = NO
                wr_s.next = YES
            elif (addr_r <= 131088):
                addr_x.next = addr_r + 1
                dataToRam_x.next = dataToRam_r + 3
            else:
                addr_x.next = 131072
                addr_res_x.next = 0
                we_res.next = YES
                sum_x.next = 0
                state_x.next = t_State.READ_AND_SUM_DATA
        elif state_r == t_State.READ_AND_SUM_DATA:
            if (done_s == NO):
                rd_s.next = YES
            elif (addr_r <= 131088):
                #up_interface.din.next = (dataFromRam_s )
                din_res_x.next = (dataFromRam_s )
                sum_x.next = sum_r + (dataFromRam_s )
                addr_res_x.next = addr_res_r + 1
                addr_x.next = addr_r + 1
                if (addr_r == 131088):
                    #muxsel_x.next = YES
                    we_res.next = NO
                    state_x.next = t_State.DONE   
        elif state_r == t_State.CK_SDRAM_RD:
            if (done_s == NO):
               rd_s.next = YES
               we_res.next = YES
            elif addr_r <= 256 :
                addr_x.next = addr_r + 1
                addr_res_x.next = addr_res_r + 1
                din_res_x.next = dataFromRam_s
            else:
                sum_x.next = dataFromRam_s
                addr_x.next = 131072
                addr_res_x.next = 0
                
                wr_s.next = 0
                we_res.next = 0
                state_x.next = t_State.CK_SDRAM_WR
        elif state_r == t_State.CK_SDRAM_WR:
            if (addr_res_r <=255):
                dataFromRam_x.next = dout_res_r
                addr_x.next = addr_r + 1
            else:
                state_x.next = t_State.DONE
        elif state_r == t_State.ODD_SAMPLES:
            if addr_r == 1:
                addr_x.next = 2
                state_x.next = t_State.DONE
        elif state_r == t_State.EVEN_SAMPLES:
            if (done_s == NO):
               rd_s.next = YES 
            elif addr_r <= 505:
                addr_x.next = addr_r + 256
            else:
                state_x.next = t_State.DONE   
        elif state_r == t_State.WR_DATA:
            if addr_r == 1:
                addr_x.next = 8
            else:
                state_x.next = t_State.DONE
        elif state_r == t_State.INTERLACE:
            if addr_r == 16:
                state_x.next = t_State.DONE
        elif state_r == t_State.DONE:
            if addr_r.next == 1:
                state_x.next = t_State.INIT

            
            
    return FSM
def jpegFsm(state_r, state_x, muxsel, reset_fsm_r, dataToRam_r, dataFromRam_s, done_s):
    #state_x.next = state_r
    @always_comb
    def Fsm():
        if reset_fsm_r == ACTIVE_LOW:
            muxsel.next = 0
        else:
            if state_r == t_State.INIT:
                addr_x.next = 0
                state_x.next = t_State.WRITE
            elif state_r == t_State.WRITE:
                state_x.next = t_State.READ_AND_SUM_DATA
            elif state_r == t_State.READ_AND_SUM_DATA:
                state_x.next = t_State.DONE
            elif state_r == t_State.DONE:
                state_x.next = t_State.INIT
            else:
                raise ValueError("Undefined state")
    return Fsm   
#def jpegFsm( state_r, state_x, reset_fsm_r, addr_res, addr_res_r, offset, offset_r,  jp_flgs, reset_col, reset_col_r, reset_row, reset_row_r, rdy,  noupdate_s, addr_not_reached, pass1_done, pass1_done_r, index, index_r, col, col_r, muxsel, muxsel_r ):
#	offset.next = offset_r
#	addr_res.next = addr_res_r
#	pass1_done.next = pass1_done_r
#	reset_col.next = reset_col_r
#	reset_row.next = reset_row_r
#	state_x.next = state_r
#	index.next = index_r
#	muxsel.next = muxsel_r
#	col.next = col_r
#	@always_comb
#	def Fsm():
#		state_x.next = state_r
#		offset.next = offset_r
#		addr_res.next = addr_res_r
#		reset_col.next = reset_col_r
#		reset_row.next = reset_row_r
#		pass1_done.next = pass1_done_r
#		index.next = index_r
#		col.next = col_r
#		if reset_fsm_r == ACTIVE_LOW:
#			offset.next = offset_r
#			addr_res.next = addr_res_r
#			muxsel.next = 0
#			col.next = 0
#			state_x.next = t_State.INIT
#		else:
#			if state_r == t_State.INIT:
#				reset_col.next = 1
#				rdy.next = 0
#				#offset.next = 0
#				offset.next = 15
#				addr_res.next = 16
#				index.next = 0
#				we_res.next = 1
#
#				state_x.next = t_State.EVEN_SA
#			elif state_r == t_State.ODD_SA:
#				rdy.next = 1
#				reset_col.next = 0
#				jp_flgs.next = 6
#				offset.next = offset_r
#				if (offset_r < 205):
#					if ((noupdate_s != 1) and (addr_not_reached)):
#						#offset.next = offset_r + 2
#						#offset.next = offset_r + 32
#						#addr_res.next = addr_res_r + 32
#						rdy.next = 1
#						reset_col.next = 1
#
#					elif (addr_not_reached):
#						offset.next = offset_r + 32
#						addr_res.next = addr_res_r + 32
#				else:
#					if (col_r <= 14):
#						col.next = col_r + 1
#						offset.next = offset_r - 191
#						addr_res.next = addr_res_r - 191
#					else:
#						"""Need to setup for next state"""
#						rdy.next = 1
#						reset_col.next = 1
#						rdy.next = 0
#						offset.next = 2
#						addr_res.next = 0
#						#addr_rom.next = 0
#						state_x.next = t_State.TR_RES
#			elif state_r == t_State.EVEN_SA:
#				rdy.next = 1
#				reset_col.next = 0
#				jp_flgs.next = 7
#				offset.next = offset_r
#				#if (offset_r <= 220):
#				if (offset_r < 207):
#					if ((noupdate_s != 1) and (addr_not_reached)):
#						#offset.next = offset_r + 2
#						#offset.next = offset_r + 32
#						#addr_res.next = addr_res_r + 32
#						rdy.next = 1
#						reset_col.next = 1
#
#					elif (addr_not_reached):
#						offset.next = offset_r + 32
#						addr_res.next = addr_res_r + 32
#				else:
#					if (col_r <= 14):
#						col.next = col_r + 1
#						offset.next = offset_r - 191
#						addr_res.next = addr_res_r - 191
#					else:
#						"""Need to setup for next state"""
#						rdy.next = 1
#						reset_col.next = 1
#						rdy.next = 0
#						offset.next = 0
#						addr_res.next = 1
#						jp_flgs.next = 6
#						we_res.next = 0
#						#sel.next = 0
#						#sel_tr.next = 1
#						#addr_rom.next = 0
#						state_x.next = t_State.TR_RES
#			elif state_r == t_State.TR_RES:
#				offset.next = offset_r
#				addr_res.next = 0
#				state_x.next = t_State.TR_INIT
#			elif state_r == t_State.TR_INIT:
#				reset_col.next = 1
#				rdy.next = 0
#				offset.next = 0
#				addr_res.next = 1
#				muxsel.next = 0
#				
#				col.next = 0
#				state_x.next = t_State.ODD_SA
#			elif state_r == t_State.TRAN_RAM:
#				state_x.next = t_State.INIT
#			elif state_r == t_State.DONE_PASS1:
#				if (reset_col_r == 1):
#					reset_col.next = 1
#					pass1_done.next = 1
#			elif state_r == t_State.EVEN_SA_COL:
#				rdy.next = 1
#				reset_row.next = 0
#				jp_row_flgs.next = 7
#				offset.next = offset_r
#				if (offset_r <= 252):
#					if ((noupdate_s != 1) and (addr_not_reached)):
#						offset.next = offset_r + 2
#						addr_res.next = addr_res_r + 2
#						rdy.next = 1
#						reset_col.next = 1
#						if (index_r == 15):
#							col.next = 0
#						elif (index_r == 31):
#							col.next = 1
#						elif (index_r == 47):
#							col.next = 2
#						elif (index_r == 63):
#							col.next = 3
#						elif (index_r == 79):
#							col.next = 4
#						elif (index_r == 95):
#							col.next = 5
#						elif (index_r == 111):
#							col.next = 6
#						elif (index_r == 127):
#							col.next = 7
#						else:
#							index.next = index_r + 1
#				else:
#					"""Need to setup for next state"""
#					rdy.next = 1
#					reset_col.next = 1
#					rdy.next = 0
#					offset.next = 0
#					addr_res.next = 0
#					#addr_rom.next = 0
#					state_x.next = t_State.ODD_SA_COL
#			elif state_r == t_State.ODD_SA_COL:
#				rdy.next = 1
#				reset_row.next = 0
#				jp_row_flgs.next = 6
#				offset.next = offset_r
#				if (offset_r <= 252):
#					if ((noupdate_s != 1) and (addr_not_reached)):
#						offset.next = offset_r + 2
#						addr_res.next = addr_res_r + 2
#						rdy.next = 1
#						reset_col.next = 1
#						if (index_r == 143):
#							col.next = 8
#						elif (index_r == 159):
#							col.next = 9
#						elif (index_r == 175):
#							col.next = 10
#						elif (index_r == 191):
#							col.next = 11
#						elif (index_r == 207):
#							col.next = 12
#						elif (index_r == 223):
#							col.next = 13
#						elif (index_r == 239):
#							col.next = 14
#						elif (index_r == 255):
#							col.next = 15
#						else:
#							index.next = index_r + 1
#				else:
#					"""Need to setup for next state"""
#					rdy.next = 1
#					reset_row.next = 1
#					rdy.next = 0
#					offset.next = 0
#					addr_res.next = 0
#					#addr_rom.next = 0
#					state_x.next = t_State.DONE_PASS1
#			else:
#				raise ValueError("Undefined state")
#	return Fsm
#def jpegfsmupdate(clk_fast, offset, offset_r, state_r, state_x, addr_res, addr_res_r, reset_col, reset_col_r, reset_row, reset_row_r, pass1_done, pass1_done_r, index, index_r, col, col_r, muxsel, muxsel_r):
#	@always(clk_fast.posedge)
#	def fsmupdate():
#		offset_r.next = offset
#		state_r.next = state_x
#		addr_res_r.next = addr_res
#		reset_col_r.next = reset_col
#		reset_row_r.next = reset_row
#		pass1_done_r.next = pass1_done
#		index_r.next = index
#		muxsel_r.next = muxsel
#		col_r.next = col
#	return fsmupdate
def jpegfsmupdate(clk_fast, addr_r, addr_x, state_r, state_x, dataToRam_r, dataToRam_x, dataFromRam_r, dataFromRam_x,  sum_r, sum_x, dout_res_r, dout_res_x, din_res_r, din_res_x, addr_res_r, addr_res_x, muxsel_r, muxsel_x ):
    @always(clk_fast.posedge)
    def fsmupdate():
        muxsel_r.next = muxsel_x
        din_res_r.next = din_res_x
        dout_res_r.next = dout_res_x
        addr_res_r.next = addr_res_x
        addr_r.next = addr_x
        dataToRam_r.next = dataToRam_x
        dataFromRam_r.next = dataFromRam_x
        state_r.next = state_x
        sum_r.next = sum_x
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
def jpegsdram_rd(clk_fast, offset, dataFromRam_s, jp_lf, jp_sa, jp_rh, jp_flgs, reset_col, addr_r, addr_not_reached):
    even = jp_flgs(0)
    @always(clk_fast.posedge)
    def sdram_rd():
        
        
        if (reset_col):
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
                        #addr_r.next = addr_r + 1
                        addr_r.next = addr_r + 16
                    else:
						#if (addr_r == (2 + offset)):
                        if (addr_r == (17 + offset)):
                            jp_sa.next = dataFromRam_s
                            #addr_r.next = addr_r + 1
                            addr_r.next = addr_r + 16
                        else:
							#if (addr_r == (3 + offset)):
                            if (addr_r == (33 + offset)):
                                jp_rh.next = dataFromRam_s
                                addr_not_reached.next = 1
            else:
                if (addr_r == (0 + offset)):
                    jp_lf.next = dataFromRam_s
                    #addr_r.next = addr_r + 1
                    addr_r.next = addr_r + 16
                else:
					#if (addr_r == (1 + offset)):
                    if (addr_r == (16 + offset)):
                        jp_sa.next = dataFromRam_s
                        #addr_r.next = addr_r + 1
                        addr_r.next = addr_r + 16
                    else:
						#if (addr_r == (2 + offset)):
                        if (addr_r == (32 + offset)):
                            jp_rh.next = dataFromRam_s
                            addr_not_reached.next = 1
    return sdram_rd
def jpegsdram_rd_col(clk_fast, offset, dataFromRam_s, jp_row_lf, jp_row_sa, jp_row_rh, jp_row_flgs, reset_row, addr_r, addr_not_reached):
    even = jp_row_flgs(0)
    @always(clk_fast.posedge)
    def sdram_rd_col():
        
        
        if (reset_row):
            jp_row_lf.next = 0
            jp_row_sa.next = 0
            jp_row_rh.next = 0
            addr_not_reached.next = 0
            #if jp_row_flgs 6 odd jp_row_flgs 7 even_odd
            if (even  == 1):           
                addr_r.next = 1 + offset
            else:
                addr_r.next = 0 + offset
        else:
            if (even):
                    if (addr_r == (1 + offset) ):
                        jp_row_lf.next = dataFromRam_s
                        addr_r.next = addr_r + 1
                    else:
                        if (addr_r == (2 + offset)):
                            jp_row_sa.next = dataFromRam_s
                            addr_r.next = addr_r + 1
                        else:
                            if (addr_r == (3 + offset)):
                                jp_row_rh.next = dataFromRam_s
                                addr_not_reached.next = 1
            else:
                if (addr_r == (0 + offset)):
                    jp_row_lf.next = dataFromRam_s
                    addr_r.next = addr_r + 1
                else:
                    if (addr_r == (1 + offset)):
                        jp_row_sa.next = dataFromRam_s
                        addr_r.next = addr_r + 1
                    else:
                        if (addr_r == (2 + offset)):
                            jp_row_rh.next = dataFromRam_s
                            addr_not_reached.next = 1
    return sdram_rd_col
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
def jpegram2sigcol(jp_row_lf, jp_row_sa ,jp_row_rh, jp_row_flgs, rdy, addr_not_reached,  sig_in):
    """Combines 3 16 bit plus 4 flags into single value """
    @always_comb
    def ram2sigcol():
        if rdy:
            if addr_not_reached:
                sig_in.next = concat(jp_row_flgs, jp_row_rh, jp_row_sa, jp_row_lf)
            else:
                sig_in.next = 0
        else:
            sig_in.next = 0
    return ram2sigcol

#def test_instances(clk_fast, rst, eog, wr_s, rst_file_in, addr_r, dataToRam_r, y, addr_r1, addr_r2, sel, sig_in, noupdate_s, res_s, offset, dataFromRam_s, jp_lf, jp_sa, jp_rh, jp_flgs, reset_col, addr_not_reached, rdy, state_r, state_x, reset_fsm_r, addr_res, addr_res_r, offset_r, addr_rom, addr_rom_r):
def ramres(dout_res_r, din_res_r, addr_res_r, we_res, clk_fast, depth=256):
    """  Ram model """
    
    mem = [Signal(intbv(0)[16:]) for i in range(depth)]
    
    @always(clk_fast.posedge)
    def write():
        if we_res:
            mem[addr_res_r].next = din_res_r
                
    @always_comb
    def read():
        dout_res_r.next = mem[addr_res_r]

    return write, read
def simul(clk_fast, addr_r, addr_r1, addr_x, state_r, state_x, addr_r2, muxsel, dataToRam_r, dataToRam_x, dataFromRam_r,  dataFromRam_r1, dataFromRam_r2, dataFromRam_x, dataFromRam_s,  done_s, wr_s, rd_s, sum_r, sum_x ):
    instance_2 = muxaddr(addr_r, addr_r1, addr_r2, muxsel, dataFromRam_r, dataFromRam_r1, dataFromRam_r2 )
    instance_6 = RamCtrl(addr_r1, addr_x, state_r, state_x, dataToRam_r, dataToRam_x, dataFromRam_r1, dataFromRam_x, dataFromRam_s,  done_s, wr_s, rd_s, sum_r, sum_x)
    instance_7 = jpegfsmupdate(clk_fast, addr_r1, addr_x, state_r, state_x, dataToRam_r, dataToRam_x, dataFromRam_r1, dataFromRam_x, sum_r, sum_x)
    return instance_2, instance_6, instance_7
#return instance_2, instance_3, instance_4, instance_5, instance_7
#def xess_jpeg_top(clk_fast, addr_r, addr_x, addr_r1, addr_r2, muxsel, dataToRam_r, dataToRam_x, sig_in, noupdate_s, res_s, jp_lf, jp_sa ,jp_rh, jp_flgs, reset_col, rdy, addr_not_reached, offset, dataFromRam_s):
#toVHDL(simul, clk_fast, addr_r, addr_r1, addr_x, state_r, state_x, addr_r2, muxsel, dataToRam_r, dataToRam_r1, dataToRam_r2, dataToRam_x, dataFromRam_r, dataFromRam_x, dataFromRam_s,  done_s, wr_s, rd_s, sum_r, sum_x )
#toVHDL(RamCtrl, addr_r, addr_x, state_r, state_x, dataToRam_r, dataToRam_x, done_s, wr_s, rd_s)
#toVHDL(jpeg, state_r, state_x, muxsel, reset_fsm_r, dataToRam_r, dataFromRam_s, done_s)
#toVHDL(read_file_sdram, clk_fast, rst, eog, wr_s, rst_file_in, addr_r, dataToRam_r, y)
#toVHDL(muxaddr, addr_r, addr_r1, addr_r2,  muxsel)
#toVHDL(jpeg_process, clk_fast, sig_in,  noupdate_s, res_s)
#toVHDL(jpegsdram_rd, clk_fast, offset, dataFromRam_s, jp_lf, jp_sa, jp_rh, jp_flgs, reset_col, addr_r, addr_not_reached)
#toVHDL(jpegram2sig, jp_lf, jp_sa ,jp_rh, jp_flgs, rdy, addr_not_reached,  sig_in)
#toVHDL(jpegfsmupdate, clk_fast, offset, offset_r, state_r, state_x, addr_res, addr_res_r )
#toVHDL(jpegFsm, state_r, state_x, reset_fsm_r, addr_res, addr_res_r, offset, offset_r,  jp_flgs, reset_col, rdy,  noupdate_s, addr_not_reached )
#toVHDL(jpeg_top, clk_fast, addr_r, addr_x, addr_r1, addr_r2, muxsel, dataToRam_r, dataToRam_x, sig_in, noupdate_s, res_s, jp_lf, jp_sa ,jp_rh, jp_flgs, reset_col, rdy, addr_not_reached, offset, dataFromRam_s, state_r, state_x, reset_fsm_r, done_s)


def xess_jpeg_top(clk_fast, addr_r, addr_x, state_r, state_x, addr_r1, addr_r2, dataToRam_r, dataToRam_x, dataFromRam_r,  dataFromRam_r1, dataFromRam_r2, dataFromRam_x, sig_in, noupdate_s, res_s, jp_lf, jp_sa ,jp_rh, jp_flgs, reset_col, rdy, addr_not_reached, offset, dataFromRam_s, done_s, wr_s, rd_s, sum_r, sum_x, dout_res_r, dout_res_r1, dout_res_r2, dout_res_x, din_res_r, din_res_x, addr_res_r,addr_res_x, we_res, muxsel_r, muxsel_x, rst ):
    #instance_1 = read_file_sdram(clk_fast, rst, eog, wr_s1, rst_file_in, addr_r1, dataToRam_r1, y)
    instance_13 = fifo_up_if.fifo_up_if_ex(clk_fast,rst,up_interface.din,up_interface.wr_en,up_interface.full)        
    instance_14 = fifo_down_if.fifo_down_if_ex(clk_fast, rst, dn_interface.dout, dn_interface.rd_en, dn_interface.empty)
    #print instance_13, instance_14
    #instance_2 = mux2(addr_r, addr_r1, addr_r2, addr_r3, addr_r4, muxsel, addr_not_reached, addr_not_reached1, addr_not_reached2, sig_in, sig_in1, sig_in2, wr_s, wr_s1, wr_s2, addr_res, addr_res1, addr_res2, dataToRam_r, dataToRam_r1, dataToRam_r2)
    instance_2 = muxaddr(addr_r, addr_r1, addr_r2, muxsel_r, dataFromRam_r, dataFromRam_r1, dataFromRam_r2, dout_res_r, dout_res_r1, dout_res_r2 )
    instance_3 = jpeg_process(clk_fast, sig_in,  noupdate_s, res_s)
    instance_4 = jpegsdram_rd(clk_fast, offset, dataFromRam_s, jp_lf, jp_sa, jp_rh, jp_flgs, reset_col, addr_r2, addr_not_reached)
    instance_5 = jpegram2sig(jp_lf, jp_sa ,jp_rh, jp_flgs, rdy, addr_not_reached, sig_in)
    instance_6 = RamCtrl(addr_r1, addr_x, state_r, state_x, dataToRam_r, dataToRam_x, dataFromRam_r1, dataFromRam_x,  dataFromRam_s,  done_s, wr_s, rd_s, sum_r, sum_x, dout_res_r1, dout_res_x, din_res_r, din_res_x, addr_res_r, addr_res_x, we_res, muxsel_r, muxsel_x, rst )
    instance_7 = jpegfsmupdate(clk_fast, addr_r1, addr_x, state_r, state_x, dataToRam_r, dataToRam_x, dataFromRam_r1, dataFromRam_x, sum_r, sum_x, dout_res_r1, dout_res_x, din_res_r, din_res_x, addr_res_r, addr_res_x, muxsel_r, muxsel_x)
    instance_8 = ramres(dout_res_r2, din_res_r, addr_res_r, we_res, clk_fast, depth=256)
    #instance_9 = jpegsdram_rd_col(clk_fast, offset, dataFromRam_s, jp_row_lf, jp_row_sa, jp_row_rh, jp_row_flgs, reset_row, addr_r3, addr_not_reached2)
    #instance_10 = jpegram2sigcol(jp_row_lf, jp_row_sa ,jp_row_rh, jp_row_flgs, rdy, addr_not_reached2,  sig_in2)
    #instance_11 = trram2sdram(wr_s2, dout_res, addr_res2, addr_r4, dataToRam_r2)
    #instance_12 = resetFsm(clk_fast, reset_fsm_r, reset_ctn)
    return instance_2, instance_3, instance_4, instance_5, instance_6, instance_7, instance_8, instance_13, instance_14


toVHDL(xess_jpeg_top, clk_fast, addr_r, addr_x, state_r, state_x, addr_r1, addr_r2, dataToRam_r,  dataFromRam_r1, dataFromRam_r2, dataToRam_x, dataFromRam_x, dataFromRam_r, sig_in, noupdate_s, res_s, jp_lf, jp_sa ,jp_rh, jp_flgs, reset_col, rdy, addr_not_reached, offset, dataFromRam_s, done_s, wr_s, rd_s, sum_r, sum_x, dout_res_r, dout_res_r1, dout_res_r2, dout_res_x, din_res_r, din_res_x, addr_res_r, addr_res_x, we_res, muxsel_r, muxsel_x, rst)
#toVerilog(xess_jpeg_top, clk_fast, addr_r, addr_x, addr_r1, addr_r2, muxsel, dataToRam_r, dataToRam_x, sig_in, noupdate_s, res_s, jp_lf, jp_sa ,jp_rh, jp_flgs, reset_col, rdy, addr_not_reached, offset, dataFromRam_s, state, even_odd_r, even_odd_x)
#toVHDL(xess_jpeg_top, clk_fast, addr_r, addr_x, state_r, state_x, addr_r1, addr_r2, muxsel, dataToRam_r, dataToRam_x, dataToRam_r2, dataToRam_x, dataFromRam_r, dataFromRam_x, sig_in, noupdate_s, res_s, jp_lf, jp_sa ,jp_rh, jp_flgs, reset_col, rdy, addr_not_reached, offset, dataFromRam_s, done_s, wr_s, rd_s, sum_r, sum_x)
