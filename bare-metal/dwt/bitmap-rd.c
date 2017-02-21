/* http://www.instesre.org/howto/BW_image/ReadingBitmaps.htm
 * read header */
#include <stdio.h>
#include <sys/time.h>
#include "lifting.h"
#include "dwtlift.h"

struct rec {
	unsigned char header[14];
	
};
struct rec1 {
	unsigned char imginfo[40];	
};

FILE *in;
char *fn;
char inchar;
int i,bpp;
long int offset,width,height;
int loop, decomp, encode, mct;
struct timeval currentTime,start,end;
int pixels, size;


int main(int argc, char **argv) {


fn = argv[1];
/*
Section	Description
Header	Basic file information, 14 bytes
Image Information Header	Information about the image, 40 bytes
Color Information (optional)	Information about how the image encodes colors, a variable number of bytes if it's present
Image data	The actual image, a variable number of bytes
*/
/*
 * 0  1  2   3 4  5 6 7 8 9 a   b c d
 * 66 77 122 0 48 0 0 0 0 0 122 0 0 0
 * 
 *                                    1                                    2 
 * 0   1 2 3 4 5 6 7 8 9 a b c d e  f 0 1 2 3 4 5 6  7 8  9  a b c  d  e f 0 1 2 3 4 5 6 7
 * 108 0 0 0 0 4 0 0 0 4 0 0 1 0 24 0 0 0 0 0 0 0 48 0 19 11 0 0 19 11 0 0 0 0 0 0 0 0 0 0
 */
 /*
  * Header size, bytes (should be 40)	4 bytes
  * Image width, pixels	4 bytes
  * Image height, pixels	4 bytes
  * Number of color planes	2 bytes
  * Bits per pixel, 1 to 24	2 bytes
  * Compression, bytes (assumed 0)	4 bytes
  * Image size, bytes	4 bytes
  * X-resolution and y-resolution, pixels per meter	4 bytes each
  * Number of colors and "important colors," bytes	4 bytes each
  */
	struct rec record;
	struct rec1 record1;
 
	in = fopen(fn,"rb");
	
	
	if (!in) {
 		printf("Unle to open file!");
		return 1;
	}
	
	/* read header */
	 
	fread(&record,sizeof(struct rec),1,in);
	while(i<14) {
	
		printf("%i ",record.header[i]);
		i++;
	}
	 
	
	printf("\n");
	//xx1 = (long)record.header[4];
	printf("file size = %li\n",(long)record.header[4]*65536+(long)record.header[3]*256+(long)record.header[2]);
	offset = (long)record.header[11]*256+(long)record.header[10];
	printf("offset to image = %i\n",offset);
	
	/* Image Information Header */
	fread(&record1,sizeof(struct rec1),1,in);
	i = 0;
		while(i<40) {
	
		printf("%i ",record1.imginfo[i]);
		i++;
	}
		
	width = (long)record1.imginfo[5]*256+(long)record1.imginfo[4];
	height = (long)record1.imginfo[9]*256+(long)record1.imginfo[8];
	printf("\n");
	printf("width = %i height = %i\n",width,height);
	
	bpp = record1.imginfo[14];
	printf("\n");
	printf("bits per pixel = %i\n",bpp);
	pixels = width * height;
	size = pixels*3;
	printf("pixels = %d size = %d \n",pixels,size);
	char data[size];
	int *databuffer;
	databuffer = &data[0];
	printf("address 0x%x\n",*databuffer);
	printf("buffer address 0x%x data address 0x%x  \n",databuffer,&data[0]);
	
	for(i=0; i<(122-54); i++) {
		fread(&inchar,sizeof(inchar),1,in);
		 
		//printf("%c ",inchar);
	}
	
	for(i=0; i<size; i++) {
		fread(&inchar,sizeof(inchar),1,in);
		data[i] = inchar;
		//printf("%c ",inchar);
	}
	printf("first byte %d \n ",data[0]);
	encode = 1;
	decomp = 5;
	mct = 1;
	lift_config(decomp, encode, mct, bpp, size, databuffer);
}
