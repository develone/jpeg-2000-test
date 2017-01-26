program LibCPass;

{$mode objfpc}{$H+}

uses
 RaspberryPi2,  
 GlobalConfig,
 GlobalConst,
 GlobalTypes,
 Platform,
 Threads,
 Console,
 Syscalls;

{$linklib lifting}

procedure lifting(w: Integer; ibuf: PInteger; tmpbuf: PInteger); cedcl; external 'liblifting' name 'lifting';
 
var
 A, B, C: Integer;
 
begin
end;

 
  
var
 Handle:THandle;

begin


  A:=1;
  B:=2;
  C:=3;
 Handle:=ConsoleWindowCreate(ConsoleDeviceGetDefault,CONSOLE_POSITION_FULL,True);

lifting(A, @B, @C);
 
 ThreadHalt(0);
end.
