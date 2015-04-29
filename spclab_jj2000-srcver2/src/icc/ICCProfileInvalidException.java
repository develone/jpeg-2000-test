/*****************************************************************************
 *
 * $Id: ICCProfileInvalidException.java,v 1.1 2006/12/14 20:58:39 devel Exp $
 *
 * Copyright Eastman Kodak Company, 343 State Street, Rochester, NY 14650
 * $Date $
 *****************************************************************************/

package icc;

/**
 * This exception is thrown when the content of an an icc profile 
 * is in someway incorrect.
 * 
 * @see		jj2000.j2k.icc.ICCProfile
 * @version	1.0
 * @author	Bruce A. Kern
 */

public class ICCProfileInvalidException extends ICCProfileException {

    /**
     * Contruct with message
     *   @param msg returned by getMessage()
     */
    ICCProfileInvalidException (String msg) {
        super (msg); }


    /**
     * Empty constructor
     */
    ICCProfileInvalidException () {
        super ("icc profile is invalid"); }
    
    /* end class ICCProfileInvalidException */ }




