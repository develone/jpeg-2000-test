module tb_mult_mul_add;

reg clk;
reg p;
reg even_odd;
reg fwd_inv;
reg [25:0] pix_x2_3;
reg [25:0] pix_x2_2;
reg [25:0] pix_x2_1;
reg [25:0] pix_x4_1;
reg [25:0] pix_x4_3;
reg [25:0] pix_x4_2;
reg [25:0] pix_x3_2;
wire [25:0] pix_d3;
reg [25:0] pix_x3_1;
wire [25:0] pix_d3_3;
reg [25:0] pix_x5_1;
reg [25:0] pix_x5_2;
reg [25:0] pix_x5_3;
wire [25:0] pix_a2_3;
reg [25:0] pix_x3_3;
wire [25:0] pix_a2;
reg [25:0] pix_x2;
reg [25:0] pix_x3;
reg [25:0] pix_x4;
reg [25:0] pix_x5;
wire [25:0] pix_d3_2;
wire [25:0] pix_a2_1;
wire [25:0] pix_a2_2;
wire [25:0] pix_d3_1;

initial begin
    $from_myhdl(
        clk,
        p,
        even_odd,
        fwd_inv,
        pix_x2_3,
        pix_x2_2,
        pix_x2_1,
        pix_x4_1,
        pix_x4_3,
        pix_x4_2,
        pix_x3_2,
        pix_x3_1,
        pix_x5_1,
        pix_x5_2,
        pix_x5_3,
        pix_x3_3,
        pix_x2,
        pix_x3,
        pix_x4,
        pix_x5
    );
    $to_myhdl(
        pix_d3,
        pix_d3_3,
        pix_a2_3,
        pix_a2,
        pix_d3_2,
        pix_a2_1,
        pix_a2_2,
        pix_d3_1
    );
end

mult_mul_add dut(
    clk,
    p,
    even_odd,
    fwd_inv,
    pix_x2_3,
    pix_x2_2,
    pix_x2_1,
    pix_x4_1,
    pix_x4_3,
    pix_x4_2,
    pix_x3_2,
    pix_d3,
    pix_x3_1,
    pix_d3_3,
    pix_x5_1,
    pix_x5_2,
    pix_x5_3,
    pix_a2_3,
    pix_x3_3,
    pix_a2,
    pix_x2,
    pix_x3,
    pix_x4,
    pix_x5,
    pix_d3_2,
    pix_a2_1,
    pix_a2_2,
    pix_d3_1
);

endmodule
