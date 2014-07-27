module tb_ram_even;

reg clk;
reg [16:0] pix_din_right;
reg [7:0] pix_sam;
reg pix_psel;
reg pix_we_even;
reg [7:0] pix_addr_even;
reg [16:0] pix_din_left;
reg pix_noupdate;
reg [31:0] pix_prdata;
reg [16:0] pix_dout_right;
reg pix_we_sam;
reg pix_pready;
reg pix_penable;
reg pix_pclk;
reg [16:0] pix_dout_left;
reg [1:0] pix_state;
reg [31:0] pix_paddr;
reg [16:0] pix_din_sam;
wire [16:0] pix_dout_odd;
reg [16:0] pix_din_odd;
reg pix_pslverr;
reg pix_even_odd;
reg [7:0] pix_addr_right;
reg pix_updated;
reg pix_full;
reg pix_fwd_inv;
reg pix_presetn;
reg [16:0] pix_din_even;
wire [16:0] pix_dout_even;
reg [7:0] pix_addr_left;
reg [31:0] pix_pwdata;
reg pix_pwrite;
reg [16:0] pix_dout_sam;
reg pix_we_right;
reg pix_transoutrdy;
reg [7:0] pix_addr_odd;
reg pix_we_odd;
reg [7:0] pix_addr_sam;
reg pix_we_left;

initial begin
    $from_myhdl(
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
        pix_din_odd,
        pix_pslverr,
        pix_even_odd,
        pix_addr_right,
        pix_updated,
        pix_full,
        pix_fwd_inv,
        pix_presetn,
        pix_din_even,
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
    $to_myhdl(
        pix_dout_odd,
        pix_dout_even
    );
end

ram_even dut(
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

endmodule
