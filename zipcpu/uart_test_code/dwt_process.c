#include "board.h"
struct results dwt_process(int *imgbuf) {
    const int LED_ON_DWT = 0x10001;
    const int LED_OFF_DWT = 0x10000;	
    const int bb = 0x3ff;
    const int gg = 0xffc00;
    const int rr = 0xff00000;
    int i;
    struct results a;
    int *buf_l;
    int *buf_r;
    int *buf_s;
    //printf("sub ptr to xx %x\n",imgbuf);
    *imgbuf++;
    //setting imgbuf sample minus 1
    buf_l = imgbuf;
    *imgbuf++;
    buf_s = imgbuf;
	*imgbuf++;
	//setting imgbuf sample plus 1
	buf_r = imgbuf;
	//setting imgbuf sample
	 *imgbuf--;
	for(i = 2; i < 16; i=i+2) {
		//printf("%d ptr %x %x %x %x %x\n",i,buf_l,*buf_l,*buf_l&rr,*buf_l&gg, *buf_l&bb);
	    //printf("%d ptr %x %x %x %x %x\n",i,buf_s,*buf_s,*buf_s&rr,*buf_s&gg, *buf_s&bb);
	    //printf("%d ptr %x %x %x %x %x\n",i,buf_r,*buf_r,*buf_r&rr,*buf_r&gg, *buf_r&bb);
 
	    a.l = *buf_l&bb;
	    a.s = *buf_s&bb;
	    a.r = *buf_r&bb;
	    a.dwt = a.s -((a.l+a.r)>>1);
	    //printf("l %x s %x r %x dwt %x %x\n",a.l,a.s,a.r,a.dwt,a.dwt&0x1ff);
	    a.l = (*buf_l&gg)>>10;
	    a.s = (*buf_s&gg)>>10;
	    a.r = (*buf_r&gg)>>10;
	    a.dwt = a.s -((a.l+a.r)>>1);
	    //printf("l %x s %x r %x dwt %x %x\n",a.l,a.s,a.r,a.dwt,a.dwt&0x1ff);	    
	    a.l = *buf_l>>20;
	    a.s = *buf_s>>20;
	    a.r = *buf_r>>20;
	    a.dwt = a.s -((a.l+a.r)>>1);
	    //printf("l %x s %x r %x dwt %x %x\n",a.l,a.s,a.r,a.dwt,a.dwt&0x1ff);
	    //sample - 1
	    //*imgbuf++;
	    buf_l++;
	    buf_s++;
	    buf_r++;
	    //a.r_p = *imgbuf&rr;
	    //a.g_p = *imgbuf&gg;
	    ///a.b_p = *imgbuf&bb;
	    //printf("%d ptr %x %x r %x g %x b %x \n",i,imgbuf,*imgbuf, a.r_p,a.g_p,a.b_p);
 
   }
  	//turn on the red led off gpio <0>
	sys -> io_gpio = LED_OFF_DWT;
	return a;
}
