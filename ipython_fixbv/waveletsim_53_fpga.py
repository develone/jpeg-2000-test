from xstools.xsdutio import *  # Import funcs/classes for PC <=> FPGA link.
from xstools.xsbitarray import *
from myhdl import intbv
print '''
##################################################################
# This program tests the interface between the host PC and the FPGA
# on the XuLA board that has been programmed to act as a jpeg_lifting .
##################################################################
'''

USB_ID = 0  # USB port index for the XuLA board connected to the host PC.
JPEG_ID = 4  # This is the identifier for the jpeg in the FPGA.

# Create a jpeg intfc obj with three 17-bit inputs and one 17-bit output.
even_odd = 1
fwd_inv = 1

jpeg = XsDut(USB_ID, JPEG_ID, [16, 16, 16, 1, 1], [16])

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
def upper_lower(s, width, height):

	temp_bank = [[0]*width for i in range(height)]
	for col in range(width/2):

		for row in range(height/2):

			temp_bank[col+width/2][row+height/2] = s[row][col]

	for row in range(width):
		for col in range(height):
			s[row][col] = temp_bank[col][row]
	return s
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

def fwt97_2d(m, nlevels=1):
    ''' Perform the CDF 9/7 transform on a 2D matrix signal m.
    nlevel is the desired number of times to recursively transform the
    signal. '''

    w = len(m[0])
    h = len(m)
    for i in range(nlevels):
        m = fwt97(m, w, h) # cols
        m = fwt97(m, w, h) # rows
        lower_upper(m, w, h)
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
    ''' Forward Cohen-Daubechies-Feauveau 5 tap / 3 tap wavelet transform
    performed on all columns of the 2D n*n matrix signal s via lifting.
    The returned result is s, the modified input matrix.
    The highpass and lowpass results are stored on the left half and right
    half of s respectively, after the matrix is transposed. '''



    for col in range(width): # Do the 1D transform on all cols:
        ''' Core 1D lifting process in this loop. '''
        ''' Lifting is done on the cols. '''

        even_odd = 1
        fwd_inv = 1
        for row in range(2, height, 2):
			#print (s[row][col])
			ll = (intbv(s[row][col])[16:] - ((intbv(s[row-1][col])>>1)[16:] + (intbv(s[row+1][col])>>1)[16:]))
			lift = jpeg.Exec(XsBitArray(intbv((s[row+1][col]))[16:]), XsBitArray(intbv((s[row-1][col]))[16:]), XsBitArray(intbv((s[row][col]))[16:]), even_odd, fwd_inv)
			s[row][col] = lift.int

			print '%3d %3d %5d %5d %1d %1d %5d %5d' % (col, row, (s[row+1][col]), (s[row-1][col]), even_odd, fwd_inv, (s[row][col]), ll)

            #s[row][col] += a1 * (s[row-1][col] + s[row+1][col])



        even_odd = 0
        fwd_inv = 1
        for row in range(1, height-1, 2):
			ll = (intbv(s[row][col])[16:] + ((intbv(s[row-1][col])[16:] + intbv(s[row+1][col])[16:] + 2)>>2))
			lift = jpeg.Exec(XsBitArray(intbv((s[row+1][col]))[16:]), XsBitArray(intbv((s[row-1][col]))[16:]), XsBitArray(intbv((s[row][col]))[16:]), even_odd, fwd_inv)
			s[row][col] = lift.int
			print '%3d %3d %5d %5d %1d %1d %5d %5d' % (col, row, (s[row+1][col]), (s[row-1][col]), even_odd, fwd_inv, (s[row][col]), ll)


    s = de_interleave(s,height,width)
    return s


def iwt97(s, width, height):
    ''' Inverse CDF 5/3. '''


    # Interleave:
    temp_bank = [[0]*width for i in range(height)]
    for col in range(width/2):
        for row in range(height):

			temp_bank[col * 2][row] = s[row][col]
			temp_bank[col * 2 + 1][row] =  s[row][col + width/2]
    for row in range(width):
        for col in range(height):
            s[row][col] = temp_bank[row][col]


    for col in range(width): # Do the 1D transform on all cols:
        ''' Perform the inverse 1D transform. '''

        # Inverse update 2.
        for row in range(1, height-1, 2):

			s[row][col] = float(s[row][col] - ((int(s[row-1][col]) + int(s[row+1][col]) + 2)>>2))

            #s[row][col] += a4 * (s[row-1][col] + s[row+1][col])
        #s[0][col] += 2 * a4 * s[1][col]

        # Inverse predict 2.
        for row in range(2, height, 2):

			s[row][col] = float(s[row][col] + ((int(s[row-1][col])>>1) + (int(s[row+1][col])>>1)))
            #s[row][col] += a3 * (s[row-1][col] + s[row+1][col])
        #s[height-1][col] += 2 * a3 * s[height-2][col]


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

