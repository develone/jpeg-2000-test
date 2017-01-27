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

procedure lifting(w: Integer; ibuf: PInteger; tmpbuf: PInteger); cdecl; external 'liblifting' name 'lifting';
 
var
	A, B, C: Integer;
  
var
	Handle:THandle;

begin

	A:=160;
	B:=156;
	C:=164;
	Handle:=ConsoleWindowCreate(ConsoleDeviceGetDefault,CONSOLE_POSITION_FULL,True);
	lifting(A, @B, @C);
 
	ThreadHalt(0);
end.
