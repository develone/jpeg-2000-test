#include "board.h"
/*
     const int LED_ON_DWT = 0x10001;
     const int LED_OFF_DWT = 0x10000;	
     sys -> io_gpio = LED_ON_DWT;
     sys -> io_gpio = LED_OFF_DWT;
*/
int twos_comp(int lsr) {
	if (lsr > 256) {
		return lsr - 512;
	}
	else { 
	    return lsr;
    }	
}
void dwt_process(int *imgbuf) {
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
    const int bb = 0x3ff;
    const int gg = 0xffc00;
    const int rr = 0x3ff00000;
    int i,v;
    //struct results 
    int *buf_l;
    int *buf_r;
    int *buf_s;
    //printf("sub ptr to xx %x\n",imgbuf);
    *imgbuf++;
    //setting imgbuf sample minus 1
    buf_l = imgbuf;
    *imgbuf++;
    //setting imgbuf sample even
    buf_s = imgbuf;
	*imgbuf++;
	//setting imgbuf sample plus 1
	buf_r = imgbuf;	
	//setting imgbuf sample even
	*imgbuf--;
	//printf("############sub ptr to xx %x\n",imgbuf);
	for(i = 2; i < 65536; i=i+2) {
		//printf("%d ptr %x %x %x %x %x\n",i-1,buf_l,*buf_l,*buf_l&rr,*buf_l&gg, *buf_l&bb);
	    //printf("%d ptr %x %x %x %x %x\n",i,buf_s,*buf_s,*buf_s&rr,*buf_s&gg, *buf_s&bb);
	    //printf("%d ptr %x %x %x %x %x\n",i+1,buf_r,*buf_r,*buf_r&rr,*buf_r&gg, *buf_r&bb);
	    v = 0;
	    l = *buf_l>>20;
	    s = *buf_s>>20;
	    r = *buf_r>>20;
	    l = twos_comp(l);
	    s = twos_comp(s);
	    r = twos_comp(r);	    
	    dwt_r = s -((l+r)>>1);
	    dwt_r = dwt_r&0x1ff;
	    v |= (dwt_r<<20);
	    //printf("%d l %x s %x r %x dwt %x %x %x \n",i,l,s,r,dwt_r,dwt_r&0x1ff,v);
        dwt_r = twos_comp(dwt_r&0x1ff);
        //printf("%x %d\n",dwt_r,dwt_r); 
        
	    l = (*buf_l&gg)>>10;
	    s = (*buf_s&gg)>>10;
	    r = (*buf_r&gg)>>10;
	    l = twos_comp(l);
	    s = twos_comp(s);
	    r = twos_comp(r);	    
	    dwt_g = s -((l+r)>>1);
	    dwt_g = dwt_g&0x1ff;
	    v |= (dwt_g<<10);
	    //printf("%d l %x s %x r %x dwt %x %x %x\n",i, l,s,r,dwt_g,dwt_g&0x1ff,v);
        dwt_g = twos_comp(dwt_g&0x1ff);
	    //printf("%x %d\n",dwt_g,dwt_g);        
	     
	    l = *buf_l&bb;
	    s = *buf_s&bb;
	    r = *buf_r&bb;
	    l = twos_comp(l);
	    s = twos_comp(s);
	    r = twos_comp(r);
	    dwt_b = s -((l+r)>>1);
	    dwt_b = dwt_b&0x1ff;
	    v |= dwt_b; 
	    //printf("%d l %x s %x r %x dwt %x %x %x\n",i, l,s,r,dwt_b,dwt_b&0x1ff,v);
	    dwt_b = twos_comp(dwt_b&0x1ff);
	    //printf("%x %d\n",dwt_b,dwt_b);

        *buf_s = v;
         
	    //printf("%d ptr %x %x %x %x %x %x\n",i,buf_s,*buf_s,*buf_s&rr,*buf_s&gg, *buf_s&bb,v);
	    //printf("\n");
	    	        
	    buf_l++;
	    buf_l++;
	    buf_s++;
	    buf_s++;
	    buf_r++;
	    buf_r++;
   }
   
    //printf("sub ptr to xx %x\n",imgbuf);
    //
    *imgbuf--; //setting imgbuf sample minus 1
    *imgbuf--;
    buf_l = imgbuf;
    *imgbuf++;
    //setting imgbuf sample odd
    buf_s = imgbuf;
	*imgbuf++;
	//setting imgbuf sample plus 1
	buf_r = imgbuf;
	//setting imgbuf sample odd
	 *imgbuf--;
	 //printf("------------sub ptr to xx %x\n",imgbuf);
	for(i = 1; i < 65535; i=i+2) {
		//printf("%d ptr %x %x %x %x %x\n",i-1,buf_l,*buf_l,*buf_l&rr,*buf_l&gg, *buf_l&bb);
	    //printf("%d ptr %x %x %x %x %x\n",i,buf_s,*buf_s,*buf_s&rr,*buf_s&gg, *buf_s&bb);
	    //printf("%d ptr %x %x %x %x %x\n",i+1,buf_r,*buf_r,*buf_r&rr,*buf_r&gg, *buf_r&bb);
	    v = 0;
	    l = *buf_l>>20;
	    s = *buf_s>>20;
	    r = *buf_r>>20;
	    l = twos_comp(l);
	    s = twos_comp(s);
	    r = twos_comp(r);	    
	    dwt_r = s + ((l+r+2)>>2);
	    dwt_r = dwt_r&0x1ff;
	    v |=(dwt_r<<20);
	    //printf("%d l %x s %x r %x dwt %x %x %x\n",i,l,s,r,dwt_r,dwt_r&0x1ff,v);
        dwt_r = twos_comp(dwt_r&0x1ff);
        //printf("%x %d\n",dwt_r,dwt_r); 
        
	    l = (*buf_l&gg)>>10;
	    s = (*buf_s&gg)>>10;
	    r = (*buf_r&gg)>>10;
	    l = twos_comp(l);
	    s = twos_comp(s);
	    r = twos_comp(r);	    
	    dwt_g = s + ((l+r+2)>>2);
	    dwt_g = dwt_g&0x1ff;
	    v |= (dwt_g<<10);
	    //printf("%d l %x s %x r %x dwt %x %x %x\n",i, l,s,r,dwt_g,dwt_g&0x1ff,v);
        dwt_g = twos_comp(dwt_g&0x1ff);
	    //printf("%x %d\n",dwt_g,dwt_g);        
	     
	    l = *buf_l&bb;
	    s = *buf_s&bb;
	    r = *buf_r&bb;
	    l = twos_comp(l);
	    s = twos_comp(s);
	    r = twos_comp(r);
	    dwt_b = s + ((l+r+2)>>2);
	    dwt_b = dwt_b&0x1ff;
	    v |= (dwt_b&0x1ff); 
	    //printf("%d l %x s %x r %x dwt %x %x %x\n",i, l,s,r,dwt_b,dwt_b&0x1ff,v);
	    dwt_b = twos_comp(dwt_b&0x1ff);
	    //printf("%x %d\n",dwt_b,dwt_b);

        *buf_s = v;
         
	    //printf("%d ptr %x %x %x %x %x %x\n",i,buf_s,*buf_s,*buf_s&rr,*buf_s&gg, *buf_s&bb,v);
	    //printf("\n");
	    	        
	    buf_l++;
	    buf_l++;
	    buf_s++;
	    buf_s++;
	    buf_r++;
	    buf_r++;
   }
   
	 
}
