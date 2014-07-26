// File: ram_sam.v
// Generated by MyHDL 0.9dev
// Date: Sat Jul 26 08:43:39 2014


`timescale 1ns/10ps

module ram_sam (
    clk,
    pix_din_right,
    pix_we_even,
    pix_addr_even,
    pix_din_left,
    pix_dout_right,
    pix_we_sam,
    pix_dout_left,
    pix_din_sam,
    pix_dout_odd,
    pix_din_odd,
    pix_even_odd,
    pix_addr_right,
    pix_fwd_inv,
    pix_din_even,
    pix_dout_even,
    pix_addr_left,
    pix_dout_sam,
    pix_we_right,
    pix_addr_odd,
    pix_we_odd,
    pix_addr_sam,
    pix_we_left
);
// Ram model 

input clk;
input signed [16:0] pix_din_right;
input pix_we_even;
input [7:0] pix_addr_even;
input signed [16:0] pix_din_left;
output signed [16:0] pix_dout_right;
wire signed [16:0] pix_dout_right;
input pix_we_sam;
output signed [16:0] pix_dout_left;
wire signed [16:0] pix_dout_left;
input signed [16:0] pix_din_sam;
output signed [16:0] pix_dout_odd;
wire signed [16:0] pix_dout_odd;
input signed [16:0] pix_din_odd;
input pix_even_odd;
input [7:0] pix_addr_right;
input pix_fwd_inv;
input signed [16:0] pix_din_even;
output signed [16:0] pix_dout_even;
wire signed [16:0] pix_dout_even;
input [7:0] pix_addr_left;
output signed [16:0] pix_dout_sam;
wire signed [16:0] pix_dout_sam;
input pix_we_right;
input [7:0] pix_addr_odd;
input pix_we_odd;
input [7:0] pix_addr_sam;
input pix_we_left;


reg signed [16:0] mem_sam [0:256-1];




always @(posedge clk) begin: RAM_SAM_WRITE_SAM
    if (pix_we_sam) begin
        mem_sam[pix_addr_sam] <= pix_din_sam;
    end
end



assign pix_dout_sam = mem_sam[pix_addr_sam];

endmodule
