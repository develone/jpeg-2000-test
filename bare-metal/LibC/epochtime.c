	#include <stdio.h>
	#include <sys/time.h>
int sam, lf, rh, dwt;
int fwd;
struct timeval currentTime;
long start_sec;
long end_sec;	
int i;
int lift(int sam, int lf, int rh, int fwd) 
{
	if (fwd==7) 
		dwt = sam - ((lf + rh) >> 1);
	else if (fwd==5)
		 dwt = sam + ((lf + rh) >> 1);
	else if (fwd==6)
		dwt = sam + ((lf + rh + 2) >> 2);
	else 
		dwt = sam - ((lf + rh + 2 ) >> 2);

	return dwt;
}	
void main(void) {
 
	
	gettimeofday(&currentTime, NULL);
	 
	start_sec = currentTime.tv_sec;
	printf("time sec %ld\n", currentTime.tv_sec);
	for(i = 0;i < 1e9; i++) {
		sam = 164;
		lf = 156; 
		rh = 160;
		fwd = 7;
		dwt = lift(sam, lf, rh, fwd); 
	}
	gettimeofday(&currentTime, NULL);
	end_sec = currentTime.tv_sec;
 	
      
	printf("start time in sec %ld end time in sec %ld 1e9 dwt processing time %ld\n", start_sec, end_sec,(end_sec - start_sec) );

}
