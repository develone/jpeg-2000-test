#include "board.h"


void zip_write_image(int *imbuf) {
const int LED_SW_ON = 0x10001;
const int LED_SW_OFF = 0x10000;	
int i, ch;
i = 0;
ch = 0;
 
const int bb = 0x1ff;
const int gg = 0x7fc00;
const int rr = 0x1ff00000;
 
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
     // Write red
     while(sys->io_uart_tx)
		; 
     ch = (*imbuf&rr)>>20;
	 // Wait while our transmitter is busy
	 while(sys->io_uart_tx)
		; 
	 sys->io_uart_tx = ch;	
 


     // Write green
     ch = (*imbuf&gg)>>10;
     // Wait while our transmitter is busy
	 while(sys->io_uart_tx)
		; 
	 sys->io_uart_tx = ch;
 

     // Write blue
     ch = *imbuf&bb;
     // Wait while our transmitter is busy
	 while(sys->io_uart_tx)
		; 
	 sys-> io_uart_tx = ch;
     while(sys->io_uart_tx)
		;
*imbuf++ ;
//sys->io_gpio = LED_SW_OFF;
//if (sys->io_pic & INT_TIMER) {
	//*ptr=0xaa5555aa;
    //break;
    //}
}
}
