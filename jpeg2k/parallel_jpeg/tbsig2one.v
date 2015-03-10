`timescale 1ns / 1ps

////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer:
//
// Create Date:   19:34:43 03/09/2015
// Design Name:   sig2one
// Module Name:   C:/Xilinx/14.7/ISE_DS/XESS_SDRAMSPIinst/array_sig/tbsig2one.v
// Project Name:  array_sig
// Target Device:  
// Tool versions:  
// Description: 
//
// Verilog Test Fixture created by ISE for module: sig2one
//
// Dependencies:
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
////////////////////////////////////////////////////////////////////////////////

module tbsig2one;

	// Inputs
	reg clk_fast;
	reg combine_sig_s;
	reg [9:0] Sin0;
	reg [9:0] Sin1;
	reg [9:0] Sin2;
	reg [9:0] Sin3;
	reg [9:0] Sin4;
	reg [9:0] Sin5;
	reg [9:0] Sin6;
	reg [9:0] Sin7;
	reg [9:0] Sin8;
	reg [9:0] Sin9;
	reg [9:0] Sin10;
	reg [9:0] Sin11;
	reg [9:0] Sin12;
	reg [9:0] Sin13;
	reg [9:0] Sin14;
	reg [9:0] Sin15;

	// Outputs
	wire [159:0] Sout_s;

	// Instantiate the Unit Under Test (UUT)
	sig2one uut (
		.Sout_s(Sout_s), 
		.clk_fast(clk_fast), 
		.combine_sig_s(combine_sig_s), 
		.Sin0(Sin0), 
		.Sin1(Sin1), 
		.Sin2(Sin2), 
		.Sin3(Sin3), 
		.Sin4(Sin4), 
		.Sin5(Sin5), 
		.Sin6(Sin6), 
		.Sin7(Sin7), 
		.Sin8(Sin8), 
		.Sin9(Sin9), 
		.Sin10(Sin10), 
		.Sin11(Sin11), 
		.Sin12(Sin12), 
		.Sin13(Sin13), 
		.Sin14(Sin14), 
		.Sin15(Sin15)
	);

	initial begin
		// Initialize Inputs
		clk_fast = 0;
		combine_sig_s = 0;
		Sin0 = 0;
		Sin1 = 0;
		Sin2 = 0;
		Sin3 = 0;
		Sin4 = 0;
		Sin5 = 0;
		Sin6 = 0;
		Sin7 = 0;
		Sin8 = 0;
		Sin9 = 0;
		Sin10 = 0;
		Sin11 = 0;
		Sin12 = 0;
		Sin13 = 0;
		Sin14 = 0;
		Sin15 = 0;

		// Wait 100 ns for global reset to finish
		#100;
        
		// Add stimulus here
		Sin0 = 160;
		#110 Sin1 = -2;
		#120 Sin2 = -4;
		#130 Sin3 = -2;
		#140 Sin4 = 156;
		#150 Sin5 = -6;
		#160 Sin6 = -4;
		//#160 combine_sig_s = 1;
		#170 Sin7 = -12;
		#180 Sin8 = 164;
		
		#190 Sin9 = -2;
		#220 Sin10 = -4;
		#230 Sin11 = -2;
 		#280 Sin12 = 164;
		#290 Sin13 = -4;
		#300 Sin14 = -12;
		#310 Sin15 = 164;		
		#320 combine_sig_s = 1;
		#325 clk_fast = 1;
		#335 clk_fast = 0;
	end
      
endmodule

