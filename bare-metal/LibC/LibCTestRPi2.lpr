program LibCTest;

{$mode objfpc}{$H+}

uses
 RaspberryPi2, {<-- Change this to suit which model you have!!}
 GlobalConfig,
 GlobalConst,
 GlobalTypes,
 Platform,
 Threads,
 Console,
 SysUtils,  { TimeToStr & Time }
 { needed by bitmap }
 GraphicsConsole, {Include the GraphicsConsole unit so we can create a graphics window}
 BMPcomn,         {Include the BMPcomn unit from the fpc-image package to give the Bitmap headers}
 Classes,
 { needed by bitmap }
 { needed to use ultibo-tftp  }
 uTFTP,
 Winsock2,
 { needed to use ultibo-tftp  }
 { needed for telnet }
      Shell,           
     ShellFilesystem, 
     ShellUpdate,
     RemoteShell,
  { needed for telnet }
 uPointersToC,
 uBufferToC,   
 Syscalls;

{$linklib test}
 
procedure test; cdecl; external 'libtest' name 'test';

var
	A, B, C: Integer;
	
var
 Handle:THandle;
 Handle1:THandle;
 {Handle2:THandle;}
 Window:TWindowHandle;
 Handle3:THandle;

 IPAddress : string;
 
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

  ConsoleWindowWriteLn (Handle1, s);

end;



procedure WaitForSDDrive;

begin

  while not DirectoryExists ('C:\') do sleep (500);

end;
function DrawBitmap(Handle:TWindowHandle;const Filename:String;X,Y:LongWord):Boolean;
 
var
 Size:LongWord;
 Count:LongWord;
 Offset:LongWord;
 Format:LongWord;
 Buffer:Pointer;
 TopDown:Boolean;
 LineSize:LongWord;
 ReadSize:LongWord;
 FileStream:TFileStream;
 
 BitMapFileHeader:TBitMapFileHeader;
 BitMapInfoHeader:TBitMapInfoHeader;
begin
 {}
 Result:=False;
      A:=160;
      B:=156;
      C:=164;
      
 {There are a few different ways to load a bitmap file and draw it on the screen in Ultibo, in this example
  we'll use a TFileStream class to read the file and then load the image data (the pixels) into a memory
  buffer that we allocate. Finally we'll put the pixels onto the screen using the GraphicsWindowDrawImage()
  function from the GraphicsConsole unit}
 
 {Check the parameters}
 if Handle = INVALID_HANDLE_VALUE then Exit;
 if Length(Filename) = 0 then Exit;
 
 {Check if the file exists} 
 if not FileExists(Filename) then Exit;
 
 {Open the file using a TFileStream class}
 FileStream:=TFileStream.Create(Filename,fmOpenRead or fmShareDenyNone);
 try
  
  {Check the file size}
  if FileStream.Size < (SizeOf(TBitMapFileHeader) + SizeOf(TBitMapInfoHeader)) then Exit;
  
  {Read the Bitmap file header}
  if FileStream.Read(BitMapFileHeader,SizeOf(TBitMapFileHeader)) <> SizeOf(TBitMapFileHeader) then Exit;
  
  {Check the magic number in the header}
  if BitMapFileHeader.bfType = BMmagic then
   begin
    {Read the Bitmap info header}
    if FileStream.Read(BitMapInfoHeader,SizeOf(TBitMapInfoHeader)) <> SizeOf(TBitMapInfoHeader) then Exit;
    
    {Most Bitmaps are stored upside down in the file, but they can be right way up}
    TopDown:=(BitMapInfoHeader.Height < 0);
    
    BitMapInfoHeader.Height:=Abs(BitMapInfoHeader.Height);
    
    {Check how many bits per pixel in this Bitmap, we only support 16, 24 and 32 in this function}
    
    if BitMapInfoHeader.BitCount = 16 then
     begin
      {Check the compression format used, this function only supports raw RGB files so far}
      if BitMapInfoHeader.Compression = BI_RGB then
       begin
        {Get the color format}
        Format:=COLOR_FORMAT_RGB15;
        {Now get the bytes per line}
        LineSize:=BitMapInfoHeader.Width * 2;
        {And also determine the actual number of bytes until the next line}
        ReadSize:=(((BitMapInfoHeader.Width * 8 * 2) + 31) div 32) shl 2;
       end
      else
       begin
        Exit;
       end;
     end
    else if BitMapInfoHeader.BitCount = 24 then
     begin
      {Check the compression}
      if BitMapInfoHeader.Compression = BI_RGB then
       begin
        {Color format, bytes per line and actual bytes as again}
        Format:=COLOR_FORMAT_RGB24;
        LineSize:=BitMapInfoHeader.Width * 3;
        ReadSize:=(((BitMapInfoHeader.Width * 8 * 3) + 31) div 32) shl 2;
        ConsoleWindowWriteLn (Handle3,'ReadSize ' + IntToStr(ReadSize));
       end
      else
       begin
        Exit;
       end;
     end
    else if BitMapInfoHeader.BitCount = 32 then
     begin
      {Check the compression}
      if BitMapInfoHeader.Compression = BI_RGB then
       begin
        {Color format, bytes per line and actual bytes as again}
        Format:=COLOR_FORMAT_URGB32;
        LineSize:=BitMapInfoHeader.Width * 4;
        ReadSize:=(((BitMapInfoHeader.Width * 8 * 4) + 31) div 32) shl 2;
       end
      else
       begin
        Exit;
       end;
     end
    else
     begin
      Exit;
     end;     
  
    {Get the size of the Bitmap image not including the headers, just the actual pixels}
    Size:=LineSize * BitMapInfoHeader.Height;
     
    {Allocate a buffer to hold all the pixels}
    
    Buffer:=GetMem(Size);
    ConsoleWindowWriteLn (Handle3, 'Buffer ' + hexStr(Buffer)+ ' Size ' + IntToStr(Size) +' LineSize ' + IntToStr(LineSize) + ' BitCount ' + IntToStr(BitMapInfoHeader.BitCount));
    
    
    
    try
     Offset:=0;
     
     {Check for a which way up}
     if TopDown then
      begin
       ConsoleWindowWriteLn (Handle3, 'TOPDOWN ');
       {Right way up is a rare case}
       for Count:=0 to BitMapInfoHeader.Height - 1 do
        begin
         {Update the position of the file stream}
         FileStream.Position:=BitMapFileHeader.bfOffset + (Count * ReadSize);
         
         {Read a full line of pixels from the file}     
         if FileStream.Read((Buffer + Offset)^,LineSize) <> LineSize then Exit;
         
         {Update the offset of our buffer}    
         Inc(Offset,LineSize);
        end;
        
      end
     else
      begin
       ConsoleWindowWriteLn (Handle3, 'UPSIDEDOWN ' );
       {Upside down is the normal case}
       for Count:=BitMapInfoHeader.Height - 1 downto 0 do
        begin
         {Update the position of the file stream}
         FileStream.Position:=BitMapFileHeader.bfOffset + (Count * ReadSize);
         
         {Read a full line of pixels from the file}     
         if FileStream.Read((Buffer + Offset)^,LineSize) <> LineSize then Exit;
         
         {Update the offset of our buffer}    
         Inc(Offset,LineSize);
        end;
      end;        
     
     {Draw the entire image onto our graphics console window in one request}
     //if GraphicsWindowDrawImage(Handle,X,Y,Buffer,BitMapInfoHeader.Width,BitMapInfoHeader.Height,Format) <> ERROR_SUCCESS then Exit;
     Pbuff(Size,Buffer);
     if GraphicsWindowDrawImage(Handle,X,Y,Buffer,BitMapInfoHeader.Width,BitMapInfoHeader.Height,Format) <> ERROR_SUCCESS then Exit;
     //PtoCptrs(A, @B, @C);
     Result:=True;
    finally
     ConsoleWindowWriteLn (Handle3, 'Going to free Buffer memory' );
      
       FreeMem(Buffer);
    end;
   end;
 finally
  FileStream.Free; 
 end;
end;


begin

 ConsoleWindowWriteLn (Handle1, 'TFTP Demo.');
 // wait for IP address and SD Card to be initialised.
 WaitForSDDrive;
 IPAddress := WaitForIPComplete;
 {Wait a few seconds for all initialization (like filesystem and network) to be done}
 Sleep(3000);

 {Create a graphics window to display our bitmap, let's use the new CONSOLE_POSITION_FULLSCREEN option}
 Window:=GraphicsWindowCreate(ConsoleDeviceGetDefault,CONSOLE_POSITION_BOTTOMLEFT);
 
 {Call our bitmap drawing function and pass the name of our bitmap file on the SD card,
  we also pass the handle for our graphics console window and the X and Y locations to
  draw the bitmap. 
  
  What happens if the bitmap is bigger than the window? It will be trimmed to fit, try it
  yourself and see}
 
 Handle:=ConsoleWindowCreate(ConsoleDeviceGetDefault,CONSOLE_POSITION_TOPLEFT,True);
 Handle1:=ConsoleWindowCreate(ConsoleDeviceGetDefault,CONSOLE_POSITION_TOPRIGHT,True);
 {Handle2:=ConsoleWindowCreate(ConsoleDeviceGetDefault,CONSOLE_POSITION_BOTTOMLEFT,True);}
 Handle3:=ConsoleWindowCreate(ConsoleDeviceGetDefault,CONSOLE_POSITION_BOTTOMRIGHT,True);
 ConsoleWindowWriteLn(Handle1, 'writing top right handle1');
 {ConsoleWindowWriteLn(Handle2, 'writing bottom left handle2');}
 ConsoleWindowWriteLn(Handle3, 'writing bottom right handle3');
 ConsoleWindowWriteLn(Handle, TimeToStr(Time));
  	
 //test;
 DrawBitmap(Window,'C:\MyBitmap.bmp',0,0); 
 //DrawBitmap(Window,'C:\MyBitmap.bmp',260,0);
 ConsoleWindowWriteLn (Handle, IntToStr(B));
 ConsoleWindowWriteLn (Handle1, 'Local Address ' + IPAddress);
 SetOnMsg (@Msg);
 ConsoleWindowWriteLn(Handle, TimeToStr(Time));
 ThreadHalt(0);
end.
