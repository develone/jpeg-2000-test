////////////////////////////////////////////////////////////////////////////////
//
// Filename: 	liftmain.c
//
// Project:	XuLA2-LX25 SoC based upon the ZipCPU
//
// Purpose:	On a PC, this file reads in an image from a PNG file, and runs
//		the lifting scheme on it.  On the ZipCPU, it just runs lifting
//	on a section of memory.
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
#include "lifting.h"

typedef struct {
	int	m_w, m_h;
	int	*m_red, *m_green, *m_blue;
	int	data[1];
} IMAGE, *IMAGEP;

#ifdef	__ZIPCPU__
#include "board.h"
#include "lx9.h"

asm("\t.section\t.start\n"
        "\t.global\t_start\n"
        "\t.type\t_start,@function\n"
        "_start:\n"
        "\tLDI\t_top_of_stack,SP\n"
        "\tBRA\tentry\n"
        "\t.section\t.text");

void	wait(unsigned int msk) {
	*PIC = 0x7fff0000|msk;
	asm("MOV\tidle_task(PC),uPC\n");
	*PIC = 0x80000000|(msk<<16);
	asm("WAIT\n");
	*PIC = 0;
}

asm("\nidle_task:\n\tWAIT\n\tBRA\tidle_task\n");

void	entry(void) {
	int	*img = SDRAM, *alt = &img[256*257];
	int	done;

	sys->io_bustimer = 0x7fffffff;
	lifting(256, img, alt);
	done = 0x7fffffff - sys->io_bustimer;
	img[0] = done;
	zip_halt();
}

#else

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <png.h>

IMAGEP readpng(const char *fname) {
	FILE	*pngfp;
	char	header[8];
	png_structp	png_ptr;
	png_infop	info_ptr, end_info;
	IMAGEP		img;
	int		i, w, h, nr;
	unsigned	*raw_data, **rowp;

	pngfp = fopen(fname, "rb");
	if (!pngfp) {
		fprintf(stderr, "Could not open %s\n", fname);
		exit(EXIT_FAILURE);
	} nr = fread(header, 1, sizeof(header), pngfp);
	if (nr != sizeof(header)) {
		fprintf(stderr, "Could not read %s\n", fname);
		exit(EXIT_FAILURE);
	} if (png_sig_cmp((png_bytep)header, 0, (png_size_t)sizeof(header))) {
		fprintf(stderr, "%s is not a PNG file\n", fname);
		exit(EXIT_FAILURE);
	}

	png_ptr = png_create_read_struct(PNG_LIBPNG_VER_STRING,
			NULL, NULL, NULL);
	if (!png_ptr) {
		fprintf(stderr, "PNG-CREATE-READ_STRUCT returned an err\n");
		exit(EXIT_FAILURE);
	}

	info_ptr = png_create_info_struct(png_ptr);
	if (!info_ptr) {
		fprintf(stderr, "PNG-CREATE-INFO_PTR failed\n");
		png_destroy_read_struct(&png_ptr, (png_infopp)NULL, (png_infopp)NULL);
		exit(EXIT_FAILURE);
	}

	end_info = png_create_info_struct(png_ptr);
	if (!end_info) {
		fprintf(stderr, "PNG-CREATE-INFO_PTR failed\n");
		png_destroy_read_struct(&png_ptr, (png_infopp)NULL, (png_infopp)NULL);
		exit(EXIT_FAILURE);
	}

	png_init_io(png_ptr, pngfp);
	png_set_sig_bytes(png_ptr, sizeof(header));

	png_read_info(png_ptr, info_ptr);

	w = png_get_image_width(png_ptr, info_ptr);
	h = png_get_image_height(png_ptr, info_ptr);

	img = (IMAGEP)malloc(sizeof(IMAGE)+3*w*h*sizeof(int));
	img->m_w = w;
	img->m_h = h;
	img->m_red   = img->data;
	img->m_green = &img->data[w*h];
	img->m_blue  = &img->data[2*w*h];

	int	depth = png_get_bit_depth(png_ptr, info_ptr);
	int	ctype = png_get_color_type(png_ptr, info_ptr);
	int	xtype = png_get_compression_type(png_ptr, info_ptr);
	int	itype = png_get_interlace_type(png_ptr, info_ptr);
	int	chans = png_get_channels(png_ptr, info_ptr);
	int	rbytes= png_get_rowbytes(png_ptr, info_ptr);

	if (0) {
	printf("WIDTH            : %d\n", w);
	printf("HEIGHT           : %d\n", h);
	printf("DEPTH            : %d\n", depth);
	printf("COLOR-TYPE       : %d %s\n", ctype,
		(ctype == PNG_COLOR_TYPE_PALETTE)?"(palette)"
		:((ctype == PNG_COLOR_TYPE_RGB)?"(rgb)"
		:((ctype == PNG_COLOR_TYPE_GRAY)?"(gray)"
		:((ctype == PNG_COLOR_TYPE_RGB_ALPHA)?"(rgba)"
		:"other-unknown"))));
	printf("COMPRESSION-TYPE : %d\n", xtype);
	printf("INTERLACE-TYPE   : %d %s\n", itype,
		(itype == PNG_INTERLACE_NONE)?"None":"Adam7");
	printf("CHANNELS         : %d\n", chans);
	printf("ROW-BYTES        : %d\n", rbytes);
	}

	if (ctype == PNG_COLOR_TYPE_PALETTE)
		png_set_palette_to_rgb(png_ptr);
	if ((ctype == PNG_COLOR_TYPE_GRAY) && (depth < 8))
		png_set_expand_gray_1_2_4_to_8(png_ptr);
	if (depth == 16)
		png_set_strip_16(png_ptr);

	png_set_filler(png_ptr, 0, 0);
	png_set_swap(png_ptr);

	raw_data = (unsigned *)malloc(sizeof(unsigned)*w*h);
	rowp = (unsigned **)malloc(sizeof(unsigned *)*h);
	for(i=0; i<h; i++)
		rowp[i] = &raw_data[w*i];

	png_read_image(png_ptr, (unsigned char **)rowp);

	for(i=0; i<w * h; i++) {
		unsigned pixv = raw_data[i];

		img->m_red[i]   = (pixv>>16)&0x0ff;
		img->m_green[i] = (pixv>> 8)&0x0ff;
		img->m_blue[i]  = (pixv>>24)&0x0ff;
	}

	// Need to delete the PNG buffers and read structures here
	// free(png_ptr);
	// free(info_ptr);
	// free(end_info);
	// png_destroy_read_struct(&png_ptr, &info_ptr, &end_info);

	free(raw_data);
	free(rowp);

	return img;
}

int main(int argc, char **argv) {
	IMAGEP	img;
	FILE	*fp;
	int	sz, *scratch;

	if (argc != 2) {
		printf("USAGE: liftmain pngfile\n");
		exit(EXIT_SUCCESS);
	}

	img = readpng(argv[1]);

	if ((img->m_h <= 8)||(img->m_w != img->m_h)) {
		printf("Don\'t know how to operate on an %d x %d image\n",
			img->m_w, img->m_h);
		exit(EXIT_FAILURE);
	}

	assert(img->m_w == img->m_h);
	assert((img->m_w&7)==0);
	sz = img->m_w * img->m_h;
	scratch = (int *)malloc(sizeof(int) * sz);
	lifting(img->m_w, img->m_red  , scratch);
	lifting(img->m_w, img->m_green, scratch);
	lifting(img->m_w, img->m_blue , scratch);

	fp = fopen("red-out.32t","w");
	if (NULL == fp) {
		fprintf(stderr, "Could not open red for writing\n");
		perror("RED-WR:");
		exit(EXIT_FAILURE);
	}
	if (sz != (int)fwrite(img->m_red,  sizeof(int), sz, fp)) {
		fprintf(stderr, "Write of red failed\n"); perror("RED:");
		exit(EXIT_FAILURE);
	}
	fclose(fp);

	fp = fopen("grn-out.32t","w");
	if (NULL == fp) {
		fprintf(stderr, "Could not open green for writing\n");
		perror("GRN-WR:");
		exit(EXIT_FAILURE);
	}
	if (sz != (int)fwrite(img->m_green, sizeof(int), sz, fp)) {
		fprintf(stderr, "Write of red failed\n"); perror("RED:");
		exit(EXIT_FAILURE);
	}
	fclose(fp);

	fp = fopen("blu-out.32t","w");
	if (NULL == fp) {
		fprintf(stderr, "Could not open blue for writing\n");
		perror("BLU-WR:");
		exit(EXIT_FAILURE);
	}
	if (sz != (int)fwrite(img->m_blue,  sizeof(int), sz, fp)) {
		fprintf(stderr, "Write of red failed\n"); perror("RED:");
		exit(EXIT_FAILURE);
	}
	fclose(fp);

	return EXIT_SUCCESS;
}

#endif
