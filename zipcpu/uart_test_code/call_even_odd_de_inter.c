
 
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


	ofp = fopen("img.bin","w");
	fwrite(img, sizeof(int), w*h, ofp);
	fclose(ofp);    
	alt = &img[256*256];

	//printf("%d %x, %x %d\n",w,img,alt,sizeof(img)); 
	//int	*img = SDRAM, *alt = &img[256*256];
	//int	done;

	//sys->io_bustimer = 0x7fffffff;
	lifting(w, img, alt);

	/*octave
	fid = fopen('outimg.bin','r'); im2 = fread(fid, [256,inf], 'int32'); fclose(fid);
	imagesc(im)
	*/

	ofp = fopen("outimg.bin","w");
	fwrite(img, sizeof(int), w*h, ofp);
	fclose(ofp);

	//./build_call_even.sh
	//./call_even_odd_de_inter > xx.txt
	//in octave load dispdwt.m or inv1lvl.m
	//dispdwt or inv1lvl
	//lines 115-130 are only to dump to file xx.txt to see what the input
	//values are being used 	
	//32768 is the lower half of 256 x 256 image
	//32896 is on the row 0 col 0 
	//of 128 x 128 in lower right hand corner.
	//In the col loop the last thing done is ip1+=1
	//ip1 is increased by 256 every time int the row loop
	//ip1 is ip + 0
	//ip1 is ip + 256
	//ip1 is ip + 512
	//ip1 is ip + 768
	//****************************************************************
	int *ip,*ip1,yy[128][128];
 

//
// Magic numbers, such as 32896, are a violation of good programming practice.
// Isn't there some other way you can note this?  Something that makes more
// sense, and yet will be more maintainable in the future?
//
// 
	ip = img+32896; //this is the offset that is will be passed
	w = 128;  //width of 1 lvl dwt
	for (row= 0 ;row<w;row++) {
		ip1 = ip + row*256;
		for(col=0;col< w;col++) {
			printf("%d ",ip1[0]);
			yy[row][col] = ip1[0];
			ip1+=1;           
		}
		printf("\n");      
	}
	ofp = fopen("testimg.bin","w");
	fwrite(&yy, sizeof(int), 128*128, ofp);
	fclose(ofp);
	//****************************************************************
	
	w = 128;
	//lvl1 32896 lvl2 49344 lvl3 57568
	//int offset = 32896;
	int offset = 32896;
	pointer_inv_de_interleave(w, offset, img, alt);
	w = 256;
	invlifting(w, alt,img);

	ofp = fopen("invdwt.bin","w");
	fwrite(img, sizeof(int), 65536, ofp);
	fclose(ofp);

	ofp = fopen("imgdwt2.bin","w");
	fwrite(img, sizeof(int), 65536, ofp);
	fclose(ofp);

	free (img);	
}
