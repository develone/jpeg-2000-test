/*
 * CVS identifier:
 *
 * $Id: FastDecoder.java,v 1.1 2006/12/14 20:58:57 devel Exp $
 *
 * Class:                   Decoder
 *
 * Description:             The decoder object
 *
 *
 *
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
package jj2000.j2k.decoder;

import cern.colt.matrix.Matrix2D;
import cern.colt.matrix.MatrixFactory;
import jj2000.j2k.quantization.dequantizer.*;
import jj2000.j2k.image.invcomptransf.*;
import jj2000.j2k.fileformat.reader.*;
import jj2000.j2k.codestream.reader.*;
import jj2000.j2k.wavelet.synthesis.*;
import jj2000.j2k.entropy.decoder.*;
import jj2000.j2k.image.output.*;
import jj2000.j2k.codestream.*;
import jj2000.j2k.image.*;
import jj2000.j2k.util.*;
import jj2000.j2k.roi.*;
import jj2000.j2k.io.*;
import jj2000.disp.*;
import jj2000.j2k.*;
import icc.*;
import java.util.*;
import java.io.*;

/**
 * This class is the main class of JJ2000's decoder. It instantiates all
 * objects and performs the decoding operations. It then writes the image to
 * the output file or displays it.
 *
 * <p>First the decoder should be initialized with a ParameterList object
 * given through the constructor. The when the run() method is invoked and the
 * decoder executes. The exit code of the class can be obtained with the
 * getExitCode() method, after the constructor and after the run method. A
 * non-zero value indicates that an error has ocurred.</p>
 *
 * <p>The decoding chain corresponds to the following sequence of modules:</p>
 *
 * <ul>
 * <li>BitstreamReaderAgent</li>
 * <li>EntropyDecoder</li>
 * <li>ROIDeScaler</li>
 * <li>Dequantizer</li>
 * <li>InverseWT</li>
 * <li>ImgDataConverter</li>
 * <li>EnumratedColorSpaceMapper, SyccColorSpaceMapper or ICCProfiler</li>
 * <li>ComponentDemixer (if needed)</li>
 * <li>ImgDataAdapter (if ComponentDemixer is needed)</li>
 * <li>ImgWriter</li>
 * <li>BlkImgDataSrcImageProducer</li>
 * </ul>
 *
 * <p>The 2 last modules cannot be used at the same time and corresponds
 * respectively to the writing of decoded image into a file or the graphical
 * display of this same image.</p>
 *
 * <p>The behaviour of each module may be modified according to the current
 * tile-component. All the specifications are kept in modules extending
 * ModuleSpec and accessible through an instance of DecoderSpecs class.</p>
 *
 * @see BitstreamReaderAgent
 * @see EntropyDecoder
 * @see ROIDeScaler
 * @see Dequantizer
 * @see InverseWT
 * @see ImgDataConverter
 * @see InvCompTransf
 * @see ImgWriter
 * @see BlkImgDataSrcImageProducer
 * @see ModuleSpec
 * @see DecoderSpecs
 * */
public class FastDecoder {   
    
    /** Information contained in the codestream's headers */
    private HeaderInfo hi;
    
    /* All the decoder options */
    private DecoderOptions options;
    
    private float bitrate;
    private int numBytes;
    
    /**
     * Instantiates a decoder object, with the ParameterList object given as
     * argument and a component where to display the image if no output file
     * is specified. It also retrieves the default ParameterList.
     *
     * @param pl The ParameterList for this decoder (contains also defaults
     * values).
     *
     * @param isp The component where the image is to be displayed if not
     * output file is specified. If null a new frame will be created to
     * display the image.
     * */
    public FastDecoder(DecoderOptions options) {
        this.options = options;
    }
    
    /**
     * Runs the decoder.
     *
     */
    public Matrix2D[] run(byte[] input) throws IOException, ICCProfileException{
        int res; // resolution level to reconstruct
        //String infile;
        RandomAccessIO in;
        InputStream is;
        FileFormatReader ff;
        AltBitstreamReaderAgent breader = null;
        AltHeaderDecoder hd = null;
        EntropyDecoder entdec = null;
        AltROIDeScaler roids = null;
        Dequantizer deq = null;
        InverseWT invWT = null;
        AltInvCompTransf ictransf = null;
        ImgDataConverter converter = null;
        ImgWriter imwriter[] = null;
        DecoderSpecs decSpec = null;
        BlkImgDataSrc palettized = null;
        BlkImgDataSrc channels = null;
        BlkImgDataSrc resampled = null;
        BlkImgDataSrc color = null;
        int i;
        int depth[];
        float rate;
        int nbytes;
        
        int datalen = input.length;
        is = new ByteArrayInputStream(input);
        // known length => initialize to length
        in = new ISRandomAccessIO(is,datalen,1,datalen);
        
        // **** File Format ****
        // If the codestream is wrapped in the jp2 fileformat, Read the
        // file format wrapper
        ff = new FileFormatReader(in);
        ff.readFileFormat();
        if(ff.JP2FFUsed) {
            in.seek(ff.getFirstCodeStreamPos());
        }
        
        // +----------------------------+
        // | Instantiate decoding chain |
        // +----------------------------+
        
        // **** Header decoder ****
        // Instantiate header decoder and read main header
        hi = new HeaderInfo();
        try {
            hd = new AltHeaderDecoder(in,options,hi);
        } catch (EOFException e) {
            error("Codestream too short or bad header, "+
                    "unable to decode.");
        }
        
        int nCompCod = hd.getNumComps();
        int nTiles = hi.siz.getNumTiles();
        decSpec = hd.getDecoderSpecs();
        
        //////////////////////////
        //Info
//        String info = nCompCod+" component(s) in codestream, "+nTiles+
//                " tile(s)\n";
//        info += "Image dimension: ";
//        for(int c=0; c<nCompCod; c++) {
//            info += hi.siz.getCompImgWidth(c)+"x"+
//                    hi.siz.getCompImgHeight(c)+" ";
//        }
//
//        if(nTiles!=1) {
//            info += "\nNom. Tile dim. (in canvas): "+
//                    hi.siz.xtsiz+"x"+hi.siz.ytsiz;
//        }
//        FacilityManager.getMsgLogger().printmsg(MsgLogger.INFO,info);
//
//        if (pl.getBooleanParameter("cdstr_info")) {
//            FacilityManager.getMsgLogger().printmsg(MsgLogger.INFO,
//                    "Main header:\n"+hi.
//                    toStringMainHeader());
//        }
        /////////////////////////
        
        // Get demixed bitdepths
        depth = new int[nCompCod];
        for(i=0; i<nCompCod;i++) { depth[i] = hd.getOriginalBitDepth(i); }
        
        // **** Bit stream reader ****
        try {
            breader = AltBitstreamReaderAgent.
                    createInstance(in,hd,options,decSpec,hi);
        } catch (IOException e) {
            error("Error while reading bit stream header or parsing "+
                    "packets"+((e.getMessage() != null) ?
                        (":\n"+e.getMessage()) : ""));
        } catch (IllegalArgumentException e) {
            error("Cannot instantiate bit stream reader"+
                    ((e.getMessage() != null) ?
                        (":\n"+e.getMessage()) : ""));
        }
        
        // **** Entropy decoder ****
        try {
            entdec = hd.createEntropyDecoder(breader,options);
        } catch (IllegalArgumentException e) {
            error("Cannot instantiate entropy decoder"+
                    ((e.getMessage() != null) ?
                        (":\n"+e.getMessage()) : ""));
        }
        
        // **** ROI de-scaler ****
        try {
            roids = hd.createROIDeScaler(entdec,options,decSpec);
        } catch (IllegalArgumentException e) {
            error("Cannot instantiate roi de-scaler."+
                    ((e.getMessage() != null) ?
                        (":\n"+e.getMessage()) : ""));
        }
        
        // **** Dequantizer ****
        try {
            deq = hd.createDequantizer(roids,depth,decSpec);
        } catch (IllegalArgumentException e) {
            error("Cannot instantiate dequantizer"+
                    ((e.getMessage() != null) ?
                        (":\n"+e.getMessage()) : ""));
        }
        
        // **** Inverse wavelet transform ***
        try {
            // full page inverse wavelet transform
            invWT = InverseWT.createInstance(deq,decSpec);
        } catch (IllegalArgumentException e) {
            error("Cannot instantiate inverse wavelet transform"+
                    ((e.getMessage() != null) ?
                        (":\n"+e.getMessage()) : ""));
        }
        
        res = breader.getImgRes();
        invWT.setImgResLevel(res);
        
        // **** Data converter **** (after inverse transform module)
        converter = new ImgDataConverter(invWT,0);
        
        // **** Inverse component transformation ****
        ictransf = new AltInvCompTransf(converter,decSpec,depth,options);
        
        // Skip colorspace mapping
        color = ictransf;
        
        
        // This is the last image in the decoding chain and should be
        // assigned by the last transformation:
        BlkImgDataSrc decodedImage = color;
        if(color==null) {
            decodedImage = ictransf;
        }
        int nCompImg = decodedImage.getNumComps();
        
        // Write decoded image to specified output file
        imwriter = new ImgWriter[nCompImg];
        
        // Need to optimize! If no component mixer is used and PGM
        // files are written need to write blocks in parallel
        // (otherwise decodes 3 times)
        
        
        Matrix2D[] out = new Matrix2D[nCompImg];
        
        // Now write the image to the file (decodes as needed)
        for(i=0; i<imwriter.length; i++) {
            out[i]=MatrixFactory.instance.make(decodedImage.getImgHeight(), decodedImage.getImgWidth());
            imwriter[i] = new Matrix2DWriter(decodedImage, out[i],i);
            imwriter[i].writeAll();
            imwriter[i].close();
        }       
      
        // if file format used add the read file format bytes
        bitrate = breader.getActualRate();
        numBytes = breader.getActualNbytes();
        if(ff.JP2FFUsed){
            int imageSize =(int)((8.0f*numBytes)/bitrate);
            numBytes +=ff.getFirstCodeStreamPos();
            bitrate = (numBytes*8.0f)/imageSize;
        }

        return out;
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
    
    /**
     * Returns the compressed number of bytes decoded. Only call this method 
     * after running the decoder for correct values.
     */
    public int getNumBytes() {
        return numBytes;
    }
    
    /**
     * Returns the actual achieved rate. Only call this method after running 
     * the decoder for correct values.
     */
    public float getBitrate() {
        return bitrate;
    }
    
    
    /**
     * Return the information found in the COM marker segments encountered in
     * the decoded codestream.
     * */
    public String[] getCOMInfo() {
        if(hi==null) { // The codestream has not been read yet
            return null;
        }
        
        int nCOMMarkers = hi.getNumCOM();
        Enumeration com = hi.com.elements();
        String[] infoCOM = new String[nCOMMarkers];
        for(int i=0; i<nCOMMarkers; i++) {
            infoCOM[i] = com.nextElement().toString();
        }
        return infoCOM;
    }
}
