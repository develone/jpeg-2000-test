// File: add_shift.v
// Generated by MyHDL 0.9dev
// Date: Sun Jun 15 13:58:48 2014


`timescale 1ns/10ps

module add_shift (
    d3,
    a2,
    x2,
    x3,
    x4,
    x5
);


output signed [18:0] d3;
reg signed [18:0] d3;
output signed [18:0] a2;
reg signed [18:0] a2;
input signed [18:0] x2;
input signed [18:0] x3;
input signed [18:0] x4;
input signed [18:0] x5;






always @(x2, x3, x4, x5) begin: ADD_SHIFT_EQ_LOGIC
    integer t;
    integer t1;
    t = $signed((x2 + x4) >>> 1);
    t = (x3 - t);
    t1 = $signed((x3 + x5) >>> 2);
    t1 = (x4 + t1);
    d3 = t;
    a2 = t1;
end

endmodule
