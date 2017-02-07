#!/bin/bash
date
rm -f test.o
rm -f libtest.a
rm -f kernel7.img
arm-none-eabi-gcc -O2 -mabi=aapcs -marm -march=armv7-a -mfpu=vfpv3-d16 -mfloat-abi=hard -c test.c
arm-none-eabi-ar rcs libtest.a test.o

fpc -vi -B -Tultibo -Parm -CpARMV7A -WpRPI2B @/home/pi/ultibo/core/fpc/bin/rpi2.cfg -O2 LibCTest_RPi2.lpr
ls -la test.o libtest.a kernel7.img
