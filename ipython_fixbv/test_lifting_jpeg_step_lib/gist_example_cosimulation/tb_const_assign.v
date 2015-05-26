module tb_const_assign;

wire aBit;
wire [7:0] aByte;

initial begin
    $to_myhdl(
        aBit,
        aByte
    );
end

const_assign dut(
    aBit,
    aByte
);

endmodule
