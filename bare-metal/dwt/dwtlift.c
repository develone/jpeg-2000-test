/*
 * dwtlift.c
 * 
 * A simple C library to include in your Ultibo project
 * 
 */
 
#include <stdio.h>
#include "lifting.h"
#include "dwtlift.h"
#include <sys/time.h>
#include <stdlib.h>
#include <math.h>
#include "openjpeg.h"

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


  
 	

//pass ip to a routine 
//which malloc 3 area
//read 65536  values of red 262144 32 bit int  0xc0000424 to 0xc0040423
//read 65536  values of green 262144 32 bit int 0xc0040424 to 0xc00c0423
//read 65536  values of blue 262144 32 bit int

void lift_config(int dec, int enc, int mct, int bp, long imgsz,int *bufferptr)
{
	OPJ_INT32* c0;
	OPJ_INT32* c1;
	OPJ_INT32* c2;
	printf("in lift_config dec %d enc %d yuv %d \n", dec,enc,mct);
	decomp = dec;
	encode = enc;
	flgyuv = mct;
	gettimeofday(&start, NULL);
	//start_sec = currentTime.tv_usec;	
	char *lclip = (char *)*bufferptr;
	printf("In lift_config first byte 0x%x\n",lclip[0]);
	printf("bpp %ld\n",bp);

	printf("size %ld\n",imgsz);
	printf("pointer passed %x %x\n",*bufferptr,bufferptr);


	/* Need to determine the ww width & hh height 
 	* given the ss bpp BPP bits per pixel & Size
 	*/   

	if(bp==8) memory = (double)imgsz;
	else memory = (double)(imgsz/3.0);

	ww = (int)sqrt(memory);
	hh = ww;
	printf("memory %lf sqrt memory %lf %d %d \n",memory,sqrt(memory),ww,hh);
	printf("local char ptr %x\n",&lclip[0]);
 
	IMAGEP		img;
 
	printf("allocating memory with malloc \n");
	if (bp == 24) {
		if(flgyuv == 1) {
			img = (IMAGEP)malloc(sizeof(IMAGE)+7*ww*hh*sizeof(int));
			y = &img->data[4*ww*hh];
			u = &img->data[5*ww*hh];
			v = &img->data[6*ww*hh];
		}
		else {
			img = (IMAGEP)malloc(sizeof(IMAGE)+4*ww*hh*sizeof(int));
		}
		img->m_w = ww;
		img->m_h = hh;
		img->m_red   = img->data;
		img->m_green = &img->data[ww*hh];
		img->m_blue  = &img->data[2*ww*hh];
		img->m_tmp  = &img->data[3*ww*hh];

		//printf("the size of malloc %x \n",sizeof(img));
		printf("img->m_red 0x%x \n",img->m_red);
		printf("img->m_green 0x%x \n",img->m_green);
		printf("img->m_blue 0x%x \n",img->m_blue);
		printf("img->m_tmp 0x%x \n",img->m_tmp);
		 
	} else if (bp == 8) {
			img = (IMAGEP)malloc(sizeof(IMAGE)+2*ww*hh*sizeof(int));
			img->m_w = ww;
			img->m_h = hh;
			img->m_red   = img->data;
			img->m_tmp = &img->data[ww*hh];
			printf("img->m_red 0x%x \n",img->m_red);
			printf("img->m_tmp 0x%x \n",img->m_tmp);
	}
	
 
	if (bp == 24) {
		printf("Copying RGB 8 bit char to 32 int \n");
	
		for (loop=0; loop < imgsz/3; loop++) {
			*img->m_red = lclip[0];
			lclip++;
			img->m_red++;
			*img->m_green = lclip[0];
			lclip++;
			img->m_green++;
			*img->m_blue = lclip[0];
			lclip++;
			img->m_blue++;
		}
		
		printf("reseting pointers \n");
		img->m_red   = img->data;
		c0 = (OPJ_INT32*)img->m_red;
		img->m_green = &img->data[ww*hh];
		c1 = (OPJ_INT32*)img->m_green;
		img->m_blue  = &img->data[2*ww*hh];
		c2 = (OPJ_INT32*)img->m_blue;	
		lclip = (char *)*bufferptr;
		printf("img->m_red 0x%x passed ptr 0x%x\n",img->m_red, &lclip[0]);
		printf("img->m_green 0x%x \n",img->m_green);
		printf("img->m_blue 0x%x \n",img->m_blue);
		if(flgyuv == 1) {
			printf("converting rgb to yuv\n");
			opj_mct_encode(c0,c1,c2,ww*ww);
			//yuv(ww, img->m_red, img->m_green, img->m_blue, u, v, v);
		}	
	
	} else if (bp == 8) {
		printf("Copying GRAY  8 bit char to 32 int \n");
	
		for (loop=0; loop < imgsz; loop++) {
			*img->m_red = lclip[0];
			lclip++;
			img->m_red++;
		}
		printf("reseting pointers \n");
		img->m_red   = img->data;
		lclip = (char *)*bufferptr;
		printf("img->m_red 0x%x passed ptr 0x%x\n",img->m_red, &lclip[0]);
	}	
 
	if (bp==24) {
		if (encode == 1) {
			if(flgyuv ==1){
				printf("Calling lifting y\n");
				lifting(ww, c0, img->m_tmp, decomp);
				printf("Calling lifting u\n");
				lifting(ww, c1, img->m_tmp, decomp); 
				printf("Calling lifting v\n");
				lifting(ww, c2, img->m_tmp,decomp);
				printf("lifting to Buffer\n");
			}
			else {
				
				printf("Calling lifting red\n");
				lifting(ww, img->m_red, img->m_tmp, decomp);
				printf("Calling lifting green\n");
				lifting(ww, img->m_green, img->m_tmp, decomp);
				printf("Calling lifting blue\n");
				lifting(ww, img->m_blue, img->m_tmp,decomp);
				printf("lifting to Buffer\n");
			}
		}
		else {
			printf("Calling invlifting red\n");
			invlifting(ww, img->m_red, img->m_tmp, decomp);
			printf("Calling invlifting green\n");
			invlifting(ww, img->m_green, img->m_tmp, decomp);
			printf("Calling invlifting blue\n");
			invlifting(ww, img->m_blue, img->m_tmp,decomp);
			printf("invlifting to Buffer\n");			
		}
		for (loop=0; loop < imgsz/3; loop++) {
			if(flgyuv ==1){
				lclip[0] = *c0 ;
				lclip++;
				c0++;
				lclip[0] = *c1;
				lclip++;
				c1++;
				lclip[0] = *c2 ;
				lclip++;
				c2++;
			}
			else {
				lclip[0] = *img->m_red ;
				lclip++;
				img->m_red++;
				lclip[0] = *img->m_green ;
				lclip++;
				img->m_green++;
				lclip[0] = *img->m_blue ;
				lclip++;
				img->m_blue++;
			}
		}
	} else if (bp == 8) {
		printf("Calling lifting red\n");
	
		//img->m_red   = img->data;
		lifting(ww, img->m_red, img->m_tmp, decomp);
		img->m_tmp  = &img->data[3*ww*hh];
 		printf("lifting to Buffer\n");
		for (loop=0; loop < imgsz; loop++) {
			lclip[0] = *img->m_red ;
			lclip++;
		}
		
	}
	gettimeofday(&end, NULL);
 
	seconds  = end.tv_sec  - start.tv_sec;
	useconds = end.tv_usec - start.tv_usec;
 
	mtime = seconds + useconds;
 
	printf("Elapsed time: %ld microseconds\n", mtime); 	
	free(img);	 
}
 
 
