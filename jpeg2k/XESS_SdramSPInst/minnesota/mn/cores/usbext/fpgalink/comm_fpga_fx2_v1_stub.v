// File: comm_fpga_fx2_v1_stub.v
// Generated by MyHDL 0.9dev
// Date: Sat Jul 13 22:29:39 2013


`timescale 1ns/10ps

module comm_fpga_fx2_v1_stub (
    clk_in,
    reset_in,
    fx2FifoSel_out,
    fx2Data_in,
    fx2Data_out,
    fx2Data_sel,
    fx2Read_out,
    fx2GotData_in,
    fx2Write_out,
    fx2GotRoom_in,
    fx2PktEnd_out,
    chanAddr_out,
    h2fData_out,
    h2fValid_out,
    h2fReady_in,
    f2hData_in,
    f2hValid_in,
    f2hReady_out
);
// A stub for the Verilog cosimulation
// The following does absolutely nothing except let the converter know what
// ports are inputs and which arre outputs.

input clk_in;
input reset_in;
output fx2FifoSel_out;
reg fx2FifoSel_out;
input [7:0] fx2Data_in;
output [7:0] fx2Data_out;
reg [7:0] fx2Data_out;
output fx2Data_sel;
reg fx2Data_sel;
output fx2Read_out;
reg fx2Read_out;
input fx2GotData_in;
output fx2Write_out;
reg fx2Write_out;
input fx2GotRoom_in;
output fx2PktEnd_out;
reg fx2PktEnd_out;
output [6:0] chanAddr_out;
reg [6:0] chanAddr_out;
output [7:0] h2fData_out;
reg [7:0] h2fData_out;
output h2fValid_out;
reg h2fValid_out;
input h2fReady_in;
input [7:0] f2hData_in;
input f2hValid_in;
output f2hReady_out;
reg f2hReady_out;






always @(posedge clk_in, negedge reset_in) begin: COMM_FPGA_FX2_V1_STUB_HDL
    if ((fx2GotData_in || fx2GotRoom_in || h2fReady_in || f2hValid_in || (fx2Data_in == 0) || (f2hData_in == 0))) begin
        fx2Data_out <= 2;
        fx2Data_sel <= 1'b0;
        fx2FifoSel_out <= 1'b1;
        fx2Read_out <= 1'b1;
        fx2Write_out <= 1'b1;
        fx2PktEnd_out <= 1'b1;
        chanAddr_out <= 1'b1;
        h2fData_out <= 3;
        h2fValid_out <= 1'b1;
        f2hReady_out <= 1'b1;
    end
end

endmodule
