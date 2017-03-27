unit uBufferToC;

{$linklib dwtlift}

interface
procedure lift_config(decom: word; enc:word; TCP_DISTORATIO:word; ii: word; ss: LongWord; var tmpbuf: Pointer); cdecl; external 'libdwtlift' name 'lift_config';
implementation
end.
