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

from argparse import Namespace

from myhdl import *
from myhdl._Signal import _Signal

_width = None

class RegisterBits(object):
    def __init__(self,name,slc,comment=""):
        self.name = name     # name of the bits
        self.b = slc         #
        self.comment = comment

    def __getitem__(self,k):
        return self.__dict__[k]

class Register(_Signal):
    def __init__(self,name,addr,width,access='rw',default=0,comment=""):
        global _width
        # the register read and write strobes to the
        # peripheral
        _Signal.__init__(self,intbv(default)[width:])
        self.wr = Signal(bool(0))
        self.rd = Signal(bool(0))

        self.name = name
        self.addr = addr
        self.width = width
        self.access = access
        self.default = default
        self.comment = comment
        self.bits = {}

        if _width is None:
            _width = width
        else:
            assert width == _width, "All registers must be the same width"

    def add_bits(self,name,slc,comment=""):
        bits = RegisterBits(name,slc,comment)
        self.bits[bits.name] = bits
        self.__dict__[bits.name] = bits
            
class RegisterFile(object):

    def __init__(self,regdef,args=None):
        """
        regdef : register file dictionary definition
        args : arguments for the register file and register
               bus interface

        The register file is 
        """
        self._rwregs = []
        self._roregs = []
        self._regdef = regdef
        self._allregs = None
        
        for k,v in regdef.iteritems():
            if isinstance(v,dict):
                # @todo: _check_register_def
                # v = Register(v['name'],...)
                raise NotImplementedError("dict description TBC");
            if not isinstance(v,Register):
                raise ValueError("Invalid type in regdef %s"%(type(v)))
                                 
            self.__dict__[k] = v
            if v.access == 'rw':  # @todo: remove or v['access'] == 'wt':
                self._rwregs.append((v.addr,v,))
            elif v.access == 'ro':
                self._roregs.append((v.addr,v,))

            # create a signal for all the bits, note the bits
            # in a modules register file must have unique names
            for kb,vb in v.bits.iteritems():
                if self.__dict__.has_key(kb):
                    raise StandardError("bit(s) name, %s, already exists"%(kb))
                self.__dict__[kb] = v(vb.b)

    def get_reglist(self):
        """ return a list of addresses and a list of registers.        
        """
        rwa = [aa for aa,rr in self._rwregs]
        rwr = [rr for aa,rr in self._rwregs]
        _rrw = [False for aa,rr in self._rwregs]
        roa = [aa for aa,rr in self._roregs]
        ror = [rr for aa,rr in self._roregs]
        _rro = [True for aa,rr in self._rwregs]
        self._allregs = rwr+ror
        dl = [rr.default for aa,rr in self._rwregs+self._roregs]
        #@todo: order the list from low address to high address
        #@todo: set flag if addresses are contiguous
        return (tuple(rwa+roa),rwr+ror,tuple(_rrw+_rro),tuple(dl))

    def get_strobelist(self):
        assert self._allregs is not None
        wr = [rr.wr for rr in self._allregs]
        rd = [rr.rd for rr in self._allregs]
        return wr,rd

    def get_readonly(self,name=None,addr=None):
        roreg = None
        if name is not None:
            addr = self._regdef[name].addr
        assert addr is not None
        for aa,rr in self._roregs:
            print(aa,rr)
            if addr == aa:
                roreg = rr
                break
        assert roreg is not None, "Invalid register %s %x"%(name,addr)
        return roreg
    
    def m_per_interface(self, clock, reset, regbus,
                        args = None,
                        base_address = 0x00):
        """
        The register bus access to the register file, external
        to the module reads and writes.
        """
        busi = regbus.m_per_interface(clock, reset, self, args=args,
                                      base_address=base_address)
        
        #if isinstance(regbus,wishbone.Wishbone):
        #    busmod = wishbone.m_regbus_interface
        #elif isinstance(regbus.avalon.Avalon):
        #    busmod = avalon.m_regbus_interface
        #else:
        #    raise StandardError("unsupport memory-map bus type %s"%(type(regbus)))
        #    
        #busi = busmod(clock, reset, regbus,
        #              self, args,
        #              base_address=base_address,
        #              )
        return busi
        
