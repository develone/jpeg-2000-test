"""Script that converts MyHDL RTL to Verilog/VDHL

Usage: python convert.py

The verilog/vhdl subdirectories are assumed to exist.
"""

import glob
import shutil
import os

from myhdl import *

from jpeg_myhdl import Jpeg

def convert(target=toVHDL):

    #ToSPieceOut = Signal(intbv(0)[6:])
    #ToSMaskOut = Signal(intbv(0)[16:]) 
    #PieceIn = Signal(intbv(0)[6:])
    #MaskIn = Signal(intbv(0)[16:])
    MaskReset = Signal(intbv(0)[16:])
    #Enable = Signal(bool(0))
    PushPop = Signal(bool(0))
    Reset = ResetSignal(bool(0), active=1, async=False)
    #Clk = Signal(bool(0))
    clk_fast = Signal(bool(0))    
    target(
        Jpeg,
        #ToSPieceOut, 
        #ToSMaskOut, 
        #PieceIn, 
        #MaskIn, 
        MaskReset, 
        #Enable, 
        PushPop, 
        Reset,
        #Clk,
        clk_fast,
    )

cwd = os.getcwd()

os.chdir(cwd)
os.chdir('vhdl')
convert(toVHDL)

os.chdir(cwd)
os.chdir('verilog')
convert(toVerilog)



