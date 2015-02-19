from PIL import Image
"""small5.png is RGB 128 x 128
small256.png is RGB 256 x 256
small512.png is RGB 512 X 512
"""
img = Image.open("small5.png")
#img = Image.open("small256.png")
#img = Image.open("small512.png")
pix = img.load()
print pix.__sizeof__()
print "img", type(img), "pix", type(pix)
 
print "small5.png", img.size
w,h = img.size


print "small256.png",  w,h
rgb = list(img.getdata())

print "col 0 row 0", "rgb", rgb[0], "pix", pix[0,0]
print "col 0 row 1", "rgb", rgb[128], "pix", pix[0,1]
print "col 0 row 2", "rgb", rgb[256], "pix", pix[0,2]
print "col 64 row 0", "rgb", rgb[64], "pix", pix[64,0]
print "col 64 row 1", "rgb", rgb[192], "pix", pix[64,1]
print "col 64 row 2", "rgb", rgb[320], "pix", pix[64,2]

#print type(rgb), type(m)
print "small5.png", rgb.__sizeof__()
"""rgb has 3 values per pixel """
print rgb[0],len(rgb),len(rgb[0])

r = []
g = []
b = []
"""get r g b from rgb"""
for n in range(len(rgb)):
    rr,gg,bb = rgb[n]
    r.append(rr)
    g.append(gg)
    b.append(bb)
    #print n, r[n],g[n],b[n], rgb[n]
"""convert to row col"""
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
for row in range(len(r)):
    for col in range(len(r)):
        rgb.append((r[row][col],g[row][col],b[row][col]))
        
for row in range(len(r)):
        for col in range(len(r)):
            #pix[row,col] = rgb[col + row*128]
            pix[col,row] = rgb[col + row*len(r)]


img.show()
img.save("test1_256_fwt.png")
"""this is after fwd dwt"""
print "after fwd  dwt", pix[0,0], rgb[0]
print "after fwd  dwt", pix[0,1], rgb[1]
 