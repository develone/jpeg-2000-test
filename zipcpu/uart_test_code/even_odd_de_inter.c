void	singlelift(int rb, int w, int *ibuf, int *obuf) {
	int	col, row;

	for(col=0; col<w; col++) {
		register int	*ip, *op;
		register int	c,e,bp,dp;
		ip = ibuf+col; op = obuf+col;
		// a,b,c,d,e
		// a = a;
		// c = c;
		// b = (b+((a+c+2)>>2));
		// e = e;
		// d = (d+((c+e+2)>>2));

		c  = ip[0];
		dp = ip[1];
		e  = ip[2];
		dp = (dp + ((c+e+2)>>2));

		op[0] = c;
		op[w/2] = dp;

		for(row=1; row<w/2; row++) {
			op+=rb; ip+=2;
			c = e;
			bp = dp;
			dp = ip[1];
			e  = ip[2];
			op[0] = (c+((bp+dp+2)>>2)); // cp
			dp = (dp - ((c+e)>>1));
			op[w/2-1] = bp;
		} op[w-1] = dp;
	}
}

void	lifting(int w, int *ibuf, int *tmpbuf) {
	int	lvl, rb=w;

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
