import waveletsim as dwt

im = dwt.Image.open("../lena_256.png")
pix = im.load()
m = list(im.getdata())
m = [m[i:i+im.size[0]] for i in range(0, len(m), im.size[0])]
# Cast every item in the list to a float:
for row in range(0, len(m)):
        for col in range(0, len(m[0])):
                m[row][col] = float(m[row][col])
               
# Perform a forward CDF 9/7 transform on the image:
m = dwt.fwt97_2d(m, 3)
# Convert the list of lists matrix to an image.    
dwt.seq_to_img(m, pix) 
# Save the transformed image.
im.save("test1_256_fwt.png")
mm = dwt.iwt97_2d(m, 3)
dwt.seq_to_img(mm, pix)
im.save("test1_256_iwt.png")
