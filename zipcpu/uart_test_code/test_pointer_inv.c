#ifdef __ZIPCPU__
void free(void *);
void zip_halt(void);
typedef int int32;
#else
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#endif


void pointer_inv_de_interleave(int ww, int offset, int *ibuf, int *tmpbuf) {
	FILE *ptr_myfile, *ofp;
	int idx,w,h,row,col, *idx_off; 
	int rb = 256;
	w = 256;
	h = 256;
	register int	*ip, *opb;
	
	idx_off = ibuf;
	//lvl1 32896 lvl2 49344 lvl3 57568   
	idx_off = idx_off + offset;
	
	//clearing the tmpbuf since it was used in fwt dwt	
	for(idx=0;idx<w*h;idx++)
		tmpbuf[idx]=0; 

		
	for(row=0;row<ww;row++) {
		//The input image for testing is 128 x 128
		ip = idx_off + row*256/2;
		opb = tmpbuf + row;  
		for(col=0;col<ww/2;col++) {
			opb[0]=ip[0];
			opb[256]=ip[128];
			 			
			ip+=1;     	//adding 1 is going down the rows
			opb+=2*256;		//adding 2*rowbytes going across the cols
		}	
	} 
	
		
}
