module tb_RamCtrl;

wire SOF;
wire [4:0] state;
reg WR_DATAFlag;
reg clk_fast;
reg reset_n;
wire [22:0] addrsam_r;
wire [22:0] addrjpeg_r;
wire rd_r;
wire wr_r;

initial begin
    $from_myhdl(
        WR_DATAFlag,
        clk_fast,
        reset_n
    );
    $to_myhdl(
        SOF,
        state,
        addrsam_r,
        addrjpeg_r,
        rd_r,
        wr_r
    );
end

RamCtrl dut(
    SOF,
    state,
    WR_DATAFlag,
    clk_fast,
    reset_n,
    addrsam_r,
    addrjpeg_r,
    rd_r,
    wr_r
);

endmodule
