

	
	

 

from myhdl import *

def iso_pricing_check(ask_price_levels_i,price_o,WIDTH=24,NUM_LEVELS=4):


  # this line of code of slicing the signal and generating list of shadow signals is
  # not getting translated into verilog.
  ask_price_levels = [ask_price_levels_i((i+1)*WIDTH, i*WIDTH) for i in range(0, NUM_LEVELS)]

  @always_comb
  def ask_price_logic():
    # just giving the last level price as output
    price_o = ask_price_levels[NUM_LEVELS-1]

  return instances()

def convert():
    WIDTH = 32
    NUM_LEVELS = 16

    ask_price_levels_i = Signal(intbv(0)[NUM_LEVELS*24:])
    price_o = Signal(intbv(0)[WIDTH:])


    dut = toVHDL(iso_pricing_check,ask_price_levels_i,price_o,
               WIDTH=WIDTH,NUM_LEVELS=NUM_LEVELS)

convert()