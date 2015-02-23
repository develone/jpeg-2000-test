from myhdl import *
ROM_CONTENT = ( 7, 5, 6, 4,
 224, 160, 192, 128,
 7168, 5120, 6144,4096,
229376, 163840,196608, 131072,
7, 0, 7, 0, 7, 0,
6, 0, 6, 0, 6, 0)
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


dout_flgs = Signal(intbv(0)[20:])
addr_flgs = Signal(intbv(0)[RADZ::])


def xx():
    toVerilog.name = 'ram_1'
    toVerilog(ram, dout, din, addr, we, clk_fast)
    toVHDL(ram, dout, din, addr, we, clk_fast)

if __name__ == '__main__':
    main()
