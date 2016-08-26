#!/bin/bash
rm -f yuv even_odd_de_inter.o test_pointer_inv.o
gcc -c even_odd_de_inter.c -o even_odd_de_inter.o
gcc -c test_pointer_inv.c -o test_pointer_inv.o
gcc yuv.c even_odd_de_inter.o test_pointer_inv.o -o yuv
