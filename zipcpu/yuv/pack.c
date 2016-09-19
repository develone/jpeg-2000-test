#ifdef __ZIPCPU__
void free(void *);
typedef int int32;
#else
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <assert.h>
#endif
void quantize(int w,int *y,int *u,int *v) {
	int idx, lidx;
	int *wy,*wu,*wv;
	
	wy = y;
	wu = u;
	wv = v;
 	
	lidx = w * w;
	
	for(idx=0; idx<lidx; idx++) {
		 
		wy[0] = wy[0]>>1;
		wu[0] = wu[0]>>1;
		wv[0] = wv[0]>>1;
		 
		wy+=1;
		wu+=1;
		wv+=1;	
	}		
}
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
void unpackyuv(int w,int *y,int *u,int *v,int *pck) {
	int idx, lidx;
	int *wy,*wu,*wv,*wpck;
	const int uv = 0x3ff;
	const int uu = 0xffc00;
	const int yy = 0x2ff00000;
	const int neg = 0x00000200;
	const int fill = 0xffffff00;
	wy = y;
	wu = u;
	wv = v;
 	wpck = pck;
	lidx = w * w;
 
	for(idx=0; idx<lidx; idx++) {
		wy[0] = (wpck[0]&yy)>>20;
		if ((wy[0]&neg) == 512) {
			wy[0] = wy[0]|fill;
		}
		wu[0] = (wpck[0]&uu)>>10;
		if ((wu[0]&neg) == 512) {
			wu[0] = wu[0]|fill;
		}
		wv[0] = (wpck[0]&uv);
		if ((wv[0]&neg) == 512) {
			wv[0] = wv[0]|fill;
		}
				 		
		wy+=1;
		wu+=1;
		wv+=1;
		wpck+=1;
	}	 
}

 
