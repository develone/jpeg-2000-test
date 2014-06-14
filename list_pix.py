import numpy as np
#numpy.zeros(shape, dtype=float, order='C'
s = (4,4)
pix = np.zeros(s) 
def seq_to_img(m, pix):
    ''' Copy matrix m to pixel buffer pix.
    Assumes m has the same number of rows and cols as pix. '''
    for row in range(len(m)):
        for col in range(len(m[row])):
            pix[col,row] = m[row][col]
m = [ [ 2, 3, 4, 6 ] , [ 5, 6, 7, 2 ], [1, 3, 4, 5],[5, 6, 7, 8] ]
print m

def seq_to_img(m, pix):
    ''' Copy matrix m to pixel buffer pix.
    Assumes m has the same number of rows and cols as pix. '''
    
    for row in range(len(m)):
        for col in range(len(m[row])):
            pix[col,row] = m[row][col]
            #print col,row, m[row][col]

seq_to_img(m,pix)

print m[0][1:3]
print pix
#print dir(pix) 

print
print pix.T
