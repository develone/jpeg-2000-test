// File: m_flat_top.v
// Generated by MyHDL 0.9.dev0
// Date: Tue Apr 21 15:39:46 2015


`timescale 1ns/10ps

module m_flat_top (
    clock,
    reset,
    sdo
);
// example convertible top-level 

input clock;
input reset;
output sdo;
reg sdo;

reg [143:0] flati;
wire [143:0] flato;
wire [8:0] gflt_col;
wire [143:0] gflt_flats;
wire [8:0] gstk_g_14_y;
wire [8:0] gstk_g_13_y;
wire [8:0] gstk_g_12_y;
wire [8:0] gstk_g_11_y;
wire [8:0] gstk_g_10_y;
wire [8:0] gstk_g_9_y;
wire [8:0] gstk_g_8_y;
wire [8:0] gstk_g_7_y;
wire [8:0] gstk_g_6_y;
wire [8:0] gstk_g_5_y;
wire [8:0] gstk_g_4_y;
wire [8:0] gstk_g_3_y;
wire [8:0] gstk_g_2_y;
wire [8:0] gstk_g_1_y;
wire [8:0] gstk_g_0_y;



assign gflt_flats[144-1:135] = gstk_g_0_y[9-1:0];
assign gflt_flats[135-1:126] = gstk_g_1_y[9-1:0];
assign gflt_flats[126-1:117] = gstk_g_2_y[9-1:0];
assign gflt_flats[117-1:108] = gstk_g_3_y[9-1:0];
assign gflt_flats[108-1:99] = gstk_g_4_y[9-1:0];
assign gflt_flats[99-1:90] = gstk_g_5_y[9-1:0];
assign gflt_flats[90-1:81] = gstk_g_6_y[9-1:0];
assign gflt_flats[81-1:72] = gstk_g_7_y[9-1:0];
assign gflt_flats[72-1:63] = gstk_g_8_y[9-1:0];
assign gflt_flats[63-1:54] = gstk_g_9_y[9-1:0];
assign gflt_flats[54-1:45] = gstk_g_10_y[9-1:0];
assign gflt_flats[45-1:36] = gstk_g_11_y[9-1:0];
assign gflt_flats[36-1:27] = gstk_g_12_y[9-1:0];
assign gflt_flats[27-1:18] = gstk_g_13_y[9-1:0];
assign gflt_flats[18-1:9] = gstk_g_14_y[9-1:0];
assign gflt_flats[9-1:0] = gflt_col[9-1:0];


always @(posedge clock) begin: M_FLAT_TOP_RTLI
    if (reset == 1) begin
        flati <= 0;
    end
    else begin
        flati <= {flati[(144 - 1)-1:0]};
    end
end



assign gstk_g_0_y = flati[9-1:0];



assign gstk_g_1_y = flati[18-1:9];



assign gstk_g_2_y = flati[27-1:18];



assign gstk_g_3_y = flati[36-1:27];



assign gstk_g_4_y = flati[45-1:36];



assign gstk_g_5_y = flati[54-1:45];



assign gstk_g_6_y = flati[63-1:54];



assign gstk_g_7_y = flati[72-1:63];



assign gstk_g_8_y = flati[81-1:72];



assign gstk_g_9_y = flati[90-1:81];



assign gstk_g_10_y = flati[99-1:90];



assign gstk_g_11_y = flati[108-1:99];



assign gstk_g_12_y = flati[117-1:108];



assign gstk_g_13_y = flati[126-1:117];



assign gstk_g_14_y = flati[135-1:126];



assign gflt_col = flati[144-1:135];



assign flato = gflt_flats;


always @(posedge clock) begin: M_FLAT_TOP_RTLO
    if (reset == 1) begin
        sdo <= 0;
    end
    else begin
        sdo <= {flato[(144 - 1)-1:0], (0 != 0)};
    end
end

endmodule
