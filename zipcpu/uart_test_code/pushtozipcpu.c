#include "board.h"


void zip_read_image(int *img1, int *img2, int *img3) {
const int LED_SW_ON = 0x10001;
const int LED_SW_OFF = 0x10000;	
int i, ch;
i = 0;
ch = 0;
int *r,*g,*b;
r = img1;
g = img2;
b = img3;


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
// Read red
 
do {
// Read a character from the UART port
ch = sys->io_uart_rx;

// Repeat while ...
//   bit 0x0100 is set, indicating we read from an
//      empty port, AND
//   the TIMER interrupt hasn't taken place
} while(((ch&0x0100)!=0));

// We'll pack our colored pixels into memory, three pixels per
// address.  This packing will allow us to do vector operations
// on the pixels later, so that we can do all three colors at
// once.
r[0] = ch;
r+=1;

// Read green
do {
// This is the same as before.  Only we never reset
// the timer interrupt, so if it triggered we'll exit
// here after only one time through.
ch = sys->io_uart_rx;
} while(((ch&0x0100)!=0) );
g[0] = ch;
g+=1;

// Read blue
do {
// Same as with green.
ch = sys->io_uart_rx;
} while(((ch&0x0100)!=0) );

// Pack our final pixel value into this word, and write it to
// memory.
b[0] = ch;
b+=1;
 
sys->io_gpio = LED_SW_OFF;
if (sys->io_pic & INT_TIMER) {
	//*ptr=0xaa5555aa;
    break;
    }
}
}
