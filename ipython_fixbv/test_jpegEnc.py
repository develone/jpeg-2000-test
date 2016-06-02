 
from _jpegEnc import JPEGEnc2k
import math
 
jp2k = JPEGEnc2k()
#help(jp2k)
jp2k.set_img_fn("../jpeg2k/parallel_jpeg/lena_rgb_512.png")
#jp2k.set_img_fn("../lena.jpg")
#jp2k.set_img_fn("../lena_256.png")
#jp2k.set_img_fn("../lena_128.png")
#jp2k.set_img_fn("../lena_64.png")
#jp2k.set_img_fn("../grabber002.png")
f = [5, 3]
jp2k.set_filter(f)

print jp2k.get_img_fn()
jp2k.read_image_file()
mode = jp2k.get_mode()
lvl = jp2k.get_dwt_level()
jp2k.set_dwt_level(3)
#lvl = jp2k.get_dwt_level()
if (jp2k.get_filter() == [9,7]):
    jp2k.fwd_f_dwt()
else:
    jp2k.fwd_dwt()
im = jp2k.get_img()
#im = im.crop((0,0,32,32))
print im.size
n = list(im.getdata())

print len(n)
x = []
p = []
non_zero = 0
'''
for i in range(len(n)):
    if (n[i] != 0):
        non_zero = non_zero + 1
        x.append(n[i])
        #print n[i], math.log(n[i],2), -n[i]*math.log(n[i],2)
        p.append(-n[i]*math.log(n[i],2))
print x
print min(x), max(x)
print non_zero
#print p
#print sum(p)
from collections import Counter
print Counter(x)
print 
print Counter(x).most_common(32)
print 
print Counter(x).most_common(8)

print 
print Counter(x).values()

print 
'''
im.save("test1_256_fwt.png")
 
