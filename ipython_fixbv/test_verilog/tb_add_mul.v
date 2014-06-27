module tb_add_mul;
initial begin
    $dumpfile("tb_add_mul.vcd");
    $dumpvars(0,tb_add_mul);
end

/* Make a regular pulsing clock. */
  reg clk = 0;
  always #5 clk = !clk;
wire [23:0] d3;
wire [23:0] a2; 

reg [23:0] x2;
reg [23:0] x3;
reg [23:0] x4;
reg [23:0] x5;
reg p;
reg even_odd;
reg fwd_inv;

initial begin

     # 10 p = 0;
     # 10 even_odd = 0;
     # 10 fwd_inv = 1;
     # 13 x2 = 80;
     # 13 x3 = 120;
     # 13 x4 = 164;
     # 13 x5 = 164;
     # 30 p = 0;
     # 30 even_odd = 0;
     # 30 fwd_inv = 1;
     # 30 x2 = 80;
     # 30 x3 = 120;	
     # 30 x4 = 164;
     # 30 x5 = 164;
     # 40 p = 0;
     # 40 even_odd = 0;
     # 40 fwd_inv = 1;
     # 40 x2 = 80;
     # 40 x3 = 120;	
     # 40 x4 = 164;
     # 40 x5 = 164;
     # 50 p = 0;
     # 50 even_odd = 1;
     # 50 fwd_inv = 1;
     # 50 x2 = 164;
     # 50 x3 = 164;	
     # 50 x4 = 164;
     # 50 x5 = 164;

     # 200 $stop;    
end 

add_mul dut(
    d3,
    a2,
    clk,
    x2,
    x3,
    x4,
    x5,
    p,
    even_odd,
    fwd_inv
);

initial
     $monitor("At time %t, d3  = %h (%0d) ,a2  = %h (%0d)",
              $time, d3, d3,a2,a2);
endmodule
