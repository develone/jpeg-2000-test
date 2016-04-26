#!/bin/bash
date
./jpeg img_to_fpga.bin pass.bin 2 1 0 0
python rd_pass.py
date
