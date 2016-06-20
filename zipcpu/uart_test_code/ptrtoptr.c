#include <stdio.h>
#include <stdlib.h>

#define NUM_ARRAYS     4
#define NUM_ELEMENTS   4
#define INVALID_VAL   -1

int main()
{
   int index            = INVALID_VAL;
   int array_index      = INVALID_VAL;
   int **ptr            = NULL;

   ptr = malloc(sizeof(int*)*NUM_ARRAYS);
    
   if (!ptr)
   {
      printf ("\nMemory Allocation Failure !\n\n");
      exit (EXIT_FAILURE);
   }

   for (index=0; index<NUM_ARRAYS; index++)
   {
      *(ptr+index) = malloc(sizeof(int)*NUM_ELEMENTS);

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
         *(*(ptr+index)+array_index) = (array_index+1)*(index+1);
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
