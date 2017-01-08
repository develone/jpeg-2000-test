cd /home/pi/ultibo/core/fpc/source

export PATH=/home/pi/ultibo/core/fpc/bin:$PATH

make rtl_clean CROSSINSTALL=1 OS_TARGET=ultibo CPU_TARGET=arm SUBARCH=armv6 BINUTILSPREFIX=arm-none-eabi- FPCFPMAKE=/home/pi/ultibo/core/fpc/bin/fpc CROSSOPT="-CpARMV6 -CfVFPV2 -CIARM -CaEABIHF -OoFASTMATH" FPC=/home/pi/ultibo/core/fpc/bin/fpc

make rtl OS_TARGET=ultibo CPU_TARGET=arm SUBARCH=armv6 BINUTILSPREFIX=arm-none-eabi- FPCFPMAKE=/home/pi/ultibo/core/fpc/bin/fpc CROSSOPT="-CpARMV6 -CfVFPV2 -CIARM -CaEABIHF -OoFASTMATH" FPC=/home/pi/ultibo/core/fpc/bin/fpc

make rtl_install CROSSINSTALL=1 BINUTILSPREFIX=arm-none-eabi- FPCFPMAKE=/home/pi/ultibo/core/fpc/bin/fpc CROSSOPT="-CpARMV6 -CfVFPV2 -CIARM -CaEABIHF -OoFASTMATH" OS_TARGET=ultibo CPU_TARGET=arm SUBARCH=armv6 FPC=/home/pi/ultibo/core/fpc/bin/fpc INSTALL_PREFIX=/home/pi/ultibo/core/fpc INSTALL_UNITDIR=/home/pi/ultibo/core/fpc/units/armv6-ultibo/rtl

make rtl_clean CROSSINSTALL=1 OS_TARGET=ultibo CPU_TARGET=arm SUBARCH=armv6 BINUTILSPREFIX=arm-none-eabi- FPCFPMAKE=/home/pi/ultibo/core/fpc/bin/fpc CROSSOPT="-CpARMV6 -CfVFPV2 -CIARM -CaEABIHF -OoFASTMATH" FPC=/home/pi/ultibo/core/fpc/bin/fpc

make packages_clean CROSSINSTALL=1 OS_TARGET=ultibo CPU_TARGET=arm SUBARCH=armv6 BINUTILSPREFIX=arm-none-eabi- FPCFPMAKE=/home/pi/ultibo/core/fpc/bin/fpc CROSSOPT="-CpARMV6 -CfVFPV2 -CIARM -CaEABIHF -OoFASTMATH" FPC=/home/pi/ultibo/core/fpc/bin/fpc

make packages OS_TARGET=ultibo CPU_TARGET=arm SUBARCH=armv6 BINUTILSPREFIX=arm-none-eabi- FPCFPMAKE=/home/pi/ultibo/core/fpc/bin/fpc CROSSOPT="-CpARMV6 -CfVFPV2 -CIARM -CaEABIHF -OoFASTMATH -Fu/home/pi/ultibo/core/fpc/units/armv6-ultibo/rtl" FPC=/home/pi/ultibo/core/fpc/bin/fpc

make packages_install CROSSINSTALL=1 BINUTILSPREFIX=arm-none-eabi- FPCFPMAKE=/home/pi/ultibo/core/fpc/bin/fpc CROSSOPT="-CpARMV6 -CfVFPV2 -CIARM -CaEABIHF -OoFASTMATH" OS_TARGET=ultibo CPU_TARGET=arm SUBARCH=armv6 FPC=/home/pi/ultibo/core/fpc/bin/fpc INSTALL_PREFIX=/home/pi/ultibo/core/fpc INSTALL_UNITDIR=/home/pi/ultibo/core/fpc/units/armv6-ultibo/packages
