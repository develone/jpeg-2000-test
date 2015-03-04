// File: tounsigned.v
// Generated by MyHDL 0.9dev
// Date: Wed Mar  4 11:21:33 2015


`timescale 1ns/10ps

module tounsigned (
    bits_in,
    v
);
// return an unsigned value to represent a possibly 'signed' value

input signed [9:0] bits_in;
output [9:0] v;
reg [9:0] v;






always @(bits_in) begin: TOUNSIGNED_UNSIGNED_LOGIC
    if ((bits_in >= 0)) begin
        v = bits_in;
    end
    else begin
        v = ((2 ** 10) + bits_in);
    end
end

endmodule
