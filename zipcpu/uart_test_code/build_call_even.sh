#!/bin/bash
rm -f call_even_odd_de_inter
gcc -c even_odd_de_inter.c -o even_odd_de_inter.o
gcc call_even_odd_de_inter.c even_odd_de_inter.o -o call_even_odd_de_inter
