import waveletsim_53 as dwt
from _jpegEnc import JPEGEnc2k

 
jp2k = JPEGEnc2k()
help(jp2k)
#jp2k.set_img_fn("../parallel_jpeg/lena_rgb_512.png")
#jp2k.set_img_fn("../lena.jpg")
jp2k.set_img_fn("../lena_256.png")

print jp2k.get_img_fn()
jp2k.read_image_file()
mode = jp2k.get_mode()
lvl = jp2k.get_dwt_level()
jp2k.set_dwt_level(1)
#lvl = jp2k.get_dwt_level()

jp2k.fwd_dwt()
im = jp2k.get_img()
im.save("test1_256_fwt.png")
 
