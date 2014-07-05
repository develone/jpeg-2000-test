// File: m_ex1.v
// Generated by MyHDL 0.9dev
// Date: Sat Jul  5 06:25:15 2014


`timescale 1ns/10ps

module m_ex1 (
    clk,
    p,
    even_odd,
    fwd_inv,
    pix_x2_3,
    pix_x2_2,
    pix_x2_1,
    pix_x4_1,
    pix_x4_3,
    pix_x4_2,
    pix_x3_2,
    pix_d3,
    pix_x3_1,
    pix_d3_3,
    pix_x5_1,
    pix_x5_2,
    pix_x5_3,
    pix_a2_3,
    pix_x3_3,
    pix_a2,
    pix_x2,
    pix_x3,
    pix_x4,
    pix_x5,
    pix_d3_2,
    pix_a2_1,
    pix_a2_2,
    pix_d3_1
);


input clk;
input p;
input even_odd;
input fwd_inv;
input signed [25:0] pix_x2_3;
input signed [25:0] pix_x2_2;
input signed [25:0] pix_x2_1;
input signed [25:0] pix_x4_1;
input signed [25:0] pix_x4_3;
input signed [25:0] pix_x4_2;
input signed [25:0] pix_x3_2;
output signed [25:0] pix_d3;
reg signed [25:0] pix_d3;
input signed [25:0] pix_x3_1;
output signed [25:0] pix_d3_3;
reg signed [25:0] pix_d3_3;
input signed [25:0] pix_x5_1;
input signed [25:0] pix_x5_2;
input signed [25:0] pix_x5_3;
output signed [25:0] pix_a2_3;
reg signed [25:0] pix_a2_3;
input signed [25:0] pix_x3_3;
output signed [25:0] pix_a2;
reg signed [25:0] pix_a2;
input signed [25:0] pix_x2;
input signed [25:0] pix_x3;
input signed [25:0] pix_x4;
input signed [25:0] pix_x5;
output signed [25:0] pix_d3_2;
reg signed [25:0] pix_d3_2;
output signed [25:0] pix_a2_1;
reg signed [25:0] pix_a2_1;
output signed [25:0] pix_a2_2;
reg signed [25:0] pix_a2_2;
output signed [25:0] pix_d3_1;
reg signed [25:0] pix_d3_1;






always @(posedge clk) begin: M_EX1_HDL
    reg signed [26-1:0] ca3;
    reg signed [26-1:0] ca2;
    reg signed [26-1:0] ca1;
    reg signed [26-1:0] ca4;
    reg signed [26-1:0] ra4;
    reg signed [26-1:0] ra2;
    reg signed [26-1:0] ra3;
    reg signed [26-1:0] ra1;
    if ((!p)) begin
        if (even_odd) begin
            if (fwd_inv) begin
                // p false 1st pass even_odd True fwd_inv True (x2+x3) * ca1 
                pix_d3 <= ((pix_x2 + pix_x3) * ca1);
                pix_d3_1 <= ((pix_x2_1 + pix_x3_1) * ca1);
                pix_d3_2 <= ((pix_x2_2 + pix_x3_2) * ca1);
                pix_d3_3 <= ((pix_x2_2 + pix_x3_2) * ca1);
            end
            else begin
                // p false 1st pass even_odd True fwd_inv False (x4+x5) * ra4 
                pix_a2 <= ((pix_x4 + pix_x5) * ra4);
                pix_a2_1 <= ((pix_x4_1 + pix_x5_1) * ra4);
                pix_a2_2 <= ((pix_x4_2 + pix_x5_2) * ra4);
                pix_a2_3 <= ((pix_x4_3 + pix_x5_3) * ra4);
            end
        end
        else begin
            if (fwd_inv) begin
                // p false 1st pass even_odd false fwd_inv True (x4+x5) * ca2 
                pix_a2 <= ((pix_x4 + pix_x5) * ca2);
                pix_a2_1 <= ((pix_x4_1 + pix_x5_1) * ca2);
                pix_a2_2 <= ((pix_x4_2 + pix_x5_2) * ca2);
                pix_a2_3 <= ((pix_x4_3 + pix_x5_3) * ca2);
            end
            else begin
                // p false 1st pass even_odd false fwd_inv False (x2+x3) * ra3 
                pix_d3 <= ((pix_x2 + pix_x3) * ra3);
                pix_d3_1 <= ((pix_x2_1 + pix_x3_1) * ra3);
                pix_d3_2 <= ((pix_x2_2 + pix_x3_2) * ra3);
                pix_d3_3 <= ((pix_x2_2 + pix_x3_3) * ra3);
            end
        end
    end
    else begin
        if (even_odd) begin
            if (fwd_inv) begin
                // p True 2nd pass even_odd True fwd_inv True (x2+x3) * ca3 
                pix_d3 <= ((pix_x2 + pix_x3) * ca3);
                pix_d3_1 <= ((pix_x2_1 + pix_x3_1) * ca3);
                pix_d3_2 <= ((pix_x2_2 + pix_x3_2) * ca3);
                pix_d3_3 <= ((pix_x2_3 + pix_x3_3) * ca3);
            end
            else begin
                // p True 2nd pass even_odd True fwd_inv False (x4+x5) * ra2 
                pix_a2 <= ((pix_x4 + pix_x5) * ra2);
                pix_a2_1 <= ((pix_x4_1 + pix_x5_1) * ra2);
                pix_a2_2 <= ((pix_x4_2 + pix_x5_2) * ra2);
                pix_a2_3 <= ((pix_x4_3 + pix_x5_3) * ra2);
            end
        end
        else begin
            if (fwd_inv) begin
                // p True 2nd pass even_odd False fwd_inv True (x2+x3) * ca4 
                pix_a2 <= ((pix_x4 + pix_x5) * ca4);
                pix_a2_1 <= ((pix_x4_1 + pix_x5_1) * ca4);
                pix_a2_2 <= ((pix_x4_2 + pix_x5_2) * ca4);
                pix_a2_3 <= ((pix_x4_3 + pix_x5_3) * ca4);
            end
            else begin
                // p True 2nd pass even_odd False fwd_inv False (x2+x3) * ra1 
                pix_d3 <= ((pix_x2 + pix_x3) * ra1);
                pix_d3_1 <= ((pix_x2_1 + pix_x3_1) * ra1);
                pix_d3_2 <= ((pix_x2_2 + pix_x3_2) * ra1);
                pix_d3_3 <= ((pix_x2_3 + pix_x3_3) * ra1);
            end
        end
    end
end

endmodule
