module tb_ram_even;

reg clk;
reg [6:0] pix_addr_r;
reg [25:0] pix_din_r;
reg pix_we_r;
reg [25:0] pix_dout_r;
wire [25:0] pix_dout_l;
reg [25:0] pix_din_l;
reg [6:0] pix_addr_odd;
reg pix_we_odd;
reg pix_we_l;
reg [6:0] pix_addr_even;
reg [25:0] pix_din_even;
reg pix_we_even;
wire [25:0] pix_dout_odd;
reg [25:0] pix_din_odd;
wire [25:0] pix_dout_even;
reg [6:0] pix_addr_l;

initial begin
    $from_myhdl(
        clk,
        pix_addr_r,
        pix_din_r,
        pix_we_r,
        pix_dout_r,
        pix_din_l,
        pix_addr_odd,
        pix_we_odd,
        pix_we_l,
        pix_addr_even,
        pix_din_even,
        pix_we_even,
        pix_din_odd,
        pix_addr_l
    );
    $to_myhdl(
        pix_dout_l,
        pix_dout_odd,
        pix_dout_even
    );
end

ram_even dut(
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

endmodule
