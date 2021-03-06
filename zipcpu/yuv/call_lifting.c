#ifdef __ZIPCPU__
void free(void *);
typedef int int32;
#else
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <assert.h>
#endif
 
struct rec {
	char raw_buf[3];
};
int main(void) {
	
	const int bb = 0x0ff;
	const int gg = 0x3fc00;
	const int rr = 0x0ff00000;
 
	//read RGB data from file 
	int index; 	
	int i,ii0,ii1,ii2,val;
	int *buf;
	int xx[65536];
	buf = (int *)&xx[0];	
	struct rec my_record;
	assert(sizeof(struct rec)==3);
	//struct results my_results;
	FILE *ptr_myfile, *ofp;

	ptr_myfile=fopen("rgb.bin","rb");
	if (!ptr_myfile) {
 		printf("Unle to open file!");
		return 1;
	} 

	for (i= 0;i<65536;i++) {
		fread(&my_record,sizeof(struct rec),1,ptr_myfile);
		ii0 = (int)my_record.raw_buf[0];
		ii1 = (int)my_record.raw_buf[1];
		ii2 = (int)my_record.raw_buf[2];
		val = ii0<<20|ii1<<10|ii2;
		*buf++=val;
		//printf("%d %x %x %x %x \n",i,ii0,ii1,ii2,val);
	}
	fclose(ptr_myfile);


	int row,col,cc;
	int w,h,r2,r2h,red,green,blue,steps;
	w = 256;
	h = 256;

 
	cc = 0;

	buf = (int *)&xx[0];

	
 
	int *img, *alt, *alt1, *alt2, *alt3, *alt4, *alt5, *sav_img;
	int *alt6, *alt7, *alt8, *alt9, *alt10;
	img = (int *)malloc(sizeof(int)*(w*h)*13);
	
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
	
	rgb(w, buf, alt, alt1, alt2);
		
	ofp = fopen("green.bin","w");
	fwrite(alt1, sizeof(int), w*w, ofp);
	fclose(ofp);

	ofp = fopen("blue.bin","w");
	fwrite(alt2, sizeof(int), w*w, ofp);
	fclose(ofp); 
	 
	ofp = fopen("red.bin","w");
	fwrite(alt, sizeof(int), w*w, ofp);
	fclose(ofp);
	
	img = sav_img;
	alt = &img[256*256];//red
	alt1 = &img[256*256*2];//green
	alt2 = &img[256*256*3];//blue
	alt3 = &img[256*256*4];//u
	alt4 = &img[256*256*5];//v
	alt5 = &img[256*256*6]; 
	alt6 = &img[256*256*7];//red
	alt7 = &img[256*256*8];//green
	alt8 = &img[256*256*9];//blue
	alt9 = &img[256*256*10];
		
	//yprime(w, alt, alt1, alt2, img);
	

	
	img = sav_img;	
	alt = &img[256*256];//red
	alt1 = &img[256*256*2];//green
	alt2 = &img[256*256*3];//blue
	alt3 = &img[256*256*4];//u
	alt4 = &img[256*256*5];//v
	alt5 = &img[256*256*6]; 
	alt6 = &img[256*256*7];//red
	alt7 = &img[256*256*8];//green
	alt8 = &img[256*256*9];//blue
	alt9 = &img[256*256*10];
	yuv(w, alt, alt1, alt2, alt3, alt4, img);
	invyuv(w, alt6, alt7, alt8, alt3, alt4, img);

	ofp = fopen("rr.bin","w");
	fwrite(alt6, sizeof(int), w*h, ofp);
	fclose(ofp);

	img = sav_img;
	alt7 = &img[256*256*8];
	ofp = fopen("gg.bin","w");
	fwrite(alt1, sizeof(int), w*h, ofp);
	fclose(ofp);
	
	ofp = fopen("bb.bin","w");
	fwrite(alt8, sizeof(int), w*h, ofp);
	fclose(ofp);

	ofp = fopen("yy.bin","w");
	fwrite(img, sizeof(int), w*w, ofp);
	fclose(ofp);
	
	
	
	img = sav_img;
	alt3 = &img[256*256*4];
	ofp = fopen("u.bin","w");
	fwrite(alt3, sizeof(int), w*h, ofp);
	fclose(ofp);

	img = sav_img;
	alt4 = &img[256*256*5];
	alt5 = &img[256*256*6];
	
	ofp = fopen("v.bin","w");
	fwrite(alt4, sizeof(int), w*h, ofp);
	fclose(ofp);	 	  

	img = sav_img;
	alt3 = &img[256*256*4];
	alt5 = &img[256*256*6];
	lifting(w,alt3,alt5);

	ofp = fopen("udwt.bin","w");
	fwrite(alt3, sizeof(int), w*h, ofp);
	fclose(ofp);
	
	img = sav_img;
	alt2 = &img[256*256*3];
	alt5 = &img[256*256*6];
	lifting(w,alt2,alt5);
	
	img = sav_img;
	alt2 = &img[256*256*3];
	alt5 = &img[256*256*6];
	ofp = fopen("bdwt.bin","w");
	fwrite(alt2, sizeof(int), w*h, ofp);
	fclose(ofp);

	img = sav_img;
	alt4 = &img[256*256*5];
	alt5 = &img[256*256*6];
	lifting(w,alt4,alt5);

	ofp = fopen("vdwt.bin","w");
	fwrite(alt4, sizeof(int), w*h, ofp);
	fclose(ofp);

	img = sav_img;
	//alt = &img[256*256];
	alt5 = &img[256*256*6];
	lifting(w,img,alt5);

	ofp = fopen("ydwt.bin","w");
	fwrite(img, sizeof(int), w*h, ofp);
	fclose(ofp);
	
	
		
	free (img);	
}
