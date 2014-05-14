/*
 * CVS identifier:
 *
 * $Id: AltPrecinctSizeSpec.java,v 1.1 2006/12/14 20:58:57 devel Exp vidal $
 *
 * Class:                   PrecinctSizeSpec
 *
 * Description:             Specification of the precinct sizes
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
package jj2000.j2k.entropy;

import jj2000.j2k.codestream.*;
import jj2000.j2k.image.*;
import jj2000.j2k.*;

import java.util.*;
import jj2000.j2k.encoder.EncoderOptions;

/**
 * This class extends ModuleSpec class for precinct partition sizes holding
 * purposes.
 *
 * <p>It stores the size a of precinct when precinct partition is used or not.
 * If precinct partition is used, we can have several packets for a given
 * resolution level whereas there is only one packet per resolution level if
 * no precinct partition is used.
 * */
public class AltPrecinctSizeSpec extends ModuleSpec {
    
    /** Name of the option */
    private static final String optName = "Cpp";
    
    /** Reference to wavelet number of decomposition levels for each
     * tile-component.  */
    private AltIntegerSpec dls;
    
    /**
     * Creates a new PrecinctSizeSpec object for the specified number of tiles
     * and components.
     *
     * @param nt The number of tiles
     *
     * @param nc The number of components
     *
     * @param type the type of the specification module i.e. tile specific,
     * component specific or both.
     *
     * @param dls Reference to the number of decomposition levels
     * specification
     * */
    public AltPrecinctSizeSpec(int nt, int nc, byte type, AltIntegerSpec dls) {
        super(nt, nc, type);
        this.dls = dls;
    }
    
    /**
     * Creates a new PrecinctSizeSpec object for the specified number of tiles
     * and components and the ParameterList instance.
     *
     * @param nt The number of tiles
     *
     * @param nc The number of components
     *
     * @param type the type of the specification module i.e. tile specific,
     * component specific or both.
     *
     * @param imgsrc The image source (used to get the image size)
     *
     * @param pl The ParameterList instance
     * */
    public AltPrecinctSizeSpec(int nt,int nc,byte type,BlkImgDataSrc imgsrc,
            AltIntegerSpec dls) {
        super(nt, nc, type);
        
        this.dls = dls;
        
        // The precinct sizes are stored in a 2 elements vector array, the
        // first element containing a vector for the precincts width for each
        // resolution level and the second element containing a vector for the
        // precincts height for each resolution level. The precincts sizes are
        // specified from the highest resolution level to the lowest one
        // (i.e. 0).  If there are less elements than the number of
        // decomposition levels, the last element is used for all remaining
        // resolution levels (i.e. if the precincts sizes are specified only
        // for resolutions levels 5, 4 and 3, then the precincts size for
        // resolution levels 2, 1 and 0 will be the same as the size used for
        // resolution level 3).
        
        // Set precinct sizes to default i.e. 2^15 =
        // Markers.PRECINCT_PARTITION_DEF_SIZE
        Vector tmpv[] = new Vector[2];
        tmpv[0] = new Vector(); // ppx
        tmpv[0].addElement(new Integer(Markers.PRECINCT_PARTITION_DEF_SIZE));
        tmpv[1] = new Vector(); // ppy
        tmpv[1].addElement(new Integer(Markers.PRECINCT_PARTITION_DEF_SIZE));
        setDefault(tmpv);     
    }
    
    /**
     * Returns the precinct partition width in component 'n' and tile 't' at
     * resolution level 'rl'. If the tile index is equal to -1 or if the
     * component index is equal to -1 it means that those should not be taken
     * into account.
     *
     * @param t The tile index, in raster scan order. Specify -1 if it is not
     * a specific tile.
     *
     * @param c The component index. Specify -1 if it is not a specific
     * component.
     *
     * @param rl The resolution level
     *
     * @return The precinct partition width in component 'c' and tile 't' at
     * resolution level 'rl'.
     * */
    public int getPPX(int t,int c,int rl) {
        int mrl, idx;
        Vector[] v=null;
        boolean tileSpecified = (t!=-1 ? true : false);
        boolean compSpecified = (c!=-1 ? true : false);
        
        // Get the maximum number of decomposition levels and the object
        // (Vector array) containing the precinct dimensions (width and
        // height) for the specified (or not) tile/component
        if (tileSpecified && compSpecified) {
            mrl = ((Integer)dls.getTileCompVal(t, c)).intValue();
            v = (Vector[])getTileCompVal(t, c);
        } else if (tileSpecified && !compSpecified) {
            mrl = ((Integer)dls.getTileDef(t)).intValue();
            v = (Vector[])getTileDef(t);
        } else if (!tileSpecified && compSpecified) {
            mrl = ((Integer)dls.getCompDef(c)).intValue();
            v = (Vector[])getCompDef(c);
        } else {
            mrl = ((Integer)dls.getDefault()).intValue();
            v = (Vector[])getDefault();
        }
        idx = mrl - rl;
        if (v[0].size()>idx) {
            return ((Integer)v[0].elementAt(idx)).intValue();
        } else {
            return ((Integer)v[0].elementAt(v[0].size()-1)).intValue();
        }
    }
    
    /**
     * Returns the precinct partition height in component 'n' and tile 't' at
     * resolution level 'rl'. If the tile index is equal to -1 or if the
     * component index is equal to -1 it means that those should not be taken
     * into account.
     *
     * @param t The tile index, in raster scan order. Specify -1 if it is not
     * a specific tile.
     *
     * @param c The component index. Specify -1 if it is not a specific
     * component.
     *
     * @param rl The resolution level.
     *
     * @return The precinct partition width in component 'n' and tile 't' at
     * resolution level 'rl'.
     * */
    public int getPPY(int t, int c, int rl) {
        int mrl, idx;
        Vector[] v=null;
        boolean tileSpecified = (t!=-1 ? true : false);
        boolean compSpecified = (c!=-1 ? true : false);
        
        // Get the maximum number of decomposition levels and the object
        // (Vector array) containing the precinct dimensions (width and
        // height) for the specified (or not) tile/component
        if ( tileSpecified && compSpecified ) {
            mrl = ((Integer)dls.getTileCompVal(t, c)).intValue();
            v = (Vector[])getTileCompVal(t, c);
        } else if ( tileSpecified && !compSpecified ) {
            mrl = ((Integer)dls.getTileDef(t)).intValue();
            v = (Vector[])getTileDef(t);
        } else if ( !tileSpecified && compSpecified ) {
            mrl = ((Integer)dls.getCompDef(c)).intValue();
            v = (Vector[])getCompDef(c);
        } else {
            mrl = ((Integer)dls.getDefault()).intValue();
            v = (Vector[])getDefault();
        }
        idx = mrl - rl;
        if ( v[1].size() > idx ) {
            return ((Integer)v[1].elementAt(idx)).intValue();
        } else {
            return ((Integer)v[1].elementAt(v[1].size()-1)).intValue();
        }
    }
}
