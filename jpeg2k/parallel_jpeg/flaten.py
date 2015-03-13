from myhdl import *
import  random

def m_flatten(matrix, flat):
	_flat = ConcatSignal(*[mcol(10,0) for mrow in matrix for mcol in mrow])
	@always_comb
	def rtl():
		flat.next = _flat
	return rtl


def test_flatten():

	matrix = [[Signal(intbv(0)[10:]) for mcol in range(4)] for mrow in range(4)]
	flat = Signal(intbv(0)[160:])
	tbdut = m_flatten(matrix, flat)
	@instance
	def tbstim():
		yield delay(1)
		print(bin(flat, 160))
		y = random.randrange(0,1024)
		for mrow in range(3,-1,-1):
			for mcol in range(3,-1,-1):

				matrix[mrow][mcol].next = y

				print mrow, mcol, y
				y = y + 1

				yield delay(1)
				print(bin(flat, 160))


	return tbdut, tbstim
Simulation(test_flatten()).run()
