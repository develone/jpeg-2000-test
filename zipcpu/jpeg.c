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
	 
    int row,col,w,h;
	index = 0;
	
   	 w = 256;
   	 h = 256;
	  
	 int buf[w*h];
	 int buf1[w*h];
	 int *buf_ptr;
 
	 buf_ptr = &buf;
	  
         int p;
	 
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
            
           buf_ptr = &buf[0];
            

for ( p =0; p < num_passes; p++) {
	printf("%x ",buf_ptr);
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

/*
write the buf to file pass.bin
*/
 
fpout = fopen(argv[2], "wb");
for (row = 0; row < h; row++) {
	for(col = 0; col < w; col++) {
		 
		fwrite(&buf[256*row+col],sizeof(int),1,fpout);
	}
}
//end of write to file  	
}
//end of program

