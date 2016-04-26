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
    extern lift(int buf[],int num_passes, int interleave );
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
 
if (debug1==1) {
	printf("writing output file\n");
	for(col = 0; col < w*h; col++) {
		printf("%d\n",buf[col]);
	}            
 	
}
//buf_ptr = buf;
lift(buf,num_passes,interleave);
wr_image(outfn,buf_ptr);
 
}
//end of program

