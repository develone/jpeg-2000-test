module tb_ram_even;

reg clk;
reg [8:0] pix_right;
reg pix_we_even;
reg [6:0] pix_addr_odd;
reg pix_fwd_inv;
reg [6:0] pix_addr_even;
reg [8:0] pix_din_even;
reg pix_we_odd;
wire [8:0] pix_dout_odd;
reg [8:0] pix_din_odd;
wire [8:0] pix_dout_even;
reg pix_even_odd;
reg [8:0] pix_left;

initial begin
    $from_myhdl(
        clk,
        pix_right,
        pix_we_even,
        pix_addr_odd,
        pix_fwd_inv,
        pix_addr_even,
        pix_din_even,
        pix_we_odd,
        pix_din_odd,
        pix_even_odd,
        pix_left
    );
    $to_myhdl(
        pix_dout_odd,
        pix_dout_even
    );
end

ram_even dut(
    clk,
    pix_right,
    pix_we_even,
    pix_addr_odd,
    pix_fwd_inv,
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
