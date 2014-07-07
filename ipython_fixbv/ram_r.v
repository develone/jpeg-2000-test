// File: ram_r.v
// Generated by MyHDL 0.9dev
// Date: Mon Jul  7 15:28:24 2014


`timescale 1ns/10ps

module ram_r (
    clk,
    pix_addr_r,
    pix_din_r,
    pix_we_r,
    pix_dout_r,
    pix_dout_l,
    pix_din_l,
    pix_addr_odd,
    pix_we_odd,
    pix_we_l,
    pix_addr_even,
    pix_din_even,
    pix_we_even,
    pix_dout_odd,
    pix_din_odd,
    pix_dout_even,
    pix_addr_l
);
// Ram model 

input clk;
input [6:0] pix_addr_r;
input signed [25:0] pix_din_r;
input pix_we_r;
output signed [25:0] pix_dout_r;
wire signed [25:0] pix_dout_r;
input signed [25:0] pix_dout_l;
input signed [25:0] pix_din_l;
input [6:0] pix_addr_odd;
input pix_we_odd;
input pix_we_l;
input [6:0] pix_addr_even;
input signed [25:0] pix_din_even;
input pix_we_even;
input signed [25:0] pix_dout_odd;
input signed [25:0] pix_din_odd;
input signed [25:0] pix_dout_even;
input [6:0] pix_addr_l;


reg signed [25:0] mem_r [0:128-1];




always @(posedge clk) begin: RAM_R_WRITE_R
    if (pix_we_r) begin
        mem_r[pix_addr_r] <= pix_din_r;
    end
end



assign pix_dout_r = mem_r[pix_addr_r];

endmodule
