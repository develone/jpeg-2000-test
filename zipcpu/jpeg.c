#include<stdio.h>
#include <stdlib.h> 
 
	
   /*	
   int *jpeg_process(int *img_ptr, int w, int h) {
	

	
	return de_interleave;
	*/
	
	
	int main(int argc, char **argv) {
	int row,col,w,h,index;
	index = 0;
	
   	 w = 256;
   	 h = 256;
	 int img[w][h];
	 int buf[w*h];
	 int *buf_ptr;
	 
	 buf_ptr = &buf;
	 int *img_ptr;	
    	 img_ptr = &img;
         int p;
	int tt[w][h];
	int *de_interleave;
	de_interleave = &tt;
        FILE  *fpin, *fpout;
        printf("%s\n", argv[1]);
        printf("%s\n", argv[2]);
        fpin = fopen(argv[1], "rb");
        
           for(col = 0; col < w*h; col++) {
        	fread(buf_ptr, sizeof(int),1,fpin);
                //printf("%d\n",buf[col]);
                buf_ptr++;
           }
           for(row = 0; row < h; row++) {
			   for (col = 0 ; col < w; col++) {
				   img[row][col] = buf[index];
				   index++;
        }
	}
	for ( p =0; p < 2; p++) {
	for ( col = 0; col<256;col++) { 
		for (row = 2;row<256;row=row+2) {
			img[row][col] = img[row][col] - ( (img[row-1][col] + img[row+1][col]) >> 1);
		}
		for (row = 1;row<256-2;row=row+2) {
			img[row][col] = img[row][col] - ( (img[row-1][col] + img[row+1][col] +2) >> 2);
		}
	}
	for ( row = 0 ; row < 256; row++) {
		for (col = 0; col < 256;col++) {  
			if (row % 2 == 0) {
				tt[col][row/2] =  img[row][col];
			}	
			else {
				tt[col][row/2 + 256/2] =  img[row][col];
			}	
		}
	}   
	for ( row = 0;row < 256-2;row++) {
		for (col = 0;col < 256;col++) {
			img[row][col] = tt[row][col];
		}
	}
	img_ptr = &img[0][0];
        fpout = fopen(argv[2], "wb");
        for (row = 0; row < h; row++) {
           for(col = 0; col < w; col++) {
        	fwrite(img_ptr,sizeof(int),1,fpout);
                img_ptr++;
           }
        }  
        }
	//de_img[w][h] = jpeg_process(img_ptr, w, h);
	}
