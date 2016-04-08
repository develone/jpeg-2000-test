#
# Copyright (c) 2013-2015 Christopher L. Felton
#

import traceback
import pytest
import argparse

import myhdl
from myhdl import (Signal, intbv, instance, always_comb,
                   delay, StopSimulation, always, ResetSignal)

from rhea.cores.spi import spi_controller
from rhea.cores.spi import SPIBus

from rhea.models.spi import SPIEEPROM

from rhea.system import Global, Clock, Reset, Signals
from rhea.system import Wishbone
from rhea.system import FIFOBus

from rhea.utils.test import run_testbench, tb_convert, tb_args, tb_default_args
from rhea.build.boards import get_board
from pprint import pprint

# global signals used by many
clock = Clock(0, frequency=100e6)
#reset = Reset(0, active=1, async=True)
reset = ResetSignal(0, active=1,async=True)
glbl = Global(clock, reset)
portmap = dict(
    glbl=glbl,
    spibus=SPIBus(),
    fifobus=FIFOBus(),
    cso=spi_controller.cso()
)


def spi_slave_top(clock, sck, mosi, miso, ss):
    """SPI top-level for conversion testing"""
    glbl = Global(clock, reset)
    spibus = SPIBus(sck, mosi, miso, ss)
    fifobus = FIFOBus()

    cso = spi_controller.cso()
    cso.isstatic = True
    cfg_inst = cso.get_generators()

    spi_controller.debug = False
    spi_inst = spi_controller(glbl, spibus, fifobus, cso=cso)

    @always_comb
    def fifo_loopback():
        fifobus.write_data.next = fifobus.read_data
        fifobus.write.next = fifobus.read_valid
        fifobus.read.next = not fifobus.empty
    reset_dly_cnt = Signal(intbv(0)[32:])
    
    @always(clock.posedge)
    
    def reset_tst():
	'''
	For the first 256 clocks the reset is forced to lo
	for clock 500 to 7000 the reset is set hi
	the the reset is lo
		
	'''

        if (reset_dly_cnt < 700):
            reset_dly_cnt.next = reset_dly_cnt + 1
            if (reset_dly_cnt == 256):
                reset.next = 0
            if (reset_dly_cnt == 500):        
                reset.next = 1
        else:
            reset.next = 0

    return myhdl.instances()


def convert():
    """convert the faux-top-level"""
    clock = Clock(0, frequency=50e6)
    reset = Reset(0, active=1, async=False)
    sck, mosi, miso, ss = Signals(bool(0), 4)
    tb_convert(spi_slave_top, clock, sck, mosi, miso, ss)

def build():
    brd = get_board('xula2_stickit_mb')
    brd.device = 'XC6SLX9'
    #chan 24 BCM9_MISO -->  RPi2B
    brd.add_port('mosi', 'F1')
    #chan 25 BCM10_MOSI <--- RPi2B
    brd.add_port('miso', 'F2')
    #chan 23 BCM10_SCLK
    brd.add_port('sck', 'H2')
    #chan 22 BCM5 
    brd.add_port('ss', 'H1')     
    flow = brd.get_flow(top=spi_slave_top)
    flow.run()
    info = flow.get_utilization()
    pprint(info)

def test_spi_controller_cso(args=None):
    args = tb_default_args(args)

    clock = Clock(0, frequency=50e6)
    reset = Reset(0, active=1, async=False)
    glbl = Global(clock, reset)
    spibus = SPIBus()
    # a FIFOBus to push-pull data from the SPI controller
    fifobus = FIFOBus(size=16)
    # control-status object for the SPI controller
    #cso = spi_controller.cso()

    spiee = SPIEEPROM()
    asserr = Signal(bool(0))

    def bench_spi_cso():
        spi_controller.debug = True    # enable debug monitors
        #tbdut = spi_controller(glbl, spibus, fifobus, cso=cso)
        tbdut = spi_controller(glbl, spibus, fifobus)
        tbeep = spiee.gen(clock, reset, spibus)
        tbclk = clock.gen(hticks=5)

        @instance
        def tbstim():
            yield reset.pulse(33)
            yield delay(100)
            yield clock.posedge

            try:
                # enable the SPI core
                cso.enable.next = True
                cso.bypass_fifo.next = True
                cso.loopback.next = True

                # write to the transmit FIFO
                values = (0x02, 0x00, 0x00, 0x00, 0x55)
                for data in values:
                    cso.tx_byte.next = data
                    cso.tx_write.next = True
                    yield clock.posedge
                cso.tx_write.next = False

                while cso.tx_fifo_count > 0:
                    yield delay(100)

                while cso.rx_fifo_count < 5:
                    yield delay(100)

                ii, nticks = 0, 0
                while ii < len(values):
                    if cso.rx_empty:
                        cso.rx_read.next = False
                    else:
                        cso.rx_read.next = True
                    if cso.rx_byte_valid:
                        assert values[ii] == cso.rx_byte, \
                            "{:<4d}: data mismatch, {:02X} != {:02X}".format(
                                ii, int(values[ii]), int(cso.rx_byte))
                        ii += 1
                        nticks = 0
                    yield clock.posedge, cso.rx_empty.posedge
                    cso.rx_read.next = False

                    if nticks > 30:
                        raise TimeoutError
                    nticks += 1

                cso.rx_read.next = False
                yield clock.posedge

            except AssertionError as err:
                asserr.next = True
                print("@E: assertion {}".format(err))
                yield delay(100)
                traceback.print_exc()
                raise err

            raise StopSimulation

        # monitor signals for debugging
        tx_write, rx_read = Signals(bool(0), 2)

        @always_comb
        def tbmon():
            rx_read.next = cso.rx_read
            tx_write.next = cso.tx_write

        return tbdut, tbeep, tbclk, tbstim, tbmon

    run_testbench(bench_spi_cso, args=args)


# enable when the register-file automation is complete
@pytest.mark.xfail()
def test_spi_memory_mapped(args=None):
    args = tb_default_args(args)
    
    base_address = ba = 0x400
    clock = Clock(0, frequency=50e6)
    reset = Reset(0, active=1, async=False)
    glbl = Global(clock, reset)
    regbus = Wishbone(glbl)    
    fifobus = FIFOBus(size=16)
    spiee = SPIEEPROM()
    spibus = SPIBus()
    asserr = Signal(bool(0))
    
    def bench_spi():
        tbdut = spi_controller(glbl, spibus, fifobus=fifobus, mmbus=regbus)
        tbeep = spiee.gen(clock, reset, spibus)
        tbclk = clock.gen(hticks=5)
        # grab all the register file outputs
        tbmap = regbus.interconnect()

        # get a reference to the SPI register file
        rf = regbus.regfiles['SPI_000']
        # dumpy the registers for the SPI peripheral
        print("SPI register file")
        for name, reg in rf.registers.items():
            print("  {0} {1:04X} {2:04X}".format(name, reg.addr, int(reg)))
        print("")

        @instance
        def tbstim():            
            yield reset.pulse(33)
            yield delay(100)
            yield clock.posedge
            
            try:
                # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                # loop through the registers and check the default 
                # values, these are the offset values.
                for addr, sig in rf.roregs:
                    yield regbus.readtrans(addr+ba)
                    assert regbus.get_read_data() == int(sig), \
                        "Invalid read-only value"

                for addr, sig in rf.rwregs:
                    # need to skip the FIFO read / write
                    if addr in (rf.sptx.addr, rf.sprx.addr,):
                        pass
                    else:
                        yield regbus.readtrans(addr+ba)
                        assert regbus.get_read_data() == int(sig), \
                            "Invalid default value"

                # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                # enable the system         
                print("enable the SPI core")
                yield regbus.writetrans(rf.spst.addr, 0x02)  # register data drives fifo
                yield regbus.writetrans(rf.spcr.addr, 0x9A)  # default plus enable (98 + 02)

                print("write to the transmit register")
                for data in (0x02, 0x00, 0x00, 0x00, 0x55):
                    print("\nwriting to sptx {:02x}".format(data))
                    yield regbus.writetrans(rf.sptx.addr, data)

                print("")
                yield regbus.readtrans(rf.sptc.addr)
                print("TX FIFO count {}".format(regbus.get_read_data()))

                yield regbus.readtrans(rf.sprc.addr)
                print("RX FIFO count {}".format(regbus.get_read_data()))

                yield delay(1000)

                print("wait for return bytes")
                for ii in range(1000):
                    yield regbus.readtrans(rf.sprc.addr)
                    if regbus.get_read_data() == 5:
                        break
                    yield delay(10)
                
                # verify bytes received and not timeout
                print("RX FIFO count {}".format(regbus.get_read_data()))
                assert regbus.get_read_data() == 5
                
                print("read the returned bytes")
                for ii in range(5):
                    yield regbus.readtrans(rf.sprx.addr)
                    print("spi readback {0}".format(regbus.get_read_data()))

            except Exception as err:
                print("@W: exception {0}".format(err))                
                yield delay(100)
                traceback.print_exc()
                raise err

            yield delay(100)
            raise StopSimulation
        
        return tbstim, tbdut, tbeep, tbclk, tbmap

    run_testbench(bench_spi, args=args)


def test_convert():
    convert()


if __name__ == '__main__':
    #  test_spi_controller_cso(tb_args())
    #test_convert()
    build()
    #test_spi_memory_mapped()