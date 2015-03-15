// File: jp_process.v
// Generated by MyHDL 0.9dev
// Date: Sat Mar 14 20:35:37 2015


`timescale 1ns/10ps

module jp_process (
    res_out_x,
    left_s_i,
    sam_s_i,
    right_s_i,
    flgs_s_i,
    noupdate_s,
    update_s
);


output signed [15:0] res_out_x;
reg signed [15:0] res_out_x;
input [255:0] left_s_i;
input [255:0] sam_s_i;
input [255:0] right_s_i;
input [79:0] flgs_s_i;
output noupdate_s;
reg noupdate_s;
input update_s;


wire [15:0] right_s [0:16-1];
wire [4:0] flgs_s [0:16-1];
wire [15:0] sam_s [0:16-1];
wire [15:0] left_s [0:16-1];



// update_s needs to be 1
// for the res_out_x to be valid
// noupdate_s goes lo when a
// res_out_x valid
// fwd dwt even flgs_s eq 7
// inv dwt even flgs_s eq 5
// fwd dwt odd flgs_s eq 6
// inv dwt odd flgs_s eq 4
always @(update_s, right_s[0], right_s[1], right_s[2], right_s[3], right_s[4], right_s[5], right_s[6], right_s[7], right_s[8], right_s[9], right_s[10], right_s[11], right_s[12], right_s[13], right_s[14], right_s[15], flgs_s[0], flgs_s[1], flgs_s[2], flgs_s[3], flgs_s[4], flgs_s[5], flgs_s[6], flgs_s[7], flgs_s[8], flgs_s[9], flgs_s[10], flgs_s[11], flgs_s[12], flgs_s[13], flgs_s[14], flgs_s[15], sam_s[0], sam_s[1], sam_s[2], sam_s[3], sam_s[4], sam_s[5], sam_s[6], sam_s[7], sam_s[8], sam_s[9], sam_s[10], sam_s[11], sam_s[12], sam_s[13], sam_s[14], sam_s[15], left_s[0], left_s[1], left_s[2], left_s[3], left_s[4], left_s[5], left_s[6], left_s[7], left_s[8], left_s[9], left_s[10], left_s[11], left_s[12], left_s[13], left_s[14], left_s[15]) begin: JP_PROCESS_JPEG_LOGIC
    integer i;
    if (update_s) begin
        noupdate_s = 0;
        for (i=0; i<16; i=i+1) begin
            if ((flgs_s[i] == 7)) begin
                res_out_x = (sam_s[i] - ((left_s[i] >>> 1) + (right_s[i] >>> 1)));
            end
            else if ((flgs_s[i] == 5)) begin
                res_out_x = (sam_s[i] + ((left_s[i] >>> 1) + (right_s[i] >>> 1)));
            end
            else if ((flgs_s[i] == 6)) begin
                res_out_x = (sam_s[i] + ((left_s[i] + (right_s[i] + 2)) >>> 2));
            end
            else if ((flgs_s[i] == 4)) begin
                res_out_x = (sam_s[i] - ((left_s[i] + (right_s[i] + 2)) >>> 2));
            end
        end
    end
    else begin
        noupdate_s = 1;
    end
end

endmodule
