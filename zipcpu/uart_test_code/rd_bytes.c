#include <stdio.h>


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
struct rec my_record;
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

for (i= 0;i<65536;i++) {
	val = xx[i];
	red = xx[i]>>20;
	
	val = xx[i];
	gr = xx[i]>>10&0x2ff;
    gr_sh = gr<<10;
	val = xx[i];
	blue = val&0x2ff;
	printf("%d %x packed %x r %x g %x b %x  %x\n",i,i+0x800000,val,red,gr,blue,gr_sh);

}
printf("----------------------------------------\n");
for (i = 2; i<65536;i=i+2) {
	printf("i %d l %x s %x r %x sum_sh %x \n",i,xx[i-1]&bb,xx[i]&bb,xx[i+1]&bb,(((xx[i-1] + xx[i+1]))>>1)&bb);
	printf("i %d l %x s %x r %x sum_sh %x \n",i,xx[i-1]&gg,xx[i]&gg,xx[i+1]&gg,(((xx[i-1] + xx[i+1]))>>1)&gg);
	printf("i %d l %x s %x r %x sum_sh %x \n",i,xx[i-1]&rr,xx[i]&rr,xx[i+1]&rr,(((xx[i-1] + xx[i+1]))>>1)&rr);
	
}
printf("########################################\n");
for (i = 1; i<65536;i=i+2) {
    printf("i %d l %x s %x r %x sum_sh %x \n",i,xx[i-1]&bb,xx[i]&bb,xx[i+1]&bb,(((xx[i-1] + xx[i+1])&bb)+2)>>2);
    printf("i %d l %x s %x r %x sum sh %x \n",i,xx[i-1]&gg,xx[i]&gg,xx[i+1]&gg,(((xx[i-1] + xx[i+1])&gg)+2)>>2);
    printf("i %d l %x s %x r %x sun_sh %x \n",i,xx[i-1]&rr,xx[i]&rr,xx[i+1]&rr,(((xx[i-1] + xx[i+1])&rr)+2)>>2);
}
return 0;   
}
