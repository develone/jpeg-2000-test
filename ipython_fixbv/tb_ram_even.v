module tb_ram_even;

reg clk;
reg [16:0] pix_din_right;
reg pix_we_even;
reg [7:0] pix_addr_even;
reg [16:0] pix_din_left;
reg [16:0] pix_dout_right;
reg pix_we_sam;
reg [16:0] pix_dout_left;
reg [16:0] pix_din_sam;
wire [16:0] pix_dout_odd;
reg [16:0] pix_din_odd;
reg pix_even_odd;
reg [7:0] pix_addr_right;
reg pix_fwd_inv;
reg [16:0] pix_din_even;
wire [16:0] pix_dout_even;
reg [7:0] pix_addr_left;
reg [16:0] pix_dout_sam;
reg pix_we_right;
reg [7:0] pix_addr_odd;
reg pix_we_odd;
reg [7:0] pix_addr_sam;
reg pix_we_left;

initial begin
    $from_myhdl(
        clk,
        pix_din_right,
        pix_we_even,
        pix_addr_even,
        pix_din_left,
        pix_dout_right,
        pix_we_sam,
        pix_dout_left,
        pix_din_sam,
        pix_din_odd,
        pix_even_odd,
        pix_addr_right,
        pix_fwd_inv,
        pix_din_even,
        pix_addr_left,
        pix_dout_sam,
        pix_we_right,
        pix_addr_odd,
        pix_we_odd,
        pix_addr_sam,
        pix_we_left
    );
    $to_myhdl(
        pix_dout_odd,
        pix_dout_even
    );
end

ram_even dut(
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

endmodule
