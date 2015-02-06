

	
	

 

from myhdl import *
toVHDL.numeric_ports = False
def jp_process(sig_in_x_i,res_s,res_o_x_i,xx_o, W0=32,LVL0=16,W1=11,LVL1=16):

    
  # this line of code of slicing the signal and generating list of shadow signals is
  # not getting translated into verilog.
  #print W0,LVL0, W1,LVL1
  sig_in_x = [sig_in_x_i((i+1)*W0, i*W0) for i in range(0, LVL0)]
  res_o_x =  [res_o_x_i((i+1)*W1, i*W1) for i in range(0, LVL1)] 
  @always_comb
  def jj_vhd_logic():
    # just giving the last level price as output
    res_s = sig_in_x[LVL0-1]
    xx_o = res_o_x[LVL1-1]
  return instances()

def convert():
    W0 = 32
    LVL0 = 16
    W1 = 11
    LVL1 = 16
    sig_in_x_i = Signal(intbv(0)[LVL0*32:])
    res_o_x_i = Signal(intbv(0, min = -1024, max = 1024)[LVL1*11:])
    res_s = Signal(intbv(0, min = -1024, max = 1024)[W0:])
    xx_o = Signal(intbv(0)[W1:])

    dut = toVerilog(jp_process,sig_in_x_i, res_s,res_o_x_i,xx_o)

convert()