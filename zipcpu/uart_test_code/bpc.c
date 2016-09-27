#ifdef __ZIPCPU__
void *malloc(int sz);
void free(void *);
void zip_halt(void);
typedef int int32;
#else
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#endif
/*
The number of bit planes in a code block to be encoded (P)
is the largest number of mag array. 
cb code block
cbw width of code block
cbh height of code block
*a points to lifting values.
*/
void bp(int cb,int cbw,int cbh,int *a) {
	int row,col,nz,P,idx,ctn;
	int *ip,*sgn,*mag,*is,*im,*sgn_mag;
	int *p_states,*thea1,*thea2;
	//sgn_mag points to sign and magnitude arrays
	sgn_mag = (int *)malloc(sizeof(int)*(cbw*cbh)*2);	
	sgn = sgn_mag;
	 
	mag = &sgn_mag[cbw*cbh];
	 
	nz = 0;
	ctn = 0;
	//clr the sgn & mag arrays
	for(idx=0;idx<cbw*cbh*2;idx++) {
		sgn_mag[idx] = 0;
	}
	//Significance Propagation Pass (SPP): 
	//Bit positions that have a
	//magnitude of 1 for the first time (i.e., 
	//the most significant bit of the
	//corresponding sample coefficients) are 
	//coded in this pass.  pg 164

	for(row=0; row<cbh; row++) {
		ip = a + row;
		is = sgn + row;
		im = mag + row;
		//printf("row %d \n",row); 
		for(col=0; col<cbw; col++) {
			if (ip[0] < 0 ) {
				sgn[0] = 1;
				mag[0] = ip[0]*(-1);
			}
			else {
				sgn[0] = 0;
				mag[0] = ip[0];
			}
			//printf("%d %d %d %d %d \n",row,col,ip[0],sgn[0],mag[0]);
			if (mag[0] > nz) nz = mag[0];
			if (ip[0] == nz) ctn+=1;
			//printf("%d %d %d %d %d \n",row,col,ip[0],nz);
			ip+=1;
			is+=1;
			im+=1;
		}
		 
		ip+=256;
 
	}
	p_states = (int *)malloc(sizeof(int)*(cbw*cbh)*3);
	thea1 = &p_states[cbw*cbh];
	thea2 = &p_states[cbw*cbh*2];
	//clr the p_states arrays
	for(idx=0;idx<cbw*cbh*3;idx++) {
		p_states[idx] = 0;
	}

	//printf("%d %d %d  \n",cb,nz,ctn);
	//nz - 1 at start
	nz-=1;
	//CUP applies to every bit-plane of a code-block
	//after completion of MRP, except the first bit-plane, 
	//which does not need the MRP.

	//test p_states & thea1 are both zero pg 179	
	free(p_states);
	free(sgn_mag);
			
}
 
