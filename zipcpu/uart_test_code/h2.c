
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
	int	counts = 0;
	 
    char *buf_ptr = (char *)0x800000;
    zip_clear_sdram(buf_ptr);
	// Let's set ourselves up for 1000000 baud, 8-bit characters, no parity,
	// and one stop bit.
	sys->io_uart_ctrl = 79;
     
	while(counts==0) {
		const char	*ptr;

		ptr = msg;
		while(*ptr) {
			// Wait while our transmitter is busy
			while(sys->io_uart_tx)
				;
			sys->io_uart_tx = *ptr++; // Transmit our character
			
			
			//ptr = msg1;  // data has been received
			
 
		}
		sys -> io_gpio = 0xffff4002;
        zip_read_image(buf_ptr);
        sys -> io_gpio = 0xffff0000;
 
		// Now, wait for the top of the second
		unsigned secv = sys->io_rtc_clock;
		while(secv == sys->io_rtc_clock)
		;

		// And repeat, saying Hello, World! once each second

		// Let's keep track of how many times we do this too ... so we
		// can know that the program is still working
		counts++;
	}
}

