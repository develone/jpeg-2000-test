#include<stdio.h>
#include <stdlib.h> 
 
	
/*	
python rd_wr_image.py used to create the file
img_to_fpga.bin
Compile the files jpeg.c & dwt_write.c

gcc jpeg.c dwt_write.c -o jpeg

run 1 level of dwt decompoistion
 
./jpeg jpeg img_to_fpga.bin pass.bin  num_passes 1 or 2 de-interleave

reads the img_to_fpga.bin and writes the file pass.bin
python rd_pass.py
Writes the file test1_256_fwt.png
 
*/
	
	extern void dwt_write(int *, int col, int row, int dum6);

	int main(int argc, char **argv) {
	int row,col,w,h,index,dum1,dum2,dum3,dum4,dum5,dum6,*dum7,num_passes,interleave;
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
        num_passes = atoi(argv[3]);
        interleave = atoi(argv[4]);
        fpin = fopen(argv[1], "rb");
           //printf("%x \n",buf_ptr);
           for(col = 0; col < w*h; col++) {
        	fread(buf_ptr, sizeof(int),1,fpin);
                //printf("%d\n",buf[col]);
                buf_ptr++;
           }
           //printf("%x \n",buf_ptr);
           /*the following is needed when pointers are used *(buf_ptr+col+row*256) 
           this was not needed when img[row][col] are used
           this was pointed out by Dr. Dan
           */
           buf_ptr = &buf[0];
           //printf("%x \n",buf_ptr);
           for(row = 0; row < h; row++) {
			   for (col = 0 ; col < w; col++) {
				   img[row][col] = buf[index];
				   index++;
        }
	}
for ( p =0; p < num_passes; p++) {
	printf("%x ",buf_ptr);
	printf("%d\n",p);
	for ( col = 0; col<w;col++) { 
		for (row = 2;row<h;row=row+2) {
			 img[row][col] = img[row][col] - ( (img[row-1][col] + img[row+1][col]) >> 1);
		}
		//end of even samples
		for (row = 1;row<h-2;row=row+2) {
			 img[row][col] = img[row][col] - ( (img[row-1][col] + img[row+1][col] +2) >> 2);
		}
		//end of odd samples
	}    

    //de_interleave 
    if ( interleave == 1) {
	/*
	zero the the tt array
	*/
	for ( row = 0;row < h-2;row++) {
		for (col = 0;col < w;col++) {
			tt[row][col] = 0;
		}
	}
	for ( row = 0 ; row < h; row++) {
		for (col = 0; col < w;col++) {  
			if (row % 2 == 0) {
				 tt[col][row/2] =  img[row][col];
			}	
			else {
				 tt[col][row/2 + 256/2] =  img[row][col];
			}	
		}
	}
	for ( row = 0;row < h-2;row++) {
		for (col = 0;col < w;col++) {
			img[row][col] = tt[row][col];
		}
	}
    }
    else {
    }
 
}
//end num_passes loop
/*
zero the the tt array
*/
for ( row = 0;row < h-2;row++) {
	for (col = 0;col < w;col++) {
		tt[row][col] = 0;
	}
}
/*
lower right corner to upper left corner
*/
for ( col = w/2; col < w ;col++) {
	for (row = h/2; row < h;row++) {
		tt[col-w/2][row-h/2] = img[row][col];
	}
}
/*
transfer tt array to img for output
*/
for ( row = 0;row < h-2;row++) {
	for (col = 0;col < w;col++) {
		img[col][row] = tt[row][col];
	}
}

/*
write the img to file pass.bin
*/
img_ptr = &img[0][0];
fpout = fopen(argv[2], "wb");
for (row = 0; row < h; row++) {
	for(col = 0; col < w; col++) {
		fwrite(&img[row][col],sizeof(int),1,fpout);
	}
}
//end of write to file  	
}
//end of program

