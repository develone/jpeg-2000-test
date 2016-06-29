
asm("\t.section\t.start\n"
	"\t.global\t_start\n"
	"\t.type\t_start,@function\n"
	"_start:\n"
	"LDI\t_top_of_stack,SP\n"
	"\tBRA\tentry\n"
	"\t.section\t.text");

#include "board.h" 
const int LED_ON = 0x20002;
const int LED_OFF = 0x20000;
const int READY_FOR_XMIT = 0x40004000;
const int XULA_BUSY = 0x40000000;
const char msg[] =  "Hello, world!\r\n";
const char msg1[] = "Data rdy     \r\n";
void entry(void) {
	
	//register IOSPACE	*sys = (IOSPACE *)0x0100;
	int	counts = 0;
	int w,h;  
    int *buf_ptr = (char *)0x800000;
    int *clocks_used = (char *)0x87fffe;
    int *tmp_ptr = (char *)0x820000;
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
		test_malloc();
		sys -> io_gpio = LED_ON|READY_FOR_XMIT ;
        zip_read_image(buf_ptr);
        
        sys->io_gpio = LED_OFF|XULA_BUSY;
        sys->io_bustimer = 0x7fffffff;
         
        *clocks_used = 0x7fffffff-sys->io_bustimer;
        
        //pp(buf_ptr,tmp_ptr);
        w = 64;
        h = 64;
        lift_step(buf_ptr,w,h);
        de_interleave(buf_ptr,w,h);
        lift_step(buf_ptr,w,h);
        de_interleave(buf_ptr,w,h);
        lower_upper(buf_ptr,w,h);
        //pp(buf_ptr,tmp_ptr);
        zip_write_image(buf_ptr);
         
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

