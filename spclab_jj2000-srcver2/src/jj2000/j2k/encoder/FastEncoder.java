/*
 * COPYRIGHT:
 *
 * This software module was originally developed by Raphaël Grosbois and
 * Diego Santa Cruz (Swiss Federal Institute of Technology-EPFL); Joel
 * Askelöf (Ericsson Radio Systems AB); and Bertrand Berthelot, David
 * Bouchard, Félix Henry, Gerard Mozelle and Patrice Onno (Canon Research
 * Centre France S.A) in the course of development of the JPEG2000
 * standard as specified by ISO/IEC 15444 (JPEG 2000 Standard). This
 * software module is an implementation of a part of the JPEG 2000
 * Standard. Swiss Federal Institute of Technology-EPFL, Ericsson Radio
 * Systems AB and Canon Research Centre France S.A (collectively JJ2000
 * Partners) agree not to assert against ISO/IEC and users of the JPEG
 * 2000 Standard (Users) any of their rights under the copyright, not
 * including other intellectual property rights, for this software module
 * with respect to the usage by ISO/IEC and Users of this software module
 * or modifications thereof for use in hardware or software products
 * claiming conformance to the JPEG 2000 Standard. Those intending to use
 * this software module in hardware or software products are advised that
 * their use may infringe existing patents. The original developers of
 * this software module, JJ2000 Partners and ISO/IEC assume no liability
 * for use of this software module or modifications thereof. No license
 * or right to this software module is granted for non JPEG 2000 Standard
 * conforming products. JJ2000 Partners have full right to use this
 * software module for his/her own purpose, assign or donate this
 * software module to any third party and to inhibit third parties from
 * using this software module for non JPEG 2000 Standard conforming
 * products. This copyright notice must be included in all copies or
 * derivative works of this software module.
 *
 * Copyright (c) 1999/2000 JJ2000 Partners.
 * */
package jj2000.j2k.encoder;

import cern.colt.matrix.Matrix2D;
import jj2000.j2k.quantization.quantizer.*;
import jj2000.j2k.image.forwcomptransf.*;
import jj2000.j2k.codestream.writer.*;
import jj2000.j2k.fileformat.writer.*;
import jj2000.j2k.wavelet.analysis.*;
import jj2000.j2k.entropy.encoder.*;
import jj2000.j2k.image.input.*;
import jj2000.j2k.roi.encoder.*;
import jj2000.j2k.image.*;
import jj2000.j2k.util.*;
import jj2000.j2k.*;
import java.io.*;

/**
 * This class was derived from the Encoder.java to read and write
 * the codestream from/to a memory buffer It uses an alternate version of
 * EncoderSpecs to eliminate all the command line parameter parsing.
 *
 * @author Alberto Aguirre
 *
 * @see ImgReader
 * @see ImgDataJoiner
 * @see ForwCompTransf
 * @see Tiler
 * @see ImgDataConverter
 * @see ForwardWT
 * @see Quantizer
 * @see ROIScaler
 * @see EntropyCoder
 * @see PostCompRateAllocator
 * @see HeaderEncoder
 * @see CodestreamWriter
 * @see CodestreamManipulator
 * @see FileFormatWriter
 * @see ModuleSpec
 * @see EncoderSpecs
 * */
public class FastEncoder {
    
    private EncoderOptions options;
    private int[] RDSlopesRates;
    
    /**
     * Instantiates an encoder object, width the ParameterList object given as
     * argument. It also retrieves the default ParameterList.
     *
     * @param pl The ParameterList for this decoder (contains also defaults
     * values);
     * */
    public FastEncoder(EncoderOptions options) {
        this.options = options;
    }
    
    /**
     * Runs the encoder. After completion the exit code is set, a non-zero
     * value indicates that an error ocurred.
     *
     * @see #getExitCode
     * */
    public byte[] run(Matrix2D data, int bitdepth) throws IOException {
        // boolean useFileFormat = false;
        
        EncoderChain chain = new EncoderChain(data, bitdepth);
        
        AltHeaderEncoder headenc = chain.getHeaderEncoder();
        AltEBCOTRateAllocator ralloc = chain.getRalloc();
        AltCodestreamWriter bwriter = chain.getCodestreamWriter();
        ByteArrayOutputStream outStream = chain.getOutputStream();
        
        // **** Write header to be able to estimate header overhead ****
        headenc.encodeMainHeader();
        
        // **** Initialize rate allocator, with proper header
        // overhead. This will also encode all the data ****
        ralloc.initialize();
        
        // **** Write header (final) ****
        headenc.reset();
        headenc.encodeMainHeader();
        
        // Insert header into the codestream
        bwriter.commitBitstreamHeader(headenc);
        
        // **** Now do the rate-allocation and write result ****
        ralloc.runAndWrite();
        
        RDSlopesRates = ralloc.getRDSlopesRates();
        // **** Done ****
        bwriter.close();
        
        return outStream.toByteArray();
    }
    
    /**
     * Prints the error message 'msg' to standard err, prepending "ERROR" to
     * it, and sets the exitCode to 'code'. An exit code different than 0
     * indicates that there where problems.
     *
     * @param msg The error message
     *
     * @param code The exit code to set
     * */
    private void error(String msg) {
        throw new IllegalArgumentException(msg);
    }
    
    public float getMinRate(Matrix2D a,  int bitdepth) throws IOException {
        return (float)(getOverhead(a, bitdepth)+2)*8.0f/a.size();
    }
    
    public int getOverhead(Matrix2D a, int bitdepth) throws IOException {
        int minBytes = 0;
        EncoderChain chain = new EncoderChain(a, bitdepth);
        int numTiles = chain.getNumberOfTiles();
        AltHeaderEncoder headEnc = chain.getHeaderEncoder();
        headEnc.encodeMainHeader();
        minBytes = headEnc.getLength();
        for(int t=0; t<numTiles; t++) {
            headEnc.reset();
            headEnc.encodeTilePartHeader(0,t);
            minBytes+= headEnc.getLength();
        }
        return minBytes;
    }
    
    public int[] getRDSlopeRates() {
        return RDSlopesRates;
    }
    
    private class EncoderChain {
        
        boolean pphTile = false;
        boolean pphMain = false;
        boolean tempSop = false;
        boolean tempEph = false;
        
        int ncomp;
        boolean imsigned[];
        BlkImgDataSrc imgsrc;
        int tw,th;
        int refx,refy;
        int trefx,trefy;
        int pktspertp;
        Tiler imgtiler;
        FastForwCompTransf fctransf;
        ImgDataConverter converter;
        AltEncoderSpecs encSpec;
        ForwardWT dwt;
        Quantizer quant;
        FastROIScaler rois;
        EntropyCoder ecoder;
        AltEBCOTRateAllocator ralloc;
        AltHeaderEncoder headenc;
        AltCodestreamWriter bwriter;
        FileFormatWriter ffw;
        ByteArrayOutputStream outStream;
        float rate;
        
        private AltEBCOTRateAllocator getRalloc() {
            return ralloc;
        }
        
        private ByteArrayOutputStream getOutputStream() {
            return outStream;
        }
        
        private AltHeaderEncoder getHeaderEncoder() {
            return headenc;
        }
        
        private AltCodestreamWriter getCodestreamWriter() {
            return bwriter;
        }
        
        private int getNumberOfTiles() {
            return imgtiler.getNumTiles();
        }
        
        private int getImgSize() {
            return imgsrc.getImgHeight()*imgsrc.getImgWidth();
        }
        private EncoderChain(Matrix2D data, int bitdepth) {
             rate = options.rate;
            if(rate==-1) {
                rate = Float.MAX_VALUE;
            }
            
            
            pktspertp = options.tile_parts;
            if(pktspertp != 0){
                if(!options.psop){
                    options.psop = true;
                    tempSop = true;
                }
                if(!options.peph) {
                    options.peph = true;
                    tempEph = true;
                }
            }
            
            // **** ImgReader ****
            ncomp = 1;
            imsigned = new boolean[ncomp];
            for(int i=0;i<imsigned.length;i++) {
                imsigned[i]=true;
            }
            imgsrc = new Matrix2DReader(data, bitdepth);
            
            // **** Tiler ****
            // get nominal tile dimensions
            
            tw = options.tw;
            th = options.th;
            
            refx = options.refx;
            refy = options.refy;
            
            if (refx < 0 || refy < 0) {
                error("Invalid value in 'ref' "+
                        "option ");
            }
            
            trefx = options.trefx;
            trefy = options.trefy;
            
            if (trefx < 0 || trefy < 0 || trefx > refx || trefy > refy) {
                error("Invalid value in 'tref' "+
                        "option ");
            }
            
            // Instantiate tiler
            
            imgtiler = new Tiler(imgsrc,refx,refy,trefx,trefy,tw,th);
            int ntiles = imgtiler.getNumTiles();
            
            // **** Encoder specifications ****
            encSpec = new AltEncoderSpecs(ntiles, ncomp, imgsrc, options);
            
            // **** Component transformation ****
            fctransf = new FastForwCompTransf(imgtiler,encSpec);
            
            // **** ImgDataConverter ****
            converter = new ImgDataConverter(fctransf);
            
            // **** ForwardWT ****
            dwt = ForwardWT.createAltInstance(converter,options,encSpec);
            
            
            // **** Quantizer ****
            quant = Quantizer.createAltInstance(dwt,encSpec);
            
            // **** ROIScaler ****
            rois = FastROIScaler.createInstance(quant,options,encSpec);
            
            // **** EntropyCoder ****
            
            ecoder = EntropyCoder.createAltInstance(rois,options,encSpec.cblks,
                    encSpec.pss,encSpec.bms,
                    encSpec.mqrs,encSpec.rts,
                    encSpec.css,encSpec.sss,
                    encSpec.lcs,encSpec.tts);
            
            // **** CodestreamWriter ****
            // Rely on rate allocator to limit amount of data
            outStream = new ByteArrayOutputStream();
            bwriter = new AltFileCodestreamWriter(outStream,Integer.MAX_VALUE);
            
            // **** Rate allocator ****
            ralloc = AltPostCompRateAllocator.createInstance(ecoder,options,rate,
                    bwriter,encSpec);
            
            // **** HeaderEncoder ****
            headenc = new AltHeaderEncoder(imgsrc,imsigned,dwt,imgtiler,encSpec,
                    rois,ralloc);
            ralloc.setHeaderEncoder(headenc);
        }
        
       
    }    
}
