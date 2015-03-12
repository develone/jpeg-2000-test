from myhdl import *
def m_flatten(matrix, flat):
	_flat = ConcatSignal(*[col(4,0) for row in matrix for col in row])
	@always_comb
	def rtl():
		flat.next = _flat
	return rtl


def test_flatten():
	matrix = [[Signal(intbv(0)[8:]) for col in range(5)] for row in range(8)]
	flat = Signal(intbv(0)[160:])
	tbdut = m_flatten(matrix, flat)
	@instance
	def tbstim():
		yield delay(1)
		print(bin(flat, 160))
		assert flat == 0
		matrix[0][0].next = 0x8
		yield delay(1)
		print(bin(flat, 160))
		assert flat[160-1] == 1
		matrix[0][1].next = 0xf
		yield delay(1)
		print(bin(flat, 160))
		matrix[0][2].next = 0x8
		yield delay(1)
		print(bin(flat, 160))
		matrix[0][3].next = 0x5
		yield delay(1)
		print(bin(flat, 160))
		matrix[0][4].next = 0xa
		yield delay(1)
		print(bin(flat, 160))

 		matrix[2][0].next = 0x8
		yield delay(1)
		print(bin(flat, 160))
		#assert flat[160-1] == 1
		matrix[2][1].next = 0xf
		yield delay(1)
		print(bin(flat, 160))
		matrix[2][2].next = 0x8
		yield delay(1)
		print(bin(flat, 160))
		matrix[2][3].next = 0x5
		yield delay(1)
		print(bin(flat, 160))
		matrix[2][4].next = 0xa
		yield delay(1)
		print(bin(flat, 160))


	return tbdut, tbstim
Simulation(test_flatten()).run()
