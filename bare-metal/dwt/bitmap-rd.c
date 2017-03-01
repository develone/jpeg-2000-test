/* http://www.instesre.org/howto/BW_image/ReadingBitmaps.htm
 * read header */
#include <stdio.h>
#include <sys/time.h>
#include "lifting.h"
#include "dwtlift.h"
#include <stdlib.h>

extern void lift_config(int dec, int enc, int mct, int bp, long imgsz,int *bufferptr);
//extern void yuv(int w,int *r,int *g,int *b,int *u,int *v,int *y);
//extern void invyuv(int w,int *r,int *g,int *b,int *u,int *v,int *y);
////////////////////////////////////////////////////////////////////////////////
//
// Filename: 	lifting.c
//
// Project:	XuLA2-LX25 SoC based upon the ZipCPU
//
// Purpose:	This goal of this file is to perform, on either the ZipCPU or
//		a more traditional architecture, the lifting/WVT step of the
//	JPEG-2000 compression (and decompression) scheme.
//
//	Currently, the lifting scheme performs both forward and inverse 
//	transforms, and so (if done properly) it constitutes an identity
//	transformation.
//
// Creator:	Dan Gisselquist, Ph.D.
//		Gisselquist Technology, LLC
//
////////////////////////////////////////////////////////////////////////////////
//
// Copyright (C) 2015-2016, Gisselquist Technology, LLC
//
// This program is free software (firmware): you can redistribute it and/or
// modify it under the terms of  the GNU General Public License as published
// by the Free Software Foundation, either version 3 of the License, or (at
// your option) any later version.
//
// This program is distributed in the hope that it will be useful, but WITHOUT
// ANY WARRANTY; without even the implied warranty of MERCHANTIBILITY or
// FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
// for more details.
//
// You should have received a copy of the GNU General Public License along
// with this program.  (It's in the $(ROOT)/doc directory, run make with no
// target there if the PDF file isn't present.)  If not, see
// <http://www.gnu.org/licenses/> for a copy.
//
// License:	GPL, v3, as defined and found on www.gnu.org,
//		http://www.gnu.org/licenses/gpl.html
//
//
////////////////////////////////////////////////////////////////////////////////
//
//

void	singlelift(int rb, int w, int * const ibuf, int * const obuf) {
	int	col, row;

	for(row=0; row<w; row++) {
		register int	*ip, *op, *opb;
		register int	ap,b,cp,d;

		//
		// Ibuf walks down rows (here), but reads across columns (below)
		// We might manage to get rid of the multiply by doing something
		// like: 
		//	ip = ip + (rb-w);
		// but we'll keep it this way for now.
		//
		//setting to beginning of each row
		ip = ibuf+row*rb;

		//
		// Obuf walks across columns (here), writing down rows (below)
		//
		// Here again, we might be able to get rid of the multiply,
		// but let's get some confidence as written first.
		//
		op = obuf+row;
		opb = op + w*rb/2;

		//
		// Pre-charge our pipeline
		//

		// a,b,c,d,e ...
		// Evens get updated first, via the highpass filter
		ap = ip[0];
		b  = ip[1];
		cp = ip[2];
		d  = ip[3]; ip += 4;
		//
		ap = ap-b; // img[0]-(img[1]+img[-1])>>1)
		cp = cp- ((b+d)>>1);
		 
		op[0] = ap;
		opb[0]  = b+((ap+cp+2)>>2);

		for(col=1; col<w/2-1; col++) {
			op +=rb; // = obuf+row+rb*col = obuf[col][row]
			opb+=rb;// = obuf+row+rb*(col+w/2) = obuf[col+w/2][row]
			ap = cp;
			b  = d;
			cp = ip[0];	// = ip[row][2*col+1]
			d  = ip[1];	// = ip[row][2*col+2]

			//HP filter in fwd dwt			
			cp  = (cp-((b+d)>>1)); //op[0] is obuf[col][row]
			*op = ap; //op[0] is obuf[col][row]
			 
			//LP filter in fwd dwt
			*opb = b+((ap+cp+2)>>2);
			ip+=2;	// = ibuf + (row*rb)+2*col
		}

		op += rb; opb += rb;
		*op  = cp;
		*opb = d+((cp+1)>>3);
	}
}

void	ilift(int rb, int w, int * const ibuf, int * const obuf) {
	int	col, row;

	for(row=0; row<w; row++) {
		register int	*ip, *ipb, *op;
		register int	b,c,d,e;

		//
		// Ibuf walks down rows (here), but reads across columns (below)
		// We might manage to get rid of the multiply by doing something
		// like: 
		//	ip = ip + (rb-w);
		// but we'll keep it this way for now.
		//
		//setting to beginning of each row
		op = obuf+row*rb;

		//
		// Obuf walks across columns (here), writing down rows (below)
		//
		// Here again, we might be able to get rid of the multiply,
		// but let's get some confidence as written first.
		//
		ip  = ibuf+row;
		ipb = ip + w*rb/2;

		//
		// Pre-charge our pipeline
		//

		// a,b,c,d,e ...
		// Evens get updated first, via the highpass filter
		c = ip[0]; // would've been called 'a'
		ip += rb;
		e = ip[0];	// Would've been called 'c'
		d  = ipb[0] -((c+e+2)>>2);

		op[0] = c+d;	// Here's the mirror, left-side
		op[1] = d;

		for(col=1; col<w/2-1; col++) {
			op += 2;
			ip += rb; ipb += rb;

			c = e; b = d;
			e = ip[0];
			d = ipb[0] - ((c+e+2)>>2);
			c = c + ((b+d)>>1);

			op[0] = c;
			op[1] = d;
		}

		ipb += rb;
		d = ipb[0] - ((e+1)>>3);

		c = e + ((b+d)>>1);
		op[2] = c;
		op[3] = d;	// Mirror
	}
}

void	lifting(int w, int *ibuf, int *tmpbuf, int decomp) {
	const	int	rb = w;
	int	lvl, LVLS = decomp;

	int	*ip = ibuf, *tp = tmpbuf;
	int	ov[5];

	for(lvl=0; lvl<LVLS; lvl++) {
		// Process columns -- leave result in tmpbuf
		singlelift(rb, w, ip, tp);
		// Process columns, what used to be the rows from the last
		// round, pulling the data from tmpbuf and moving it back
		// to ibuf.
		singlelift(rb, w, tp, ip);

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
		ip = &ip[offset];
		tp = &tp[offset];
		ov[lvl] = offset + ((lvl)?(ov[lvl-1]):0);

		// Move to the corner, and repeat
		w>>=1;
	}
 
}

void	dosinglelift(int rb, int w, int * const ibuf, int * const obuf) {
	int	col, row;

	for(row=0; row<w; row++) {
		register int	*ip, *op, *opb;
		register int	ap,b,cp,d;

		//
		// Ibuf walks down rows (here), but reads across columns (below)
		// We might manage to get rid of the multiply by doing something
		// like: 
		//	ip = ip + (rb-w);
		// but we'll keep it this way for now.
		//
		//setting to beginning of each row
		ip = ibuf+row*rb;

		//
		// Obuf walks across columns (here), writing down rows (below)
		//
		// Here again, we might be able to get rid of the multiply,
		// but let's get some confidence as written first.
		//
		op = obuf+row;
		opb = op + w*rb/2;

		//
		// Pre-charge our pipeline
		//

		// a,b,c,d,e ...
		// Evens get updated first, via the highpass filter
		ap = ip[0];
		b  = ip[1];
		cp = ip[2];
		d  = ip[3]; ip += 4;
		//
		ap = ap-b; // img[0]-(img[1]+img[-1])>>1)
		cp = cp- ((b+d)>>1);
		 
		op[0] = ap;
		opb[0]  = b+((ap+cp+2)>>2);

		for(col=1; col<w/2-1; col++) {
			op +=rb; // = obuf+row+rb*col = obuf[col][row]
			opb+=rb;// = obuf+row+rb*(col+w/2) = obuf[col+w/2][row]
			ap = cp;
			b  = d;
			cp = ip[0];	// = ip[row][2*col+1]
			d  = ip[1];	// = ip[row][2*col+2]

			//HP filter in fwd dwt			
			cp  = (cp-((b+d)>>1)); //op[0] is obuf[col][row]
			*op = ap; //op[0] is obuf[col][row]
			 
			//LP filter in fwd dwt
			*opb = b+((ap+cp+2)>>2);
			ip+=2;	// = ibuf + (row*rb)+2*col
		}

		op += rb; opb += rb;
		*op  = cp;
		*opb = d+((cp+1)>>3);
	}
}


void	invlifting(int w, int *ibuf, int *tmpbuf, int decomp) {
	const	int	rb = w;
	int	lvl, LVLS = decomp;

	int	*ip = ibuf, *tp = tmpbuf;
	int	ov[5];

	for(lvl=0; lvl<LVLS; lvl++) {
		// Process columns -- leave result in tmpbuf
		dosinglelift(rb, w, ip, tp);
		
		// Process columns, what used to be the rows from the last
		// round, pulling the data from tmpbuf and moving it back
		// to ibuf.
		
		dosinglelift(rb, w, tp, ip);

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
		ip = &ip[offset];
		tp = &tp[offset];
		ov[lvl] = offset + ((lvl)?(ov[lvl-1]):0);

		// Move to the corner, and repeat
		w>>=1;
	}
    	
	for(lvl=(LVLS-1); lvl>=0; lvl--) {
		int	offset;

		w <<= 1;

		if (lvl)
			offset = ov[lvl-1];
		else
			offset = 0;
		ip = &ibuf[offset];
		tp = &tmpbuf[offset];

		ilift(rb, w, ip, tp);
		ilift(rb, w, tp, ip);
	}
	
}

int main(int argc, char **argv) {
struct rec {
	unsigned char header[14];	
};
struct rec1 {
	unsigned char imginfo[40];	
};

FILE *in,*fp;
char *fn;

char inchar;
int bpp;
long int offset,width,height;
int pixels, size, sz;
int *databuffer;
int plot=1;
	encode = 1;
	decomp = 3;
	flgyuv = 1;
	printf("enc %d decomp %d yuv %d\n",encode,decomp,flgyuv);

	fn = argv[1];
/*
Section	Description
Header	Basic file information, 14 bytes
Image Information Header	Information about the image, 40 bytes
Color Information (optional)	Information about how the image encodes colors, a variable number of bytes if it's present
Image data	The actual image, a variable number of bytes
*/
/*
 * 0  1  2   3 4  5 6 7 8 9 a   b c d
 * 66 77 122 0 48 0 0 0 0 0 122 0 0 0
 * 
 *                                    1                                    2 
 * 0   1 2 3 4 5 6 7 8 9 a b c d e  f 0 1 2 3 4 5 6  7 8  9  a b c  d  e f 0 1 2 3 4 5 6 7
 * 108 0 0 0 0 4 0 0 0 4 0 0 1 0 24 0 0 0 0 0 0 0 48 0 19 11 0 0 19 11 0 0 0 0 0 0 0 0 0 0
 */
 /*
  * Header size, bytes (should be 40)	4 bytes
  * Image width, pixels	4 bytes
  * Image height, pixels	4 bytes
  * Number of color planes	2 bytes
  * Bits per pixel, 1 to 24	2 bytes
  * Compression, bytes (assumed 0)	4 bytes
  * Image size, bytes	4 bytes
  * X-resolution and y-resolution, pixels per meter	4 bytes each
  * Number of colors and "important colors," bytes	4 bytes each
  * 3145850
  * 14 40 54
  * 3145728
  * 68
  */
	struct rec record;
	struct rec1 record1;
 
	in = fopen(fn,"rb");
	
	
	if (!in) {
 		printf("Unle to open file!");
		return 1;
	}
	
	/* read header */
	 
	fread(&record,sizeof(struct rec),1,in);
	loop = 0;	
	while(loop<14) {
		printf("%i ",record.header[loop]);
		loop++;
	}
	 
	
	printf("\n");
	//xx1 = (long)record.header[4];
	printf("file size = %li\n",(long)record.header[4]*65536+(long)record.header[3]*256+(long)record.header[2]);
	offset = (long)record.header[11]*256+(long)record.header[10];
	printf("offset to image = %i\n",offset);
	
	/* Image Information Header */
	fread(&record1,sizeof(struct rec1),1,in);
	loop = 0;
	while(loop<40) {
		printf("%i ",record1.imginfo[loop]);
		loop++;
	}
		
	width = (long)record1.imginfo[5]*256+(long)record1.imginfo[4];
	height = (long)record1.imginfo[9]*256+(long)record1.imginfo[8];
	printf("\n");
	printf("width = %i height = %i\n",width,height);
	bpp = record1.imginfo[14];
	printf("\n");
	printf("bits per pixel = %i\n",bpp);
	pixels = width * height;
	size = pixels*3;
	printf("pixels = %d size = %d \n",pixels,size);
	char data[size];
	
	databuffer = (int*)(&data[0]);
	char *lclip;
	printf("databuffer address 0x%x data address 0x%x  \n",databuffer,&data[0]);
	
	for(loop=0; loop<(offset-54); loop++) {
		fread(&inchar,sizeof(inchar),1,in);
		 
		//printf("%c ",inchar);
	}
	fread(&data[0],sizeof(data),1,in);
	
	gettimeofday(&start, NULL);
	
	IMAGEP		imgbm;
	ww = width;
	hh = height;
	sz = ww*hh;
	imgbm = (IMAGEP)malloc(sizeof(IMAGE)+7*ww*hh*sizeof(int));
	y = &imgbm->data[4*ww*hh];
	u = &imgbm->data[5*ww*hh];
	v = &imgbm->data[6*ww*hh];
	imgbm->m_w = ww;
	imgbm->m_h = hh;
	imgbm->m_red   = imgbm->data;
	imgbm->m_green = &imgbm->data[ww*hh];
	imgbm->m_blue  = &imgbm->data[2*ww*hh];
	imgbm->m_tmp  = &imgbm->data[3*ww*hh];
	printf("Copying RGB 8 bit char to 32 int \n");
	printf("splitting data to rgb\n");
	lclip = &data[0];	
	for (loop=0; loop < size/3; loop++) {
		*imgbm->m_red = lclip[0];
		lclip++;
		imgbm->m_red++;
		*imgbm->m_green = lclip[0];
		lclip++;
		imgbm->m_green++;
		*imgbm->m_blue = lclip[0];
		lclip++;
		imgbm->m_blue++;
	}
	imgbm->m_red   = imgbm->data;
	imgbm->m_green = &imgbm->data[ww*hh];
	imgbm->m_blue  = &imgbm->data[2*ww*hh];
 
	printf("splitting data to rgb done \n");
	yuv(ww, imgbm->m_red, imgbm->m_green, imgbm->m_blue, u, v, y);
				printf("Calling lifting y\n");
				lifting(ww, y, imgbm->m_tmp, decomp);
				
				printf("Calling lifting u\n");
				lifting(ww, u, imgbm->m_tmp, decomp); 
				printf("Calling lifting v\n");
				lifting(ww, v, imgbm->m_tmp,decomp);
				printf("lifting to Buffer\n");	
				quantize(ww,y,u,v);
				quantize(ww,y,u,v);
	gettimeofday(&end, NULL);
 
	seconds  = end.tv_sec  - start.tv_sec;
	useconds = end.tv_usec - start.tv_usec;
 
	mtime = seconds + useconds;
 
	printf("Elapsed time: %ld microseconds\n", mtime);
	if(plot == 1) {
	fp = fopen("red-out.32t","w");
	if (NULL == fp) {
		fprintf(stderr, "Could not open red for writing\n");
		perror("RED-WR:");
		exit(EXIT_FAILURE);
	}
		 
	if (sz != (int)fwrite(imgbm->m_red,  sizeof(int), sz, fp)) {
		fprintf(stderr, "Write of red failed\n"); perror("RED:");
		exit(EXIT_FAILURE);
	}
	fclose(fp);

	fp = fopen("grn-out.32t","w");
	if (NULL == fp) {
		fprintf(stderr, "Could not open red for writing\n");
		perror("RED-WR:");
		exit(EXIT_FAILURE);
	}
		 
	if (sz != (int)fwrite(imgbm->m_green,  sizeof(int), sz, fp)) {
		fprintf(stderr, "Write of green failed\n"); perror("GREEN:");
		exit(EXIT_FAILURE);
	}
	fclose(fp);
	
	fp = fopen("blu-out.32t","w");
	if (NULL == fp) {
		fprintf(stderr, "Could not open red for writing\n");
		perror("RED-WR:");
		exit(EXIT_FAILURE);
	}
		 
	if (sz != (int)fwrite(imgbm->m_blue,  sizeof(int), sz, fp)) {
		fprintf(stderr, "Write of green failed\n"); perror("BLUE:");
		exit(EXIT_FAILURE);
	}
	fclose(fp);
	
	//lift_config(decomp, encode, flgyuv, bpp, (long)size, databuffer);
	
	fp = fopen("y-out.32t","w");
	if (NULL == fp) {
		fprintf(stderr, "Could not open red for writing\n");
		perror("RED-WR:");
		exit(EXIT_FAILURE);
	}
		 
	if (sz != (int)fwrite(y,  sizeof(int), sz, fp)) {
		fprintf(stderr, "Write of red failed\n"); perror("RED:");
		exit(EXIT_FAILURE);
	}
	fclose(fp);

	fp = fopen("u-out.32t","w");
	if (NULL == fp) {
		fprintf(stderr, "Could not open red for writing\n");
		perror("RED-WR:");
		exit(EXIT_FAILURE);
	}
		 
	if (sz != (int)fwrite(u,  sizeof(int), sz, fp)) {
		fprintf(stderr, "Write of green failed\n"); perror("GREEN:");
		exit(EXIT_FAILURE);
	}
	fclose(fp);
	
	fp = fopen("v-out.32t","w");
	if (NULL == fp) {
		fprintf(stderr, "Could not open red for writing\n");
		perror("RED-WR:");
		exit(EXIT_FAILURE);
	}
		 
	if (sz != (int)fwrite(v,  sizeof(int), sz, fp)) {
		fprintf(stderr, "Write of green failed\n"); perror("BLUE:");
		exit(EXIT_FAILURE);
	}
	fclose(fp);
	}
	
	free(imgbm);
	return 0;
}
 
/*
computes u  v using y.  b. and  r
y = (r + (g * 2) + b) >> 2;
u = b - g;
v = r - g;
*/
void yuv(int w,int *r,int *g,int *b,int *u,int *v,int *y) {
	int idx, lidx;
	int *aa, *aa1, *aa2, *aa3, *aa4, *im;
	
	aa = r;
	aa1 = g;
	aa2 = b;
	aa3 = u;
	aa4 = v;
	im = y;
	
	lidx = w * w;
	
	for(idx=0; idx<lidx; idx++) {

 
		
		im[0] = (aa[0] + aa1[0]*2 + aa2[0])>>2;
		//u = b - g 
		aa3[0] = aa2[0] - aa1[0];
		//v = r - g
		aa4[0] = aa[0] - aa1[0];
		im+=1;
		aa+=1;
		aa2+=1;
		aa3+=1;
		aa4+=1;
		
	} 
}
/*computes r g b  from u v using y  u  v . 
r  g , and  b.
g = y - ((u + v) >> 2);
r = v + g;
b = u + g;
*/
void invyuv(int w,int *r,int *g,int *b,int *u,int *v,int *y) {
	int idx, lidx;
	int *aa, *aa1, *aa2, *aa3, *aa4, *im;
	
	aa = r;
	aa1 =g;
	aa2 = b;
	aa3 = u;
	aa4 = v;
	im = y;
	
	lidx = w * w;
	
	for(idx=0; idx<lidx; idx++) {
		
		//g = y - ((u + v) >> 2);
		aa1[0] = (im[0] - ((aa3[0] + aa4[0]) >> 2));
		 
		//r = v + g;
		aa[0] = aa4[0] + aa1[0];
		//b = u + g;
		aa2[0] = aa3[0] + aa1[0];
		
		im+=1;
		aa+=1;
		aa1+=1;
		aa2+=1;
		aa3+=1;
		aa4+=1;
		
	} 
}

void quantize(int w,int *y,int *u,int *v) {
	int idx, lidx;
	int *wy,*wu,*wv;
	
	wy = y;
	wu = u;
	wv = v;
 	
	lidx = w * w;
	
	for(idx=0; idx<lidx; idx++) {
		 
		wy[0] = wy[0]>>1;
		wu[0] = wu[0]>>1;
		wv[0] = wv[0]>>1;
		 
		wy+=1;
		wu+=1;
		wv+=1;	
	}		
}
