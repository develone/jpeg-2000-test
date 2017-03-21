/*
 * dwtlift.c
 * 
 * A simple C library to include in your Ultibo project
 * 
 */
 
#include <stdio.h>
 
#include "dwtlift.h"
#include <sys/time.h>
#include <stdlib.h>
#include <math.h>
#include "openjpeg.h"

 
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
				//lifting(ww, c0, img->m_tmp, decomp);
				printf("Calling lifting u\n");
				//lifting(ww, c1, img->m_tmp, decomp); 
				printf("Calling lifting v\n");
				//lifting(ww, c2, img->m_tmp,decomp);
				printf("lifting to Buffer\n");
			}
			else {
				
				printf("Calling lifting red\n");
				//lifting(ww, img->m_red, img->m_tmp, decomp);
				printf("Calling lifting green\n");
				//lifting(ww, img->m_green, img->m_tmp, decomp);
				printf("Calling lifting blue\n");
				//lifting(ww, img->m_blue, img->m_tmp,decomp);
				printf("lifting to Buffer\n");
			}
		}
		else {
			printf("Calling invlifting red\n");
			//invlifting(ww, img->m_red, img->m_tmp, decomp);
			printf("Calling invlifting green\n");
			//invlifting(ww, img->m_green, img->m_tmp, decomp);
			printf("Calling invlifting blue\n");
			//invlifting(ww, img->m_blue, img->m_tmp,decomp);
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
 
 
