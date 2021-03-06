// File: ram.v
// Generated by MyHDL 0.9dev
// Date: Tue Mar 24 10:04:43 2015


`timescale 1ns/10ps

module ram (
    dout,
    din,
    addr,
    we,
    clk_fast
);
// Ram model 

output [143:0] dout;
wire [143:0] dout;
input [143:0] din;
input [9:0] addr;
input we;
input clk_fast;


reg [143:0] mem [0:512-1];




always @(posedge clk_fast) begin: RAM_WRITE
    if (we) begin
        mem[addr] <= din;
    end
end



assign dout = mem[addr];

endmodule
