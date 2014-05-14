/*
 * CVS identifier:
 *
 * $Id: AltEncoderSpecs.java,v 1.1 2006/12/14 20:58:57 devel Exp vidal $
 *
 * Class:                   EncoderSpecs
 *
 * Description:             Hold all encoder specifications
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
package jj2000.j2k.encoder;

import jj2000.j2k.image.forwcomptransf.*;
import jj2000.j2k.wavelet.analysis.*;
import jj2000.j2k.quantization.*;
import jj2000.j2k.entropy.*;
import jj2000.j2k.image.*;
import jj2000.j2k.roi.*;
import jj2000.j2k.*;

/**
 * This class holds references to each module specifications used in the
 * encoding chain. This avoid big amount of arguments in method calls. A
 * specification contains values of each tile-component for one module. All
 * members must be instance of ModuleSpec class (or its children).
 *
 * @see ModuleSpec
 * */
public class AltEncoderSpecs{
    
    /** ROI maxshift value specifications */
    public MaxShiftSpec rois;
    
    /** Quantization type specifications */
    public AltQuantTypeSpec qts;
    
    /** Quantization normalized base step size specifications */
    public AltQuantStepSizeSpec qsss;
    
    /** Number of guard bits specifications */
    public AltGuardBitsSpec gbs;
    
    /** Analysis wavelet filters specifications */
    public AltAnWTFilterSpec wfs;
    
    /** Component transformation specifications */
    public AltForwCompTransfSpec cts;
    
    /** Number of decomposition levels specifications */
    public AltIntegerSpec dls;
    
    /** The length calculation specifications */
    public AltIntegerSpec lcs;
    
    /** The termination type specifications */
    public AltIntegerSpec tts;
    
    /** Error resilience segment symbol use specifications */
    public BooleanSpec sss;
    
    /** Causal stripes specifications */
    public BooleanSpec css;
    
    /** Regular termination specifications */
    public BooleanSpec rts;
    
    /** MQ reset specifications */
    public BooleanSpec mqrs;
    
    /** By-pass mode specifications */
    public BooleanSpec bms;
    
    /** Precinct partition specifications */
    public AltPrecinctSizeSpec pss;
    
    /** Start of packet (SOP) marker use specification */
    public BooleanSpec sops;
    
    /** End of packet header (EPH) marker use specification */
    public BooleanSpec ephs;
    
    /** Code-blocks sizes specification */
    public AltCBlkSizeSpec cblks;
    
    /** Progression/progression changes specification */
    public AltProgressionSpec pocs;
    
    /** The number of tiles within the image */
    public int nTiles;
    
    /** The number of components within the image */
    public int nComp;
    
    
    /**
     * Initialize all members with the given number of tiles and components
     * and the command-line arguments stored in a ParameterList instance
     *
     * @param nt Number of tiles
     *
     * @param nc Number of components
     *
     * @param imgsrc The image source (used to get the image size)
     *
     * @param pl The ParameterList instance
     * */
    public AltEncoderSpecs(int nt,int nc,BlkImgDataSrc imgsrc, EncoderOptions options) {
        nTiles = nt;
        nComp  = nc;
        // ROI
        rois = new MaxShiftSpec(nt,nc,ModuleSpec.SPEC_TYPE_TILE_COMP);
        
        // Quantization
        
        qts  = new AltQuantTypeSpec(nt,nc,ModuleSpec.SPEC_TYPE_TILE_COMP,options);
        qsss = new AltQuantStepSizeSpec(nt,nc,ModuleSpec.SPEC_TYPE_TILE_COMP,options);
        gbs  = new AltGuardBitsSpec(nt,nc,ModuleSpec.SPEC_TYPE_TILE_COMP,options);
        
        // Wavelet transform
        wfs = new AltAnWTFilterSpec(nt,nc,ModuleSpec.SPEC_TYPE_TILE_COMP,options);
        dls = new AltIntegerSpec(nt,nc,ModuleSpec.SPEC_TYPE_TILE_COMP,options.wlev);
        
        // Component transformation
        cts = new AltForwCompTransfSpec(nt,nc,ModuleSpec.SPEC_TYPE_TILE,options);
        
        // Entropy coder
        //String[] strLcs = {"near_opt","lazy_good","lazy"};
        lcs = new AltIntegerSpec(nt,nc,ModuleSpec.SPEC_TYPE_TILE_COMP,options.clen_calc);
        //String[] FaststrTerm = {"near_opt","easy","predict","full"};
        tts = new AltIntegerSpec(nt,nc,ModuleSpec.SPEC_TYPE_TILE_COMP,options.cterm_type);
        //String[] strBoolean = {"on","off"};
        sss = new BooleanSpec(nt,nc,ModuleSpec.SPEC_TYPE_TILE_COMP,options.cseg_symbol);
        css = new BooleanSpec(nt,nc,ModuleSpec.SPEC_TYPE_TILE_COMP,options.ccausal);
        rts = new BooleanSpec(nt,nc,ModuleSpec.SPEC_TYPE_TILE_COMP,options.cterminate);
        mqrs = new BooleanSpec(nt,nc,ModuleSpec.SPEC_TYPE_TILE_COMP,options.cresetMQ);
        bms = new BooleanSpec(nt,nc,ModuleSpec.SPEC_TYPE_TILE_COMP,options.cbypass);
        cblks = new AltCBlkSizeSpec(nt,nc,ModuleSpec.SPEC_TYPE_TILE_COMP,options);
        
        // Precinct partition
        pss = new AltPrecinctSizeSpec(nt,nc,ModuleSpec.SPEC_TYPE_TILE_COMP,imgsrc,dls);
        
        // Codestream
        sops = new BooleanSpec(nt,nc,ModuleSpec.SPEC_TYPE_TILE,options.psop);
        ephs = new BooleanSpec(nt,nc,ModuleSpec.SPEC_TYPE_TILE,options.peph);
        
    }
    
    
    
}
