module tb_wbdeppsimple1;
	reg i_clk;
	reg i_astb_n;
	reg i_dstb_n;
	reg i_write_n;
	reg [7:0] i_depp;
	reg [7:0] o_depp;
	reg i_wb_ack;
	reg i_wb_stall;
	reg i_wb_err;
	reg [31:0] i_wb_data;
	reg i_int;
	
	reg i_b0;
	reg i_b1;
	reg i_b2;
	reg i_b3;
	reg i_b4;
	reg i_b5;
	reg i_b6;
	reg i_b7;

	// Outputs
	//wire [7:0] o_depp;
	wire o_wait;
	wire o_wb_cyc;
	wire o_wb_stb;
	wire o_wb_we;
	wire [31:0] o_wb_addr;
	wire [31:0] o_wb_data;
	reg o_b0;
	reg o_b1;
	reg o_b2;
	reg o_b3;
	reg o_b4;
	reg o_b5;
	reg o_b6;
	reg o_b7;
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
        o_depp,
        i_wb_ack,
        i_wb_stall,
        i_wb_err,
        i_wb_data,
        i_int,
        i_b0,
        i_b1,
        i_b2,
        i_b3,
        i_b4,
        i_b5,
        i_b6,
        i_b7
        
    );
    $to_myhdl(
        o_depp,
        o_wait,
        o_wb_we,
        o_wb_addr,
        o_wb_data,
        o_wb_cyc,
        o_wb_stb,
        o_b0,
        o_b1,
        o_b2,
        o_b3,
        o_b4,
        o_b5,
        o_b6,
        o_b7
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
