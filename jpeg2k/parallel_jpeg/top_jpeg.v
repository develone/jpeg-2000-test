// File: top_jpeg.v
// Generated by MyHDL 0.9dev
// Date: Wed Apr  1 16:37:00 2015


`timescale 1ns/10ps

module top_jpeg (
    clk,
    res_out_x,
    left_s_i,
    sam_s_i,
    right_s_i,
    flgs_s_i,
    noupdate_s,
    update_s,
    row_ind,
    col_ind,
    flat_lf,
    flat_sa,
    flat_rt,
    z,
    x,
    ma_row,
    ma_col,
    bits_in_sig,
    vv,
    dout_lf,
    dout_sa,
    dout_rt,
    dout_res,
    din_lf,
    din_sa,
    din_rt,
    din_res,
    addr_lf,
    addr_sa,
    addr_rt,
    addr_res,
    we_lf,
    we_sa,
    we_rt,
    we_res,
    dout_flgs,
    addr_flgs
);


input clk;
output signed [9:0] res_out_x;
reg signed [9:0] res_out_x;
input [143:0] left_s_i;
input [143:0] sam_s_i;
input [143:0] right_s_i;
input [79:0] flgs_s_i;
output noupdate_s;
reg noupdate_s;
input update_s;
input [9:0] row_ind;
input [9:0] col_ind;
output [143:0] flat_lf;
wire [143:0] flat_lf;
output [143:0] flat_sa;
wire [143:0] flat_sa;
output [143:0] flat_rt;
wire [143:0] flat_rt;
input [8:0] z;
input signed [9:0] x;
input [3:0] ma_row;
input [3:0] ma_col;
input signed [9:0] bits_in_sig;
output [8:0] vv;
wire [8:0] vv;
output [143:0] dout_lf;
wire [143:0] dout_lf;
output [143:0] dout_sa;
wire [143:0] dout_sa;
output [143:0] dout_rt;
wire [143:0] dout_rt;
output [8:0] dout_res;
wire [8:0] dout_res;
input [143:0] din_lf;
input [143:0] din_sa;
input [143:0] din_rt;
input [8:0] din_res;
input [9:0] addr_lf;
input [9:0] addr_sa;
input [9:0] addr_rt;
input [9:0] addr_res;
input we_lf;
input we_sa;
input we_rt;
input we_res;
output [79:0] dout_flgs;
reg [79:0] dout_flgs;
input [9:0] addr_flgs;

wire [8:0] instance_mat_rt_mcol;
wire [143:0] instance_mat_rt_flat_i;
wire [8:0] instance_mat_sa_mcol;
wire [143:0] instance_mat_sa_flat_i;
wire [8:0] instance_mat_lf_mcol;
wire [143:0] instance_mat_lf_flat_i;

wire [8:0] instance_dut_right_s [0:16-1];
wire [4:0] instance_dut_flgs_s [0:16-1];
wire [8:0] instance_dut_sam_s [0:16-1];
wire [8:0] instance_dut_left_s [0:16-1];
reg [8:0] instance_ram_res_mem [0:512-1];
reg [143:0] instance_ram_rt_mem [0:512-1];
reg [143:0] instance_ram_sa_mem [0:512-1];
reg [143:0] instance_ram_lf_mem [0:512-1];

assign instance_mat_rt_mcol = 0;
assign instance_mat_sa_mcol = 0;
assign instance_mat_lf_mcol = 0;

assign instance_mat_rt_flat_i[144-1:135] = None;
assign instance_mat_rt_flat_i[135-1:126] = None;
assign instance_mat_rt_flat_i[126-1:117] = None;
assign instance_mat_rt_flat_i[117-1:108] = None;
assign instance_mat_rt_flat_i[108-1:99] = None;
assign instance_mat_rt_flat_i[99-1:90] = None;
assign instance_mat_rt_flat_i[90-1:81] = None;
assign instance_mat_rt_flat_i[81-1:72] = None;
assign instance_mat_rt_flat_i[72-1:63] = None;
assign instance_mat_rt_flat_i[63-1:54] = None;
assign instance_mat_rt_flat_i[54-1:45] = None;
assign instance_mat_rt_flat_i[45-1:36] = None;
assign instance_mat_rt_flat_i[36-1:27] = None;
assign instance_mat_rt_flat_i[27-1:18] = None;
assign instance_mat_rt_flat_i[18-1:9] = None;
assign instance_mat_rt_flat_i[9-1:0] = instance_mat_rt_mcol[9-1:0];
assign instance_mat_sa_flat_i[144-1:135] = None;
assign instance_mat_sa_flat_i[135-1:126] = None;
assign instance_mat_sa_flat_i[126-1:117] = None;
assign instance_mat_sa_flat_i[117-1:108] = None;
assign instance_mat_sa_flat_i[108-1:99] = None;
assign instance_mat_sa_flat_i[99-1:90] = None;
assign instance_mat_sa_flat_i[90-1:81] = None;
assign instance_mat_sa_flat_i[81-1:72] = None;
assign instance_mat_sa_flat_i[72-1:63] = None;
assign instance_mat_sa_flat_i[63-1:54] = None;
assign instance_mat_sa_flat_i[54-1:45] = None;
assign instance_mat_sa_flat_i[45-1:36] = None;
assign instance_mat_sa_flat_i[36-1:27] = None;
assign instance_mat_sa_flat_i[27-1:18] = None;
assign instance_mat_sa_flat_i[18-1:9] = None;
assign instance_mat_sa_flat_i[9-1:0] = instance_mat_sa_mcol[9-1:0];
assign instance_mat_lf_flat_i[144-1:135] = None;
assign instance_mat_lf_flat_i[135-1:126] = None;
assign instance_mat_lf_flat_i[126-1:117] = None;
assign instance_mat_lf_flat_i[117-1:108] = None;
assign instance_mat_lf_flat_i[108-1:99] = None;
assign instance_mat_lf_flat_i[99-1:90] = None;
assign instance_mat_lf_flat_i[90-1:81] = None;
assign instance_mat_lf_flat_i[81-1:72] = None;
assign instance_mat_lf_flat_i[72-1:63] = None;
assign instance_mat_lf_flat_i[63-1:54] = None;
assign instance_mat_lf_flat_i[54-1:45] = None;
assign instance_mat_lf_flat_i[45-1:36] = None;
assign instance_mat_lf_flat_i[36-1:27] = None;
assign instance_mat_lf_flat_i[27-1:18] = None;
assign instance_mat_lf_flat_i[18-1:9] = None;
assign instance_mat_lf_flat_i[9-1:0] = instance_mat_lf_mcol[9-1:0];



assign vv = bits_in_sig;

// update_s needs to be 1
// for the res_out_x to be valid
// noupdate_s goes lo when a
// res_out_x valid
// fwd dwt even flgs_s eq 7
// inv dwt even flgs_s eq 5
// fwd dwt odd flgs_s eq 6
// inv dwt odd flgs_s eq 4
always @(update_s, instance_dut_right_s[0], instance_dut_right_s[1], instance_dut_right_s[2], instance_dut_right_s[3], instance_dut_right_s[4], instance_dut_right_s[5], instance_dut_right_s[6], instance_dut_right_s[7], instance_dut_right_s[8], instance_dut_right_s[9], instance_dut_right_s[10], instance_dut_right_s[11], instance_dut_right_s[12], instance_dut_right_s[13], instance_dut_right_s[14], instance_dut_right_s[15], instance_dut_flgs_s[0], instance_dut_flgs_s[1], instance_dut_flgs_s[2], instance_dut_flgs_s[3], instance_dut_flgs_s[4], instance_dut_flgs_s[5], instance_dut_flgs_s[6], instance_dut_flgs_s[7], instance_dut_flgs_s[8], instance_dut_flgs_s[9], instance_dut_flgs_s[10], instance_dut_flgs_s[11], instance_dut_flgs_s[12], instance_dut_flgs_s[13], instance_dut_flgs_s[14], instance_dut_flgs_s[15], instance_dut_sam_s[0], instance_dut_sam_s[1], instance_dut_sam_s[2], instance_dut_sam_s[3], instance_dut_sam_s[4], instance_dut_sam_s[5], instance_dut_sam_s[6], instance_dut_sam_s[7], instance_dut_sam_s[8], instance_dut_sam_s[9], instance_dut_sam_s[10], instance_dut_sam_s[11], instance_dut_sam_s[12], instance_dut_sam_s[13], instance_dut_sam_s[14], instance_dut_sam_s[15], instance_dut_left_s[0], instance_dut_left_s[1], instance_dut_left_s[2], instance_dut_left_s[3], instance_dut_left_s[4], instance_dut_left_s[5], instance_dut_left_s[6], instance_dut_left_s[7], instance_dut_left_s[8], instance_dut_left_s[9], instance_dut_left_s[10], instance_dut_left_s[11], instance_dut_left_s[12], instance_dut_left_s[13], instance_dut_left_s[14], instance_dut_left_s[15]) begin: TOP_JPEG_INSTANCE_DUT_JPEG_LOGIC
    integer i;
    if (update_s) begin
        noupdate_s = 0;
        for (i=0; i<16; i=i+1) begin
            if ((instance_dut_flgs_s[i] == 7)) begin
                res_out_x = ($signed(instance_dut_sam_s[i]) - ($signed($signed(instance_dut_left_s[i]) >>> 1) + $signed($signed(instance_dut_right_s[i]) >>> 1)));
            end
            else if ((instance_dut_flgs_s[i] == 5)) begin
                res_out_x = ($signed(instance_dut_sam_s[i]) + ($signed($signed(instance_dut_left_s[i]) >>> 1) + $signed($signed(instance_dut_right_s[i]) >>> 1)));
            end
            else if ((instance_dut_flgs_s[i] == 6)) begin
                res_out_x = ($signed(instance_dut_sam_s[i]) + $signed((($signed(instance_dut_left_s[i]) + $signed(instance_dut_right_s[i])) + 2) >>> 2));
            end
            else if ((instance_dut_flgs_s[i] == 4)) begin
                res_out_x = ($signed(instance_dut_sam_s[i]) - $signed((($signed(instance_dut_left_s[i]) + $signed(instance_dut_right_s[i])) + 2) >>> 2));
            end
        end
    end
    else begin
        noupdate_s = 1;
    end
end



assign flat_rt = instance_mat_rt_flat_i;


always @(posedge clk) begin: TOP_JPEG_INSTANCE_RAM_LF_WRITE
    if (we_lf) begin
        instance_ram_lf_mem[addr_lf] <= din_lf;
    end
end



assign dout_lf = instance_ram_lf_mem[addr_lf];



assign flat_sa = instance_mat_sa_flat_i;


always @(negedge clk) begin: TOP_JPEG_INSTANCE_RAM_RES_WRITE
    if (we_res) begin
        instance_ram_res_mem[addr_res] <= din_res;
    end
end



assign dout_res = instance_ram_res_mem[addr_res];


always @(posedge clk) begin: TOP_JPEG_INSTANCE_RAM_SA_WRITE
    if (we_sa) begin
        instance_ram_sa_mem[addr_sa] <= din_sa;
    end
end



assign dout_sa = instance_ram_sa_mem[addr_sa];



assign flat_lf = instance_mat_lf_flat_i;


always @(addr_flgs) begin: TOP_JPEG_INSTANCE_ROM_FLGS_READ
    case (addr_flgs)
        0: dout_flgs = 7;
        1: dout_flgs = 224;
        2: dout_flgs = 7168;
        3: dout_flgs = 229376;
        4: dout_flgs = 7340032;
        5: dout_flgs = 234881024;
        6: dout_flgs = 34'h1c0000000;
        7: dout_flgs = 39'h3800000000;
        8: dout_flgs = 44'h70000000000;
        9: dout_flgs = 49'he00000000000;
        10: dout_flgs = 54'h1c000000000000;
        11: dout_flgs = 59'h380000000000000;
        12: dout_flgs = 64'h7000000000000000;
        13: dout_flgs = 69'he0000000000000000;
        14: dout_flgs = 74'h1c00000000000000000;
        15: dout_flgs = 79'h38000000000000000000;
        16: dout_flgs = 6;
        17: dout_flgs = 192;
        18: dout_flgs = 6144;
        19: dout_flgs = 196608;
        20: dout_flgs = 6291456;
        21: dout_flgs = 201326592;
        22: dout_flgs = 34'h180000000;
        23: dout_flgs = 39'h3000000000;
        24: dout_flgs = 44'h60000000000;
        25: dout_flgs = 49'hc00000000000;
        26: dout_flgs = 54'h18000000000000;
        27: dout_flgs = 59'h300000000000000;
        28: dout_flgs = 64'h6000000000000000;
        29: dout_flgs = 69'hc0000000000000000;
        30: dout_flgs = 74'h1800000000000000000;
        31: dout_flgs = 79'h30000000000000000000;
        32: dout_flgs = 5;
        33: dout_flgs = 160;
        34: dout_flgs = 5120;
        35: dout_flgs = 163840;
        36: dout_flgs = 5242880;
        37: dout_flgs = 167772160;
        38: dout_flgs = 34'h140000000;
        39: dout_flgs = 39'h2800000000;
        40: dout_flgs = 44'h50000000000;
        41: dout_flgs = 49'ha00000000000;
        42: dout_flgs = 54'h14000000000000;
        43: dout_flgs = 59'h280000000000000;
        44: dout_flgs = 64'h5000000000000000;
        45: dout_flgs = 69'ha0000000000000000;
        46: dout_flgs = 74'h1400000000000000000;
        47: dout_flgs = 79'h28000000000000000000;
        48: dout_flgs = 4;
        49: dout_flgs = 128;
        50: dout_flgs = 4096;
        51: dout_flgs = 131072;
        52: dout_flgs = 4194304;
        53: dout_flgs = 134217728;
        54: dout_flgs = 34'h100000000;
        55: dout_flgs = 39'h2000000000;
        56: dout_flgs = 44'h40000000000;
        57: dout_flgs = 49'h800000000000;
        58: dout_flgs = 53'h10000000000000;
        59: dout_flgs = 58'h200000000000000;
        60: dout_flgs = 64'h4000000000000000;
        61: dout_flgs = 68'h80000000000000000;
        62: dout_flgs = 73'h1000000000000000000;
        default: dout_flgs = 78'h20000000000000000000;
    endcase
end


always @(posedge clk) begin: TOP_JPEG_INSTANCE_RAM_RT_WRITE
    if (we_rt) begin
        instance_ram_rt_mem[addr_rt] <= din_rt;
    end
end



assign dout_rt = instance_ram_rt_mem[addr_rt];

endmodule
