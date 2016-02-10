'''
python wr_bin_off.py will create a file
led_off.bin which can be uploaded to ICE40 FPGA

 od -x led_off.bin 
0000000 02de 0000 2000 ca04 0000 0000
0000014

'''
file = open("led_off.bin","wb")
file.write("\xde\x02\x00\x00\x00\x20\x04\xca\x00\x00\x00\x00")
file.close
 
