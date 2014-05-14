/*
 * MatrixReader.java
 *
 */

package jj2000.j2k.image.input;

import cern.colt.matrix.Matrix2D;
import java.io.IOException;
import jj2000.j2k.image.DataBlk;
import jj2000.j2k.image.DataBlkInt;

/**
 *
 * @author Alberto Aguirre
 */
public class Matrix2DReader extends ImgReader {
    
    private Matrix2D data;
      private int bitdepth;
    
    /** Temporary DataBlkInt object (needed when encoder uses floating-point
     * filters). This avoid allocating new DataBlk at each time */
    private DataBlkInt intBlk;   
    
    /** Creates a new instance of MatrixReader */
    public Matrix2DReader(Matrix2D input, int bitDepth) {
        this.data = input;
        this.bitdepth = bitDepth;
        
        this.w = input.columns();
        this.h = input.rows();
        this.nc =1;
    }
    
    public DataBlk getInternCompData(DataBlk blk, int c) {
        //System.out.println("Reader Ulx: "+blk.ulx+"\tUly: "+blk.uly+"\tW: "+blk.w+"\t"+blk.h);
        // Check type of block provided as an argument
        if(blk.getDataType()!=DataBlk.TYPE_INT){
            if(intBlk==null)
                intBlk = new DataBlkInt(blk.ulx,blk.uly,blk.w,blk.h);
            else{
                intBlk.ulx = blk.ulx;
                intBlk.uly = blk.uly;
                intBlk.w = blk.w;
                intBlk.h = blk.h;
            }
            blk = intBlk;
        }
        
        // Get data array
        int[] barr = (int[]) blk.getData();
        if (barr == null || barr.length < blk.w*blk.h) {
            barr = new int[blk.w*blk.h];
            blk.setData(barr);
        }
        int index =  0;
        for(int j=blk.uly;j<blk.uly+blk.h;j++) {
            for(int i=blk.ulx;i<blk.w+blk.ulx;i++) {                
                barr[index++] = (int)data.get(j, i);
               // System.a
            }
        }
        
        // Turn off the progressive attribute
        blk.progressive = false;
        // Set buffer attributes
        blk.offset = 0;
        blk.scanw = blk.w;
        return blk;
    }
    
    public DataBlk getCompData(DataBlk blk, int c) {
        return this.getInternCompData(blk, c);
    }
    
    public boolean isOrigSigned(int c) {
        return true;
    }
    
    public int getNomRangeBits(int c) {
        return bitdepth;
    }
    
    public int getFixedPoint(int c) {
        return 0;
    }
    
    public void close() throws IOException {
        data = null;
    }
    
}
