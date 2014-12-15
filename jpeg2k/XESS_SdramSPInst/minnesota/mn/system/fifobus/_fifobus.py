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

_fb_num = 0
_fb_list = {}

def _add_bus(fb,args=None):
    """ globally keep track of all the busses added.
    """
    global _fb_num, _fb_list
    _fb_num += 1
    _fb_list[args.name] = fb

class FIFOBus(object):
    def __init__(self,args=None):
        # @todo: ?? not sure if this how the arguments should
        #        should be handled.  Passing args is simple but a
        #        little obscure ??
        if args is None:
            args = Namespace(name='fifobus%d'%(_fb_num),
                             width=8,  # fifobus data width
                             size=128  # depth of the fifo
                             )

        # all the data signals are from the perspective
        # of the FIFO being interfaced to.
        self.wr = Signal(bool(0))       # write strobe to fifo
        self.di = Signal(intbv(0)[8:])  # fifo data in
        self.rd = Signal(bool(0))       # fifo read strobe
        self.do = Signal(intbv(0)[8:])  # fifo data out
        self.empty = Signal(bool(0))    # fifo empty
        self.full = Signal(bool(0))     # fifo full

        self.width = args.width
        self.size = args.size

        _add_bus(self,args)
