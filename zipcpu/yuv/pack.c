#ifdef __ZIPCPU__
void free(void *);
typedef int int32;
#else
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <assert.h>
#endif

void packyuv(int w,int *y,int *u,int *v,int *pck) {
	int idx, lidx;
	int *wy,*wu,*wv,*wpck;
	const int msk = 0x2ff;
	wy = y;
	wu = u;
	wv = v;
 	wpck = pck;
	lidx = w * w;
 
	for(idx=0; idx<lidx; idx++) {
		
		wy[0] = (wy[0]&msk)<<20;
		wu[0] = (wu[0]&msk)<<10;		 
		wv[0] = wv[0]&msk;
                wpck[0] = wy[0]+wu[0]+wv[0];
		
		wy+=1;
		wu+=1;
		wv+=1;
		wpck+=1;
	}
	
	 
}


 
