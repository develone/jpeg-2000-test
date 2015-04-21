from myhdl import *
from sigmat import SignalMatrix, m_flat_top
import  random
W0 = 9
matrix = SignalMatrix()
flati = matrix.get_flat_signal()
flato = matrix.get_flat_signal()
clock = Signal(bool(0))
reset = ResetSignal(0, active=1, async=False)
sdi = Signal(bool(0))
sdo = Signal(bool(0))
#sdi = Signal(intbv(0)[W0:])
#sdo = Signal(intbv(0)[W0:])
def test_matrix(clock, reset, sdi, sdo):
    @always(delay(10))
    def clkgen():
        clock.next = not clock
    dut = m_flat_top( clock, reset, sdi, sdo)
    
    @instance
    def tbsim():
        yield clock.posedge 
        reset.next = 1
        yield clock.posedge 
        reset.next = 0
        for j in range(512):
            j = random.randrange(-2**(W0-1),2**(W0-1))
            print j
            reset.next = 1
            #row(0).next = 3
            yield clock.posedge 
            reset.next = 0
            #row(0).next = 2  
            yield clock.posedge 
        raise StopSimulation
    return dut, clkgen, tbsim
tb_fsm = traceSignals(test_matrix, clock, reset, sdi, sdo)
sim = Simulation(tb_fsm)
sim.run()

