#!/bin/bash
date
rm -f lifting.o
rm -f liblifting.a
rm -f kernel7.img
arm-none-eabi-gcc -O2 -mabi=aapcs -marm -march=armv7-a -mfpu=vfpv3-d16 -mfloat-abi=hard -c lifting.c
arm-none-eabi-ar rcs liblifting.a lifting.o

fpc -vi -B -Tultibo -Parm -CpARMV7A -WpRPI2B @/home/pi/ultibo/core/fpc/bin/rpi2.cfg -O2 LibCPassRPi2.lpr
ls -la lifting.o liblifting.a kernel7.img
