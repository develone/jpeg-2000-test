///////////////////////////////////////////////////////////////////////////////
//
// Filename:	cputest.c
//
// Project:	Zip CPU -- a small, lightweight, RISC CPU soft core
//
// Purpose:	To test the CPU, it's instructions, cache, and pipeline, to make
//		certain that it works.  This includes testing that each of the
//	instructions works, as well as any strange instruction combinations.
//
//
// Creator:	Dan Gisselquist, Ph.D.
//		Gisselquist Technology, LLC
//
///////////////////////////////////////////////////////////////////////////////
//
// Copyright (C) 2015-2016, Gisselquist Technology, LLC
//
// This program is free software (firmware): you can redistribute it and/or
// modify it under the terms of  the GNU General Public License as published
// by the Free Software Foundation, either version 3 of the License, or (at
// your option) any later version.
//
// This program is distributed in the hope that it will be useful, but WITHOUT
// ANY WARRANTY; without even the implied warranty of MERCHANTIBILITY or
// FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
// for more details.
//
// License:	GPL, v3, as defined and found on www.gnu.org,
//		http://www.gnu.org/licenses/gpl.html
//
//
///////////////////////////////////////////////////////////////////////////////
//
//
#define NULL	(void *)0
volatile	int	*const UARTTX = (volatile int *)0x010b,
	* const UART_CTRL = (int *)0x0107;
// #define	ZIPSYS
#ifdef	ZIPSYS
#define	HAVE_COUNTER
volatile	int * const PIC = (volatile int *)0xc0000000;
const int	INT_UARTTX = 0x2000;
volatile	int	*const COUNTER = (volatile int *)0xc0000008;

#define	HAVE_SCOPE

#else
volatile	int	* const PIC = (volatile int *)0x0102;
const int	INT_UARTTX = 0x080;
volatile	int	*const TIMER = (volatile int *)0x0104;
#define	HAVE_TIMER
#endif

#ifdef	HAVE_SCOPE
volatile	int	*const SCOPE = (volatile int *)0x011e;
#endif

unsigned	zip_ucc(void);
void		zip_save_context(int *);
void		zip_halt(void);

asm("\t.section\t.start\n"
	"\t.global\t_start\n"
	"\t.type\t_start,@function\n"
"_start:\n"
#ifdef	HAVE_SCOPE
	"\tNOOP\n"
	"\tLOD\t286,R0\n"
	"\tROL\t16,R0\n"
	"\tTST\t0x1000,R0\n"
	"\tBZ\t_start\n"
	"\tOR\t0x0f00,R0\n"
	"\tROL\t16,R0\n"
	"\tSTO\tR0,286\n"
#endif
	"\tCLR\tR0\n"
	"\tCLR\tR1\n"
	"\tCLR\tR2\n"
	"\tCLR\tR3\n"
	"\tCLR\tR4\n"
	"\tCLR\tR5\n"
	"\tCLR\tR6\n"
	"\tCLR\tR7\n"
	"\tCLR\tR8\n"
	"\tCLR\tR9\n"
	"\tCLR\tR10\n"
	"\tCLR\tR11\n"
	"\tCLR\tR12\n"
	"\tLDI\t_top_of_stack,SP\n"
	"\tCLR\tCC\n"
	"\tMOV\tbusy_failure(PC),R0\n"
	"\tBRA\tentry\n"
"busy_failure:\n"
	"\tBUSY\n"
	"\t.section\t.text");

#ifdef	HAVE_COUNTER
#define	MARKSTART	start_time = *COUNTER
#define	MARKSTOP	stop_time  = *COUNTER
#else
#ifdef	HAVE_TIMER
#define	MARKSTART	start_time = *TIMER
#define	MARKSTOP	stop_time  = *TIMER
#else
#define	MARKSTART
#define	MARKSTOP
#endif
#endif


extern	int	run_test(void *pc, void *stack);
asm("\t.global\trun_test\n"
	"\t.type\trun_test,@function\n"
"run_test:\n"
	"\tCLR\tR3\n"
	"\tMOV\ttest_return(PC),uR0\n"
	"\tMOV\tR3,uR1\n"
	"\tMOV\tR3,uR2\n"
	"\tMOV\tR3,uR3\n"
	"\tMOV\tR3,uR4\n"
	"\tMOV\tR3,uR5\n"
	"\tMOV\tR3,uR6\n"
	"\tMOV\tR3,uR7\n"
	"\tMOV\tR3,uR8\n"
	"\tMOV\tR3,uR9\n"
	"\tMOV\tR3,uR10\n"
	"\tMOV\tR1,uR11\n"
	"\tMOV\tR1,uR12\n"
	"\tMOV\tR2,uSP\n"
	"\tMOV\t0x20+R3,uCC\n"
	"\tMOV\tR1,uPC\n"
	"\tRTU\n"
"test_return:\n"
	"\tMOV\tuR1,R1\n"
	"\tAND\t0xffffffdf,CC\n"
	// Works with 5 NOOPS, works with 3 NOOPS, works with 1 NOOP
	"\tJMP\tR0\n");

void	break_one(void);
asm("\t.global\tbreak_one\n"
	"\t.type\tbreak_one,@function\n"
"break_one:\n"
	"\tLDI\t0,R1\n"
	"\tBREAK\n"
	"\tLDI\t1,R1\n"	// Test fails
	"\tJMP\tR0");

void	break_two(void);
asm("\t.global\tbreak_two\n"
	"\t.type\tbreak_two,@function\n"
"break_two:\n"
	"\tLDI\t0,R1\n"
	"\tJMP\tR0\n"
	"\tBREAK\n");

void	early_branch_test(void);
asm("\t.global\tearly_branch_test\n"
	"\t.type\tearly_branch_test,@function\n"
"early_branch_test:\n"
	"\tLDI\t1,R1\n"
	"\tBRA\t_eb_a\n"
	"\tBREAK\n"	
"_eb_a:\n"
	"\tLDI\t2,R1\n"
	"\tBRA\t_eb_b\n"
	"\tNOP\n"
	"\tBREAK\n"
"_eb_b:\n"
	"\tLDI\t3,R1\n"
	"\tBRA\t_eb_c\n"
	"\tNOP\n"
	"\tNOP\n"
	"\tBREAK\n"
"_eb_c:\n"
	"\tLDI\t4,R1\n"
	"\tBRA\t_eb_d\n"
	"\tNOP\n"
	"\tNOP\n"
	"\tNOP\n"
	"\tBREAK\n"
"_eb_d:\n"
	"\tLDI\t5,R1\n"
	"\tBRA\t_eb_e\n"
	"\tNOP\n"
	"\tNOP\n"
	"\tNOP\n"
	"\tNOP\n"
	"\tBREAK\n"
"_eb_e:\n"
	"\tLDI\t6,R1\n"
	"\tBRA\t_eb_f\n"
	"\tNOP\n"
	"\tNOP\n"
	"\tNOP\n"
	"\tNOP\n"
	"\tNOP\n"
	"\tBREAK\n"
"_eb_f:\n"
	"\tLDI\t0,R1\n"
	"\tJMP\tR0");

void	trap_test_and(void);
asm("\t.global\ttrap_test_and\n"
	"\t.type\ttrap_test_and,@function\n"
"trap_test_and:\n"
	"\tLDI\t0,R1\n"
	"\tAND\t0xffffffdf,CC\n"
	"\tLDI\t1,R1\n"	// Test fails
	"\tJMP\tR0");

void	trap_test_clr(void);
asm("\t.global\ttrap_test_clr\n"
	"\t.type\ttrap_test_clr,@function\n"
"trap_test_clr:\n"
	"\tLDI\t0,R1\n"
	"\tCLR\tCC\n"
	"\tLDI\t1,R1\n"	// Test fails
	"\tJMP\tR0");

void	overflow_test(void);
asm("\t.global\toverflow_test\n"
	"\t.type\toverflow_test,@function\n"
"overflow_test:\n"
	"\tLDI\t0,R1\n"
	"\tLDI\t0,R3\n"		// Clear our scorecard
// First test: does adding one to the maximum integer cause an overflow?
	"\tLDI\t-1,R2\n"
	"\tLSR\t1,R2\n"
	"\tADD\t1,R2\n"
	"\tOR.V\t1,R3\n"
// Second test: does subtracting one to the minimum integer cause an overflow?
	"\tLDI\t0x80000000,R2\n"
	"\tSUB\t1,R2\n"
	"\tOR.V\t2,R3\n"
// Third test, overflow from LSR
	"\tLDI\t0x80000000,R2\n"
	"\tLSR\t1,R2\n"		// Overflows 'cause the sign changes
	"\tOR.V\t4,R3\n"
// Fourth test, overflow from LSL
	"\tLDI\t0x40000000,R2\n"
	"\tLSL\t1,R2\n"
	"\tOR.V\t8,R3\n"
// Fifth test, overflow from LSL, negative to positive
	"\tLDI\t0x80000000,R2\n"
	"\tLSL\t1,R2\n"
	"\tOR.V\t16,R3\n"
// Record our scores
	"\tXOR\t31,R3\n"
	"\tOR\tR3,R1\n"
// And return the results
	"\tJMP\tR0");


void	carry_test(void);
asm("\t.global\tcarry_test\n"
	"\t.type\tcarry_test,@function\n"
"carry_test:\n"
	"\tLDI\t0,R1\n"
	"\tLDI\t0,R3\n"
// First, in adding
	"\tLDI\t-1,R2\n"
	"\tADD\t1,R2\n"
	"\tOR.C\t1,R3\n"
// Then, in subtraction
	"\tSUB\t1,R2\n"
	"\tOR.C\t2,R3\n"
// From a right shift
	"\tLDI\t1,R2\n"
	"\tLSR\t1,R2\n"
	"\tOR.C\t4,R3\n"
	"\tLDI\t1,R2\n"
	"\tASR\t1,R2\n"
	"\tOR.C\t8,R3\n"
// Or from a compare
	"\tLDI\t0,R2\n"
	"\tCMP\t1,R2\n"
	"\tOR.C\t16,R3\n"
// Set our return and clean up
	"\tXOR\t31,R3\n"
	"\tOR\tR3,R1\n"
	"\tJMP\tR0");

void	loop_test(void);
asm("\t.global\tloop_test\n"
	"\t.type\tloop_test,@function\n"
"loop_test:\n"
	"\tLDI\t0,R1\n"
// Let's try a loop: for(i=0; i<5; i++)
	"\tLDI\t0,R2\n"
	"\tLDI\t0,R3\n"
	"\tCMP\t5,R2\n"
	"\tBGE\tend_for_loop_test\n"
"for_loop_test:"
	"\tADD\t1,R2\n"
	"\tADD\t1,R3\n"
	"\tCMP\t5,R2\n"
	"\tBLT\tfor_loop_test\n"
"end_for_loop_test:"
	"\tCMP\t5,R3\n"
	"\tOR.NZ\t1,R1\n"
// How about a reverse do{} while loop?  These are usually cheaper than for()
// loops.
	"\tLDI\t0,R2\n"
	"\tLDI\t5,R3\n"
"bgt_loop_test:\n"
	"\tADD\t1,R2\n"
	"\tSUB\t1,R3\n"
	"\tBGT\tbgt_loop_test\n"
	"\tCMP\t5,R2\n"
	"\tOR.NZ\t2,R1\n"
// What if we use >=?
	"\tLDI\t0,R2\n"
	"\tLDI\t5,R3\n"
"bge_loop_test:\n"
	"\tADD\t1,R2\n"
	"\tSUB\t1,R3\n"
	"\tBGE\tbge_loop_test\n"
	"\tCMP\t6,R2\n"
	"\tOR.NZ\t4,R1\n"
// Once more with the reverse loop, this time storing the loop variable in
// memory
	"\tSUB\t1,SP\n"
	"\tLDI\t0,R2\n"
	"\tLDI\t5,R3\n"
	"\tSTO\tR3,(SP)\n"
"mem_loop_test:\n"
	"\tADD\t1,R2\n"
	"\tADD\t14,R3\n"
	"\tLOD\t(SP),R3\n"
	"\tSUB\t1,R3\n"
	"\tSTO\tR3,(SP)\n"
	"\tBGT\tmem_loop_test\n"
	"\tCMP\t5,R2\n"
	"\tOR.NZ\t8,R1\n"
	"\tADD\t1,SP\n"
//
	"\tJMP\tR0\n");

// Test whether or not LSL, LSR, and ASR instructions work, together with their
// carry flags
void	shift_test(void);
asm("\t.global\tshift_test\n"
	"\t.type\tshift_test,@function\n"
"shift_test:\n"
	"\tLDI\t0,R1\n"
	"\tLDI\t0,R3\n"
	"\tLDI\t0,R4\n"
// Does shifting right by 32 result in a zero?
	"\tLDI\t-1,R2\n"
	"\tLSR\t32,R2\n"
	"\tOR.Z\t1,R3\n"
	"\tOR.C\t2,R3\n"
	"\tCMP\t0,R2\n"
	"\tOR.Z\t4,R3\n"
// Does shifting a -1 right arithmetically by 32 result in a -1?
	"\tLDI\t-1,R2\n"
	"\tASR\t32,R2\n"
	"\tOR.LT\t8,R3\n"
	"\tOR.C\t16,R3\n"
	"\tCMP\t-1,R2\n"
	"\tOR.Z\t32,R3\n"
// Does shifting a -4 right arithmetically by 2 result in a -1?
	"\tLDI\t-4,R2\n"
	"\tASR\t2,R2\n"
	"\tOR.LT\t64,R3\n"
	"\tOR.C\t128,R1\n"
	"\tOR\t128,R3\n" // Artificially declare passing, so as not to fail it
	"\tCMP\t-1,R2\n"
	"\tOR.Z\t256,R3\n"
// Does one more set the carry flag as desired?
	"\tASR\t1,R2\n"
	"\tOR.LT\t512,R3\n"
	"\tOR.C\t1024,R3\n"
	"\tCMP\t-1,R2\n"
	"\tOR.Z\t2048,R3\n"
// Does shifting -1 left by 32 result in a zero?
	"\tLDI\t-1,R2\n"
	"\tLSL\t32,R2\n"
	"\tOR.Z\t4096,R3\n"
	"\tOR.C\t8192,R3\n"	
	"\tCMP\t0,R2\n"
	"\tOR.Z\t16384,R3\n"
// How about shifting by zero?
	"\tLDI\t-1,R2\n"
	"\tASR\t0,R2\n"
	"\tOR.C\t32768,R1\n"
	"\tOR\t32768,R3\n"
	"\tCMP\t-1,R2\n"
	"\tOR.Z\t1,R4\n"
// 
	"\tLSR\t0,R2\n"
	"\tOR.C\t131072,R1\n"
	"\tCMP\t-1,R2\n"
	"\tOR.Z\t2,R4\n"
//
	"\tLSL\t0,R2\n"
	"\tOR.C\t524288,R1\n"
	"\tCMP\t-1,R2\n"
	"\tOR.Z\t4,R4\n"
// Tally up our results and return
	"\tXOR\t7,R4\n"
	"\tXOR\t65535,R3\n"
	"\tLSL\t16,R4\n"
	"\tOR\tR4,R3\n"
	"\tOR\tR3,R1\n"
	"\tJMP\tR0");

int	sw_brev(int v);
asm("\t.global\tsw_brev\n"
	"\t.type\tsw_brev,@function\n"
"sw_brev:\n"
	"\tSUB\t2,SP\n"
	"\tSTO\tR2,(SP)\n"
	"\tSTO\tR3,1(SP)\n"
	"\tLDI\t-1,R2\n"
	"\tCLR\tR3\n"
"sw_brev_loop:\n"
	"\tLSL\t1,R3\n"
	"\tLSR\t1,R1\n"
	"\tOR.C\t1,R3\n"
	"\tLSR\t1,R2\n"
	"\tBZ\tsw_brev_endloop\n"
	"\tBRA\tsw_brev_loop\n"
"sw_brev_endloop:\n"
	"\tMOV\tR3,R1\n"
	"\tLOD\t(SP),R2\n"
	"\tLOD\t1(SP),R3\n"
	"\tADD\t2,SP\n"
	"\tJMP\tR0");

void	pipeline_stack_test(void);
asm("\t.global\tpipeline_stack_test\n"
	"\t.type\tpipeline_stack_test,@function\n"
"pipeline_stack_test:\n"
	"\tSUB\t1,SP\n"
	"\tSTO\tR0,(SP)\n"
	"\tLDI\t0,R0\n"
	"\tMOV\t1(R0),R1\n"
	"\tMOV\t1(R1),R2\n"
	"\tMOV\t1(R2),R3\n"
	"\tMOV\t1(R3),R4\n"
	"\tMOV\t1(R4),R5\n"
	"\tMOV\t1(R5),R6\n"
	"\tMOV\t1(R6),R7\n"
	"\tMOV\t1(R7),R8\n"
	"\tMOV\t1(R8),R9\n"
	"\tMOV\t1(R9),R10\n"
	"\tMOV\t1(R10),R11\n"
	"\tMOV\t1(R11),R12\n"
	"\tMOV\tpipeline_stack_test_component_return(PC),R0\n"
	// "\tLJMP\tpipeline_stack_test_component\n"
	"\tBRA\tpipeline_stack_test_component\n"
"pipeline_stack_test_component_return:\n"
	"\tCMP\t1,R1\n"
	"\tLDI.Z\t0,R1\n"
	"\tCMP\t2,R2\n"
	"\tCMP.Z\t3,R3\n"
	"\tCMP.Z\t4,R4\n"
	"\tCMP.Z\t5,R5\n"
	"\tCMP.Z\t6,R6\n"
	"\tCMP.Z\t7,R7\n"
	"\tCMP.Z\t8,R8\n"
	"\tCMP.Z\t9,R9\n"
	"\tCMP.Z\t10,R10\n"
	"\tCMP.Z\t11,R11\n"
	"\tCMP.Z\t12,R12\n"
	"\tBREV.NZ\t-1,R1\n"
	"\tLOD\t(SP),R0\n"
	"\tADD\t1,SP\n"
	"\tJMP\tR0\n"
	);

void	pipeline_stack_test_component(void);
asm("\t.global\tpipeline_stack_test_component\n"
	"\t.type\tpipeline_stack_test_component,@function\n"
"pipeline_stack_test_component:\n"
	"\tSUB\t13,SP\n"
	"\tSTO\tR0,(SP)\n"
	"\tSTO\tR1,1(SP)\n"
	"\tSTO\tR2,2(SP)\n"
	"\tSTO\tR3,3(SP)\n"
	"\tSTO\tR4,4(SP)\n"
	"\tSTO\tR5,5(SP)\n"
	"\tSTO\tR6,6(SP)\n"
	"\tSTO\tR7,7(SP)\n"
	"\tSTO\tR8,8(SP)\n"
	"\tSTO\tR9,9(SP)\n"
	"\tSTO\tR10,10(SP)\n"
	"\tSTO\tR11,11(SP)\n"
	"\tSTO\tR12,12(SP)\n"
	"\tXOR\t-1,R0\n"
	"\tXOR\t-1,R1\n"
	"\tXOR\t-1,R2\n"
	"\tXOR\t-1,R3\n"
	"\tXOR\t-1,R4\n"
	"\tXOR\t-1,R5\n"
	"\tXOR\t-1,R6\n"
	"\tXOR\t-1,R7\n"
	"\tXOR\t-1,R8\n"
	"\tXOR\t-1,R9\n"
	"\tXOR\t-1,R10\n"
	"\tXOR\t-1,R11\n"
	"\tXOR\t-1,R12\n"
	"\tLOD\t(SP),R0\n"
	"\tLOD\t1(SP),R1\n"
	"\tLOD\t2(SP),R2\n"
	"\tLOD\t3(SP),R3\n"
	"\tLOD\t4(SP),R4\n"
	"\tLOD\t5(SP),R5\n"
	"\tLOD\t6(SP),R6\n"
	"\tLOD\t7(SP),R7\n"
	"\tLOD\t8(SP),R8\n"
	"\tLOD\t9(SP),R9\n"
	"\tLOD\t10(SP),R10\n"
	"\tLOD\t11(SP),R11\n"
	"\tLOD\t12(SP),R12\n"
	"\tADD\t13,SP\n"
	"\tJMP\tR0\n");

//mpy_test
void	mpy_test(void);
asm("\t.global\tmpy_test\n"
	"\t.type\tmpy_test,@function\n"
"mpy_test:\n"
	"\tCLR\tR1\n"
	// First test: let's count multiples of 137
	"\tLDI\t137,R2\n"	// What we're doing multiples of
	"\tCLR\tR3\n"		// Our accumulator via addition
	"\tCLR\tR4\n"		// Our index for multiplication
	"mpy_137_test_loop:\n"
	"\tMOV\tR2,R5\n"
	"\tMPY\tR4,R5\n"
	"\tCMP\tR3,R5\n"
	"\tBNZ\tend_mpy_137_test_loop_failed\n"
	// Let's try negative while we are at it
	"\tMOV\tR2,R6\n"
	"\tNEG\tR6\n"
	"\tMPY\tR4,R6\n"
	"\tNEG\tR6\n"
	"\tCMP\tR3,R6\n"
	"\tBNZ\tend_mpy_137_test_loop_failed\n"
	"\tCLR\tR6\n"
	"\tTEST\t0xffff0000,R3\n"
	"\tBNZ\tend_mpy_137_test_loop\n"
	"\tADD\tR2,R3\n"
	"\tADD\t1,R4\n"
	"\tBRA\tmpy_137_test_loop\n"
"end_mpy_137_test_loop_failed:\n"
	"\tOR\t1,R1\n"
"end_mpy_137_test_loop:\n"
	// Second test ... whatever that might be
	"\tJMP\tR0\n");

//brev_test
//pipeline_test -- used to be called pipeline memory race conditions
void	pipeline_test(void);
asm("\t.global\tpipeline_test\n"
	"\t.type\tpipeline_test,@function\n"
"pipeline_test:\n"
	"\tSUB\t2,SP\n"
	// Test setup
	"\tLDI\t275,R2\n"
	"\tSTO\tR2,1(SP)\n"
	"\tMOV\t1(SP),R2\n"
	"\tSTO\tR2,(SP)\n"
	"\tCLR\tR2\n"
	//
	"\tMOV\tSP,R2\n"
	"\tLOD\t(R2),R2\n"
	"\tLOD\t(R2),R2\n"
	"\tCMP\t275,R2\n"
	"\tOR.NZ\t1,R1\n"
	//
	"\tMOV\tSP,R2\n"
	// Here's the test sequence
	"\tLOD\t(R2),R3\n"
	"\tLOD\t1(R2),R4\n"
	"\tSTO\tR4,1(R3)\n"
	// Make sure we clear the load pipeline
	"\tLOD\t(R2),R3\n"
	// Load our written value
	"\tLOD\t2(R2),R4\n"
	"\tCMP\t275,R4\n"
	"\tOR.NZ\t2,R1\n"
	//
	//
	// Next (once upon a time) failing sequence:
	//	LOD -x(R12),R0
	//	LOD y(R0),R0
	"\tMOV\tSP,R2\n"
	"\tMOV\t1(R2),R3\n"
	"\tSTO\tR3,1(R2)\n"
	"\tLDI\t3588,R4\n"	// Just some random value
	"\tSTO\tR4,2(R2)\n"
	"\tMOV\tR2,R3\n"
	// Here's the test sequence
	"\tLOD\t(R2),R3\n"
	"\tLOD\t1(R3),R3\n"
	"\tCMP\tR4,R3\n"
	"\tOR.NZ\t4,R1\n"
	//
	"\tADD\t2,SP\n"
	"\tJMP\tR0\n");

//mempipe_test
void	mempipe_test(void);
asm("\t.global\tmempipe_test\n"
	"\t.type\tmempipe_test,@function\n"
"mempipe_test:\n"
	"\tSUB\t4,SP\n"
	"\tSTO\tR0,(SP)\n"
	"\tLDI\t0x1000,R11\n"
	// Test #1 ... Let's start by writing a value to memory
	"\tLDI\t-1,R2\n"
	"\tCLR\tR3\n"
	"\tSTO\tR2,2(SP)\n"
	"\tLOD\t2(SP),R3\n"
	"\tCMP\tR3,R2\n"
	"\tOR.NZ\t1,R1\n"
	// Test #2, reading and then writing a value from memory
	"\tNOOP\n"
	"\tNOOP\n"
	"\tCLR\tR2\n"
	"\tCLR\tR3\n"
	"\tLOD\t2(SP),R2\n"	// This should load back up our -1 value
	"\tSTO\tR2,3(SP)\n"
	// Insist that the pipeline clear
	"\tLOD\t2(SP),R2\n"
	// Now let's try loading into R3
	"\tNOOP\n"
	"\tNOOP\n"
	"\tNOOP\n"
	"\tNOOP\n"
	"\tLOD\t3(SP),R3\n"
	"\tCMP\tR3,R2\n"
	"\tOR.NZ\t2,R1\n"
	//
	"\tLOD\t(SP),R0\n"
	"\tADD\t4,SP\n"
	"\tJMP\tR0\n");

//cexec_test
void	cexec_test(void);
asm("\t.global\tcexec_test\n"
	"\t.type\tcexec_test,@function\n"
"cexec_test:\n"
	"\tSUB\t1,SP\n"
	"\tSTO\tR0,(SP)\n"
	//
	"\tXOR\tR2,R2\n"
	"\tADD.Z\t1,R2\n"
	"\tADD.NZ\t1,R1\n"
	"\tCMP.Z\t0,R2\n"
	"\tOR.Z\t2,R1\n"
	//
	"\tLOD\t(SP),R0\n"
	"\tADD\t1,SP\n"
	"\tJMP\tR0\n");

// Pipeline stalls have been hideous problems for me.  The CPU has been modified
// with special logic to keep stages from stalling.  For the most part, this
// means that ALU and memory results may be accessed either before or as they
// are written to the register file.  This set of code is designed to test
// whether this bypass logic works.
//
//nowaitpipe_test
void	nowaitpipe_test(void);
asm("\t.global\tnowaitpipe_test\n"
	"\t.type\tnowaitpipe_test,@function\n"
"nowaitpipe_test:\n"
	"\tSUB\t2,SP\n"
	//
	// Let's start with ALU-ALU testing
	//	AA: result->input A
	"\tLDI\t-1,R2\n"
	"\tCLR\tR2\n"
	"\tADD\t1,R2\n"
	"\tCMP\t1,R2\n"
	"\tOR.NZ\t1,R1\n"
	//
	//	AA: result -> input B
	"\tCLR\tR2\n"
	"\tCLR\tR3\n"
	"\tADD\t1,R2\n"
	"\tCMP\tR2,R3\n"
	"\tOR.Z\t2,R1\n"
	//	AA: result -> input A on condition
	"\tXOR\tR2,R2\n"
	"\tADD.Z\t5,R2\n"
	"\tCMP\t5,R2\n"
	"\tOR.NZ\t4,R1\n"
	//	AA: result -> input B on condition
	"\tCLR\tR2\n"
	"\tXOR\tR3,R3\n"
	"\tADD.Z\t5,R2\n"
	"\tCMP\tR2,R3\n"
	"\tOR.Z\t8,R1\n"
	//	AA: result->input B plus offset
	"\tCLR\tR2\n"
	"\tXOR\tR3,R3\n"
	"\tADD\t5,R2\n"
	"\tCMP\t-5(R2),R3\n"
	"\tOR.NZ\t16,R1\n"
	//	AA: result->input B plus offset on condition
	"\tCLR\tR2\n"
	"\tXOR\tR3,R3\n"
	"\tADD.Z\t5,R2\n"
	"\tCMP\t-5(R2),R3\n"
	"\tOR.NZ\t32,R1\n"
	//
	// Then we need to do the ALU-MEM input testing
	//
	"\tCLR\tR2\n"
	"\tSTO\tR2,1(SP)\n"
	"\tLDI\t8352,R2\n"
	"\tLOD\t1(SP),R2\n"
	"\tTST\t-1,R2\n"
	"\tOR.NZ\t64,R1\n"
	// Let's try again, this time with something that's not zero
	"\tLDI\t937,R2\n"
	"\tSTO\tR2,1(SP)\n"
	"\tNOOP\n"
	"\tLOD\t1(SP),R2\n"
	"\tCMP\t938,R2\n"
	"\tOR.GE\t128,R1\n"
	"\tCMP\t936,R2\n"
	"\tOR.LT\t256,R1\n"
	// Mem output->ALU input testing
	//	Okay, we just did that as part of our last test
	// Mem output->mem input testing
	"\tLDI\t5328,R2\n"
	"\tLOD\t1(SP),R2\n"
	"\tSTO\tR2,1(SP)\n"
	"\tLOD\t1(SP),R3\n"
	"\tCMP\t937,R3\n"
	"\tOR.NZ\t512,R1\n"
	//
	"\tADD\t2,SP\n"
	"\tJMP\tR0\n");

//bcmem_test
void	bcmem_test(void);
asm("\t.global\tbcmem_test\n"
	"\t.type\tbcmem_test,@function\n"
"bcmem_test:\n"
	"\tSUB\t1,SP\n"
	"\tCLR\tR1\n"
	"\tCLR\tR2\n"
	"\tLDI\t-1,R3\n"
	"\tLDI\t0x13000,R4\n"
	"\tSTO\tR2,(SP)\n"
	"\tLOD\t(SP),R3\n"
	"\tCMP\tR2,R3\n"
	"\tOR.NZ\t1,R1\n"
	"\tCMP\t0x13000,R4\n"
	"\tBZ\tbcmem_test_cmploc_1\n"
	"\tSTO\tR4,(SP)\n"
"bcmem_test_cmploc_1:\n"
	"\tLOD\t(SP),R2\n"
	"\tCMP\tR2,R4\n"
	"\tOR.Z\t2,R1\n"
	"\tCLR\tR2\n"
	"\tCMP\tR2,R4\n"
	"\tBZ\tbcmem_test_cmploc_2\n"
	"\tSTO.NZ\tR4,(SP)\n"
"bcmem_test_cmploc_2:\n"
	"\tLOD\t(SP),R2\n"
	"\tCMP\tR2,R4\n"
	"\tOR.NZ\t4,R1\n"
//
	"\tADD\t1,SP\n"
	"\tJMP\tR0\n");

//
// The CC register has some ... unique requirements associated with it.
// Particularly, flags are unavailable until after an ALU operation completes,
// and they can't really be bypassed for the CC register.  After writeback,
// the "new" CC register isn't really available for another clock.  Trying to
// bypass this extra clock can have problems, since ... some bits are fixed,
// some bits can only be changed by the supervisor, and others can/will change
// and even have effects--like sending the CPU to supervisor mode or
// alternatively to sleep.
//
// Here, let's see if our pipeline can successfully navigate any of these
// issues.
//
void	ccreg_test(void);
asm("\t.global\tccreg_test\n"
	"\t.type\tccreg_test,@function\n"
"ccreg_test:\n"
	// First test: If we try to change the fixed bits, will they change
	// because the pipeline tries to bypass the write-back stage
	"\tCLR\tR1\n"	// We'll start with an "answer" of success
	"\tMOV\tCC,R2\n"
	"\tMOV\tR2,R4\n"	// Keep a copy
	"\tBREV\t0x0ff,R3\n"	// Attempt to change the top fixed bits
	"\tXOR\tR3,R2\n"	// Arrange for the changes
	"\tMOV\tR2,CC\n"	// Set the changes (they won't take)
	"\tMOV\tCC,R5\n"	// See if the pipeline makes them take
	"\tXOR\tR4,R5\n"	// Let's look for anything that has changed
	"\tOR.NZ\t1,R1\n"	// If anything has changed, then we fail the tst
	// 
	// Test #2: Can we set the flags?
	"\tMOV\tCC,R6\n"
	"\tOR\t15,R6\n"
	"\tMOV\tR6,CC\n"
	"\tMOV\tCC,R7\n"
	"\tAND\t15,R7\n"
	"\tCMP\t15,R7\n"
	"\tOR.NZ\t2,R1\n"
	//
	// Test #3: How about setting specific flags, and immediately acting
	// on them?
	"\tXOR\t1+R8,R8\n"	// Turn off the Z bit
	"\tOR\t1,CC\n"		// Turn on the Z bit
	"\tOR.NZ\t4,R1\n"
	//
	// Test #4: Can we load the CC plus a value into a register?
	//	I don't think so ...
	"\tJMP\tR0\n");

// Multiple argument test
__attribute__((noinline))
int	multiarg_subroutine(int a, int b, int c, int d, int e, int f, int g) {
	if (a!=0)	return 1;
	if (b!=1)	return 2;
	if (c!=2)	return 4;
	if (d!=3)	return 8;
	if (e!=4)	return 16;
	if (f!=5)	return 32;
	if (g!=6)	return 64;
	return 0;
}

int	multiarg_test(void) {
	return multiarg_subroutine(0,1,2,3,4,5,6);
}

__attribute__((noinline))
void	wait(unsigned int msk) {
	*PIC = 0x7fff0000|msk;
	asm("MOV\tidle_task(PC),uPC\n");
	*PIC = 0x80000000|(msk<<16);
	asm("WAIT\n");
	*PIC = 0; // Turn interrupts back off, lest they confuse the test
}

asm("\nidle_task:\n\tWAIT\n\tBRA\tidle_task\n");

__attribute__((noinline))
void	txchr(char v) {
	wait(INT_UARTTX);
	*UARTTX = v;
}

__attribute__((noinline))
void	txstr(const char *str) {
	const char *ptr = str;
	while(*ptr)
		txchr(*ptr++);
}

__attribute__((noinline))
void	txhex(int num) {
	for(int ds=28; ds>=0; ds-=4) {
		int	ch;
		ch = (num >> ds)&0x0f;
		if (ch >= 10)
			ch = 'A'+ch-10;
		else
			ch += '0';
		txchr(ch);
	}
}

__attribute__((noinline))
void	txreg(const char *name, int val) {
	txstr(name);	// 4 characters
	txstr("0x");	// 2 characters
	txhex(val);	// 8 characters
	txstr("    ");	// 4 characters
}

__attribute__((noinline))
void	save_context(int *context) {
	zip_save_context(context);
}

__attribute__((noinline))
void	test_fails(int start_time, int *listno) {
	int	context[16], stop_time;

	// Trigger the scope, if it hasn't already triggered.  Otherwise,
	// if it has triggered, don't clear it.
#ifdef	HAVE_SCOPE
	*SCOPE = 0x8f000004;
#endif

	MARKSTOP;
	save_context(context);
	*listno++ = context[1];
	*listno++ = context[14];
	*listno++ = context[15];
#ifdef	HAVE_COUNTER
	*listno   = stop_time;
#endif

	txstr("FAIL!\r\n\r\n");
	txstr("Between 0x"); txhex(start_time);
		txstr(" and 0x"); txhex(stop_time); txstr("\r\n\r\n");
	txstr("Core-dump:\r\n");
	txreg("uR0 : ", context[0]);
	txreg("uR1 : ", context[1]);
	txreg("uR2 : ", context[2]);
	txreg("uR3 : ", context[3]);
	txstr("\r\n");

	txreg("uR4 : ", context[4]);
	txreg("uR5 : ", context[5]);
	txreg("uR6 : ", context[6]);
	txreg("uR7 : ", context[7]);
	txstr("\r\n");

	txreg("uR8 : ", context[8]);
	txreg("uR9 : ", context[9]);
	txreg("uR10: ", context[10]);
	txreg("uR11: ", context[11]);
	txstr("\r\n");

	txreg("uR12: ", context[12]);
	txreg("uSP : ", context[13]);
	txreg("uCC : ", context[14]);
	txreg("uPC : ", context[15]);
	txstr("\r\n\r\n");

	asm("\tBUSY");
}

void	testid(const char *str) {
	const int	WIDTH=32;
	txstr(str);
	const char *ptr = str;
	int	i = 0;
	while(0 != *ptr++)
		i++;
	i = WIDTH-i;
	while(i-- > 0)
		txchr(' ');
}

int	testlist[32];

void entry(void) {
	int	context[16];
	int	user_stack[256], *user_stack_ptr = &user_stack[256];
	int	start_time, i;

	for(i=0; i<32; i++)
		testlist[i] = -1;

#ifdef	HAVE_TIMER
	*TIMER = 0x7fffffff;
#endif
#ifdef	HAVE_COUNTER
	*COUNTER = 0;
#endif

// #define	STACKTEST	asm("CMP\t16108,SP\n\tHALT.NZ\n")
#define	STACKTEST
	STACKTEST;

	// *UART_CTRL = 8333; // 9600 Baud, 8-bit chars, no parity, one stop bit
	*UART_CTRL = 25; // 9600 Baud, 8-bit chars, no parity, one stop bit
	//
	STACKTEST;

	txstr("\r\n");
	txstr("Running CPU self-test\n");
	txstr("-----------------------------------\r\n");

	int	tnum = 0;
	STACKTEST;

	// Test break instruction in user mode
	// Make sure the break works as designed
	testid("Break test #1"); MARKSTART;
	STACKTEST;

	if ((run_test(break_one, user_stack_ptr))||(zip_ucc()&0x1f50))
		test_fails(start_time, &testlist[tnum]);
	STACKTEST;

	save_context(context);
	if (context[15] != (int)break_one+1)
		test_fails(start_time, &testlist[tnum]);
	if (0==(zip_ucc()&0x80))
		test_fails(start_time, &testlist[tnum]);
	txstr("Pass\r\n"); testlist[tnum++] = 0;	// 0

	STACKTEST;

	// Test break instruction in user mode
	// Make sure that a decision on the clock prior won't still cause a 
	// break condition
	testid("Break test #2"); MARKSTART;
	if ((run_test(break_two, user_stack_ptr))||(zip_ucc()&0x1f10))
		test_fails(start_time, &testlist[tnum]);
	txstr("Pass\r\n"); testlist[tnum++] = 0;	// #1

	// LJMP test ... not (yet) written

	// Test the early branching capability
	//	Does it successfully clear whatever else is in the pipeline?
	testid("Early Branch test"); MARKSTART;
	if ((run_test(early_branch_test, user_stack_ptr))||(zip_ucc()&0x01d90))
		test_fails(start_time, &testlist[tnum]);
	txstr("Pass\r\n"); testlist[tnum++] = 0;	// #2

	// TRAP test
	testid("Trap test/AND"); MARKSTART;
	if ((run_test(trap_test_and, user_stack_ptr))||(zip_ucc()&0x01d90))
		test_fails(start_time, &testlist[tnum]);
	if ((zip_ucc() & 0x0200)==0)
		test_fails(start_time, &testlist[tnum]);
	txstr("Pass\r\n"); testlist[tnum++] = 0;	// #3

	testid("Trap test/CLR"); MARKSTART;
	if ((run_test(trap_test_clr, user_stack_ptr))||(zip_ucc()&0x01d90))
		test_fails(start_time, &testlist[tnum]);
	if ((zip_ucc() & 0x0200)==0)
		test_fails(start_time, &testlist[tnum]);
	txstr("Pass\r\n"); testlist[tnum++] = 0;	// #4

	// Overflow test
	testid("Overflow test"); MARKSTART;
	if ((run_test(overflow_test, user_stack_ptr))||(zip_ucc()&0x01d90))
		test_fails(start_time, &testlist[tnum]);
	txstr("Pass\r\n"); testlist[tnum++] = 0;	// #5

	// Carry test
	testid("Carry test"); MARKSTART;
	if ((run_test(carry_test, user_stack_ptr))||(zip_ucc()&0x01d90))
		test_fails(start_time, &testlist[tnum]);
	txstr("Pass\r\n"); testlist[tnum++] = 0;	// #6

	// LOOP_TEST
	testid("Loop test"); MARKSTART;
	if ((run_test(loop_test, user_stack_ptr))||(zip_ucc()&0x01d90))
		test_fails(start_time, &testlist[tnum]);
	txstr("Pass\r\n"); testlist[tnum++] = 0;	// #7 -- FAILS

	// SHIFT_TEST
	testid("Shift test"); MARKSTART;
	if ((run_test(shift_test, user_stack_ptr))||(zip_ucc()&0x01d90))
		test_fails(start_time, &testlist[tnum]);
	txstr("Pass\r\n"); testlist[tnum++] = 0;	// #8

	// MPY_TEST
	testid("Multiply test"); MARKSTART;
	if ((run_test(mpy_test, user_stack_ptr))||(zip_ucc()&0x01d90))
		test_fails(start_time, &testlist[tnum]);
	txstr("Pass\r\n"); testlist[tnum++] = 0;	// #9

	// BREV_TEST
	//testid("BREV/stack test"); MARKSTART;
	//if ((run_test(brev_test, user_stack_ptr))||(zip_ucc()&0x01d90))
		//test_fails(start_time);
	//txstr("Pass\r\n");

	// PIPELINE_TEST
	testid("Pipeline test"); MARKSTART;
	if ((run_test(pipeline_test, user_stack_ptr))||(zip_ucc()&0x01d90))
		test_fails(start_time, &testlist[tnum]);
	txstr("Pass\r\n"); testlist[tnum++] = 0;	// #10

	// MEM_PIPELINE_STACK_TEST
	testid("Mem-Pipeline test"); MARKSTART;
	if ((run_test(mempipe_test, user_stack_ptr))||(zip_ucc()&0x01d90))
		test_fails(start_time, &testlist[tnum]);
	txstr("Pass\r\n"); testlist[tnum++] = 0;	// #11

	// CONDITIONAL EXECUTION test
	testid("Conditional Execution test"); MARKSTART;
	if ((run_test(cexec_test, user_stack_ptr))||(zip_ucc()&0x01d90))
		test_fails(start_time, &testlist[tnum]);
	txstr("Pass\r\n"); testlist[tnum++] = 0;	// #12 -- FAILS

	// NOWAIT pipeline test
	testid("No-waiting pipeline test"); MARKSTART;
	if ((run_test(nowaitpipe_test, user_stack_ptr))||(zip_ucc()&0x01d90))
		test_fails(start_time, &testlist[tnum]);
	txstr("Pass\r\n"); testlist[tnum++] = 0;	// #13

	// BCMEM test
	testid("Conditional Branching test"); MARKSTART;
	if ((run_test(bcmem_test, user_stack_ptr))||(zip_ucc()&0x01d90))
		test_fails(start_time, &testlist[tnum]);
	txstr("Pass\r\n"); testlist[tnum++] = 0;	// #14

	// Illegal Instruction test
	testid("Illegal Instruction test"); MARKSTART;
	if ((run_test(NULL, user_stack_ptr))||((zip_ucc()^0x100)&0x01d90))
		test_fails(start_time, &testlist[tnum]);
	txstr("Pass\r\n"); testlist[tnum++] = 0;

	// Pipeline memory race condition test
	// DIVIDE test

	// CC Register test
	testid("CC Register test"); MARKSTART;
	if ((run_test(ccreg_test, user_stack_ptr))||(zip_ucc()&0x01d90))
		test_fails(start_time, &testlist[tnum]);
	txstr("Pass\r\n"); testlist[tnum++] = 0;

	// Multiple argument test
	testid("Multi-Arg test"); MARKSTART;
	if ((run_test(multiarg_test, user_stack_ptr))||(zip_ucc()&0x01d90))
		test_fails(start_time, &testlist[tnum]);
	txstr("Pass\r\n"); testlist[tnum++] = 0;

	txstr("\r\n");
	txstr("-----------------------------------\r\n");
	txstr("All tests passed.  Halting CPU.\n");
	zip_halt();
}

// To build this:
//	zip-gcc -O3 -Wall -Wextra -nostdlib -fno-builtin -T xula.ld -Wl,-Map,cputest.map cputest.cpp -o cputest
//	zip-objdump -D cputest > cputest.txt
//
