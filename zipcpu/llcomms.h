////////////////////////////////////////////////////////////////////////////////
//
// Filename:	llcomms.h
//
// Project:	XuLA2 board
//
// Purpose:	This is the C++ program on the command side that will interact
//		with a UART on an FPGA, both sending and receiving characters.
//		Any bus interaction will call routines from this lower level
//		library to accomplish the actual connection to and
//		transmission to/from the board.
//
//
// Creator:	Dan Gisselquist, Ph.D.
//		Gisselquist Technology, LLC
//
////////////////////////////////////////////////////////////////////////////////
//
// Copyright (C) 2015, Gisselquist Technology, LLC
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
////////////////////////////////////////////////////////////////////////////////
//
//
//
#ifndef	LLCOMMS_H
#define	LLCOMMS_H

class	LLCOMMSI {
protected:
	int	m_fdw, m_fdr;
	LLCOMMSI(void);
public:
	unsigned long	m_total_nread, m_total_nwrit;

	virtual	~LLCOMMSI(void) { close(); }
	virtual	void	kill(void)  { this->close(); };
	virtual	void	close(void);
	virtual	void	write(char *buf, int len);
	virtual int	read(char *buf, int len);
	virtual	bool	poll(unsigned ms);
};

class	TTYCOMMS : public LLCOMMSI {
public:
	TTYCOMMS(const char *dev);
};

class	NETCOMMS : public LLCOMMSI {
public:
	NETCOMMS(const char *dev, const int port);
};

#endif