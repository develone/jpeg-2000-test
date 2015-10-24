`timescale 1ns / 1ps

////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer:
//
// Create Date:   08:39:36 10/20/2015
// Design Name:   lift_step
// Module Name:   /home/vidal/wkg/jpeg-2000-test/pc_fast_blinker_jpeg/pc_fast_blinker_jpeg/lift_step_tb.v
// Project Name:  pc_fast_blinker_jpeg
// Target Device:  
// Tool versions:  
// Description: 
//
// Verilog Test Fixture created by ISE for module: lift_step
//
// Dependencies:
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
////////////////////////////////////////////////////////////////////////////////

module lift_step_tb;

	// Inputs
	reg [2:0] flags_i;
	reg update_i;
	//reg update_o;
	reg [8:0] left_i;
	reg [8:0] sam_i;
	reg [8:0] right_i;
	reg clk_i;
    
	// Outputs
	wire signed [9:0] res_o;
   wire update_o;
	wire [8:0] z;
	// Instantiate the Unit Under Test (UUT)
	lift_step uut (
		.flags_i(flags_i),
      .update_i(update_i),		
		.left_i(left_i), 
		.sam_i(sam_i), 
		.right_i(right_i), 
		.res_o(res_o), 
		.update_o(update_o),
		.clk_i(clk_i)
	);
   
	signed2twoscomplement uut1 (
	    .clk(clk_i),
       .res_o(res_o),
       .z(z)
	);
  initial begin
    clk_i = 1'b0;
     
    repeat(4) #10 clk_i = ~clk_i;
    
    forever #10 clk_i = ~clk_i; // generate a clock
  end

	initial begin
		// Initialize Inputs
		flags_i = 0;
		update_i = 0;
		left_i = 0;
		sam_i = 0;
		right_i = 0;
		clk_i = 0;

		// Wait 100 ns for global reset to finish
		#100;
        
		// Add stimulus here
      #110 left_i = 68;
		#120 right_i = 163;
		#130 sam_i = 218;
		#140 flags_i = 7;
		#150 update_i = 1;
		#160 update_i = 0;
		 
		#170 left_i = 68;
		#180 right_i = 163;
		#190 sam_i = 231;
		#200 flags_i = 5;
		#210 update_i = 1;
		#220 update_i = 0;

		#230 left_i = 164;
		#240 right_i = 160;
		#250 sam_i = 250;
		#260 flags_i = 6;
		#270 update_i = 1;
		#280 update_i = 0;		
		#290 sam_i = 203;
		#300 flags_i = 4;
		#310 update_i = 1;
		#320 update_i = 0;
 		 
	end
      
endmodule

