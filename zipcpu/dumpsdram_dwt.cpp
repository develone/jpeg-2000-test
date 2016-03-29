////////////////////////////////////////////////////////////////////////////////
//
// Filename: 	dumpsdram.cpp
//
// Project:	XuLA2 board
//
// Purpose:	Read local memory, dump into a file.
//
//
// Creator:	Dan Gisselquist, Ph.D.
//		Gisselquist Technology, LLC
//
////////////////////////////////////////////////////////////////////////////////
//
// Copyright (C) 2015, Gisselquist Technology, LLC
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
// License:	GPL, v3, as defined and found on www.gnu.org,
//		http://www.gnu.org/licenses/gpl.html
//
//
////////////////////////////////////////////////////////////////////////////////
//
//
//
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <strings.h>
#include <ctype.h>
#include <string.h>
#include <signal.h>
#include <assert.h>

#include "llcomms.h"
#include "usbi.h"
#include "port.h"
#include "regdefs.h"

FPGA	*m_fpga;

int main(int argc, char **argv) {

int index,row,col;
int w,h;
w = 256;
h = 256;
index = 0;
row = 0;
col = 0;
int img[w][h];
/*
int *img_ptr = (int *)0x800000;
point to start of SDRAM
int *img_ptr1 = (int *)0x810000;
*/
int bb[w*h],cc[w*h],*img_ptr,*img_ptr1;
int temp[w][h];
img_ptr = &bb[0]; 
img_ptr1 = &cc[0];
	FILE        *fp, *fpin, *fpout; 
	unsigned	pos=0;
	int		port = FPGAPORT, skp;
	const int	BUFLN = 127;
	FPGA::BUSW	*buf = new FPGA::BUSW[BUFLN],
			*cmp = new FPGA::BUSW[BUFLN];
	bool		use_usb = true;

	skp = 1;
	for(int argn=0; argn<argc-skp; argn++) {
		if (argv[argn+skp][0] == '-') {
			if (argv[argn+skp][1] == 'u')
				use_usb = true;
			else if (argv[argn+skp][1] == 'p') {
				use_usb = false;
				if (isdigit(argv[argn+skp][2]))
					port = atoi(&argv[argn+skp][2]);
			} skp++; argn--;
		} else
			argv[argn] = argv[argn+skp];
	} argc -= skp;

	if (argc!=2) {
		printf("Usage: dumpsdram [-p [port]] srcfile outfile\n");
		exit(-1);
	}

	/*
	for(int i=0; i<argc; i++) {
		printf("ARG[%d] = %s\n", i, argv[i]);
	} */

	fpin = fopen(argv[0], "rb");
	if (fpin == NULL) {
		fprintf(stderr, "Could not open %s\n", argv[1]);
		exit(-1);
	}

	if (use_usb)
		m_fpga = new FPGA(new USBI());
	else
		m_fpga = new FPGA(new NETCOMMS(FPGAHOST, port));


	try {
		int	nr;
		pos = SDRAMBASE;
		do {
			nr = BUFLN;
			if (nr + pos > SDRAMBASE*2)
				nr = SDRAMBASE*2 - pos;
			nr = fread(buf, sizeof(FPGA::BUSW), nr, fpin);
			/*for(int ii= 0;ii<nr;ii++) 
				printf("%d \n",buf[ii]);*/
			//printf("%d %d %d\n",sizeof(FPGA::BUSW), nr,sizeof(buf));
			//This loop puts the data in array bb
			for(int ii= 0;ii<nr;ii++)
			{
				bb[index] =buf[ii];
				//printf("%d %d \n",index, bb[index]);
				index = index + 1;
			}
			//printf("%d %d\n",sizeof(FPGA::BUSW), nr);
			if (nr <= 0)
				break;

			if (false) {
				for(int i=0; i<nr; i++)
					m_fpga->writeio(pos+i, buf[i]);
			} else
			    //printf("%x %x %x \n",pos, nr, *buf);
				m_fpga->writei(pos, nr, buf);
			pos += nr;
		} while((nr > 0)&&(pos < 2*SDRAMBASE));

		printf("SUCCESS::fully wrote full file to memory (pos = %08x)\n", pos);
	} catch(BUSERR a) {
		fprintf(stderr, "BUS Err while writing at address 0x%08x\n", a.addr);
		fprintf(stderr, "... is your program too long for this memory?\n");
		exit(-2);
	} catch(...) {
		fprintf(stderr, "Other error\n");
		exit(-3);
	}
 	
	delete	m_fpga;
	/* Placing the read data in the img[row][col]
	 * The following lines were when the python program
	 * read the image and wrote the data to the
	 * file img_to_fpga.bin
	 * col 17 row 16 pixel 164 sdram 0x801011
     * col 18 row 16 pixel 172 sdram 0x801012
     * col 19 row 16 pixel 164 sdram 0x801013

	 * col 175 row 60 pixel 156 sdram 0x803caf
     * col 176 row 60 pixel 148 sdram 0x803cb0
     * col 177 row 60 pixel 148 sdram 0x803cb1
     * col 178 row 60 pixel 156 sdram 0x803cb2
     * 			.
     * 			.
     * col 252 row 255 pixel 92 sdram 0x80fffc
     * col 253 row 255 pixel 92 sdram 0x80fffd
     * col 254 row 255 pixel 100 sdram 0x80fffe
     * col 255 row 255 pixel 108 sdram 0x80ffff

     * The following lines were when the 
     * dumpsdram read the file img_to_fpga.bin
     * col 17 row 16 164
	 * col 18 row 16 172
     * col 19 row 16 164
     * 			.
     *          .
     * col 175 row 60 156
     * col 176 row 60 148
     * col 177 row 60 148
	 * col 178 row 60 156
	 * 			.
	 * 			.
	 * col 252 row 255 92
     * col 253 row 255 92
     * col 254 row 255 100
     * col 255 row 255 108


	 */

	for (int p =0; p < 2; p++) {
	//img_ptr pass 0 points to array bb	SDRAM 0x800000 
	//img_ptr pass 1 points to array cc	SDRAM 0x810000
	if (p == 0)	img_ptr = &bb[0];
	else img_ptr = &cc[0];
    for (int col = 0; col<256;col++) { 
		for (int row = 2;row<256;row=row+2) {
			//printf("row %d col %d lft %d sam %d rht %d\n",row,col,img[row-1][col],img[row][col],img[row+1][col]);
			//img[row][col] = img[row][col] - ( (img[row-1][col] + img[row+1][col]) >> 1);
			*(img_ptr+col+row*256) = *(img_ptr+col+row*256) - ((*(img_ptr+col+(row-1)*256) + *(img_ptr+col+(row+1)*256)) >> 1);
			//printf("%d %d %d\n",row,col,img[row][col]);
			/*
			C					Python
			116 248 0			116 248 0
			118 248 -4			118 248 -4
			120 248 4			120 248 4
			122 248 0			122 248 0
			124 248 8			124 248 8
			126 248 4			126 248 4
			*/
			
	    }
		for (int row = 1;row<256-2;row=row+2) {
			//printf("row %d col %d lft %d sam %d rht %d\n",row,col,img[row-1][col],img[row][col],img[row+1][col]);
			//img[row][col] = img[row][col] - ( (img[row-1][col] + img[row+1][col] +2) >> 2);
			*(img_ptr+col+row*256) = *(img_ptr+col+row*256) - ((*(img_ptr+col+(row-1)*256) + *(img_ptr+col+(row+1)*256)+2) >> 2);
			//printf("%d %d %d\n",row,col,img[row][col]);
			/*
			C					Python
			81 253 156			81 253 156			
			83 253 155			83 253 157**			
			85 253 147			85 253 149**
			87 253 147			87 253 149**
			89 253 157			89 253 155**


			 */
		} 
	}
	

	
	
	
 
	// de-interleave img_ptr1 pass 0 points to array cc
	// de-interleave img_ptr1 pass 1 points to array bb
	if (p == 0)	img_ptr1 = &cc[0];
	else img_ptr1 = &bb[0];
	for (int row = 0 ; row < 256; row++) {
		
		for (int col = 0; col < 256;col++) {  
            //printf("row %d col %d %d\n", row, col, row/2);
			if (row % 2 == 0) {
				
				//temp[col][row/2] =  img[row][col];
				*(img_ptr1+col*256+row/2) =  *(img_ptr+col+row*256);
				 
				 
			}	
			else {
				
				//temp[col][row/2 + 256/2] =  img[row][col];
				 *(img_ptr1+col*256+row/2+256/2) =  *(img_ptr+col+row*256);
				 
			}	
		}
	}
	//End of 2 passes
    }
    index = 0;
	for(row = 0 ; row < 256;row++) {
		for(col = 0; col < 256;col++) {
			
			img[row][col] = bb[index];
			//printf ("col %d row %d %d\n", col,row,img[row][col]);
			index = index + 1;
		}
	}
	/*
	fpout = fopen("pass.bin", "wb");
	for (int jj= 0; jj<65536; jj++) fwrite(&bb[jj],sizeof(int),1,fpout);
	*/
	fpout = fopen("pass.bin", "wb");
	for (int row = 0 ; row < 256; row++) {
		
	for (int col = 0; col < 256;col++) { 
		fwrite(&img[row][col],sizeof(int),1,fpout);
	}
    } 
}


