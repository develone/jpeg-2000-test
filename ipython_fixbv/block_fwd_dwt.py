from PIL import Image
im = Image.open("../lena_256.png")
#im = Image.open("block_256_fwt.png")
pix = im.load()
w, h = im.size
m = list(im.getdata())
'''transform 1D list to 2D'''
m = [m[i:i+im.size[0]] for i in range(0, len(m), im.size[0])]

def lower_upper(s, width, height):

	temp_bank = [[0]*width for i in range(height)]
	for col in range(width/2,width,1):

		for row in range(height/2,height,1):

			temp_bank[col-width/2][row-height/2] = s[row][col]

	for row in range(width):
		for col in range(height):
			s[row][col] = temp_bank[col][row]
	return s

def print_list(cblk):
    for i in range(8):
         
        print "{:6s}".format(cblk[i])
    print ""

def seq_to_img(m, pix):
    ''' Copy matrix m to pixel buffer pix.
    Assumes m has the same number of rows and cols as pix. '''
    for row in range(len(m)):
        for col in range(len(m[row])):
            pix[col,row] = m[row][col]

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
def block_dwt(s):
    '''m is transferred to 8 rows at time''' 
    for r in range(0,256,8):
        r0 = s[r]
        r1 = s[r+1]
        r2 = s[r+2]
        r3 = s[r+3]
        r4 = s[r+4]
        r5 = s[r+5]
        r6 = s[r+6]
        r7 = s[r+7]
        #print r, r+1, r+2, r+3, r+4, r+5, r+6, r+7
        #print r0
        #print r7
        for a in range(0,256,8):
            b = a + 8
            #print a, b
            '''8 rows of 8 values are used to create the cblk'''
            cblk = [r0[a:b], r1[a:b], r2[a:b], r3[a:b], r4[a:b], r5[a:b], r6[a:b], r7[a:b]]
            extra_row_top = []
            extra_row_bot = []
            for j in range(8):
                extra_row_top.append(cblk[0][j])
                extra_row_bot.append(cblk[7][j])
            print 'extra top', extra_row_top
            print 'extra bot', extra_row_bot
            print 
            '''i is the row
            j is the col of an 8x8 cblk
            odd samples'''
    
            '''8 x 8 cblk prior to fwd dwt'''
            print 'prior'
            print_list(cblk)
            '''
            This is the first 8 x 8 cblk from the image
            ../lena_256.png
            [156, 156, 164, 164, 164, 164, 156, 164]
            [164, 164, 164, 164, 164, 164, 156, 164]
            [164, 164, 164, 164, 164, 164, 156, 156]
            [164, 164, 164, 156, 156, 156, 156, 156]
            [156, 156, 156, 156, 164, 156, 156, 156]
            [156, 156, 156, 156, 156, 156, 164, 156]
            [156, 156, 156, 164, 156, 164, 156, 156]
            [164, 156, 156, 156, 156, 156, 156, 156]
            
            [246, 246, 256, 257, 257, 257, 244, 256]
            [203, 203, 205, 206, 206, 206, 195, 204]
            [0, 0, 0, 4, 4, 4, 0, -4]
            [163, 163, 163, 157, 159, 157, 155, 155]
            [-4, -4, -4, 0, 8, 0, -4, 0]
            [154, 155, 155, 158, 158, 158, 162, 156]
            [-4, 0, 0, 8, 0, 8, -4, 0]
            [126, 117, 117, 115, 117, 115, 118, 117]
 
            '''

            for i in range(8):
                '''i is the col of an 8x8 cblk
                j is the row of an 8x8 cblk
                even samples'''
                '''fwd dwt for even samples'''
                for j in range(2,8,2):
                    #print 'even',j,i,cblk[j-1][i], cblk[j][i], cblk[j+1][i]
                    cblk[j][i] = cblk[j][i] - ((cblk[j-1][i] + cblk[j+1][i])>>1)
                    #print 'even dwt',j,i,j-1, j+1, cblk[j][i]
                '''i is the col of an 8x8 cblk
                j is the row of an 8x8 cblk
                fwd dwt for odd samples'''
                for j in range(1,9-1,2):
                    #print 'odd',j,i,cblk[j-1][i], cblk[j][i], cblk[j+1][i]
                    if (j < 7):
                        cblk[j][i] = cblk[j][i] + (((cblk[j-1][i]) + (cblk[j + 1][i]) + 2)>>2)
                        #print j, i,j-1,j+1,  cblk[j-1][i], cblk[j][i], cblk[j+1][i]
                    else:
                        cblk[j][i] = cblk[j][i] - (((cblk[j-1][i]) + (extra_row_bot[j]) +2)>>2)
                        #cblk[j][i] = cblk[j][i] - ((cblk[j-1][i] + extra_row_bot[j])>>1)
                        #print  j, i,  cblk[j-1][i], cblk[j][i], extra_row_bot[i]
                #print 'odd',j,i,j-1,j+1,cblk[j][i]
                #print_list()
                
                
            for j in range(8): 
                cblk[0][j] = cblk[0][j] + ((extra_row_top[j] + cblk[1][j] + 2)>>2)
                #print 'even extra row dwt',j, cblk[0][j],extra_row_top[j] , cblk[1][j]
                
            '''8 x 8 cblk after fwd dwt''' 
            print 'after'
            print_list(cblk),
            print len(cblk[0]), len(cblk[1]), r, a, b
         
            c0 = cblk[0]
            c1 = cblk[1]
            c2 = cblk[2]
            c3 = cblk[3]
            c4 = cblk[4]
            c5 = cblk[5]
            c6 = cblk[6]
            c7 = cblk[7]
            #print c0, c1, c2, c3, c4,c5, c6,c7
            '''r is the column'''
            
            for jj in range(8):
                '''cblk values need 0 to 7'''
                s[r][jj+a] = c0[jj]
                s[r+1][jj+a] = c1[jj]
                s[r+2][jj+a] = c2[jj]
                s[r+3][jj+a] = c3[jj]
                s[r+4][jj+a] = c4[jj]
                s[r+5][jj+a] = c5[jj]
                s[r+6][jj+a] = c6[jj]
                s[r+7][jj+a] = c7[jj]
            
            print s[r][a], s[r][a+1], s[r][a+2], s[r][a+3], s[r][a+4], s[r][a+5], s[r][a+6], s[r][a+7] 
            print s[r+1][a], s[r+1][a+1], s[r+1][a+2], s[r+1][a+3], s[r+1][a+4], s[r+1][a+5], s[r+1][a+6], s[r+1][a+7]
            print s[r+2][a], s[r+2][a+1], s[r+2][a+2], s[r+2][a+3], s[r+2][a+4], s[r+2][a+5], s[r+2][a+6], s[r+2][a+7]
            print s[r+3][a], s[r+3][a+1], s[r+3][a+2], s[r+3][a+3], s[r+3][a+4], s[r+3][a+5], s[r+3][a+6], s[r+3][a+7]
            print s[r+4][a], s[r+4][a+1], s[r+4][a+2], s[r+4][a+3], s[r+4][a+4], s[r+4][a+5], s[r+4][a+6], s[r+4][a+7]
            print s[r+5][a], s[r+5][a+1], s[r+5][a+2], s[r+5][a+3], s[r+5][a+4], s[r+5][a+5], s[r+5][a+6], s[r+5][a+7]
            print s[r+6][a], s[r+6][a+1], s[r+6][a+2], s[r+6][a+3], s[r+6][a+4], s[r+6][a+5], s[r+6][a+6], s[r+6][a+7]
            print s[r+7][a], s[r+7][a+1], s[r+7][a+2], s[r+7][a+3], s[r+7][a+4], s[r+7][a+5], s[r+7][a+6], s[r+7][a+7]
            ''' cblk needs to be put back into m'''
    de_interleave(s,256,256)
    return s

m = block_dwt(m)
m = block_dwt(m)
#lower_upper(m,256,256)
seq_to_img(m, pix)
im.save("block_256_fwt.png")
