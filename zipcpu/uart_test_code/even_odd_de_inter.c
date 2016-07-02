#include<stdio.h>


void	singlelift(int rb, int w, int *ibuf, int *obuf) {
	int	col, row,loop=0;
    printf("%d %x, %x\n",w,ibuf,obuf);
	for(row=0; row<rb*w; row+=rb) {
		register int	*ip, *op,*ip1,*ip2;
		register int	c,e,bp,dp;
		ip = ibuf+rb+row; op = obuf+rb+row;
		ip1 = ibuf+rb*2+row;
		ip2 = ibuf+rb*3+row;
		// a,b,c,d,e
		// a = a;
		// c = c;
		// b = (b+((a+c+2)>>2));
		// e = e;
		// d = (d+((c+e+2)>>2));

		c  = ip[0];
		dp = ip1[0];
		e  = ip2[0];
		printf("row %d %x, %x %x, %d %d %d %d\n",row,&ip[0],&ip1[0],&ip2[0],(ip-ibuf),(ip1-ibuf),(ip2-ibuf),loop);
		dp = (dp - ((c+e)>>1));

		op[0] = c;
		op[w/2] = dp;
		printf("row %d %x \n",row,&op[w/2]);
		loop++;
/*
		for(col=0; col<w/2; col++) {
			op+=rb; ip+=2;
			c = e;
			bp = dp;
			dp = ip[1];
			e  = ip[2];
			printf("col %d %x, %x %x\n",col,&ip[0],&ip[1],&ip[2]);
			op[0] = (c+((bp+dp+2)>>2)); // cp
			dp = (dp - ((c+e)>>1));
			op[w/2-1] = bp;
		} op[w-1] = dp;*/
	}
}

void	lifting(int w, int *ibuf, int *tmpbuf) {
	int	lvl, rb=w;
	//printf("%d %x, %x\n",w,ibuf,tmpbuf);
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
