
import argparse
from pprint import pprint 

import myhdl
from myhdl import (Signal, ResetSignal, intbv, always_seq, always,
                   always_comb)

from rhea.build.boards import get_board
from rhea.system import Global, Clock, Reset, FIFOBus, Signals
from rhea.cores.spi import SPIBus, spi_slave_fifo                   
from rhea.cores.spi import spi_controller
led_port_pin_map = {
    'xula':  dict(name='led', pins=(32,)),
    'xula2': dict(name='led', pins=('T4',)),
}

                   
def xula_blinky_spi_slave(led, clock, mosi, miso, sck, reset=None):
    """ a simple LED blinks example.
    This is intended to be used with the Xula, Stickit motherboard
    and an LED / button pmod board.
    """    
    maxcnt = int(clock.frequency)
    cnt = Signal(intbv(0, min=0, max=maxcnt))
    toggle = Signal(bool(0))
    spibus, fifobus = SPIBus(sck, mosi, miso), FIFOBus()
    reset = Reset(0, active=1, async=False)
    glbl = Global(clock, reset)
    #inst_spi = spi_slave_fifo(glbl, spibus, fifobus)
    data = Signal(intbv(0)[8:])
    rd, wr, full, empty = Signals(bool(0), 4)
    cso = spi_controller.cso()
    cso.isstatic = True
    cfg_inst = cso.get_generators()
    spi_controller.debug = False
    spi_inst = spi_controller(glbl, spibus, fifobus, cso=cso)
    
    @always_seq(clock.posedge, reset=None)
    def rtl():
		if cnt == maxcnt-1:
			toggle.next = not toggle
			cnt.next = 0
		else:
			cnt.next = cnt + 1


    @always_comb
    def tb_fifo_loopback():
        if not fifobus.full:
            fifobus.write.next = not fifobus.empty
            fifobus.read.next = not fifobus.empty
            fifobus.write_data.next = fifobus.read_data
    reset_dly_cnt = Signal(intbv(0)[5:])
    # software reset need for xula2
    @always(clock.posedge)
    def reset_tst():
        '''
        For the first 4 clocks the reset is forced to lo
        for clock 6 to 31 the reset is set hi
        then the reset is lo
        '''
        if (reset_dly_cnt < 31):
            reset_dly_cnt.next = reset_dly_cnt + 1
            if (reset_dly_cnt <= 4):
                reset.next = 0
            if (reset_dly_cnt >= 5):
                reset.next = 1
        else:
            reset.next = 0

    # monitors
    @always_comb
    def mon():
        data.next = fifobus.read_data
        rd.next = fifobus.read
        wr.next = fifobus.write
        full.next = fifobus.full
        empty.next = fifobus.empty
   
    return myhdl.instances()
    
        
def build(args):
    brd = get_board(args.brd)
    # the design port names don't match the board pin names,
    # add the ports here (all the IO are a generic "chan")
    brd.add_port(**led_port_pin_map[args.brd])
    brd.device = 'XC6SLX9' 
    #brd.add_port(name='button', pins=(R2,))
    brd.add_port('mosi', 'F2')
    brd.add_port('miso', 'F1')
    brd.add_port('sck', 'H2')
    flow = brd.get_flow(xula_blinky_spi_slave)
    flow.run()
    info = flow.get_utilization()
    pprint(info)
    
    
def cliparse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--brd", default='xula2')
    parser.add_argument("--flow", default="ise")
    args = parser.parse_args()
    return args
    
    
def main():
    args = cliparse()
    build(args)
    
        
if __name__ == '__main__':
    main()
    
            
