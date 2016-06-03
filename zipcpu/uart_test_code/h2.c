
asm("\t.section\t.start\n"
	"\t.global\t_start\n"
	"\t.type\t_start,@function\n"
	"_start:\n"
	"LDI\t_top_of_stack,SP\n"
	"\tBRA\tentry\n"
	"\t.section\t.text");

#include "board.h" 

const char msg[] = "Hello, world!\r\n";
const char msg1[] = "Data rdy\r\n";
void entry(void) {
	//register IOSPACE	*sys = (IOSPACE *)0x0100;
	int	counts = 0;
	int recdflg = 0;
    char *buf_ptr = (char *)0x800000;
	// Let's set ourselves up for 1000000 baud, 8-bit characters, no parity,
	// and one stop bit.
	sys->io_uart_ctrl = 79;
     
	while(1) {
		const char	*ptr;

		if (recdflg == 0) ptr = msg;
		while(*ptr) {
			// Wait while our transmitter is busy
			while(sys->io_uart_tx)
				;
			sys->io_uart_tx = *ptr++; // Transmit our character
			recdflg = zip_read_image(buf_ptr);
			if (recdflg == 65536) {
				ptr = msg1;  // data has been received
			}
			else {
				recdflg = zip_read_image(buf_ptr);
			}
		}

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

