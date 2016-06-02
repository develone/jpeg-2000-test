#ifndef	BOARD_H
#define	BOARD_H


#define	INT_RTC		0x002
#define	INT_FLASH	0x004
#define	INT_SCOPE	0x008
#define	INT_GPIO	0x010
#define	INT_PWM		0x020
#define	INT_UARTRX	0x040
#define	INT_UARTTX	0x080
#define	INT_TIMER	0x100

typedef	struct	{
	volatile int		io_reserved, io_version, io_pic;
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
	volatile unsigned	io_scope, io_scopd;
} IOSPACE;

static IOSPACE	* const sys = (IOSPACE *)0x0100;

typedef	struct	{
	volatile unsigned	sd_ctrl, sd_data, sd_fifo[2];
} SDCARD;

static SDCARD	* const sd = (SDCARD *)0x0120;

#define	SDRAM	(void *)0x800000
#define	FLASH	(void *)0x040000
#define	CLOCKFREQHZ	80000000

#endif
