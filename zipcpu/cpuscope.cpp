//
//
// Filename: 	cpuscope.cpp
//
// Project:	FPGA library development (Basys-3 development board)
//
// Purpose:	To read out, and decompose, the results of the wishbone scope
//		as applied to the ICAPE2 interaction.
//
// Creator:	Dan Gisselquist
//		Gisselquist Tecnology, LLC
//
// Copyright:	2015
//
//
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <strings.h>
#include <ctype.h>
#include <string.h>
#include <signal.h>
#include <assert.h>

#include "usbi.h"
#include "port.h"
#include "llcomms.h"
#include "regdefs.h"

#define	WBSCOPE		R_CPUSCOPE
#define	WBSCOPEDATA	R_CPUSCOPED

#include "zopcodes.h"

FPGA	*m_fpga;
void	closeup(int v) {
	m_fpga->kill();
	exit(0);
}

unsigned brev(const unsigned v) {
	unsigned int r, a;
	a = v;
	r = 0;
	for(int i=0; i<8; i++) {
		r <<= 1;
		r |= (a&1);
		a >>= 1;
	} return r;
}

unsigned wrev(const unsigned v) {
	unsigned r = brev(v&0x0ff);
	r |= brev((v>>8)&0x0ff)<<8;
	return r;
}

int main(int argc, char **argv) {
	FPGAOPEN(m_fpga);

	signal(SIGSTOP, closeup);
	signal(SIGHUP, closeup);

	unsigned	v, lgln, scoplen;
	v = m_fpga->readio(WBSCOPE);
	if (0x60000000 != (v & 0x60000000)) {
		printf("Scope is not yet ready:\n");
		printf("\tRESET:\t\t%s\n", (v&0x80000000)?"Ongoing":"Complete");
		printf("\tSTOPPED:\t%s\n", (v&0x40000000)?"Yes":"No");
		printf("\tTRIGGERED:\t%s\n", (v&0x20000000)?"Yes":"No");
		printf("\tPRIMED:\t\t%s\n", (v&0x10000000)?"Yes":"No");
		printf("\tMANUAL:\t\t%s\n", (v&0x08000000)?"Yes":"No");
		printf("\tDISABLED:\t%s\n", (v&0x04000000)?"Yes":"No");
		printf("\tZERO:\t\t%s\n", (v&0x02000000)?"Yes":"No");
		exit(0);
	} else printf("SCOPD = %08x\n", v);

	lgln = (v>>20) & 0x1f;
	scoplen = (1<<lgln);

	DEVBUS::BUSW	*buf;
	buf = new DEVBUS::BUSW[scoplen];

	if (false) {
		m_fpga->readz(WBSCOPEDATA, scoplen, buf);
	} else {
		for(unsigned int i=0; i<scoplen; i++)
			buf[i] = m_fpga->readio(WBSCOPEDATA);
	}

	for(unsigned int i=0; i<scoplen; i++) {
		char	sbuf[64];

		if ((i>0)&&(buf[i] == buf[i-1])&&
				(i<scoplen-1)&&(buf[i] == buf[i+1]))
			continue;
		printf("%6d %08x:", i, buf[i]);

		unsigned addr = (buf[i]>>24)&0x0ff;
		zipi_to_string(m_fpga->readio(0x02000+addr),sbuf);
		printf(" %2x %-24s", (buf[i]>>24)&0x0ff, sbuf);
		printf(" %s%s%s%s%s %s%s%s",
			((buf[i]>>23)&1)?"P":" ",
			((buf[i]>>22)&1)?"D":" ",
			((buf[i]>>21)&1)?"O":" ",
			((buf[i]>>20)&1)?"A":" ",
			((buf[i]>>19)&1)?"M":" ",
			((buf[i]>>18)&1)?"o":" ",
			((buf[i]>>17)&1)?"a":" ",
			((buf[i]>>16)&1)?"m":" ");
		printf(" A=%02x ", (buf[i]>>8)&0x0ff);
		printf(" %s%02x ",
			(((buf[i]>>16)&3)!=0)?"W->":"(w)",
			(buf[i]&0x0ff));
		/*
		printf("%s", ((buf[i]>>31)&1)?"OpV":"   ");
		printf("%s", ((buf[i]>>30)&1)?"opA":"   ");
		printf("%s", ((buf[i]>>29)&1)?"AlV":"   ");
		printf("%s", ((buf[i]>>28)&1)?"AlW":"   ");
		printf("%s", ((buf[i]>>27)&1)?"opM":"   ");
		printf("%s", ((buf[i]>>26)&1)?"MmV":"   ");
		if (true) {
			int	op = (buf[i]>>22)&0x0f;
			switch(op) {
			case  0: printf("CMP "); break;
			case  1: printf("TST "); break;
			case  2: printf("MOV "); break;
			case  3: printf("LDI "); break;
			case  4: printf("AUX "); break;
			case  5: printf("ROL "); break;
			case  6: printf("LOD "); break;
			case  7: printf("STO "); break;
			case  8: printf("SUB "); break;
			case  9: printf("AND "); break;
			case 10: printf("ADD "); break;
			case 11: printf(" OR "); break;
			case 12: printf("XOR "); break;
			case 13: printf("LSL "); break;
			case 14: printf("ASR "); break;
			case 15: printf("LSR "); break;
			default: printf("ILL "); break;
			}
		} else
			printf("%x", (buf[i]>>22)&0x0f);
		printf(" %s", ((buf[i]>>21)&1)?"W":" ");
		if ((buf[i]>>21)&1)
			printf("[%X]", ((buf[i]>>17)&0x0f));
		else
			printf("(%x)", ((buf[i]>>17)&0x0f));
		printf("D[%X]", ((buf[i]>>13)&0x0f));
		printf(" r_opA=..%02x", (buf[i]>>7)&0x3f);
		printf(" opA=..%02x", (buf[i]>>1)&0x3f);
		printf(" ALU=..%d", buf[i]&1);
		*/

		printf("\n");
	}

	if (m_fpga->poll()) {
		printf("FPGA was interrupted\n");
		m_fpga->clear();
		m_fpga->writeio(R_ICONTROL, SCOPEN);
	}
	delete	m_fpga;
}

