module tb_fpgalink_nexys;

reg IFCLK;
reg RST;
wire SLWR;
wire SLRD;
wire SLOE;
reg [7:0] FDI;
wire [7:0] FDO;
wire FDS;
wire [1:0] ADDR;
reg FLAGA;
reg FLAGB;
reg FLAGC;
reg FLAGD;
wire PKTEND;
wire [7:0] LEDS;

initial begin
    $from_myhdl(
        IFCLK,
        RST,
        FDI,
        FLAGA,
        FLAGB,
        FLAGC,
        FLAGD
    );
    $to_myhdl(
        SLWR,
        SLRD,
        SLOE,
        FDO,
        FDS,
        ADDR,
        PKTEND,
        LEDS
    );
end

fpgalink_nexys dut(
    IFCLK,
    RST,
    SLWR,
    SLRD,
    SLOE,
    FDI,
    FDO,
    FDS,
    ADDR,
    FLAGA,
    FLAGB,
    FLAGC,
    FLAGD,
    PKTEND,
    LEDS
);

endmodule
