import wavelet97lift as dwt

im = dwt.Image.open("../lena_256.png")
pix = im.load()
m = list(im.getdata())
m = [m[i:i+im.size[0]] for i in range(0, len(m), im.size[0])]

#Cast every item in the list to a float:
for row in range(0, len(m)):
        for col in range(0, len(m[0])):
                m[row][col] = float(m[row][col])

im1 = dwt.Image.open("test1_256_iwt.png")
pix = im1.load()
m1 = list(im1.getdata())
m1 = [m1[i:i+im1.size[0]] for i in range(0, len(m1), im1.size[0])]
#Cast every item in the list to a float:
for row in range(0, len(m1)):
        for col in range(0, len(m1[0])):
                m1[row][col] = float(m1[row][col])
max = 0.0
d_sum = 0.0
for row in range(0, len(m1)):
        for col in range(0, len(m1[0])):
			mse = (m[row][col] - m1[row][col]) **2
			d = m[row][col] - m1[row][col]
			if d >= max:
				max = d
                                print row,col,max
			#print mse

#print 1/(im1.size[0]*im1.size[1])
print 'mse = ',mse/(im1.size[0]*im1.size[1])
print 'max = ', max
