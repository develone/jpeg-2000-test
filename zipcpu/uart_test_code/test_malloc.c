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
    //sys->io_bustimer = 0x7fffffff;
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
	int *clocks_used = (int *)0x87fffe;
	int *ar_used = (int *)0x87fff8;
	int *ar_size =	 (int *)0x87fff9;
	int *sptr_used = (int *)0x87fffa;
	int *dptr_used = (int *)0x87fffb;
	int *buf_ptr = (int *)0x800000;
    int *buf_dwt = (int *)0x810000;

	int row,col,steps;
	int w,h,rgb;

	w = 256;
	h = 256;

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
 
 


	
	*sptr_used = sptr; 
	for(row=0;row<h;row++)
	{
		for(col=0;col<w;col++)
		{
			rgb = *buf_ptr++;
			*buf_r++ = (rgb&rr)>>20;
			*buf_g++ = (rgb&gg)>>10;
			*buf_b++ = (rgb&bb);
		}
 
	}

	//time to here 0x30c514 0.03995225  splitting 256 x 256 following read 1.971 
	sptr = *buf_r_used;
    sys->io_bustimer = 0x7fffffff;
	//lifting(w,sptr,buf_dwt);
	*clocks_used = 0x7fffffff-sys->io_bustimer;
	//set sptr to buf_r - increments of setting
	//buf_r with values from rgb
 
free(sptr);

free(buf_r);
free(buf_g);
free(buf_b);
}
