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
	//flato wire blue zzzzz
	//flato red 
	wire [143:0] flato;
	wire [8:0] gflt_col;
	//gflt_flats wire blue zzzzz
   wire [143:0] gflt_flats;
	//reg [143:0] gflt_flats;
	//gstk_g_0_y wire blue zzzzz
	wire [8:0] gstk_g_14_y;
   wire [8:0] gstk_g_13_y;
   wire [8:0] gstk_g_12_y;
   wire [8:0] gstk_g_11_y;
   wire [8:0] gstk_g_10_y;
   wire [8:0] gstk_g_9_y;
   wire [8:0] gstk_g_8_y;
   wire [8:0] gstk_g_7_y;
   wire [8:0] gstk_g_6_y;
   wire [8:0] gstk_g_5_y;
   wire [8:0] gstk_g_4_y;
   wire [8:0] gstk_g_3_y;
   wire [8:0] gstk_g_2_y;
   wire [8:0] gstk_g_1_y;
	wire [8:0] gstk_g_0_y;
 
	// Outputs
   wire sdo;
	
  
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
      flati = 0;
      //gflt_col = 0;
		// Wait 100 ns for global reset to finish
		#100;
        
		// Add stimulus here
      #110;
		reset = 1;
      #120;
		reset = 0;
		#130;
		//flati = 0;
		#140;
		flati = 144'h1ffc0000000000000001c0000000000001ff;
		#150;
		 
	end
      
endmodule

