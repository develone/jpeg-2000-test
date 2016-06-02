/*******************************************************************************
*
* Filename:	zipcmod.x
*
* Project:	XuLA2-LX25 SoC
*
* Purpose:	This script provides a description of the XuLA2-LX25 SoC,
* 		and specifically the memory bus that the Zip CPU would see,
*		for the purposes of where to place memory when linking.
*
* Creator:	Dan Gisselquist, Ph.D.
*		Gisselquist Technology, LLC
*
********************************************************************************
*
* Copyright (C) 2016, Gisselquist Technology, LLC
*
* This program is free software (firmware): you can redistribute it and/or
* modify it under the terms of  the GNU General Public License as published
* by the Free Software Foundation, either version 3 of the License, or (at
* your option) any later version.
*
* This program is distributed in the hope that it will be useful, but WITHOUT
* ANY WARRANTY; without even the implied warranty of MERCHANTIBILITY or
* FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
* for more details.
*
* License:	GPL, v3, as defined and found on www.gnu.org,
*		http://www.gnu.org/licenses/gpl.html
*
*
*******************************************************************************/

ENTRY(_start)

MEMORY
{
	blkram (wx) : ORIGIN = 0x002000, LENGTH = 0x002000
	flash  (rx) : ORIGIN = 0x040000, LENGTH = 0x040000
	sdram  (wx) : ORIGIN = 0x800000, LENGTH = 0x800000
}

_top_of_stack = ORIGIN(blkram) + LENGTH(blkram) - 1;

SECTIONS
{
  . = 0x02000;
  .rocode 0x02000 : { *(.start) *(.text)
	*(.rodata)
	*(.strings) } > blkram
  .data : { *(.data) *(COMMON) *(.bss) } > blkram
  _top_of_heap = 0xf00000;
}
