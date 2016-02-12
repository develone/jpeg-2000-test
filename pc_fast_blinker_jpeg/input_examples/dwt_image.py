from PIL import Image # Part of the standard Python Library
def lower_upper(s, width, height):

	temp_bank = [[0]*width for i in range(height)]
	for col in range(width/2,width,1):

		for row in range(height/2,height,1):

			temp_bank[col-width/2][row-height/2] = s[row][col]

	for row in range(width):
		for col in range(height):
			s[row][col] = temp_bank[col][row]
	return s
def de_interleave(s,height,width):
	# de-interleave
	temp_bank = [[0]*width for i in range(height)]
	for row in range(width):
		for col in range(width):
            # k1 and k2 scale the vals
            # simultaneously transpose the matrix when deinterleaving
			if row % 2 == 0:

				temp_bank[col][row/2] =  s[row][col]
			else:

				temp_bank[col][row/2 + height/2] =  s[row][col]
    # write temp_bank to s:
	for row in range(width):
		for col in range(height):
			s[row][col] = temp_bank[row][col]
	return s

def seq_to_img(m, pix):
    ''' Copy matrix m to pixel buffer pix.
    Assumes m has the same number of rows and cols as pix. '''
    for row in range(len(m)):
        for col in range(len(m[row])):
            pix[col,row] = m[row][col]

def rd_img(imgfn): 
    im = Image.open(imgfn)
    pix = im.load()
    m = list(im.getdata())
    #print m.__sizeof__()
    m = [m[i:i+im.size[0]] for i in range(0, len(m), im.size[0])]
    return im, m, pix

def lsr(row,col,m,flag):
    x0 = m[row-1][col] << 18
    x1 = m[row][col] << 9
    x2 = m[row+1][col]
    f = flag << 27
    #upd = 0 << 30
    return (f+x0+x1+x2)
