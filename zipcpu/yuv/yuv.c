#ifdef __ZIPCPU__
void free(void *);
typedef int int32;
#else
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <assert.h>
#endif

/*
computes u  v using y' ii. blue a2. and red a
y = (r + (g * 2) + b) >> 2;
u = b - g;
v = r - g;
*/
void yuv(int w, int *a, int *a1, int *a2, int *a3, int *a4, int *ii) {
	int idx, lidx;
	int *aa, *aa1, *aa2, *aa3, *aa4, *im;
	
	aa = a;
	aa1 = a1;
	aa2 = a2;
	aa3 = a3;
	aa4 = a4;
	im = ii;
		
	lidx = w * w;
	
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

/*
computes r g b  from u v using y ii u a3 v a4 . 
red a green a1, and blue a2.
g = y - ((u + v) >> 2);
r = v + g;
b = u + g;
*/
void invyuv(int w, int *a, int *a1, int *a2, int *a3, int *a4, int *ii) {
	int idx, lidx;
	int *aa, *aa1, *aa2, *aa3, *aa4, *im;
	
	aa = a;  //red
	aa1 = a1;  //green
	aa2 = a2;  //blue
	aa3 = a3;  //u
	aa4 = a4;  //v
	im = ii;   //y
	
 
		
	lidx = w * w;
	
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
