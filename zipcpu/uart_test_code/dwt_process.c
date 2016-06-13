#include "board.h"
int twos_comp(int lsr) {
	if (lsr > 256) {
		return lsr - 512;
	}
	else { 
	    return lsr;
    }	
}
void dwt_process(char *imgbuf) {
	int r_l;
	int g_l;
	int b_l;
	int s_sh_r;
	int s_sh_g;
	int s_sh_b;
	int l;
	int s;
	int r;
	int dwt_b;
	int dwt_g;
	int dwt_r;
    const int LED_ON_DWT = 0x10001;
    const int LED_OFF_DWT = 0x10000;	
    const int bb = 0x3ff;
    const int gg = 0xffc00;
    const int rr = 0x3ff00000;
    int i,v;
    //location to store test result
    char *st_test_ptr = (char *)0x820000; 
    //turn on the red led off gpio <0>
	sys -> io_gpio = LED_ON_DWT;
    char *buf_l;
    char *buf_r;
    char *buf_s;
    //printf("sub ptr to xx %x\n",imgbuf);
    *imgbuf++;
    //setting imgbuf even sample minus 1
    buf_l = imgbuf;
    *imgbuf++;
    buf_s = imgbuf;
	*imgbuf++;
	//setting imgbuf even sample plus 1
	buf_r = imgbuf;
	//setting imgbuf even sample
	 *imgbuf--;
	    
 
	
	for(i = 2; i < 8; i=i+2) {
		//printf("%d ptr %x %x %x %x %x\n",i,buf_l,*buf_l,*buf_l&rr,*buf_l&gg, *buf_l&bb);
	    //printf("%d ptr %x %x %x %x %x\n",i,buf_s,*buf_s,*buf_s&rr,*buf_s&gg, *buf_s&bb);
	    //printf("%d ptr %x %x %x %x %x\n",i,buf_r,*buf_r,*buf_r&rr,*buf_r&gg, *buf_r&bb);
 
	    v = 0;
	    l = (*buf_l&rr)>>20;
	    s = (*buf_s&rr)>>20;
	    r = (*buf_r&rr)>>20;
	    l = twos_comp(l);
	    s = twos_comp(s);
	    r = twos_comp(r);	    
	    dwt_r = s -((l+r)>>1);
	    //v |= (twos_comp(dwt_r&0x1ff)<<20);
	    
	    l = (*buf_l&gg)>>10;
	    s = (*buf_s&gg)>>10;
	    r = (*buf_r&gg)>>10;
	    l = twos_comp(l);
	    s = twos_comp(s);
	    r = twos_comp(r);	    
	    dwt_g = s -((l+r)>>1);
	    v |= (twos_comp(dwt_g&0x1ff)<<10)&gg;
	        	    
	 	l = *buf_l&bb;
	    s = *buf_s&bb;
	    r = *buf_r&bb;
	    l = twos_comp(l);
	    s = twos_comp(s);
	    r = twos_comp(r);
	    dwt_b = s -((l+r)>>1);
	    
	    //v |= (twos_comp(dwt_b&0x1ff))&bb;
	    
        
	    *st_test_ptr++ = v; 	
	    //*buf_s = v;
	    //printf("%d ptr %x %x %x %x %x\n",i,buf_s,*buf_s,*buf_s&rr,*buf_s&gg, *buf_s&bb);    
	    buf_l++;
	    buf_s++;
	    buf_r++;
   }
   /*
    //printf("sub ptr to xx %x\n",imgbuf);
    *imgbuf--;
    *imgbuf--; // setting to zero
    //setting imgbuf sple minus 1
    buf_l = imgbuf;
    *imgbuf++;
    buf_s = imgbuf;
	*imgbuf++;
	//setting imgbuf sple plus 1
	buf_r = imgbuf;
	//setting imgbuf sple
	 *imgbuf--;
	for(i = 1; i < 1; i=i+2) {
		//printf("%d ptr %x %x %x %x %x\n",i,buf_l,*buf_l,*buf_l&rr,*buf_l&gg, *buf_l&bb);
	    //printf("%d ptr %x %x %x %x %x\n",i,buf_s,*buf_s,*buf_s&rr,*buf_s&gg, *buf_s&bb);
	    //printf("%d ptr %x %x %x %x %x\n",i,buf_r,*buf_r,*buf_r&rr,*buf_r&gg, *buf_r&bb);
 
	    l = *buf_l&bb;
	    
	    s = *buf_s&bb;
	    r = *buf_r&bb;
	    l = twos_comp(l);
	    s = twos_comp(s);
	    r = twos_comp(r);
	    dwt_b = s -((l+r)>>1);
	    v = 0;
	    v |= dwt_b&0x1ff; 
	    //printf("%d l %x s %x r %x dwt %x %x\n",i, l,s,r,dwt_b,dwt_b&0x1ff);
	    
	    dwt_b = twos_comp(dwt_b&0x1ff);
	    //printf("%x %d\n",dwt_b,dwt_b);
	    l = (*buf_l&gg)>>10;
	    s = (*buf_s&gg)>>10;
	    r = (*buf_r&gg)>>10;
	    l = twos_comp(l);
	    s = twos_comp(s);
	    r = twos_comp(r);	    
	    dwt_g = s -((l+r)>>1);
	    dwt_g = dwt_g&0x1ff;
	    v |= dwt_g<<10;
	    //printf("%d l %x s %x r %x dwt %x %x\n",i, l,s,r,dwt_g,dwt_g&0x1ff);

	    dwt_g = twos_comp(dwt_g&0x1ff);
	    //printf("%x %d\n",dwt_g,dwt_g);	    
	    l = *buf_l>>20;
	    s = *buf_s>>20;
	    r = *buf_r>>20;
	    l = twos_comp(l);
	    s = twos_comp(s);
	    r = twos_comp(r);	    
	    dwt_r = s -((l+r)>>1);
	    v |= dwt_r<<20;
	    //printf("%d l %x s %x r %x dwt %x %x\n",i,l,s,r,dwt_r,dwt_r&0x1ff);

	    dwt_r = twos_comp(dwt_r&0x1ff);
	    //printf("%x %d\n",dwt_r,dwt_r);
 
 
	    *buf_s = v;
	    //printf("%d ptr %x %x %x %x %x\n",i,buf_s,*buf_s,*buf_s&rr,*buf_s&gg, *buf_s&bb);    
	    buf_l++;
	    buf_s++;
	    buf_r++;
   }*/

}
