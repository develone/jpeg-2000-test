import os
from myhdl import *


def const_assign(aBit, aByte):

    b = Signal(bool(True)) # to avoid "myhdl.AlwaysCombError: sensitivity list is empty"

    @always_comb
    def logic():
        aBit.next = b
        aByte.next = 0x55

    return logic

def convert():
    my_bit = Signal(bool(0))
    my_byte = Signal(intbv(0)[8:])
    toVerilog(const_assign, my_bit, my_byte)

def test():
    my_bit = Signal(bool(0))
    my_byte = Signal(intbv(0)[8:])

    cmd = "iverilog -o const_assign const_assign.v tb_const_assign.v"
    os.system(cmd)

    def _test():
        dut = Cosimulation("vvp -m ./myhdl.vpi const_assign", aBit=my_bit, aByte=my_byte)
#         dut = const_assign(aBit=my_bit, aByte=my_byte)

        @instance
        def stim():
            print "-------------"

            yield delay(10)
            print "Expected ({}, {}), detected ({}, {})".format(True, 0x55, my_bit, my_byte)

            yield delay(10)
            print "Expected ({}, {}), detected ({}, {})".format(True, 0x55, my_bit, my_byte)

            yield delay(10)
            print "Expected ({}, {}), detected ({}, {})".format(True, 0x55, my_bit, my_byte)

            print "-------------"

            raise StopSimulation

        return dut, stim

    Simulation(_test()).run()

if __name__ == '__main__':
    convert()
    test()