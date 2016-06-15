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
int main(int argc, char * argv[]) {
int xx[65536];
int i;
 
printf("%x  \n", &xx[0]);
printf("%x \n", &xx[256]);
printf("%d \n", &xx[256] - &xx[0]); 
return 0;
}
