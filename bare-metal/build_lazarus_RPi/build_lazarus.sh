#!/bin/bash

cd ultibo/core

git clone https://github.com/develone/Lazarus.git

cp -R Lazarus lazarus

cd lazarus

export PATH=/home/pi/ultibo/core/fpc/bin:$PATH

export FPCDIR=/home/pi/ultibo/core/fpc/lib/fpc/3.1.1

echo $PATH

which fpcmake

echo $FPCDIR

cp jpeg-2000-test/bare-metal/build_lazarus_RPi/regexpr/Package.fpc ultibo/core/fpc/lib/fpc/3.1.1/units/arm-linux/regexpr

fpcmake -v

make 
