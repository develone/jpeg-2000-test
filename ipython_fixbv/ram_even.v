// File: ram_even.v
// Generated by MyHDL 0.9dev
// Date: Sun Jul 27 07:13:39 2014


`timescale 1ns/10ps

module ram_even (
    clk,
    pix_din_right,
    pix_sam,
    pix_psel,
    pix_we_even,
    pix_addr_even,
    pix_din_left,
    pix_noupdate,
    pix_prdata,
    pix_dout_right,
    pix_we_sam,
    pix_pready,
    pix_penable,
    pix_pclk,
    pix_dout_left,
    pix_state,
    pix_paddr,
    pix_din_sam,
    pix_dout_odd,
    pix_din_odd,
    pix_pslverr,
    pix_even_odd,
    pix_addr_right,
    pix_updated,
    pix_full,
    pix_fwd_inv,
    pix_presetn,
    pix_din_even,
    pix_dout_even,
    pix_addr_left,
    pix_pwdata,
    pix_pwrite,
    pix_dout_sam,
    pix_we_right,
    pix_transoutrdy,
    pix_addr_odd,
    pix_we_odd,
    pix_addr_sam,
    pix_we_left
);
// Ram model 

input clk;
input signed [16:0] pix_din_right;
input [7:0] pix_sam;
input pix_psel;
input pix_we_even;
input [7:0] pix_addr_even;
input signed [16:0] pix_din_left;
input pix_noupdate;
input [31:0] pix_prdata;
input signed [16:0] pix_dout_right;
input pix_we_sam;
input pix_pready;
input pix_penable;
input pix_pclk;
input signed [16:0] pix_dout_left;
input [1:0] pix_state;
input [31:0] pix_paddr;
input signed [16:0] pix_din_sam;
output signed [16:0] pix_dout_odd;
wire signed [16:0] pix_dout_odd;
input signed [16:0] pix_din_odd;
input pix_pslverr;
input pix_even_odd;
input [7:0] pix_addr_right;
input pix_updated;
input pix_full;
input pix_fwd_inv;
input pix_presetn;
input signed [16:0] pix_din_even;
output signed [16:0] pix_dout_even;
wire signed [16:0] pix_dout_even;
input [7:0] pix_addr_left;
input [31:0] pix_pwdata;
input pix_pwrite;
input signed [16:0] pix_dout_sam;
input pix_we_right;
input pix_transoutrdy;
input [7:0] pix_addr_odd;
input pix_we_odd;
input [7:0] pix_addr_sam;
input pix_we_left;


reg signed [16:0] mem_even [0:256-1];




always @(posedge clk) begin: RAM_EVEN_WRITE_EVEN
    if (pix_we_even) begin
        mem_even[pix_addr_even] <= pix_din_even;
    end
end



assign pix_dout_even = mem_even[pix_addr_even];

endmodule
