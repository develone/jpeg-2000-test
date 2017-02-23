#!/bin/bash
gcc -g -c dwtlift.c -o dwtlift.o
gcc -g bitmap-rd.c dwtlift.o  -lm -o bitmap-rd
