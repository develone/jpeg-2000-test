#ifdef __ZIPCPU__
void free(void *);
void zip_halt(void);
typedef int int32;
#else
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#endif
/*  process the input image which is in the lower right corner
 *  rotates the images 90 degrees clockwise with the output 
 *  is twice the height of the original. 
 *   
*/
void array_inv(int *xxx, int ww) {
	FILE *ptr_myfile, *ofp;
	 
 
	int row,col, *offset_xxx,*origin_xxx;
 
    int rb = 256;
    register int	*ip, *opb;
    //register int	*ip, *op, *opb, a, b;
    origin_xxx = xxx;
    offset_xxx = xxx;
    
	//point to the 3 lvls of dwt within the image to 
	//create the yy array
	//32768 + 16384 + 8192 + 128 + 64 + 32
	if (ww==32) offset_xxx = offset_xxx + 57568;
	//32768 + 16384 + 128 + 64 
	if (ww==64) offset_xxx = offset_xxx + 49344;
	//32768  + 128 
	if (ww==128) offset_xxx = offset_xxx + 32896;
	//printf("%x %x %x\n",xxx,origin_xxx,offset_xxx); 
    for(row=0;row<ww;row++) { 
		ip = offset_xxx + 2*row*rb/2;
		opb = origin_xxx + 2*row;
		//op = opb + rb/2; 
		for(col=0;col<ww;col++) {

		
			ip+=1;     	//adding 1 is going across the row
			//op+=256;		//adding 256 is going down the col
			opb+=256;		//adding 256 is going down the co
            opb[0]=ip[0];
            opb[1]=ip[1];
	}
	
	} 
	   
	ofp = fopen("inpimg.bin","w");
	fwrite(xxx, sizeof(int), 256*256, ofp);
	fclose(ofp);
	
 
	
}
