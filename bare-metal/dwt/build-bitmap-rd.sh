#!/bin/bash
gcc -c dwtlift.c -o dwtlift.o
gcc bitmap-rd.c dwtlift.o  -lm -o bitmap-rd
