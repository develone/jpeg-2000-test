module tb_eq_d_c2;

initial 
 begin
    $dumpfile("tb_eq_d_c2.vcd");
    $dumpvars(0,tb_eq_d_c2);
 end

/* Make a regular pulsing clock. */
  reg clk = 0;
  always #5 clk = !clk;

initial begin
     # 17 x2 = 4;
     # 15 x3 = 32;
     # 14 x4 = 66;

     # 19 x2 = 68;
     # 17 x3 = 19;
     # 16 x4 = 524283; 

     # 21 x2 = 524247;
     # 19 x3 = 4;
     # 18 x4 = 36; 

     # 30 x2 = 524246;
     # 28 x3 = 244;
     # 27 x4 = 164;

     # 40 x2 = 92;
     # 38 x3 = 116;
     # 37 x4 =  92;
     
     # 100 $stop;
end 
  
wire [18:0] d3;
wire [18:0] a2;

reg [18:0] x2;
reg [18:0] x3;
reg [18:0] x4;

 

eq_d_c2 dut(
    d3,
    a2,
    clk,
    x2,
    x3,
    x4
);

initial
     $monitor("At time %t, d3  = %h (%0d) ,a2  = %h (%0d)",
              $time, d3, d3,a2,a2);

 
endmodule
