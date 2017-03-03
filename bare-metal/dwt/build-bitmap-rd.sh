#!/bin/bash
 
#gcc -g -c mct.c -lm -o mct.o
#gcc -g -c dwt.c -lm -o dwt.o
#gcc -g -c thread.c -lm -o thread.o
#gcc -g -c opj_malloc.c -lm -o opj_malloc.o
gcc  -g bitmap-rd.c -L. -lopenjp2 -lm -o bitmap-rd
