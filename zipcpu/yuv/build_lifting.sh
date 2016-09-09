#!/bin/bash
rm -f call_lifting lifting.o  yuv.o rd_rgb.o
gcc -c lifting.c -o lifting.o
gcc -c yuv.c -o yuv.o 
gcc -c rd_rgb.c -o rd_rgb.o
gcc call_lifting.c lifting.o yuv.o rd_rgb.o -o call_lifting
