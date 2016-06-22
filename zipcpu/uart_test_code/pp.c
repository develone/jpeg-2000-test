#include "board.h"

#define NUM_ARRAYS     256
#define NUM_ELEMENTS   256
#define INVALID_VAL   -1
struct transfer {
	int **ptr;
	int *row;
};	
void pp(int *imgbuf, int*tmpbuf) {
   struct transfer tmp;
   struct transfer src;	
   int index            = INVALID_VAL;
   int array_index      = INVALID_VAL;
   int *limgbuf;
   
   unsigned  int w,h,r2,r2h;
   w = 256;
   h = 256;
   /*
    * src 0x800000
    * tmp 0x820000
    */ 
   tmp.ptr = tmpbuf;
   src.ptr = imgbuf;
   limgbuf = 0x820000;
   /* prepare the row pointers for tmp */ 
   for (index = 0; index<NUM_ELEMENTS; index++)
   {    
   *(tmp.ptr +index) = (int *)0x820000+index*NUM_ELEMENTS;
   } 
   
   /* prepare the tmp array setting all values to zero*/
   for (index=0; index<NUM_ARRAYS; index++)
   {
      for (array_index = 0; array_index<NUM_ELEMENTS; array_index++)
      {
         *(*(tmp.ptr+index)+array_index) = 0 ;    
      }
   }   
  /* Fill Elements Into This 2-D Array tmp
   * with values pointed by imgbuf
   * rows transposed to cols
   * row  outer loop col inner loop
   */
   for (index=0; index<NUM_ARRAYS; index++)
   {
      for (array_index = 0; array_index<NUM_ELEMENTS; array_index++)
      {
		 if (index % 2 == 0)
		 {
			 //even
			 r2 = index/2;
			 *(*(tmp.ptr+r2)+array_index) = *imgbuf;
	     }  	  
	     else
	     {
		     //odd
		     r2h = index/2 + h/2;
		     *(*(tmp.ptr+r2h)+array_index) = *imgbuf;
         }
         /*incremet the imgbuf to next col */
         *imgbuf++ ; 
          
      }
      /*incremet the imgbuf to next row */
      *imgbuf = *(imgbuf + NUM_ELEMENTS);
   }
   /* prepare the row pointers for src */ 
   for (index = 0; index<NUM_ELEMENTS; index++)
   {    
   *(src.ptr +index) = (int *)0x800000+index*NUM_ELEMENTS;
   } 
  /* Fill Elements Into This 2-D Array src
   * with values pointed by tmp
   * row  outer loop col inner loop
   */
   for (index=0; index<NUM_ARRAYS; index++)
   {
      for (array_index = 0; array_index<NUM_ELEMENTS; array_index++)
      {
		 *(*(src.ptr+index)+array_index) = *limgbuf;
         /*incremet the imgbuf to next col */
         *limgbuf++ ; 
          
      }
      /*incremet the imgbuf to next row */
      *limgbuf = *(limgbuf + NUM_ELEMENTS);
   }
 
}
