
from pprint import pprint

import rhea.build as build
from rhea.build.boards import get_board
from test_boards import led_port_pin_map
#from blink import blinky
from test_top import dwt_top


def run_xula():
    brd = get_board('xula2')
    brd.device = 'XC6SLX9'
    brd.add_port_name(**led_port_pin_map['xula2'])
    '''testing connecting signals to the PM2 & PM3 connectors on
    CAT-Board
    '''
    #PM2-A1
    brd.add_port('reset', 'T4')
    #PM3-A1
    brd.add_port('si0', 'H2')
    #PM3-B1
    brd.add_port('fB0', 'F1')
    #PM3-A2
    brd.add_port('si1', 'F2')
    #PM3-B2
    brd.add_port('fB1', 'E1')
    #PM3-A3
    brd.add_port('si2', 'E2')
    #PM3-B3
    brd.add_port('fB2', 'C1')
    #PM3-A4
    brd.add_port('si3', 'B1')
    #PM3-B4
    brd.add_port('fB3', 'R2')
    #PM2-B1
    brd.add_port('pp0', 'R1')
    #PM2-A2
    brd.add_port('ss0', 'M2')
    #PM2-A3
    brd.add_port('ld', 'M1')
    flow = build.flow.ISE(brd=brd, top=dwt_top)
    flow.run()
    info = flow.get_utilization()
    pprint(info)

    # get a board to implement the design on
    brd = get_board('xula2')
    brd.device = 'XC6SLX9'
    brd.add_port_name(**led_port_pin_map['xula2'])
    '''testing connecting signals to the PM2 & PM3 connectors on
    CAT-Board
    '''
    #PM2-A1
    brd.add_port('reset', 'T4')
    #PM3-A1
    brd.add_port('si0', 'H2')
    #PM3-B1
    brd.add_port('fB0', 'F1')
    #PM3-A2
    brd.add_port('si1', 'F2')
    #PM3-B2
    brd.add_port('fB1', 'E1')
    #PM3-A3
    brd.add_port('si2', 'E2')
    #PM3-B3
    brd.add_port('fB2', 'C1')
    #PM3-A4
    brd.add_port('si3', 'B1')
    #PM3-B4
    brd.add_port('fB3', 'R2')
    #PM2-B1
    brd.add_port('pp0', 'R1')
    #PM2-A2
    brd.add_port('ss0', 'M2')
    #PM2-A3
    brd.add_port('ld', 'M1')
    flow = build.flow.ISE(brd=brd, top=dwt_top)
    flow.run()
    info = flow.get_utilization()
    pprint(info)


if __name__ == '__main__':
    run_xula()
