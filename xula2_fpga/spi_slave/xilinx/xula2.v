// File: xula2.v
// Generated by MyHDL 1.0dev
// Date: Sat Apr  9 09:05:52 2016


`timescale 1ns/10ps

module xula2 (
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

input led;
input clock;
input mosi;
input miso;
input sck;
input ss;

reg fifobus_write;
reg [23:0] cnt;
wire full;
reg [4:0] reset_dly_cnt;
wire rd;
reg toggle;
reg [7:0] fifobus_read_data;
reg fifobus_full;
wire wr;
reg fifobus_read;
reg [7:0] fifobus_write_data;
reg reset;
wire [7:0] data;
wire empty;
reg fifobus_empty;
wire [7:0] spi_inst_cso_slave_select;
reg [7:0] spi_inst_cso_rx_fifo_count;
wire spi_inst_cso_clock_polarity;
reg spi_inst_irx_empty;
reg [7:0] spi_inst_irx_write_data;
wire [4:0] spi_inst_itx_count;
reg [2:0] spi_inst_bcnt;
wire spi_inst_cso_loopback;
reg spi_inst_itx_full;
reg spi_inst_cso_rx_full;
wire [7:0] spi_inst_itx_read_data;
wire spi_inst_cso_manual_slave_select;
reg [7:0] spi_inst_spibus_ss;
reg spi_inst_fifobus_read_valid;
wire spi_inst_cso_enable;
reg [2:0] spi_inst_state;
wire [7:0] spi_inst_irx_read_data;
reg spi_inst_spibus_sck;
reg spi_inst_x_ss;
reg [7:0] spi_inst_itx_write_data;
wire spi_inst_irx_read_valid;
wire spi_inst_cso_tx_write;
reg [11:0] spi_inst_clkcnt;
wire [7:0] spi_inst_cso_tx_byte;
reg spi_inst_irx_write;
reg spi_inst_cso_tx_empty;
reg spi_inst_ena;
reg spi_inst_x_miso;
wire [4:0] spi_inst_irx_count;
reg spi_inst_cso_rx_empty;
reg spi_inst_x_sck;
wire spi_inst_cso_freeze;
wire spi_inst_cso_bypass_fifo;
reg [7:0] spi_inst_rreg;
reg spi_inst_itx_empty;
wire spi_inst_spibus_miso;
reg spi_inst_cso_rx_byte_valid;
wire [7:0] spi_inst_cso_clock_divisor;
reg spi_inst_itx_write;
reg [7:0] spi_inst_cso_rx_byte;
reg spi_inst_itx_read;
reg [7:0] spi_inst_cso_tx_fifo_count;
wire spi_inst_x_mosi;
reg [7:0] spi_inst_treg;
reg spi_inst_cso_tx_full;
reg spi_inst_spibus_mosi;
reg spi_inst_irx_full;
reg spi_inst_irx_read;
wire spi_inst_cso_rx_read;
wire spi_inst_cso_clock_phase;
reg [3:0] spi_inst_fifo_rx_inst_addr;
wire [4:0] spi_inst_fifo_rx_inst_ntenant;
wire spi_inst_fifo_rx_inst_fbus_clear;
reg [3:0] spi_inst_fifo_tx_inst_addr;
wire [4:0] spi_inst_fifo_tx_inst_ntenant;
wire spi_inst_fifo_tx_inst_fbus_clear;
wire spi_inst_fifo_tx_inst_fbus_read_valid;
wire gens_0_keep;
wire gens_0_gas_5_keep;
wire gens_0_gas_4_keep;
wire gens_0_gas_3_keep;
wire gens_0_gas_2_keep;
wire gens_0_gas_1_keep;
wire gens_0_gas_0_keep;

reg [7:0] spi_inst_fifo_rx_inst_mem [0:16-1];
reg [7:0] spi_inst_fifo_tx_inst_mem [0:16-1];

assign spi_inst_cso_manual_slave_select = 1'd0;
assign spi_inst_cso_tx_write = 1'd0;
assign spi_inst_cso_tx_byte = 8'd0;
assign spi_inst_spibus_miso = 1'd1;
assign spi_inst_cso_rx_read = 1'd0;
assign spi_inst_fifo_rx_inst_ntenant = 5'd0;
assign spi_inst_fifo_rx_inst_fbus_clear = 1'd0;
assign spi_inst_fifo_tx_inst_ntenant = 5'd0;
assign spi_inst_fifo_tx_inst_fbus_clear = 1'd0;
assign gens_0_keep = 1'd0;



always @(posedge clock) begin: XULA2_RTL
    if (($signed({1'b0, cnt}) == (12000000 - 1))) begin
        toggle <= (!toggle);
        cnt <= 0;
    end
    else begin
        cnt <= (cnt + 1);
    end
end


always @(fifobus_full, fifobus_read_data, fifobus_empty) begin: XULA2_TB_FIFO_LOOPBACK
    if ((!fifobus_full)) begin
        fifobus_write = (!fifobus_empty);
        fifobus_read = (!fifobus_empty);
        fifobus_write_data = fifobus_read_data;
    end
end

// For the first 4 clocks the reset is forced to lo
// for clock 6 to 31 the reset is set hi
// then the reset is lo
always @(posedge clock) begin: XULA2_RESET_TST
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

// In the static configuration case only one value makes sense
// for certain configuration signals, those are set here

assign spi_inst_cso_enable = gens_0_keep ? 1'b1 : 1'b1;
assign spi_inst_cso_freeze = 1'b0;



assign spi_inst_cso_clock_polarity = gens_0_gas_0_keep ? 0 : 0;



assign spi_inst_cso_loopback = gens_0_gas_1_keep ? 0 : 0;



assign spi_inst_cso_slave_select = gens_0_gas_2_keep ? 0 : 0;



assign spi_inst_cso_clock_phase = gens_0_gas_3_keep ? 0 : 0;



assign spi_inst_cso_clock_divisor = gens_0_gas_4_keep ? 0 : 0;



assign spi_inst_cso_bypass_fifo = gens_0_gas_5_keep ? 0 : 0;


always @(posedge clock) begin: XULA2_SPI_INST_GENS_0
    if ((spi_inst_cso_enable && (spi_inst_clkcnt != 0) && (spi_inst_state != 3'b000))) begin
        spi_inst_clkcnt <= (spi_inst_clkcnt - 1);
    end
    else begin
        case (spi_inst_cso_clock_divisor)
            0: spi_inst_clkcnt <= 0;
            1: spi_inst_clkcnt <= 1;
            2: spi_inst_clkcnt <= 3;
            3: spi_inst_clkcnt <= 7;
            4: spi_inst_clkcnt <= 15;
            5: spi_inst_clkcnt <= 31;
            6: spi_inst_clkcnt <= 63;
            7: spi_inst_clkcnt <= 127;
            8: spi_inst_clkcnt <= 255;
            9: spi_inst_clkcnt <= 511;
            10: spi_inst_clkcnt <= 1023;
            11: spi_inst_clkcnt <= 2047;
            default: spi_inst_clkcnt <= 4095;
        endcase
    end
end


always @(spi_inst_x_mosi, spi_inst_spibus_miso, spi_inst_x_sck, spi_inst_cso_loopback) begin: XULA2_SPI_INST_GENS_1
    spi_inst_spibus_sck = spi_inst_x_sck;
    if (spi_inst_cso_loopback) begin
        spi_inst_x_miso = spi_inst_x_mosi;
    end
    else begin
        spi_inst_x_miso = spi_inst_spibus_miso;
    end
end



assign spi_inst_itx_read_data = spi_inst_fifo_tx_inst_mem[spi_inst_fifo_tx_inst_addr];



assign spi_inst_itx_count = spi_inst_fifo_tx_inst_ntenant;



assign spi_inst_fifo_tx_inst_fbus_read_valid = (spi_inst_itx_read && (!spi_inst_itx_empty));


always @(posedge clock) begin: XULA2_SPI_INST_FIFO_TX_INST_RTL_FIFO
    if (reset == 1) begin
        spi_inst_itx_full <= 0;
        spi_inst_itx_empty <= 1;
        spi_inst_fifo_tx_inst_addr <= 0;
    end
    else begin
        if (spi_inst_fifo_tx_inst_fbus_clear) begin
            spi_inst_fifo_tx_inst_addr <= 0;
            spi_inst_itx_empty <= 1'b1;
            spi_inst_itx_full <= 1'b0;
        end
        else if ((spi_inst_itx_read && (!spi_inst_itx_write))) begin
            spi_inst_itx_full <= 1'b0;
            if ((spi_inst_fifo_tx_inst_addr == 0)) begin
                spi_inst_itx_empty <= 1'b1;
            end
            else begin
                spi_inst_fifo_tx_inst_addr <= (spi_inst_fifo_tx_inst_addr - 1);
            end
        end
        else if ((spi_inst_itx_write && (!spi_inst_itx_read))) begin
            spi_inst_itx_empty <= 1'b0;
            if ((!spi_inst_itx_empty)) begin
                spi_inst_fifo_tx_inst_addr <= (spi_inst_fifo_tx_inst_addr + 1);
            end
            if (($signed({1'b0, spi_inst_fifo_tx_inst_addr}) == (16 - 2))) begin
                spi_inst_itx_full <= 1'b1;
            end
        end
    end
end


always @(posedge clock) begin: XULA2_SPI_INST_FIFO_TX_INST_RTL_SRL_IN
    integer jj;
    if (spi_inst_itx_write) begin
        spi_inst_fifo_tx_inst_mem[0] <= spi_inst_itx_write_data;
        for (jj=1; jj<16; jj=jj+1) begin
            spi_inst_fifo_tx_inst_mem[jj] <= spi_inst_fifo_tx_inst_mem[(jj - 1)];
        end
    end
end


always @(spi_inst_x_mosi, spi_inst_cso_loopback) begin: XULA2_SPI_INST_RTL_GATE_MOSI
    if (spi_inst_cso_loopback) begin
        spi_inst_spibus_mosi = 1'b0;
    end
    else begin
        spi_inst_spibus_mosi = spi_inst_x_mosi;
    end
end



assign spi_inst_x_mosi = spi_inst_treg[7];

// Designed to the following timing diagram
// 
// SCK   CPOL=0 ______/---\___/---\___/---\___/---\___/---\___/---\___/---\___/---\___/---\ 
//       CPOL=1 ------\___/---\___/---\___/---\___/---\___/---\___/---\___/---\___/---\___/ 
// SS           ---\_______________________________________________________________________ 
// CPHA=0 MOSI  ...|.0....|.1.....|.2.....|.3.....|.4.....|.5.....|.6.....|.7.....|.0.....| 
//        MISO  ...|.0....|.1.....|.2.....|.3.....|.4.....|.5.....|.6.....|.7.....|.0.....| 
// CPHA=1 MOSI  ...|....0.....|.1.....|.2.....|.3.....|.4.....|.5.....|.6.....|.7.....|.0...
//        MISO  ......|.0.....|.1.....|.2.....|.3.....|.4.....|.5.....|.6.....|.7.....|.0...
always @(posedge clock) begin: XULA2_SPI_INST_RTL_STATE_AND_MORE
    if (reset == 1) begin
        spi_inst_itx_read <= 0;
        spi_inst_x_sck <= 0;
        spi_inst_treg <= 0;
        spi_inst_state <= 3'b000;
        spi_inst_bcnt <= 0;
        spi_inst_x_ss <= 0;
        spi_inst_irx_write <= 0;
        spi_inst_rreg <= 0;
    end
    else begin
        if ((!spi_inst_cso_enable)) begin
            spi_inst_state <= 3'b000;
            spi_inst_bcnt <= 0;
            spi_inst_treg <= 0;
            spi_inst_itx_read <= 1'b0;
            spi_inst_irx_write <= 1'b0;
            spi_inst_x_sck <= 1'b0;
            spi_inst_x_ss <= 1'b0;
        end
        else begin
            if ((!spi_inst_cso_freeze)) begin
                case (spi_inst_state)
                    3'b000: begin
                        spi_inst_bcnt <= 7;
                        spi_inst_treg <= spi_inst_itx_read_data;
                        spi_inst_x_sck <= spi_inst_cso_clock_polarity;
                        spi_inst_irx_write <= 1'b0;
                        if (((!spi_inst_itx_empty) && (!spi_inst_irx_full))) begin
                            spi_inst_itx_read <= 1'b1;
                            spi_inst_x_ss <= 1'b0;
                            if (spi_inst_cso_clock_phase) begin
                                spi_inst_state <= 3'b001;
                            end
                            else begin
                                spi_inst_state <= 3'b010;
                            end
                        end
                        else begin
                            spi_inst_itx_read <= 1'b0;
                            spi_inst_x_ss <= 1'b1;
                        end
                    end
                    3'b001: begin
                        spi_inst_itx_read <= 1'b0;
                        spi_inst_irx_write <= 1'b0;
                        if (spi_inst_ena) begin
                            spi_inst_x_sck <= (!spi_inst_x_sck);
                            spi_inst_state <= 3'b010;
                        end
                    end
                    3'b010: begin
                        spi_inst_itx_read <= 1'b0;
                        spi_inst_irx_write <= 1'b0;
                        if (spi_inst_ena) begin
                            spi_inst_x_sck <= (!spi_inst_x_sck);
                            spi_inst_rreg <= {spi_inst_rreg[7-1:0], spi_inst_x_miso};
                            if ((spi_inst_cso_clock_phase && (spi_inst_bcnt == 0))) begin
                                spi_inst_irx_write <= 1'b1;
                                if ((spi_inst_itx_empty || spi_inst_irx_full)) begin
                                    spi_inst_state <= 3'b101;
                                end
                                else begin
                                    spi_inst_state <= 3'b011;
                                end
                            end
                            else begin
                                spi_inst_state <= 3'b011;
                            end
                        end
                    end
                    3'b011: begin
                        spi_inst_itx_read <= 1'b0;
                        spi_inst_irx_write <= 1'b0;
                        if (spi_inst_ena) begin
                            spi_inst_x_sck <= (!spi_inst_x_sck);
                            if ((spi_inst_bcnt == 0)) begin
                                if ((!spi_inst_cso_clock_phase)) begin
                                    spi_inst_irx_write <= 1'b1;
                                end
                                if ((spi_inst_itx_empty || spi_inst_irx_full)) begin
                                    spi_inst_state <= 3'b101;
                                end
                                else begin
                                    spi_inst_bcnt <= 7;
                                    spi_inst_state <= 3'b010;
                                    spi_inst_itx_read <= 1'b1;
                                    spi_inst_treg <= spi_inst_itx_read_data;
                                end
                            end
                            else begin
                                spi_inst_treg <= {spi_inst_treg[7-1:0], 1'h0};
                                spi_inst_bcnt <= (spi_inst_bcnt - 1);
                                spi_inst_state <= 3'b010;
                            end
                        end
                    end
                    3'b101: begin
                        spi_inst_itx_read <= 1'b0;
                        spi_inst_irx_write <= 1'b0;
                        if (spi_inst_ena) begin
                            spi_inst_state <= 3'b000;
                        end
                    end
                    default: begin
                        spi_inst_state <= 3'b000;
                        if (1'b0 !== 1) begin
                            $display("*** AssertionError ***");
                        end
                    end
                endcase
            end
        end
    end
end


always @(spi_inst_irx_count, spi_inst_clkcnt, spi_inst_itx_count) begin: XULA2_SPI_INST_RTL_ASSIGN
    spi_inst_cso_tx_fifo_count = spi_inst_itx_count;
    spi_inst_cso_rx_fifo_count = spi_inst_irx_count;
    if ((spi_inst_clkcnt > 0)) begin
        spi_inst_ena = 1'b0;
    end
    else begin
        spi_inst_ena = 1'b1;
    end
end


always @(spi_inst_cso_slave_select, spi_inst_x_ss, spi_inst_cso_manual_slave_select) begin: XULA2_SPI_INST_RTL_SLAVE_SELECT
    if (spi_inst_cso_manual_slave_select) begin
        spi_inst_spibus_ss = (~spi_inst_cso_slave_select);
    end
    else if (spi_inst_x_ss) begin
        spi_inst_spibus_ss = 255;
    end
    else begin
        spi_inst_spibus_ss = (~spi_inst_cso_slave_select);
    end
end

// The `itx` and `irx` FIFO interfaces are driven by different
// logic depending on the configuration.  This modules accesses
// the `itx` read side and drives the `irx` write side.  The
// `itx` write side is driven by the `cso` or the `fifobus` port.
// The `irx` read side is accessed by the `cso` or the `fifobus`
// port.
always @(fifobus_write, spi_inst_rreg, spi_inst_irx_empty, spi_inst_cso_rx_read, spi_inst_cso_bypass_fifo, spi_inst_itx_full, spi_inst_irx_read_data, spi_inst_irx_full, spi_inst_itx_empty, fifobus_read, spi_inst_irx_read_valid, spi_inst_cso_tx_write, fifobus_write_data, spi_inst_cso_tx_byte) begin: XULA2_SPI_INST_RTL_FIFO_SEL
    if (spi_inst_cso_bypass_fifo) begin
        spi_inst_cso_tx_empty = spi_inst_itx_empty;
        spi_inst_cso_tx_full = spi_inst_itx_full;
        spi_inst_itx_write_data = spi_inst_cso_tx_byte;
        spi_inst_cso_rx_empty = spi_inst_irx_empty;
        spi_inst_cso_rx_full = spi_inst_irx_full;
        spi_inst_cso_rx_byte = spi_inst_irx_read_data;
        spi_inst_cso_rx_byte_valid = spi_inst_irx_read_valid;
        spi_inst_itx_write = spi_inst_cso_tx_write;
        spi_inst_irx_read = spi_inst_cso_rx_read;
    end
    else begin
        fifobus_full = spi_inst_itx_full;
        spi_inst_itx_write_data = fifobus_write_data;
        spi_inst_itx_write = fifobus_write;
        fifobus_empty = spi_inst_irx_empty;
        fifobus_read_data = spi_inst_irx_read_data;
        spi_inst_fifobus_read_valid = spi_inst_irx_read_valid;
        spi_inst_irx_read = fifobus_read;
    end
    spi_inst_irx_write_data = spi_inst_rreg;
end



assign spi_inst_irx_read_data = spi_inst_fifo_rx_inst_mem[spi_inst_fifo_rx_inst_addr];



assign spi_inst_irx_count = spi_inst_fifo_rx_inst_ntenant;



assign spi_inst_irx_read_valid = (spi_inst_irx_read && (!spi_inst_irx_empty));


always @(posedge clock) begin: XULA2_SPI_INST_FIFO_RX_INST_RTL_FIFO
    if (reset == 1) begin
        spi_inst_irx_full <= 0;
        spi_inst_irx_empty <= 1;
        spi_inst_fifo_rx_inst_addr <= 0;
    end
    else begin
        if (spi_inst_fifo_rx_inst_fbus_clear) begin
            spi_inst_fifo_rx_inst_addr <= 0;
            spi_inst_irx_empty <= 1'b1;
            spi_inst_irx_full <= 1'b0;
        end
        else if ((spi_inst_irx_read && (!spi_inst_irx_write))) begin
            spi_inst_irx_full <= 1'b0;
            if ((spi_inst_fifo_rx_inst_addr == 0)) begin
                spi_inst_irx_empty <= 1'b1;
            end
            else begin
                spi_inst_fifo_rx_inst_addr <= (spi_inst_fifo_rx_inst_addr - 1);
            end
        end
        else if ((spi_inst_irx_write && (!spi_inst_irx_read))) begin
            spi_inst_irx_empty <= 1'b0;
            if ((!spi_inst_irx_empty)) begin
                spi_inst_fifo_rx_inst_addr <= (spi_inst_fifo_rx_inst_addr + 1);
            end
            if (($signed({1'b0, spi_inst_fifo_rx_inst_addr}) == (16 - 2))) begin
                spi_inst_irx_full <= 1'b1;
            end
        end
    end
end


always @(posedge clock) begin: XULA2_SPI_INST_FIFO_RX_INST_RTL_SRL_IN
    integer jj;
    if (spi_inst_irx_write) begin
        spi_inst_fifo_rx_inst_mem[0] <= spi_inst_irx_write_data;
        for (jj=1; jj<16; jj=jj+1) begin
            spi_inst_fifo_rx_inst_mem[jj] <= spi_inst_fifo_rx_inst_mem[(jj - 1)];
        end
    end
end



assign data = fifobus_read_data;
assign rd = fifobus_read;
assign wr = fifobus_write;
assign full = fifobus_full;
assign empty = fifobus_empty;

endmodule
