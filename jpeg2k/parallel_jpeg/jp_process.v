// File: jp_process.v
// Generated by MyHDL 0.9dev
// Date: Wed Feb 18 18:51:31 2015


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


output signed [7:0] res_out_x;
reg signed [7:0] res_out_x;
input [2047:0] left_s_i;
input [2047:0] sam_s_i;
input [2047:0] right_s_i;
input [1279:0] flgs_s_i;
output noupdate_s;
reg noupdate_s;
input update_s;


wire [7:0] right_s [0:256-1];
wire [4:0] flgs_s [0:256-1];
wire [7:0] sam_s [0:256-1];
wire [7:0] left_s [0:256-1];



// update_s needs to be 1
// for the res_out_x to be valid
// noupdate_s goes lo when a
// res_out_x valid
// fwd dwt even flgs_s eq 7
// inv dwt even flgs_s eq 5
// fwd dwt odd flgs_s eq 6
// inv dwt odd flgs_s eq 4
always @(update_s, right_s[0], right_s[1], right_s[2], right_s[3], right_s[4], right_s[5], right_s[6], right_s[7], right_s[8], right_s[9], right_s[10], right_s[11], right_s[12], right_s[13], right_s[14], right_s[15], right_s[16], right_s[17], right_s[18], right_s[19], right_s[20], right_s[21], right_s[22], right_s[23], right_s[24], right_s[25], right_s[26], right_s[27], right_s[28], right_s[29], right_s[30], right_s[31], right_s[32], right_s[33], right_s[34], right_s[35], right_s[36], right_s[37], right_s[38], right_s[39], right_s[40], right_s[41], right_s[42], right_s[43], right_s[44], right_s[45], right_s[46], right_s[47], right_s[48], right_s[49], right_s[50], right_s[51], right_s[52], right_s[53], right_s[54], right_s[55], right_s[56], right_s[57], right_s[58], right_s[59], right_s[60], right_s[61], right_s[62], right_s[63], right_s[64], right_s[65], right_s[66], right_s[67], right_s[68], right_s[69], right_s[70], right_s[71], right_s[72], right_s[73], right_s[74], right_s[75], right_s[76], right_s[77], right_s[78], right_s[79], right_s[80], right_s[81], right_s[82], right_s[83], right_s[84], right_s[85], right_s[86], right_s[87], right_s[88], right_s[89], right_s[90], right_s[91], right_s[92], right_s[93], right_s[94], right_s[95], right_s[96], right_s[97], right_s[98], right_s[99], right_s[100], right_s[101], right_s[102], right_s[103], right_s[104], right_s[105], right_s[106], right_s[107], right_s[108], right_s[109], right_s[110], right_s[111], right_s[112], right_s[113], right_s[114], right_s[115], right_s[116], right_s[117], right_s[118], right_s[119], right_s[120], right_s[121], right_s[122], right_s[123], right_s[124], right_s[125], right_s[126], right_s[127], right_s[128], right_s[129], right_s[130], right_s[131], right_s[132], right_s[133], right_s[134], right_s[135], right_s[136], right_s[137], right_s[138], right_s[139], right_s[140], right_s[141], right_s[142], right_s[143], right_s[144], right_s[145], right_s[146], right_s[147], right_s[148], right_s[149], right_s[150], right_s[151], right_s[152], right_s[153], right_s[154], right_s[155], right_s[156], right_s[157], right_s[158], right_s[159], right_s[160], right_s[161], right_s[162], right_s[163], right_s[164], right_s[165], right_s[166], right_s[167], right_s[168], right_s[169], right_s[170], right_s[171], right_s[172], right_s[173], right_s[174], right_s[175], right_s[176], right_s[177], right_s[178], right_s[179], right_s[180], right_s[181], right_s[182], right_s[183], right_s[184], right_s[185], right_s[186], right_s[187], right_s[188], right_s[189], right_s[190], right_s[191], right_s[192], right_s[193], right_s[194], right_s[195], right_s[196], right_s[197], right_s[198], right_s[199], right_s[200], right_s[201], right_s[202], right_s[203], right_s[204], right_s[205], right_s[206], right_s[207], right_s[208], right_s[209], right_s[210], right_s[211], right_s[212], right_s[213], right_s[214], right_s[215], right_s[216], right_s[217], right_s[218], right_s[219], right_s[220], right_s[221], right_s[222], right_s[223], right_s[224], right_s[225], right_s[226], right_s[227], right_s[228], right_s[229], right_s[230], right_s[231], right_s[232], right_s[233], right_s[234], right_s[235], right_s[236], right_s[237], right_s[238], right_s[239], right_s[240], right_s[241], right_s[242], right_s[243], right_s[244], right_s[245], right_s[246], right_s[247], right_s[248], right_s[249], right_s[250], right_s[251], right_s[252], right_s[253], right_s[254], right_s[255], flgs_s[0], flgs_s[1], flgs_s[2], flgs_s[3], flgs_s[4], flgs_s[5], flgs_s[6], flgs_s[7], flgs_s[8], flgs_s[9], flgs_s[10], flgs_s[11], flgs_s[12], flgs_s[13], flgs_s[14], flgs_s[15], flgs_s[16], flgs_s[17], flgs_s[18], flgs_s[19], flgs_s[20], flgs_s[21], flgs_s[22], flgs_s[23], flgs_s[24], flgs_s[25], flgs_s[26], flgs_s[27], flgs_s[28], flgs_s[29], flgs_s[30], flgs_s[31], flgs_s[32], flgs_s[33], flgs_s[34], flgs_s[35], flgs_s[36], flgs_s[37], flgs_s[38], flgs_s[39], flgs_s[40], flgs_s[41], flgs_s[42], flgs_s[43], flgs_s[44], flgs_s[45], flgs_s[46], flgs_s[47], flgs_s[48], flgs_s[49], flgs_s[50], flgs_s[51], flgs_s[52], flgs_s[53], flgs_s[54], flgs_s[55], flgs_s[56], flgs_s[57], flgs_s[58], flgs_s[59], flgs_s[60], flgs_s[61], flgs_s[62], flgs_s[63], flgs_s[64], flgs_s[65], flgs_s[66], flgs_s[67], flgs_s[68], flgs_s[69], flgs_s[70], flgs_s[71], flgs_s[72], flgs_s[73], flgs_s[74], flgs_s[75], flgs_s[76], flgs_s[77], flgs_s[78], flgs_s[79], flgs_s[80], flgs_s[81], flgs_s[82], flgs_s[83], flgs_s[84], flgs_s[85], flgs_s[86], flgs_s[87], flgs_s[88], flgs_s[89], flgs_s[90], flgs_s[91], flgs_s[92], flgs_s[93], flgs_s[94], flgs_s[95], flgs_s[96], flgs_s[97], flgs_s[98], flgs_s[99], flgs_s[100], flgs_s[101], flgs_s[102], flgs_s[103], flgs_s[104], flgs_s[105], flgs_s[106], flgs_s[107], flgs_s[108], flgs_s[109], flgs_s[110], flgs_s[111], flgs_s[112], flgs_s[113], flgs_s[114], flgs_s[115], flgs_s[116], flgs_s[117], flgs_s[118], flgs_s[119], flgs_s[120], flgs_s[121], flgs_s[122], flgs_s[123], flgs_s[124], flgs_s[125], flgs_s[126], flgs_s[127], flgs_s[128], flgs_s[129], flgs_s[130], flgs_s[131], flgs_s[132], flgs_s[133], flgs_s[134], flgs_s[135], flgs_s[136], flgs_s[137], flgs_s[138], flgs_s[139], flgs_s[140], flgs_s[141], flgs_s[142], flgs_s[143], flgs_s[144], flgs_s[145], flgs_s[146], flgs_s[147], flgs_s[148], flgs_s[149], flgs_s[150], flgs_s[151], flgs_s[152], flgs_s[153], flgs_s[154], flgs_s[155], flgs_s[156], flgs_s[157], flgs_s[158], flgs_s[159], flgs_s[160], flgs_s[161], flgs_s[162], flgs_s[163], flgs_s[164], flgs_s[165], flgs_s[166], flgs_s[167], flgs_s[168], flgs_s[169], flgs_s[170], flgs_s[171], flgs_s[172], flgs_s[173], flgs_s[174], flgs_s[175], flgs_s[176], flgs_s[177], flgs_s[178], flgs_s[179], flgs_s[180], flgs_s[181], flgs_s[182], flgs_s[183], flgs_s[184], flgs_s[185], flgs_s[186], flgs_s[187], flgs_s[188], flgs_s[189], flgs_s[190], flgs_s[191], flgs_s[192], flgs_s[193], flgs_s[194], flgs_s[195], flgs_s[196], flgs_s[197], flgs_s[198], flgs_s[199], flgs_s[200], flgs_s[201], flgs_s[202], flgs_s[203], flgs_s[204], flgs_s[205], flgs_s[206], flgs_s[207], flgs_s[208], flgs_s[209], flgs_s[210], flgs_s[211], flgs_s[212], flgs_s[213], flgs_s[214], flgs_s[215], flgs_s[216], flgs_s[217], flgs_s[218], flgs_s[219], flgs_s[220], flgs_s[221], flgs_s[222], flgs_s[223], flgs_s[224], flgs_s[225], flgs_s[226], flgs_s[227], flgs_s[228], flgs_s[229], flgs_s[230], flgs_s[231], flgs_s[232], flgs_s[233], flgs_s[234], flgs_s[235], flgs_s[236], flgs_s[237], flgs_s[238], flgs_s[239], flgs_s[240], flgs_s[241], flgs_s[242], flgs_s[243], flgs_s[244], flgs_s[245], flgs_s[246], flgs_s[247], flgs_s[248], flgs_s[249], flgs_s[250], flgs_s[251], flgs_s[252], flgs_s[253], flgs_s[254], flgs_s[255], sam_s[0], sam_s[1], sam_s[2], sam_s[3], sam_s[4], sam_s[5], sam_s[6], sam_s[7], sam_s[8], sam_s[9], sam_s[10], sam_s[11], sam_s[12], sam_s[13], sam_s[14], sam_s[15], sam_s[16], sam_s[17], sam_s[18], sam_s[19], sam_s[20], sam_s[21], sam_s[22], sam_s[23], sam_s[24], sam_s[25], sam_s[26], sam_s[27], sam_s[28], sam_s[29], sam_s[30], sam_s[31], sam_s[32], sam_s[33], sam_s[34], sam_s[35], sam_s[36], sam_s[37], sam_s[38], sam_s[39], sam_s[40], sam_s[41], sam_s[42], sam_s[43], sam_s[44], sam_s[45], sam_s[46], sam_s[47], sam_s[48], sam_s[49], sam_s[50], sam_s[51], sam_s[52], sam_s[53], sam_s[54], sam_s[55], sam_s[56], sam_s[57], sam_s[58], sam_s[59], sam_s[60], sam_s[61], sam_s[62], sam_s[63], sam_s[64], sam_s[65], sam_s[66], sam_s[67], sam_s[68], sam_s[69], sam_s[70], sam_s[71], sam_s[72], sam_s[73], sam_s[74], sam_s[75], sam_s[76], sam_s[77], sam_s[78], sam_s[79], sam_s[80], sam_s[81], sam_s[82], sam_s[83], sam_s[84], sam_s[85], sam_s[86], sam_s[87], sam_s[88], sam_s[89], sam_s[90], sam_s[91], sam_s[92], sam_s[93], sam_s[94], sam_s[95], sam_s[96], sam_s[97], sam_s[98], sam_s[99], sam_s[100], sam_s[101], sam_s[102], sam_s[103], sam_s[104], sam_s[105], sam_s[106], sam_s[107], sam_s[108], sam_s[109], sam_s[110], sam_s[111], sam_s[112], sam_s[113], sam_s[114], sam_s[115], sam_s[116], sam_s[117], sam_s[118], sam_s[119], sam_s[120], sam_s[121], sam_s[122], sam_s[123], sam_s[124], sam_s[125], sam_s[126], sam_s[127], sam_s[128], sam_s[129], sam_s[130], sam_s[131], sam_s[132], sam_s[133], sam_s[134], sam_s[135], sam_s[136], sam_s[137], sam_s[138], sam_s[139], sam_s[140], sam_s[141], sam_s[142], sam_s[143], sam_s[144], sam_s[145], sam_s[146], sam_s[147], sam_s[148], sam_s[149], sam_s[150], sam_s[151], sam_s[152], sam_s[153], sam_s[154], sam_s[155], sam_s[156], sam_s[157], sam_s[158], sam_s[159], sam_s[160], sam_s[161], sam_s[162], sam_s[163], sam_s[164], sam_s[165], sam_s[166], sam_s[167], sam_s[168], sam_s[169], sam_s[170], sam_s[171], sam_s[172], sam_s[173], sam_s[174], sam_s[175], sam_s[176], sam_s[177], sam_s[178], sam_s[179], sam_s[180], sam_s[181], sam_s[182], sam_s[183], sam_s[184], sam_s[185], sam_s[186], sam_s[187], sam_s[188], sam_s[189], sam_s[190], sam_s[191], sam_s[192], sam_s[193], sam_s[194], sam_s[195], sam_s[196], sam_s[197], sam_s[198], sam_s[199], sam_s[200], sam_s[201], sam_s[202], sam_s[203], sam_s[204], sam_s[205], sam_s[206], sam_s[207], sam_s[208], sam_s[209], sam_s[210], sam_s[211], sam_s[212], sam_s[213], sam_s[214], sam_s[215], sam_s[216], sam_s[217], sam_s[218], sam_s[219], sam_s[220], sam_s[221], sam_s[222], sam_s[223], sam_s[224], sam_s[225], sam_s[226], sam_s[227], sam_s[228], sam_s[229], sam_s[230], sam_s[231], sam_s[232], sam_s[233], sam_s[234], sam_s[235], sam_s[236], sam_s[237], sam_s[238], sam_s[239], sam_s[240], sam_s[241], sam_s[242], sam_s[243], sam_s[244], sam_s[245], sam_s[246], sam_s[247], sam_s[248], sam_s[249], sam_s[250], sam_s[251], sam_s[252], sam_s[253], sam_s[254], sam_s[255], left_s[0], left_s[1], left_s[2], left_s[3], left_s[4], left_s[5], left_s[6], left_s[7], left_s[8], left_s[9], left_s[10], left_s[11], left_s[12], left_s[13], left_s[14], left_s[15], left_s[16], left_s[17], left_s[18], left_s[19], left_s[20], left_s[21], left_s[22], left_s[23], left_s[24], left_s[25], left_s[26], left_s[27], left_s[28], left_s[29], left_s[30], left_s[31], left_s[32], left_s[33], left_s[34], left_s[35], left_s[36], left_s[37], left_s[38], left_s[39], left_s[40], left_s[41], left_s[42], left_s[43], left_s[44], left_s[45], left_s[46], left_s[47], left_s[48], left_s[49], left_s[50], left_s[51], left_s[52], left_s[53], left_s[54], left_s[55], left_s[56], left_s[57], left_s[58], left_s[59], left_s[60], left_s[61], left_s[62], left_s[63], left_s[64], left_s[65], left_s[66], left_s[67], left_s[68], left_s[69], left_s[70], left_s[71], left_s[72], left_s[73], left_s[74], left_s[75], left_s[76], left_s[77], left_s[78], left_s[79], left_s[80], left_s[81], left_s[82], left_s[83], left_s[84], left_s[85], left_s[86], left_s[87], left_s[88], left_s[89], left_s[90], left_s[91], left_s[92], left_s[93], left_s[94], left_s[95], left_s[96], left_s[97], left_s[98], left_s[99], left_s[100], left_s[101], left_s[102], left_s[103], left_s[104], left_s[105], left_s[106], left_s[107], left_s[108], left_s[109], left_s[110], left_s[111], left_s[112], left_s[113], left_s[114], left_s[115], left_s[116], left_s[117], left_s[118], left_s[119], left_s[120], left_s[121], left_s[122], left_s[123], left_s[124], left_s[125], left_s[126], left_s[127], left_s[128], left_s[129], left_s[130], left_s[131], left_s[132], left_s[133], left_s[134], left_s[135], left_s[136], left_s[137], left_s[138], left_s[139], left_s[140], left_s[141], left_s[142], left_s[143], left_s[144], left_s[145], left_s[146], left_s[147], left_s[148], left_s[149], left_s[150], left_s[151], left_s[152], left_s[153], left_s[154], left_s[155], left_s[156], left_s[157], left_s[158], left_s[159], left_s[160], left_s[161], left_s[162], left_s[163], left_s[164], left_s[165], left_s[166], left_s[167], left_s[168], left_s[169], left_s[170], left_s[171], left_s[172], left_s[173], left_s[174], left_s[175], left_s[176], left_s[177], left_s[178], left_s[179], left_s[180], left_s[181], left_s[182], left_s[183], left_s[184], left_s[185], left_s[186], left_s[187], left_s[188], left_s[189], left_s[190], left_s[191], left_s[192], left_s[193], left_s[194], left_s[195], left_s[196], left_s[197], left_s[198], left_s[199], left_s[200], left_s[201], left_s[202], left_s[203], left_s[204], left_s[205], left_s[206], left_s[207], left_s[208], left_s[209], left_s[210], left_s[211], left_s[212], left_s[213], left_s[214], left_s[215], left_s[216], left_s[217], left_s[218], left_s[219], left_s[220], left_s[221], left_s[222], left_s[223], left_s[224], left_s[225], left_s[226], left_s[227], left_s[228], left_s[229], left_s[230], left_s[231], left_s[232], left_s[233], left_s[234], left_s[235], left_s[236], left_s[237], left_s[238], left_s[239], left_s[240], left_s[241], left_s[242], left_s[243], left_s[244], left_s[245], left_s[246], left_s[247], left_s[248], left_s[249], left_s[250], left_s[251], left_s[252], left_s[253], left_s[254], left_s[255]) begin: JP_PROCESS_JPEG_LOGIC
    integer i;
    if (update_s) begin
        noupdate_s = 0;
        for (i=0; i<256; i=i+1) begin
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
