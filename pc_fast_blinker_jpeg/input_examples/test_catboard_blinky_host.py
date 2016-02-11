
from __future__ import print_function, division

import myhdl
from myhdl import (Signal, intbv, instance, delay, StopSimulation)

from rhea.system import Global, Clock, Reset
from rhea.models.uart import UARTModel
from rhea.utils.test import run_testbench, tb_args, tb_default_args
from rhea.utils import CommandPacket
from rhea.utils.command_packet import PACKET_LENGTH

from catboard_blinky_host import catboard_blinky_host
from dwt_image import (seq_to_img, de_interleave, lower_upper, rd_img, lsr)

def test_ibh(args=None):
    args = tb_default_args(args)
    numbytes = 13

    imgfn = "../../lena_256.png"

    im, m, pix = rd_img(imgfn)
     

    clock = Clock(0, frequency=50e6)
    glbl = Global(clock, None)
    led = Signal(intbv(0)[8:])
    uart_tx = Signal(bool(0))
    uart_rx = Signal(bool(0))
    uartmdl = UARTModel()

    def bench_ibh():
        tbclk = clock.gen()
        tbmdl = uartmdl.process(glbl, uart_tx, uart_rx)
        tbdut = catboard_blinky_host(clock, led, 
                                     uart_tx, uart_rx)

        @instance
        def tbstim():
            yield delay(1000)
            row = 2
            col = 0
            flag = 7
            v0 = lsr(row,col,m,flag)
            # send a write that should enable all five LEDs
            pkt = CommandPacket(False, address=0x00, vals=[v0])
            for bb in pkt.rawbytes:
                uartmdl.write(bb)
            waitticks = int((1/115200.) / 1e-9) * 10 * 28
            yield delay(waitticks)
            row = 1
            flag = 6
            v1 = lsr(row,col,m,flag)              
            pkt = CommandPacket(False, address=0x04, vals=[v1])
            for bb in pkt.rawbytes:
                uartmdl.write(bb)
            waitticks = int((1/115200.) / 1e-9) * 10 * 28
            yield delay(waitticks)
            row = 4
            flag = 7
            v2 = lsr(row,col,m,flag)    
            pkt = CommandPacket(False, address=0x08, vals=[v2])
            for bb in pkt.rawbytes:
                uartmdl.write(bb)
            waitticks = int((1/115200.) / 1e-9) * 10 * 28
            yield delay(waitticks)
            row = 3
            flag = 6
            v3 = lsr(row,col,m,flag)    
            pkt = CommandPacket(False, address=0x0C, vals=[v3 ])
            for bb in pkt.rawbytes:
                uartmdl.write(bb)
            waitticks = int((1/115200.) / 1e-9) * 10 * 28
            yield delay(waitticks) 
            pkt = CommandPacket(False, address=0x20, vals=[0xFF])
            for bb in pkt.rawbytes:
                uartmdl.write(bb)
            waitticks = int((1/115200.) / 1e-9) * 10 * 28
            yield delay(waitticks) 
            timeout = 100
            yield delay(waitticks) 
            # get the response packet
            for ii in range(PACKET_LENGTH):
                rb = uartmdl.read()
                while rb is None and timeout > 0:
                    yield clock.posedge
                    rb = uartmdl.read()
                    timeout -= 1
                if rb is None:
                    raise TimeoutError

            # the last byte should be the byte written
            #assert rb == 0xFF

            yield delay(1000)
            raise StopSimulation

        return tbclk, tbmdl, tbdut, tbstim

    run_testbench(bench_ibh, args=args)
    myhdl.toVerilog.directory = 'output'
    myhdl.toVerilog(catboard_blinky_host, clock, led,
                    uart_tx, uart_rx)


if __name__ == '__main__':
    test_ibh(tb_args())
