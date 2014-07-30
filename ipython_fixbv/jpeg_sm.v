// File: jpeg_sm.v
// Generated by MyHDL 0.9dev
// Date: Tue Jul 29 18:03:50 2014


`timescale 1ns/10ps

module jpeg_sm (
    resetn,
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
// If state is TRANSFER_IN data is written to ram_sam, ram_left, and ram_right.
// If state is TRANSFER_OUT ram_even and ram_odd.
// If state is Update_Sample on a given sam the addr_left will be set sam - 1 & addr_right will
// be set sam + 1 updated will be set True
// if sam is even even_odd will be set True if sam is odd even_odd will be set False
// if sam = 255 or 256 state_t is set TRANSFER_OUT which is the end of samples

input resetn;
input signed [16:0] pix_din_right;
input [7:0] pix_sam;
input pix_psel;
input pix_we_even;
output [7:0] pix_addr_even;
reg [7:0] pix_addr_even;
input signed [16:0] pix_din_left;
input pix_noupdate;
input [31:0] pix_prdata;
input signed [16:0] pix_dout_right;
input pix_we_sam;
input pix_pready;
input pix_penable;
input pix_pclk;
input signed [16:0] pix_dout_left;
output [1:0] pix_state;
reg [1:0] pix_state;
input [31:0] pix_paddr;
input signed [16:0] pix_din_sam;
input signed [16:0] pix_dout_odd;
input signed [16:0] pix_din_odd;
input pix_pslverr;
output pix_even_odd;
reg pix_even_odd;
output [7:0] pix_addr_right;
reg [7:0] pix_addr_right;
output pix_updated;
reg pix_updated;
input pix_full;
input pix_fwd_inv;
input pix_presetn;
input signed [16:0] pix_din_even;
input signed [16:0] pix_dout_even;
output [7:0] pix_addr_left;
reg [7:0] pix_addr_left;
input [31:0] pix_pwdata;
input pix_pwrite;
input signed [16:0] pix_dout_sam;
input pix_we_right;
output pix_transoutrdy;
reg pix_transoutrdy;
output [7:0] pix_addr_odd;
reg [7:0] pix_addr_odd;
input pix_we_odd;
output [7:0] pix_addr_sam;
reg [7:0] pix_addr_sam;
input pix_we_left;






always @(posedge pix_pclk, negedge pix_presetn) begin: JPEG_SM_STATE_MACHINE
    if (pix_presetn == 0) begin
        pix_state <= 2'b00;
        pix_addr_left <= 0;
        pix_even_odd <= 0;
        pix_transoutrdy <= 0;
        pix_addr_right <= 0;
        pix_addr_sam <= 0;
        pix_updated <= 0;
        pix_addr_odd <= 0;
        pix_addr_even <= 0;
    end
    else begin
        if ((pix_presetn == 0)) begin
            pix_updated <= 0;
            pix_even_odd <= 0;
            pix_addr_left <= 0;
            pix_addr_right <= 0;
            pix_addr_sam <= 0;
            pix_addr_odd <= 0;
            pix_addr_even <= 0;
            pix_transoutrdy <= 0;
            pix_state <= 2'b00;
        end
        else begin
            pix_state <= 2'b01;
            case (pix_state)
                2'b00: begin
                    pix_state <= 2'b01;
                end
                2'b01: begin
                    if (((pix_sam % 2) == 0)) begin
                        pix_even_odd <= 1;
                        pix_addr_even <= pix_sam;
                    end
                    else begin
                        pix_even_odd <= 0;
                        pix_addr_odd <= pix_sam;
                        pix_addr_sam <= pix_sam;
                        pix_addr_left <= (pix_sam - 1);
                        if ((pix_sam <= 254)) begin
                            pix_addr_right <= (pix_sam + 1);
                        end
                        pix_addr_even <= pix_sam;
                        pix_addr_odd <= pix_sam;
                        pix_updated <= 1;
                        case (pix_sam)
                            'hff: begin
                                pix_updated <= 0;
                                pix_state <= 2'b10;
                            end
                            'hfe: begin
                                pix_updated <= 0;
                                pix_state <= 2'b10;
                            end
                        endcase
                    end
                end
                2'b10: begin
                    pix_transoutrdy <= 1;
                    pix_state <= 2'b00;
                end
                2'b11: begin
                    pix_updated <= 1;
                    pix_state <= 2'b01;
                    pix_state <= 2'b00;
                end
            endcase
        end
    end
end

endmodule