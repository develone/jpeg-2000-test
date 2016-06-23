#include <stdio.h>
#include <stdlib.h>

#define NUM_ARRAYS     8
#define NUM_ELEMENTS   8
#define INVALID_VAL   -1

int main()
{
   int index            = INVALID_VAL;
   int array_index      = INVALID_VAL;
   int **ptr            = NULL;
   int cc = 0; 
   ptr = malloc(sizeof(int*)*NUM_ARRAYS);
   //printf("%d %x \n",sizeof(int*)*NUM_ARRAYS,ptr);
   if (!ptr)
   {
      printf ("\nMemory Allocation Failure !\n\n");
      exit (EXIT_FAILURE);
   }

   for (index=0; index<NUM_ARRAYS; index++)
   {
      *(ptr+index) = malloc(sizeof(int)*NUM_ELEMENTS);
      //printf("%x \n",*(ptr+index));

      if (!*(ptr+index))
      {
         printf ("\nMemory Allocation Failure !\n");
         exit (EXIT_FAILURE);
      }
   }
  /* Fill Elements Into This 2-D Array */
   for (index=0; index<NUM_ARRAYS; index++)
   {
      for (array_index = 0; array_index<NUM_ELEMENTS; array_index++)
      {
        // *(*(ptr+index)+array_index) = (array_index+1)*(index+1);
        *(*(ptr+index)+array_index) = cc++ ;
      }
   }

   /* Print Array Elements */
   for (index = 0; index<NUM_ARRAYS; index++)
   {
      printf ("\nArray %d Elements:\n", index);
      for (array_index = 0; array_index<NUM_ELEMENTS; array_index++)
      {
         printf (" %d ", *(*(ptr+index)+array_index));
      }
      printf ("\n\n");
   }

   return 0;
}
