# MIT license
# 
# Copyright (C) 2015 by XESS Corp.
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import rhea.build as build
from rhea.build.boards import get_board
#from led_digits_display import led_digits_cnt, led_digits_scroll
from test_top import dwt_top


def run_catboard():
    # Get the CAT Board object.
    brd = get_board('catboard')
    '''testing connecting signals to the PM2 & PM3 connectors on
    CAT-Board
    '''
    #PM2-A1
    brd.add_port('reset', 'A1')
    #PM3-A1
    brd.add_port('si0', 'A11')
    #PM3-B1
    brd.add_port('fB0', 'B10')
    #PM3-A2
    brd.add_port('si1', 'B12')
    #PM3-B2
    brd.add_port('fB1', 'B11')
    #PM3-A3
    brd.add_port('si2', 'B14')
    #PM3-B3
    brd.add_port('fB2', 'B13')
    #PM3-A4
    brd.add_port('si3', 'B15')
    #PM3-B4
    brd.add_port('fB3', 'A15')
    #PM2-B1
    brd.add_port('pp0', 'A2')
    #PM2-A2
    brd.add_port('ss0', 'B3')
    #PM2-A3
    brd.add_port('ld', 'B5')
    flow = brd.get_flow(top=dwt_top)
    flow.run()


if __name__ == '__main__':
    run_catboard()
