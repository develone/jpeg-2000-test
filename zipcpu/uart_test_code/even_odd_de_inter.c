
#ifdef __ZIPCPU__
void free(void *);
typedef int int32;
#else
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#endif

void	singlelift(int rb, int w, int *ibuf, int *obuf) {
	int	col, row,loop=0;
    printf("sl %d addr %d, %d\n",w,ibuf,obuf);
    for(col=0; col< w; col++) {
		
		ibuf = ibuf + col;
		ibuf = &ibuf[col];
		printf("col %d addr %d \n",col,ibuf);
	for(row=1; row<w-6; row+= 2) {
		register int	*ip, *op,*ip1,*ip2;
		register int	a,c,e,bp,dp,idp;
		ip = ibuf+(row*rb); op = obuf+(row*rb);
 
		// dp = (dp - ((c+e)>>1));

		c  = ip[0]; 	//1 3 5 ... 245 247 249
		dp = ip[256];	//2 4 6 ... 246 248 250
		e  = ip[512];	//3 5 7 ... 247 249 251
		printf("row  %d (row-1) %d sam %d  (row+1) %d \n", row, c,dp,e);
		dp = (dp - ((c+e)>>1));
		printf("row %d addr (row-1) %d addr sam %d addr (row+1) %d even lift %d %d\n",row,&ip[0],&ip[256],&ip[512],dp,loop);
		ip[256] = dp;
		printf("row %d addr ibuf %d %d \n",row,&ip[256],ip[256]);
		// bp = (bp+((a+c+2)>>2));
		a = ip[-256];	//0 2 4 ... 244 246 248
		bp = ip[0];		//1 3 5 ... 245 247 249
		c = ip[256];	//2 4 6 ... 246 248 250 
        printf("row %d (row-1) %d sam %d (row+1) %d \n", row, a,bp,c);
        bp = (bp + ((a + c + 2 )>>2));
        printf("row %d addr (row-1) %d addr sam %d addr (row+1) %d  odd lift %d %d\n",row,&ip[-256],&ip[0],&ip[256],bp,loop);
		//op[0] = c;
		ip[-256] = bp;
		printf("row %d addr ibuf %d %d \n",row,&ip[-256],ip[-256]);
		loop++;
 
	}
	}
}

void	lifting(int w, int *ibuf, int *tmpbuf) {
	int	lvl, rb=w;
	//printf("%d %d, %d\n",w,ibuf,tmpbuf);
	for(lvl=0; lvl<3; lvl++) {
		// Process columns -- leave result in tmpbuf
		singlelift(rb, w, ibuf, tmpbuf);
		singlelift(rb, w, tmpbuf, ibuf);

		// lower_upper
		int	offset = w*rb/2+w/2;
		ibuf = &ibuf[offset];
		tmpbuf = &tmpbuf[offset];

		// Move to the corner, and repeat
		w>>=1;
	}
}
