module tb_eq_d_c2;

wire [18:0] d3;
wire [18:0] a2;
reg clk;
reg [18:0] x2;
reg [18:0] x3;
reg [18:0] x4;

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

eq_d_c2 dut(
    d3,
    a2,
    clk,
    x2,
    x3,
    x4
);

endmodule
