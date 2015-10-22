`timescale 1ns / 1ps

////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer:
//
// Create Date:   12:53:57 10/22/2015
// Design Name:   signed2twoscomplement
// Module Name:   /home/vidal/wkg/jpeg-2000-test/pc_fast_blinker_jpeg/pc_fast_blinker_jpeg/signed2twoscomplement_tb.v
// Project Name:  pc_fast_blinker_jpeg
// Target Device:  
// Tool versions:  
// Description: 
//
// Verilog Test Fixture created by ISE for module: signed2twoscomplement
//
// Dependencies:
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
////////////////////////////////////////////////////////////////////////////////

module signed2twoscomplement_tb;

	// Inputs
	reg clk;
	reg [8:0] res_o;

	// Outputs
	wire [7:0] z;

	// Instantiate the Unit Under Test (UUT)
	signed2twoscomplement uut (
		.clk(clk), 
		.res_o(res_o), 
		.z(z)
	);
   initial begin
    clk = 1'b0;
     
    repeat(4) #10 clk = ~clk;
    
    forever #10 clk = ~clk; // generate a clock
  end
	initial begin
		// Initialize Inputs
		clk = 0;
		res_o = 0;

		// Wait 100 ns for global reset to finish
		#100;
		#110 res_o = 1;
      #120 res_o = 2;
		#130 res_o = 3;
		#140 res_o = 4;
		#150 res_o = 5;
      #160 res_o = -1;
      #170 res_o = -2;
		#180 res_o = -3;
		#190 res_o = -4;
		#200 res_o = -5;        
		// Add stimulus here

	end
      
endmodule

