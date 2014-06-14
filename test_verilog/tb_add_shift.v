module tb_add_shift;

initial begin
    $dumpfile("tb_add_shift.vcd");
    $dumpvars(0,tb_add_shift);
 end
wire [18:0] d3;
wire [18:0] a2;
reg [18:0] x2;
reg [18:0] x3;
reg [18:0] x4;

initial begin
     # 17 x2 = 164;
     # 17 x3 = 164;
     # 17 x4 = 164;
     # 20 x2 = 164;
     # 20 x3 = 156;
     # 20 x4 = 148;	
     # 17 x2 = 112;
     # 17 x3 = 132;
     # 17 x4 = 142;
     # 100 $stop; 

end

add_shift dut(
    d3,
    a2,
    x2,
    x3,
    x4
);

initial
     $monitor("At time %t, d3  = %h (%0d) ,a2  = %h (%0d)",
              $time, d3, d3,a2,a2);
endmodule
