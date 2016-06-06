
asm("\t.section\t.start\n"
	"\t.global\t_start\n"
	"\t.type\t_start,@function\n"
	"_start:\n"
	"LDI\t_top_of_stack,SP\n"
	"\tBRA\tentry\n"
	"\t.section\t.text");

#include "board.h" 

const char msg[] =  "Hello, world!\r\n";
const char msg1[] = "Data rdy     \r\n";
void entry(void) {
	//register IOSPACE	*sys = (IOSPACE *)0x0100;
	
	
	int ch;
    char *buf_ptr; 
    buf_ptr = (char *)SDRAM;
	// Let's set ourselves up for 1000000 baud, 8-bit characters, no parity,
	// and one stop bit.
	sys->io_uart_ctrl = 79;
    while(1) {
		
		ch = sys->io_uart_rx;	
		
		
	    sys->io_uart_tx = ch;
	    /*
	    *buf_ptr=ch;
	    ch = *buf_ptr;
	    sys->io_uart_tx = ch;
	    *buf_ptr = *buf_ptr + 1; */
	}
	 
 
     

		
  
	}


