/*
 * lifting.c
 * 
 * A simple C library to include in your Ultibo project
 * This example allow passing int & pointer
 * 
 */
 
#include <stdio.h>

void lifting (int w, int *ibuf, int *tmpbuf)
{

	printf ("Hello Ultibo from C!!\n");
	printf(" a %d b %d c %d \n",w,ibuf,tmpbuf);
	printf(" a %d b %d c %d \n",w,*ibuf,*tmpbuf);
}
