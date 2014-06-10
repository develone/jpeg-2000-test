// File: eq_d_c1.v
// Generated by MyHDL 0.8
// Date: Tue Jun 10 09:06:52 2014


`timescale 1ns/10ps

module eq_d_c1 (
    d3,
    a2,
    clk,
    x2,
    x3,
    x4
);


output signed [18:0] d3;
reg signed [18:0] d3;
output signed [18:0] a2;
reg signed [18:0] a2;
input clk;
input signed [18:0] x2;
input signed [18:0] x3;
input signed [18:0] x4;






always @(posedge clk) begin: EQ_D_C1_EQ_LOGIC
    integer t2;
    integer t3;
    integer t1;
    t1 = (x2 + x4);
    t1 = $signed(t1 >>> 1);
    t2 = (x3 - t1);
    t1 = $signed(x4 >>> 2);
    t3 = ((x2 + t1) + t2);
    d3 <= t2;
    a2 <= t3;
end

endmodule
