// . setzipcpuPath.sh
// xsload --usb 0 --fpga tmp_svn_bld_bitfiles/toplevel.bit
// to compile zip-gcc -fno-builtin -nostdlib -O3 dwt.c -o dwt -T xulalink.x
// to disasmble
// zipobj-dump -d dwt
// ziprun test_zipcpu/dwt

asm("\t.section\t.start\n"
	"\t.global\t_start\n"
	"\t.type\t_start,@function\n"
	"_start:\n"
	"LDI\t_top_of_stack,SP\n"
	"\tBRA\tentry\n"
	"\t.section\t.text");

#define	INT_RTC		0x002
#define	INT_FLASH	0x004
#define	INT_SCOPE	0x008
#define	INT_GPIO	0x010
#define	INT_PWM		0x020
#define	INT_UARTRX	0x040
#define	INT_UARTTX	0x080

typedef	struct	{
	volatile int		io_reserved, io_version, io_pic;
	volatile unsigned	*io_buserr;
	volatile unsigned	io_rtcdate;
	volatile unsigned	io_gpio;
	volatile unsigned	io_uart_ctrl;
	volatile unsigned	io_pwm_audio, io_pwm_timer;
	volatile unsigned	io_uart_rx, io_uart_tx;
	volatile unsigned	io_flash_ereg, io_flash_config,
				io_flash_status, io_flash_devid;
	volatile unsigned	io_rtc_clock, io_rtc_timer, io_rtc_stopwatch,
				io_rtc_alarm;
} IOSPACE;

const char msg[] = "Hello, world!\n";

void entry(void) {
	register IOSPACE	*sys = (IOSPACE *)0x0100;
	int	counts = 0;

	// Let's set ourselves up for 9600 baud, 8-bit characters, no parity,
	// and one stop bit.
	sys->io_uart_ctrl = 8333;

	int *buf_ptr = (int *)0x800000;
	int *img_ptr1 = (int *)0x810000;
	int col,row,p;
	int w,h;
	w = 256;
	h = 256;
	
	
    
	for ( p =0; p < 2; p++) {	
	for (int col = 0; col<256;col++) { 
		//even samples
		for (int row = 2;row<256;row=row+2) { 
			*(buf_ptr+col+row*256) = *(buf_ptr+col+row*256) - ((*(buf_ptr+col+(row-1)*256) + *(buf_ptr+col+(row+1)*256)) >> 1);
		}
		//odd samples
		for (int row = 1; row < h -2 ; row = row + 2) {
			*(buf_ptr+col+row*256) = *(buf_ptr+col+row*256) - ((*(buf_ptr+col+(row-1)*256) + *(buf_ptr+col+(row+1)*256)) >> 1);
		}
		 
	}
    }
	while(1) {
		const char	*ptr;

		ptr = msg;
		while(*ptr) {
			// Wait while our transmitter is busy
			while(sys->io_uart_tx)
				;
			sys->io_uart_tx = *ptr++; // Transmit our character
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

