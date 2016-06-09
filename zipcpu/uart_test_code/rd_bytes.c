#include <stdio.h>


int main(int argc, char* argv[])
{
struct rec
	{
	char raw_buf[3];
};
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
return 0;   
}
