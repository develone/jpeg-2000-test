#include "board.h"

#ifdef __ZIPCPU__
void *malloc(int sz);
void free(void *);
void zip_halt(void);
typedef int int32;
#else
#include <stdlib.h>
#include <stdint.h>
#endif
void test_malloc(void) {
	const int LED_ON = 0x20002;
	const int LED_OFF = 0x20000;
	const int READY_FOR_XMIT = 0x40004000;
	const int XULA_BUSY = 0x40000000;
    
 
    int *buf_r;
    int *buf_g;
    int *buf_b;    	
	int *wptr;
	//the contents of the buf_r_used
	//where the red lift steps are stored
	//before packing to send back to RPi2B
	
	int *buf_r_used = (int *)0x89fff2;
	int *buf_g_used = (int *)0x89fff3;
	int *buf_b_used = (int *)0x89fff4;
	int *clocks_used = (int *)0x89fff5;
 
	int *wptr_used = (int *)0x89fff6;
	 
	int *buf_ptr = (int *)0x800000;
    int *buf_dwt = (int *)0x810000;

 
	int w,h;

	w = 256;
	h = 256;

	//pointers to r g b
 
	buf_r = malloc(sizeof(int)*(w*h));
	buf_g = malloc(sizeof(int)*(w*h));
	buf_b = malloc(sizeof(int)*(w*h));

	//pointer to un-packed r g b
	//saved at pointer 
	//buf_r_used 0x87fff2
	//buf_g_used 0x87fff3
	//buf_b_used 0x87fff4
	*buf_r_used = buf_r;
	*buf_g_used = buf_g;
	*buf_b_used = buf_b;
		
 
 
	sys -> io_gpio = LED_ON|READY_FOR_XMIT ;
    zip_read_image(buf_r, buf_g, buf_b);
	sys->io_gpio = LED_OFF|XULA_BUSY; 


	
	*wptr_used = wptr; 
	
 
	wptr = *buf_r_used;
    sys->io_bustimer = 0x7fffffff;
	lifting(w,wptr,buf_dwt);
	wptr = *buf_g_used;
	lifting(w,wptr,buf_dwt);
	wptr = *buf_b_used;
	lifting(w,wptr,buf_dwt);	
	*clocks_used = 0x7fffffff-sys->io_bustimer;
	//transfer image to RPi2B
	buf_r = *buf_r_used;
	buf_g = *buf_g_used;
	buf_b = *buf_b_used;
    zip_write(buf_r);
    zip_write(buf_g);
    zip_write(buf_b);  


free(buf_r);
free(buf_g);
free(buf_b);
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
