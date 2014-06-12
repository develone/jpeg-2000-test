
import  wavelet97lift
im = wavelet97lift.Image.open("lena_256.png")
pix = im.load()
m = list(im.getdata())
m = [m[i:i+im.size[0]] for i in range(0, len(m), im.size[0])]
# Cast every item in the list to a float:
for row in range(0, len(m)):
	for col in range(0, len(m[0])):
		m[row][col] = float(m[row][col])
                
# Perform a forward CDF 9/7 transform on the image:
m = wavelet97lift.fwt97_2d(m, 1)
    
wavelet97lift.seq_to_img(m, pix) # Convert the list of lists matrix to an image.
im.save("test1_512_fwt.png") # Save the transformed image.
