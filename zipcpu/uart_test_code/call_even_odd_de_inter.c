
 
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

int *sptr, *sptr1, *dptr;

int row,col,cc;
int w,h,r2,r2h,red,green,blue,steps;
w = 256;
h = 256;
int sar[w][h];
int tar[w][h];

sptr = (int *)malloc(sizeof(int)*(w*h));
sptr1 = &sar[0][0]; 
dptr = (int *)malloc(sizeof(int)*(w*h));
//printf("%x %x %x\n",sptr,sptr1,dptr);
cc = 0;

buf = (int *)&xx[0];
//printf("buf %x \n",buf);
for(row=0;row<h;row++)
{
	for(col=0;col<w;col++)
	{
	    //blue = *buf&bb;
	    //sar[row][col] = blue;
	    red = (*buf&rr)>>20;
		sar[row][col] = red;
	    //green = (*buf&gg)>>10;
		//sar[row][col] = green;		
		//*buf = blue;
		//printf("%d ",sar[row][col]);
		//starts at 0 to 15
		buf++;
	}
	//buf = buf + 192;
	//printf(" %x \n",buf);
}
//printf("64 x 64 input data \n");

	
 
    int *img, *alt;
    
    img = (int *)malloc(sizeof(int)*(w*h)*2);
    for(row=0;row<h;row++) {
    for(col=0;col<w;col++) {
		*img++ = sar[row][col];
    }
    }
    img = img - w*h;
    alt = &img[256*256];
    //printf("%d %x, %x %d\n",w,img,alt,sizeof(img)); 
	//int	*img = SDRAM, *alt = &img[256*256];
	//int	done;

	//sys->io_bustimer = 0x7fffffff;
	lifting(w, img, alt);
	//done = 0x7fffffff - sys->io_bustimer;
	//img[0] = done;
	free (sptr);
	free (dptr);
    free (img);	
    }
