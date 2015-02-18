from PIL import Image
img = Image.open("small5.png")
print img.size
w,h = img.size
print w,h
pixel = img.load()
m = list(img.getdata())
print m.__sizeof__()
print len(m[0]), len(m[1])

print m[0]
print
print m[1]
#img.show()
print img.mode
r,g,b = m[0]
print r,g,b
for row in range(h):
    
    for col in range(w):
        print row,col, m[col]