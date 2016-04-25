#include<stdio.h>
#include <stdlib.h> 
#include <string.h> 
	
/*	
python rd_wr_image.py used to create the file
img_to_fpga.bin
compile rd_wr_img.c 
gcc -c rd_wr_img.c -o rd_wr_img.o
Compile the files jpeg.c 

gcc jpeg.c  rd_wr_img.o -o jpeg

run 1 level of dwt decompoistion
 
./jpeg jpeg img_to_fpga.bin pass.bin  num_passes 1 or 2 de-interleave 0 or 1 to print input file 0 or 1 to print output file

reads the img_to_fpga.bin and writes the file pass.bin
python rd_pass.py
Writes the file test1_256_fwt.png
 
*/
	
	//extern void dwt_write(int *, int col, int row, int dum6);
	extern rd_image(char *fn,int *buf_ptr);
	extern wr_image(char *fn,int *buf_ptr);
	int main(int argc, char **argv) {
	 
    int row,col,w,h,interleave,num_passes,debug,debug1;
	 
	  
   	 w = 256;
   	 h = 256;
	 char *inpfn,*outfn; 
	 int buf[w*h];
	 int buf1[w*h];
	 int *buf_ptr;
 
	 buf_ptr = buf;
	  
         int p;
	 
        //FILE  *fpin, *fpout;
        inpfn = argv[1];
        outfn = argv[2];
        printf("in main %s\n", inpfn);
        printf("in main %s\n", outfn);

        num_passes = atoi(argv[3]);
        interleave = atoi(argv[4]);
 		debug = atoi(argv[5]);
        debug1 = atoi(argv[6]); 
rd_image(inpfn,buf_ptr);
	if(debug == 1) { 
	for(col = 0; col < w*h; col++) {
		printf("%d\n",buf[col]);
	}            
 	}
for ( p =0; p < num_passes; p++) {
	
	printf("%d\n",p);
	for ( col = 0; col<w;col++) { 
		for (row = 2;row<h;row=row+2) { 
			  
             buf[(row*256)+col] = buf[(row*256)+col] - (( buf[((row-1)*256)+col] + buf[((row+1)*256)+col] ) >> 1); 
		}
		//end of even samples
		for (row = 1;row<h-2;row=row+2) {
			  
             buf[(row*256)+col] = buf[(row*256)+col] + (( buf[((row-1)*256)+col] + buf[((row+1)*256)+col] + 2) >> 2);

		}
		//end of odd samples
	}    

    //de_interleave 
    if ( interleave == 1) {
 
	//zero the the buf1 array
	for (col = 0; col<w*h;col++) {
		buf1[col] = 0;
	}
	for ( row = 0 ; row < h; row++) {
		for (col = 0; col < w;col++) {  
			if (row % 2 == 0) {
				  
				buf1[(row/2)+256*col] =  buf[(row*256)+col];
			}	
			else {
				 
				 buf1[col*256+(row/2 + 256/2)] =  buf[(row)*256+col];
			}	
		}
	}
	for ( row = 0;row < h-2;row++) {
		for (col = 0;col < w;col++) {
			 
			buf[(row)*256+col] = buf1[(row)*256+col];
		}
	}
    }
    else {
    }
 
}
//end num_passes loop
 
	//zero the the buf1 array
	for (col = 0; col<w*h;col++) {
		buf1[col] = 0;
	}
/*
lower right corner to upper left corner
*/
for ( col = w/2; col < w ;col++) {
	for (row = h/2; row < h;row++) {
 
		buf1[256*(col-w/2)+ (row-h/2)] = buf[256*row+col];
	}
}
/*
transfer tt array to img for output
*/
for ( row = 0;row < h-2;row++) {
	for (col = 0;col < w;col++) {
 
		buf[256*col+row] = buf1[256*row+col];
	}
}

if (debug1==1) {
	printf("writing output file\n");
	for(col = 0; col < w*h; col++) {
		printf("%d\n",buf[col]);
	}            
 	
}
//buf_ptr = buf;
wr_image(outfn,buf_ptr);
 
}
//end of program

