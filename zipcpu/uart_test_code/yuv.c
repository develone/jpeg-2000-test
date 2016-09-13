#ifdef __ZIPCPU__
void free(void *);
typedef int int32;
#else
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <assert.h>
#endif
typedef struct {
    int w, *y, *u, *v, *r, *g, *b;
} YUVARGS;

/*
computes u  v using y.  b. and  r
y = (r + (g * 2) + b) >> 2;
u = b - g;
v = r - g;
*/
void yuv(YUVARGS *ya) {
	int idx, lidx;
	int *aa, *aa1, *aa2, *aa3, *aa4, *im;
	
	aa = ya->r;
	aa1 = ya->g;
	aa2 = ya->b;
	aa3 = ya->u;
	aa4 = ya->v;
	im = ya->y;
	
	lidx = ya->w * ya->w;
	
	for(idx=0; idx<lidx; idx++) {

 
		
		im[0] = (aa[0] + aa1[0]*2 + aa2[0])>>2;
		//u = b - g 
		aa3[0] = aa2[0] - aa1[0];
		//v = r - g
		aa4[0] = aa[0] - aa1[0];
		im+=1;
		aa+=1;
		aa2+=1;
		aa3+=1;
		aa4+=1;
		
	} 
}

/*computes r g b  from u v using y  u  v . 
r  g , and  b.
g = y - ((u + v) >> 2);
r = v + g;
b = u + g;
*/
void invyuv(YUVARGS *ya) {
	int idx, lidx;
	int *aa, *aa1, *aa2, *aa3, *aa4, *im;
	
	aa = ya->r;
	aa1 = ya->g;
	aa2 = ya->b;
	aa3 = ya->u;
	aa4 = ya->v;
	im = ya->y;
	
	lidx = ya->w * ya->w;
	
	for(idx=0; idx<lidx; idx++) {
		
		//g = y - ((u + v) >> 2);
		aa1[0] = (im[0] - ((aa3[0] + aa4[0]) >> 2));
		 
		//r = v + g;
		aa[0] = aa4[0] + aa1[0];
		//b = u + g;
		aa2[0] = aa3[0] + aa1[0];
		
		im+=1;
		aa+=1;
		aa1+=1;
		aa2+=1;
		aa3+=1;
		aa4+=1;
		
	} 
}
