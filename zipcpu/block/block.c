
 
#ifdef __ZIPCPU__
void free(void *);
typedef int int32;
#else
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <assert.h>
#endif


void extract(int *ibuf, int *obuf, int w, int h) {
	int *ip,*op;
	int row,col;	
		
	for (row=0;row<h;row++) {
		ip = ibuf + row;
		op = obuf + row;
		for (col=0;col<w;col++) {
			op[0] = ip[0];
			
			ip+=256;
			op+=256;
		}
	}
}
/*
 *process across the row
 * process row col 
*/
void disp(int *ibuf,  int w, int h) {
	int *ip;
	int row,col;		
	for (row=0;row<h;row++) {
		ip = ibuf + row;
		 
		for (col=0;col<w;col++) {
			printf("%5d ", ip[0]);
			ip+=256;
		}
		printf("\n");
	}
}

/*
 *process down the col
 * process col row
 * based on ibuf of 256 x 256 
*/
void disp1(int *ibuf,  int w, int h) {
	int *ip;
	int row,col;		
	for (row=0;row<h;row++) {
		ip = ibuf + row*256;
		 
		for (col=0;col<w;col++) {
			printf("%5d ", ip[0]);
			ip+=1;
		}
		printf("\n");
	}
}

 
 /*
 *process down the col
 * based on ibuf of 256 x 256
 * even samples 
*/
void hi_pass(int *ibuf,  int w, int h, int fwdinv) {
	int *ip,*x0,*x1;
	int row,col,dwt;		
	for (row=2;row<h;row+=2) {
		ip = ibuf + row*256;
		x0 = ibuf + (row-1)*256;
		x1 = ibuf + (row+1)*256;
		for (col=0;col<w;col++) {
			if(fwdinv == 1) {
				ip[0] = (ip[0] - ((x0[0]+x1[0])>>1));
			}
			else {
				ip[0] = (ip[0] + ((x0[0]+x1[0])>>1));
			}
 			ip+=1;
			x0+=1;
			x1+=1;
			
		}
	}
}

/*
 *process down the col
 * based on ibuf of 256 x 256
 * odd samples  
*/
void lo_pass(int *ibuf,  int w, int h, int fwdinv) {
	int *ip,*x0,*x1;
	int row,col,dwt;		
	for (row=1;row<h;row+=2) {
		ip = ibuf + row*256;
		x0 = ibuf + (row-1)*256;
		x1 = ibuf + (row+1)*256;		 
		for (col=0;col<w;col++) {
			if(fwdinv == 1) {
				ip[0] = (ip[0] + ((x0[0]+x1[0]+2)>>2));
			}
			else {
				ip[0] = (ip[0] - ((x0[0]+x1[0]+2)>>2));
			}
			ip+=1;
			x0+=1;
			x1+=1;
		}
	}
}

/*
 *process down the col
 * based on ibuf of 256 x 256
 * odd samples  
*/
void de_interleave(int *ibuf, int *obuf, int w, int h) {
	int *ip,*x0,*x1;
	int row,col,dwt;		
	for (row=0;row<h;row++) {
		//each time the row is incremented
		//ip is incremented to next row
		//ip starts at row 0
		ip = ibuf + row*256;
		//each time the row is incremented
		//x0 is increment by 1
		//each time the col is incremented
		//x0+=256; increments to next row
		x0 = obuf + row;
		x1 = x0 + 128/2;		 
		for (col=0;col<w;col++) {
			if(row % 2 == 0) {
				//printf("even %d %d %d\n",row,ip[0],x0[0]);
				x0[0] = ip[0];
			}
			
			else {
				//writes zeros to see where is writing
				//x0[0] = ip[0];
				x0[0] = 0;
			}
			//ip is giing across the row
			ip+=1;
			x0+=256;
			x1+=256;
		}
	}
}

int main(void) {
 	int m[8*8],bl[12*12],tmpbnk[12*12];
 	int *blptr,*tmpbnkptr;
 	int *img,*alt,*ip,*op;
 	int idx,idx1,idx2,w,h,row,col,fwdinv;
 		
 	FILE *ptr_myfile, *ofp;
	w = 256;
	h = 256;
	img = (int *)malloc(sizeof(int)*(w*h)*2);
	alt = &img[256*256];
	//ofp = fopen("img.bin","r");
	ofp = fopen("c2.bin","r");
	//ofp = fopen("c1.bin","r");
	fread(img, sizeof(int), w*h, ofp);
	fclose(ofp); 
	ofp = fopen("img.bin","w");
	fwrite(img, sizeof(int), w*h, ofp);
	fclose(ofp); 	   
	//w = 8;
	//h = 8;
	int arr[w][h],tp[w][h],passes,lvls;	
 
 	
 	extract(img,alt,w,h);
 	printf("extracted disp row as rows\n");	
 	disp(img,w,h);
 	printf("disp row as rows\n");
 	disp(alt,w,h);
 
 	printf("disp row as col\n");
 	disp1(alt,w,h);	
  	printf("\n");
  	for(lvls=0;lvls<3;lvls++) {
  	for(passes=0; passes<2;passes++) {
		printf("even samples hi pass fwd\n");
		printf("rows 2, 4, and 6\n");
		fwdinv = 1;
		hi_pass(alt,w,h,fwdinv);
		disp1(alt,w,h);
		/*	
		fwdinv = 0;
		printf("even samples hi pass inv\n");
		printf("rows 2, 4, and 6\n");	
		hi_pass(alt,w,h,fwdinv);
		disp1(alt,w,h);
		*/	
		printf("odd samples lo pass fwd\n");
		printf("rows 1, 3, 5 and 7\n");
		fwdinv = 1;
		lo_pass(alt,w,h,fwdinv);
		disp1(alt,w,h);	
		printf("\n");

  
		for(row=0;row<h;row++) {
			ip = alt + row*256;
			for(col=0;col<w;col++) {
				arr[row][col] = ip[0];
				ip+=1;
			}
		
		}
		printf("arr print \n");
		for(row=0;row<h;row++) {
		
			for(col=0;col<w;col++) {
				printf("%5d ",arr[row][col]);
			}
			printf("\n");
			
		
		}
		printf("arr de_interleave\n");
	
		for (row=0;row<h;row++) {
			for (col=0;col<w;col++) {
				if (row % 2 == 0) {
					tp[col][row/2] =  arr[row][col];
					printf("%5d ",tp[col][row/2]);
				}
				else {
					tp[col][row/2 + h/2] =  arr[row][col];
					printf("%5d ",tp[col][row/2 + h/2]);
				}
			
			}
			printf("\n");
		}
		printf("\n");
	
		for (row=0;row<h;row++) {
			for (col=0;col<w;col++) {
				arr[row][col] = tp[row][col];
			}
		}
		printf("arr print \n");
			for(row=0;row<h;row++) {
		
				for(col=0;col<w;col++) {
					printf("%5d ",arr[row][col]);
				}
			printf("\n");
			
		
		}
		for(row=0;row<h;row++) {
			ip = alt + row*256;
			for(col=0;col<w;col++) {
				ip[0] = arr[row][col];
				ip+=1;
			}
		
		}
	printf("fwd passes %d\n",passes);
	}
   	
	ofp = fopen("block.bin","w");
	fwrite(alt, sizeof(int), w*h, ofp);
	fclose(ofp); 
	}

  	for(lvls=0;lvls<3;lvls++) {
	for(passes=0; passes<2;passes++) {

		
		printf("arr print \n");
		for(row=0;row<h;row++) {
		
			for(col=0;col<w;col++) {
				printf("%5d ",arr[row][col]);
			}
			printf("\n");
			
		
		}
		printf("arr interleave\n");
		for(row=0;row<h;row++) {
			for(col=0;col<h;col++) {
				tp[row][col]= 0;
			}
		}
		for(col=0;col<w/2;col++) {
			for(row=0;row<h;row++) {
				tp[col*2][row] = arr[row][col];
				tp[col*2+1][row] = arr[row][col+w/2];
	
			}
		}
		for (row=0;row<h;row++) {
			for (col=0;col<w;col++) {
				arr[row][col] = tp[row][col];
			}
		}
		printf("arr print \n");
			for(row=0;row<h;row++) {
		
				for(col=0;col<w;col++) {
					printf("%5d ",arr[row][col]);
				}
			printf("\n");
			
		
		}
		for(row=0;row<h;row++) {
			ip = alt + row*256;
			for(col=0;col<w;col++) {
				ip[0] = arr[row][col];
				ip+=1;
			}
		}
		ofp = fopen("interleaveblk.bin","w");
		fwrite(alt, sizeof(int), w*h, ofp);
		fclose(ofp);
		printf("odd samples lo pass inv\n");
		printf("rows 1, 3, 5 and 7\n"); 	
		fwdinv = 0;
		lo_pass(alt,w,h,fwdinv);
		disp1(alt,w,h);	
		printf("\n");
		fwdinv = 0;
		printf("even samples hi pass inv\n");
		printf("using disp not disp1\n");	
		hi_pass(alt,w,h,fwdinv);
		disp(alt,w,h);
		printf("even samples hi pass inv\n");
		printf("using disp1\n");
		disp1(alt,w,h);
		ofp = fopen("invblock.bin","w");
		fwrite(alt, sizeof(int), w*h, ofp);
		fclose(ofp);
		
		}
	}
		
	 	
	free (img);
 


 }
