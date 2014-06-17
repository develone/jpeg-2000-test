module tb_add_mul;

wire [35:0] d3;
wire [35:0] a2;
reg clk;
reg [10:0] x1;
reg [10:0] x2;
reg [10:0] x3;
reg [10:0] x4;
reg [10:0] x5;
reg odd_even;

initial begin
    $from_myhdl(
        clk,
        x1,
        x2,
        x3,
        x4,
        x5,
        odd_even
    );
    $to_myhdl(
        d3,
        a2
    );
end

add_mul dut(
    d3,
    a2,
    clk,
    x1,
    x2,
    x3,
    x4,
    x5,
    odd_even
);

endmodule
