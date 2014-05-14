/*
 * CVS identifier:
 *
 * $Id: AltQuantStepSizeSpec.java,v 1.1 2006/12/14 20:58:57 devel Exp vidal $
 *
 * Class:                   QuantStepSizeSpec
 *
 * Description:    Quantization base normalized step size specifications
 *
 *
 *
 * COPYRIGHT:
 *
 * This software module was originally developed by Rapha�l Grosbois and
 * Diego Santa Cruz (Swiss Federal Institute of Technology-EPFL); Joel
 * Askel�f (Ericsson Radio Systems AB); and Bertrand Berthelot, David
 * Bouchard, F�lix Henry, Gerard Mozelle and Patrice Onno (Canon Research
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
package jj2000.j2k.quantization;

import jj2000.j2k.*;
import jj2000.j2k.encoder.EncoderOptions;

/**
 * This class extends ModuleSpec class in order to hold specifications about
 * the quantization base normalized step size to use in each tile-component.
 *
 * @see ModuleSpec
 * */
public class AltQuantStepSizeSpec extends ModuleSpec {
    
    /**
     * Constructs an empty 'QuantStepSizeSpec' with specified number of
     * tile and components. This constructor is called by the decoder.
     *
     * @param nt Number of tiles
     *
     * @param nc Number of components
     *
     * @param type the type of the specification module i.e. tile specific,
     * component specific or both.
     * */
    public AltQuantStepSizeSpec(int nt, int nc, byte type) {
        super(nt,nc,type);
    }
    
    /**
     * Constructs a new 'QuantStepSizeSpec' for the specified number of
     * components and tiles and the arguments of "-Qstep" option.
     *
     * @param nt The number of tiles
     *
     * @param nc The number of components
     *
     * @param type the type of the specification module i.e. tile specific,
     * component specific or both.
     *
     * @param pl The ParameterList
     * */
    public AltQuantStepSizeSpec(int nt,int nc,byte type,EncoderOptions options) {
        super(nt, nc, type);
        
        float qstep = options.qstep;
        if (qstep <= 0.0f) {
            throw new IllegalArgumentException("Normalized base step "+
                    "must be positive : "+qstep);
        }
        setDefault(Float.valueOf(qstep));
    }
    
}
