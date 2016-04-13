#include<stdio.h>
#include <stdlib.h> 
 
	
/*	
python rd_wr_image.py used to create the file
img_to_fpga.bin
Compile the files jpeg.c & dwt_write.c

gcc jpeg.c dwt_write.c -o jpeg

run 1 level of dwt decompoistion
 
./jpeg jpeg img_to_fpga.bin pass.bin

reads the img_to_fpga.bin and writes the file pass.bin
python rd_pass.py
Writes the file test1_256_fwt.png
 
*/
	
	extern void dwt_write(int *, int col, int row, int dum6);

	int main(int argc, char **argv) {
	int row,col,w,h,index,dum1,dum2,dum3,dum4,dum5,dum6,*dum7;
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
			 
				//img[row][col] = img[row][col] - ( (img[row-1][col] + img[row+1][col]) >> 1);
			
			 
				 //*(buf_ptr+col+row*256) = *(buf_ptr+col+row*256) - ((*(buf_ptr+col+(row-1)*256) + *(buf_ptr+col+(row+1)*256)) >> 1);
			 dum1 = *(buf_ptr+col+row*256);
			 dum2 = *(buf_ptr+col+(row-1)*256);
			 dum3 = *(buf_ptr+col+(row+1)*256);
			 dum4 = ((dum2 + dum3) >> 1);
			 
			 dum5 = *(buf_ptr+col+row*256);
			 dum6 = dum5 - dum4;
			 //dum7 = (&buf_ptr+col+row*256);
			 dum7 = buf_ptr;
			 dwt_write(dum7,col,row,dum6);
			 //printf("even %x %d %d %d\n",dum7, col, row, row*col*256 );
			 //*(buf_ptr+col+row*256)= dum6;
		}
		for (row = 1;row<256-2;row=row+2) {
			 
				//img[row][col] = img[row][col] - ( (img[row-1][col] + img[row+1][col] +2) >> 2);
			 
				// *(buf_ptr+col+row*256) = *(buf_ptr+col+row*256) - ((*(buf_ptr+col+(row-1)*256) + *(buf_ptr+col+(row+1)*256)+2) >> 2);
		     dum1 = *(buf_ptr+col+row*256);
			 dum2 = *(buf_ptr+col+(row-1)*256);
			 dum3 = *(buf_ptr+col+(row+1)*256);
			 dum4 = ((dum2 + dum3) >> 2);
			 
			 dum5 = *(buf_ptr+col+row*256);
			 dum6 = dum5 + dum4;
			 //dum7 = (&buf_ptr+col+row*256);
			 dum7 = buf_ptr;
			 dwt_write(dum7,col,row,dum6);
			 //printf("odd %x%d %d %d\n",dum7, col, row, row*col*256);
			 //*(buf_ptr+col+row*256) = dum6;
		}
	}
	for ( row = 0 ; row < 256; row++) {
		for (col = 0; col < 256;col++) {  
			if (row % 2 == 0) {
				 
					//tt[col][row/2] =  img[row][col];
				 
					*(de_interleave+col*256+row/2) =  *(buf_ptr+col+row*256);
				 
			}	
			else {
				 
					//tt[col][row/2 + 256/2] =  img[row][col];
				 
					*(de_interleave+col*256+row/2+256/2) =  *(buf_ptr+col+row*256);
				
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
