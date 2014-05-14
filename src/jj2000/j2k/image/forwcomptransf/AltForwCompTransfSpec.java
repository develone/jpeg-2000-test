/*
 * CVS identifier:
 *
 * $Id: AltForwCompTransfSpec.java,v 1.1 2006/12/14 20:59:21 devel Exp vidal $
 *
 * Class:                   ForwCompTransfSpec
 *
 * Description:             Component Transformation specification for encoder
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
package jj2000.j2k.image.forwcomptransf;

import jj2000.j2k.wavelet.analysis.*;
import jj2000.j2k.wavelet.*;
import jj2000.j2k.image.*;

import java.util.*;
import jj2000.j2k.encoder.EncoderOptions;

/**
 * This class extends CompTransfSpec class in order to hold encoder specific
 * aspects of CompTransfSpec.
 *
 * @see CompTransfSpec
 * */
public class AltForwCompTransfSpec extends CompTransfSpec implements FilterTypes {
    /**
     * Constructs a new 'ForwCompTransfSpec' for the specified number of
     * components and tiles, the wavelet filters type and the parameter of the
     * option 'Mct'. This constructor is called by the encoder. It also checks
     * that the arguments belong to the recognized arguments list.
     *
     * <p>This constructor chose the component transformation type depending
     * on the wavelet filters : RCT with w5x3 filter and ICT with w9x7
     * filter. Note: All filters must use the same data type.</p>
     *
     * @param nt The number of tiles
     *
     * @param nc The number of components
     *
     * @param type the type of the specification module i.e. tile specific,
     * component specific or both.
     *
     * @param wfs The wavelet filter specifications
     *
     * @param pl The ParameterList
     * */
    public AltForwCompTransfSpec(int nt,int nc,byte type,EncoderOptions options){
        super(nt,nc,type);
        
        boolean mct = options.mct;
        
        if(nc<3) {
            setDefault("none");
            return;
        }
        // If the compression is lossless, uses RCT
        else if(options.lossless) {
            setDefault("rct");
            return;
        } else {
            
            if(options.ffilters==FilterTypes.W9X7) {
                setDefault("ict");
            } else {
                setDefault("rct");
            }
        }
    }  
    
    /**
     * Get the filter type common to all component of a given tile. If the
     * tile index is -1, it searches common filter type of default
     * specifications.
     *
     * @param t The tile index
     *
     * @param wfs The analysis filters specifications
     *
     * @return The filter type common to all the components
     * */
    private int getFilterType(int t, AnWTFilterSpec wfs){
        AnWTFilter[][] anfilt;
        int[] filtType = new int[nComp];
        for(int c=0;c<nComp; c++){
            if(t==-1) {
                anfilt = (AnWTFilter[][])wfs.getCompDef(c);
            } else {
                anfilt = (AnWTFilter[][])wfs.getTileCompVal(t,c);
            }
            filtType[c] = anfilt[0][0].getFilterType();
        }
        
        // Check that all filters are the same one
        boolean reject = false;
        for(int c=1; c<nComp;c++){
            if(filtType[c]!=filtType[0])
                reject = true;
        }
        if(reject){
            throw new IllegalArgumentException("Can not use component"+
                    " transformation when "+
                    "components do not use "+
                    "the same filters");
        }
        return filtType[0];
    }
}
