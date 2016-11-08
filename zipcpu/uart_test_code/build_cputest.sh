#!/bin/bash
#The path needs to be set to the location
#where the zip-gcc is located
#This is what should appear in the 
#Telnet localhost 7240
#window if the tests pass
#Running CPU self-test
##-----------------------------------
#Break test #1                   Pass
#Break test #2                   Pass
#Early Branch test               Pass
#Trap test/AND                   Pass
#Trap test/CLR                   Pass
#Overflow test                   Pass
#Carry test                      Pass
#Loop test                       Pass
#Shift test                      Pass
#Multiply test                   Pass
#Pipeline test                   Pass
#Mem-Pipeline test               Pass
#Conditional Execution test      Pass
#No-waiting pipeline test        Pass
#Conditional Branching test      Pass
#Illegal Instruction test        Pass
#CC Register test                Pass
#Multi-Arg test                  Pass
#
#-----------------------------------
#All tests passed.  Halting CPU.

rm -f cputest
zip-gcc -O3 -Wall -Wextra -nostdlib -fno-builtin -T xula.ld -Wl,-Map,cputest.map cputest.c -o cputest
