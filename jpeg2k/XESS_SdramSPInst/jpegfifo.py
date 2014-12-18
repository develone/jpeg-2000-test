
# Copyright (c) 2006-2013 Christopher L. Felton
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from myhdl import *
NO = bool(0)
YES = bool(1)
ASZ = 8
DSZ = 16


clk_fast = Signal(bool(0))
enw_r = Signal(bool(0))
enr_r = Signal(bool(0))
empty_r = Signal(bool(0))
full_r = Signal(bool(0))
dataout_r = Signal(intbv(0)[DSZ:])
datain_r = Signal(intbv(0)[DSZ:])

enw_x = Signal(bool(0))
enr_x = Signal(bool(0))
empty_x = Signal(bool(0))
full_x = Signal(bool(0))
dataout_x = Signal(intbv(0)[DSZ:])
datain_x = Signal(intbv(0)[DSZ:])

readptr = Signal(intbv(0)[ASZ:])
writeptr = Signal(intbv(0)[ASZ:])
mem = [Signal(intbv(0)[DSZ:]) for ii in range(2**ASZ)]
def jpegfifo(clk_fast, empty_r, full_r, enr_r, enw_r, dataout_r, datain_r ):
    """Following the code being converted requires the that both readptr
    writeptr be initialized :="00000000" """
    readptr = Signal(intbv(0)[ASZ:])
    writeptr = Signal(intbv(0)[ASZ:])
    mem = [Signal(intbv(0)[DSZ:]) for ii in range(2**ASZ)]
    @always(clk_fast.posedge)
    def rtl():
        if ( enr_r == YES):
            dataout_x.next = mem[int(readptr)]
            readptr.next = readptr + 1
        if (enw_r == YES):
            mem[int(writeptr)].next = datain_x    
            writeptr.next = writeptr + 1
        if  (readptr == 255):
                readptr.next = 0
        if (writeptr == 255):
            full_x.next = YES
            writeptr.next = 0
        else:
            full_x.next = NO
        if (writeptr == 0):
            empty_x.next = YES
        else:
            empty_x.next = NO
        

    return rtl

def jpegfsmupdate(clk_fast, empty_r, full_r, enr_r, enw_r, dataout_r, datain_r, empty_x, full_x, enr_x, enw_x, dataout_x, datain_x):
    @always(clk_fast.posedge)
    def fsmupdate():
        empty_r.next = empty_x
        full_r.next = full_x
        enr_r.next = enr_x
        enw_r.next = enw_x
        dataout_r.next = dataout_x
        datain_r.next = datain_x
    return fsmupdate
def jpeg_fifo_fsmupdate(clk_fast,
                        empty_r,
                        full_r,
                        enr_r,
                        enw_r,
                        dataout_r,
                        datain_r,
                        empty_x,
                        full_x,
                        enr_x,
                        enw_x,
                        dataout_x,
                        datain_x):
    instance_1 = jpegfifo(clk_fast,
                          empty_r,
                          full_r,
                          enr_r,
                          enw_r,
                          dataout_r,
                          datain_r)
    instance_2 = jpegfsmupdate(clk_fast,
                               empty_r,
                               full_r,
                               enr_r,
                               enw_r,
                               dataout_r,
                               datain_r,
                               empty_x,
                               full_x,
                               enr_x,
                               enw_x,
                               dataout_x,
                               datain_x)
    return instance_1, instance_2
if __name__ == '__main__':
    #toVHDL(jpegfifo, clk_fast, empty_r, full_r, enr_r, enw_r, dataout_r, datain_r)
    #toVHDL(jpegfsmupdate, clk_fast, empty_r, full_r, enr_r, enw_r, dataout_r, datain_r, empty_x, full_x, enr_x, enw_x, dataout_x, datain_x)
    toVHDL(jpeg_fifo_fsmupdate, clk_fast, empty_r, full_r, enr_r, enw_r, dataout_r, datain_r, empty_x, full_x, enr_x, enw_x, dataout_x, datain_x)
