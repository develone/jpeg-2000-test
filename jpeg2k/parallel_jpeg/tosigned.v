// File: tosigned.v
// Generated by MyHDL 0.9dev
// Date: Wed Mar  4 10:10:07 2015


`timescale 1ns/10ps

module tosigned (
    bits_in,
    v
);
// return a signed representation of an 'unsigned' value 

input signed [9:0] bits_in;
output [9:0] v;
reg [9:0] v;






always @(bits_in) begin: TOSIGNED_TOSIGNED_LOGIC
    if (($signed(bits_in >>> (10 - 1)) & 1)) begin
        v = (-((~bits_in) + 1));
    end
    else begin
        v = bits_in;
    end
end

endmodule
