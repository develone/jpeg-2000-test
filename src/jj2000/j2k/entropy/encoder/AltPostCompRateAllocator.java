/*
 * CVS identifier:
 *
 * $Id: AltPostCompRateAllocator.java,v 1.1 2006/12/14 20:59:11 devel Exp vidal $
 *
 * Class:                   PostCompRateAllocator
 *
 * Description:             Generic interface for post-compression
 *                          rate allocator.
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
package jj2000.j2k.entropy.encoder;

import jj2000.j2k.codestream.writer.*;
import jj2000.j2k.codestream.*;
import jj2000.j2k.entropy.*;
import jj2000.j2k.encoder.*;
import jj2000.j2k.image.*;
import jj2000.j2k.util.*;
import jj2000.j2k.*;

import java.io.*;

/**
 * This is the abstract class from which post-compression rate allocators
 * which generate layers should inherit. The source of data is a
 * 'CodedCBlkDataSrcEnc' which delivers entropy coded blocks with
 * rate-distortion statistics.
 *
 * <p>The post compression rate allocator implementation should create the
 * layers, according to a rate allocation policy, and send the packets to a
 * CodestreamWriter. Since the rate allocator sends the packets to the bit
 * stream then it should output the packets to the bit stream in the order
 * imposed by the bit stream profiles.</p>
 *
 * @see CodedCBlkDataSrcEnc
 * @see jj2000.j2k.codestream.writer.CodestreamWriter
 * */
public abstract class AltPostCompRateAllocator extends ImgDataAdapter {       

    /** The source of entropy coded data */
    protected CodedCBlkDataSrcEnc src;
    
    /** The source of entropy coded data */
    protected AltEncoderSpecs encSpec;

    /** The number of layers. */
    protected int numLayers;

    /** The bit-stream writer */
    AltCodestreamWriter bsWriter;

    /** The header encoder */
    AltHeaderEncoder headEnc;
    
    /**
     * Initializes the source of entropy coded data.
     *
     * @param src The source of entropy coded data.
     *
     * @param ln The number of layers to create
     *
     * @param pt The progressive type, as defined in 'ProgressionType'.
     *
     * @param bw The packet bit stream writer.
     *
     * @see ProgressionType
     * */
    public AltPostCompRateAllocator(CodedCBlkDataSrcEnc src, int nl,
                                 AltCodestreamWriter bw, AltEncoderSpecs encSpec) {
        super(src);
        this.src = src;
        this.encSpec = encSpec;
        numLayers = nl;
        bsWriter = bw;
    }

    /** 
     * Keep a reference to the header encoder.
     *
     * @param headEnc The header encoder
     * */
    public void setHeaderEncoder(AltHeaderEncoder headEnc){
	this.headEnc = headEnc;
    }

    /**
     * Initializes the rate allocation points, taking into account header
     * overhead and such. This method must be called after the header has been
     * simulated but before calling the runAndWrite() one. The header must be
     * rewritten after a call to this method since the number of layers may
     * change.
     *     
     *
     * @see #runAndWrite
     * */
    public abstract void initialize() throws IOException;

    /**
     * Runs the rate allocation algorithm and writes the data to the
     * bit stream. This must be called after the initialize() method.
     *
     * @see #initialize
     * */
    public abstract void runAndWrite() throws IOException;

    /**
     * Returns the number of layers that are actually generated.
     *
     * @return The number of layers generated.
     * */
    public int getNumLayers() {
        return numLayers;
    }
    
    /**
     * Creates a PostCompRateAllocator object for the appropriate rate
     * allocation parameters in the parameter list 'pl', having 'src' as the
     * source of entropy coded data, 'rate' as the target bitrate and 'bw' as
     * the bit stream writer object.
     *
     * @param src The source of entropy coded data.
     *
     * @param pl The parameter lis (or options).
     *
     * @param rate The target bitrate for the rate allocation
     *
     * @param bw The bit stream writer object, where the bit stream data will
     * be written.
     * */
    public static AltEBCOTRateAllocator createInstance(CodedCBlkDataSrcEnc src,
                                                       EncoderOptions options,
                                                       float rate,
                                                       AltCodestreamWriter bw,
                                                       AltEncoderSpecs encSpec){        

        // Construct the layer specification from the 'Alayers' option
        LayersInfo lyrs = parseAlayers(options.alayers, options.rate);

	int nTiles = encSpec.nTiles;
	int nComp = encSpec.nComp;
	int numLayers = lyrs.getTotNumLayers();

        // Parse the progressive type
	encSpec.pocs = new AltProgressionSpec(nTiles,nComp,numLayers,encSpec.dls,
                                           ModuleSpec.SPEC_TYPE_TILE_COMP,options);

        return new AltEBCOTRateAllocator(src,lyrs,bw,encSpec,options);
    }    

    /**
     * Convenience method that parses the 'Alayers' option.
     *
     * @param params The parameters of the 'Alayers' option
     *
     * @param rate The overall target bitrate
     *
     * @return The layer specification.
     * */
    private static LayersInfo parseAlayers(String params,float rate) {
        LayersInfo lyrs;
        StreamTokenizer stok;
        boolean islayer,ratepending;
        float r;

        lyrs = new LayersInfo(rate);
        stok = new StreamTokenizer(new StringReader(params));
        stok.eolIsSignificant(false);

        try {
            stok.nextToken();
        } catch (IOException e) {
            throw new Error("An IOException has ocurred where it "+
                            "should never occur");
        }
        ratepending = false;
        islayer = false;
        r = 0; // to keep compiler happy
        while (stok.ttype != stok.TT_EOF) {
            switch(stok.ttype) {
            case StreamTokenizer.TT_NUMBER:
                if (islayer) { // layer parameter
                    try {
                        lyrs.addOptPoint(r,(int)stok.nval);
                    } catch (IllegalArgumentException e) {
                        throw new
                            IllegalArgumentException("Error in 'Alayers' "+
                                                     "option: "+
                                                     e.getMessage());
                    }
                    ratepending = false;
                    islayer = false;
                } else { // rate parameter
                    if (ratepending) { // Add pending rate parameter
                        try {
                            lyrs.addOptPoint(r,0);
                        } catch (IllegalArgumentException e) {
                            throw new
                                IllegalArgumentException("Error in 'Alayers' "+
                                                         "option: "+
                                                         e.getMessage());
                        }
                    }
                    // Now store new rate parameter
                    r = (float) stok.nval;
                    ratepending = true;
                }
                break;
            case '+':
                if (!ratepending || islayer) {
                    throw new
                        IllegalArgumentException("Layer parameter without "+
                                                 "previous rate parameter "+
                                                 "in 'Alayers' option");
                }
                islayer = true; // Next number is layer parameter
                break;
            case StreamTokenizer.TT_WORD:
                try {
                    stok.nextToken();
                } catch(IOException e) {
                    throw new Error("An IOException has ocurred where it "+
                                    "should never occur");
                }
                if (stok.ttype != stok.TT_EOF) {
                    throw new 
                        IllegalArgumentException("'sl' argument of "+
                                                 "'-Alayers' option must be "+
                                                 "used alone.");
                }
                break;
            default:
                throw new IllegalArgumentException("Error parsing 'Alayers' "+
                                                   "option");
            }
            try {
                stok.nextToken();
            } catch (IOException e) {
                throw new Error("An IOException has ocurred where it "+
                                "should never occur");
            }
        }
        if (islayer) {
            throw new IllegalArgumentException("Error parsing 'Alayers' "+
                                               "option");
        }
        if (ratepending) {
            try {
                lyrs.addOptPoint(r,0);
            } catch (IllegalArgumentException e) {
                throw new
                    IllegalArgumentException("Error in 'Alayers' "+
                                             "option: "+
                                             e.getMessage());
            }
        }
        return lyrs;
    }

}
