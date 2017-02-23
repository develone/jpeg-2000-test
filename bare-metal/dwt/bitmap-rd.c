/* http://www.instesre.org/howto/BW_image/ReadingBitmaps.htm
 * read header */
#include <stdio.h>
#include <sys/time.h>
#include "lifting.h"
#include "dwtlift.h"
#include <stdlib.h>

extern void lift_config(int dec, int enc, int mct, int bp, long imgsz,int *bufferptr);
//extern void yuv(int w,int *r,int *g,int *b,int *u,int *v,int *y);
//extern void invyuv(int w,int *r,int *g,int *b,int *u,int *v,int *y);

int main(int argc, char **argv) {
struct rec {
	unsigned char header[14];	
};
struct rec1 {
	unsigned char imginfo[40];	
};

FILE *in,*fp;
char *fn;
int *red, *green, *blue;
char inchar;
int i,bpp;
long int offset,width,height;
int pixels, size, sz;
int *databuffer;

	encode = 1;
	decomp = 5;
	flgyuv = 1;
	printf("enc %d decomp %d yuv %d\n",encode,decomp,flgyuv);

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
  * 3145850
  * 14 40 54
  * 3145728
  * 68
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
	i = 0;	
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
	
	databuffer = (int*)(&data[0]);
	
	printf("databuffer address 0x%x data address 0x%x  \n",databuffer,&data[0]);
	
	for(i=0; i<(offset-54); i++) {
		fread(&inchar,sizeof(inchar),1,in);
		 
		//printf("%c ",inchar);
	}
	fread(&data[0],sizeof(data),1,in);
	/*
	for(i=0; i<size; i++) {
		//fread(&inchar,sizeof(inchar),1,in);
		//data[i] = inchar;
		printf(" %d %d\n ",i,data[i]);
	}
	*/
	printf("first byte 0x%x sixe/3 %d\n ",data[0],size/3);
	
	int data_red[size/3],data_green[size/3],data_blue[size/3];
	
	red = &data_red[0];
	green = &data_green[0];
	blue = &data_blue[0];
	/*
	printf("splitting data to rgb\n");
	
	for(i=0; i<size-3; i=i+3) { 	
		*red = data[i];
		*green = data[i+1];
		*blue = data[i+2];
		red++;
		green++;
		blue++;
		
		//printf("%d\n",i);
		
	}
	printf("splitting data to rgb done \n");

	/*	
	red = &data_red[0];
	green = &data_green[0];
	blue = &data_blue[0];
	
	fp = fopen("red-out.32t","w");
	if (NULL == fp) {
		fprintf(stderr, "Could not open red for writing\n");
		perror("RED-WR:");
		exit(EXIT_FAILURE);
	}
		 
	if (sz != (int)fwrite(red,  sizeof(int), sz, fp)) {
		fprintf(stderr, "Write of red failed\n"); perror("RED:");
		exit(EXIT_FAILURE);
	}
	fclose(fp);
	*/
	//lift_config(decomp, encode, flgyuv, bpp, (long)size, databuffer);
	return 0;
}
