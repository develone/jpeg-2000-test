`timescale 1ns/1ns

module tb_comm_fpga_fx2_m;

   reg clk_in;
   reg reset_in;
   wire fx2FifoSel_out;
   reg [7:0] fx2Data_in;
   wire [7:0] fx2Data_out;
   wire       fx2Data_sel;   
   wire       fx2Read_out;
   reg 	      fx2GotData_in;
   wire       fx2Write_out;
   reg 	      fx2GotRoom_in;
   wire       fx2PktEnd_out;
   wire [6:0] chanAddr_out;
   wire [7:0] h2fData_out;
   wire       h2fValid_out;
   reg 	      h2fReady_in;
   reg [7:0]  f2hData_in;
   reg 	      f2hValid_in;
   wire       f2hReady_out;
   
   initial begin
      $from_myhdl(
		  clk_in,
		  reset_in,
		  fx2Data_in,
		  fx2GotData_in,
		  fx2GotRoom_in,
		  h2fReady_in,
		  f2hData_in,
		  f2hValid_in
		  );
      $to_myhdl(
		fx2FifoSel_out,
		fx2Data_out,
		fx2Data_sel,
		fx2Read_out,
		fx2Write_out,
		fx2PktEnd_out,
		chanAddr_out,
		h2fData_out,
		h2fValid_out,
		f2hReady_out
		);
   end
   
   initial begin
      $dumpfile("comm_fpga_fx2_m.vcd");
      $dumpvars(0,tb_comm_fpga_fx2_m);
   end
   

   wire v1_reset_in = ~reset_in;
   comm_fpga_fx2_v1 
     dut_v1(
	 .clk_in(clk_in),
	 .reset_in(v1_reset_in),
	 .fx2FifoSel_out(fx2FifoSel_out),
	 .fx2Data_in(fx2Data_in),
	 .fx2Data_out(fx2Data_out),
	 .fx2Data_sel(fx2Data_sel),
	 .fx2Read_out(fx2Read_out),
	 .fx2GotData_in(fx2GotData_in),
	 .fx2Write_out(fx2Write_out),
	 .fx2GotRoom_in(fx2GotRoom_in),
	 .fx2PktEnd_out(fx2PktEnd_out),
	 .chanAddr_out(chanAddr_out),
	 .h2fData_out(h2fData_out),
	 .h2fValid_out(h2fValid_out),
	 .h2fReady_in(h2fReady_in),
	 .f2hData_in(f2hData_in),
	 .f2hValid_in(f2hValid_in),
	 .f2hReady_out(f2hReady_out)
	 );
   
   // Add the MyHDL converted version
   /// @todo: add separate signals for tracing
   comm_fpga_fx2_v2 
     dut_v2(
	    .clk_in(clk_in),
	    .reset_in(reset_in),
	    //.fx2FifoSel_out(fx2FifoSel_out),
	    .fx2Data_in(fx2Data_in),
	    //.fx2Data_out(fx2Data_out),
	    .fx2Data_sel(fx2Data_sel),
	    //.fx2Read_out(fx2Read_out),
	    .fx2GotData_in(fx2GotData_in),
	    //.fx2Write_out(fx2Write_out),
	    .fx2GotRoom_in(fx2GotRoom_in),
	    //.fx2PktEnd_out(fx2PktEnd_out),
	    .chanAddr_out(chanAddr_out),
	    //.h2fData_out(h2fData_out),
	    //.h2fValid_out(h2fValid_out),
	    .h2fReady_in(h2fReady_in),
	    .f2hData_in(f2hData_in),
	    .f2hValid_in(f2hValid_in)
	    //.f2hReady_out(f2hReady_out)
	 );
   
endmodule
