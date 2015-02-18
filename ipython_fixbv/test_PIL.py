from PIL import Image
img = Image.open("small5.png")
pix = img.load()
print pix.__sizeof__()
print "img", type(img), "pix", type(pix)
img1 = Image.open("../lena_256.png")
pix1 = img1.load()
print "small5.png", img.size, "lena_256.png", img1.size
w,h = img.size

w1,h1 = img1.size
#print "small5.png",  w,h, "lena_256.png", w1,h1
rgb = list(img.getdata())

print "col 0 row 0", "rgb", rgb[0], "pix", pix[0,0]
print "col 0 row 1", "rgb", rgb[128], "pix", pix[0,1]
print "col 0 row 2", "rgb", rgb[256], "pix", pix[0,2]
print "col 64 row 0", "rgb", rgb[64], "pix", pix[64,0]
print "col 64 row 1", "rgb", rgb[192], "pix", pix[64,1]
print "col 64 row 2", "rgb", rgb[320], "pix", pix[64,2]

m = list(img1.getdata())
#print type(rgb), type(m)
print "small5.png", rgb.__sizeof__(), "lena_256.png", m.__sizeof__()
"""rgb has 3 values per pixel m has 1 value per pixel"""
#print rgb[0],len(rgb),len(rgb[0]), m[0], len(m)

r = []
g = []
b = []
for n in range(len(rgb)):
    rr,gg,bb = rgb[n]
    r.append(rr)
    g.append(gg)
    b.append(bb)
    #print n, r[n],g[n],b[n], rgb[n]
r = [r[i:i+img.size[0]] for i in range(0, len(r), img.size[0])]
g = [g[i:i+img.size[0]] for i in range(0, len(g), img.size[0])]
b = [b[i:i+img.size[0]] for i in range(0, len(b), img.size[0])]
print len(r[0]),len(r[1])
import waveletsim_53 as dwt
r = dwt.fwt97_2d(r, 1)
g = dwt.fwt97_2d(g, 1)
b = dwt.fwt97_2d(b, 1)
print len(r)

print r[0][0]
print g[0][0]
print b[0][0]
print
print r[0][1]
print g[0][1]
print b[0][1]
print
print r[0][2]
print g[0][2]
print b[0][2]
"""this is before fwd dwt"""
print "before fwd dwt", pix[0,0], rgb[0]
rgb = []
for row in range(128):
    for col in range(128):
        rgb.append((r[row][col],g[row][col],b[row][col]))
        
for row in range(127):
        for col in range(127):
            pix[row,col] = rgb[col + row*128]

img.show()
"""this is after fwd dwt"""
print "after fwd  dwt", pix[0,0], rgb[0]
print "after fwd  dwt", pix[0,1], rgb[1]
#print rgb
#dwt.seq_to_img(rgb, pix)
#img.show()
#im.save("test1_256_fwt.png")
#img.show()
"""
print len(rgb[0]), len(rgb[1]),len(m[0]), len(m[1])
rgb = [rgb[i:i+img.size[0]] for i in range(0, len(rgb), img.size[0])]
#print len(rgb[0]), len(rgb[1])
print m.__sizeof__()
m = [m[i:i+img1.size[0]] for i in range(0, len(m), img1.size[0])]
print len(m[0]), len(m[1])

print rgb[0]
print
print rgb[1]
#img.show()
print img.mode
r,g,b = rgb[0]
print r,g,b
for row in range(h):
    
    for col in range(w):
        print row,col, rgb[col]
"""