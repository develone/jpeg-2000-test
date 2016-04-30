module tb_wbdeppsimple1;
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

initial begin
    $dumpfile("tb/vcd/wbdeppsimple1.vcd");
    $dumpvars(0, tb_wbdeppsimple1);
end

 

initial begin
    $from_myhdl(
        i_clk,
        i_astb_n,
        i_dstb_n,
        i_write_n,
        i_depp,
 
        i_wb_ack,
        i_wb_stall,
        i_wb_err,
        i_wb_data,
        i_int
    );
    $to_myhdl(
        o_depp,
        o_wait,
        o_wb_we,
        o_wb_addr,
        o_wb_data,
        o_wb_cyc,
        o_wb_stb
    );
    
end

wbdeppsimple dut_wbdeppsimple(i_clk,
	i_astb_n, 
	i_dstb_n, 
	i_write_n,
	i_depp, 
	o_depp,
	o_wait,
	o_wb_cyc,
	o_wb_stb, 
	o_wb_we,
	o_wb_addr,
	o_wb_data,
	i_wb_ack,
	i_wb_stall,
	i_wb_err,
	i_wb_data,
	i_int);

endmodule
