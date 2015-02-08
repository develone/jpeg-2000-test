`timescale 1ns / 1ps

////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer:
//
// Create Date:   19:16:11 02/07/2015
// Design Name:   jp_process
// Module Name:   C:/Xilinx/14.7/ISE_DS/XESS_SDRAMSPIinst/array_sig/TBjp_process.v
// Project Name:  array_sig
// Target Device:  
// Tool versions:  
// Description: 
//
// Verilog Test Fixture created by ISE for module: jp_process
//
// Dependencies:
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
////////////////////////////////////////////////////////////////////////////////

module TBjp_process;

	// Inputs
	reg [511:0] sig_in_x_i;
	reg [127:0] res_out_x_i;
	reg [127:0] left_s_i;
	reg [127:0] sam_s_i;
	reg [127:0] right_s_i;
	reg [79:0] flgs_s_i;

	// Instantiate the Unit Under Test (UUT)
	jp_process uut (
		.sig_in_x_i(sig_in_x_i), 
		.res_out_x_i(res_out_x_i), 
		.left_s_i(left_s_i), 
		.sam_s_i(sam_s_i), 
		.right_s_i(right_s_i), 
		.flgs_s_i(flgs_s_i)
	);

	initial begin
		// Initialize Inputs
		sig_in_x_i = 0;
		res_out_x_i = 0;
		left_s_i = 0;
		sam_s_i = 0;
		right_s_i = 0;
		flgs_s_i = 0;

		// Wait 100 ns for global reset to finish
		#100;
        
		// Add stimulus here
		#110 left_s_i = 164;
		#120 sam_s_i = 160;
		#130 right_s_i = 176;
		#140 flgs_s_i = 7;
	end
      
endmodule

