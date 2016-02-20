`timescale 1ns/10ps

module xula2 (
    clock,
    led,
    uart_tx,
	 uart_rx_1,
    uart_rx
);
// The LEDs are controlled from the RPi over the UART
// to the FPGA.

input clock;
output [3:0] led;
reg [3:0] led;
output uart_tx;
wire uart_tx;
input uart_rx;
output uart_rx_1;
reg uart_rx_1;
wire [8:0] lft2;
wire [8:0] lft3;
wire [8:0] lft0;
wire [8:0] lft1;
wire [8:0] lft6;
wire [8:0] lft7;
wire [8:0] lft4;
wire [8:0] lft5;
reg [31:0] myregister0;
reg [31:0] myregister1;
reg [31:0] myregister2;
reg [31:0] myregister3;
reg [31:0] myregister4;
reg [31:0] myregister5;
reg [31:0] myregister6;
reg [31:0] myregister7;
reg [27:0] memmap_mem_addr;
wire signed [9:0] res2;
wire signed [9:0] res3;
wire signed [9:0] res0;
wire signed [9:0] res1;
wire signed [9:0] res6;
wire signed [9:0] res7;
wire signed [9:0] res4;
wire signed [9:0] res5;
wire [2:0] flgs1;
reg [31:0] memmap_read_data;
wire [2:0] flgs3;
wire [2:0] flgs2;
wire [2:0] flgs5;
wire [2:0] flgs4;
wire [2:0] flgs7;
wire [2:0] flgs6;
reg glbl_tick_sec;
wire [2:0] flgs0;
wire [8:0] z4;
wire [8:0] z5;
wire [8:0] z6;
wire [8:0] z7;
wire [8:0] rht2;
wire [8:0] rht3;
wire [8:0] z2;
wire [8:0] rht1;
wire [31:0] data_to_host2;
wire [31:0] data_to_host3;
wire [31:0] data_to_host0;
wire [31:0] data_to_host1;
reg done5;
reg done4;
reg done7;
reg done6;
reg [7:0] tone;
reg done0;
reg done3;
reg done2;
wire [8:0] rht6;
wire [8:0] rht7;
wire [8:0] rht4;
wire [8:0] rht5;
wire [8:0] z0;
wire [8:0] z1;
wire [8:0] rht0;
wire [8:0] z3;
reg upd7;
reg upd6;
reg upd5;
reg upd4;
reg upd3;
reg upd2;
reg upd1;
reg upd0;
reg done1;
reg memmap_read;
reg [31:0] memmap_write_data;
reg memmap_write;
reg memmap_done;
reg [7:0] ledreg;
reg signed [9:0] lift0;
reg signed [9:0] lift1;
reg signed [9:0] lift2;
reg signed [9:0] lift3;
reg signed [9:0] lift4;
reg signed [9:0] lift5;
reg signed [9:0] lift6;
reg signed [9:0] lift7;
wire [8:0] sam3;
wire [8:0] sam2;
wire [8:0] sam1;
wire [8:0] sam0;
wire [8:0] sam7;
wire [8:0] sam6;
wire [8:0] sam5;
wire [8:0] sam4;
reg cmd_inst_ready;
reg cmd_inst_fbtx_full;
reg [3:0] cmd_inst_state;
reg cmd_inst_fbrx_rd;
reg [7:0] cmd_inst_bytemon;
wire cmd_inst_fbrx_rvld;
reg cmd_inst_fbtx_wr;
wire [31:0] cmd_inst_address;
wire [31:0] cmd_inst_data;
reg [3:0] cmd_inst_bb_per_addr;
reg cmd_inst_fbrx_empty;
wire cmd_inst_reset;
reg [7:0] cmd_inst_fbtx_wdata;
reg cmd_inst_error;
wire [7:0] cmd_inst_fbrx_rdata;
reg [5:0] cmd_inst_mmc_inst_tocnt;
reg [2:0] cmd_inst_mmc_inst_state;
reg uart_inst_baudce16;
reg uart_inst_tx;
wire uart_inst_rx;
reg uart_inst_baudce;
reg [7:0] uart_inst_instrx_fbusrx_wdata;
reg uart_inst_instrx_midbit;
reg [7:0] uart_inst_instrx_rxbyte;
reg uart_inst_instrx_fbusrx_wr;
reg uart_inst_instrx_rxd;
reg [3:0] uart_inst_instrx_bitcnt;
reg [1:0] uart_inst_instrx_state;
reg [3:0] uart_inst_instrx_mcnt;
reg uart_inst_instrx_rxinprog;
reg [7:0] uart_inst_insttx_txbyte;
reg uart_inst_insttx_fbustx_empty;
reg uart_inst_insttx_fbustx_rd;
reg [3:0] uart_inst_insttx_bitcnt;
reg [2:0] uart_inst_insttx_state;
wire [7:0] uart_inst_insttx_fbustx_rdata;
reg [10:0] uart_inst_instbaud_cnt;
reg [3:0] uart_inst_instbaud_cnt16;
reg [2:0] uart_inst_instrxfifo_nvacant;
reg [1:0] uart_inst_instrxfifo_addr;
reg uart_inst_instrxfifo_fbus_full;
wire uart_inst_instrxfifo_fbus_clear;
wire [2:0] uart_inst_instrxfifo_fbus_count;
reg [2:0] uart_inst_instrxfifo_ntenant;
reg [2:0] uart_inst_insttxfifo_nvacant;
reg [1:0] uart_inst_insttxfifo_addr;
wire uart_inst_insttxfifo_fbus_clear;
wire uart_inst_insttxfifo_fbus_rvld;
wire [2:0] uart_inst_insttxfifo_fbus_count;
reg [2:0] uart_inst_insttxfifo_ntenant;
reg [13:0] tick_inst_mscnt;
reg [9:0] tick_inst_seccnt;
reg tick_inst_g2_increment;

reg [7:0] cmd_inst_packet [0:12-1];
reg [7:0] uart_inst_instrxfifo_mem [0:4-1];
reg [7:0] uart_inst_insttxfifo_mem [0:4-1];
reg uart_inst_instsynctx_staps [0:2-1];
reg uart_inst_instsyncrx_staps [0:2-1];

assign cmd_inst_reset = 1'd0;
assign uart_inst_instrxfifo_fbus_clear = 1'd0;
assign uart_inst_insttxfifo_fbus_clear = 1'd0;

assign cmd_inst_address[32-1:24] = cmd_inst_packet[2];
assign cmd_inst_address[24-1:16] = cmd_inst_packet[3];
assign cmd_inst_address[16-1:8] = cmd_inst_packet[4];
assign cmd_inst_address[8-1:0] = cmd_inst_packet[5];
assign cmd_inst_data[32-1:24] = cmd_inst_packet[8];
assign cmd_inst_data[24-1:16] = cmd_inst_packet[9];
assign cmd_inst_data[16-1:8] = cmd_inst_packet[10];
assign cmd_inst_data[8-1:0] = cmd_inst_packet[11];


always @(cmd_inst_ready, cmd_inst_fbrx_empty) begin: XULA2_CMD_INST_BEH_FIFO_READ
    if ((cmd_inst_ready && (!cmd_inst_fbrx_empty))) begin
        cmd_inst_fbrx_rd = 1'b1;
    end
    else begin
        cmd_inst_fbrx_rd = 1'b0;
    end
end


always @(posedge clock) begin: XULA2_CMD_INST_MMC_INST_BEH_SM
    if (cmd_inst_reset == 1) begin
        cmd_inst_mmc_inst_tocnt <= 0;
        cmd_inst_mmc_inst_state <= 3'b000;
    end
    else begin
        case (cmd_inst_mmc_inst_state)
            3'b000: begin
                if ((!memmap_done)) begin
                    cmd_inst_mmc_inst_state <= 3'b001;
                end
                else if (memmap_write) begin
                    cmd_inst_mmc_inst_state <= 3'b010;
                end
                else if (memmap_read) begin
                    cmd_inst_mmc_inst_state <= 3'b100;
                end
            end
            3'b001: begin
                if (memmap_done) begin
                    cmd_inst_mmc_inst_tocnt <= 0;
                    if (memmap_write) begin
                        cmd_inst_mmc_inst_state <= 3'b110;
                    end
                    else if (memmap_read) begin
                        cmd_inst_mmc_inst_state <= 3'b101;
                    end
                end
            end
            3'b010: begin
                cmd_inst_mmc_inst_state <= 3'b110;
                cmd_inst_mmc_inst_tocnt <= 0;
            end
            3'b100: begin
                cmd_inst_mmc_inst_state <= 3'b101;
            end
            3'b101: begin
                if (memmap_done) begin
                    cmd_inst_mmc_inst_state <= 3'b110;
                end
            end
            3'b110: begin
                if ((!(memmap_write || memmap_read))) begin
                    cmd_inst_mmc_inst_state <= 3'b000;
                end
            end
            default: begin
                if (1'b0 !== 1) begin
                    $display("*** AssertionError ***");
                end
            end
        endcase
    end
end


always @(posedge clock) begin: XULA2_CMD_INST_BEH_STATE_MACHINE
    integer ii;
    reg [8-1:0] bytecnt;
    integer val;
    integer idx;
    if (cmd_inst_reset == 1) begin
        memmap_read <= 0;
        memmap_write <= 0;
        cmd_inst_bytemon <= 0;
        memmap_mem_addr <= 0;
        memmap_write_data <= 0;
        cmd_inst_packet[0] <= 0;
        cmd_inst_packet[1] <= 0;
        cmd_inst_packet[2] <= 0;
        cmd_inst_packet[3] <= 0;
        cmd_inst_packet[4] <= 0;
        cmd_inst_packet[5] <= 0;
        cmd_inst_packet[6] <= 0;
        cmd_inst_packet[7] <= 0;
        cmd_inst_packet[8] <= 0;
        cmd_inst_packet[9] <= 0;
        cmd_inst_packet[10] <= 0;
        cmd_inst_packet[11] <= 0;
        cmd_inst_fbtx_wr <= 0;
        cmd_inst_state <= 4'b0000;
        cmd_inst_error <= 0;
        cmd_inst_ready <= 0;
        cmd_inst_fbtx_wdata <= 0;
        cmd_inst_bb_per_addr <= 0;
        bytecnt = 0;
    end
    else begin
        case (cmd_inst_state)
            4'b0000: begin
                cmd_inst_state <= 4'b0001;
                cmd_inst_ready <= 1'b1;
                bytecnt = 0;
            end
            4'b0001: begin
                if (cmd_inst_fbrx_rvld) begin
                    for (ii=0; ii<2; ii=ii+1) begin
                        case (ii)
                            0: idx = 0;
                            default: idx = 7;
                        endcase
                        case (ii)
                            0: val = 222;
                            default: val = 202;
                        endcase
                        if (($signed({1'b0, bytecnt}) == idx)) begin
                            if (($signed({1'b0, cmd_inst_fbrx_rdata}) != val)) begin
                                cmd_inst_error <= 1'b1;
                                cmd_inst_state <= 4'b1001;
                            end
                        end
                    end
                    cmd_inst_packet[bytecnt] <= cmd_inst_fbrx_rdata;
                    bytecnt = (bytecnt + 1);
                end
                if ((bytecnt == 12)) begin
                    cmd_inst_ready <= 1'b0;
                    cmd_inst_state <= 4'b0010;
                end
            end
            4'b0010: begin
                cmd_inst_bb_per_addr <= cmd_inst_address[32-1:28];
                memmap_mem_addr <= cmd_inst_address[28-1:0];
                if (memmap_done !== 1) begin
                    $display("*** AssertionError ***");
                end
                bytecnt = 0;
                case (cmd_inst_packet[1])
                    'h1: begin
                        cmd_inst_state <= 4'b0101;
                    end
                    'h2: begin
                        memmap_write_data <= cmd_inst_data;
                        cmd_inst_state <= 4'b0011;
                    end
                    default: begin
                        cmd_inst_error <= 1'b1;
                        cmd_inst_state <= 4'b1001;
                    end
                endcase
            end
            4'b0011: begin
                if (memmap_done) begin
                    memmap_write <= 1'b1;
                    cmd_inst_state <= 4'b0100;
                end
            end
            4'b0100: begin
                memmap_write <= 1'b0;
                if (memmap_done) begin
                    cmd_inst_state <= 4'b0101;
                end
            end
            4'b0101: begin
                if (memmap_done) begin
                    memmap_read <= 1'b1;
                    cmd_inst_state <= 4'b0110;
                end
            end
            4'b0110: begin
                memmap_read <= 1'b0;
                if (memmap_done) begin
                    cmd_inst_packet[(8 + 0)] <= memmap_read_data[32-1:24];
                    cmd_inst_packet[(8 + 1)] <= memmap_read_data[24-1:16];
                    cmd_inst_packet[(8 + 2)] <= memmap_read_data[16-1:8];
                    cmd_inst_packet[(8 + 3)] <= memmap_read_data[8-1:0];
                    cmd_inst_state <= 4'b0111;
                end
            end
            4'b0111: begin
                cmd_inst_fbtx_wr <= 1'b0;
                if ((bytecnt < 12)) begin
                    if ((!cmd_inst_fbtx_full)) begin
                        cmd_inst_fbtx_wr <= 1'b1;
                        cmd_inst_fbtx_wdata <= cmd_inst_packet[bytecnt];
                        bytecnt = (bytecnt + 1);
                    end
                    cmd_inst_state <= 4'b1000;
                end
                else begin
                    cmd_inst_state <= 4'b1010;
                end
            end
            4'b1000: begin
                cmd_inst_fbtx_wr <= 1'b0;
                cmd_inst_state <= 4'b0111;
            end
            4'b1001: begin
                if ((!cmd_inst_fbrx_rvld)) begin
                    cmd_inst_state <= 4'b1010;
                    cmd_inst_ready <= 1'b0;
                end
            end
            4'b1010: begin
                cmd_inst_error <= 1'b0;
                cmd_inst_ready <= 1'b0;
                cmd_inst_state <= 4'b0000;
            end
            default: begin
                if (1'b0 !== 1) begin
                    $display("*** AssertionError ***");
                end
            end
        endcase
        cmd_inst_bytemon <= bytecnt;
    end
end



assign z2 = res2;



assign z3 = res3;


always @(posedge clock) begin: XULA2_JPEG4_RTL
    if ((upd4 == 1)) begin
        done4 <= 0;
        case (flgs4)
            'h7: begin
                lift4 <= ($signed(sam4) - ($signed($signed(lft4) >>> 1) + $signed($signed(rht4) >>> 1)));
            end
            'h5: begin
                lift4 <= ($signed(sam4) + ($signed($signed(lft4) >>> 1) + $signed($signed(rht4) >>> 1)));
            end
            'h6: begin
                lift4 <= ($signed(sam4) + $signed((($signed(lft4) + $signed(rht4)) + 2) >>> 2));
            end
            'h4: begin
                lift4 <= ($signed(sam4) - $signed((($signed(lft4) + $signed(rht4)) + 2) >>> 2));
            end
        endcase
    end
    else begin
        done4 <= 1;
    end
end


always @(posedge clock) begin: XULA2_BEH_MY_REGISTERS
    if (memmap_write) begin
        case (memmap_mem_addr)
            'h0: begin
                myregister0 <= memmap_write_data;
            end
            'h4: begin
                myregister1 <= memmap_write_data;
            end
            default: begin
                case (memmap_mem_addr)
                    'h8: begin
                        myregister2 <= memmap_write_data;
                    end
                    'hc: begin
                        myregister3 <= memmap_write_data;
                    end
                endcase
            end
        endcase
        case (memmap_mem_addr)
            'h10: begin
                myregister4 <= memmap_write_data;
            end
            'h14: begin
                myregister5 <= memmap_write_data;
            end
            default: begin
                case (memmap_mem_addr)
                    'h18: begin
                        myregister6 <= memmap_write_data;
                    end
                    'h1c: begin
                        myregister7 <= memmap_write_data;
                    end
                    'h20: begin
                        upd0 <= 1;
                        upd1 <= 1;
                        upd2 <= 1;
                        upd3 <= 1;
                        upd4 <= 1;
                        upd5 <= 1;
                        upd6 <= 1;
                        upd7 <= 1;
                    end
                    'h24: begin
                        upd0 <= 0;
                        upd1 <= 0;
                        upd2 <= 0;
                        upd3 <= 0;
                        upd4 <= 0;
                        upd5 <= 0;
                        upd6 <= 0;
                        upd7 <= 0;
                    end
                endcase
            end
        endcase
    end
end



assign data_to_host0 = ((z1 << 16) | z0);
assign data_to_host1 = ((z3 << 16) | z2);
assign data_to_host2 = ((z5 << 16) | z4);
assign data_to_host3 = ((z7 << 16) | z6);


always @(posedge clock) begin: XULA2_BEH_LED_CONTROL
    memmap_done <= (!(memmap_write || memmap_read));
    if ((memmap_write && (memmap_mem_addr == 64))) begin
        ledreg <= memmap_write_data;
    end
end



assign flgs3 = myregister3[30-1:27];
assign rht3 = myregister3[27-1:18];
assign sam3 = myregister3[18-1:9];
assign lft3 = myregister3[9-1:0];



assign flgs2 = myregister2[30-1:27];
assign rht2 = myregister2[27-1:18];
assign sam2 = myregister2[18-1:9];
assign lft2 = myregister2[9-1:0];



assign flgs1 = myregister1[30-1:27];
assign rht1 = myregister1[27-1:18];
assign sam1 = myregister1[18-1:9];
assign lft1 = myregister1[9-1:0];



assign flgs0 = myregister0[30-1:27];
assign rht0 = myregister0[27-1:18];
assign sam0 = myregister0[18-1:9];
assign lft0 = myregister0[9-1:0];



assign flgs7 = myregister7[30-1:27];
assign rht7 = myregister7[27-1:18];
assign sam7 = myregister7[18-1:9];
assign lft7 = myregister7[9-1:0];



assign flgs6 = myregister6[30-1:27];
assign rht6 = myregister6[27-1:18];
assign sam6 = myregister6[18-1:9];
assign lft6 = myregister6[9-1:0];



assign flgs5 = myregister5[30-1:27];
assign rht5 = myregister5[27-1:18];
assign sam5 = myregister5[18-1:9];
assign lft5 = myregister5[9-1:0];


always @(posedge clock) begin: XULA2_JPEG3_RTL
    if ((upd3 == 1)) begin
        done3 <= 0;
        case (flgs3)
            'h7: begin
                lift3 <= ($signed(sam3) - ($signed($signed(lft3) >>> 1) + $signed($signed(rht3) >>> 1)));
            end
            'h5: begin
                lift3 <= ($signed(sam3) + ($signed($signed(lft3) >>> 1) + $signed($signed(rht3) >>> 1)));
            end
            'h6: begin
                lift3 <= ($signed(sam3) + $signed((($signed(lft3) + $signed(rht3)) + 2) >>> 2));
            end
            'h4: begin
                lift3 <= ($signed(sam3) - $signed((($signed(lft3) + $signed(rht3)) + 2) >>> 2));
            end
        endcase
    end
    else begin
        done3 <= 1;
    end
end


always @(posedge clock) begin: XULA2_JPEG2_RTL
    if ((upd2 == 1)) begin
        done2 <= 0;
        case (flgs2)
            'h7: begin
                lift2 <= ($signed(sam2) - ($signed($signed(lft2) >>> 1) + $signed($signed(rht2) >>> 1)));
            end
            'h5: begin
                lift2 <= ($signed(sam2) + ($signed($signed(lft2) >>> 1) + $signed($signed(rht2) >>> 1)));
            end
            'h6: begin
                lift2 <= ($signed(sam2) + $signed((($signed(lft2) + $signed(rht2)) + 2) >>> 2));
            end
            'h4: begin
                lift2 <= ($signed(sam2) - $signed((($signed(lft2) + $signed(rht2)) + 2) >>> 2));
            end
        endcase
    end
    else begin
        done2 <= 1;
    end
end


always @(posedge clock) begin: XULA2_JPEG1_RTL
    if ((upd1 == 1)) begin
        done1 <= 0;
        case (flgs1)
            'h7: begin
                lift1 <= ($signed(sam1) - ($signed($signed(lft1) >>> 1) + $signed($signed(rht1) >>> 1)));
            end
            'h5: begin
                lift1 <= ($signed(sam1) + ($signed($signed(lft1) >>> 1) + $signed($signed(rht1) >>> 1)));
            end
            'h6: begin
                lift1 <= ($signed(sam1) + $signed((($signed(lft1) + $signed(rht1)) + 2) >>> 2));
            end
            'h4: begin
                lift1 <= ($signed(sam1) - $signed((($signed(lft1) + $signed(rht1)) + 2) >>> 2));
            end
        endcase
    end
    else begin
        done1 <= 1;
    end
end


always @(posedge clock) begin: XULA2_JPEG0_RTL
    if ((upd0 == 1)) begin
        done0 <= 0;
        case (flgs0)
            'h7: begin
                lift0 <= ($signed(sam0) - ($signed($signed(lft0) >>> 1) + $signed($signed(rht0) >>> 1)));
            end
            'h5: begin
                lift0 <= ($signed(sam0) + ($signed($signed(lft0) >>> 1) + $signed($signed(rht0) >>> 1)));
            end
            'h6: begin
                lift0 <= ($signed(sam0) + $signed((($signed(lft0) + $signed(rht0)) + 2) >>> 2));
            end
            'h4: begin
                lift0 <= ($signed(sam0) - $signed((($signed(lft0) + $signed(rht0)) + 2) >>> 2));
            end
        endcase
    end
    else begin
        done0 <= 1;
    end
end


always @(posedge clock) begin: XULA2_JPEG7_RTL
    if ((upd7 == 1)) begin
        done7 <= 0;
        case (flgs7)
            'h7: begin
                lift7 <= ($signed(sam7) - ($signed($signed(lft7) >>> 1) + $signed($signed(rht7) >>> 1)));
            end
            'h5: begin
                lift7 <= ($signed(sam7) + ($signed($signed(lft7) >>> 1) + $signed($signed(rht7) >>> 1)));
            end
            'h6: begin
                lift7 <= ($signed(sam7) + $signed((($signed(lft7) + $signed(rht7)) + 2) >>> 2));
            end
            'h4: begin
                lift7 <= ($signed(sam7) - $signed((($signed(lft7) + $signed(rht7)) + 2) >>> 2));
            end
        endcase
    end
    else begin
        done7 <= 1;
    end
end


always @(posedge clock) begin: XULA2_JPEG6_RTL
    if ((upd6 == 1)) begin
        done6 <= 0;
        case (flgs6)
            'h7: begin
                lift6 <= ($signed(sam6) - ($signed($signed(lft6) >>> 1) + $signed($signed(rht6) >>> 1)));
            end
            'h5: begin
                lift6 <= ($signed(sam6) + ($signed($signed(lft6) >>> 1) + $signed($signed(rht6) >>> 1)));
            end
            'h6: begin
                lift6 <= ($signed(sam6) + $signed((($signed(lft6) + $signed(rht6)) + 2) >>> 2));
            end
            'h4: begin
                lift6 <= ($signed(sam6) - $signed((($signed(lft6) + $signed(rht6)) + 2) >>> 2));
            end
        endcase
    end
    else begin
        done6 <= 1;
    end
end


always @(posedge clock) begin: XULA2_JPEG5_RTL
    if ((upd5 == 1)) begin
        done5 <= 0;
        case (flgs5)
            'h7: begin
                lift5 <= ($signed(sam5) - ($signed($signed(lft5) >>> 1) + $signed($signed(rht5) >>> 1)));
            end
            'h5: begin
                lift5 <= ($signed(sam5) + ($signed($signed(lft5) >>> 1) + $signed($signed(rht5) >>> 1)));
            end
            'h6: begin
                lift5 <= ($signed(sam5) + $signed((($signed(lft5) + $signed(rht5)) + 2) >>> 2));
            end
            'h4: begin
                lift5 <= ($signed(sam5) - $signed((($signed(lft5) + $signed(rht5)) + 2) >>> 2));
            end
        endcase
    end
    else begin
        done5 <= 1;
    end
end


always @(posedge clock) begin: XULA2_BEH_MY_RET_REG
    if (memmap_read) begin
        if ((memmap_mem_addr == 36)) begin
            memmap_read_data <= data_to_host0;
        end
        if ((memmap_mem_addr == 40)) begin
            memmap_read_data <= data_to_host1;
        end
        if ((memmap_mem_addr == 44)) begin
            memmap_read_data <= data_to_host2;
        end
        if ((memmap_mem_addr == 48)) begin
            memmap_read_data <= data_to_host3;
        end
    end
end


always @(posedge clock) begin: XULA2_TICK_INST_G1_RTL_COUNT
    if (cmd_inst_reset == 1) begin
        tick_inst_mscnt <= 0;
    end
    else begin
        if (1'b1) begin
            if (($signed({1'b0, tick_inst_mscnt}) == (12000 - 1))) begin
                tick_inst_mscnt <= 0;
            end
            else begin
                tick_inst_mscnt <= (tick_inst_mscnt + 1);
            end
        end
    end
end


always @(posedge clock) begin: XULA2_TICK_INST_G1_RTL_OVERFLOW
    if ((1'b1 && ($signed({1'b0, tick_inst_mscnt}) == (12000 - 2)))) begin
        tick_inst_g2_increment <= 1'b1;
    end
    else begin
        tick_inst_g2_increment <= 1'b0;
    end
end


always @(posedge clock) begin: XULA2_TICK_INST_G2_RTL_COUNT
    if (cmd_inst_reset == 1) begin
        tick_inst_seccnt <= 0;
    end
    else begin
        if (tick_inst_g2_increment) begin
            if (($signed({1'b0, tick_inst_seccnt}) == (1000 - 1))) begin
                tick_inst_seccnt <= 0;
            end
            else begin
                tick_inst_seccnt <= (tick_inst_seccnt + 1);
            end
        end
    end
end


always @(posedge clock) begin: XULA2_TICK_INST_G2_RTL_OVERFLOW
    if ((tick_inst_g2_increment && ($signed({1'b0, tick_inst_seccnt}) == (1000 - 2)))) begin
        glbl_tick_sec <= 1'b1;
    end
    else begin
        glbl_tick_sec <= 1'b0;
    end
end


always @(posedge clock) begin: XULA2_UART_INST_INSTTXFIFO_RTL_SRL_IN
    integer ii;
    if (cmd_inst_fbtx_wr) begin
        uart_inst_insttxfifo_mem[0] <= cmd_inst_fbtx_wdata;
        for (ii=1; ii<4; ii=ii+1) begin
            uart_inst_insttxfifo_mem[ii] <= uart_inst_insttxfifo_mem[(ii - 1)];
        end
    end
end



assign uart_inst_insttx_fbustx_rdata = uart_inst_insttxfifo_mem[uart_inst_insttxfifo_addr];



assign uart_inst_insttxfifo_fbus_rvld = uart_inst_insttx_fbustx_rd;


always @(posedge clock) begin: XULA2_UART_INST_INSTTXFIFO_GENS_3
    if (cmd_inst_reset == 1) begin
        cmd_inst_fbtx_full <= 0;
        uart_inst_insttx_fbustx_empty <= 1;
        uart_inst_insttxfifo_addr <= 0;
    end
    else begin
        if (uart_inst_insttxfifo_fbus_clear) begin
            uart_inst_insttxfifo_addr <= 0;
            uart_inst_insttx_fbustx_empty <= 1'b1;
            cmd_inst_fbtx_full <= 1'b0;
        end
        else if ((uart_inst_insttx_fbustx_rd && (!cmd_inst_fbtx_wr))) begin
            cmd_inst_fbtx_full <= 1'b0;
            if ((uart_inst_insttxfifo_addr == 0)) begin
                uart_inst_insttx_fbustx_empty <= 1'b1;
            end
            else begin
                uart_inst_insttxfifo_addr <= (uart_inst_insttxfifo_addr - 1);
            end
        end
        else if ((cmd_inst_fbtx_wr && (!uart_inst_insttx_fbustx_rd))) begin
            uart_inst_insttx_fbustx_empty <= 1'b0;
            if ((!uart_inst_insttx_fbustx_empty)) begin
                uart_inst_insttxfifo_addr <= (uart_inst_insttxfifo_addr + 1);
            end
            if (($signed({1'b0, uart_inst_insttxfifo_addr}) == (4 - 2))) begin
                cmd_inst_fbtx_full <= 1'b1;
            end
        end
    end
end


always @(posedge clock) begin: XULA2_UART_INST_INSTTXFIFO_GENS_4
    if (cmd_inst_reset == 1) begin
        uart_inst_insttxfifo_nvacant <= 4;
        uart_inst_insttxfifo_ntenant <= 0;
    end
    else begin
        if (uart_inst_insttxfifo_fbus_clear) begin
            uart_inst_insttxfifo_nvacant <= 4;
            uart_inst_insttxfifo_ntenant <= 0;
        end
        else if ((uart_inst_insttx_fbustx_rd && (!cmd_inst_fbtx_wr))) begin
            uart_inst_insttxfifo_nvacant <= (uart_inst_insttxfifo_nvacant + 1);
            uart_inst_insttxfifo_ntenant <= (uart_inst_insttxfifo_ntenant - 1);
        end
        else if ((cmd_inst_fbtx_wr && (!uart_inst_insttx_fbustx_rd))) begin
            uart_inst_insttxfifo_nvacant <= (uart_inst_insttxfifo_nvacant - 1);
            uart_inst_insttxfifo_ntenant <= (uart_inst_insttxfifo_ntenant + 1);
        end
    end
end



assign uart_inst_insttxfifo_fbus_count = uart_inst_insttxfifo_ntenant;


always @(posedge clock) begin: XULA2_UART_INST_INSTSYNCTX_RTL
    integer ii;
    uart_inst_instsynctx_staps[0] <= uart_inst_tx;
    for (ii=1; ii<2; ii=ii+1) begin
        uart_inst_instsynctx_staps[ii] <= uart_inst_instsynctx_staps[(ii - 1)];
    end
end



assign uart_tx = uart_inst_instsynctx_staps[(2 - 1)];


always @(posedge clock) begin: XULA2_UART_INST_INSTTX_RTLTX
    if (cmd_inst_reset == 1) begin
        uart_inst_insttx_fbustx_rd <= 0;
        uart_inst_insttx_bitcnt <= 0;
        uart_inst_insttx_state <= 3'b000;
        uart_inst_insttx_txbyte <= 0;
        uart_inst_tx <= 1;
    end
    else begin
        uart_inst_insttx_fbustx_rd <= 1'b0;
        case (uart_inst_insttx_state)
            3'b000: begin
                if (((!uart_inst_insttx_fbustx_empty) && uart_inst_baudce)) begin
                    uart_inst_insttx_txbyte <= uart_inst_insttx_fbustx_rdata;
                    uart_inst_insttx_fbustx_rd <= 1'b1;
                    uart_inst_insttx_state <= 3'b001;
                end
            end
            3'b001: begin
                if (uart_inst_baudce) begin
                    uart_inst_insttx_bitcnt <= 0;
                    uart_inst_tx <= 1'b0;
                    uart_inst_insttx_state <= 3'b010;
                end
            end
            3'b010: begin
                if (uart_inst_baudce) begin
                    uart_inst_insttx_bitcnt <= (uart_inst_insttx_bitcnt + 1);
                    uart_inst_tx <= uart_inst_insttx_txbyte[uart_inst_insttx_bitcnt];
                end
                else if ((uart_inst_insttx_bitcnt == 8)) begin
                    uart_inst_insttx_state <= 3'b011;
                    uart_inst_insttx_bitcnt <= 0;
                end
            end
            3'b011: begin
                if (uart_inst_baudce) begin
                    uart_inst_tx <= 1'b1;
                    uart_inst_insttx_state <= 3'b100;
                end
            end
            3'b100: begin
                if (uart_inst_baudce) begin
                    uart_inst_insttx_state <= 3'b000;
                end
            end
            default: begin
                if (1'b0 !== 1) begin
                    $display("*** AssertionError ***");
                end
            end
        endcase
    end
end


always @(posedge clock) begin: XULA2_UART_INST_INSTRXFIFO_RTL_SRL_IN
    integer ii;
    if (uart_inst_instrx_fbusrx_wr) begin
        uart_inst_instrxfifo_mem[0] <= uart_inst_instrx_fbusrx_wdata;
        for (ii=1; ii<4; ii=ii+1) begin
            uart_inst_instrxfifo_mem[ii] <= uart_inst_instrxfifo_mem[(ii - 1)];
        end
    end
end



assign cmd_inst_fbrx_rdata = uart_inst_instrxfifo_mem[uart_inst_instrxfifo_addr];



assign cmd_inst_fbrx_rvld = cmd_inst_fbrx_rd;


always @(posedge clock) begin: XULA2_UART_INST_INSTRXFIFO_GENS_3
    if (cmd_inst_reset == 1) begin
        uart_inst_instrxfifo_fbus_full <= 0;
        cmd_inst_fbrx_empty <= 1;
        uart_inst_instrxfifo_addr <= 0;
    end
    else begin
        if (uart_inst_instrxfifo_fbus_clear) begin
            uart_inst_instrxfifo_addr <= 0;
            cmd_inst_fbrx_empty <= 1'b1;
            uart_inst_instrxfifo_fbus_full <= 1'b0;
        end
        else if ((cmd_inst_fbrx_rd && (!uart_inst_instrx_fbusrx_wr))) begin
            uart_inst_instrxfifo_fbus_full <= 1'b0;
            if ((uart_inst_instrxfifo_addr == 0)) begin
                cmd_inst_fbrx_empty <= 1'b1;
            end
            else begin
                uart_inst_instrxfifo_addr <= (uart_inst_instrxfifo_addr - 1);
            end
        end
        else if ((uart_inst_instrx_fbusrx_wr && (!cmd_inst_fbrx_rd))) begin
            cmd_inst_fbrx_empty <= 1'b0;
            if ((!cmd_inst_fbrx_empty)) begin
                uart_inst_instrxfifo_addr <= (uart_inst_instrxfifo_addr + 1);
            end
            if (($signed({1'b0, uart_inst_instrxfifo_addr}) == (4 - 2))) begin
                uart_inst_instrxfifo_fbus_full <= 1'b1;
            end
        end
    end
end


always @(posedge clock) begin: XULA2_UART_INST_INSTRXFIFO_GENS_4
    if (cmd_inst_reset == 1) begin
        uart_inst_instrxfifo_nvacant <= 4;
        uart_inst_instrxfifo_ntenant <= 0;
    end
    else begin
        if (uart_inst_instrxfifo_fbus_clear) begin
            uart_inst_instrxfifo_nvacant <= 4;
            uart_inst_instrxfifo_ntenant <= 0;
        end
        else if ((cmd_inst_fbrx_rd && (!uart_inst_instrx_fbusrx_wr))) begin
            uart_inst_instrxfifo_nvacant <= (uart_inst_instrxfifo_nvacant + 1);
            uart_inst_instrxfifo_ntenant <= (uart_inst_instrxfifo_ntenant - 1);
        end
        else if ((uart_inst_instrx_fbusrx_wr && (!cmd_inst_fbrx_rd))) begin
            uart_inst_instrxfifo_nvacant <= (uart_inst_instrxfifo_nvacant - 1);
            uart_inst_instrxfifo_ntenant <= (uart_inst_instrxfifo_ntenant + 1);
        end
    end
end



assign uart_inst_instrxfifo_fbus_count = uart_inst_instrxfifo_ntenant;


always @(posedge clock) begin: XULA2_UART_INST_INSTRX_RTLMID
    uart_inst_instrx_rxd <= uart_inst_rx;
    if (((uart_inst_instrx_rxd && (!uart_inst_rx)) && (uart_inst_instrx_state == 2'b00))) begin
        uart_inst_instrx_mcnt <= 0;
        uart_inst_instrx_rxinprog <= 1'b1;
    end
    else if ((uart_inst_instrx_rxinprog && (uart_inst_instrx_state == 2'b11))) begin
        uart_inst_instrx_rxinprog <= 1'b0;
    end
    else if (uart_inst_baudce16) begin
        uart_inst_instrx_mcnt <= (uart_inst_instrx_mcnt + 1);
    end
    if ((uart_inst_instrx_rxinprog && (uart_inst_instrx_mcnt == 7) && uart_inst_baudce16)) begin
        uart_inst_instrx_midbit <= 1'b1;
    end
    else begin
        uart_inst_instrx_midbit <= 1'b0;
    end
end


always @(posedge clock) begin: XULA2_UART_INST_INSTRX_RTLRX
    if (cmd_inst_reset == 1) begin
        uart_inst_instrx_bitcnt <= 0;
        uart_inst_instrx_fbusrx_wdata <= 0;
        uart_inst_instrx_state <= 2'b00;
        uart_inst_instrx_rxbyte <= 0;
        uart_inst_instrx_fbusrx_wr <= 0;
    end
    else begin
        uart_inst_instrx_fbusrx_wr <= 1'b0;
        case (uart_inst_instrx_state)
            2'b00: begin
                if ((uart_inst_instrx_midbit && (!uart_inst_rx))) begin
                    uart_inst_instrx_state <= 2'b01;
                end
            end
            2'b01: begin
                if (uart_inst_instrx_midbit) begin
                    uart_inst_instrx_rxbyte[uart_inst_instrx_bitcnt] <= uart_inst_rx;
                    uart_inst_instrx_bitcnt <= (uart_inst_instrx_bitcnt + 1);
                end
                else if ((uart_inst_instrx_bitcnt == 8)) begin
                    uart_inst_instrx_state <= 2'b10;
                    uart_inst_instrx_bitcnt <= 0;
                end
            end
            2'b10: begin
                if (uart_inst_instrx_midbit) begin
                    uart_inst_instrx_state <= 2'b11;
                    uart_inst_instrx_fbusrx_wr <= 1'b1;
                    uart_inst_instrx_fbusrx_wdata <= uart_inst_instrx_rxbyte;
                end
            end
            2'b11: begin
                uart_inst_instrx_state <= 2'b00;
                uart_inst_instrx_bitcnt <= 0;
            end
        endcase
    end
end


always @(posedge clock) begin: XULA2_UART_INST_INSTSYNCRX_RTL
    integer ii;
    uart_inst_instsyncrx_staps[0] <= uart_rx;
    for (ii=1; ii<2; ii=ii+1) begin
        uart_inst_instsyncrx_staps[ii] <= uart_inst_instsyncrx_staps[(ii - 1)];
		  uart_rx_1<= uart_rx;
    end
end



assign uart_inst_rx = uart_inst_instsyncrx_staps[(2 - 1)];


always @(posedge clock) begin: XULA2_UART_INST_INSTBAUD_RTLBAUD16
    if (cmd_inst_reset == 1) begin
        uart_inst_instbaud_cnt <= 0;
        uart_inst_baudce16 <= 0;
    end
    else begin
        if ((uart_inst_instbaud_cnt >= 529)) begin
            uart_inst_instbaud_cnt <= (uart_inst_instbaud_cnt - 529);
            uart_inst_baudce16 <= 1'b1;
        end
        else begin
            uart_inst_instbaud_cnt <= (uart_inst_instbaud_cnt + 96);
            uart_inst_baudce16 <= 1'b0;
        end
    end
end


always @(posedge clock) begin: XULA2_UART_INST_INSTBAUD_RTLBAUD
    if (cmd_inst_reset == 1) begin
        uart_inst_instbaud_cnt16 <= 0;
        uart_inst_baudce <= 0;
    end
    else begin
        if (uart_inst_baudce16) begin
            uart_inst_instbaud_cnt16 <= (uart_inst_instbaud_cnt16 + 1);
            if ((uart_inst_instbaud_cnt16 == 0)) begin
                uart_inst_baudce <= 1'b1;
            end
            else begin
                uart_inst_baudce <= 1'b0;
            end
        end
        else begin
            uart_inst_baudce <= 1'b0;
        end
    end
end


always @(posedge clock) begin: XULA2_BEH_ASSIGN
    if (glbl_tick_sec) begin
        tone <= ((~tone) & 1);
    end
    led <= (ledreg | tone[5-1:0]);
end



assign z4 = res4;



assign z5 = res5;



assign z6 = res6;



assign z7 = res7;



assign res6 = lift6[9-1:0];



assign res7 = lift7[9-1:0];



assign res4 = lift4[9-1:0];



assign res5 = lift5[9-1:0];



assign res2 = lift2[9-1:0];



assign res3 = lift3[9-1:0];



assign flgs4 = myregister4[30-1:27];
assign rht4 = myregister4[27-1:18];
assign sam4 = myregister4[18-1:9];
assign lft4 = myregister4[9-1:0];



assign res0 = lift0[9-1:0];



assign res1 = lift1[9-1:0];



assign z0 = res0;



assign z1 = res1;

endmodule