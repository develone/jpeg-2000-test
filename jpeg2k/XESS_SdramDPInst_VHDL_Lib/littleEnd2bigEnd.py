from cStringIO import StringIO
from  intelhex import IntelHex
from struct import *
CONTENT = (
982599844,980498596,982595740,980498596,980498588,980498588,980498588,980498588,980498588,982599836,982599844,982599844,980502692,982599836,982595748,982603940)
def convert_list_to_bin():
    #fmt = '>H'
    f = open('tmp_level.bin','wb')
    
    for i in range(0, len(CONTENT)):
        x = pack('<L',CONTENT[i])
        #x = pack('>L',CONTENT[i])
        f.write(x)
    f.close()
#print CONTENT
#print len(CONTENT)
convert_list_to_bin()
for i in range(0, len(CONTENT)):
    print ("%s" " big endian using >L  "  "%s" "   " "%d" ) % (hex(CONTENT[i]), bin(CONTENT[i]), CONTENT[i])