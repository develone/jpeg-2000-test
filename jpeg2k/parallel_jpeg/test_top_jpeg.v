`timescale 1ns / 1ps

////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer:
//
// Create Date:   07:22:25 04/01/2015
// Design Name:   top_jpeg
// Module Name:   C:/Xilinx/14.7/ISE_DS/jpeg_para/test_top_jpeg.v
// Project Name:  jpeg_para
// Target Device:  
// Tool versions:  
// Description: 
//
// Verilog Test Fixture created by ISE for module: top_jpeg
//
// Dependencies:
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
////////////////////////////////////////////////////////////////////////////////

module test_top_jpeg;

	// Inputs
	reg clk;
	reg [143:0] left_s_i;
	reg [143:0] sam_s_i;
	reg [143:0] right_s_i;
	reg [79:0] flgs_s_i;
	reg update_s;
	reg [9:0] row_ind;
	reg [9:0] col_ind;
	reg [8:0] z;
	reg [9:0] x;
	reg [3:0] ma_row;
	reg [3:0] ma_col;
	reg [9:0] bits_in_sig;

	reg [143:0] din_lf;
	reg [143:0] din_sa;
	reg [143:0] din_rt;
	reg [8:0] din_res;
	reg [9:0] addr_lf;
	reg [9:0] addr_sa;
	reg [9:0] addr_rt;
	reg [9:0] addr_res;
	reg [9:0] addr_flgs;
	reg we_lf;
	reg we_sa;
	reg we_rt;
	reg we_res;
   
	// Outputs
	wire [9:0] res_out_x;
	wire noupdate_s;
	wire [143:0] flat_lf;
	wire [143:0] flat_sa;
	wire [143:0] flat_rt;
	wire [143:0] dout_lf;
	wire [143:0] dout_sa;
	wire [143:0] dout_rt;
	wire [8:0] dout_res;
   //output [8:0] vv;
   wire [8:0] vv;
	wire [79:0] dout_flgs;
 


	// Instantiate the Unit Under Test (UUT)
	top_jpeg uut (
		.clk(clk), 
		.res_out_x(res_out_x), 
		.left_s_i(left_s_i), 
		.sam_s_i(sam_s_i), 
		.right_s_i(right_s_i), 
		.flgs_s_i(flgs_s_i), 
		.noupdate_s(noupdate_s), 
		.update_s(update_s), 
		.row_ind(row_ind), 
		.col_ind(col_ind), 
		.flat_lf(flat_lf), 
		.flat_sa(flat_sa), 
		.flat_rt(flat_rt), 
		.z(z), 
		.x(x), 
		.ma_row(ma_row), 
		.ma_col(ma_col),
      .bits_in_sig(bits_in_sig),
      .vv(vv),		
		.dout_lf(dout_lf), 
		.dout_sa(dout_sa), 
		.dout_rt(dout_rt), 
		.dout_res(dout_res),
      		
		.din_lf(din_lf), 
		.din_sa(din_sa), 
		.din_rt(din_rt), 
		.din_res(din_res), 
		.addr_lf(addr_lf), 
		.addr_sa(addr_sa), 
		.addr_rt(addr_rt),
		
		.addr_res(addr_res), 
		.we_lf(we_lf), 
		.we_sa(we_sa), 
		.we_rt(we_rt),		
		.we_res(we_res),
		.dout_flgs(dout_flgs),
		.addr_flgs(addr_flgs)
	);
initial begin
clk = 0;
forever #20 clk = ~clk;
end
	initial begin
		// Initialize Inputs
		clk = 0;
		left_s_i = 0;
		sam_s_i = 0;
		right_s_i = 0;
		flgs_s_i = 0;
		update_s = 0;
		row_ind = 0;
		col_ind = 0;
		z = 0;
		x = 0;
		ma_row = 0;
		ma_col = 0;
		bits_in_sig = 0;
		din_lf = 0;
		din_sa = 0;
		din_rt = 0;
		din_res = 0;
		addr_lf = 0;
		addr_sa = 0;
		addr_rt = 0;
		addr_res = 0;
		we_lf = 0;
		we_sa = 0;
		we_rt = 0;
		we_res = 0;
      addr_flgs = 0;
		// Wait 100 ns for global reset to finish
		#100;
        
		// Add stimulus here
      #110;
		we_lf = 1;
		we_sa = 1;
		we_rt = 1;
		#120;
		addr_lf = 0;
		#130;
		din_lf = 144'h5229138a452291389c4e271389c5227148a4;
		din_sa = 144'h5627148a452291489c4e271389c4e27138a4;
		din_rt = 144'h52291489c52291489c4e271389c4e29138a4;
		
		#140;
		we_res = 1;
		#150;
		addr_res = 0;
		#160;
		bits_in_sig = 10'h7ff;
		#170;
		din_res = vv;
		#180;
		bits_in_sig = 10'h7fe;
		#190;
		din_res = vv;
		#200;
		we_res = 0;
		#210;
		addr_res = 0;
		#220;
		addr_res = 1;
		#230;
		we_lf = 0;
		we_sa = 0;
		we_rt = 0;
		#240;
		left_s_i = dout_lf;
		sam_s_i = dout_sa;
		right_s_i = dout_rt;
		#250;
		flgs_s_i = 7;
		//flgs_s_i = dout_flgs;
		#270;
		update_s = 1;
		#280;
		update_s = 0;
		
	end
      
endmodule

