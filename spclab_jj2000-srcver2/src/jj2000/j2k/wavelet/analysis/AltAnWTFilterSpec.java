/*
 * CVS identifier:
 *
 * $Id: AltAnWTFilterSpec.java,v 1.1 2006/12/14 20:59:36 devel Exp $
 *
 * Class:                   AnWTFilterSpec
 *
 * Description:             Analysis filters specification
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
package jj2000.j2k.wavelet.analysis;

import jj2000.j2k.quantization.*;
import jj2000.j2k.*;

import java.util.*;
import jj2000.j2k.encoder.EncoderOptions;
import jj2000.j2k.wavelet.FilterTypes;

/**
 * This class extends ModuleSpec class for analysis filters specification
 * holding purpose.
 *
 * @see ModuleSpec
 * */
public class AltAnWTFilterSpec extends ModuleSpec {
    
    /**
     * Constructs a new 'AnWTFilterSpec' for the specified number of
     * components and tiles.
     *
     * @param nt The number of tiles
     *
     * @param nc The number of components
     *
     * @param type the type of the specification module i.e. tile specific,
     * component specific or both.
     *
     * @param qts Quantization specifications
     *
     * @param pl The ParameterList
     * */
    public AltAnWTFilterSpec(int nt, int nc, byte type,EncoderOptions options) {
        super(nt,nc,type);
        
        int filterType = options.ffilters;
        
        if(options.lossless) {
            setDefault(parseFilters(FilterTypes.W5X3));
            options.ffilters = FilterTypes.W5X3;
            return;
        }
        if( options.qtype == options.QTYPE_REVERSIBLE ) {
            setDefault(parseFilters(FilterTypes.W5X3));
            options.ffilters = FilterTypes.W5X3;
        } else {
            setDefault(parseFilters(FilterTypes.W9X7));
            options.ffilters = FilterTypes.W9X7;
        }
    }
    
    /**
     * Parse filters from the given word
     *
     * @param word String to parse
     *
     * @return Analysis wavelet filter (first dimension: by direction,
     * second dimension: by decomposition levels)
     */
    private AnWTFilter[][] parseFilters(int filterType){
        AnWTFilter[][] filt=new AnWTFilter[2][1];
        if(filterType == FilterTypes.W5X3){
            filt[0][0]=new AnWTFilterIntLift5x3();
            filt[1][0]=new AnWTFilterIntLift5x3();
            return filt;
        } else {
            filt[0][0]=new AnWTFilterFloatLift9x7();
            filt[1][0]=new AnWTFilterFloatLift9x7();
            return filt;
        }
    }
    
    /**
     * Returns the data type used by the filters in this object, as defined in
     * the 'DataBlk' interface for specified tile-component.
     *
     * @param t Tile index
     *
     * @param c Component index
     *
     * @return The data type of the filters in this object
     *
     * @see jj2000.j2k.image.DataBlk
     * */
    public int getWTDataType(int t,int c){
        AnWTFilter[][] an = (AnWTFilter[][])getSpec(t,c);
        return an[0][0].getDataType();
    }
    
    /**
     * Returns the horizontal analysis filters to be used in component 'n' and
     * tile 't'.
     *
     * <P>The horizontal analysis filters are returned in an array of
     * AnWTFilter. Each element contains the horizontal filter for each
     * resolution level starting with resolution level 1 (i.e. the analysis
     * filter to go from resolution level 1 to resolution level 0). If there
     * are less elements than the maximum resolution level, then the last
     * element is assumed to be repeated.
     *
     * @param t The tile index, in raster scan order
     *
     * @param c The component index.
     *
     * @return The array of horizontal analysis filters for component 'n' and
     * tile 't'.
     * */
    public AnWTFilter[] getHFilters(int t, int c) {
        AnWTFilter[][] an = (AnWTFilter[][])getSpec(t,c);
        return an[0];
    }
    
    /**
     * Returns the vertical analysis filters to be used in component 'n' and
     * tile 't'.
     *
     * <P>The vertical analysis filters are returned in an array of
     * AnWTFilter. Each element contains the vertical filter for each
     * resolution level starting with resolution level 1 (i.e. the analysis
     * filter to go from resolution level 1 to resolution level 0). If there
     * are less elements than the maximum resolution level, then the last
     * element is assumed to be repeated.
     *
     * @param t The tile index, in raster scan order
     *
     * @param c The component index.
     *
     * @return The array of horizontal analysis filters for component 'n' and
     * tile 't'.
     * */
    public AnWTFilter[] getVFilters(int t,int c) {
        AnWTFilter[][] an = (AnWTFilter[][])getSpec(t,c);
        return an[1];
    }
    
    /** Debugging method */
    public String toString(){
        String str = "";
        AnWTFilter[][] an;
        
        str += "nTiles="+nTiles+"\nnComp="+nComp+"\n\n";
        
        for(int t=0; t<nTiles; t++){
            for(int c=0; c<nComp; c++){
                an = (AnWTFilter[][])getSpec(t,c);
                
                str += "(t:"+t+",c:"+c+")\n";
                
                // Horizontal filters
                str += "\tH:";
                for(int i=0; i<an[0].length; i++)
                    str += " "+an[0][i];
                // Horizontal filters
                str += "\n\tV:";
                for(int i=0; i<an[1].length; i++)
                    str += " "+an[1][i];
                str += "\n";
            }
        }
        
        return str;
    }
    
    /**
     * Check the reversibility of filters contained is the given
     * tile-component.
     *
     * @param t The index of the tile
     *
     * @param c The index of the component
     * */
    public boolean isReversible(int t,int c){
        // Note: no need to buffer the result since this method is
        // normally called once per tile-component.
        AnWTFilter[]
                hfilter = getHFilters(t,c),
                vfilter = getVFilters(t,c);
        
        // As soon as a filter is not reversible, false can be returned
        for(int i=hfilter.length-1; i>=0; i--)
            if(!hfilter[i].isReversible() || !vfilter[i].isReversible())
                return false;
        return true;
    }
    
}
