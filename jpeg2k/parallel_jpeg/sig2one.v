// File: sig2one.v
// Generated by MyHDL 0.9dev
// Date: Tue Mar 10 11:18:46 2015


`timescale 1ns/10ps

module sig2one (
    Sout_s,
    clk_fast,
    combine_sig_s,
    Sin0,
    Sin1,
    Sin2,
    Sin3,
    Sin4,
    Sin5,
    Sin6,
    Sin7,
    Sin8,
    Sin9,
    Sin10,
    Sin11,
    Sin12,
    Sin13,
    Sin14,
    Sin15
);


output [159:0] Sout_s;
reg [159:0] Sout_s;
input clk_fast;
input combine_sig_s;
input [9:0] Sin0;
input [9:0] Sin1;
input [9:0] Sin2;
input [9:0] Sin3;
input [9:0] Sin4;
input [9:0] Sin5;
input [9:0] Sin6;
input [9:0] Sin7;
input [9:0] Sin8;
input [9:0] Sin9;
input [9:0] Sin10;
input [9:0] Sin11;
input [9:0] Sin12;
input [9:0] Sin13;
input [9:0] Sin14;
input [9:0] Sin15;






always @(posedge clk_fast) begin: SIG2ONE_COMBINE_LOGIC
    if ((combine_sig_s == 1)) begin
        Sout_s <= {Sin15, Sin14, Sin13, Sin12, Sin11, Sin10, Sin9, Sin8, Sin7, Sin6, Sin5, Sin4, Sin3, Sin2, Sin1, Sin0};
    end
    else begin
        Sout_s <= 0;
    end
end

endmodule
