#include <stdio.h>
#ifdef __ZIPCPU__
void free(void *);
#else
#include <stdlib.h>
#endif

/*
generated data
0  1  2  3  4  5  6  7  
8  9  10  11  12  13  14  15  
16  17  18  19  20  21  22  23  
24  25  26  27  28  29  30  31  
32  33  34  35  36  37  38  39  
40  41  42  43  44  45  46  47  
48  49  50  51  52  53  54  55  
56  57  58  59  60  61  62  63  
deinterleaved data
0  16  32  48  8  24  40  56  
1  17  33  49  9  25  41  57  
2  18  34  50  10  26  42  58  
3  19  35  51  11  27  43  59  
4  20  36  52  12  28  44  60  
5  21  37  53  13  29  45  61  
6  22  38  54  14  30  46  62  
7  23  39  55  15  31  47  63  

0  2  4  6  1  3  5  7  
16  18  20  22  17  19  21  23  
32  34  36  38  33  35  37  39  
48  50  52  54  49  51  53  55  
8  10  12  14  9  11  13  15  
24  26  28  30  25  27  29  31  
40  42  44  46  41  43  45  47  
56  58  60  62  57  59  61  63  

lower to upper 

9 25 41 57 
11 27 43 59 
13 29 45 61 
15 31 47 63
*/

void de_interleave(int *ptr) 
{
int row,col,w,h,r2,r2h;	
w = 16;
h = 16;
int tar[w][h];
//save ptr to initial value passed into subroutine
//so it can be restored 
int *init_ptr;
init_ptr = ptr;

//create an empty array the size of the src array
for(row=0;row<h;row++)
{
	for(col=0;col<w;col++)
	{
		tar[row][col] = 0;
	}
}
//transfer the src array to the tmp array		
for(row=0;row<h;row++)
{
	for(col=0;col<w;col++)
	{
	   //printf("%d",tar[col][row]);
	   if (row % 2 == 0)
	   {
		   r2 = row/   2;
		   tar[col][r2] = *ptr++; 
	   }	 
	   else {
		   r2h= (((row/2)+(h/2)));
		   tar[col][r2h] = *ptr++;
       }	   	   
    }
}
//restore ptr to initial value passed into subroutine
ptr = init_ptr;
//transfer the tmp array to the src arrray
for(row=0;row<h;row++)
{
	for(col=0;col<w;col++)
	{
		*ptr++ = tar[row][col];
		 
    }
}
} 


void lower_upper(int *ptr) 
{
int row,col,w,h,r2,r2h;	
w = 16;
h = 16;
int tar[w][h];
//save ptr to initial value passed into subroutine
//so it can be restored 
int *init_ptr;
init_ptr = ptr;
int sar[w][h];
//transfer ptr to sar
//printf("\n");
for(row=0;row<h;row++)
{
	for(col=0;col<w;col++)
	{
       sar[row][col] = *ptr++;
    }
}
//create an empty array the size of the src array

for(row=0;row<h;row++)
{
	for(col=0;col<w;col++)
	{
		tar[row][col] = 0;
	}
}

//col row
//temp_bank[col-width/2][row-height/2] = s[row][col]
printf("\n");
printf("lower to upper \n");
printf("\n");
for(col=w/2;col<w;col++)
{
	for(row=h/2;row< h;row++)
	{
		tar[col-w/2][row-h/2] = sar[row][col];
		printf("%d ",tar[col-w/2][row-h/2]); 
	}
	printf("\n");
}
for(row=0;row<h;row++)
{
	for(col=0;col<w;col++)
	{
		sar[row][col] = tar[col][row];
	}
}
}

void lift_step(int *ptr) 
{
int row,col,w,h,r2,r2h;	
w = 16;
h = 16;
int tar[w][h];
//save ptr to initial value passed into subroutine
//so it can be restored 
int *init_ptr;
init_ptr = ptr;
int sar[w][h];
//transfer ptr to sar
//printf("\n");
printf("in lift step\n");
for(row=0;row<h;row++)
{
	for(col=0;col<w;col++)
	{
       sar[row][col] = *ptr++;
       printf(" %d ", sar[row][col]);
    }
    printf("\n");
}
for(col=0;col<w;col++)
{
	for(row=2;row<h-1;row=row+2)
	{
		sar[row][col] = sar[row][col] - ((sar[row-1][col] + sar[row+1][col])>>1);
		printf(" %d ", sar[row][col]); 
    }
    
    for(row=1;row<h-1;row=row+2)
	{
		sar[row][col] = sar[row][col] + ((sar[row-1][col] + sar[row+1][col] + 2)>>2);
		printf(" %d ", sar[row][col]);
    }
    printf("\n");
} 
ptr = init_ptr;
//transfer the tmp array to the src arrray
for(row=0;row<h;row++)
{
	for(col=0;col<w;col++)
	{
		*ptr++ = sar[row][col];
		 
    }
}  
}
void inv_lift_step(int *ptr) 
{
int row,col,w,h,r2,r2h;	
w = 16;
h = 16;
int tar[w][h];
//save ptr to initial value passed into subroutine
//so it can be restored 
int *init_ptr;
init_ptr = ptr;
int sar[w][h];
//transfer ptr to sar
//printf("\n");
printf("in inv_lift step\n");
for(row=0;row<h;row++)
{
	for(col=0;col<w;col++)
	{
       sar[row][col] = *ptr++;
       printf(" %d ", sar[row][col]);
    }
    printf("\n");
}
for(col=0;col<w;col++)
{
	for(row=1;row<h-1;row=row+2)
	{
		sar[row][col] = sar[row][col] + ((sar[row-1][col] + sar[row+1][col])>>1);
		printf(" %d ", sar[row][col]); 
    }
    
    for(row=2;row<h;row=row+2)
	{
		sar[row][col] = sar[row][col] - ((sar[row-1][col] + sar[row+1][col] + 2)>>2);
		printf(" %d ", sar[row][col]);
    }
    printf("\n");
} 
ptr = init_ptr;
//transfer the tmp array to the src arrray
for(row=0;row<h;row++)
{
	for(col=0;col<w;col++)
	{
		*ptr++ = sar[row][col];
		 
    }
}  
}
int main()
{
	const int bb = 0x1ff;
    const int gg = 0x7fc00;
    const int rr = 0x1ff00000;
//read RGB data from file 
 	
int i,ii0,ii1,ii2,val;
int *buf;
int xx[65536];
buf = (int *)&xx[0];	
struct rec
	{
	char raw_buf[3];
};
struct rec my_record;
//struct results my_results;
FILE *ptr_myfile;
ptr_myfile=fopen("rgb.bin","rb");
if (!ptr_myfile)
{
 	printf("Unle to open file!");
	return 1;
} 

for (i= 0;i<65536;i++) {
fread(&my_record,sizeof(struct rec),1,ptr_myfile);
ii0 = (int)my_record.raw_buf[0];
ii1 = (int)my_record.raw_buf[1];
ii2 = (int)my_record.raw_buf[2];
val = ii0<<20|ii1<<10|ii2;
*buf++=val;
//printf("%d %x %x %x %x \n",i,ii0,ii1,ii2,val);

}
fclose(ptr_myfile);

int *sptr, *sptr1, *dptr;

int row,col,cc;
int w,h,r2,r2h,red,green,blue;
w = 16;
h = 16;
int sar[w][h];
int tar[w][h];

sptr = malloc(sizeof(int)*(w*h));
sptr1 = &sar[0][0]; 
dptr = malloc(sizeof(int)*(w*h));
//printf("%x %x %x\n",sptr,sptr1,dptr);
cc = 0;

buf = (int *)&xx[0];
//printf("buf %x \n",buf);
for(row=0;row<h;row++)
{
	for(col=0;col<w;col++)
	{
	    //blue = *buf&bb;
	    //sar[row][col] = blue;
	    //red = (*buf&rr)>>20;
		//sar[row][col] = red;
	    green = (*buf&gg)>>10;
		sar[row][col] = green;		
		//*buf = blue;
		//printf("%d ",sar[row][col]);
		//starts at 0 to 15
		buf++;
	}
	buf = buf + 240;
	//printf(" %x \n",buf);
}
buf = (int *)&xx[0];
printf("\n");
lift_step(sptr1);
//inv_lift_step(sptr1);

de_interleave(sptr1);

 	
printf("deinterleaved data\n");
for(row=0;row<h;row++)
{
	for(col=0;col<w;col++)
	{ 
	   printf("%d  ",sar[row][col]);
	}
	printf("\n");
}
printf("\n");
lift_step(sptr1);
de_interleave(sptr1);

printf("\n");
printf("deinterleaved data\n");
for(row=0;row<h;row++)
{
	for(col=0;col<w;col++)
	{ 
	   printf("%d  ",sar[row][col]);
	}
	printf("\n");
}

lower_upper(sptr1);
/*
w = w/2;
h = h/2;	
printf("\n");
for(row=0;row<h;row++)
{
	for(col=0;col<w;col++)
	{ 
	   printf("%d  ",sar[row][col]);
	}
	printf("\n");
}
*/ 		   	
free ((int*)*sptr);

free ((int*)*dptr);
}
/*
printf("generated data\n");
for(row=0;row<h;row++)
{
	for(col=0;col<w;col++)
	{
	   sar[row][col] = cc;
	   printf("%d  ",sar[row][col]);
       cc++;
    }
    printf("\n");
}
*/ 
