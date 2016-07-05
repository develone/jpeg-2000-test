#include "board.h"
#include "lx9.h"

asm("\t.section\t.start\n"
        "\t.global\t_start\n"
        "\t.type\t_start,@function\n"
        "_start:\n"
        "\tLDI\t_top_of_stack,SP\n"
        "\tBRA\tentry\n"
        "\t.section\t.text");

void	lifting(int w, int *ibuf, int *tmpbuf);

void	entry(void) {
	int	*img = SDRAM, *alt = &img[256*257];
	int	done;

	sys->io_bustimer = 0x7fffffff;
	lifting(256, img, alt);
	done = 0x7fffffff - sys->io_bustimer;
	img[0] = done;
	zip_halt();
}

__attribute__((noinline))
void	singlelift(int rb, int w, int * const ibuf, int * const obuf) {
	int	col, row;

	for(row=0; row<w; row++) {
		register int	*ip, *op, *opb;
		register int	c,e,bp,dp;

		//
		// Ibuf walks down rows (here), but reads across columns (below)
		// We might manage to get rid of the multiply by doing something
		// like: 
		//	ip = ip + (rb-w);
		// but we'll keep it this way for now.
		//
		ip = ibuf+row*rb;

		//
		// Obuf walks across columns (here), writing down rows (below)
		//
		// Here again, we might be able to get rid of the multiply,
		// but let's get some confidence as written first.
		//
		opb = obuf+row;
		op = opb + w*rb/2;

		//
		// Pre-charge our pipeline
		//

		// a,b,c,d,e
		// a = a;
		// c = c;
		// b = (b+((a+c+2)>>2));
		// e = e;
		// d = (d+((c+e+2)>>2));

		// Put these three together so that they can get some
		// potential pipeline savings.  (Sadly, looking at the 
		// assembly, these could be pipelined, just the compiler
		// didn't -- so there's some benefit to be had here.)
		c  = ip[0];
		dp = ip[1];
		e  = ip[2];
		dp = (dp + ((c+e+2)>>2));

		op[0]  = c;
		opb[0] = dp;

		for(col=1; col<w/2; col++) {
			op +=rb; // = obuf+row+rb*col = obuf[col][row]
			opb+=rb;// = obuf+row+rb*(col+w/2) = obuf[col+w/2][row]
			ip+=2;	// = ibuf + (row*rb)+2*col
			c = e;
			bp = dp;
			dp = ip[1];	// = ip[row][2*col+1]
			e  = ip[2];	// = ip[row][2*col+2]
			*op  = (c+((bp+dp+2)>>2)); //op[0] is obuf[col][row]
			dp = (dp - ((c+e)>>1));
			*opb = bp;	// opb[0] is obuf[col+w/2][row-1]
		} op[w-1] = dp;
	}
}

void	lifting(int w, int *ibuf, int *tmpbuf) {
	const	int	rb = w;
	int	lvl;

	for(lvl=0; lvl<3; lvl++) {
		// Process columns -- leave result in tmpbuf
		singlelift(rb, w, ibuf, tmpbuf);
		// Process columns, what used to be the rows from the last
		// round, pulling the data from tmpbuf and moving it back
		// to ibuf.
		singlelift(rb, w, tmpbuf, ibuf);

		// lower_upper
		//
		// For this, we just adjust our pointer(s) so that the "image"
		// we are processing, as referenced by our two pointers, now
		// references the bottom right part of the image.
		//
		// Of course, we haven't really changed the dimensions of the
		// image.  It started out rb * rb in size, or the initial w*w,
		// we're just changing where our pointer into the image is.
		// Rows remain rb long.  We pretend (above) that this new image
		// is w*w, or should I say (w/2)*(w/2), but really we're just
		// picking a new starting coordinate and it remains rb*rb.
		//
		// Still, this makes a subimage, within our image, containing
		// the low order results of our processing.
		int	offset = w*rb/2+w/2;
		ibuf = &ibuf[offset];
		tmpbuf = &tmpbuf[offset];

		// Move to the corner, and repeat
		w>>=1;
	}
}

