#!/bin/bash
date
rm -f mct.o
rm -f opj_malloc.o
rm -f dwtlift.o
rm -f libdwtlift.a
rm -f kernel7.img
arm-none-eabi-gcc -O2 -mabi=aapcs -marm -march=armv7-a -mfpu=vfpv3-d16 -mfloat-abi=hard -c opj_malloc.c
arm-none-eabi-gcc -O2 -mabi=aapcs -marm -march=armv7-a -mfpu=vfpv3-d16 -mfloat-abi=hard -c mct.c
arm-none-eabi-gcc -O2 -mabi=aapcs -marm -march=armv7-a -mfpu=vfpv3-d16 -mfloat-abi=hard -c dwtlift.c
arm-none-eabi-ar rcs libdwtlift.a dwtlift.o mct.o opj_malloc.o

fpc -vi -B -Tultibo -Parm -CpARMV7A -WpRPI2B @/home/pi/ultibo/core/fpc/bin/rpi2.cfg -O2 DWT_LIFT_RPi2.lpr
ls -la dwtlift.o libdwtlift.a kernel7.img
