from myhdl import *
from multi_jpeg import *
from rom import *
from jpfifo import *
def tb(clk_fast, sig0_in_x, noupdate0_s, res0_s,
        sig1_in_x, noupdate1_s, res1_s,
        sig2_in_x, noupdate2_s, res2_s,
        sig3_in_x, noupdate3_s, res3_s,
        sig4_in_x, noupdate4_s, res4_s,
        sig5_in_x, noupdate5_s, res5_s,
        sig6_in_x, noupdate6_s, res6_s,
        sig7_in_x, noupdate7_s, res7_s,
        sig8_in_x, noupdate8_s, res8_s,
        sig9_in_x, noupdate9_s, res9_s,
        sig10_in_x, noupdate10_s, res10_s,
        sig11_in_x, noupdate11_s, res11_s,
        sig12_in_x, noupdate12_s, res12_s,
        sig13_in_x, noupdate13_s, res13_s,
        sig14_in_x, noupdate14_s, res14_s,
        sig15_in_x, noupdate15_s, res15_s,
        dout_rom, addr_rom_r, CONTENT,empty_r,full_r, enr_r, enw_r, dataout_r, datain_r):
    
    instance_1 = rom(dout_rom, addr_rom_r, CONTENT)
    instance_2 = jpegfifo(clk_fast, empty_r, full_r, enr_r, enw_r, dataout_r, datain_r )
    instance_3 = multi_jpeg(clk_fast, sig0_in_x, noupdate0_s, res0_s,
               sig1_in_x, noupdate1_s, res1_s,
               sig2_in_x, noupdate2_s, res2_s,
               sig3_in_x, noupdate3_s, res3_s,
               sig4_in_x, noupdate4_s, res4_s,
               sig5_in_x, noupdate5_s, res5_s,
               sig6_in_x, noupdate6_s, res6_s,
               sig7_in_x, noupdate7_s, res7_s,
               sig8_in_x, noupdate8_s, res8_s,
               sig9_in_x, noupdate9_s, res9_s,
               sig10_in_x, noupdate10_s, res10_s,
               sig11_in_x, noupdate11_s, res11_s,
               sig12_in_x, noupdate12_s, res12_s,
               sig13_in_x, noupdate13_s, res13_s,
               sig14_in_x, noupdate14_s, res14_s,
               sig15_in_x, noupdate15_s, res15_s)
    @always(delay(10))
    def clkgen():
        clk_fast.next = not clk_fast
    @instance
    def stimulus():
        for i in range(10):
           yield clk_fast.posedge 
        while(empty_x == 0):
            #print("%3d wait for empty") % (now())
            yield clk_fast.posedge
        addr_rom_r.next = 0
        enw_r.next = 1
        #print("%3d %d") % (now(), enw_r)
        yield clk_fast.posedge
        print("%3d %d") % (now(), enw_r)
        for i in range(30):
            datain_x.next = dout_rom
            addr_rom_r.next = addr_rom_r + 1
            
            #print("%3d %d %s ") % (now(), addr_rom_r, bin(dout_rom))
            yield clk_fast.posedge
        enw_r.next = 0
        enr_r.next = 1
        for i in range(30):
            print("%3d %d %s ") % (now(), (res0_s), bin(sig0_in_x))
            sig0_in_x.next = dataout_x
            yield clk_fast.posedge
            
        raise StopSimulation
    
    return instance_1, instance_2, instance_3, stimulus, clkgen
tb_fsm = traceSignals(tb, clk_fast, sig0_in_x, noupdate0_s, res0_s,
        sig1_in_x, noupdate1_s, res1_s,
        sig2_in_x, noupdate2_s, res2_s,
        sig3_in_x, noupdate3_s, res3_s,
        sig4_in_x, noupdate4_s, res4_s,
        sig5_in_x, noupdate5_s, res5_s,
        sig6_in_x, noupdate6_s, res6_s,
        sig7_in_x, noupdate7_s, res7_s,
        sig8_in_x, noupdate8_s, res8_s,
        sig9_in_x, noupdate9_s, res9_s,
        sig10_in_x, noupdate10_s, res10_s,
        sig11_in_x, noupdate11_s, res11_s,
        sig12_in_x, noupdate12_s, res12_s,
        sig13_in_x, noupdate13_s, res13_s,
        sig14_in_x, noupdate14_s, res14_s,
        sig15_in_x, noupdate15_s, res15_s,
        dout_rom, addr_rom_r, CONTENT,empty_r,full_r, enr_r, enw_r, dataout_r, datain_r)   
sim = Simulation(tb(clk_fast, sig0_in_x, noupdate0_s, res0_s,
        sig1_in_x, noupdate1_s, res1_s,
        sig2_in_x, noupdate2_s, res2_s,
        sig3_in_x, noupdate3_s, res3_s,
        sig4_in_x, noupdate4_s, res4_s,
        sig5_in_x, noupdate5_s, res5_s,
        sig6_in_x, noupdate6_s, res6_s,
        sig7_in_x, noupdate7_s, res7_s,
        sig8_in_x, noupdate8_s, res8_s,
        sig9_in_x, noupdate9_s, res9_s,
        sig10_in_x, noupdate10_s, res10_s,
        sig11_in_x, noupdate11_s, res11_s,
        sig12_in_x, noupdate12_s, res12_s,
        sig13_in_x, noupdate13_s, res13_s,
        sig14_in_x, noupdate14_s, res14_s,
        sig15_in_x, noupdate15_s, res15_s,
        dout_rom, addr_rom_r, CONTENT,empty_r,full_r, enr_r, enw_r, dataout_r, datain_r))
def jp(clk_fast, sig0_in_x, noupdate0_s, res0_s,
        sig1_in_x, noupdate1_s, res1_s,
        sig2_in_x, noupdate2_s, res2_s,
        sig3_in_x, noupdate3_s, res3_s,
        sig4_in_x, noupdate4_s, res4_s,
        sig5_in_x, noupdate5_s, res5_s,
        sig6_in_x, noupdate6_s, res6_s,
        sig7_in_x, noupdate7_s, res7_s,
        sig8_in_x, noupdate8_s, res8_s,
        sig9_in_x, noupdate9_s, res9_s,
        sig10_in_x, noupdate10_s, res10_s,
        sig11_in_x, noupdate11_s, res11_s,
        sig12_in_x, noupdate12_s, res12_s,
        sig13_in_x, noupdate13_s, res13_s,
        sig14_in_x, noupdate14_s, res14_s,
        sig15_in_x, noupdate15_s, res15_s,
        dout_rom, addr_rom_r, CONTENT,empty_r,full_r, enr_r, enw_r, dataout_r, datain_r):
    instance_1 = rom(dout_rom, addr_rom_r, CONTENT)
    instance_2 = jpegfifo(clk_fast, empty_r, full_r, enr_r, enw_r, dataout_r, datain_r )
    instance_3 = multi_jpeg(clk_fast, sig0_in_x, noupdate0_s, res0_s,
               sig1_in_x, noupdate1_s, res1_s,
               sig2_in_x, noupdate2_s, res2_s,
               sig3_in_x, noupdate3_s, res3_s,
               sig4_in_x, noupdate4_s, res4_s,
               sig5_in_x, noupdate5_s, res5_s,
               sig6_in_x, noupdate6_s, res6_s,
               sig7_in_x, noupdate7_s, res7_s,
               sig8_in_x, noupdate8_s, res8_s,
               sig9_in_x, noupdate9_s, res9_s,
               sig10_in_x, noupdate10_s, res10_s,
               sig11_in_x, noupdate11_s, res11_s,
               sig12_in_x, noupdate12_s, res12_s,
               sig13_in_x, noupdate13_s, res13_s,
               sig14_in_x, noupdate14_s, res14_s,
               sig15_in_x, noupdate15_s, res15_s)
    return instance_1, instance_2, instance_3

toVHDL(jp, clk_fast, sig0_in_x, noupdate0_s, res0_s,
        sig1_in_x, noupdate1_s, res1_s,
        sig2_in_x, noupdate2_s, res2_s,
        sig3_in_x, noupdate3_s, res3_s,
        sig4_in_x, noupdate4_s, res4_s,
        sig5_in_x, noupdate5_s, res5_s,
        sig6_in_x, noupdate6_s, res6_s,
        sig7_in_x, noupdate7_s, res7_s,
        sig8_in_x, noupdate8_s, res8_s,
        sig9_in_x, noupdate9_s, res9_s,
        sig10_in_x, noupdate10_s, res10_s,
        sig11_in_x, noupdate11_s, res11_s,
        sig12_in_x, noupdate12_s, res12_s,
        sig13_in_x, noupdate13_s, res13_s,
        sig14_in_x, noupdate14_s, res14_s,
        sig15_in_x, noupdate15_s, res15_s,
        dout_rom, addr_rom_r, CONTENT,empty_r,full_r, enr_r, enw_r, dataout_r, datain_r)
sim = Simulation(tb_fsm)
sim.run()