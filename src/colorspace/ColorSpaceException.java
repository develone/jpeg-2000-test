/*****************************************************************************
 *
 * $Id: ColorSpaceException.java,v 1.1 2006/12/14 20:58:39 devel Exp vidal $
 *
 * Copyright Eastman Kodak Company, 343 State Street, Rochester, NY 14650
 * $Date $
 *****************************************************************************/

package colorspace;

/**
 * This exception is thrown when the content of an
 * image contains an incorrect colorspace box
 * 
 * @see		jj2000.j2k.colorspace.ColorSpaceMapper
 * @version	1.0
 * @author	Bruce A. Kern
 */

public class ColorSpaceException extends Exception {

    /**
     * Contruct with message
     *   @param msg returned by getMessage()
     */
    public ColorSpaceException (String msg) {
        super (msg); }


    /**
     * Empty constructor
     */
    public ColorSpaceException () {
    }
    
    /* end class ColorSpaceException */ }




