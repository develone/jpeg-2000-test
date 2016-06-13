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
	int dwt_b;
	int dwt_g;
	int dwt_r;
	
};
union Data {
	int xx[65536];
	char yy[65536]; 
}data;
int twos_comp(int lsr) {
	if (lsr > 256) {
		return lsr - 512;
	}
	else { 
	    return lsr;
    }	
}
struct results dwt_process(int *imgbuf) {
    const int bb = 0x3ff;
    const int gg = 0xffc00;
    const int rr = 0x3ff00000;
    int i,val;
    struct results a;
    int *buf_l;
    int *buf_r;
    int *buf_s;
    printf("sub ptr to xx %x\n",imgbuf);
    *imgbuf++;
    //setting imgbuf sample minus 1
    buf_l = imgbuf;
    *imgbuf++;
    //setting imgbuf sample even
    buf_s = imgbuf;
	*imgbuf++;
	//setting imgbuf sample plus 1
	buf_r = imgbuf;	
	//setting imgbuf sample even
	*imgbuf++;
	for(i = 2; i < 10; i=i+2) {
		printf("%d ptr %x %x %x %x %x\n",i-1,buf_l,*buf_l,*buf_l&rr,*buf_l&gg, *buf_l&bb);
	    printf("%d ptr %x %x %x %x %x\n",i,buf_s,*buf_s,*buf_s&rr,*buf_s&gg, *buf_s&bb);
	    printf("%d ptr %x %x %x %x %x\n",i+1,buf_r,*buf_r,*buf_r&rr,*buf_r&gg, *buf_r&bb);
	    
	    a.l = *buf_l>>20;
	    a.s = *buf_s>>20;
	    a.r = *buf_r>>20;
	    a.l = twos_comp(a.l);
	    a.s = twos_comp(a.s);
	    a.r = twos_comp(a.r);	    
	    a.dwt_r = a.s -((a.l+a.r)>>1);
	    val |= a.dwt_r<<20;
	    printf("%d l %x s %x r %x dwt %x %x\n",i,a.l,a.s,a.r,a.dwt_r,a.dwt_r&0x1ff);
        a.dwt_r = twos_comp(a.dwt_r&0x1ff);
        printf("%x %d\n",a.dwt_r,a.dwt_r); 
        
	    a.l = (*buf_l&gg)>>10;
	    a.s = (*buf_s&gg)>>10;
	    a.r = (*buf_r&gg)>>10;
	    a.l = twos_comp(a.l);
	    a.s = twos_comp(a.s);
	    a.r = twos_comp(a.r);	    
	    a.dwt_g = a.s -((a.l+a.r)>>1);
	    a.dwt_g = a.dwt_g&0x1ff;
	    val |= a.dwt_g<<10;
	    printf("%d l %x s %x r %x dwt %x %x\n",i, a.l,a.s,a.r,a.dwt_g,a.dwt_g&0x1ff);
        a.dwt_g = twos_comp(a.dwt_g&0x1ff);
	    printf("%x %d\n",a.dwt_g,a.dwt_g);        
	     
	    a.l = *buf_l&bb;
	    a.s = *buf_s&bb;
	    a.r = *buf_r&bb;
	    a.l = twos_comp(a.l);
	    a.s = twos_comp(a.s);
	    a.r = twos_comp(a.r);
	    a.dwt_b = a.s -((a.l+a.r)>>1);
	    
	    val |= a.dwt_b&0x1ff; 
	    printf("%d l %x s %x r %x dwt %x %x\n",i, a.l,a.s,a.r,a.dwt_b,a.dwt_b&0x1ff);
	    a.dwt_b = twos_comp(a.dwt_b&0x1ff);
	    printf("%x %d\n",a.dwt_b,a.dwt_b);

        *buf_s = val;
        printf("%d ptr %x %x %x %x %x\n",i,buf_s,*buf_s,*buf_s&rr,*buf_s&gg, *buf_s&bb);
	    //printf("%d ptr %x %x %x %x %x %x\n",i,buf_s,*buf_s,*buf_s&rr,*buf_s&gg, *buf_s&bb,val);
	    printf("\n");
	    	        
	    buf_l++;
	    buf_s++;
	    buf_r++;
   }
   
    printf("sub ptr to xx %x\n",imgbuf);
    //
    *imgbuf--; //setting imgbuf sample minus 1
    buf_l = imgbuf;
    *imgbuf++;
    //setting imgbuf sample odd
    buf_s = imgbuf;
	*imgbuf++;
	//setting imgbuf sample plus 1
	buf_r = imgbuf;
	//setting imgbuf sample odd
	 *imgbuf--;
	for(i = 1; i < 11; i=i+2) {
		printf("%d ptr %x %x %x %x %x\n",i-1,buf_l,*buf_l,*buf_l&rr,*buf_l&gg, *buf_l&bb);
	    printf("%d ptr %x %x %x %x %x\n",i,buf_s,*buf_s,*buf_s&rr,*buf_s&gg, *buf_s&bb);
	    printf("%d ptr %x %x %x %x %x\n",i+1,buf_r,*buf_r,*buf_r&rr,*buf_r&gg, *buf_r&bb);
	    
	    a.l = *buf_l>>20;
	    a.s = *buf_s>>20;
	    a.r = *buf_r>>20;
	    a.l = twos_comp(a.l);
	    a.s = twos_comp(a.s);
	    a.r = twos_comp(a.r);	    
	    a.dwt_r = a.s -((a.l+a.r)>>1);
	    val |= a.dwt_r<<20;
	    printf("%d l %x s %x r %x dwt %x %x\n",i,a.l,a.s,a.r,a.dwt_r,a.dwt_r&0x1ff);
        a.dwt_r = twos_comp(a.dwt_r&0x1ff);
        printf("%x %d\n",a.dwt_r,a.dwt_r); 
        
	    a.l = (*buf_l&gg)>>10;
	    a.s = (*buf_s&gg)>>10;
	    a.r = (*buf_r&gg)>>10;
	    a.l = twos_comp(a.l);
	    a.s = twos_comp(a.s);
	    a.r = twos_comp(a.r);	    
	    a.dwt_g = a.s -((a.l+a.r)>>1);
	    a.dwt_g = a.dwt_g&0x1ff;
	    val |= a.dwt_g<<10;
	    printf("%d l %x s %x r %x dwt %x %x\n",i, a.l,a.s,a.r,a.dwt_g,a.dwt_g&0x1ff);
        a.dwt_g = twos_comp(a.dwt_g&0x1ff);
	    printf("%x %d\n",a.dwt_g,a.dwt_g);        
	     
	    a.l = *buf_l&bb;
	    a.s = *buf_s&bb;
	    a.r = *buf_r&bb;
	    a.l = twos_comp(a.l);
	    a.s = twos_comp(a.s);
	    a.r = twos_comp(a.r);
	    a.dwt_b = a.s -((a.l+a.r)>>1);
	    
	    val |= a.dwt_b&0x1ff; 
	    printf("%d l %x s %x r %x dwt %x %x\n",i, a.l,a.s,a.r,a.dwt_b,a.dwt_b&0x1ff);
	    a.dwt_b = twos_comp(a.dwt_b&0x1ff);
	    printf("%x %d\n",a.dwt_b,a.dwt_b);

        *buf_s = val;
        printf("%d ptr %x %x %x %x %x\n",i,buf_s,*buf_s,*buf_s&rr,*buf_s&gg, *buf_s&bb);
	    //printf("%d ptr %x %x %x %x %x %x\n",i,buf_s,*buf_s,*buf_s&rr,*buf_s&gg, *buf_s&bb,val);
	    printf("\n");
	    	        
	    buf_l++;
	    buf_s++;
	    buf_r++;
   }
   
	return a;
}
int main(int argc, char* argv[])
{
struct rec
	{
	char raw_buf[3];
};
union Data data;
const int bb = 0x2ff;
const int gg = 0xffc00;
const int rr = 0xff00000;
char str_buf[1];
int i,val;
int ii0,ii1,ii2;
int *buf;
//int xx[65536];
int red,gr,gr_sh,blue;
buf = &data.xx;
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
printf("data.xx %d data.yy %d \n",sizeof(data.xx),sizeof(data.yy));
printf("data.xx %x data.yy %x \n",&(data.xx),&(data.yy));
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

for (i= 0;i<65536;i++) {
	val = data.xx[i];
	red = data.xx[i]>>20;
	
	val = data.xx[i];
	gr = data.xx[i]>>10&0x2ff;
    gr_sh = gr<<10;
	val = data.xx[i];
	blue = val&0x2ff;
	printf("%d %x packed %x r %x g %x b %x  %x\n",i,i+0x800000,val,red,gr,blue,gr_sh);

}
buf = &data.xx;
dwt_process(buf); 
 
return 0;   
}
