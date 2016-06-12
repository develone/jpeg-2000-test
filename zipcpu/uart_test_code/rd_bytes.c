#include <stdio.h>

struct results {
	int r_l;
	int g_l;
	int b_l;
	int s_sh_r;
	int s_sh_g;
	int s_sh_b;
	int l;
	int s;
	int r;
	int dwt;
	
};
struct results dwt_process(int *imgbuf) {
    const int bb = 0x3ff;
    const int gg = 0xffc00;
    const int rr = 0xff00000;
    int i;
    struct results a;
    int *buf_l;
    int *buf_r;
    int *buf_s;
    printf("sub ptr to xx %x\n",imgbuf);
    *imgbuf++;
    //setting imgbuf sample minus 1
    buf_l = imgbuf;
    *imgbuf++;
    buf_s = imgbuf;
	*imgbuf++;
	//setting imgbuf sample plus 1
	buf_r = imgbuf;
	//setting imgbuf sample
	 *imgbuf--;
	for(i = 2; i < 16; i=i+2) {
		printf("%d ptr %x %x %x %x %x\n",i,buf_l,*buf_l,*buf_l&rr,*buf_l&gg, *buf_l&bb);
	    printf("%d ptr %x %x %x %x %x\n",i,buf_s,*buf_s,*buf_s&rr,*buf_s&gg, *buf_s&bb);
	    printf("%d ptr %x %x %x %x %x\n",i,buf_r,*buf_r,*buf_r&rr,*buf_r&gg, *buf_r&bb);
 
	    a.l = *buf_l&bb;
	    a.s = *buf_s&bb;
	    a.r = *buf_r&bb;
	    a.dwt = a.s -((a.l+a.r)>>1);
	    printf("l %x s %x r %x dwt %x %x\n",a.l,a.s,a.r,a.dwt,a.dwt&0x1ff);
	    a.l = (*buf_l&gg)>>10;
	    a.s = (*buf_s&gg)>>10;
	    a.r = (*buf_r&gg)>>10;
	    a.dwt = a.s -((a.l+a.r)>>1);
	    printf("l %x s %x r %x dwt %x %x\n",a.l,a.s,a.r,a.dwt,a.dwt&0x1ff);	    
	    a.l = *buf_l>>20;
	    a.s = *buf_s>>20;
	    a.r = *buf_r>>20;
	    a.dwt = a.s -((a.l+a.r)>>1);
	    printf("l %x s %x r %x dwt %x %x\n",a.l,a.s,a.r,a.dwt,a.dwt&0x1ff);
	    //sample - 1
	    //*imgbuf++;
	    buf_l++;
	    buf_s++;
	    buf_r++;
	    //a.r_p = *imgbuf&rr;
	    //a.g_p = *imgbuf&gg;
	    ///a.b_p = *imgbuf&bb;
	    //printf("%d ptr %x %x r %x g %x b %x \n",i,imgbuf,*imgbuf, a.r_p,a.g_p,a.b_p);
 
   }
  
	return a;
}
int main(int argc, char* argv[])
{
struct rec
	{
	char raw_buf[3];
};
const int bb = 0x2ff;
const int gg = 0xffc00;
const int rr = 0xff00000;
char str_buf[1];
int i,val;
int ii0,ii1,ii2;
int *buf;
int xx[65536],red,gr,gr_sh,blue;
buf = &xx;
printf("main ptr to xx %x\n",buf);
struct rec my_record;
struct results my_results;
FILE *ptr_myfile;
ptr_myfile=fopen("rgb.bin","rb");
if (!ptr_myfile)
{
 	printf("Unable to open file!");
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
/*
for (i= 0;i<65536;i++) {
	val = xx[i];
	red = xx[i]>>20;
	
	val = xx[i];
	gr = xx[i]>>10&0x2ff;
    gr_sh = gr<<10;
	val = xx[i];
	blue = val&0x2ff;
	printf("%d %x packed %x r %x g %x b %x  %x\n",i,i+0x800000,val,red,gr,blue,gr_sh);

}*/
buf = &xx;
dwt_process(buf); 
 
return 0;   
}
