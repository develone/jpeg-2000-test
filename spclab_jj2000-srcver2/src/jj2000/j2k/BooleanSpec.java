/*
 * CVS identifier:
 *
 * $Id: BooleanSpec.java,v 1.1 2006/12/14 20:58:52 devel Exp $
 *
 * Class:                   IntegerSpec
 *
 * Description:             Holds specs corresponding to an Integer
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
package jj2000.j2k;

import jj2000.j2k.encoder.EncoderOptions;

/**
 * This class extends ModuleSpec and is responsible of Integer specifications
 * for each tile-component.
 *
 * @see ModuleSpec
 * */
public class BooleanSpec extends ModuleSpec {   
    
    /**
     * Constructs a new 'IntegerSpec' for the specified number of tiles and
     * components and with allowed type of specifications. This constructor is
     * normally called at decoder side.
     *
     * @param nt The number of tiles
     *
     * @param nc The number of components
     *
     * @param type The type of allowed specifications
     * */
    public BooleanSpec(int nt,int nc,byte type) {
        super(nt,nc,type);
    }
    
    /**
     * Constructs a new 'IntegerSpec' for the specified number of tiles and
     * components, the allowed specifications type and the ParameterList
     * instance. This constructor is normally called at encoder side and parse
     * arguments of specified option.
     *
     * @param nt The number of tiles
     *
     * @param nc The number of components
     *
     * @param type The allowed specifications type
     *
     * @param pl The ParameterList instance
     *
     * @param optName The name of the option to process
     * */
    public BooleanSpec(int nt,int nc,byte type,boolean value) {
        super(nt,nc,type);        
        setDefault(Boolean.valueOf(value));
    }      
}

