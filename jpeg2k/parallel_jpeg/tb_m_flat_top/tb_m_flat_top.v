`timescale 1ns / 1ps

////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer:
//
// Create Date:   15:06:28 04/21/2015
// Design Name:   m_flat_top
// Module Name:   C:/Users/vidal/Documents/GitHub/jpeg-2000-test/jpeg2k/parallel_jpeg/tb_m_flat_top/tb_m_flat_top.v
// Project Name:  tb_m_flat_top
// Target Device:  
// Tool versions:  
// Description: 
//
// Verilog Test Fixture created by ISE for module: m_flat_top
//
// Dependencies:
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
////////////////////////////////////////////////////////////////////////////////

module tb_m_flat_top;

	// Inputs
	reg clock;
	reg reset;
	reg [143:0] flati;

	// Outputs
 
	
   wire [143:0] flato;
	// Instantiate the Unit Under Test (UUT)
	m_flat_top uut (
		.clock(clock), 
		.reset(reset), 
		.sdo(sdo)
	);
initial begin
clock = 0;
forever #20 clock = ~clock;
end
	initial begin
		// Initialize Inputs
		clock = 0;
		reset = 0;

		// Wait 100 ns for global reset to finish
		#100;
        
		// Add stimulus here
      #110;
		reset = 1;
      #120;
		reset = 0;
		#130;
		flati = 144'h001c0000000000000001c000000000000000;
	end
      
endmodule

