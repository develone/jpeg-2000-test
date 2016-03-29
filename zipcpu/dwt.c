// . setzipcpuPath.sh
// xsload --usb 0 --fpga tmp_svn_bld_bitfiles/toplevel.bit
// to compile zip-gcc -fno-builtin -nostdlib dwt.c -o dwt -T xulalink.x
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
	int *img_ptr = (int *)0x800000;
	int *img_ptr1 = (int *)0x810000;
	int col,row;
	int w,h;
	w = 256;
	h = 256;
	
	
    
		
	for (int col = 0; col<256;col++) { 
		//even samples
		for (int row = 2;row<256;row=row+2) { 
			
		}
		//odd samples
		for (int row = 1; row < h -2 ; row = row + 2) {
			*(img_ptr+col+row*256) = *(img_ptr+col+row*256) - ((*(img_ptr+col+(row-1)*256) + *(img_ptr+col+(row+1)*256)) >> 1);
		}
		 
	}
	
 
}

