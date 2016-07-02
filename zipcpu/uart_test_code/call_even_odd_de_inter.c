#include<stdio.h>
#include<stdlib.h>
#include<stdint.h>
void main(void) {
    int w,h;
    w = 256;
    h = 256;
    int *img, *alt;
    
    img = (int *)malloc(sizeof(int)*(w*h)*2);
    alt = &img[256*256];
    //printf("%d %x, %x %d\n",w,img,alt,sizeof(img)); 
	//int	*img = SDRAM, *alt = &img[256*256];
	//int	done;

	//sys->io_bustimer = 0x7fffffff;
	lifting(w, img, alt);
	//done = 0x7fffffff - sys->io_bustimer;
	//img[0] = done;
    free (img);	
    }
