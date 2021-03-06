// File: add_shift_ram.v
// Generated by MyHDL 0.9dev
// Date: Sun Aug  3 18:21:35 2014


`timescale 1ns/10ps

module add_shift_ram (
    pix_din_right,
    pix_sam,
    pix_psel,
    pix_din_res,
    pix_dout_res,
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
    pix_addr_res,
    pix_din_sam,
    pix_pslverr,
    pix_even_odd,
    pix_addr_right,
    pix_updated,
    pix_full,
    pix_we_res,
    pix_fwd_inv,
    pix_presetn,
    pix_addr_left,
    pix_pwdata,
    pix_pwrite,
    pix_dout_sam,
    pix_we_right,
    pix_transinrdy,
    pix_transoutrdy,
    pix_addr_sam,
    pix_we_left
);
// Ram model 

input signed [16:0] pix_din_right;
input [7:0] pix_sam;
input pix_psel;
output signed [16:0] pix_din_res;
reg signed [16:0] pix_din_res;
output signed [16:0] pix_dout_res;
wire signed [16:0] pix_dout_res;
input signed [16:0] pix_din_left;
output pix_noupdate;
reg pix_noupdate;
input [31:0] pix_prdata;
output signed [16:0] pix_dout_right;
wire signed [16:0] pix_dout_right;
input pix_we_sam;
input pix_pready;
input pix_penable;
input pix_pclk;
output signed [16:0] pix_dout_left;
wire signed [16:0] pix_dout_left;
input [1:0] pix_state;
input [31:0] pix_paddr;
input [7:0] pix_addr_res;
input signed [16:0] pix_din_sam;
input pix_pslverr;
input pix_even_odd;
input [7:0] pix_addr_right;
input pix_updated;
input pix_full;
input pix_we_res;
input pix_fwd_inv;
input pix_presetn;
input [7:0] pix_addr_left;
input [31:0] pix_pwdata;
input pix_pwrite;
output signed [16:0] pix_dout_sam;
wire signed [16:0] pix_dout_sam;
input pix_we_right;
input pix_transinrdy;
input pix_transoutrdy;
input [7:0] pix_addr_sam;
input pix_we_left;


reg signed [16:0] mem_right [0:256-1];
reg signed [16:0] mem_res [0:256-1];
reg signed [16:0] mem_sam [0:256-1];
reg signed [16:0] mem_left [0:256-1];




always @(posedge pix_pclk) begin: ADD_SHIFT_RAM_HDL
    if ((pix_updated == 1)) begin
        if (pix_even_odd) begin
            if (pix_fwd_inv) begin
                pix_din_res <= (pix_dout_sam - ($signed(pix_dout_left >>> 1) + $signed(pix_dout_right >>> 1)));
            end
            else begin
                pix_din_res <= (pix_dout_sam + ($signed(pix_dout_left >>> 1) + $signed(pix_dout_right >>> 1)));
            end
        end
        else begin
            if (pix_fwd_inv) begin
                pix_din_res <= $signed((pix_dout_sam + ((pix_dout_left + pix_dout_right) + 2)) >>> 2);
            end
            else begin
                pix_din_res <= $signed((pix_dout_sam - ((pix_dout_left + pix_dout_right) + 2)) >>> 2);
            end
        end
    end
    else begin
        pix_noupdate <= 1;
    end
end


always @(posedge pix_pclk) begin: ADD_SHIFT_RAM_WRITE_SAM
    if (pix_we_sam) begin
        mem_sam[pix_addr_sam] <= pix_din_sam;
    end
end



assign pix_dout_sam = mem_sam[pix_addr_sam];


always @(posedge pix_pclk) begin: ADD_SHIFT_RAM_WRITE_RIGHT
    if (pix_we_right) begin
        mem_right[pix_addr_right] <= pix_din_right;
    end
end



assign pix_dout_right = mem_right[pix_addr_right];


always @(posedge pix_pclk) begin: ADD_SHIFT_RAM_WRITE_LEFT
    if (pix_we_left) begin
        mem_left[pix_addr_left] <= pix_din_left;
    end
end



assign pix_dout_left = mem_left[pix_addr_left];


always @(posedge pix_pclk) begin: ADD_SHIFT_RAM_WRITE_RES
    if (pix_we_res) begin
        mem_res[pix_addr_res] <= pix_din_res;
    end
end



assign pix_dout_res = mem_res[pix_addr_res];

endmodule
