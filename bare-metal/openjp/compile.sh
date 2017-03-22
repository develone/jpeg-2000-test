#!/bin/bash
date

rm -f dwtlift.o
rm -f libdwtlift.a
rm -f kernel7.img
rm -f libopenjp2.a

cp ~/t_ultibo/src/lib/openjp2/libopenjp2.a .
arm-none-eabi-ar -t libopenjp2.a | wc
arm-none-eabi-objdump -d libopenjp2.a > dis_orig_libopenjp2.txt
arm-none-eabi-gcc -L. -llibopenjp2 -O2 -mabi=aapcs -marm -march=armv7-a -mfpu=vfpv3-d16 -mfloat-abi=hard -c dwtlift.c 
#The file was created using the script build_gccultibo.sh
#src/lib/openjp2 folder 
#the files opj_malloc.c dwt.c
arm-none-eabi-ar rcs libopenjp2.a dwtlift.o 
cp libopenjp2.a libdwtlift.a
arm-none-eabi-ar -t libopenjp2.a > libopenjp2_obj.txt
arm-none-eabi-objdump -d libopenjp2.a > dis_libopenjp2.txt
fpc -vi -B -Tultibo -Parm -CpARMV7A -WpRPI2B @/home/pi/ultibo/core/fpc/bin/rpi2.cfg -O2 DWT_LIFT_RPi2.lpr
ls -la dwtlift.o libdwtlift.a kernel7.img libopenjp2.a
echo "when ./compile.sh is executed should be 21"
echo "Word count libopenjp2_obj.txt in src/lib/openjp2"
wc libopenjp2_obj.txt
