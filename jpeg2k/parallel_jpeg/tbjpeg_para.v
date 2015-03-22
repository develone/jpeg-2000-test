`timescale 1ns / 1ps

////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer:
//
// Create Date:   19:46:56 03/21/2015
// Design Name:   ram
// Module Name:   C:/Xilinx/14.7/ISE_DS/jpeg_para/tbjpeg_para.v
// Project Name:  jpeg_para
// Target Device:  
// Tool versions:  
// Description: 
//
// Verilog Test Fixture created by ISE for module: ram
//
// Dependencies:
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
////////////////////////////////////////////////////////////////////////////////

module tbjpeg_para;

	// Inputs
	reg [143:0] din_lf;
	reg [9:0] addr_lf;
	reg we_lf;
	
	reg [143:0] din_sa;
	reg [9:0] addr_sa;
	reg we_sa;
	
	reg [143:0] din_rt;
	reg [9:0] addr_rt;
	reg we_rt;
	
	reg [9:0] din_res;
	reg [9:0] addr_res;
	reg we_res;
   reg [9:0] addr_flgs;
   
 
	
	//jpeg signals
	reg [143:0] left_s_i;
	reg [143:0] sam_s_i;
	reg [143:0] right_s_i;
	reg [79:0] flgs_s_i;
	//reg [9:0] res_out_x;
	reg update_s;
	
	reg clk_fast;

	// Outputs
	wire [143:0] dout_lf;
	wire [143:0] dout_sa;
	wire [143:0] dout_rt;
	wire [9:0] dout_res;	
   wire [79:0] dout_flgs;
	//jpeg signals
  wire signed [9:0] res_out_x;
  //reg signed [9:0] res_out_x;
	wire noupdate_s;
	
 
	
 
	// Instantiate the Unit Under Test (UUT)
	ram uut (
		.dout(dout_lf), 
		.din(din_lf), 
		.addr(addr_lf), 
		.we(we_lf), 
		.clk_fast(clk_fast)
	);
 
	ram uut_sa (
		.dout(dout_sa), 
		.din(din_sa), 
		.addr(addr_sa), 
		.we(we_sa), 
		.clk_fast(clk_fast)
	); 

	ram uut_rt (
		.dout(dout_rt), 
		.din(din_rt), 
		.addr(addr_rt), 
		.we(we_rt), 
		.clk_fast(clk_fast)
	); 
	
	ram_res uut_res (
		.dout_res(dout_res), 
		.din_res(din_res), 
		.addr_res(addr_res), 
		.we_res(we_res), 
		.clk_fast(clk_fast)
	);
   rom_flgs uut_flgs (
      .dout_flgs(dout_flgs),
      .addr_flgs(addr_flgs)
   );	
   
   jp_process uut_jpeg(
      .res_out_x(res_out_x),
      .left_s_i(left_s_i),
      .sam_s_i(sam_s_i),
      .right_s_i(right_s_i),
      .flgs_s_i(flgs_s_i),
      .update_s(update_s),
		.noupdate_s(noupdate_s)
	);
 
	
initial begin
clk_fast = 0;
forever #20 clk_fast = ~clk_fast;
end
	initial begin
		// Initialize Inputs
		din_lf = 0;
		addr_lf = 0;
		we_lf = 0;
		clk_fast = 0;

		din_sa = 0;
		addr_sa = 0;
		we_sa = 0;

		din_rt = 0;
		addr_rt = 0;
		we_rt = 0;

		din_res = 0;
		addr_res = 0;
		we_res = 0;
		
		update_s = 0;
		left_s_i = 0;
		sam_s_i = 0;
		flgs_s_i = 0;
		
 
		
		// Wait 100 ns for global reset to finish
		#100;
        
		// Add stimulus here
	#110;
	addr_lf = 0;
	#120;
	we_lf = 1;
	#140;
	din_lf = 160;
	#150;
	we_lf = 0;
	
	#160;
 	addr_sa = 0;
	#170;
	we_sa = 1;
	#180;
	din_sa = 164;
	#190;
	we_sa = 0;
	
	#200;
 	addr_rt = 0;
	#210;
	we_rt = 1;
	#220;
	din_rt = 156;
	#230;
	we_rt = 0;
	
	#240;
 	addr_res = 0;
	#250;
	we_res = 1;
 
	#260;
	addr_flgs = 0;
	#270;
	left_s_i = dout_lf;
	#280;
	sam_s_i = dout_sa;
	#290;
	right_s_i = dout_rt;
	#300;
	flgs_s_i = dout_flgs;
	#330;
	


	#340;
	update_s = 1;
	#350;
	update_s = 0;
	#360;
	addr_flgs = 15;
	#370;
	update_s = 1;
	#380;
	update_s = 0;
	end
      
endmodule

