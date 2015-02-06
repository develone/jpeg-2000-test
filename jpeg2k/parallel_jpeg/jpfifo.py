from myhdl import *
from jpeg_constants import *
#force std_logic_vectors
#toVHDL.numeric_ports = False
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
clk_fast = Signal(bool(0))
def jpegfifo(clk_fast, empty_r, full_r, enr_r, enw_r, dataout_r, datain_r ):
    """Following the code being converted requires the that both readptr
    writeptr be initialized :="00000000" """
    readptr = Signal(intbv(0)[ASZ:])
    writeptr = Signal(intbv(0)[ASZ:])
    reset_ctn = Signal(intbv(val=0, min=0, max=16))
    mem = [Signal(intbv(0)[DSZ:]) for ii in range(2**ASZ)]
    @always(clk_fast.posedge)
    def rtl():     
        if (reset_ctn < reset_dly_c):
            readptr.next = 0
            writeptr.next = 0
            reset_ctn.next = reset_ctn + 1
        if ( enr_r == YES):
            dataout_x.next = mem[int(readptr)]
            readptr.next = readptr + 1
        if (enw_r == YES):
            mem[int(writeptr)].next = datain_x    
            writeptr.next = writeptr + 1
        if  (readptr == (2**ASZ-1)):
            readptr.next = 0
        if (writeptr == (2**ASZ -1)):
            full_x.next = YES
            writeptr.next = 0
        else:
            full_x.next = NO
        if (writeptr == 0):
            empty_x.next = YES
        else:
            empty_x.next = NO
    return rtl
#toVHDL(jpegfifo, clk_fast, empty_r, full_r, enr_r, enw_r, dataout_r, datain_r )