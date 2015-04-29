/*
 * CVS identifier:
 *
 * $Id: AltQuantTypeSpec.java,v 1.1 2006/12/14 20:58:57 devel Exp $
 *
 * Class:                   QuantTypeSpec
 *
 * Description:             Quantization type specifications
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

import java.util.*;
import jj2000.j2k.encoder.EncoderOptions;

/**
 * This class extends ModuleSpec class in order to hold specifications about
 * the quantization type to use in each tile-component. Supported quantization
 * type are:<br>
 *
 * <ul>
 * <li> Reversible (no quantization)</li>
 * <li> Derived (the quantization step size is derived from the one of the
 * LL-subband)</li>
 * <li> Expounded (the quantization step size of each subband is signalled in
 * the codestream headers) </li>
 * </ul>
 *
 * @see ModuleSpec
 * */
public class AltQuantTypeSpec extends ModuleSpec {
    
    /**
     * Constructs an empty 'QuantTypeSpec' with the specified number of tiles
     * and components. This constructor is called by the decoder.
     *
     * @param nt Number of tiles
     *
     * @param nc Number of components
     *
     * @param type the type of the allowed specifications for this module
     * i.e. tile specific, component specific or both.
     * */
    public AltQuantTypeSpec(int nt,int nc,byte type) {
        super(nt,nc,type);
    }
    
    
    /**
     * Constructs a new 'QuantTypeSpec' for the specified number of components
     * and tiles and the arguments of "-Qtype" option. This constructor is
     * called by the encoder.
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
    public AltQuantTypeSpec(int nt,int nc,byte type,EncoderOptions options) {
        super(nt,nc,type);        
        if(options.lossless) {
            setDefault("reversible");
        } else {
            setDefault("expounded");
        }      
    }
    
    /**
     * Returns true if given tile-component uses derived quantization step
     * size.
     *
     * @param t Tile index
     *
     * @param c Component index
     *
     * @return True if derived quantization step size
     * */
    public boolean isDerived(int t,int c) {
        if( ((String)getTileCompVal(t,c)).equals("derived") ) {
            return true;
        } else {
            return false;
        }
    }
    
    /**
     * Check the reversibility of the given tile-component.
     *
     * @param t The index of the tile
     *
     * @param c The index of the component
     *
     * @return Whether or not the tile-component is reversible
     * */
    public boolean isReversible(int t,int c) {
        if( ((String)getTileCompVal(t,c)).equals("reversible") ) {
            return true;
        } else {
            return false;
        }
    }
    
    /**
     * Check the reversibility of the whole image.
     *
     * @return Whether or not the whole image is reversible
     * */
    public boolean isFullyReversible() {
        // The whole image is reversible if default specification is
        // rev and no tile default, component default and
        // tile-component value has been specificied
        if( ((String)getDefault()).equals("reversible") ) {
            for(int t=nTiles-1; t>=0; t--)
                for(int c=nComp-1; c>=0; c--)
                    if(specValType[t][c]!=SPEC_DEF)
                        return false;
            return true;
        }
        
        return false;
    }
    
    /**
     * Check the irreversibility of the whole image.
     *
     * @return Whether or not the whole image is reversible
     * */
    public boolean isFullyNonReversible() {
        // The whole image is irreversible no tile-component is reversible
        for(int t=nTiles-1; t>=0; t--)
            for(int c=nComp-1; c>=0; c--)
                if( ((String)getSpec(t,c)).equals("reversible") )
                    return false;
        return true;
    }
    
}
