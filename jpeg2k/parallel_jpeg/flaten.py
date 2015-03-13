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
		for j in range(512):
			j = random.randrange(-512,512)
			x = Signal(intbv(j, min=-512, max=512))
			z = Signal(intbv(0)[10:])
			for mrow in range(3,-1,-1):
				for mcol in range(3,-1,-1):
					z = x[10:]
					print bin(z,10)
					matrix[mrow][mcol].next = z

					print mrow, mcol, z.signed()

					if (flat[10:0] == flat[160:150]):
						print 'lsb', flat[10:0],  flat[10:0].signed(),'msb', flat[160:150],  flat[160:150].signed()

					yield delay(1)
					print(bin(flat, 160))
			'''
			for mrow in range(3,-1,-1):
				for mcol in range(3,-1,-1):

					print bin(z,10)
					matrix[mrow][mcol].next = 0
					yield delay(1)
					print(bin(flat, 160))
			'''
	return tbdut, tbstim
Simulation(test_flatten()).run()
