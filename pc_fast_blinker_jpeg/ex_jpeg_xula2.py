
from pprint import pprint

import rhea.build as build
from rhea.build.boards import get_board
from test_boards import led_port_pin_map
#from blink import blinky
from test_top import dwt_top


def run_xula():
    brd = get_board('xula2')
    brd.device = 'XC6SLX9'
 
    '''testing connecting signals to gpio on RPi2B
    CAT-Board
    si3 T8 #BCM8	CHAN8	J14	
    ld R10 #BCM27	CHAN27	E2
    reset T2 BCM26	CHAN0	R7
    fB3 T9 #BCM24	CHAN10	F16
    ss0 P9 #BCM23	CHAN11	C16 
    fB0 R4 #BCM16	CHAN3	M15
    si0 R5 #BCM13	CHAN4	M16
    fB1 R6 BCM12	CHAN6	K16
    fB2 T7 #BCM7	CHAN7	J16
    si1 T5 #BCM6	CHAN5	K15
    si2 T6 #BCM5	CHAN22	H1
    pp0 R9 #BCM4	CHAN29 	B1
    '''
    #CHAN8
    brd.add_port('reset', 'J14', pullup=True)
    #CHAN27
    brd.add_port('si0', 'E2', pullup=True)
    #CHAN0
    brd.add_port('fB0', 'R7', pullup=True)
    #CHAN10
    brd.add_port('si1', 'F16', pullup=True)
    #CHAN11
    brd.add_port('fB1', 'C16', pullup=True)
    #CHAN3
    brd.add_port('si2', 'M15', pullup=True)
    #CHAN4
    brd.add_port('fB2', 'M16', pullup=True)
    #CHAN6
    brd.add_port('si3', 'K16', pullup=True)
    #CHAN7
    brd.add_port('fB3', 'J16', pullup=True)
    #CHAN5
    brd.add_port('pp0', 'K15')
    #CHAN22
    brd.add_port('ss0', 'H1', pullup=True)
    #CHAN29
    brd.add_port('ld', 'B1')
    flow = build.flow.ISE(brd=brd, top=dwt_top)
    flow.run()
    info = flow.get_utilization()
    pprint(info)

 


if __name__ == '__main__':
    run_xula()
