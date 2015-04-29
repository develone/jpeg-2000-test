/*
 * CVS identifier:
 *
 * $Id: AltProgressionSpec.java,v 1.1 2006/12/14 20:58:57 devel Exp $
 *
 * Class:                   ProgressionSpec
 *
 * Description:             Specification of the progression(s) type(s) and
 *                          changes of progression.
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
import jj2000.j2k.*;
import jj2000.j2k.encoder.EncoderOptions;

/**
 * This class extends ModuleSpec class for progression type(s) and progression
 * order changes holding purposes.
 *
 * <p>It stores  the progression type(s) used in the  codestream. There can be
 *  several progression  type(s) if  progression order  changes are  used (POC
 * markers).</p>
 * */
public class AltProgressionSpec extends ModuleSpec {
    
    /**
     * Creates a new ProgressionSpec object for the specified number of tiles
     * and components.
     *
     * @param nt The number of tiles
     *
     * @param nc The number of components
     *
     * @param type the type of the specification module i.e. tile specific,
     * component specific or both. The ProgressionSpec class should only be
     * used only with the type ModuleSpec.SPEC_TYPE_TILE.
     * */
    public AltProgressionSpec(int nt, int nc, byte type) {
        super(nt, nc, type);
        if ( type !=  ModuleSpec.SPEC_TYPE_TILE ) {
            throw new Error("Illegal use of class ProgressionSpec !");
        }
    }
    
    /**
     * Creates a new ProgressionSpec object for the specified number of tiles,
     * components and the ParameterList instance.
     *
     * @param nt The number of tiles
     *
     * @param nc The number of components
     *
     * @param nl The number of layer
     *
     * @param dls The number of decomposition levels specifications
     *
     * @param type the type of the specification module. The ProgressionSpec
     * class should only be used only with the type ModuleSpec.SPEC_TYPE_TILE.
     *
     * @param pl The ParameterList instance
     * */
    public AltProgressionSpec(int nt,int nc,int nl,AltIntegerSpec dls,byte type,
            EncoderOptions options){
        super(nt,nc,type);
        
        Progression[] prog;
        int mode = -1;
        mode = options.aptype;
//        if(options.roi_type == -1) {
//            mode = ProgressionType.RES_LY_COMP_POS_PROG;
//        } else {
//            mode = ProgressionType.LY_RES_COMP_POS_PROG;
//        }       
        prog = new Progression[1];
        prog[0] = new Progression(mode,0,nc,0,dls.getMax()+1,nl);
        setDefault(prog);        
    }
}
