#!/bin/bash
rm -f liftmain
gcc -Wall -g liftmain.c lifting.c -lpng -o liftmain
