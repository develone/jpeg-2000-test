#!/bin/bash
#Prerequisites for Free Pascal and Lazarus on Raspbian
#-----------------------------------------------------
#Lazarus requires the following Gtk+ dev packages which
#can be installed on Raspbian by using:

#sudo apt-get install libgtk2.0-dev libcairo2-dev \
#  libpango1.0-dev libgdk-pixbuf2.0-dev libatk1.0-dev \
#  libghc-x11-dev

mkdir Development

cd Development/

git clone https://github.com/sysrpl/Codebot.Setup.git

cd Codebot.Setup/raspberry/

chmod +x install.fpc-3.0.raspberry.sh

./install.fpc-3.0.raspberry.sh

#Press return to check your system

#libgtk2.0-dev found
#libcairo2-dev found
#libpango1.0-dev found
#libgdk-pixbuf2.0-dev found
#libatk1.0-dev found
#libghc-x11-dev found
#Raspberry Free Pascal 3.0 with Lazarus install script
#-----------------------------------------------------
#This script will install a lightweight version of

#The Free Pascal Compiler version 3.0
#The Lazarus Development Environment

#After install 242MB of drive space will be used

#This lightweight version is designed specifically
#for the Raspberry Pi running Raspbian OS

#Enter an installation folder or press return to
#accept the default install location

#[/home/pi/Development/FreePascal]:
#The install folder will be:
#/home/pi/Development/FreePascal

#Continue? (y,n):
#After install do you want to shortcuts created in:
#/home/pi/.local/share/applications (y/n)?

#Your Free Pascal 3.0 with Lazarus is now installed
