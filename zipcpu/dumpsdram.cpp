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
//int *ptr_one;
int index,row,col;
index = 0;
row = 0;
col = 0;
int img[256][256];
int bb[65536];
int temp[256][256];
 
	FILE		*fp, *fpin, *fpout;
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
/*
	rewind(fpin);

	fp = fopen(argv[1], "wb");
	if (fp == NULL) {
		fprintf(stderr, "Could not open: %s\n", argv[2]);
		exit(-1);
	}

	unsigned	mmaddr[65536], mmval[65536], mmidx = 0;

	try {
		pos = SDRAMBASE;
		const unsigned int MAXRAM = SDRAMBASE*2;
		bool	mismatch = false;
		unsigned	total_reread = 0;
		do {
			int nw, nr;
			if (MAXRAM-pos > BUFLN)
				nr = BUFLN;
			else
				nr = MAXRAM-pos;

			if (false) {
				for(int i=0; i<nr; i++)
					buf[i] = m_fpga->readio(pos+i);
			} else
				m_fpga->readi(pos, nr, buf);

			pos += nr;
			nw = fwrite(buf, sizeof(FPGA::BUSW), nr, fp);
			if (nw < nr) {
				printf("Only wrote %d of %d words!\n", nw, nr);
				exit(-2);
			} // printf("nr = %d, pos = %08x (%08x / %08x)\n", nr,
			//	pos, SDRAMBASE, MAXRAM);

			{int cr;
			cr = fread(cmp, sizeof(FPGA::BUSW), nr, fpin);
			total_reread += cr;
			for(int i=0; i<cr; i++)
				if (cmp[i] != buf[i]) {
					printf("MISMATCH: MEM[%08x] = %08x(read) != %08x(expected)\n",
						pos-nr+i, buf[i], cmp[i]);
					mmaddr[mmidx] = pos-nr+i;
					mmval[mmidx] = cmp[i];
					if (mmidx < 65536)
						mmidx++;
					mismatch = true;
				}
			if (cr != nr) {
				printf("Only read %d words from our input file\n", total_reread);
				break;
			}
			}
		} while(pos < MAXRAM);
		if (mismatch)
			printf("Read %04x (%6d) words from memory.  These did not match the source file.  (Failed test)\n",
				pos-SDRAMBASE, pos-SDRAMBASE);
		else
			printf("Successfully  read&copied %04x (%6d) words from memory\n",
				pos-SDRAMBASE, pos-SDRAMBASE);
	} catch(BUSERR a) {
		fprintf(stderr, "BUS Err at address 0x%08x\n", a.addr);
		fprintf(stderr, "... is your program too long for this memory?\n");
		exit(-2);
	} catch(...) {
		fprintf(stderr, "Other error\n");
		exit(-3);
	}

	for(unsigned i=0; i<mmidx; i++) {
		unsigned bv = m_fpga->readio(mmaddr[i]);
		if (bv == mmval[i])
			printf("Re-match, MEM[%08x]\n", mmaddr[i]);
		else
			printf("2ndary Fail: MEM[%08x] = %08x(read) != %08x(expected)\n",
				mmaddr[i], bv, mmval[i]);
	}
*/	
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
	index = 0;
	for(row = 0 ; row < 256;row++) {
		for(col = 0; col < 256;col++) {
			
			img[row][col] = bb[index];
			//printf ("col %d row %d %d\n", col,row,img[row][col]);
			index = index + 1;
		}
	}
	/*From line 276 to 330 Needs to be perform twice currently only once.
	 */ 	
    for (int col = 0; col<256;col++) { 
		for (int row = 2;row<256;row=row+2) {
			//printf("row %d col %d lft %d sam %d rht %d\n",row,col,img[row-1][col],img[row][col],img[row+1][col]);
			img[row][col] = img[row][col] - ( (img[row-1][col] + img[row+1][col]) >> 1);
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
			img[row][col] = img[row][col] - ( (img[row-1][col] + img[row+1][col] +2) >> 2);
			printf("%d %d %d\n",row,col,img[row][col]);
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
	
	// de-interleave
	 
	for (int row = 0 ; row < 256; row++) {
		
		for (int col = 0; col < 256;col++) {  
            //printf("row %d col %d %d\n", row, col, row/2);
			if (row % 2 == 0) {
				//printf("if row %d col %d %d\n", row, col, row/2);
				temp[col][row/2] =  img[row][col];
			}	
			else {
				//printf("else row %d col %d %d\n", row, col, row/2);
				temp[col][row/2 + 256/2] =  img[row][col];
			}	
		}
	}
    //write temp to img
	for (int row = 0;row < 256-2;row++) {
		for (int col = 0;col < 256;col++) {
			img[row][col] = temp[row][col];
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


