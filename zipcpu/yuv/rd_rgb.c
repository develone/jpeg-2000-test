#ifdef __ZIPCPU__
void free(void *);
typedef int int32;
#else
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <assert.h>
#endif


void rgb(int w, int *ibuf, int *a, int *a1, int *a2) {
	int *ip, *aa, *aa1, *aa2;
	ip = ibuf;
	aa = a;
	aa1 = a1;
	aa2 = a2;
	
	int idx,lidx;
	int red,green,blue;
	lidx = w * w;
	const int bb = 0x0ff;
	const int gg = 0x3fc00;
	const int rr = 0x0ff00000;

  	
	for(idx=0; idx<lidx; idx++) {
		
		red = ((ip[0])&rr)>>20;
		green = ((ip[0])&gg)>>10;
		blue = ((ip[0])&bb);
		
		ip+=1;
		
		aa[0] = red;
		aa1[0] = green;
		aa2[0] = blue;
		 
		aa+=1;
		aa1+=1;
		aa2+=1;
	}
}
