#include "board.h"
#include "lifting.h"

#ifdef __ZIPCPU__
void *malloc(int sz);
void free(void *);
void zip_halt(void);
typedef int int32;
#else
#include <stdlib.h>
#include <stdint.h>
#endif
 

void rd_dwt_wr(void) {
	const int LED_ON = 0x20002;
	const int LED_OFF = 0x20000;
	const int READY_FOR_XMIT = 0x40004000;
	const int XULA_BUSY = 0x40000000;
    
	//struct images im;
	int *buf_r;
	int *buf_g;
	int *buf_b;
	int *y;
	int *wptr,*wptr1,*wptr2;
	int *alt,*alt1,*alt2,*u,*v;
	//the contents of the buf_r_used
	//where the red lift steps are stored
	//before packing to send back to RPi2B
	int *buf_yuv_used = (int *)0x8efff1;
	int *buf_r_used = (int *)0x8efff2;
	int *buf_g_used = (int *)0x8efff3;
	int *buf_b_used = (int *)0x8efff4;
	int *clocks_used = (int *)0x8efff5;
	int *fwd_inv = (int *)0x8efff6;
	int *flgyuv = (int *)0x8efff7;

 
	int w,h;

	w = 256;
	h = 256;

	//pointers to r g b & yuv
	
	y = malloc(sizeof(int)*(w*h)*3);
	buf_r = malloc(sizeof(int)*(w*h)*2);
	buf_g = malloc(sizeof(int)*(w*h)*2);
	buf_b = malloc(sizeof(int)*(w*h)*2);

 
	*buf_yuv_used = (int )y;
	*buf_r_used = (int) buf_r;
	*buf_g_used = (int) buf_g;
	*buf_b_used = (int) buf_b;
 	

	wptr = buf_r;
	wptr1 =  buf_g;
	wptr2 = buf_b;
	sys -> io_gpio = LED_ON|READY_FOR_XMIT ;
	zip_read_image(wptr, wptr1, wptr2);
	
	sys->io_gpio = LED_OFF|XULA_BUSY;
	sys->io_bustimer = 0x7fffffff;
	/*
	y u v reduced the range of dwt lift values
	flgyuv is set with either
	wbregs 0x8efff7 0 y u v
	wbregs 0x8efff7 1 r g b
	if flgyuv is equal to zero y u v is computed
	from r g b
	sets the wptr, wptr1, and wptr2 y u v
	else sets wptr, wptr1, and wptr2 to r g b
	*/ 
	if(flgyuv[0] == 0) {
	
		wptr = buf_r;
		wptr1 =  buf_g;
		wptr2 = buf_b;
 
		
		u = &y[w*h];
		v = &y[w*h*2];
 	
		yuv(w,wptr,wptr1,wptr2,u,v,y);
		wptr = y;
		wptr1 =  u;
		wptr2 = v;
	}
 	else {	
		wptr = buf_r;
		wptr1 = buf_g;
		wptr2 = buf_b;
	
	}
 	
 	
	alt = &buf_r[256*256];
	lifting(w,wptr,alt,fwd_inv);
	
	alt1 = &buf_g[256*256];
	lifting(w,wptr1,alt1,fwd_inv);
	

	alt2 = &buf_b[256*256];
	lifting(w,wptr2,alt2,fwd_inv);
	
	*clocks_used = 0x7fffffff-sys->io_bustimer;
	/*
	y u v reduces the range of dwt lift values
	flgyuv is set with either
	wbregs 0x8efff7 0 y u v
	wbregs 0x8efff7 1 r g b
	if flgyuv is equal to zero 
	sets the wptr, wptr1, and wptr2 to y u v
	else sets wptr, wptr1, and wptr2 to r g b
	*/	
	if(flgyuv[0] == 0) {
		wptr = y;
		wptr1 =  u;
		wptr2 = v;
	}	
	else {	
		wptr = buf_r;
		wptr1 = buf_g;
		wptr2 = buf_b;
	}	
	
	zip_write(wptr);
	zip_write(wptr1);
	zip_write(wptr2);  
    

	free(buf_r);
	free(buf_g);
	free(buf_b);
	free(y);
}

void zip_write(int *imbuf) {
	//0x90ab12cd
	//little endia
	//cd uu
	//12 ul
	//ab lu
	//90 ll
const int LED_SW_ON = 0x10001;
const int LED_SW_OFF = 0x10000;	
int i, ch;
i = 0;
ch = 0;
const int uu = 0xff000000;
const int ul = 0x00ff0000; 

const int lu = 0x0000ff00;
const int ll = 0x000000ff;
 
// Set a timer to abort in case things go bad
// We'll set our abort for about 750 ms into the future ... that should
//   be plenty of time to transfer the image
//sys->io_bustimer = 220000000;
sys->io_bustimer = 0;
// Let's also shut down all interrupts, and clear the timer interrupt
// That way we can poll the interrupt timer later, to see if things
// have gone poorly.
//sys->io_pic = INT_TIMER;
sys->io_gpio = LED_SW_ON; 
for(i=0; i<256*256; i++) {
     // Write lower byte
     while(sys->io_uart_tx)
		; 
     ch = (*imbuf&ll);
	 // Wait while our transmitter is busy
	 while(sys->io_uart_tx)
		; 
	 sys->io_uart_tx = ch;	
 
     // Write upper byte
     ch = (*imbuf&lu)>>8;
     // Wait while our transmitter is busy
	 while(sys->io_uart_tx)
		; 
	 sys->io_uart_tx = ch;
     while(sys->io_uart_tx)
		; 
     ch = (*imbuf&ul)>>16;
	 // Wait while our transmitter is busy
	 while(sys->io_uart_tx)
		; 
	 sys->io_uart_tx = ch;	
 
     // Write upper byte
     //if (((*imbuf&uu)>>24) == 0x3f) ch = 255;
     //else ch = (*imbuf&uu)>>24;
     ch = (*imbuf&uu)>>24;
     // Wait while our transmitter is busy
	 while(sys->io_uart_tx)
		; 
	 sys->io_uart_tx = ch; 
*imbuf++ ;
}
sys->io_gpio = LED_SW_OFF;
 

}
