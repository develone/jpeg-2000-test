#include "board.h"
#include "dwt_funcs.h"

#ifdef __ZIPCPU__
void *malloc(int sz);
void free(void *);
typedef int int32;
#else
#include <stdlib.h>
#include <stdint.h>
#endif
void test_malloc(void) {

    const int bb = 0x1ff;
    const int gg = 0x7fc00;
    const int rr = 0x1ff00000;
    int *buf_r;
    int *buf_g;
    int *buf_b;    	
	int *dptr, *sptr;
	//the contents of the buf_r_used
	//where the red lift steps are stored
	//before packing to send back to RPi2B
	
	int *buf_r_used = (int *)0x87fff2;
	int *buf_g_used = (int *)0x87fff3;
	int *buf_b_used = (int *)0x87fff4;
	
	int *ar_used = (int *)0x87fff8;
	int *ar_size =	 (int *)0x87fff9;
	int *sptr_used = (int *)0x87fffa;
	int *dptr_used = (int *)0x87fffb;
	int *buf_ptr = (int *)0x800000;
    int *buf_dwt = (int *)0x810000;

	int row,col,steps;
	int w,h,rgb;

	w = 32;
	h = 32;

	int ar[w][h];
	//pointers to r g b
	
	buf_r = (int *)malloc(sizeof(int)*(w*h));
	buf_g = (int *)malloc(sizeof(int)*(w*h));
	buf_b = (int *)malloc(sizeof(int)*(w*h));
	//pointer to un-packed r g b
	//saved at pointer buf_r_used 0x87fff2
	//buf_g_used 0x87fff3
	//buf_b_used 0x87fff4
	*buf_r_used = buf_r;
	*buf_g_used = buf_g;
	*buf_b_used = buf_b;
	
	sptr = (int *)malloc(sizeof(int)*(w*h));
 
	dptr = (int *)malloc(sizeof(int)*(w*h));
	*ar_size = sizeof(ar);
	*ar_used = &ar;


	
	*sptr_used = sptr; 
	*dptr_used = dptr;
	for(row=0;row<h;row++)
	{
		for(col=0;col<w;col++)
		{
			rgb = *buf_ptr++;
			*buf_r++ = (rgb&rr)>>20;
			*buf_g++ = (rgb&gg)>>10;
			*buf_b++ = (rgb&bb);
		}
	    //buf_ptr moved to next row
	    //buf_ptr at 0x40 incremented by col loop above
		buf_ptr = buf_ptr + 224;
 
	}
	//time to here 0x3111 0.0001570125 16 x 16 following read 1.971 buf_ptr = buf_ptr + 240;
	//time to here 0xc4d7 0.0006298875 32 x 32	following read 1.971 buf_ptr = buf_ptr + 224;
	//time to here 0x305e4 0.00247645 64 x 64 following read 1.971 buf_ptr = buf_ptr + 192;
	//time to here 0x30c8ed 0.0399645625 256 x 256 following read 1.971 
	sptr = *buf_r_used;
	lift_step(sptr,w,h);
	//set sptr to buf_r - increments of setting
	//buf_r with values from rgb
	/*
	sptr = buf_r - (w*h);		
	for(steps=0;steps<1;steps++){
		if (steps == 0)	{
			w = 64;
			h = 64;
		}
		if (steps == 1)	{
			w = 32;
			h = 32;
		}
		if (steps == 2)	{
			w = 16;
			h = 16;
		}
	 	
		lift_step(sptr,w, h);
		de_interleave(sptr,w,h);
		lift_step(sptr,w, h);
		de_interleave(sptr,w,h);
		lower_upper(sptr,w,h);
}*/

free(sptr);
free(dptr);
free(buf_r);
free(buf_g);
free(buf_b);
}
