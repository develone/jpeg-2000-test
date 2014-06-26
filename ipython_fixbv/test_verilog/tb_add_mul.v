module tb_add_mul;

reg [23:0] d3;
reg [23:0] a2;
reg clk;
reg [23:0] x2;
reg [23:0] x3;
reg [23:0] x4;
reg [23:0] x5;
reg p;
reg odd_even;
reg fwd_res;

initial begin
    $from_myhdl(
        d3,
        a2,
        clk,
        x2,
        x3,
        x4,
        x5,
        p,
        odd_even,
        fwd_res
    );
end

add_mul dut(
    d3,
    a2,
    clk,
    x2,
    x3,
    x4,
    x5,
    p,
    odd_even,
    fwd_res
);

endmodule
