from myhdl import *
ROM_CONTENT = ( 7, 7<<5, 7<<10, 7<<15,
 7<<20, 7<<25, 7<<30, 7<<35,
 7<<40, 7<<45, 7<<50, 7<<55,
7<<60, 7<<65,7<<70, 7<<75,
5, 5<<5, 5<<10, 5<<15,
 5<<20, 5<<25, 5<<30, 5<<35,
 5<<40, 5<<45, 5<<50, 5<<55,
5<<60, 5<<65,5<<50, 5<<75)
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
addr_flgs = Signal(intbv(0)[RADZ::])


def xx():
    toVerilog.name = 'ram_1'
    toVerilog(ram, dout, din, addr, we, clk_fast)
    toVHDL(ram, dout, din, addr, we, clk_fast)

if __name__ == '__main__':
    main()
