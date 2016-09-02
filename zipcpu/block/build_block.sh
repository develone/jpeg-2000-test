#!/bin/bash
rm -f block even_odd_de_inter.o 
gcc -c even_odd_de_inter.c -o even_odd_de_inter.o
gcc block.c even_odd_de_inter.o -o block
