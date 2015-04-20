
from myhdl import *


class SignalMatrix(object):

    def __init__(self, size=(4,4,), stype=intbv(0)[9:]):
        # the size of the matrix
        self.size = size
        nrows,ncols = size

        # the size (number of bits) for each item in the matrix
        if isinstance(stype, intbv):
            self.nbits = len(stype)
        else:
            self.nbits = 1

        # the signal matrix
        self.M = [[Signal(stype) for col in range(ncols)]
                  for row in range(nrows)]


    def __getitem__(self, idx):
        print(type(idx), idx)
        item = None
        if isinstance(idx, tuple):
            item = self.M[idx[0]][idx[1]]

        return item


    def get_flat_signal(self):
        nbits = self.size[0] * self.size[1] * self.nbits
        sig = Signal(intbv(0)[nbits:])
        return sig


    def m_stack(self, flat):
        ''' convert flat bit-vector to a signal matrix '''
        nitems = self.size[0]*self.size[1]
        nbits = self.nbits
        assert len(flat) == nitems*nbits
        # create a flat list of signals (references)
        flats = [col for row in self.M for col in row]

        # avoid Verilog indexing limitation ...
        def _assign(y, x):
            @always_comb
            def assign():
                y.next = x
            return assign

        g = [None for _ in range(nitems)]
        for ii in range(nitems):
            g[ii] = _assign(flats[ii], flat(ii*nbits+nbits, ii*nbits))

        return g


    def m_flatten(self, flat):
        ''' convert this matrix to flat bit-vector '''
        nbits = self.nbits
        flats = ConcatSignal(*[col(nbits, 0) for row in self.M for col in row])
        @always_comb
        def rtl():
            flat.next = flats
        return rtl


def m_flat_top(clock, reset, sdi, sdo):
    ''' example convertible top-level '''
    matrix = SignalMatrix()
    flati = matrix.get_flat_signal()
    flato = matrix.get_flat_signal()
    nbits = len(flati)

    @always_seq(clock.posedge, reset=reset)
    def rtli():
        flati.next = concat(flati[nbits-1:0], sdi)

    gstk = matrix.m_stack(flati)
    gflt = matrix.m_flatten(flato)

    @always_seq(clock.posedge, reset=reset)
    def rtlo():
        sdo.next = concat(flato[nbits-1:0], bool(0))

    return rtli, gstk, gflt, rtlo


def convert():
    clock = Signal(bool(0))
    reset = ResetSignal(0, active=1, async=False)
    sdi = Signal(bool(0))
    sdo = Signal(bool(0))
    toVerilog(m_flat_top, clock, reset, sdi, sdo)
    toVHDL(m_flat_top, clock, reset, sdi, sdo)


if __name__ == '__main__':
    convert()
