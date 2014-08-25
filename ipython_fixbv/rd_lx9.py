from intelhex import IntelHex
ih_ttt = IntelHex()                     # create empty object
ih_ttt.loadhex('ttt.hex')               # load from bin
ih_lena = IntelHex()                     # create empty object
ih_lena.loadhex('lena.hex')

print len(ih_lena)
for i in range(len(ih_ttt)):
	print i, ih_ttt[i], ih_lena[i]
