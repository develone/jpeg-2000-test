from myhdl import *
W0 = 9
#toVHDL.numeric_ports = False
from PIL import Image
im = Image.open("../lena_256.png")
pix = im.load()
w, h = im.size
m = list(im.getdata())
m = [m[i:i+im.size[0]] for i in range(0, len(m), im.size[0])]
#print m

reset_dly_c = 2
ASZ = 2
DSZ = 9
NO = bool(0)
YES = bool(1)

clk = Signal(bool(0))

enw_L = Signal(bool(0))
enr_L = Signal(bool(0))
empty_L = Signal(bool(0))
full_L = Signal(bool(0))
dataout_L = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
datain_L = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))

enw_S = Signal(bool(0))
enr_S = Signal(bool(0))
empty_S = Signal(bool(0))
full_S = Signal(bool(0))
dataout_S = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
datain_S = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))

enw_R = Signal(bool(0))
enr_R = Signal(bool(0))
empty_R = Signal(bool(0))
full_R = Signal(bool(0))
dataout_R = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
datain_R = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
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
mem = [Signal(intbv(0, min=-(2**(W0)), max=(2**(W0)))) for ii in range(2**ASZ)]
def fifo(clk, empty_L, full_L, enr_L, enw_L, dataout_L, datain_L ):
    """The following between the single quotes ':= "0000"' needs to added to line below
    signal instance_1_reset_ctn: unsigned(3 downto 0);
    before the ';' to be like the following
    signal instance_1_reset_ctn: unsigned(3 downto 0):= "0000";
     """
    readptr = Signal(intbv(0)[ASZ:])
    writeptr = Signal(intbv(0)[ASZ:])
    reset_ctn = Signal(intbv(val=0, min=0, max=16))
    mem = [Signal(intbv(0, min=-(2**(W0)), max=(2**(W0)))) for ii in range(2**ASZ)]
    @always(clk.posedge)
    def rtl():
        if (reset_ctn < reset_dly_c):
            readptr.next = 0
            writeptr.next = 0
            reset_ctn.next = reset_ctn + 1
        if ( enr_L == YES):
            dataout_L.next = mem[int(readptr)]
            if (readptr < (2**ASZ-1)):
                readptr.next = readptr + 1
        if (enw_L == YES):
            mem[int(writeptr)].next = datain_L
            writeptr.next = writeptr + 1
        if  (readptr == (2**ASZ-1)):
            readptr.next = 0
        if (writeptr == (2**ASZ-1)):
            full_L.next = YES
            writeptr.next = 0
        else:
            full_L.next = NO
        if (writeptr == 0):
            empty_L.next = YES
        else:
            empty_L.next = NO

         
    return rtl


LeSo = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
Se = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
Ro = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
L = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
S = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
R = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
res_o = Signal(intbv(0, min=-(2**(W0)), max=(2**(W0))))
muxsel_ev_od = Signal(bool(0))
clk = Signal(bool(0))
update_i = Signal(bool(0))
update_o = Signal(bool(0))
flgs_i = Signal(intbv(0)[4:])
 
def lift_step(L, S, R, flgs_i, update_i, clk, res_o, update_o):
    @always(clk.posedge)
    def rtl ():
        if (update_i == 1):
            update_o.next = 0
            if (flgs_i == 7):
                res_o.next = S - ( (L >> 1) + (R >> 1) )

            elif (flgs_i == 5):
                res_o.next = S + ( (L >> 1) + (R >> 1) )
            elif (flgs_i == 6):
                res_o.next = S + ( (L + R + 2) >> 2 )
            elif (flgs_i == 4):
                res_o.next = S - ( (L + R + 2) >> 2 )
        else:
            update_o.next = 1
    return rtl   
def mux_data(LeSo, Se, Ro, muxsel_ev_od ):
    @always_comb
    def muxLogic():
        LeSo.next = Se
	if (muxsel_ev_od == 1):
	    LeSo.next = Ro
			
    return muxLogic
def top_lift(LeSo, Se, Ro, muxsel_ev_od, L, S, R, flgs_i, update_i, clk, res_o, update_o,
empty_L, full_L, enr_L, enw_L, dataout_L, datain_L,
empty_S, full_S, enr_S, enw_S, dataout_S, datain_S,
empty_R, full_R, enr_R, enw_R, dataout_R, datain_R): 
    dut = mux_data(LeSo, Se, Ro, muxsel_ev_od)
    dut1 = lift_step(L, S, R, flgs_i, update_i, clk, res_o, update_o)
    dut2 = fifo(clk, empty_L, full_L, enr_L, enw_L, dataout_L, datain_L )
    dut3 = fifo(clk, empty_S, full_S, enr_S, enw_S, dataout_S, datain_S )
    dut4 = fifo(clk, empty_R, full_R, enr_R, enw_R, dataout_R, datain_R )
    return instances()		
def convert():
	toVHDL(mux_data, LeSo, Se, Ro, muxsel_ev_od)
	toVerilog(mux_data, LeSo, Se, Ro, muxsel_ev_od)
#convert()
def tb(	LeSo, Se, Ro, muxsel_ev_od, L, S, R, flgs_i, update_i, res_o, update_o, 
empty_L, full_L, enr_L, enw_L, dataout_L, datain_L,
empty_S, full_S, enr_S, enw_S, dataout_S, datain_S,
empty_R, full_R, enr_R, enw_R, dataout_R, datain_R):
    dut = mux_data(LeSo, Se, Ro, muxsel_ev_od)
    dut1 = lift_step(L, S, R, flgs_i, update_i, clk, res_o, update_o)
    dut2 = fifo(clk, empty_L, full_L, enr_L, enw_L, dataout_L, datain_L )
    dut3 = fifo(clk, empty_S, full_S, enr_S, enw_S, dataout_S, datain_S )
    dut4 = fifo(clk, empty_R, full_R, enr_R, enw_R, dataout_R, datain_R )
    @always(delay(10))
    def clkgen():
        clk.next = not clk
    @instance
    def stimulus():
        for i in range(10):
            yield clk.posedge
        
        datain_L.next = 160
        #yield clk.posedge
        enw_L.next = 1
        yield clk.posedge
        enw_L.next = 0
        yield clk.posedge
        datain_L.next = 162
        #yield clk.posedge
        enw_L.next = 1
        yield clk.posedge
        enw_L.next = 0
        yield clk.posedge
        datain_L.next = 164
        #yield clk.posedge
        enw_L.next = 1
        yield clk.posedge
        enw_L.next = 0
        yield clk.posedge
        
        datain_S.next = 162
        yield clk.posedge
        enw_S.next = 1
        yield clk.posedge
        enw_S.next = 0
        yield clk.posedge
        datain_S.next = 164
        yield clk.posedge
        enw_S.next = 1
        yield clk.posedge
        enw_S.next = 0
        yield clk.posedge
        datain_S.next = 166
        yield clk.posedge
        enw_S.next = 1
        yield clk.posedge
        enw_S.next = 0
        yield clk.posedge

        datain_R.next = 172
        yield clk.posedge
        enw_R.next = 1
        yield clk.posedge
        enw_R.next = 0
        yield clk.posedge
        datain_R.next = 174
        yield clk.posedge
        enw_R.next = 1
        yield clk.posedge
        enw_R.next = 0
        yield clk.posedge
        datain_R.next = 176
        yield clk.posedge
        enw_R.next = 1
        yield clk.posedge
        enw_R.next = 0
        yield clk.posedge
        
        enr_L.next = 1
        enr_S.next = 1
        enr_R.next = 1
        yield clk.posedge
        enr_L.next = 0
        enr_S.next = 0
        enr_R.next = 0
        yield clk.posedge

        enr_L.next = 1
        enr_S.next = 1
        enr_R.next = 1
        yield clk.posedge
        enr_L.next = 0
        enr_S.next = 0
        enr_R.next = 0

        yield clk.posedge

        enr_L.next = 1
        enr_S.next = 1
        enr_R.next = 1
        yield clk.posedge
        enr_L.next = 0
        enr_S.next = 0
        enr_R.next = 0
        yield clk.posedge
 

        muxsel_ev_od.next = 0
        yield clk.posedge

 

        S.next = 160
        yield clk.posedge

        Se.next = 164
        R.next = LeSo
        yield clk.posedge

        muxsel_ev_od.next = 1
        R.next = LeSo
        yield clk.posedge

        Se.next = 162
        yield clk.posedge
        Se.next = 158
        yield clk.posedge
        Ro.next = 164

        flgs_i.next = 7
        yield clk.posedge
        update_i.next = 1
        yield clk.posedge
        update_i.next = 0

        muxsel_ev_od.next = 1
        yield clk.posedge
        Ro.next = 166
        yield clk.posedge
        Ro.next = 162


        yield clk.posedge
        L.next = 162
        yield clk.posedge
        S.next = 160
        yield clk.posedge
        R.next = 164
        yield clk.posedge
        flgs_i.next = 7
        yield clk.posedge
        update_i.next = 1
        yield clk.posedge
        update_i.next = 0
        yield clk.posedge
        flgs_i.next = 5
        yield clk.posedge
        update_i.next = 1
        yield clk.posedge
        update_i.next = 0
        yield clk.posedge
        flgs_i.next = 6
        yield clk.posedge
        update_i.next = 1
        yield clk.posedge
        update_i.next = 0
        yield clk.posedge
        flgs_i.next = 4
        yield clk.posedge
        update_i.next = 1
        yield clk.posedge
        update_i.next = 0
        yield clk.posedge
        raise StopSimulation
    return instances()
tbfsm = traceSignals(tb,LeSo, Se, Ro, muxsel_ev_od, L, S, R, flgs_i, update_i, res_o, update_o,
empty_L, full_L, enr_L, enw_L, dataout_L, datain_L,
empty_S, full_S, enr_S, enw_S, dataout_S, datain_S,
empty_R, full_R, enr_R, enw_R, dataout_R, datain_R)

sim = Simulation(tbfsm)
sim.run()
'''
top_lift(LeSo, Se, Ro, muxsel_ev_od, L, S, R, flgs_i, update_i, clk, res_o, update_o,
empty_L, full_L, enr_L, enw_L, dataout_L, datain_L,
empty_S, full_S, enr_S, enw_S, dataout_S, datain_S,
empty_R, full_R, enr_R, enw_R, dataout_R, datain_R)

toVHDL(top_lift, LeSo, Se, Ro, muxsel_ev_od, L, S, R, flgs_i, update_i, clk, res_o, update_o,
empty_L, full_L, enr_L, enw_L, dataout_L, datain_L,
empty_S, full_S, enr_S, enw_S, dataout_S, datain_S,
empty_R, full_R, enr_R, enw_R, dataout_R, datain_R)
'''
