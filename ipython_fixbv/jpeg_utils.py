from myhdl import *

class Add_shift_top(object):

	def __init__(self):
		DATA_WIDTH = 65536
		ACTIVE_LOW = bool(0)
		self.even_odd = Signal(bool(0))
		self.fwd_inv = Signal(bool(0))

		self.din_sam = Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))
		self.dout_sam = Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))
		self.din_left = Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))
		self.dout_left = Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))
		self.din_right = Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))
		self.dout_right = Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))
		self.din_odd = Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))
		self.dout_odd = Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))
		self.din_even = Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))
		self.dout_even = Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))

		self.we_odd = Signal(bool(0))
		self.addr_odd = Signal(intbv(0)[8:])

		self.we_sam = Signal(bool(0))
		self.addr_sam = Signal(intbv(0)[8:])

		self.we_even = Signal(bool(0))
		self.addr_even = Signal(intbv(0)[8:])

 		self.we_left = Signal(bool(0))
		self.addr_left = Signal(intbv(0)[8:])

		self.we_right = Signal(bool(0))
		self.addr_right = Signal(intbv(0)[8:])


		self.pslverr = Signal(bool(0))
		self.prdata = Signal(intbv(0, 0, 2**32))
		self.pready = Signal(bool(0))
		self.pwdata = Signal(intbv(0, 0, 2**32))
		self.paddr = Signal(intbv(0, 0, 2**32))

		self.presetn = ResetSignal(1, ACTIVE_LOW, async=True)
		#self.kwargs = kwargs

		self.transoutrdy  = Signal(bool(0))
		#self.resetn  = Signal(bool(0))
		self.penable  = Signal(bool(0))
		self.psel  = Signal(bool(0))
		self.pwrite = Signal(bool(0))
		self.full = Signal(bool(0))
		self.pclk  = Signal(bool(0))
		self.sam = Signal(intbv(0)[8:])
		self.updated = Signal(bool(0))
		self.state_t = enum('IDLE', 'UPDATE_SAMPLE', 'TRANSFER_OUT','TRANSFER_IN')
		self.state = Signal(self.state_t.IDLE)
		self.noupdate = Signal(bool(0))

	def setSig_state_update_sample(self):
		self.state.next = Signal(self.state_t.UPDATE_SAMPLE)

	def setSig_state_transfer_out(self):
		self.state.next = Signal(self.state_t.TRANSFER_OUT)

	def setSig_state_transfer_in(self):
		self.state.next = Signal(self.state_t.TRANSFER_IN)

	def setSig_state_idle(self):
		self.state.next = Signal(self.state_t.IDLE)

	def __str__(self):
		return " %s " % self.state

	def reset(self):
		duration = self.kwargs['duration']

		print '-- Resetting --'
		self.presetn.next = False
		yield delay(duration * 5)

		print '-- Reset --'
		self.presetn.next = True
		yield delay(duration * 5)

	def setSig_we_odd(self,val):
		self.we_odd.next = Signal(bool(val))

	def setSig_we_even(self,val):
		self.we_even.next = Signal(bool(val))

	def setSig_we_left(self,val):
		self.we_left.next = (bool(val))

	def setSig_we_sam(self,val):
		self.we_sam.next = Signal(bool(val))

	def setSig_we_right(self,val):
		self.we_right.next = Signal(bool(val))

 	def setSig_addr_sam(self,val):
		self.addr_sam.next = Signal(intbv(val))

 	def setSig_addr_left(self,val):
		self.addr_left.next = Signal(intbv(val))

 	def setSig_addr_right(self,val):
		self.addr_right.next = Signal(intbv(val))

	def  setSig_addr_even(self,val):
		self.addr_even.next = Signal(intbv(val))

	def  setSig_addr_odd(self,val):
		self.addr_odd.next = Signal(intbv(val))


	def setSig_din_odd(self,val):
		DATA_WIDTH = 65536
		self.din_odd.next = Signal(intbv(val, min = -DATA_WIDTH, max = DATA_WIDTH))

	def setSig_din_sam(self,val):
		DATA_WIDTH = 65536
		self.din_sam.next = Signal(intbv(val, min = -DATA_WIDTH, max = DATA_WIDTH))

	def setSig_din_left(self,val):
		DATA_WIDTH = 65536
		self.din_left.next = Signal(intbv(val, min = -DATA_WIDTH, max = DATA_WIDTH))

	def setSig_din_right(self,val):
		DATA_WIDTH = 65536
		self.din_right.next = Signal(intbv(val, min = -DATA_WIDTH, max = DATA_WIDTH))

	def setSig_even_odd(self,val):
		self.even_odd.next = Signal(bool(val))

	def setSig_fwd_inv(self,val):
		self.fwd_inv.next = Signal(bool(val))

	def setSig_updated(self,val):
		self.updated.next = Signal(bool(val))

	def setSig_noupdate(self,val):
		self.noupdate.next = Signal(bool(val))

	def setSig_transoutrdy(self,val):
		self.transoutrdy.next = Signal(bool(val))

	def setSig_sam(self,val):
		DATA_WIDTH = 256
		self.sam.next = Signal(intbv(val, min = 0, max = DATA_WIDTH))

	def transmit(self, addr, data):
		duration = self.kwargs['duration']
		timeout = self.kwargs.get('timeout') or 5 * duration

		print '-- Transmitting addr=%s data=%s --' % (hex(addr), hex(data))
		print 'TX: start'
		self.pclk.next = True
		self.paddr.next = intbv(addr)
		self.pwrite.next = True
		self.psel.next = True
		self.pwdata.next = intbv(data)
		yield delay(duration // 2)

		self.pclk.next = False
		yield delay(duration // 2)

		print 'TX: enable'
		self.pclk.next = True
		self.penable.next = True
		yield delay(duration // 2)

		timeout_count = 0
		while not self.pready:
			print 'TX: wait'
			timeout_count += duration
		if timeout_count > timeout:
			raise Apb3TimeoutError
		self.pclk.next = False
		yield delay(duration // 2)
		self.pclk.next = True
		yield delay(duration // 2)

		self.pclk.next = False
		yield delay(duration // 2)

		print 'TX: stop'
		self.pclk.next = True
		self.pwrite.next = False
		self.psel.next = False
		self.penable.next = False
		yield delay(duration // 2)

		self.pclk.next = False
		yield delay(duration // 2)
import unittest

class TestApb3BusFunctionalModel(unittest.TestCase):
    def test_simulate(self):
        import myhdl
        duration=1

        def _sim():
            pix = Add_shift_top(duration=duration)
            pix_presetn = pix.presetn
            pix_pclk = pix.pclk
            pix_paddr = pix.paddr
            pix_psel = pix.psel
            pix_penable = pix.penable
            pix_pwrite = pix.pwrite
            pix_pwdata = pix.pwdata
            pix_pready = pix.pready
            pix_prdata = pix.prdata
            pix_pslverr = pix.pslverr

            @myhdl.instance
            def __sim():
                yield pix.reset()
                yield pix.transmit(0x4000, 0x0110)
            return __sim

        s = myhdl.Simulation(myhdl.traceSignals(_sim))
        s.run(10000)

if __name__ == '__main__':
    unittest.main()
