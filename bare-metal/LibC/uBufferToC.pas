unit uBufferToC;

{$linklib test}

interface
procedure Pbuff(var ss: LongWord; var tmpbuf: Pointer); cdecl; external 'libtest' name 'xyz';
implementation
end.
