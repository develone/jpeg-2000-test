module tb_eq_d;

wire [9:0] d3;
wire [9:0] a2;
reg clk;
reg [9:0] x2;
reg [9:0] x3;
reg [9:0] x4;

initial begin
    $from_myhdl(
        clk,
        x2,
        x3,
        x4
    );
    $to_myhdl(
        d3,
        a2
    );
end

eq_d dut(
    d3,
    a2,
    clk,
    x2,
    x3,
    x4
);

endmodule
