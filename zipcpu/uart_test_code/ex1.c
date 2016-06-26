#include <stdio.h>
#include <stdlib.h>
/*
row0 0 1 2 3
row1 4 5 6 7
row2 8 9 10 11
row3 12 13 14 15

1st row 1st col
3rd row 2nd col
2nd row 3rd col
3rd row 4th col

row0 0  8 4 12
row1 1  9 5 13
row2 2 10 6 14
row3 3  11 7 15 
*/

void interleave(int sar[4][4]) 
{
int row,col,w,h,r2,r2h;	
w = 4;
h = 4;
int tar[w][h];

printf("%d %d\n",&sar,sizeof(sar));
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
		   r2 = row/2;
		   tar[col][r2] = sar[row][col]; 
	   }	 
	   else {
		   r2h= (((row/2)+(h/2)));
		   tar[col][r2h] = sar[row][col];
       }	   	   
    }
}
//transfer the tmp array to the src arrray
for(row=0;row<h;row++)
{
	for(col=0;col<w;col++)
	{
		sar[row][col]= tar[row][col]; 
    }
}
} 
int main()
{

 
int *sptr, *sptr1, *dptr;

int row,col,cc;
int w,h,r2,r2h;
w = 4;
h = 4;
int sar[w][h];
int tar[w][h];

sptr = malloc(sizeof(int)*(w*h));
sptr1 = sptr; 
dptr = malloc(sizeof(int)*(w*h));
printf("%x %x %x\n",sptr,sptr1,dptr);
cc = 0;

for(row=0;row<h;row++)
{
	for(col=0;col<w;col++)
	{
	   sar[row][col] = cc;
	   printf("%d",sar[row][col]);
	   printf(" row %d col %d \n", row,col);
	   cc++;
    }
}
interleave(sar);
 	
printf("\n");
for(row=0;row<h;row++)
{
	for(col=0;col<w;col++)
	{ 
	   printf("%d",sar[row][col]);
	   printf(" row %d col %d \n", row,col);
	}
}	   	
free ((int*)*sptr);

free ((int*)*dptr);
}
