// File: signed2twoscomplement.v
// Generated by MyHDL 1.0dev
// Date: Sat Oct 24 10:38:06 2015


`timescale 1ns/10ps

module signed2twoscomplement (
    clk,
    res_o,
    z
);


input clk;
input signed [9:0] res_o;
output [8:0] z;
reg [8:0] z;






always @(posedge clk) begin: SIGNED2TWOSCOMPLEMENT_UNSIGNED_LOGIC
    z <= res_o;
end

endmodule
