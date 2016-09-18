#ifdef __ZIPCPU__
void free(void *);
typedef int int32;
#else
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <assert.h>
#endif
 
 
int main(void) {

	int row,col;
	int w,h,r2,r2h,red,green,blue,steps;
	w = 256;
	h = 256;

 
	int *img, *alt, *alt1, *alt2, *alt3, *alt4, *alt5, *sav_img;
	int *alt6, *alt7, *alt8, *alt9, *alt10;
	img = (int *)malloc(sizeof(int)*(w*h)*13);
	FILE *ptr_myfile, *ofp;
	sav_img = img;	
	alt = &img[256*256];//red
	alt1 = &img[256*256*2];//green
	alt2 = &img[256*256*3];//blue
	alt3 = &img[256*256*4];//u
	alt4 = &img[256*256*5];//v
	alt5 = &img[256*256*6];//red
	alt6 = &img[256*256*7];//green
	alt7 = &img[256*256*8];//blue
	alt8 = &img[256*256*9];//u
	alt9 = &img[256*256*10];//v
	
 
	
	ofp = fopen("pck.bin","r");
	fread(alt, sizeof(int), w*h, ofp);
	fclose(ofp);
	
	unpackyuv(w,img,alt3,alt4,alt);	

	ofp = fopen("uydwt.bin","w");
	fwrite(img, sizeof(int), w*h, ofp);
	fclose(ofp);
	
	ofp = fopen("uudwt.bin","w");
	fwrite(alt3, sizeof(int), w*h, ofp);
	fclose(ofp);
	
	ofp = fopen("uvdwt.bin","w");
	fwrite(alt4, sizeof(int), w*h, ofp);
	fclose(ofp);		
	free (img);	
}
