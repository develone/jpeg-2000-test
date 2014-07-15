import waveletsim_53 as dwt

im = dwt.Image.open("../lena_256.png")
pix = im.load()
m = list(im.getdata())
m = [m[i:i+im.size[0]] for i in range(0, len(m), im.size[0])]
# Perform a forward CDF 9/7 transform on the image:
m = dwt.fwt97_2d(m, 1)
# Convert the list of lists matrix to an image.    
dwt.seq_to_img(m, pix)
#print m[0][128:] 
# Save the transformed image.
im.save("test1_256_fwt.png")
mm = dwt.iwt97_2d(m, 1)
dwt.seq_to_img(mm, pix)
im.save("test1_256_iwt.png")

