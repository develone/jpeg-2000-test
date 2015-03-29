from __future__ import division
from __future__ import print_function

import sys
import os
import random
import datetime
import argparse
from argparse import Namespace

from PIL import Image
from myhdl import *

#from _jpeg_prep_cosim import prep_cosim
# the interfaces to the encoders
from _jpeg_2k_intf import JPEGEnc2k
def runbench(args):

    clk_fast = Signal(bool(0))
    reset = ResetSignal(1, active=1, async=True)

 
    jpg2k = JPEGEnc2k(clk_fast, reset, args=args)
 
 
    '''
    # prepare the cosimulation
    #tbdut = prep_cosim(clk_fast, reset, jpg2k, args=args)

    # save the bitstreams here
    v1_bic,v2_bic = [None],[None]
    
    # clock generator (20 tick period)
    @always(delay(10))
    def tbclk():
        clk_fast.next = not clk_fast

    
    def _dump_bitstreams(v1_bic, v2_bic, args):
        """ dump the retrieved bitstreams
        """
        v1_non_zero = False
        for bb in v1_bic:
            if bb != 0:
                v1_non_zero = True

        print("V1 bitstream, len %d (more than zeros %s)" % (len(v1_bic),v1_non_zero,))
        for ii,bb in enumerate(v1_bic):
            print("  [%6d]  %08X" % (ii, int(bb),))
            if ii > 4 and not args.dump_bitstreams:
                break;
        print("V1 max frame rate %8.3f @ %s" % (jpgv1.max_frame_rate, str(jpgv2.img_size),))

        print("V2 bitstream, len %d" % (len(v2_bic),))
        for ii,bb in enumerate(v2_bic):
            print("  [%6d]  %08X" % (ii, int(bb),))
            if ii > 4 and not args.dump_bitstreams:
                break
        print("V2 max frame rate %8.3f @ %s" % (jpgv2.max_frame_rate, str(jpgv2.img_size),))

    
    def _test():
        # get the bus adapters to the encoders
        tbintf = (jpgv1.get_gens(), jpgv2.get_gens(),)
        finished = [Signal(bool(0)) for _ in range(2)]

        # open the image for testing
        img = Image.open(args.imgfn)

        def _pulse_reset():
            reset.next = reset.active
            yield delay(13)
            reset.next = reset.active
            yield delay(113)
            reset.next = not reset.active
            yield delay(13)
            yield clock.posedge

        @instance
        def tbstim():
            print("start simulation ...")
            yield _pulse_reset()

            wait = True
            while wait:
                if False in finished:
                    yield delay(100)
                else:
                    wait = False

            for ii in range(100):
                yield clock.posedge

            if not args.no_wait:
                _dump_bitstreams(v1_bic[0], v2_bic[0], args)


            end_time = datetime.datetime.now()
            dt = end_time - args.start_time
            print("end simulation %s" % (dt,))
            raise StopSimulation

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # stimulate V1 (design1)
        @instance
        def tbstimv1():
            yield delay(100)
            while reset == reset.active:
                yield delay(10)
            yield delay(100)
            yield clock.posedge

            # initialize the JPEG encoder
            yield jpgv1.initialize()
            # send and image to be encoded
            yield jpgv1.put_image(img)

            # no_wait indicates to stream the input and exit,
            # don't wait the encoder to finish
            if args.no_wait:
                while not jpgv1.pxl_done:
                    yield delay(1000)
                    yield clock.posedge
                    # this is a debug mode, after all pixles streamed
                    # in continue simulation for some period of time ...
                    for _ in range(600):
                        yield delay(1000)
            else:
                yield jpgv1.get_jpeg(v1_bic)

            finished[0].next = True

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # stimulate V2 (design2)
        @instance
        def tbstim2k():
            yield delay(100)
            while reset == reset.active:
                yield delay(10)
            yield delay(100)
            yield clock.posedge

            yield jpg2k.put_image(img)

            # no_wait indicates to stream the input and exit,
            # don't wait the encoder to finish
            if args.no_wait:
                while not jpg2k.pxl_done:
                    yield delay(1000)
                    yield clock.posedge
                for _ in range(100):
                    yield delay(100)
            else:
                yield jpg2k.get_jpeg(v2_bic)

            finished[1].next = True

        return tbclk, tbstim, tbintf, tbstimv1, tbstimv2


    if args.trace:
        traceSignals.name = 'vcd/_test_jpegenc2k'
        traceSignals.timescale = '1ns'
        fn = traceSignals.name + '.vcd'
        if os.path.isfile(fn):
            os.remove(fn)
        gt = traceSignals(_test)
    else:
        gt = _test()

    # run the simulation
    Simulation((gt, tbdut,)).run()
    '''
def test_jpegenc2k():
    # randomly select a test image
    #ipth = "./lena_256.png"
    ipth = "./lena_rgb_512.png"
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
 
 
    """= 'small'
    while 'small' in ifn:
        ifn = random.choice(os.listdir(ipth))

    parser = argparse.ArgumentParser()
    parser.add_argument('--random_image', action='store_true', default=False,
                        help="use small3.png as test file")
    parser.add_argument('--vtrace', action='store_true', default=False,
                        help="enable Verilog simulator tracing")

    args = parser.parse_args()
    if args.random_image:
        ipth = os.path.join(ipth, ifn)
    else:

    ipth = os.path.join(ipth, 'small4.png')
    """

    # setup arguments for the test (future capture from CLI)
    vmod = 'tb_jpegenc2k'
    # tracing arguments
    args.trace=False            # enable tracing (debug)
    args.vtrace=True            # enable VCD tracing in Verilog cosim
    args.vtrace_level=0         # Verilog VCD dumpvars level
    args.vtrace_module=vmod     # Verilog VCD dumpvars module to trace

    args.imgfn=ipth             # image to test compression

    # verification (debug) options
    args.build_only=False       # compile the V* only, not test
    args.build_skip_v1=False    # skip the V1 encoder compile
    args.nout=0                 # number of encoded outputs to capture (debug mode)
    args.no_wait=False          # don't wait for the encoder,exit after input
    args.dump_bitstreams=False  # dump full bitstreams at the end
    args.ncyc = 200             # generate some prints

    args.start_time = datetime.datetime.now()

    # run the JPEG encoder test
    print("Using args trace %s " % (args.trace))
    print("Using args vtrace %s " % (args.vtrace))
    print("Using args vtrace_level %s " % (args.vtrace_level))
    print("Using args vtrace_module %s " % (args.vtrace_module))
    print("Using image %s " % (ipth,))
    
    print("Using args build_only %s " % (args.build_only))
    print("Using args nout %s " % (args.nout))
    print("Using args no_wait %s " % (args.no_wait))
    print("Using args dump_bitstreams %s " % (args.dump_bitstreams))
    print("Using args start_time %s " % (args.start_time))
    img = Image.open(ipth) 
    print("Image size %d %d " % (img.size))
    print("Image mode %s " % (img.mode))
    runbench(args)

if __name__ == '__main__':
    test_jpegenc2k()


