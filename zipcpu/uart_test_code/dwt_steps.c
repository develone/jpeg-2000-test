#include "board.h" 

void dwt_steps(void) {
	 

	 

 
	 
    const int LED_ON_DWT = 0x10001;
    const int LED_OFF_DWT = 0x10000;  
	int *buf_ptr = (int *)0x800000;
	int *img_ptr1 = (int *)0x830000;
	
	int *array_ptr;
	
	 	
	int col,row,dum1_r,dum1_g, dum1_b,dum1_l;
	int dum2_r,dum2_g, dum2_b,dum2_l,dum3_r,dum3_g, dum3_b,dum3_l;
	int dum4,dum5,dum6,*dum7;
	int dum1,dum2,dum3;
	int w,h;
	w = 256;
	h = 256;
	
	//turn on the red led on gpio <0>
	sys -> io_gpio = LED_ON_DWT;
    
	//for ( p =0; p < 2; p++) {	
	for (col = 0; col< w;col++) { 
		//even samples
		for (int row = 2;row<256;row=row+2) { 
                         //extracting red to dum1_r, dum1_g, and dum1_b
                         //bits 32-20 are red
             /*            
			 dum1_r = *(buf_ptr+col+(row-1)*256)>>20;
			 dum1_g = (*(buf_ptr+col+(row-1)*256)&0xffc00)>>10;
			 dum1_b = *(buf_ptr+col+(row-1)*256)&0x2ff;
			 */
			  
			 dum1_r = *(buf_ptr+col+(row-1)*256);
			 dum1_g = *(buf_ptr+col+(row-1)*256);
			 dum1_b = *(buf_ptr+col+(row-1)*256);
                         //extracting green to dum2_r, dum2_g, and dum2_b
                         //bits 19-11 are green
             /*            
			 dum2_r = *(buf_ptr+col+(row)*256)>>20;
			 dum2_g = (*(buf_ptr+col+row)*256)&0xffc00)>>10;
			 dum2_b = *(buf_ptr+col+(row)*256)&0x2ff;
             */
             dum2_r = *(buf_ptr+col+(row)*256);
			 dum2_g = *(buf_ptr+col+(row)*256);
			 dum2_b = *(buf_ptr+col+(row)*256);
                         //extracting blue to dum3_r, dum3_g, and dum3_b
                         //bits 10-0 are blue
             /*            
             dum3_r = *(buf_ptr+col+(row+1)*256)>>20;
			 dum3_g = (*(buf_ptr+col+row+1)*256)&0xffc00)>>10;
			 dum3_b = *(buf_ptr+col+(row+1)*256)&0x2ff;
			 */ 	
             dum3_r = *(buf_ptr+col+(row+1)*256);
			 dum3_g = *(buf_ptr+col+(row+1)*256);
			 dum3_b = *(buf_ptr+col+(row+1)*256);	
			 dum1_l = ((dum1_r + dum3_r) >> 1);
			 dum1_l = dum2_r - dum1_l;

			 dum2_l = ((dum2_g + dum3_g) >> 1);
			 dum2_l = dum2_r - dum2_l;

			 dum3_l = ((dum2_g + dum3_g) >> 1);
			 dum3_l = dum3_r - dum3_l;

			 dum5 = *(buf_ptr+col+row*256);
			 dum6 = dum5 - dum4;
			 dum7 = buf_ptr;
			 if (row == 0) {
				 *img_ptr1++ = dum1_r;
				 *img_ptr1++ = dum2_r;
				 *img_ptr1++ = dum3_r;
			 }
 			 
		}
        //odd samples
        /*
		for (row = 1;row<h-2;row=row+2) { 
			 dum1 = *(buf_ptr+col+row*256);
			 dum2 = *(buf_ptr+col+(row-1)*256);
			 dum3 = *(buf_ptr+col+(row+1)*256);
			 dum4 = ((dum2 + dum3) >> 2);
			 
			 dum5 = *(buf_ptr+col+row*256);
			 dum6 = dum5 + dum4;
			 dum7 = buf_ptr;
 			 
		}
		*/
		//sys -> io_gpio = LED_OFF_DWT;  
	}
    
 
 
}

