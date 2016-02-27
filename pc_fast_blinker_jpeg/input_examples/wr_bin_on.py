'''
python wr_bin_on.py will create a file
led_on.bin which can be uploaded to ICE40 FPGA

od -x led_on.bin 
0000000 02de 0000 2000 ca04 0000 ff00
0000014
'''

file = open("led_on.bin","wb")
file.write("\xde\x02\x00\x00\x00\x80\x04\xca\x00\x00\x00\xff")
file.close
 


