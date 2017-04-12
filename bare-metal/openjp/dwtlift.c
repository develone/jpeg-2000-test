/*
 * Copyright (c) 2008, Jerome Fimes, Communications & Systemes <jerome.fimes@c-s.fr>
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 * 1. Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in the
 *    documentation and/or other materials provided with the distribution.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS `AS IS'
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
 * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
 * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
 */
 
#include <stdio.h>
 
#include "dwtlift.h"
#include <sys/time.h>
#include <stdlib.h>
#include <math.h>
#include "openjpeg.h"
#include "opj_config.h"
#include "openjpeg.h"
#include <string.h>





//pass ip to a routine 
//which malloc 3 area
//read 65536  values of red 262144 32 bit int  0xc0000424 to 0xc0040423
//read 65536  values of green 262144 32 bit int 0xc0040424 to 0xc00c0423
//read 65536  values of blue 262144 32 bit int
int octave_write_byte(const char * fn,char * d_ptr, int sz) {
	 
	FILE *subfileptr;
	subfileptr = fopen(fn,"w");
	printf("file name %s data ptr 0x%x size %d \n",fn, d_ptr,sz);
	if (NULL == subfileptr) {
		/*
		fprintf(stderr, "Could not open red for writing\n");
		perror("RED-WR:");
		exit(EXIT_FAILURE);
		*/
		return(0);
	}
 
	if (sz != (int)fwrite(d_ptr,  sizeof(char), sz, subfileptr)) {
		fprintf(stderr, "Write of red failed\n"); perror("RED:");
		exit(EXIT_FAILURE);
	}
	
 	
	fclose(subfileptr);
	
	return(1);
}

/**
sample error debug callback expecting no client object
*/
static void error_callback(const char *msg, void *client_data) {
	(void)client_data;
	fprintf(stdout, "[ERROR] %s", msg);
}
/**
sample warning debug callback expecting no client object
*/
static void warning_callback(const char *msg, void *client_data) {
	(void)client_data;
	fprintf(stdout, "[WARNING] %s", msg);
}
/**
sample debug callback expecting no client object
*/
static void info_callback(const char *msg, void *client_data) {
	(void)client_data;
	fprintf(stdout, "[INFO] %s", msg);
}

void lift_config(int dec, int enc, int TCP_DISTORATIO, int FILTER, int bp, long imgsz,int *bufferptr)
{
 
	int height, width;
	int TopDown,plot;
	TopDown = 0;
	plot = 0;
	printf("in lift_config dec %d enc %d distoratio %d \n", dec,enc,TCP_DISTORATIO);
	decomp = dec;
	encode = enc;
	
 	
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

	width = (int)sqrt(memory);
	
	
	height = width;
	printf("memory %lf sqrt memory %lf %d %d \n",memory,sqrt(memory),width,height);
	printf("local char ptr %x\n",&lclip[0]);
 
	

	/*from test_tile_encoder*/
 
 
	TopDown = 0;
	
 	/*char *r,*g,*b;
	const char *octave_output_file_1;
	const char *octave_output_file_2;
	const char *octave_output_file_3;*/
	#define NUM_COMPS_MAX 4
	opj_cparameters_t l_param;
	opj_codec_t * l_codec;
	opj_image_t * l_image;
	opj_image_cmptparm_t l_params [NUM_COMPS_MAX];
	opj_stream_t * l_stream;
	OPJ_UINT32 l_nb_tiles;
	OPJ_UINT32 l_data_size;
	size_t len;

#ifdef USING_MCT
	const OPJ_FLOAT32 l_mct [] =
	{
		1 , 0 , 0 ,
		0 , 1 , 0 ,
		0 , 0 , 1
	};

	const OPJ_INT32 l_offsets [] =
	{
		128 , 128 , 128
	};
#endif

	opj_image_cmptparm_t * l_current_param_ptr;
	OPJ_UINT32 i;
	OPJ_BYTE *l_data;

  OPJ_UINT32 num_comps;
  int image_width;
  int image_height;
  int tile_width;
  int tile_height;
  int comp_prec;
  int irreversible;
  const char *output_file;

  
 

    num_comps = 3;
    image_width = width;
    image_height = height;
    tile_width = width;
    tile_height = height;
    comp_prec = 8;
    irreversible = FILTER;
    output_file = "test.j2k";
    
  if( num_comps > NUM_COMPS_MAX )
    {
	printf("num_comps > NUM_COMPS_MAX\n");	
    //return 1;
    }
	l_nb_tiles = (OPJ_UINT32)(image_width/tile_width) * (OPJ_UINT32)(image_height/tile_height);
	l_data_size = (OPJ_UINT32)tile_width * (OPJ_UINT32)tile_height * (OPJ_UINT32)num_comps * (OPJ_UINT32)(comp_prec/8);
	printf("l_nb_tiles %d l_data_size %d \n", l_nb_tiles, l_data_size);
	l_data = (OPJ_BYTE*) malloc(l_data_size * sizeof(OPJ_BYTE));
	if(l_data == NULL){
		printf("could not allocate the memory for l_data\n");
		//return 1;
	}	
	
	

	
	
	/*from test_tile_encoder*/
	
 
    /*
	r = malloc(sizeof(char)*height*width);
	g = malloc(sizeof(char)*height*width);
	b = malloc(sizeof(char)*height*width);
	printf("allocating rgb 0x%x 0x%x 0x%x \n",r,g,b);	 
	
	for (loop=0; loop < imgsz/3; loop++) {
			
		*b = lclip[0];
		lclip++;
		b++;
		*r = lclip[0];
		lclip++;
		r++;
		*g = lclip[0];
		lclip++;
		g++;
	}
		 
	printf("reseting pointers \n");
	r = r - (imgsz/3);
	g = g - (imgsz/3);
	b = b - (imgsz/3);
	*/
	for (i=0;i<((imgsz/3));i++)	{
		/*	
		l_data[i] = (OPJ_BYTE)g[i];
		l_data[i+(imgsz/3)] = (OPJ_BYTE)r[i];
		l_data[i+(imgsz/3)*2] = (OPJ_BYTE)b[i];	
		*/
		/*red to blue*/
		l_data[i+(imgsz/3)*2] = (OPJ_BYTE)lclip[0];
		lclip++;
		/*green to green*/
		l_data[i+(imgsz/3)]  = (OPJ_BYTE)lclip[0];
		lclip++;		
		/*blue to red*/
		l_data[i] = (OPJ_BYTE)lclip[0];
		lclip++;


	}

	/*
	printf("before reset 0x%x 0x%x 0x%x \n",r,g,b); 
	printf(" rgb 0x%x 0x%x 0x%x %d \n",r,g,b,plot);
	if(plot == 1) {
			
		printf("write the files \n");
		printf("red-out.32t, grn-out.32t, and blu-out.32t\n");
		octave_output_file_1 = "red-out.32t";
			 
			
		i = octave_write_byte(octave_output_file_1,r , width*height);
		if(i == 0) printf("could not write file\n");
	
		octave_output_file_2 = "grn-out.32t";
		//i = octave_write(octave_output_file_2, imgbm->m_green, sz);
		i = octave_write_byte(octave_output_file_2, g, width*height);	
		if(i == 0) printf("could not write file\n");
	
		octave_output_file_3 = "blu-out.32t";
			 
		i = octave_write_byte(octave_output_file_3, b, width*height);
		if(i == 0) printf("could not write file\n");
		}
		printf("FREE rgb 0x%x 0x%x 0x%x \n",r,g,b);
		free(r);
		free(g);
		free(b); 	 
 	*/
	lclip = (char *)*bufferptr;
 
 	
	gettimeofday(&start, NULL);
	/*from test_tile_encoder*/
	opj_set_default_encoder_parameters(&l_param);
	/** you may here add custom encoding parameters */
	/* rate specifications */
	/** number of quality layers in the stream */
	l_param.tcp_numlayers = 1;
	l_param.cp_fixed_quality = 1;
	l_param.tcp_distoratio[0] = TCP_DISTORATIO;
	/* is using others way of calculation */
	/* l_param.cp_disto_alloc = 1 or l_param.cp_fixed_alloc = 1 */
	/* l_param.tcp_rates[0] = ... */
	

	/* tile definitions parameters */
	/* position of the tile grid aligned with the image */
	l_param.cp_tx0 = 0;
	l_param.cp_ty0 = 0;
	/* tile size, we are using tile based encoding */
	l_param.tile_size_on = OPJ_TRUE;
	l_param.cp_tdx = tile_width;
	l_param.cp_tdy = tile_height;

	/* use irreversible encoding ?*/
	l_param.irreversible = irreversible;

	/* do not bother with mct, the rsiz is set when calling opj_set_MCT*/
	/*l_param.cp_rsiz = OPJ_STD_RSIZ;*/

	/* no cinema */
	/*l_param.cp_cinema = 0;*/

	/* no not bother using SOP or EPH markers, do not use custom size precinct */
	/* number of precincts to specify */
	/* l_param.csty = 0;*/
	/* l_param.res_spec = ... */
	/* l_param.prch_init[i] = .. */
	/* l_param.prcw_init[i] = .. */


	/* do not use progression order changes */
	/*l_param.numpocs = 0;*/
	/* l_param.POC[i].... */

	/* do not restrain the size for a component.*/
	/* l_param.max_comp_size = 0; */

	/** block encoding style for each component, do not use at the moment */
	/** J2K_CCP_CBLKSTY_TERMALL, J2K_CCP_CBLKSTY_LAZY, J2K_CCP_CBLKSTY_VSC, J2K_CCP_CBLKSTY_SEGSYM, J2K_CCP_CBLKSTY_RESET */
	/* l_param.mode = 0;*/

	/** number of resolutions */
	l_param.numresolution = decomp;

	/** progression order to use*/
	/** OPJ_LRCP, OPJ_RLCP, OPJ_RPCL, PCRL, CPRL */
	l_param.prog_order = OPJ_LRCP;

	/** no "region" of interest, more precisally component */
	/* l_param.roi_compno = -1; */
	/* l_param.roi_shift = 0; */

	/* we are not using multiple tile parts for a tile. */
	/* l_param.tp_on = 0; */
	/* l_param.tp_flag = 0; */

	/* if we are using mct */
#ifdef USING_MCT
	opj_set_MCT(&l_param,l_mct,l_offsets,NUM_COMPS);
#endif


	/* image definition */
	l_current_param_ptr = l_params;
	for (i=0;i<num_comps;++i) {
		/* do not bother bpp useless */
		/*l_current_param_ptr->bpp = COMP_PREC;*/
		l_current_param_ptr->dx = 1;
		l_current_param_ptr->dy = 1;

		l_current_param_ptr->h = (OPJ_UINT32)image_height;
		l_current_param_ptr->w = (OPJ_UINT32)image_width;

		l_current_param_ptr->sgnd = 0;
		l_current_param_ptr->prec = (OPJ_UINT32)comp_prec;

		l_current_param_ptr->x0 = 0;
		l_current_param_ptr->y0 = 0;

		++l_current_param_ptr;
	}

  /* should we do j2k or jp2 ?*/
  len = strlen( output_file );
  if( strcmp( output_file + len - 4, ".jp2" ) == 0 )
    {
    l_codec = opj_create_compress(OPJ_CODEC_JP2);
    }
  else
    {
		printf("In test_tile_encoder\n");
		printf("creating J2k\n");
    l_codec = opj_create_compress(OPJ_CODEC_J2K);
    }
	if (!l_codec) {
		free(l_data);
		printf("no l_codec\n");
		//return 1;
	}

	/* catch events using our callbacks and give a local context */
	opj_set_info_handler(l_codec, info_callback,00);
	opj_set_warning_handler(l_codec, warning_callback,00);
	opj_set_error_handler(l_codec, error_callback,00);

	l_image = opj_image_tile_create(num_comps,l_params,OPJ_CLRSPC_SRGB);
	if (! l_image) {
		free(l_data);
		opj_destroy_codec(l_codec);
		printf("no l_image\n");
		//return 1;
	}

	l_image->x0 = 0;
	l_image->y0 = 0;
	l_image->x1 = (OPJ_UINT32)image_width;
	l_image->y1 = (OPJ_UINT32)image_height;
	l_image->color_space = OPJ_CLRSPC_SRGB;

	if (! opj_setup_encoder(l_codec,&l_param,l_image)) {
		fprintf(stderr, "ERROR -> test_tile_encoder: failed to setup the codec!\n");
		opj_destroy_codec(l_codec);
		opj_image_destroy(l_image);
		free(l_data);
		printf("no opj_setup_encoder\n");
		//return 1;
	}

    l_stream = opj_stream_create_default_file_stream(output_file, OPJ_FALSE);
    if (! l_stream) {
		fprintf(stderr, "ERROR -> test_tile_encoder: failed to create the stream from the output file %s !\n",output_file );
		opj_destroy_codec(l_codec);
		opj_image_destroy(l_image);
		free(l_data);
		printf("no l_stream\n");
		//return 1;
	}

	if (! opj_start_compress(l_codec,l_image,l_stream)) {
		fprintf(stderr, "ERROR -> test_tile_encoder: failed to start compress!\n");
        opj_stream_destroy(l_stream);
		opj_destroy_codec(l_codec);
		opj_image_destroy(l_image);
		free(l_data);
		printf("no opj_start_compress\n");
		//return 1;
	}
	gettimeofday(&end, NULL);

	seconds  = end.tv_sec  - start.tv_sec;
	useconds = end.tv_usec - start.tv_usec;
 
	mtime = seconds + useconds;
 
	printf("Elapsed time: %ld seconds %ld useconds %ld starting openjpeg\n", mtime,seconds, useconds);
	gettimeofday(&start, NULL);
	for (i=0;i<l_nb_tiles;++i) {
		if (! opj_write_tile(l_codec,i,l_data,l_data_size,l_stream)) {
			fprintf(stderr, "ERROR -> test_tile_encoder: failed to write the tile %d!\n",i);
            opj_stream_destroy(l_stream);
			opj_destroy_codec(l_codec);
			opj_image_destroy(l_image);
			free(l_data);
			printf("no opj_write_tile\nn");
			//return 1;
		}
	}

	if (! opj_end_compress(l_codec,l_stream)) {
		fprintf(stderr, "ERROR -> test_tile_encoder: failed to end compress!\n");
        opj_stream_destroy(l_stream);
		opj_destroy_codec(l_codec);
		opj_image_destroy(l_image);
		free(l_data);
		printf("no opj_end_compress\n");
		//return 1;
	}

    opj_stream_destroy(l_stream);
	opj_destroy_codec(l_codec);
	opj_image_destroy(l_image);
		
		/*from test_tile_encoder*/
 
	
		/* 
		for (loop=0; loop < imgsz/3; loop++) {
 
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
		*/
	 
	gettimeofday(&end, NULL);

	seconds  = end.tv_sec  - start.tv_sec;
	useconds = end.tv_usec - start.tv_usec;
 
	mtime = seconds + useconds;
 
	printf("Elapsed time: %ld seconds %ld useconds %ld \n", mtime,seconds, useconds);

 	 
}
 
 
