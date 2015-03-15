from myhdl import *
from jpeg_constants import *
#toVHDL.numeric_ports = False
def combine( left_com_x, sam_com_x, right_com_x, lft_s_i, sa_s_i, rht_s_i, combine_rdy_s, nocombine_s, W0=3, LVL0=4, W1=3, LVL1=4, W2=3, LVL2=4,  W3=3, LVL3=4, SIMUL=0 ):
	lft_s = [lft_s_i((i+1)*W2, i*W2) for i in range(0, LVL2) ]
	sa_s = [sa_s_i((i+1)*W2, i*W2) for i in range(0, LVL2) ]
	rht_s = [rht_s_i((i+1)*W2, i*W2) for i in range(0, LVL2) ]
	if(LVL0==1):
		@always_comb
		def combine_logic():
			if (combine_rdy_s == 1):
				left_com_x.next = concat(lft_s[0])
				sam_com_x.next = concat(sa_s[0])
				right_com_x.next = concat(rht_s[0])
				nocombine_s.next = 0
			else:
				left_com_x.next = 0
				sam_com_x.next = 0
				right_com_x.next = 0
				nocombine_s.next = 1

	if(LVL0==2):
		@always_comb
		def combine_logic():
			if (combine_rdy_s == 1):
				left_com_x.next = concat(lft_s[1],lft_s[0])
				sam_com_x.next = concat(sa_s[1],sa_s[0])
				right_com_x.next = concat(rht_s[1],rht_s[0])
				nocombine_s.next = 0
			else:
				left_com_x.next = 0
				sam_com_x.next = 0
				right_com_x.next = 0
				nocombine_s.next = 1

	elif(LVL0==4):
		@always_comb
		def combine_logic():
			if (combine_rdy_s == 1):
				left_com_x.next = concat(lft_s[3],lft_s[2],lft_s[1],lft_s[0])
				sam_com_x.next = concat(sa_s[3],sa_s[2],sa_s[1],sa_s[0])
				right_com_x.next = concat(rht_s[3],rht_s[2],rht_s[1],rht_s[0])
				nocombine_s.next = 0
			else:
				left_com_x.next = 0
				sam_com_x.next = 0
				right_com_x.next = 0
				nocombine_s.next = 1

	elif(LVL0==8):
		@always_comb
		def combine_logic():
			if (combine_rdy_s == 1):
				left_com_x.next = concat(lft_s[7],lft_s[6],lft_s[5],lft_s[4],
				lft_s[3],lft_s[2],lft_s[1],lft_s[0])
				sam_com_x.next = concat(sa_s[7],sa_s[6],sa_s[5],sa_s[4],
				sa_s[3],sa_s[2],sa_s[1],sa_s[0])
				right_com_x.next = concat(rht_s[7],rht_s[6],rht_s[5],rht_s[4],
				rht_s[3],rht_s[2],rht_s[1],rht_s[0])
				nocombine_s.next = 0
			else:
				left_com_x.next = 0
				sam_com_x.next = 0
				right_com_x.next = 0
				nocombine_s.next = 1
	elif(LVL0==16):
		@always_comb
		def combine_logic():
			if (combine_rdy_s == 1):
				left_com_x.next = concat(lft_s[15],lft_s[14],lft_s[13],lft_s[12],
				lft_s[11],lft_s[10],lft_s[9],lft_s[8],
				lft_s[7],lft_s[6],lft_s[5],lft_s[4],
				lft_s[3],lft_s[2],lft_s[1],lft_s[0])
				sam_com_x.next = concat(sa_s[15],sa_s[14],sa_s[13],sa_s[12],
				sa_s[11],sa_s[10],sa_s[9],sa_s[8],
				sa_s[7],sa_s[6],sa_s[5],sa_s[4],
				sa_s[3],sa_s[2],sa_s[1],sa_s[0])
				right_com_x.next = concat(rht_s[15],rht_s[14],rht_s[13],rht_s[12],
				rht_s[11],rht_s[10],rht_s[9],rht_s[8],
				rht_s[7],rht_s[6],rht_s[5],rht_s[4],
				rht_s[3],rht_s[2],rht_s[1],rht_s[0])
				nocombine_s.next = 0
			else:
				left_com_x.next = 0
				sam_com_x.next = 0
				right_com_x.next = 0
				nocombine_s.next = 1
	return combine_logic
def convert():
	if (SIMUL == 0):
		left_com_x = Signal(intbv(0)[LVL2*W2:])
		sam_com_x = Signal(intbv(0)[LVL2*W2:])
		right_com_x = Signal(intbv(0)[LVL2*W2:])
		""" W0, LVL0, W1, LVL1, W2, LVL2, W3, and LVL3
		Required  by jp_process
		these are used to set the size of the
		arrays"""
		combine_rdy_s = Signal(bool(0))
		nocombine_s = Signal(bool(0))
		lft_s_i = Signal(intbv(0)[LVL2*W2:])
		sa_s_i = Signal(intbv(0)[LVL2*W2:])
		rht_s_i = Signal(intbv(0)[LVL2*W2:])
		dut = toVHDL(combine, left_com_x, sam_com_x, right_com_x, lft_s_i, sa_s_i, rht_s_i, combine_rdy_s, nocombine_s, W0=W0, LVL0=LVL0, W1=W1, LVL1=LVL1, W2=W2, LVL2=LVL2,  W3=W3, LVL3=LVL3, SIMUL=0 )
		dut = toVerilog(combine, left_com_x, sam_com_x, right_com_x, lft_s_i, sa_s_i, rht_s_i, combine_rdy_s, nocombine_s, W0=W0, LVL0=LVL0, W1=W1, LVL1=LVL1, W2=W2, LVL2=LVL2,  W3=W3, LVL3=LVL3, SIMUL=0 )
	else:
		print "In simulation mode"


convert()
