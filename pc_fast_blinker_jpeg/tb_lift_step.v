module tb_lift_step;

reg [2:0] flags_i;
reg update_i;
reg [7:0] left_i;
reg [7:0] sam_i;
reg [7:0] right_i;
wire [8:0] res_o;
wire update_o;
reg clk_i;

initial begin
    $from_myhdl(
        flags_i,
        update_i,
        left_i,
        sam_i,
        right_i,
        clk_i
    );
    $to_myhdl(
        res_o,
        update_o
    );
end

lift_step dut(
    flags_i,
    update_i,
    left_i,
    sam_i,
    right_i,
    res_o,
    update_o,
    clk_i
);

endmodule
