m:
dir ttt.hex
del ttt.hex
"c:\Program Files (x86)\XSTOOLs\xsload.exe" -usb 0 -f hex -u 0x0000 0x3FFFF -ram ttt.hex
dir ttt.hex
copy ttt.hex "c:\Users\vidal\Documents\GitHub\jpeg-2000-test\ipython_fixbv"
 
pause
