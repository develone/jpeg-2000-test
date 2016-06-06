#include "board.h"


void zip_clear_sdram(char *imbuf) {
int val,i;

val = 0;
 
 
 
for(i=0; i<256*256; i++) {
	*imbuf++ = val;
}
}
