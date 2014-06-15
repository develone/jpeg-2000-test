module tb_add_shift;

wire [18:0] d3;
wire [18:0] a2;
reg [18:0] x2;
reg [18:0] x3;
reg [18:0] x4;
reg [18:0] x5;

initial begin
    $from_myhdl(
        x2,
        x3,
        x4,
        x5
    );
    $to_myhdl(
        d3,
        a2
    );
end

add_shift dut(
    d3,
    a2,
    x2,
    x3,
    x4,
    x5
);

endmodule
