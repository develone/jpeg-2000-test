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

int INT_TIMER;
int ch;
typedef	struct	{
	volatile int		io_reserved, io_version, io_pic,ch;
	volatile unsigned	*io_buserr;
	volatile unsigned	io_bustimer;
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
