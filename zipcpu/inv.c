#include<stdio.h>
#include <stdlib.h> 
#include <string.h> 
	
void inv_lift(int buf[],int num_passes, int interleave ) {
int row,col,w,h;
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
	  
   	 w = 256;
   	 h = 256;
	 char *inpfn,*outfn; 
	 //int buf[];
	 int buf1[w*h];
	 //int *buf_ptr;
	 int p;
     //&buf = buf_ptr;
    //zero the the buf1 array
	for (col = 0; col<w*h;col++) {
		buf1[col] = 0;
	}
/*
upper left corner to lower right corner 
*/
for ( col = 0; col < w/2 ;col++) {
	for (row = 0; row < h/2;row++) {
 
		buf1[256*(col+w/2)+ (row+h/2)] = buf[256*row+col];
	}
}

for ( row = 0;row < h-2;row++) {
	for (col = 0;col < w;col++) {
 
		buf[256*col+row] = buf1[256*row+col];
	}
}
exit;
for ( p =0; p < num_passes; p++) {
	
	printf("%d\n",p);
	for ( col = 0; col<w;col++) { 
		for (row = 1;row<h-2;row=row+2) {
			  
	             buf[(row*256)+col] = buf[(row*256)+col] - (( buf[((row-1)*256)+col] + buf[((row+1)*256)+col] + 2) >> 2);

		}
		//end of odd samples
		for (row = 2;row<h;row=row+2) { 
			  
             buf[(row*256)+col] = buf[(row*256)+col] + (( buf[((row-1)*256)+col] + buf[((row+1)*256)+col] ) >> 1); 
		}
		//end of even samples
	}    

    //de_interleave 
    if ( interleave == 1) {
 
	//zero the the buf1 array
	for (col = 0; col<w*h;col++) {
		buf1[col] = 0;
	}
	for ( row = 0 ; row < h; row++) {
		for (col = 0; col < w;col++) {  
			if (row % 2 == 0) {
				  
				buf1[(row/2)+256*col] =  buf[(row*256)+col];
			}	
			else {
				 
				 buf1[col*256+(row/2 + 256/2)] =  buf[(row)*256+col];
			}	
		}
	}
	for ( row = 0;row < h-2;row++) {
		for (col = 0;col < w;col++) {
			 
			buf[(row)*256+col] = buf1[(row)*256+col];
		}
	}
    }
    else {
    }
 
}
//end num_passes loop
 
	//zero the the buf1 array
	for (col = 0; col<w*h;col++) {
		buf1[col] = 0;
	}
/*
lower right corner to upper left corner
*/
for ( col = w/2; col < w ;col++) {
	for (row = h/2; row < h;row++) {
 
		buf1[256*(col-w/2)+ (row-h/2)] = buf[256*row+col];
	}
}
/*
transfer buf1 array to buf array for output
*/
for ( row = 0;row < h-2;row++) {
	for (col = 0;col < w;col++) {
 
		buf[256*col+row] = buf1[256*row+col];
	}
}

            
 	
}
	


