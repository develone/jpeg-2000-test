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
    '''testing connecting signals to gpio on RPi2B
    CAT-Board
    si3 T8 #BCM8
    ld R10 #BCM27
    reset T2 BCM26
    fB3 T9 #BCM24
    ss0 P9 #BCM23
    fB0 R4 #BCM16
    si0 R5 #BCM13
    fB1 R6 BCM12
    fB2 T7 #BCM7
    si1 T5 #BCM6
    si2 T6 #BCM5
    pp0 R9 #BCM4 
    '''
    #BCM26
    brd.add_port('reset', 'T2')
    #BCM13
    brd.add_port('si0', 'R5')
    #BCM16
    brd.add_port('fB0', 'R4')
    #PM3-A2
    #BCM6
    brd.add_port('si1', 'T5')
    #BCM12
    brd.add_port('fB1', 'R6')
    #BCM5
    brd.add_port('si2', 'T6')
    #BCM7
    brd.add_port('fB2', 'T7')
    #BCM8
    brd.add_port('si3', 'T8')
    #BCM24
    brd.add_port('fB3', 'T9')
    #BCM4
    brd.add_port('pp0', 'R9')
    #BCM23
    brd.add_port('ss0', 'P9')
    #BCM27
    brd.add_port('ld', 'R10')
    flow = brd.get_flow(top=dwt_top)
    flow.run()


if __name__ == '__main__':
    run_catboard()
