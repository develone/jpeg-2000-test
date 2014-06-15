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
reg [18:0] x5;

initial begin
     # 10 x2 = 164;
     # 20 x3 = 164;
     # 30 x4 = 164;
     # 40 x5 = 164;
     # 50 x2 = 156;
     # 60 x3 = 148;	
     # 70 x4 = 112;
     # 80 x5 = 132;
     # 200 $stop; 

end

add_shift dut(
    d3,
    a2,
    x2,
    x3,
    x4,
    x5
);

initial
     $monitor("At time %t, d3  = %h (%0d) ,a2  = %h (%0d)",
              $time, d3, d3,a2,a2);
endmodule
