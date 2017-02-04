program FIQTest;

{$mode delphi}{$H+}

uses
  RaspberryPi2, {Include the RaspberryPi2 unit to give us network, filesystem etc}
  GlobalConfig,
  GlobalConst,
  GlobalTypes,
  Threads,
  Console,
  Devices,      {Include the Devices unit for the Timer device API}
  BCM2709,      {Include the BCM2709 unit so we can look at the interrupt statistics}
  HTTP,         {Include HTTP and WebStatus so we can see from a web browser what is happening}
  WebStatus,
  RemoteShell,     {Include RemoteShell and the ShellUpdate unit for remote updating}
  ShellFilesystem,
  ShellUpdate,
  SysUtils;
 
var
 Window:TWindowHandle;
 CallbackCounter:LongWord;
 HTTPListener:THTTPListener;

procedure TimerCallback(Data:Pointer);
begin
 {}
 Inc(CallbackCounter);
end;

begin
 {Wait a few seconds for all initialization to be done}
 Sleep(3000);

 {Create a console window to show what is happening}
 Window:=ConsoleWindowCreate(ConsoleDeviceGetDefault,CONSOLE_POSITION_FULL,True);
 
 {Display a startup message on the console}
 ConsoleWindowWriteLn(Window,'Starting Fast Interrupt (FIQ) test');
 
 {Create and start the HTTP Listener for our web status page}
 HTTPListener:=THTTPListener.Create;
 HTTPListener.Active:=True;
 
 {Register the web status page to allow checking the rest of the system for responsiveness}
 WebStatusRegister(HTTPListener,'','',True);
 
 {Set the clock rate and interval for the timer (1MHz / 1000 microseconds)}
 TimerDeviceSetRate(TimerDeviceGetDefault,1000000);
 TimerDeviceSetInterval(TimerDeviceGetDefault,1000);
 
 {Set the timer to use FIQ (This variable is form GlobalConfig)}
 {Set to False to use IRQ instead}
 BCM2709ARM_TIMER_FIQ_ENABLED:=True;
 //BCM2709ARM_TIMER_FIQ_ENABLED:=False;
 
 {Start the timer}
 ConsoleWindowWriteLn(Window,'Calling TimerDeviceStart()');
 TimerDeviceStart(TimerDeviceGetDefault);
 
 {Register the callback event (Repeating / Interrupt)}
 {The TIMER_EVENT_FLAG_REPEAT tells it to keep repeating the event}
 {And TIMER_EVENT_FLAG_INTERRUPT tells it to call the function from within the interrupt handler (Use carefully!)}
 ConsoleWindowWriteLn(Window,'Calling TimerDeviceEvent()');
 TimerDeviceEvent(TimerDeviceGetDefault,TIMER_EVENT_FLAG_REPEAT or TIMER_EVENT_FLAG_INTERRUPT,TimerCallback,nil);
 
 {Increase the clock rate and interval for the timer (25MHz / 40 microseconds)}
 TimerDeviceSetRate(TimerDeviceGetDefault,25000000);
 
 {Increase the clock rate and interval for the timer (50MHz / 20 microseconds)}
 //TimerDeviceSetRate(TimerDeviceGetDefault,50000000);
 
 {Increase the clock rate and interval for the timer (200MHz / 5 microseconds)}
 //TimerDeviceSetRate(TimerDeviceGetDefault,200000000);
 
 {Output the details}
 ConsoleWindowWriteLn(Window,'TimerDeviceGetRate = ' + IntToStr(TimerDeviceGetRate(TimerDeviceGetDefault)));
 ConsoleWindowWriteLn(Window,'TimerDeviceGetInterval = ' + IntToStr(TimerDeviceGetInterval(TimerDeviceGetDefault)));
 
 while True do
  begin
   {Reset position}
   ConsoleWindowSetXY(Window,1,10);
   
   {Output callback count}
   ConsoleWindowWriteLn(Window,'CallbackCounter = ' + IntToStr(CallbackCounter));
   
   {Output interrupt count}
   ConsoleWindowWriteLn(Window,'PBCM2709ARMTimer(TimerDeviceGetDefault).InterruptCount = ' + IntToStr(PBCM2709ARMTimer(TimerDeviceGetDefault).InterruptCount));
   
   Sleep(1000);
  end;
 
 {Halt this thread}
 ThreadHalt(0);
end.
