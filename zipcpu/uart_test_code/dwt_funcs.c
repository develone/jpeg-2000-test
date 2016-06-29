
#include "dwt_funcs.h"

#ifdef __ZIPCPU__
void free(void *);
typedef int int32;
#else
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#endif
void de_interleave(int *ptr, int w, int h) 
{
int row,col,r2,r2h;	
 
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


void lower_upper(int *ptr, int w, int h) 
{
int row,col,r2,r2h;	
 
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
//printf("\n");
//printf("lower to upper \n");
//printf("\n");
for(col=w/2;col<w;col++)
{
	for(row=h/2;row< h;row++)
	{
		tar[col-w/2][row-h/2] = sar[row][col];
		//printf("%d ",tar[col-w/2][row-h/2]); 
	}
	//printf("\n");
}
//printf("\n");
//restore ptr to initial value passed into subroutine
ptr = init_ptr;
//transfer the tmp array to the src arrray
for(row=0;row<h;row++)
{
	for(col=0;col<w;col++)
	{
		*ptr++ = tar[row][col];
		//sar[row][col] = tar[col][row];
		//printf("%d ",sar[row][col]);
	}
	//printf("\n");
}
}

void lift_step(int *ptr, int w, int h) 
{
int row,col,r2,r2h;	
 
int tar[w][h];
//save ptr to initial value passed into subroutine
//so it can be restored 
int *init_ptr;
init_ptr = ptr;
int sar[w][h];
//transfer ptr to sar
//printf("\n");
//printf("in lift step\n");
for(row=0;row<h;row++)
{
	for(col=0;col<w;col++)
	{
       sar[row][col] = *ptr++;
       //printf(" %d ", sar[row][col]);
    }
    //printf("\n");
}
for(col=0;col<w;col++)
{
	for(row=2;row<h-1;row=row+2)
	{
		sar[row][col] = sar[row][col] - ((sar[row-1][col] + sar[row+1][col])>>1);
		//printf(" %d ", sar[row][col]); 
    }
    
    for(row=1;row<h-1;row=row+2)
	{
		sar[row][col] = sar[row][col] + ((sar[row-1][col] + sar[row+1][col] + 2)>>2);
		//printf(" %d ", sar[row][col]);
    }
    //printf("\n");
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
void inv_lift_step(int *ptr, int w, int h) 
{
int row,col,r2,r2h;	
 
int tar[w][h];
//save ptr to initial value passed into subroutine
//so it can be restored 
int *init_ptr;
init_ptr = ptr;
int sar[w][h];
//transfer ptr to sar
//printf("\n");
//printf("in inv_lift step\n");
for(row=0;row<h;row++)
{
	for(col=0;col<w;col++)
	{
       sar[row][col] = *ptr++;
       //printf(" %d ", sar[row][col]);
    }
    //printf("\n");
}
for(col=0;col<w;col++)
{
	for(row=1;row<h-1;row=row+2)
	{
		sar[row][col] = sar[row][col] + ((sar[row-1][col] + sar[row+1][col])>>1);
		//printf(" %d ", sar[row][col]); 
    }
    
    for(row=2;row<h;row=row+2)
	{
		sar[row][col] = sar[row][col] - ((sar[row-1][col] + sar[row+1][col] + 2)>>2);
		//printf(" %d ", sar[row][col]);
    }
    //printf("\n");
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
/*
def upper_lower(s, width, height):

	temp_bank = [[0]*width for i in range(height)]
	for col in range(width/2):

		for row in range(height/2):

			temp_bank[col+width/2][row+height/2] = s[row][col]

	for row in range(width):
		for col in range(height):
			s[row][col] = temp_bank[col][row]
	return s
*/
void upper_lower(int *ptr, int w, int h) 
{
int row,col,r2,r2h;	
 
 
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
       //printf(" %d ",sar[row][col]); 
    }
    //printf("\n");
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

//printf("\n");
//printf("upper to lower \n");
//printf("\n");
for(col=0;col<w/2;col++)
{
	for(row=0;row< h/2;row++)
	{
		tar[col+w/2][row+h/2] = sar[row][col];
		//printf("%d ",tar[col+w/2][row+h/2]); 
	}
	//printf("\n");
}
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
