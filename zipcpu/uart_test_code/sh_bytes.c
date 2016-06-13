#include <stdio.h>

int twos_comp(int lsr) {
	if (lsr > 256) {
		return lsr - 512;
	}
	else { 
	    return lsr;
    }	
}
void main(void) {
int i;
for (i=1; i<256;i++) {
printf("green\n");
printf("%d 0x%x 0x%x 0x%x \n",-i,-i,twos_comp(-i)&0x1ff,(twos_comp(-i)&0x1ff)<<10);
printf("red\n");
printf("%d 0x%x 0x%x 0x%x \n",-i,-i,twos_comp(-i)&0x1ff,(twos_comp(-i)&0x1ff)<<20);
}
for (i=0; i<256;i++) {
printf("green\n");	
printf("%d 0x%x 0x%x \n",i,i,i<<10);
printf("red\n");
printf("%d 0x%x 0x%x \n",i,i,i<<20);
}


}
