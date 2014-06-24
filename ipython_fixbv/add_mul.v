// File: add_mul.v
// Generated by MyHDL 0.9dev
// Date: Tue Jun 24 10:35:35 2014


`timescale 1ns/10ps

module add_mul (
    d3,
    a2,
    clk,
    x2,
    x3,
    x4,
    x5,
    p,
    odd_even
);


input signed [35:0] d3;
input signed [35:0] a2;
input clk;
input signed [10:0] x2;
input signed [10:0] x3;
input signed [10:0] x4;
input signed [10:0] x5;
input p;
input odd_even;






always @(posedge clk) begin: ADD_MUL_RTL
    integer xx3;
    integer xx2;
    integer xx5;
    integer xx4;
    reg signed [36-1:0] ca3;
    reg signed [36-1:0] ca2;
    reg signed [36-1:0] ca1;
    integer t1;
    integer t;
    reg signed [36-1:0] ca4;
    if ((!p)) begin
        if (odd_even) begin
            ca1 = fixbv((-1.586134342));
            xx2 = (x2 / 10.0);
            xx3 = (x3 / 10.0);
            t = (((xx2 + xx3) * ca1) * 10.0);
        end
        else begin
            ca2 = fixbv((-0.05298011854));
            xx4 = (x4 / 10.0);
            xx5 = (x5 / 10.0);
            t1 = (((xx4 + xx5) * ca2) * 10.0);
        end
    end
    else begin
        if (odd_even) begin
            ca3 = fixbv(0.8829110762);
            xx2 = (x2 / 10.0);
            xx3 = (x3 / 10.0);
            t = (((x2 + x3) * ca3) * 10.0);
        end
        else begin
            ca4 = fixbv(0.4435068522);
            xx4 = (x4 / 10.0);
            xx5 = (x5 / 10.0);
            t1 = (((x4 + x5) * ca4) * 10.0);
        end
    end
end

endmodule
