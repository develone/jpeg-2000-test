from myhdl import *
ROM_CONTENT = ( 7, 7<<5, 7<<10, 7<<15,
 7<<20, 7<<25, 7<<30, 7<<35,
 7<<40, 7<<45, 7<<50, 7<<55,
7<<60, 7<<65,7<<70, 7<<75,
6, 6<<5, 6<<10, 6<<15,
 6<<20, 6<<25, 6<<30, 6<<35,
 6<<40, 6<<45, 6<<50, 6<<55,
6<<60, 6<<65,6<<70, 6<<75,
5, 5<<5, 5<<10, 5<<15,
 5<<20, 5<<25, 5<<30, 5<<35,
 5<<40, 5<<45, 5<<50, 5<<55,
5<<60, 5<<65,5<<70, 5<<75,
4, 4<<5, 4<<10, 4<<15,
 4<<20, 4<<25, 4<<30, 4<<35,
 4<<40, 4<<45, 4<<50, 4<<55,
4<<60, 4<<65,4<<70, 4<<75)
RADZ = 10

def rom_flgs(dout_flgs, addr_flgs, ROM_CONTENT):
    """ ROM model """

    @always_comb
    def read():
        dout_flgs.next = ROM_CONTENT[int(addr_flgs)]

    return read

def romconvert():
    toVerilog(rom_flgs, dout_flgs, addr_flgs, ROM_CONTENT)
    toVHDL(rom_flgs, dout_flgs, addr_flgs, ROM_CONTENT)


dout_flgs = Signal(intbv(0)[80:])
addr_flgs = Signal(intbv(0)[RADZ:])



romconvert()
#if __name__ == '__main__':
#main()
