#include<stdio.h>
#include <stdlib.h>

void rd_image(char *fn,int *buf_ptr) { 
    int row, col,w,h;
    w = 256;
	h = 256;
    char *inpfn;
    inpfn = fn;
	FILE  *fpin;
    printf("in rd_image %s\n", inpfn);
        
	fpin = fopen(inpfn, "rb");
	for(col = 0; col < w*h; col++) {
		fread(buf_ptr, sizeof(int),1,fpin);
			buf_ptr++;
	}
}
void wr_image(char *fn, int *buf_ptr) {
    
    
    int row, col,w,h;
    w = 256;
	h = 256;
    char *outfn;
    outfn = fn;
    
	FILE *fpout;
    printf("in wr_image %s\n", outfn);
	fpout = fopen(outfn, "wb");
	for(col =0 ; col< w*h;col++) {
		 
			fwrite(buf_ptr,sizeof(int),1,fpout);
            buf_ptr++;
	}
	fclose(fpout);

}
 

