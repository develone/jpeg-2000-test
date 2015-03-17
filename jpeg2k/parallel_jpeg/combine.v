// File: combine.v
// Generated by MyHDL 0.9dev
// Date: Tue Mar 17 12:58:36 2015


`timescale 1ns/10ps

module combine (
    left_com_x,
    sam_com_x,
    right_com_x,
    lft_s_i,
    sa_s_i,
    rht_s_i,
    combine_rdy_s,
    nocombine_s
);


output [127:0] left_com_x;
reg [127:0] left_com_x;
output [127:0] sam_com_x;
reg [127:0] sam_com_x;
output [127:0] right_com_x;
reg [127:0] right_com_x;
input [127:0] lft_s_i;
input [127:0] sa_s_i;
input [127:0] rht_s_i;
input combine_rdy_s;
output nocombine_s;
reg nocombine_s;


wire [7:0] rht_s [0:16-1];
wire [7:0] sa_s [0:16-1];
wire [7:0] lft_s [0:16-1];




always @(rht_s[0], rht_s[1], rht_s[2], rht_s[3], rht_s[4], rht_s[5], rht_s[6], rht_s[7], rht_s[8], rht_s[9], rht_s[10], rht_s[11], rht_s[12], rht_s[13], rht_s[14], rht_s[15], sa_s[0], sa_s[1], sa_s[2], sa_s[3], sa_s[4], sa_s[5], sa_s[6], sa_s[7], sa_s[8], sa_s[9], sa_s[10], sa_s[11], sa_s[12], sa_s[13], sa_s[14], sa_s[15], lft_s[0], lft_s[1], lft_s[2], lft_s[3], lft_s[4], lft_s[5], lft_s[6], lft_s[7], lft_s[8], lft_s[9], lft_s[10], lft_s[11], lft_s[12], lft_s[13], lft_s[14], lft_s[15], combine_rdy_s) begin: COMBINE_COMBINE_LOGIC
    if ((combine_rdy_s == 1)) begin
        left_com_x = {lft_s[15], lft_s[14], lft_s[13], lft_s[12], lft_s[11], lft_s[10], lft_s[9], lft_s[8], lft_s[7], lft_s[6], lft_s[5], lft_s[4], lft_s[3], lft_s[2], lft_s[1], lft_s[0]};
        sam_com_x = {sa_s[15], sa_s[14], sa_s[13], sa_s[12], sa_s[11], sa_s[10], sa_s[9], sa_s[8], sa_s[7], sa_s[6], sa_s[5], sa_s[4], sa_s[3], sa_s[2], sa_s[1], sa_s[0]};
        right_com_x = {rht_s[15], rht_s[14], rht_s[13], rht_s[12], rht_s[11], rht_s[10], rht_s[9], rht_s[8], rht_s[7], rht_s[6], rht_s[5], rht_s[4], rht_s[3], rht_s[2], rht_s[1], rht_s[0]};
        nocombine_s = 0;
    end
    else begin
        left_com_x = 0;
        sam_com_x = 0;
        right_com_x = 0;
        nocombine_s = 1;
    end
end

endmodule
