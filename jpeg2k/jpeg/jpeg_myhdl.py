from myhdl import *
DATA_WIDTH = 32768
def Jpeg(
    #ToSPieceOut, 
    #ToSMaskOut, 
    #PieceIn, 
    #MaskIn, 
    MaskReset, 
    #Enable, 
    PushPop, 
    Reset,
    #Clk,
    clk_fast,
    DEPTH = 16
):
    """Stack module in MyHDL

    This the MyHDL RTL code for the Stack module. It
    can be converted to Verilog/VHDL and synthesized.
    """

    ONES = 2**16-1

    #ToSPiece = Signal(intbv(0)[6:])
    #ToSMask = Signal(intbv(ONES)[16:])
    #Stack = [Signal(intbv(0)[16:]) for i in range(DEPTH-1)]
    Jpeg = [Signal(intbv(0)[16:]) for i in range(DEPTH-1)]
    StackWriteData = Signal(intbv(0)[16:])
    StackReadData = Signal(intbv(0)[16:])
    StackWrite = Signal(bool(0))
    Pointer = Signal(intbv(0, min=0, max=DEPTH-1))
    WritePointer = Signal(intbv(0, min=0, max=DEPTH-1))
    NrItems = Signal(intbv(0, min=0, max=DEPTH+1))
    sig_out = [Signal(intbv(0)[52:]) for i in range(DEPTH-1) ]
    sig_in = [Signal(intbv(0)[52:]) for i in range(DEPTH-1) ]
    left_s = Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))
    right_s = Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))
    sam_s = Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))
    even_odd_s = Signal(bool(0))
    fwd_inv_s = Signal(bool(0))
    updated_s = Signal(bool(0))
    noupdate_s = Signal(bool(0))
    
    #@always_seq(Clk.posedge, reset=Reset)
    @always_seq(clk_fast.posedge, reset=Reset)
    def control():
        StackWrite.next = False
        if MaskReset != 0:
            #ToSMask.next = ToSMask & ~MaskReset
            #this is a dummy statement
            updated_s.next = 0
        #elif PushPop and Enable: # push    
        elif PushPop : # push
            #ToSPiece.next = PieceIn
            #ToSMask.next = MaskIn  
            NrItems.next = NrItems + 1
            if NrItems > 0:
                #StackWriteData.next = concat(ToSPiece, ToSMask)
                StackWrite.next = True
                Pointer.next = WritePointer
                if WritePointer < DEPTH-2:
                    WritePointer.next = WritePointer + 1
        #elif not PushPop and Enable: # pop
        elif not PushPop : # pop
            #ToSPiece.next = StackReadData[22:16]
            #ToSMask.next = StackReadData[16:]
            NrItems.next = NrItems - 1
            WritePointer.next = Pointer
            if Pointer > 0:
                Pointer.next = Pointer - 1


        if updated_s:
            noupdate_s.next = 0
            if even_odd_s:
                if  fwd_inv_s:
                    Jpeg[Pointer].next =  sam_s - ((left_s >> 1) + (right_s >> 1))
                else:
                    Jpeg[Pointer].next =  sam_s + ((left_s >> 1) + (right_s >> 1))
            else:
                if fwd_inv_s:
                    Jpeg[Pointer].next =  sam_s + ((left_s +  right_s + 2)>>2)
                else:
                    Jpeg[Pointer].next =  sam_s - ((left_s +  right_s + 2)>>2)
        else:
            noupdate_s.next = 1 
    #@always_seq(Clk.posedge, reset=None)                    
    @always_seq(clk_fast.posedge, reset=None)
    def write_stack():
        if StackWrite:
            #Stack[Pointer].next = StackWriteData
            Jpeg[Pointer].next = StackWriteData

 
    @always_comb
    def read_stack():
        #StackReadData.next = Stack[Pointer]
        StackReadData.next = Jpeg[Pointer]
        sig_in[Pointer].next = sig_out[Pointer]

    #@always_comb
    #def output():
         #ToSPieceOut.next = ToSPiece
         #ToSMaskOut.next = ToSMask 
               
    #return control, write_stack, read_stack, output
    return control, write_stack, read_stack