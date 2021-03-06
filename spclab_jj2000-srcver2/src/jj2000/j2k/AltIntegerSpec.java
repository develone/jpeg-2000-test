/*
 * CVS identifier:
 *
 * $Id: AltIntegerSpec.java,v 1.1 2006/12/14 20:58:52 devel Exp $
 *
 * Class:                   IntegerSpec
 *
 * Description:             Holds specs corresponding to an Integer
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
package jj2000.j2k;

import jj2000.j2k.encoder.EncoderOptions;

/**
 * This class extends ModuleSpec and is responsible of Integer specifications
 * for each tile-component.
 *
 * @see ModuleSpec
 * */
public class AltIntegerSpec extends ModuleSpec {
    
    
    /** The largest value of type int */
    protected static int MAX_INT = Integer.MAX_VALUE;
    
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
    public AltIntegerSpec(int nt,int nc,byte type) {
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
    public AltIntegerSpec(int nt,int nc,byte type,int value) {
        super(nt,nc,type);        
        setDefault(Integer.valueOf(value));
    }    
               
    /**
     * Gets the maximum value of all tile-components.
     *
     * @return The maximum value
     * */
    public int getMax() {
        int max = ((Integer)def).intValue();
        int tmp;
        
        for(int t=0; t<nTiles; t++) {
            for(int c=0; c<nComp; c++) {
                tmp = ((Integer)getSpec(t,c)).intValue();
                if(max<tmp)
                    max = tmp;
            }
        }
        
        return max;
    }
    
    /**
     * Get the minimum value of all tile-components.
     *
     * @return The minimum value
     * */
    public int getMin() {
        int min = ((Integer)def).intValue();
        int tmp;
        
        for(int t=0; t<nTiles; t++) {
            for(int c=0; c<nComp; c++) {
                tmp = ((Integer)getSpec(t,c)).intValue();
                if(min>tmp)
                    min = tmp;
            }
        }
        
        return min;
    }
    
    /**
     * Gets the maximum value of each tile for specified component
     *
     * @param c The component index
     *
     * @return The maximum value
     * */
    public int getMaxInComp(int c) {
        int max = 0;
        int tmp;
        
        for(int t=0; t<nTiles; t++) {
            tmp = ((Integer)getSpec(t,c)).intValue();
            if(max<tmp)
                max = tmp;
        }
        
        return max;
    }
    
    /**
     * Gets the minimum value of all tiles for the specified component.
     *
     * @param c The component index
     *
     * @return The minimum value
     * */
    public int getMinInComp(int c) {
        int min = MAX_INT; // Big value
        int tmp;
        
        for(int t=0; t<nTiles; t++) {
            tmp = ((Integer)getSpec(t,c)).intValue();
            if(min>tmp)
                min = tmp;
        }
        
        return min;
    }
    
    /**
     * Gets the maximum value of all components in the specified tile.
     *
     * @param t The tile index
     *
     * @return The maximum value
     * */
    public int getMaxInTile(int t) {
        int max = 0;
        int tmp;
        
        for(int c=0; c<nComp; c++) {
            tmp = ((Integer)getSpec(t,c)).intValue();
            if(max<tmp)
                max = tmp;
        }
        
        return max;
    }
    
    /**
     * Gets the minimum value of each component in specified tile
     *
     * @param t The tile index
     *
     * @return The minimum value
     * */
    public int getMinInTile(int t) {
        int min = MAX_INT; // Big value
        int tmp;
        
        for(int c=0; c<nComp; c++) {
            tmp = ((Integer)getSpec(t,c)).intValue();
            if(min>tmp)
                min = tmp;
        }
        
        return min;
    }
}

