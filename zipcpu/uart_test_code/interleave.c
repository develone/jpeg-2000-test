#include <stdio.h>
/*
def de_interleave(s,height,width):
	# de-interleave
	temp_bank = [[0]*width for i in range(height)]
	for row in range(width):
		for col in range(width):
            # k1 and k2 scale the vals
            # simultaneously transpose the matrix when deinterleaving
			if row % 2 == 0:

				temp_bank[col][row/2] =  s[row][col]
			else:

				temp_bank[col][row/2 + height/2] =  s[row][col]
    # write temp_bank to s:
	for row in range(width):
		for col in range(height):
			s[row][col] = temp_bank[row][col]
	return s
*/

const int * pixel = image + w * y  +  x;
void interleave(int *imgbuf)
{
	int col,row,offset;
	int w,h,x,y;
	w = 256;
	h = 256;
	x = 256;
	y = 256;
	int *image;
	//const int *pixel = image + w * y  +  x;
	
	for (row=0;row<h;row++){
		for(col=0;col<w;col++) {
			offset = col+(row)*256;
			//imgbuf = (int *)(*imgbuf + offset);
			//printf("%d %d %d %x\n",row,col,offset,imgbuf);
			//printf("%d %d %d \n",row,col,offset);
			printf("%d %d %d\n",row,col,offset);
			if (row %2 == 0)
			   printf("even\n");
			else
			   printf("odd\n");
		}
	}

}	
int main(int argc, char * argv[]) {
	int *buf;
	//*buf = (int *)0x800000;
int xx[65536];
buf = (int *)&xx;
int i;
int col,row;
int w,h;
w = 256;
h = 256;
/* 
printf("%x  \n", &xx[0]);
printf("%x \n", &xx[256]);
printf("%d \n", &xx[256] - &xx[0]);
*/
interleave(buf); 
return 0;
}
