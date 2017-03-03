#!/bin/bash
date

rm -f dwtlift.o
rm -f libdwtlift.a
rm -f kernel7.img


arm-none-eabi-gcc -O2 -mabi=aapcs -marm -march=armv7-a -mfpu=vfpv3-d16 -mfloat-abi=hard -c dwtlift.c 
#The file was created using the script build_gccultibo.sh
#src/lib/openjp2 folder 
#the files opj_malloc.c dwt.c
arm-none-eabi-ar rcs libopenjp2.a dwtlift.o
cp libopenjp2.a libdwtlift.a
fpc -vi -B -Tultibo -Parm -CpARMV7A -WpRPI2B @/home/pi/ultibo/core/fpc/bin/rpi2.cfg -O2 DWT_LIFT_RPi2.lpr
ls -la dwtlift.o libdwtlift.a kernel7.img
echo "when ./compile.sh is executed should be 21"
echo "Word cpunt libopenjp2_obj.txt in src/lib/openjp2"
wc libopenjp2_obj.txt
