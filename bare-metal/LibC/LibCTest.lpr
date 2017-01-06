program LibCTest;

{$mode objfpc}{$H+}

uses
 RaspberryPi3,  
 GlobalConfig,
 GlobalConst,
 GlobalTypes,
 Platform,
 Threads,
 Console,
 Syscalls;

{$linklib test}

procedure test; cdecl; external 'libtest' name 'test';

var
 Handle:THandle;

begin
 Handle:=ConsoleWindowCreate(ConsoleDeviceGetDefault,CONSOLE_POSITION_FULL,True);

 test;
 
 ThreadHalt(0);
end.
