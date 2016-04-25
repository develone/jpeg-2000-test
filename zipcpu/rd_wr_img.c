#include<stdio.h>
#include <stdlib.h>

void rd_image(int *buf_ptr) { 
    int row, col,w,h;
    w = 256;
	h = 256;
	FILE  *fpin;
	fpin = fopen("img_to_fpga.bin", "rb");
	for(col = 0; col < w*h; col++) {
		fread(buf_ptr, sizeof(int),1,fpin);
			buf_ptr++;
	}
}
void wr_image(int *buf_ptr) {
    
    
    int row, col,w,h;
    w = 256;
	h = 256;
    
	FILE *fpout;
	fpout = fopen("pass.bin", "wb");
	for(col =0 ; col< w*h;col++) {
		 
			fwrite(buf_ptr,sizeof(int),1,fpout);
            buf_ptr++;
	}
	fclose(fpout);

}
 

