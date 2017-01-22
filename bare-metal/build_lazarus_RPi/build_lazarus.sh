#!/bin/bash

cd ultibo/core

git clone https://github.com/develone/Lazarus.git

cp -R Lazarus lazarus

cd lazarus
#adding ultibo edition fpc to PATH
export PATH=/home/pi/ultibo/core/fpc/bin:$PATH

export FPCDIR=/home/pi/ultibo/core/fpc/lib/fpc/3.1.1

echo $PATH

which fpcmake

echo $FPCDIR

#need a Package.fpc for regexpr foe ulribo edition
#	[package]
#	name=regexpr
#	version=3.1.1
#	[require]
#	packages_linux_arm=
cp /home/pi/jpeg-2000-test/bare-metal/build_lazarus_RPi/regexpr/Package.fpc /home/pi/ultibo/core/fpc/lib/fpc/3.1.1/units/arm-linux/regexpr

fpcmake -v

#make 

make clean all OPT="@/home/pi/ultibo/core/fpc/bin/fpc.cfg" 

#make  all OPT="@/home/pi/ultibo/core/fpc/bin/fpc.cfg"
