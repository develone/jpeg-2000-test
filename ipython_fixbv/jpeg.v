// File: jpeg.v
// Generated by MyHDL 0.9dev
// Date: Wed Aug 20 10:32:16 2014


`timescale 1ns/10ps

module jpeg (
    clk_fast,
    left_s,
    right_s,
    sam_s,
    res_s,
    even_odd_s,
    fwd_inv_s
);


input clk_fast;
input signed [15:0] left_s;
input signed [15:0] right_s;
input signed [15:0] sam_s;
output signed [15:0] res_s;
reg signed [15:0] res_s;
input even_odd_s;
input fwd_inv_s;






always @(posedge clk_fast) begin: JPEG_HDL
    if (even_odd_s) begin
        if (fwd_inv_s) begin
            res_s <= (sam_s - ($signed(left_s >>> 1) + $signed(right_s >>> 1)));
        end
        else begin
            res_s <= (sam_s + ($signed(left_s >>> 1) + $signed(right_s >>> 1)));
        end
    end
    else begin
        if (fwd_inv_s) begin
            res_s <= (sam_s + $signed(((left_s + right_s) + 2) >>> 2));
        end
        else begin
            res_s <= (sam_s - $signed(((left_s + right_s) + 2) >>> 2));
        end
    end
end

endmodule
