#!/bin/bash
 
gcc -g -c mct.c -lm -o mct.o
gcc -g -c dwt.c -lm -o dwt.o
gcc -g -c thread.c -lm -o thread.o
gcc -g -c opj_malloc.c -lm -o opj_malloc.o
gcc -g bitmap-rd.c opj_malloc.o mct.o dwt.o thread.o -lm -o bitmap-rd
