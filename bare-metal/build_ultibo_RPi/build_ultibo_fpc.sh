#!/bin/bash

#These instructions assume that FPC 3.0.0 from GetLazarus was installed to:

#/home/pi/Development/FreePascal/fpc/bin

mkdir -p ultibo/core

cd ultibo/core

git clone https://github.com/ultibohub/FPC.git

mv FPC fpc

git clone https://github.com/ultibohub/Core.git

cp -R  Core/source/rtl/ultibo fpc/source/rtl

ls fpc/source/rtl/ultibo

cp -R Core/source/packages/ultibounits fpc/source/packages

ls fpc/source/packages

cp -R Core/units fpc

ls fpc

cd /home/pi/ultibo/core/fpc/source

export PATH=/home/pi/Development/FreePascal/fpc/bin:$PATH

make distclean

make all OPT=-dFPC_ARMHF

make install OPT=-dFPC_ARMHF PREFIX=/home/pi/ultibo/core/fpc

cp /home/pi/ultibo/core/fpc/source/compiler/ppcarm /home/pi/ultibo/core/fpc/bin/ppcarm

/home/pi/ultibo/core/fpc/bin/fpc -i | grep ultibo

/home/pi/ultibo/core/fpc/bin/fpc -i | grep 'Free Pascal Compiler version 3.1.1'


/home/pi/ultibo/core/fpc/bin/fpcmkcfg -d basepath=$HOME/ultibo/core/fpc/lib/fpc/3.1.1 -o /home/pi/ultibo/core/fpc/bin/fpc.cfg
