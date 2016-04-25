// File: catboard.v
// Generated by MyHDL 1.0dev
// Date: Tue Apr 19 20:05:18 2016


`timescale 1ns/10ps

module catboard (
    led,
    clock,
    mosi,
    miso,
    sck,
    ss
);
// a simple LED blinks example.
// This is intended to be used with the Xula, Stickit motherboard
// and an LED / button pmod board.

output [3:0] led;
reg [3:0] led;
input clock;
input mosi;
output miso;
reg miso;
input sck;
input ss;

reg fifobus_write;
reg [7:0] tone;
wire fifobus_empty;
reg [4:0] reset_dly_cnt;
reg glbl_tick_sec;
wire rd;
reg fifobus_read;
reg [7:0] fifobus_write_data;
wire empty;
wire full;
wire fifobus_full;
wire [7:0] ledreg;
wire wr;
wire [7:0] data;
reg reset;
wire [7:0] fifobus_read_data;
reg [16:0] tick_inst_mscnt;
reg [9:0] tick_inst_seccnt;
reg tick_inst_g2_increment;
reg [7:0] inst_spi_sl_ireg;
wire inst_spi_sl_csn;
reg inst_spi_sl_gotit;
reg inst_spi_sl_writepath_empty;
reg inst_spi_sl_writepath_read;
reg inst_spi_sl_spi_start;
reg [7:0] inst_spi_sl_readpath_write_data;
wire [7:0] inst_spi_sl_icaps;
reg [7:0] inst_spi_sl_oreg;
reg [7:0] inst_spi_sl_icap;
reg [3:0] inst_spi_sl_bitcnt;
reg [7:0] inst_spi_sl_ocap;
reg [3:0] inst_spi_sl_b2;
wire [3:0] inst_spi_sl_b3;
wire [7:0] inst_spi_sl_writepath_read_data;
reg inst_spi_sl_readpath_write;
wire inst_spi_sl_mp_fifo_inst_readpath_read;
wire [7:0] inst_spi_sl_mp_fifo_inst_writepath_write_data;
wire inst_spi_sl_mp_fifo_inst_readpath_read_valid;
reg inst_spi_sl_mp_fifo_inst_readpath_empty;
reg inst_spi_sl_mp_fifo_inst_writepath_full;
wire [7:0] inst_spi_sl_mp_fifo_inst_readpath_read_data;
wire inst_spi_sl_mp_fifo_inst_writepath_write;
wire inst_spi_sl_mp_fifo_inst_self_read_valid;
reg [4:0] inst_spi_sl_rx_fifo_inst_nvacant;
reg inst_spi_sl_rx_fifo_inst_fbus_full;
reg [3:0] inst_spi_sl_rx_fifo_inst_addr;
reg [4:0] inst_spi_sl_rx_fifo_inst_ntenant;
wire inst_spi_sl_rx_fifo_inst_fbus_clear;
wire [4:0] inst_spi_sl_rx_fifo_inst_fbus_count;
reg [4:0] inst_spi_sl_tx_fifo_inst_nvacant;
reg [3:0] inst_spi_sl_tx_fifo_inst_addr;
reg [4:0] inst_spi_sl_tx_fifo_inst_ntenant;
wire inst_spi_sl_tx_fifo_inst_fbus_clear;
wire [4:0] inst_spi_sl_tx_fifo_inst_fbus_count;
wire inst_spi_sl_tx_fifo_inst_fbus_read_valid;

reg [3:0] inst_spi_sl_isync2_inst_staps [0:3-1];
reg [7:0] inst_spi_sl_isync1_inst_staps [0:3-1];
reg [7:0] inst_spi_sl_rx_fifo_inst_mem [0:16-1];
reg [7:0] inst_spi_sl_tx_fifo_inst_mem [0:16-1];

assign ledreg = 0;
assign inst_spi_sl_csn = 1;
assign inst_spi_sl_rx_fifo_inst_fbus_clear = 0;
assign inst_spi_sl_tx_fifo_inst_fbus_clear = 0;



always @(fifobus_full, fifobus_read_data, fifobus_empty) begin: CATBOARD_TB_FIFO_LOOPBACK
    if ((!fifobus_full)) begin
        fifobus_write = (!fifobus_empty);
        fifobus_read = (!fifobus_empty);
        fifobus_write_data = fifobus_read_data;
    end
end

// For the first 4 clocks the reset is forced to lo
// for clock 6 to 31 the reset is set hi
// then the reset is lo
always @(posedge clock) begin: CATBOARD_RESET_TST
    if ((reset_dly_cnt < 31)) begin
        reset_dly_cnt <= (reset_dly_cnt + 1);
        if ((reset_dly_cnt <= 4)) begin
            reset <= 0;
        end
        if ((reset_dly_cnt >= 5)) begin
            reset <= 1;
        end
    end
    else begin
        reset <= 0;
    end
end


always @(posedge clock) begin: CATBOARD_INST_SPI_SL_BEH_IO_CAPTURE
    inst_spi_sl_readpath_write <= 1'b0;
    inst_spi_sl_writepath_read <= 1'b0;
    if ((inst_spi_sl_b3 == 0)) begin
        inst_spi_sl_gotit <= 1'b0;
    end
    else if (((inst_spi_sl_b3 == 8) && (!inst_spi_sl_gotit))) begin
        inst_spi_sl_readpath_write <= 1'b1;
        inst_spi_sl_readpath_write_data <= inst_spi_sl_icaps;
        inst_spi_sl_gotit <= 1'b1;
        inst_spi_sl_ocap <= inst_spi_sl_writepath_read_data;
        if ((!inst_spi_sl_writepath_empty)) begin
            inst_spi_sl_writepath_read <= 1'b1;
        end
    end
end



assign inst_spi_sl_b3 = inst_spi_sl_isync2_inst_staps[(3 - 1)];


always @(posedge clock) begin: CATBOARD_INST_SPI_SL_ISYNC2_INST_BEH_SYNC_STAGES
    integer ii;
    inst_spi_sl_isync2_inst_staps[0] <= inst_spi_sl_b2;
    for (ii=1; ii<3; ii=ii+1) begin
        inst_spi_sl_isync2_inst_staps[ii] <= inst_spi_sl_isync2_inst_staps[(ii - 1)];
    end
end


always @(posedge sck, posedge inst_spi_sl_csn) begin: CATBOARD_INST_SPI_SL_SCK_CAPTURE_SEND
    if (inst_spi_sl_csn) begin
        inst_spi_sl_b2 <= 0;
        inst_spi_sl_bitcnt <= 0;
    end
    else begin
        if (((inst_spi_sl_bitcnt == 0) || inst_spi_sl_spi_start)) begin
            miso <= inst_spi_sl_ocap[7];
            inst_spi_sl_oreg <= ((inst_spi_sl_ocap << 1) & 255);
        end
        else begin
            miso <= inst_spi_sl_oreg[7];
            inst_spi_sl_oreg <= ((inst_spi_sl_oreg << 1) & 255);
        end
        inst_spi_sl_ireg <= {inst_spi_sl_ireg[7-1:0], mosi};
        inst_spi_sl_bitcnt <= (inst_spi_sl_bitcnt + 1);
        if (($signed({1'b0, inst_spi_sl_bitcnt}) == (8 - 1))) begin
            inst_spi_sl_bitcnt <= 0;
            inst_spi_sl_b2 <= 8;
            inst_spi_sl_icap <= {inst_spi_sl_ireg[7-1:0], mosi};
        end
        else begin
            inst_spi_sl_b2 <= 0;
        end
    end
end


always @(posedge clock) begin: CATBOARD_INST_SPI_SL_TX_FIFO_INST_RTL_OCCUPANCY
    if (reset == 1) begin
        inst_spi_sl_tx_fifo_inst_nvacant <= 16;
        inst_spi_sl_tx_fifo_inst_ntenant <= 0;
    end
    else begin
        if (inst_spi_sl_tx_fifo_inst_fbus_clear) begin
            inst_spi_sl_tx_fifo_inst_nvacant <= 16;
            inst_spi_sl_tx_fifo_inst_ntenant <= 0;
        end
        else if ((inst_spi_sl_writepath_read && (!inst_spi_sl_mp_fifo_inst_writepath_write))) begin
            inst_spi_sl_tx_fifo_inst_nvacant <= (inst_spi_sl_tx_fifo_inst_nvacant + 1);
            inst_spi_sl_tx_fifo_inst_ntenant <= (inst_spi_sl_tx_fifo_inst_ntenant - 1);
        end
        else if ((inst_spi_sl_mp_fifo_inst_writepath_write && (!inst_spi_sl_writepath_read))) begin
            inst_spi_sl_tx_fifo_inst_nvacant <= (inst_spi_sl_tx_fifo_inst_nvacant - 1);
            inst_spi_sl_tx_fifo_inst_ntenant <= (inst_spi_sl_tx_fifo_inst_ntenant + 1);
        end
    end
end



assign inst_spi_sl_writepath_read_data = inst_spi_sl_tx_fifo_inst_mem[inst_spi_sl_tx_fifo_inst_addr];



assign inst_spi_sl_tx_fifo_inst_fbus_count = inst_spi_sl_tx_fifo_inst_ntenant;



assign inst_spi_sl_tx_fifo_inst_fbus_read_valid = (inst_spi_sl_writepath_read && (!inst_spi_sl_writepath_empty));


always @(posedge clock) begin: CATBOARD_INST_SPI_SL_TX_FIFO_INST_RTL_FIFO
    if (reset == 1) begin
        inst_spi_sl_mp_fifo_inst_writepath_full <= 0;
        inst_spi_sl_writepath_empty <= 1;
        inst_spi_sl_tx_fifo_inst_addr <= 0;
    end
    else begin
        if (inst_spi_sl_tx_fifo_inst_fbus_clear) begin
            inst_spi_sl_tx_fifo_inst_addr <= 0;
            inst_spi_sl_writepath_empty <= 1'b1;
            inst_spi_sl_mp_fifo_inst_writepath_full <= 1'b0;
        end
        else if ((inst_spi_sl_writepath_read && (!inst_spi_sl_mp_fifo_inst_writepath_write))) begin
            inst_spi_sl_mp_fifo_inst_writepath_full <= 1'b0;
            if ((inst_spi_sl_tx_fifo_inst_addr == 0)) begin
                inst_spi_sl_writepath_empty <= 1'b1;
            end
            else begin
                inst_spi_sl_tx_fifo_inst_addr <= (inst_spi_sl_tx_fifo_inst_addr - 1);
            end
        end
        else if ((inst_spi_sl_mp_fifo_inst_writepath_write && (!inst_spi_sl_writepath_read))) begin
            inst_spi_sl_writepath_empty <= 1'b0;
            if ((!inst_spi_sl_writepath_empty)) begin
                inst_spi_sl_tx_fifo_inst_addr <= (inst_spi_sl_tx_fifo_inst_addr + 1);
            end
            if (($signed({1'b0, inst_spi_sl_tx_fifo_inst_addr}) == (16 - 2))) begin
                inst_spi_sl_mp_fifo_inst_writepath_full <= 1'b1;
            end
        end
    end
end


always @(posedge clock) begin: CATBOARD_INST_SPI_SL_TX_FIFO_INST_RTL_SRL_IN
    integer jj;
    if (inst_spi_sl_mp_fifo_inst_writepath_write) begin
        inst_spi_sl_tx_fifo_inst_mem[0] <= inst_spi_sl_mp_fifo_inst_writepath_write_data;
        for (jj=1; jj<16; jj=jj+1) begin
            inst_spi_sl_tx_fifo_inst_mem[jj] <= inst_spi_sl_tx_fifo_inst_mem[(jj - 1)];
        end
    end
end


always @(posedge clock) begin: CATBOARD_INST_SPI_SL_RX_FIFO_INST_RTL_OCCUPANCY
    if (reset == 1) begin
        inst_spi_sl_rx_fifo_inst_nvacant <= 16;
        inst_spi_sl_rx_fifo_inst_ntenant <= 0;
    end
    else begin
        if (inst_spi_sl_rx_fifo_inst_fbus_clear) begin
            inst_spi_sl_rx_fifo_inst_nvacant <= 16;
            inst_spi_sl_rx_fifo_inst_ntenant <= 0;
        end
        else if ((inst_spi_sl_mp_fifo_inst_readpath_read && (!inst_spi_sl_readpath_write))) begin
            inst_spi_sl_rx_fifo_inst_nvacant <= (inst_spi_sl_rx_fifo_inst_nvacant + 1);
            inst_spi_sl_rx_fifo_inst_ntenant <= (inst_spi_sl_rx_fifo_inst_ntenant - 1);
        end
        else if ((inst_spi_sl_readpath_write && (!inst_spi_sl_mp_fifo_inst_readpath_read))) begin
            inst_spi_sl_rx_fifo_inst_nvacant <= (inst_spi_sl_rx_fifo_inst_nvacant - 1);
            inst_spi_sl_rx_fifo_inst_ntenant <= (inst_spi_sl_rx_fifo_inst_ntenant + 1);
        end
    end
end



assign inst_spi_sl_mp_fifo_inst_readpath_read_data = inst_spi_sl_rx_fifo_inst_mem[inst_spi_sl_rx_fifo_inst_addr];



assign inst_spi_sl_rx_fifo_inst_fbus_count = inst_spi_sl_rx_fifo_inst_ntenant;



assign inst_spi_sl_mp_fifo_inst_readpath_read_valid = (inst_spi_sl_mp_fifo_inst_readpath_read && (!inst_spi_sl_mp_fifo_inst_readpath_empty));


always @(posedge clock) begin: CATBOARD_INST_SPI_SL_RX_FIFO_INST_RTL_FIFO
    if (reset == 1) begin
        inst_spi_sl_rx_fifo_inst_fbus_full <= 0;
        inst_spi_sl_mp_fifo_inst_readpath_empty <= 1;
        inst_spi_sl_rx_fifo_inst_addr <= 0;
    end
    else begin
        if (inst_spi_sl_rx_fifo_inst_fbus_clear) begin
            inst_spi_sl_rx_fifo_inst_addr <= 0;
            inst_spi_sl_mp_fifo_inst_readpath_empty <= 1'b1;
            inst_spi_sl_rx_fifo_inst_fbus_full <= 1'b0;
        end
        else if ((inst_spi_sl_mp_fifo_inst_readpath_read && (!inst_spi_sl_readpath_write))) begin
            inst_spi_sl_rx_fifo_inst_fbus_full <= 1'b0;
            if ((inst_spi_sl_rx_fifo_inst_addr == 0)) begin
                inst_spi_sl_mp_fifo_inst_readpath_empty <= 1'b1;
            end
            else begin
                inst_spi_sl_rx_fifo_inst_addr <= (inst_spi_sl_rx_fifo_inst_addr - 1);
            end
        end
        else if ((inst_spi_sl_readpath_write && (!inst_spi_sl_mp_fifo_inst_readpath_read))) begin
            inst_spi_sl_mp_fifo_inst_readpath_empty <= 1'b0;
            if ((!inst_spi_sl_mp_fifo_inst_readpath_empty)) begin
                inst_spi_sl_rx_fifo_inst_addr <= (inst_spi_sl_rx_fifo_inst_addr + 1);
            end
            if (($signed({1'b0, inst_spi_sl_rx_fifo_inst_addr}) == (16 - 2))) begin
                inst_spi_sl_rx_fifo_inst_fbus_full <= 1'b1;
            end
        end
    end
end


always @(posedge clock) begin: CATBOARD_INST_SPI_SL_RX_FIFO_INST_RTL_SRL_IN
    integer jj;
    if (inst_spi_sl_readpath_write) begin
        inst_spi_sl_rx_fifo_inst_mem[0] <= inst_spi_sl_readpath_write_data;
        for (jj=1; jj<16; jj=jj+1) begin
            inst_spi_sl_rx_fifo_inst_mem[jj] <= inst_spi_sl_rx_fifo_inst_mem[(jj - 1)];
        end
    end
end



assign inst_spi_sl_mp_fifo_inst_writepath_write = fifobus_write;
assign inst_spi_sl_mp_fifo_inst_writepath_write_data = fifobus_write_data;
assign fifobus_full = inst_spi_sl_mp_fifo_inst_writepath_full;
assign inst_spi_sl_mp_fifo_inst_readpath_read = fifobus_read;
assign fifobus_read_data = inst_spi_sl_mp_fifo_inst_readpath_read_data;
assign inst_spi_sl_mp_fifo_inst_self_read_valid = inst_spi_sl_mp_fifo_inst_readpath_read_valid;
assign fifobus_empty = inst_spi_sl_mp_fifo_inst_readpath_empty;



assign inst_spi_sl_icaps = inst_spi_sl_isync1_inst_staps[(3 - 1)];


always @(posedge clock) begin: CATBOARD_INST_SPI_SL_ISYNC1_INST_BEH_SYNC_STAGES
    integer ii;
    inst_spi_sl_isync1_inst_staps[0] <= inst_spi_sl_icap;
    for (ii=1; ii<3; ii=ii+1) begin
        inst_spi_sl_isync1_inst_staps[ii] <= inst_spi_sl_isync1_inst_staps[(ii - 1)];
    end
end


always @(posedge sck, negedge inst_spi_sl_csn) begin: CATBOARD_INST_SPI_SL_CSN_FALLS
    if (sck) begin
        inst_spi_sl_spi_start <= 1'b0;
    end
    else if ((!inst_spi_sl_csn)) begin
        inst_spi_sl_spi_start <= 1'b1;
    end
end


always @(posedge clock) begin: CATBOARD_TICK_INST_G1_RTL_COUNT
    if (reset == 1) begin
        tick_inst_mscnt <= 0;
    end
    else begin
        if (1'b1) begin
            if (($signed({1'b0, tick_inst_mscnt}) == (100000 - 1))) begin
                tick_inst_mscnt <= 0;
            end
            else begin
                tick_inst_mscnt <= (tick_inst_mscnt + 1);
            end
        end
    end
end


always @(posedge clock) begin: CATBOARD_TICK_INST_G1_RTL_OVERFLOW
    if ((1'b1 && ($signed({1'b0, tick_inst_mscnt}) == (100000 - 2)))) begin
        tick_inst_g2_increment <= 1'b1;
    end
    else begin
        tick_inst_g2_increment <= 1'b0;
    end
end


always @(posedge clock) begin: CATBOARD_TICK_INST_G2_RTL_COUNT
    if (reset == 1) begin
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


always @(posedge clock) begin: CATBOARD_TICK_INST_G2_RTL_OVERFLOW
    if ((tick_inst_g2_increment && ($signed({1'b0, tick_inst_seccnt}) == (1000 - 2)))) begin
        glbl_tick_sec <= 1'b1;
    end
    else begin
        glbl_tick_sec <= 1'b0;
    end
end


always @(posedge clock) begin: CATBOARD_BEH_ASSIGN
    if (glbl_tick_sec) begin
        tone <= ((~tone) & 1);
    end
    led <= (ledreg | tone[5-1:0]);
end



assign data = fifobus_read_data;
assign rd = fifobus_read;
assign wr = fifobus_write;
assign full = fifobus_full;
assign empty = fifobus_empty;

endmodule