unit uBufferToC;

{$linklib dwtlift}

interface
procedure lift_config(ii: word; ss: LongWord; var tmpbuf: Pointer); cdecl; external 'libdwtlift' name 'lift_config';
implementation
end.
