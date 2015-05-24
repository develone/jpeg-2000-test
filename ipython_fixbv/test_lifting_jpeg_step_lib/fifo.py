from myhdl import *
#toVHDL.numeric_ports = False
from PIL import Image
im = Image.open("../../lena_256.png")
pix = im.load()
w, h = im.size
m = list(im.getdata())
m = [m[i:i+im.size[0]] for i in range(0, len(m), im.size[0])]
#print m

reset_dly_c = 10
ASZ = 8
DSZ = 9
NO = bool(0)
YES = bool(1)

clk = Signal(bool(0))

enw_r = Signal(bool(0))
enr_r = Signal(bool(0))
empty_r = Signal(bool(0))
full_r = Signal(bool(0))
dataout_r = Signal(intbv(0)[DSZ:])
datain_r = Signal(intbv(0)[DSZ:])
'''
enw_x = Signal(bool(0))
enr_x = Signal(bool(0))
empty_x = Signal(bool(0))
full_x = Signal(bool(0))
dataout_x = Signal(intbv(0)[DSZ:])
datain_x = Signal(intbv(0)[DSZ:])
'''
readptr = Signal(intbv(0)[ASZ:])
writeptr = Signal(intbv(0)[ASZ:])
mem = [Signal(intbv(0)[DSZ:]) for ii in range(2**ASZ)]
def fifo(clk, empty_r, full_r, enr_r, enw_r, dataout_r, datain_r ):
    """The following between the single quotes ':= "0000"' needs to added to line below
    signal instance_1_reset_ctn: unsigned(3 downto 0);
    before the ';' to be like the following
    signal instance_1_reset_ctn: unsigned(3 downto 0):= "0000";
     """
    readptr = Signal(intbv(0)[ASZ:])
    writeptr = Signal(intbv(0)[ASZ:])
    reset_ctn = Signal(intbv(val=0, min=0, max=16))
    mem = [Signal(intbv(0)[DSZ:]) for ii in range(2**ASZ)]
    @always(clk.posedge)
    def rtl():
        if (reset_ctn < reset_dly_c):
            readptr.next = 0
            writeptr.next = 0
            reset_ctn.next = reset_ctn + 1
        if ( enr_r == YES):
            dataout_r.next = mem[int(readptr)]
            readptr.next = readptr + 1
        if (enw_r == YES):
            mem[int(writeptr)].next = datain_r
            writeptr.next = writeptr + 1
        if  (readptr == (2**ASZ-1)):
            readptr.next = 0
        if (writeptr == (2**ASZ-1)):
            full_r.next = YES
            writeptr.next = 0
        else:
            full_r.next = NO
        if (writeptr == 0):
            empty_r.next = YES
        else:
            empty_r.next = NO

         
    return rtl
def tb(clk, empty_r, full_r, enr_r, enw_r, dataout_r, datain_r):
    instance_pc_in = fifo(clk, empty_r, full_r, enr_r, enw_r, dataout_r, datain_r)
    @always(delay(10))
    def clkgen():
        clk.next = not clk
    @instance
    def stimulus():
        empty_r.next = 0
        yield clk.posedge
        full_r.next = 0
        yield clk.posedge
        enr_r.next = 0
        yield clk.posedge
        enw_r.next = 0
        yield clk.posedge
        for i in range(20):
            yield clk.posedge

        datain_r.next = m[0][0]
        yield clk.posedge
        enw_r.next = 1
        yield clk.posedge
        for j in range(1,255):
            k = 0
            datain_r.next = m[j][k]
            #print m[j][k]
            yield clk.posedge
 
        enw_r.next = 0
        yield clk.posedge

        for i in range(4):
            yield clk.posedge
        enr_r.next = 1
        yield clk.posedge 
        for j in range(255):
            print ("%d %d %d") % (now(), j, dataout_r)
            yield clk.posedge
        raise StopSimulation
    return instances()
#tbfsm = traceSignals(tb,clk, empty_r, full_r, enr_r, enw_r, dataout_r, datain_r)

#sim = Simulation(tbfsm)
#sim.run()

toVHDL(fifo,clk, empty_r, full_r, enr_r, enw_r, dataout_r, datain_r)

