`timescale 1ns / 1ps

////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer:
//
// Create Date:   10:24:36 04/28/2016
// Design Name:   wbdeppsimple
// Module Name:   /home/vidal/wkg/jpeg-2000-test/xula2_fpga/parallel/wbdeppsimple/wbdeppsimple_tb.v
// Project Name:  wbdeppsimple
// Target Device:  
// Tool versions:  
// Description: 
//
// Verilog Test Fixture created by ISE for module: wbdeppsimple
//
// Dependencies:
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
////////////////////////////////////////////////////////////////////////////////

module wbdeppsimple_tb;

	// Inputs
	reg i_clk;
	reg i_astb_n;
	reg i_dstb_n;
	reg i_write_n;
	reg [7:0] i_depp;
	reg i_wb_ack;
	reg i_wb_stall;
	reg i_wb_err;
	reg [31:0] i_wb_data;
	reg i_int;

	// Outputs
	wire [7:0] o_depp;
	wire o_wait;
	wire o_wb_cyc;
	wire o_wb_stb;
	wire o_wb_we;
	wire [31:0] o_wb_addr;
	wire [31:0] o_wb_data;

	// Instantiate the Unit Under Test (UUT)
	wbdeppsimple uut (
		.i_clk(i_clk), 
		.i_astb_n(i_astb_n), 
		.i_dstb_n(i_dstb_n), 
		.i_write_n(i_write_n), 
		.i_depp(i_depp), 
		.o_depp(o_depp), 
		.o_wait(o_wait), 
		.o_wb_cyc(o_wb_cyc), 
		.o_wb_stb(o_wb_stb), 
		.o_wb_we(o_wb_we), 
		.o_wb_addr(o_wb_addr), 
		.o_wb_data(o_wb_data), 
		.i_wb_ack(i_wb_ack), 
		.i_wb_stall(i_wb_stall), 
		.i_wb_err(i_wb_err), 
		.i_wb_data(i_wb_data), 
		.i_int(i_int)
	);
	
	
	
	initial begin
		// Initialize Inputs
		i_clk = 0;
		i_astb_n = 0;
		i_dstb_n = 0;
		i_write_n = 0;
		i_depp = 0;
		i_wb_ack = 0;
		i_wb_stall = 0;
		i_wb_err = 0;
		i_wb_data = 0;
		i_int = 0;

		// Wait 100 ns for global reset to finish
		#100;
		#103 i_int = 1;
      #104 i_write_n = 1;
		#105 i_dstb_n = 1;
      #106 i_astb_n = 1;
		#108  i_depp = 208;
		#110 i_write_n = 0;
		#112 i_astb_n = 0;
		#113 i_dstb_n = 0;
      #114 i_write_n = 1;
		#115 i_depp = 164;
      #116 i_astb_n = 1;
		#117 i_dstb_n = 1;
      #118 i_write_n = 1;
		#119 i_write_n = 0;
      #120 i_astb_n = 0;
      #121 i_dstb_n = 0;
      
      #123 i_astb_n = 1;
		#124 i_dstb_n = 1;
      #126 i_write_n = 1;
      #128 i_astb_n = 0;
      #130 i_dstb_n = 0;
      #132 i_write_n = 0;
      #134 i_astb_n = 1;
      #136 i_dstb_n = 1;
      #138 i_write_n = 1;		
		//#105 i_int = 1;
      
      //#110 i_write_n = 1;
		//#110 i_astb_n = 1;
      //#110 i_dstb_n = 1;
		//#110 i_dstb_n = 1;
		//#150 i_write_n = 0;
		// Add stimulus here
		//#160 i_wb_ack = 1;
		//#151 i_write_n = 0;
		//#152 i_depp = 1;
		//#160 i_astb_n = 0;
      //#170 i_dstb_n = 0;
		//#180 i_depp = 208;
		//#181 i_write_n = 1;
      //#190 i_dstb_n = 1;
      //#200 i_dstb_n = 0;
      //#210 i_depp = 164;
		//#212 i_write_n = 0;
      //#220 i_dstb_n = 1;
      //#230 i_dstb_n = 0;	
      //#250 i_write_n = 1;
		//#260 i_depp = 2;
		//#270 i_astb_n = 0;
	end
      always i_clk = #5 ~i_clk;  // 100 MHz
endmodule

