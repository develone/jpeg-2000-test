#include "board.h"


void zip_clear_sdram(int *imbuf) {
int val,i;

val = 0;
 
 
 
for(i=0; i<256*256*8; i++) {
	*imbuf++ = val;
}
}
