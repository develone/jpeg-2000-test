program KeyboardInput;

{$mode objfpc}{$H+}

{ Example 04 Keyboard Input                                                    }
{                                                                              }
{  Example 03 showed some of the screen output capabilities, now we want to    }
{  read from a connected keyboard and print the typed characters on the screen.}
{                                                                              }
{  In this example we also begin to use the USB which is an important element  }
{  to allow Raspberry Pi to communicate with other devices.                    }
{                                                                              }
{  To compile the example select Run, Compile (or Run, Build) from the menu.   }
{                                                                              }
{  Once compiled copy the kernel7.img file to an SD card along with the        }
{  firmware files and use it to boot your Raspberry Pi.                        }
{                                                                              }
{  Raspberry Pi 2B version                                                     }
{   What's the difference? See Project, Project Options, Config and Target.    }

{Declare some units used by this example.}
uses
  RaspberryPi2, 
  GlobalConfig,
  GlobalConst,
  GlobalTypes,
  Platform,
  Threads,
  Console,
  Framebuffer,
  //BCM2836,
  //BCM2709,
  FPWriteXPM, FPWritePNG, FPWriteBMP,
  FPReadXPM, FPReadPNG, FPReadBMP, fpreadjpeg,fpwritejpeg,
  fpreadtga,fpwritetga,fpreadpnm,fpwritepnm,
  classes,
  FPImage,
  SysUtils,
  Keyboard, {Keyboard uses USB so that will be included automatically}
  DWCOTG,   {We need to include the USB host driver for the Raspberry Pi}
   uTFTP,
 Winsock2,
 { needed to use ultibo-tftp  }
 { needed for telnet }
      Shell,
     ShellFilesystem,
     ShellUpdate,
     RemoteShell,
  { needed for telnet }
  uImgConv;
{We'll need a window handle again.}
var
 Tin, Tout, Character:Char;
 WindowHandle:TWindowHandle;
 fn_in, fn_out, buf : string;
 num_rds, outer_lp : integer;
 img : TFPMemoryImage;
 reader : TFPCustomImageReader;
 Writer : TFPCustomimageWriter;
 ReadFile, WriteFile, WriteOptions : string;
 IPAddress : string;
 
procedure WaitForSDDrive;

begin

  while not DirectoryExists ('C:\') do sleep (500);

end;

function WaitForIPComplete : string;

var

  TCP : TWinsock2TCPClient;

begin

  TCP := TWinsock2TCPClient.Create;

  Result := TCP.LocalAddress;

  if (Result = '') or (Result = '0.0.0.0') or (Result = '255.255.255.255') then

    begin

      while (Result = '') or (Result = '0.0.0.0') or (Result = '255.255.255.255') do

        begin

          sleep (1500);

          Result := TCP.LocalAddress;

        end;

    end;

  TCP.Free;

end;

procedure Msg (Sender : TObject; s : string);

begin

  ConsoleWindowWriteLn (WindowHandle, s);

end;

begin
 WaitForSDDrive;
  IPAddress := WaitForIPComplete;
 {Wait a few seconds for all initialization (like filesystem and network) to be done}
 Sleep(5000);

 num_rds := 4;
 {Create a console window at full size}
 WindowHandle:=ConsoleWindowCreate(ConsoleDeviceGetDefault,CONSOLE_POSITION_FULL,True);

 {Output some welcome text on the console window}
 ConsoleWindowWriteLn(WindowHandle,'Welcome to Example 04 Keyboard Input');
 ConsoleWindowWriteLn(WindowHandle,'Make sure you have a USB keyboard connected and start typing some characters');

 {Loop endlessly while checking for Keyboard characters}
 while num_rds <> 0 do
  begin
   {Read a character from the global keyboard buffer. If multiple keyboards are
    connected all characters will end up in a single buffer and be received here

    What happens if no keyboard is connected?

    Ultibo has dynamic USB attach and detach so just plug one in and start typing}
   if ConsoleGetKey(Character,nil) then
    begin
     {Before we print the character to the screen, check what was pressed}
     if Character = #0 then
      begin
       {If a control character like a function key or one of the arrow keys was pressed then
        ConsoleGetKey will return 0 first to let us know, we need to read the next character
        to get the key that was pressed}
       ConsoleGetKey(Character,nil);
      end
     else if Character = #13 then
      begin
       num_rds := num_rds - 1;
       ConsoleWindowWriteLn(WindowHandle, ' num_rds ' + IntToStr(num_rds));
       ConsoleWindowWriteLn(WindowHandle, 'buf ' + buf);
       if num_rds = 2 then
         begin
         fn_in := buf;
       end;        
 
       if num_rds = 0 then
         begin
         fn_out := buf;
         //ConsoleWindowWriteLn(WindowHandle,Tin + ' ' + fn_in + ' ' + Tout + ' ' + fn_out);
       end; 
       if num_rds = 1 then
       begin
          Tout := buf[1];
       end;             
       buf :='';
       {If the enter key was pressed, write a new line to the console instead of a
        character}
       ConsoleWindowWriteLn(WindowHandle,'');
      end
     else
      begin
       {Something other than enter was pressed, print that character on the screen}
       ConsoleWindowWriteChr(WindowHandle,Character);
       buf := buf + Character;
       if num_rds = 4 then
       begin
          Tin := Character;
       end;

      end;
    end;
     
   {No need to sleep on each loop, ConsoleGetKey will wait until a key is pressed}
  end;
  ConsoleWindowWriteLn(WindowHandle,Tin + ' ' + fn_in + ' ' + Tout + ' ' + fn_out);
  Writer := TFPWriterBMP.Create;
  Reader := TFPReaderPNG.Create;
  WriteOptions := 'B';
  ReadFile := fn_in;
  WriteFile := fn_out;
  img := TFPMemoryImage.Create(0,0);
  img.UsePalette:=false;
     try
      writeln ('Initing');
      //Init;
      writeln ('In initInitConv Reading image '+ ReadFile );
      ReadImage(ReadFile,Reader,img); 
      writeln ('In initInitConv Writing image ');
      WriteImage(WriteFile,Writer,WriteOptions,img);
      writeln ('Clean up');
      Clean(Reader,Writer,img);
    except
      on e : exception do
        writeln ('Error: ',e.message);
    end;
 {No need to halt, we never reach this point}
end.

