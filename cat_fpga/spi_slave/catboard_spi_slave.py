
import argparse
from pprint import pprint 

import myhdl
from myhdl import (Signal, ResetSignal, intbv, always_seq, always,
                   always_comb, traceSignals, Simulation, StopSimulation, delay, instance)

from rhea.build.boards import get_board
from rhea.system import Global, Clock, Reset, FIFOBus, Signals
from rhea.cores.spi import SPIBus, spi_slave_fifo
from rhea.cores.misc import glbl_timer_ticks                  
ledreg = Signal(intbv(0)[8:])
'''
led_port_pin_map = {
    'xula':  dict(name='led', pins=(32,)),
    'xula2': dict(name='led', pins=('T4',)),
}
'''
                   
def catboard_blinky_spi_slave(led, clock, mosi, miso, sck, ss, reset=None):
    """ a simple LED blinks example.
    This is intended to be used with the Xula, Stickit motherboard
    and an LED / button pmod board.
    """    
    maxcnt = int(clock.frequency)
    cnt = Signal(intbv(0, min=0, max=maxcnt))
    toggle = Signal(bool(0))
    spibus, fifobus = SPIBus(sck, mosi, miso, ss), FIFOBus()
    #spibus_sl, fifobus_sl = SPIBus(), FIFOBus()
    reset = Reset(0, active=1, async=False)
    glbl = Global(clock, reset)
    inst_spi_sl = spi_slave_fifo(glbl, spibus, fifobus)
    data = Signal(intbv(0)[8:])
    rd, wr, full, empty = Signals(bool(0), 4)
    tone = Signal(intbv(0)[8:])
    
    # create the timer tick instance
    tick_inst = glbl_timer_ticks(glbl, include_seconds=True)
    
    #cso = spi_controller.cso()
    #cso.isstatic = True
    #cfg_inst = cso.get_generators()
    #spi_controller.debug = False
    #spi_inst = spi_controller(glbl, spibus, fifobus, cso=cso)
    
    @always_seq(clock.posedge, reset=None)
    def beh_assign():
		if glbl.tick_sec:
			tone.next = (~tone) & 0x1
		led.next = ledreg | tone[5:]
    '''
    @always(clock.posedge)
    def beh_led_control():
        if (data == 0x23):
            ledreg.next = 1
    '''
      



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
    
def tb(led, clock, mosi, miso, sck, ss, reset=None):
    """ a simple LED blinks example.
    This is intended to be used with the Xula, Stickit motherboard
    and an LED / button pmod board.
    """
    @always(delay(10))
    def clkgen():
		clock.next = not clock
    @instance
    def tbstim():
        #yield reset.pulse(40)
        yield delay(1000)
        yield clock.posedge

        # @todo: make generic
        # @todo: random_sequence = [randint(0, fifobus.write_data.max) for _ in range(ntx)]
        yield spibus.writeread(0x55)
        yield spibus.writeread(0xAA)
        yield spibus.writeread(0xCE)
        assert spibus.get_read_data() == 0x55
        yield spibus.writeread(0x01)
        assert spibus.get_read_data() == 0xAA
        yield spibus.writeread(0x01)
        assert spibus.get_read_data() == 0xCE 

        raise StopSimulation	    
    maxcnt = int(clock.frequency)
    cnt = Signal(intbv(0, min=0, max=maxcnt))
    toggle = Signal(bool(0))
    spibus, fifobus = SPIBus(sck, mosi, miso, ss), FIFOBus()
    #spibus_sl, fifobus_sl = SPIBus(), FIFOBus()
    reset = Reset(0, active=1, async=False)
    glbl = Global(clock, reset)
    inst_spi_sl = spi_slave_fifo(glbl, spibus, fifobus)
    data = Signal(intbv(0)[8:])
    rd, wr, full, empty = Signals(bool(0), 4)
    tone = Signal(intbv(0)[8:])
    
    # create the timer tick instance
    tick_inst = glbl_timer_ticks(glbl, include_seconds=True)
    #cso = spi_controller.cso()
    #cso.isstatic = True
    #cfg_inst = cso.get_generators()
    #spi_controller.debug = False
    #spi_inst = spi_controller(glbl, spibus, fifobus, cso=cso)

    @always(clock.posedge)
    def beh_assign():
		if glbl.tick_sec:
			tone.next = (~tone) & 0x1
		led.next = ledreg | tone[5:]    
 
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
    #brd.add_port(**led_port_pin_map[args.brd])
    #brd.add_port_name('led', 'pm2', slice(0, 8))
    #brd.device = 'XC6SLX9' 
    #brd.add_port(name='button', pins=(R2,))
    #xula2 chan25 BCM20_MOSI   ----> RPI_GPIO_P1_19 /* MOSI */
    brd.add_port('mosi', 'R3')
    #xula2 chan24 BCM19_MISO  ---->  RPI_GPIO_P1_21 /* MISO */
    brd.add_port('miso', 'T3')
    #xula2 chan23 BCM21_SCLK  ----> RPI_ GPIO_P1_23  /* CLK */
    brd.add_port('sck', 'T1')  
    #xula2 chan08 BCM08_CE0   ----> RPI_GPIO_P1_24 /* CE0 */
    brd.add_port('ss', 'T8')
    flow = brd.get_flow(catboard_blinky_spi_slave)
    flow.run()
    info = flow.get_utilization()
    pprint(info)
    
    
def cliparse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--brd", default='catboard')
    parser.add_argument("--flow", default="ise")
    parser.add_argument("--trace", default=False, action='store_true')
    parser.add_argument("--build", default=False, action='store_true')
    args = parser.parse_args()
    return args

def convert(args):
    toVerilog(dwt,flgs,upd,lft,sam,rht,lift,done,clock)
    #toVHDL(dwt_top,clock)
 
def main():
    args = cliparse()
    if args.trace:
        mosi, miso, sck, ss = Signals(bool(0), 4)
        led = Signal(bool(0))
        clock=Clock(0, frequency=50e6)
        tb_fsm = traceSignals(tb,led, clock, mosi, miso, sck, ss, reset=None)
        sim = Simulation(tb_fsm)
        sim.run()  
    if args.build:
        build(args)    
    
 
        
if __name__ == '__main__':
    main() 
