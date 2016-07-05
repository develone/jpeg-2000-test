
 
#ifdef __ZIPCPU__
void free(void *);
typedef int int32;
#else
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#endif
int main(void) {
	
	const int bb = 0x1ff;
    const int gg = 0x7fc00;
    const int rr = 0x1ff00000;
//read RGB data from file 
int index; 	
int i,ii0,ii1,ii2,val;
int *buf;
int xx[65536];
buf = (int *)&xx[0];	
struct rec
	{
	char raw_buf[3];
};
struct rec my_record;
//struct results my_results;
FILE *ptr_myfile;
ptr_myfile=fopen("rgb.bin","rb");
if (!ptr_myfile)
{
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

	
 
    int *img, *alt, *xxx;
    
    img = (int *)malloc(sizeof(int)*(w*h)*2);
    xxx = img;
	for(index=0; index<h*w; index++) {
		red = ((*buf++)&rr)>>20;
		*img++ = red;
	}
    img = xxx;
    alt = &img[256*256];
    //printf("%d %x, %x %d\n",w,img,alt,sizeof(img)); 
	//int	*img = SDRAM, *alt = &img[256*256];
	//int	done;

	//sys->io_bustimer = 0x7fffffff;
	lifting(w, img, alt);
	xxx = xxx + 57568;
	for (row= 0 ;row<32;row++) {
		for(col=0;col< 32;col++) {
			printf("%d ",*xxx++);
		}
		printf("\n");
	}
	 
	//done = 0x7fffffff - sys->io_bustimer;
	//img[0] = done;
 
	
    free (img);	
    }
