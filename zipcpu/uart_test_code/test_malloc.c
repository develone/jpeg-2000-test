#include "board.h"

void test_malloc(void) {
	
int *dptr, *sptr;	
int *sptr_used = (char *)0x87fffa;
int *dptr_used = (char *)0x87fffb;



int row,col,cc;
int w,h,r2,r2h;
w = 4;
h = 4;
sptr = malloc(sizeof(int)*(w*h));
 
dptr = malloc(sizeof(int)*(w*h));
*sptr_used = sptr; 
*dptr_used = dptr;
//free(sptr);
//free(dptr);
}
