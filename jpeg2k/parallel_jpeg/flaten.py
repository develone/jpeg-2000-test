from myhdl import *
from jpeg_constants import *
import  random

def m_flatten(matrix, flat):
	_flat = ConcatSignal(*[mcol(W0,0) for mrow in matrix for mcol in mrow])
	@always_comb
	def rtl():
		flat.next = _flat
	return rtl


def test_flatten():

	matrix = [[Signal(intbv(0)[W0:]) for mcol in range(4)] for mrow in range(4)]
	flat = Signal(intbv(0)[W0*LVL0:])
	tbdut = m_flatten(matrix, flat)
	@instance
	def tbstim():
		yield delay(1)
		print(bin(flat, 192))
		for j in range(512):
			j = random.randrange(-2**(W0-1),2**(W0-1))
			x = Signal(intbv(j, min=-2**(W0-1), max=2**(W0-1)))
			z = Signal(intbv(0)[W0:])
			for mrow in range(3,-1,-1):
				for mcol in range(3,-1,-1):
					z = x[W0:]
					print bin(z,W0)
					matrix[mrow][mcol].next = z

					print mrow, mcol, z.signed()

					if (flat[W0:0] == flat[W0*LVL0:150]):
						print 'lsb', flat[W0:0],  flat[W0:0].signed(),'msb', flat[W0*LVL0:(W0*LVL0)-W0],  flat[W0*LVL0:(W0*LVL0)-W0].signed()

					yield delay(1)
					print(bin(flat, W0*LVL0))
			'''
			for mrow in range(3,-1,-1):
				for mcol in range(3,-1,-1):

					print bin(z,10)
					matrix[mrow][mcol].next = 0
					yield delay(1)
					print(bin(flat, 160))
			'''
	return tbdut, tbstim
#Simulation(test_flatten()).run()
def convert():
	matrix = [[Signal(intbv(0)[W0:]) for mcol in range(4)] for mrow in range(4)]
	flat = Signal(intbv(0)[W0*LVL0:])
	toVerilog(m_flatten, matrix, flat)
	toVHDL(m_flatten, matrix, flat)
#convert()
