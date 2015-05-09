module tb_lift_step;

reg [8:0] left_i;
reg [8:0] sam_i;
reg [8:0] right_i;
reg [3:0] flgs_i;
reg update_i;
reg clk;
wire [9:0] res_o;
wire update_o;

initial begin
    $from_myhdl(
        left_i,
        sam_i,
        right_i,
        flgs_i,
        update_i,
        clk
    );
    $to_myhdl(
        res_o,
        update_o
    );
end

lift_step dut(
    left_i,
    sam_i,
    right_i,
    flgs_i,
    update_i,
    clk,
    res_o,
    update_o
);

endmodule
