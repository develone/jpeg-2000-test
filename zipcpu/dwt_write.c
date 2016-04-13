/*#include<stdio.h>
#include <stdlib.h> 
*/
void dwt_write(int *a, int c, int r, int v) {
	int *b;
	b = a;
	*(a+c+r*256) = v;
//printf("in sub %x %d %d %d % d\n",b,c,r,c*r*256,  v);	
}
