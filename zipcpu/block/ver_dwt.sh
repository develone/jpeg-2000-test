#!/bin/bash
rm -f dwt.v ram.v
rm -rf obj_dir/
python jpeg.py --convert
python ram.py --convert

verilator --cc --trace dwt.v
verilator --cc --trace ram.v

cd obj_dir

make -f Vdwt.mk
make -f Vram.mk

