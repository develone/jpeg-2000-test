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
ibuf points to packed rgb
W R = 0.299 
W G = 1 − W R − W B = 0.587 
W B = 0.114 
Y ′ = W R R + W G G + W B B = 0.299 R + 0.587 G + 0.114 B
*/
/*
computes u  v using y' ii. blue a2. and red a

*/
void yuv(int w, int *a, int *a2, int *a3, int *a4, int *ii) {
	int idx, lidx;
	int *aa, *aa2, *aa3, *aa4, *im;
	
	aa = a;
	aa2 = a2;
	aa3 = a3;
	aa4 = a4;
	im = ii;

	//0.492 * 1024 504
	const int c4 = 504;
	//0.877 *1024 898
	const int c5 = 898;
		
	lidx = w * w;
	
	for(idx=0; idx<lidx; idx++) {

		//0.492(blue - Y')
		aa3[0] = (aa2[0] - im[0]);
		aa3[0] = ((aa3[0]*c4)/1024);
		//0.877(red - Y')
		aa4[0] = (aa[0] - im[0]);
		aa4[0] = ((aa4[0]*c5)/1024);
		
		
		im+=1;
		aa+=1;
		aa2+=1;
		aa3+=1;
		aa4+=1;
		
	} 
}
/*
computes yprime from r g b  this will be used on zipcpu before calling yuv.
*/
void yprime(int w, int *a, int *a1, int *a2, int *ii) {
	int *aa, *aa1, *aa2, *im;
	int idx,lidx, wght;
	lidx = w * w;

	//0.299 * 1024 306
	const int c1 = 306;
	//0.587 * 1024 601
	const int c2 = 601;
	//0.114 * 1024 117
	const int c3 = 117;
	
	aa = a;
	aa1 = a1;
	aa2 = a2;
	im = ii;
	for(idx=0; idx<lidx; idx++) {
		 
		wght = ((aa[0]*c1+aa1[0]*c2+aa2[0]*c3)/1024);
		 
		im[0] = wght;
		im+=1;
		aa+=1;
		aa1+=1;
		aa2+=1;
	}
}
