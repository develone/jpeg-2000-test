from add_mul_sim import add_mul_sim
from myhdl import fixbv
DATA_WIDTH = 262144
d3 = fixbv(0, min = -DATA_WIDTH, max = DATA_WIDTH, res=1e-5)
a2 = fixbv(0, min = -DATA_WIDTH, max = DATA_WIDTH, res=1e-5)
'''
2D CDF 9/7 Wavelet Forward and Inverse Transform (lifting implementation)

This code is provided "as is" and is given for educational purposes.
2008 - Kris Olhovsky - code.inquiries@olhovsky.com
'''

from PIL import Image # Part of the standard Python Library
        
''' Example matrix as a list of lists: '''
mat4x4 = [                 
         [0,   1,  2,  3], # Row 1
         [4,   5,  6,  7], # Row 2
         [8,   9, 10, 11], # Row 3
         [12, 13, 14, 15], # Row 4
         ]                 # We don't do anything with this matrix.
                           # It's just here for clarification.
                           
def fwt97_2d(m, nlevels=1):
    ''' Perform the CDF 9/7 transform on a 2D matrix signal m.
    nlevel is the desired number of times to recursively transform the 
    signal. '''
    
    w = len(m[0])
    h = len(m)
    for i in range(nlevels):
        m = fwt97(m, w, h) # cols
        m = fwt97(m, w, h) # rows
        w /= 2
        h /= 2
    
    return m


def iwt97_2d(m, nlevels=1):
    ''' Inverse CDF 9/7 transform on a 2D matrix signal m.
        nlevels must be the same as the nlevels used to perform the fwt.
    '''
    
    w = len(m[0])
    h = len(m)

    # Find starting size of m:
    for i in range(nlevels-1):
        h /= 2
        w /= 2
        
    for i in range(nlevels):
        m = iwt97(m, w, h) # rows
        m = iwt97(m, w, h) # cols
        h *= 2
        w *= 2
    
    return m


def fwt97(s, width, height):
    ''' Forward Cohen-Daubechies-Feauveau 9 tap / 7 tap wavelet transform   
    performed on all columns of the 2D n*n matrix signal s via lifting.
    The returned result is s, the modified input matrix.
    The highpass and lowpass results are stored on the left half and right
    half of s respectively, after the matrix is transposed. '''
    
	    
    # 9/7 Coefficients:
    a1 = -1.586134342
    ca1 = -1.586134342
    a2 = -0.05298011854
    ca2 = -0.05298011854
    a3 = 0.8829110762
    ca3 = 0.8829110762
    a4 = 0.4435068522
    ca4 = 0.4435068522

    # Scale coeff:
    k1 = 0.81289306611596146 # 1/1.230174104914
    k2 = 0.61508705245700002 # 1.230174104914/2
    # Another k used by P. Getreuer is 1.1496043988602418
        
    for col in range(width): # Do the 1D transform on all cols:
        ''' Core 1D lifting process in this loop. '''
        ''' Lifting is done on the cols. '''
        # Predict 1. y1
        for row in range(1, height-1, 2):
			odd_even = bool(1)
			p = bool(0)

			x2 = fixbv(s[row-1][col], min = -DATA_WIDTH, max = DATA_WIDTH)
			x3 = fixbv(s[row+1][col], min = -DATA_WIDTH, max = DATA_WIDTH)
			x4 = fixbv(156, min = -DATA_WIDTH, max = DATA_WIDTH)
			x5 = fixbv(156, min = -DATA_WIDTH, max = DATA_WIDTH)
			print row, float(x2), float(x3),odd_even,p
			d_instance = add_mul_sim(d3,a2,x2,x3,x4,x5,p,odd_even)
			#print row, float(d_instance[0]),float(x2), float(x3),odd_even,p
			s[row][col] += float(d_instance[0])
			print s[row][col]
            #s[row][col] += a1 * (s[row-1][col] + s[row+1][col])   
        s[height-1][col] += 2 * ca1 * s[height-2][col] # Symmetric extension

        # Update 1. y0
        for row in range(2, height, 2):
			odd_even = bool(0)
			p= bool(0)
			x2 = fixbv(156, min = -DATA_WIDTH, max = DATA_WIDTH)
			x3 = fixbv(156, min = -DATA_WIDTH, max = DATA_WIDTH)
			x4 = fixbv(s[row-1][col], min = -DATA_WIDTH, max = DATA_WIDTH)
			x5 = fixbv(s[row+1][col], min = -DATA_WIDTH, max = DATA_WIDTH)
			#print row, float(x4), float(x5),odd_even,p
			d_instance = add_mul_sim(d3,a2,x2,x3,x4,x5,p,odd_even)
			#print row, float(d_instance[1]), float(x4), float(x5),odd_even,p
			s[row][col] += float(d_instance[1])
			print s[row][col]
            #s[row][col] += a2 * (s[row-1][col] + s[row+1][col])
        s[0][col] +=  2 * ca2 * s[1][col] # Symmetric extension
        
        # Predict 2.
        for row in range(1, height-1, 2):
            s[row][col] += a3 * (s[row-1][col] + s[row+1][col])
        s[height-1][col] += 2 * ca3 * s[height-2][col]
        
        # Update 2.
        for row in range(2, height, 2):
            s[row][col] += a4 * (s[row-1][col] + s[row+1][col])
        s[0][col] += 2 * ca4 * s[1][col]
               
    # de-interleave
    temp_bank = [[0]*width for i in range(height)]
    for row in range(height):
        for col in range(width):
            # k1 and k2 scale the vals
            # simultaneously transpose the matrix when deinterleaving
            if row % 2 == 0: # even
                temp_bank[col][row/2] = k1 * s[row][col]
            else:            # odd
                temp_bank[col][row/2 + height/2] = k2 * s[row][col]
                
    # write temp_bank to s:
    for row in range(width):
        for col in range(height):
            s[row][col] = temp_bank[row][col]
                
    return s


def iwt97(s, width, height):
    ''' Inverse CDF 9/7. '''
    
    # 9/7 inverse coefficients:
    a1 = 1.586134342
    a2 = 0.05298011854
    a3 = -0.8829110762
    a4 = -0.4435068522
    
    # Inverse scale coeffs:
    k1 = 1.230174104914
    k2 = 1.6257861322319229
    
    # Interleave:
    temp_bank = [[0]*width for i in range(height)]
    for col in range(width/2):
        for row in range(height):
            # k1 and k2 scale the vals
            # simultaneously transpose the matrix when interleaving
            temp_bank[col * 2][row] = k1 * s[row][col]
            temp_bank[col * 2 + 1][row] = k2 * s[row][col + width/2]
                
    # write temp_bank to s:
    for row in range(width):
        for col in range(height):
            s[row][col] = temp_bank[row][col]

                
    for col in range(width): # Do the 1D transform on all cols:
        ''' Perform the inverse 1D transform. '''
        
        # Inverse update 2.
        for row in range(2, height, 2):
            s[row][col] += a4 * (s[row-1][col] + s[row+1][col])
        s[0][col] += 2 * a4 * s[1][col]
        
        # Inverse predict 2.
        for row in range(1, height-1, 2):
            s[row][col] += a3 * (s[row-1][col] + s[row+1][col])
        s[height-1][col] += 2 * a3 * s[height-2][col]

        # Inverse update 1.
        for row in range(2, height, 2):
            s[row][col] += a2 * (s[row-1][col] + s[row+1][col])
        s[0][col] +=  2 * a2 * s[1][col] # Symmetric extension
        
        # Inverse predict 1.
        for row in range(1, height-1, 2):
            s[row][col] += a1 * (s[row-1][col] + s[row+1][col])   
        s[height-1][col] += 2 * a1 * s[height-2][col] # Symmetric extension
                
    return s


def seq_to_img(m, pix):
    ''' Copy matrix m to pixel buffer pix.
    Assumes m has the same number of rows and cols as pix. '''
    for row in range(len(m)):
        for col in range(len(m[row])):
            pix[col,row] = m[row][col]
            
            
if __name__ == "__main__":
    # Load image.
    im = Image.open("../lena_256.png") # Must be a single band image! (grey)

    # Create an image buffer object for fast access.
    pix = im.load()
    
    # Convert the 2d image to a 1d sequence:
    m = list(im.getdata())
        
    # Convert the 1d sequence to a 2d matrix.
    # Each sublist represents a row. Access is done via m[row][col].
    m = [m[i:i+im.size[0]] for i in range(0, len(m), im.size[0])]
    
    # Cast every item in the list to a float:
    for row in range(0, len(m)):
        for col in range(0, len(m[0])):
            m[row][col] = float(m[row][col])
                
    # Perform a forward CDF 9/7 transform on the image:
    m = fwt97_2d(m, 1)
    
    seq_to_img(m, pix) # Convert the list of lists matrix to an image.
    im.save("lena_256_fwt.png") # Save the transformed image.
    
    # Perform an inverse transform:
    m = iwt97_2d(m, 1)
    
    seq_to_img(m, pix) # Convert the inverse list of lists matrix to an image.
    im.save("lena_256_iwt.png") # Save the inverse transformation.
    
