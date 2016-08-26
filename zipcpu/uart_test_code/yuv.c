
 
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

	
 
	int *img, *alt, *xxx,*sav_img;
     
	img = (int *)malloc(sizeof(int)*(w*h)*2);
    
    
	xxx = img;
	sav_img = img;
	for(index=0; index<h*w; index++) {
		red = ((*buf++)&rr)>>20;
		*img++ = red;
	}
	
	img = sav_img;
   
	/*octave
	fid = fopen('img.bin','r'); im1 = fread(fid, [256,inf], 'int32'); fclose(fid);
	imagesc(im)
	*/


	//ofp = fopen("img.bin","w");
	//fwrite(img, sizeof(int), w*h, ofp);
	//fclose(ofp);    
	alt = &img[256*256];

	//read the Y generatered with openjpeg
	ofp = fopen("c0.bin","r");
	fread(img, sizeof(int), w*h, ofp);
	fclose(ofp);    
	//printf("%d %x, %x %d\n",w,img,alt,sizeof(img)); 
	//int	*img = SDRAM, *alt = &img[256*256];
	//int	done;

	//sys->io_bustimer = 0x7fffffff;
	lifting(w, img, alt);

	/*octave
	fid = fopen('outimg.bin','r'); im2 = fread(fid, [256,inf], 'int32'); fclose(fid);
	imagesc(im)
	*/

	ofp = fopen("c0_3.bin","w");
	fwrite(img, sizeof(int), w*h, ofp);
	fclose(ofp);
	
	//read the U generatered with openjpeg
	
	ofp = fopen("c1.bin","r");
	fread(img, sizeof(int), w*h, ofp);
	fclose(ofp);    
 
	lifting(w, img, alt);
	
	ofp = fopen("c1_3.bin","w");
	fwrite(img, sizeof(int), w*h, ofp);
	fclose(ofp);
	
	//read the V generatered with openjpeg


	ofp = fopen("c2.bin","r");
	fread(img, sizeof(int), w*h, ofp);
	fclose(ofp);    

	lifting(w, img, alt);
	
	ofp = fopen("c2_3.bin","w");
	fwrite(img, sizeof(int), w*h, ofp);
	fclose(ofp);	


 


	free (img);	
}
