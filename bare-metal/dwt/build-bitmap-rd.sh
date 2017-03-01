#!/bin/bash
 
gcc -g -c mct.c -lm -o mct.o
gcc -g -c opj_malloc.c -lm -o opj_malloc.o
gcc -g bitmap-rd.c opj_malloc.o mct.o -lm -o bitmap-rd
