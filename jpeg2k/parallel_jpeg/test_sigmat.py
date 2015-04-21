from myhdl import *
from sigmat import SignalMatrix, m_flat_top
import  random
W0 = 9
matrix = SignalMatrix()
flati = matrix.get_flat_signal()
flato = matrix.get_flat_signal()
nbits = len(flati)
print nbits

clock = Signal(bool(0))
reset = ResetSignal(0, active=1, async=False)

sdo = Signal(bool(0))


def test_matrix(clock, reset, sdo):
    @always(delay(10))
    def clkgen():
        clock.next = not clock
    dut = m_flat_top( clock, reset, sdo)
    gstk = matrix.m_stack(flati)
    gflt = matrix.m_flatten(flato)
    @instance
    def tbsim():
        yield clock.posedge 
        reset.next = 1
        yield clock.posedge 
        reset.next = 0
        yield clock.posedge
        #flati.next = 160
        #gstk_g_0_y.next = 160
        yield clock.posedge 
        #sdi.next = 1
        yield clock.posedge
        #sdi.next = 0
        yield clock.posedge  
        for j in range(512):
            j = random.randrange(0,2**(W0-1))
            
            print ("time %d j  %d j %s") % (now(), j, hex(j))
            flati.next = j
            print ("time %d  flati %s") % (now(), hex(flati))          
            yield clock.posedge
            flati.next = j << 9
            print ("time %d  flati %s") % (now(), hex(flati))          
            yield clock.posedge
            flati.next = j << 18
            print ("time %d  flati %s") % (now(), hex(flati))          
            yield clock.posedge
            flati.next = j << 27
            print ("time %d  flati %s") % (now(), hex(flati))          
            yield clock.posedge
            flati.next = j << 36
            print ("time %d  flati %s") % (now(), hex(flati))          
            yield clock.posedge        

 
 
             
        raise StopSimulation
    return dut, clkgen, tbsim, gstk, gflt
tb_fsm = traceSignals(test_matrix, clock, reset, sdo)
sim = Simulation(tb_fsm)
sim.run()

