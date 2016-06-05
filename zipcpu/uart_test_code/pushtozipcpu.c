#include "board.h"


void zip_read_image(char *imbuf) {
int i, ch, val,recd;
i = 0;
ch = 0;
val = 0;
recd = 0;
int *ptr;
ptr = 0x830000;
*ptr = 0x55aaaa55;
// Set a timer to abort in case things go bad
// We'll set our abort for about 750 ms into the future ... that should
//   be plenty of time to transfer the image
sys->io_bustimer = 220000000;
// Let's also shut down all interrupts, and clear the timer interrupt
// That way we can poll the interrupt timer later, to see if things
// have gone poorly.
sys->io_pic = INT_TIMER;
 
for(i=0; i<256*256; i++) {
// Read red
do {
// Read a character from the UART port
ch = sys->io_uart_rx;

// Repeat while ...
//   bit 0x0100 is set, indicating we read from an
//      empty port, AND
//   the TIMER interrupt hasn't taken place
} while(((ch&0x0100)!=0)&&((sys->io_pic&INT_TIMER)==0));

// We'll pack our colored pixels into memory, three pixels per
// address.  This packing will allow us to do vector operations
// on the pixels later, so that we can do all three colors at
// once.
val = ch<<20;

// Read green
do {
// This is the same as before.  Only we never reset
// the timer interrupt, so if it triggered we'll exit
// here after only one time through.
ch = sys->io_uart_rx;
} while(((ch&0x0100)!=0)&&((sys->io_pic&INT_TIMER)==0));
val |= ch<<10;

// Read blue
do {
// Same as with green.
ch = sys->io_uart_rx;
} while(((ch&0x0100)!=0)&&((sys->io_pic&INT_TIMER)==0));

// Pack our final pixel value into this word, and write it to
// memory.
val |= ch;
recd = recd + 1;
*imbuf++ = val;
*ptr = recd;
if (sys->io_pic & INT_TIMER) {
	*ptr=0xaa5555aa;
    break;
    }
}
}
