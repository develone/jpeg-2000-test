#include "dwt_funcs.h"

asm("\t.section\t.start\n" // Makes sure we start at the beginning of program memory, and specifically that the _start function is the first address (a.k.a. the reset address) in memory.
    "\t.global\t_start\n"        // Makes certain the linker sees this symbol
    "\t.type\t_start,@function\n" // Probably superfluous--some CPU's treat function symbols different from data symbols, the ZipCPU doesn't care
    "_start:\n"    // Here's the entry symbol for this routine.  Note the lack of a tab starting the line
    "\tLDI\t_top_of_stack,SP\n"
    "\tLDI\t1,R1\n"    // Place a 1 into R1 as a marker, in case we don't stop where we think we should
    "\tLDI\t-1,R0\n"    // Load a -1 into R0
    "\tASR\t2,R0\n"    // Shift R0 to the right by two places, using an arithmetic shift.  The result should still be -1
    "\tCMP\t-1,R0\n"    // Compare the result of the shift to -1
    "\tHALT.NZ\n"        // If the result is not equal to -1, then halt the CPU here
    "\tLDI\t2,R1\n"    // Place a 2 into R1 as a marker
    "\tLDI\t-14,R0\n"    // Let's try again with a different number, in case there' s something special about -1
    "\tASR\t2,R0\n"    // Shift R0 to the right by two places, using an arithmetic shift.  The result should be -4
    "\tCMP\t-4,R0\n"    // Compare the result of the shift to -4
    "\tHALT.NZ\n"        // If the result is not equal to -4, then halt the CPU here
    "\tLDI\t3,R1\n"    // Marker #3
    "\tLDI\t538314514,R2\n"    // What should be your version number
    "\tLOD\t0x101,R0\n"        // Load up the version into R0
    "\tCMP\tR0,R2\n"        // Make certain it is today's, 12 July, 2016
    "\tHALT.NZ\n"            // Halt if we are running another version of the XuLA2 core
    "\tLDI\t4,R1\n"        // Set our marker to 4 before starting the program
    "\tBRA\tentry\n"    // Otherwise--start your program.
    "\t.section\t.text"); // Switch back to the text segment, so that nothing else ends up in that ".start" segment

/*
asm("\t.section\t.start\n"
	"\t.global\t_start\n"
	"\t.type\t_start,@function\n"
	"_start:\n"
	"LDI\t_top_of_stack,SP\n"
	"\tBRA\tentry\n"
	"\t.section\t.text"); 
*/
#include "board.h" 

const char msg[] =  "Hello, world!\r\n";
const char msg1[] = "Data rdy     \r\n";
void entry(void) {
	
	//register IOSPACE	*sys = (IOSPACE *)0x0100;
	int	counts = 0;
	 
    int *buf_ptr = (int *)0x800000;
    
    //int *tmp_ptr = (int *)0x820000;
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
		

        //testing time to perform 64 x 64
        //red subband
        //sys->io_bustimer = 0x7fffffff;
        //testing red subband
        test_malloc();         
        
        
        //zip_write_image(buf_ptr);
         
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

