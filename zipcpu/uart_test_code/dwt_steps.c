#include "board.h" 

void dwt_steps(void) {
	 

	 

	// Let's set ourselves up for 9600 baud, 8-bit characters, no parity,
	// and one stop bit.
	 

	int *buf_ptr = (int *)0x800000;
	//int *img_ptr1 = (int *)0x810000, p;
	int col,row,dum1_r,dum1_g, dum1_b;
	int dum2_r,dum2_g, dum2_b,dum3_r,dum3_g, dum3_b;
	int dum4,dum5,dum6,*dum7;
	int dum1,dum2,dum3;
	int w,h;
	w = 256;
	h = 256;
	
	
    
	//for ( p =0; p < 2; p++) {	
	for (col = 0; col< w;col++) { 
		//even samples
		for (int row = 2;row<256;row=row+2) { 
			 dum1_r = *(buf_ptr+col+row*256)>>20;
			 dum1_g = *(buf_ptr+col+row*256);
			 dum1_b = *(buf_ptr+col+row*256)&0x2ff;
			 dum2_r = *(buf_ptr+col+(row-1)*256)>>20;
			 dum2_g = *(buf_ptr+col+(row-1)*256);
			 dum2_b = *(buf_ptr+col+(row-1)*256)&0x2ff;
			 dum3_r = *(buf_ptr+col+(row+1)*256)>>20;
			 dum3_g = *(buf_ptr+col+(row+1)*256);
			 dum3_b = *(buf_ptr+col+(row+1)*256)&0x2ff;
			 dum4 = ((dum2 + dum3) >> 1);
			 
			 dum5 = *(buf_ptr+col+row*256);
			 dum6 = dum5 - dum4;
			 dum7 = buf_ptr;
 			 
		}
        //odd samples
		for (row = 1;row<h-2;row=row+2) { 
			 dum1 = *(buf_ptr+col+row*256);
			 dum2 = *(buf_ptr+col+(row-1)*256);
			 dum3 = *(buf_ptr+col+(row+1)*256);
			 dum4 = ((dum2 + dum3) >> 2);
			 
			 dum5 = *(buf_ptr+col+row*256);
			 dum6 = dum5 + dum4;
			 dum7 = buf_ptr;
 			 
		} 
	}
    
 
 
}

