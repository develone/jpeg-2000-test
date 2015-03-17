// File: rom_flgs.v
// Generated by MyHDL 0.9dev
// Date: Tue Mar 17 12:59:56 2015


`timescale 1ns/10ps

module rom_flgs (
    dout_flgs,
    addr_flgs
);
// ROM model 

output [79:0] dout_flgs;
reg [79:0] dout_flgs;
input [9:0] addr_flgs;






always @(addr_flgs) begin: ROM_FLGS_READ
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

endmodule
