module tb_eq_d_c1;

initial 
 begin
    $dumpfile("tb_eq_d_c1.vcd");
    $dumpvars(0,tb_eq_d_c1);
 end

/* Make a regular pulsing clock. */
  reg clk = 0;
  always #5 clk = !clk;

initial begin
     # 17 x2 = 205;
     # 15 x3 = 207;
     # 14 x4 = 179;

     # 19 x2 = 215;
     # 17 x3 = 190;
     # 16 x4 = 214; 

     # 21 x2 = 178;
     # 19 x3 = 201;
     # 18 x4 = 169; 

     # 30 x2 = 121;
     # 28 x3 = 139;
     # 27 x4 = 164;

     # 40 x2 = 92;
     # 38 x3 = 205;
     # 37 x4 =  139;
     
     # 100 $stop;
end 
  
wire [18:0] d3;
wire [18:0] a2;

reg [18:0] x2;
reg [18:0] x3;
reg [18:0] x4;

 

eq_d_c1 dut(
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
