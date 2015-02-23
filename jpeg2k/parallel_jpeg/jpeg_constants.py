
reset_dly_c = 10
ASZ = 4
""" The following 3 constants are used during testing of 32 bit sdram
DSZ = 32
SDRAMDSZ = 32
JPEG_RAM_ADDR = 24
"""

""" The following 3 constants are used during simulation testing of 32 bit sdram
manual chgs required
In entity of XESS_SdramSPInst/XESS_SDRAMSPINST_32/XESS_SdramDPInst.vhd and
in COMPONENT XESS_SdramSPInst/XESS_SDRAMSPINST_32/XESS_SdramDPInstTB.vhd
sdData_io : inout std_logic_vector(31 downto 0);    -- SDRAM data bus.
XESS_SdramSPInst/XESS_SDRAMSPINST_32/XESS_SdramDPInstTB.vhd
signal sdData_io : std_logic_vector(31 downto 0);
component mt48lc8m16a2
Dq : inout std_logic_vector(31 downto 0);
XESS_SdramSPInst/XESS_SDRAMSPINST_32/mt48lc8m16a2.v
parameter data_bits =      32;"""
DSZ = 32
SDRAMDSZ = 32
JPEG_RAM_ADDR = 23


DATA_WIDTH = 32768

JPEG_RES_RAM_ADDR = 9

ROW_NUM = 8
ACTIVE_LOW = bool(0)
NO = bool(0)
YES = bool(1)

SUB2 = 256
SUB3 = 512
ROM_ADDR = 4
""" Required  by array_jpeg.py
these are used to set the size of the
arrays"""
W0 = 10
LVL0 = 16
W1 = 10
LVL1 = 16
W2 = 10
LVL2 = 16
W3 = 5
LVL3 = 16
SIMUL = 0