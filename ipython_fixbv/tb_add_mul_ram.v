module tb_add_mul_ram;

reg clk;
reg [25:0] pix_dout_even1;
reg [25:0] pix_right;
reg [25:0] pix_left1;
reg [6:0] pix_addr_odd1;
reg [6:0] pix_addr_even1;
reg pix_we_even;
reg [6:0] pix_addr_even;
reg [25:0] pix_right1;
reg [25:0] pix_dout_odd1;
wire [25:0] pix_din_even1;
reg [25:0] pix_dout_odd;
wire [25:0] pix_din_odd;
reg pix_even_odd;
reg pix_we_even1;
wire [25:0] pix_din_odd1;
reg pix_fwd_inv;
wire [25:0] pix_din_even;
reg [25:0] pix_dout_even;
reg pix_we_odd1;
reg pix_p;
reg [6:0] pix_addr_odd;
reg pix_we_odd;
reg [25:0] pix_left;

initial begin
    $from_myhdl(
        clk,
        pix_dout_even1,
        pix_right,
        pix_left1,
        pix_addr_odd1,
        pix_addr_even1,
        pix_we_even,
        pix_addr_even,
        pix_right1,
        pix_dout_odd1,
        pix_dout_odd,
        pix_even_odd,
        pix_we_even1,
        pix_fwd_inv,
        pix_dout_even,
        pix_we_odd1,
        pix_p,
        pix_addr_odd,
        pix_we_odd,
        pix_left
    );
    $to_myhdl(
        pix_din_even1,
        pix_din_odd,
        pix_din_odd1,
        pix_din_even
    );
end

add_mul_ram dut(
    clk,
    pix_dout_even1,
    pix_right,
    pix_left1,
    pix_addr_odd1,
    pix_addr_even1,
    pix_we_even,
    pix_addr_even,
    pix_right1,
    pix_dout_odd1,
    pix_din_even1,
    pix_dout_odd,
    pix_din_odd,
    pix_even_odd,
    pix_we_even1,
    pix_din_odd1,
    pix_fwd_inv,
    pix_din_even,
    pix_dout_even,
    pix_we_odd1,
    pix_p,
    pix_addr_odd,
    pix_we_odd,
    pix_left
);

endmodule
