module tb_ram_l;

reg clk;
reg [6:0] pix_addr_r;
reg [25:0] pix_right;
reg [25:0] pix_din_r;
reg pix_we_r;
wire [25:0] pix_dout_r;
reg pix_we_even;
wire [25:0] pix_dout_l;
reg [25:0] pix_din_l;
reg pix_p;
reg [6:0] pix_addr_odd;
reg pix_fwd_inv;
reg pix_we_l;
reg [6:0] pix_addr_l;
reg [6:0] pix_addr_even;
reg [25:0] pix_din_even;
reg pix_we_odd;
reg [25:0] pix_dout_odd;
reg [25:0] pix_din_odd;
reg [25:0] pix_dout_even;
reg pix_even_odd;
reg [25:0] pix_left;

initial begin
    $from_myhdl(
        clk,
        pix_addr_r,
        pix_right,
        pix_din_r,
        pix_we_r,
        pix_we_even,
        pix_din_l,
        pix_p,
        pix_addr_odd,
        pix_fwd_inv,
        pix_we_l,
        pix_addr_l,
        pix_addr_even,
        pix_din_even,
        pix_we_odd,
        pix_dout_odd,
        pix_din_odd,
        pix_dout_even,
        pix_even_odd,
        pix_left
    );
    $to_myhdl(
        pix_dout_r,
        pix_dout_l
    );
end

ram_l dut(
    clk,
    pix_addr_r,
    pix_right,
    pix_din_r,
    pix_we_r,
    pix_dout_r,
    pix_we_even,
    pix_dout_l,
    pix_din_l,
    pix_p,
    pix_addr_odd,
    pix_fwd_inv,
    pix_we_l,
    pix_addr_l,
    pix_addr_even,
    pix_din_even,
    pix_we_odd,
    pix_dout_odd,
    pix_din_odd,
    pix_dout_even,
    pix_even_odd,
    pix_left
);

endmodule
