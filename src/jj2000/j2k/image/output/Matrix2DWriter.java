/*
 * SingleMatrix2DWriter.java
 *
 */

package jj2000.j2k.image.output;

import cern.colt.matrix.Matrix2D;
import java.io.IOException;
import jj2000.j2k.image.BlkImgDataSrc;
import jj2000.j2k.image.DataBlkInt;

/**
 *
 * @author Alberto Aguirre
 */
public class Matrix2DWriter extends ImgWriter {
    
    private Matrix2D data;
    
    /** The number of fractional bits in the source data */
    private int fb;
    
    /** A DataBlk, just used to avoid allocating a new one each time
     * it is needed */
    private DataBlkInt db = new DataBlkInt();
    
    /** The offset of the raw pixel data in the PGM file */
    private int offset;
    
    /** The line buffer. */
    // This makes the class not thrad safe
    // (but it is not the only one making it so)
    private byte buf[];
    
    private int c;
    /** Creates a new instance of SingleMatrix2DWriter */
    public Matrix2DWriter(BlkImgDataSrc src, Matrix2D out, int c) {
        this.src = src;
        this.data = out;
        this.c = c;
        this.w = src.getImgWidth();
        this.h = src.getImgHeight();
        this.fb = src.getFixedPoint(c);
    }
    
    public void write(int ulx, int uly, int w, int h) throws IOException {
        
        //System.out.println("Ulx: "+ulx+"\tUly: "+uly+"\tW: "+w+"\t"+h);
        int fracbits = fb;     // In local variable for faster access
        int tOffx;
        int tOffy;      // Active tile offset in the X and Y direction
        
        // Initialize db
        db.ulx = ulx;
        db.uly = uly;
        db.w = w;
        db.h = h;
        // Get the current active tile offset
        tOffx = src.getCompULX(c)-
                (int)Math.ceil(src.getImgULX()/(double)src.getCompSubsX(c));
        tOffy = src.getCompULY(c)-
                (int)Math.ceil(src.getImgULY()/(double)src.getCompSubsY(c));
        // Check the array size
        if(db.data!=null && db.data.length<w*h) {
            // A new one will be allocated by getInternCompData()
            db.data = null;
        }
        // Request the data and make sure it is not
        // progressive
        do {
            db = (DataBlkInt) src.getInternCompData(db,c);
        } while (db.progressive);
        
        int index = 0;
        for(int i=tOffy+uly ; i<(h+uly+tOffy);i++) {
            for(int j=ulx+tOffx;j<(w+ulx+tOffx);j++) {
                data.set(i, j, db.data[index++]);
            }
        }
    }
    
    public void write() throws IOException {
        write(0,0,w,h);
    }
    
    public void flush() throws IOException {
    }
    
    public void close() throws IOException {
        src = null;
        data = null;
    }
    
}
