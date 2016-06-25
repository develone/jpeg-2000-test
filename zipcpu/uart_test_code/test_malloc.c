#include "board.h"

void test_malloc(void) {
	
int *dptr, *sptr;
int *ar_used = (char *)0x87fff8;
int *ar_size =	 (char *)0x87fff9;
int *sptr_used = (char *)0x87fffa;
int *dptr_used = (char *)0x87fffb;



int row,col,cc;
int w,h,r2,r2h;
w = 4;
h = 4;
int ar[w][h];
sptr = malloc(sizeof(int)*(w*h));
 
dptr = malloc(sizeof(int)*(w*h));
*ar_size = sizeof(ar);
*ar_used = &ar;
*sptr_used = sptr; 
*dptr_used = dptr;
free(sptr);
free(dptr);
}
