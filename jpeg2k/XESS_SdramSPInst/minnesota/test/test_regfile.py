#
# Copyright (c) 2006-2013 Christopher L. Felton
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from pprint import pprint
from collections import OrderedDict
from random import randint

from myhdl import *
from myhdl_tools import Clock,Reset

from mn.system import RegisterFile
from mn.system import Register
from mn.system import Wishbone
from mn.system import RWData

from _test_utils import *

regdef = None

def _create_mask(n):
    m = 1
    for _ in xrange(n):
        m = (m << 1) | 1
    return m

def _create_test_regfile():
    global regdef
    regdef = OrderedDict()
    # --register 0--
    reg = Register('reg0',0x0018,8,'rw',0)
    reg.comment = "register 0"
    reg.add_bits('enable', slice(1,0))
    reg.add_bits('loop', slice(2,1))
    regdef[reg.name] = reg
    
    # -- more registers register --
    for addr,default in zip((0x20,0x40,0x80),
                            (0xDE,0xCA,0xFB)):
        reg = Register('reg%s'%(addr),addr,8,'rw',default)
        regdef[reg.name] = reg

    # -- read only register --
    reg = Register('regro',0x100,8,'ro',0xAA)
    regdef[reg.name] = reg

    regfile = RegisterFile(regdef)
    return regfile

def m_per_top(clock,reset,mon):
    wb = Wishbone(clock,reset)
    #gpm = wb.m_controller(wb)
    gp1 = m_per(clock,reset,wb,mon)
    return gp1

def m_per(clock,reset,regbus,mon):
    regfile = _create_test_regfile()
    g_regfile = regfile.m_per_interface(clock,reset,regbus)

    ## all "read-only" (status) bits if needed
    @always_seq(clock.posedge,reset=reset)
    def rtl_roregs():
        if regfile.regro.rd:
            regfile.regro.next = mon
        
    return g_regfile #, rtl_roregs

def test_register_def():
    regfile = _create_test_regfile()
    #pprint(vars(regfile))
    assert len(regfile._rwregs) == 4
    assert len(regfile._roregs) == 1

def test_register_file():

    # top-level signals and interfaces
    clock = Clock(0, frequency=50e6)
    reset = Reset(0,active=1,async=False)
    regbus = Wishbone(clock,reset) 

    def _test_rf():
        tb_dut = m_per(clock,reset,regbus,0xAA)
        tb_or = regbus.m_per_outputs()
        tb_mclk = clock.gen()
        tb_rclk = regbus.clk_i.gen()
        rwd = RWData()
        asserr = Signal(bool(0))
        
        @instance
        def tb_stim():
            try:
                yield delay(100)
                yield reset.pulse(111)

                for k,reg in regdef.iteritems():
                    #pprint(vars(reg))
                    if reg.access == 'ro':
                        yield regbus.read(reg.addr,rwd)
                        assert rwd.rval == reg.default, "ro: %02x != %02x"%(rwd.rval,reg.default)
                    else:
                        rwd.wval = randint(0,(2**reg.width)-1)
                        yield regbus.write(reg.addr,rwd)
                        for _ in xrange(4):
                            yield clock.posedge
                        yield regbus.read(reg.addr,rwd)
                        assert rwd.rval == rwd.wval, "rw: %02x != %02x"%(rwd.rval,rwd.wval)
                
                yield delay(100)
            except AssertionError,err:
                asserr.next = True
                for _ in xrange(10):
                    yield clock.posedge
                raise err

            raise StopSimulation

        return tb_mclk,tb_stim,tb_dut,tb_or,tb_rclk

    tb_clean_vcd('_test_rf')
    g = traceSignals(_test_rf)
    Simulation(g).run()
    
def test_convert():
    clock = Clock(0,frequency=50e6)
    reset = Reset(0,active=1,async=False)
    mon = Signal(intbv(0)[8:])
    toVerilog(m_per_top,clock,reset,mon)
    
if __name__ == '__main__':
    #parser = tb_arparser()
    #args = parser.parse_args()
    
    test_register_def()
    test_register_file()
    test_convert()
    

