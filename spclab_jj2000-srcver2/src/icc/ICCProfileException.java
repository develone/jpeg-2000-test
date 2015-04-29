/*****************************************************************************
 *
 * $Id: ICCProfileException.java,v 1.1 2006/12/14 20:58:39 devel Exp $
 *
 * Copyright Eastman Kodak Company, 343 State Street, Rochester, NY 14650
 * $Date $
 *****************************************************************************/
package icc;

/**
 * This exception is thrown when the content of a profile
 * is incorrect.
 * 
 * @see		jj2000.j2k.icc.ICCProfile
 * @version	1.0
 * @author	Bruce A. Kern
 */
public class ICCProfileException extends Exception {

    /**
     *  Contruct with message
     *  @param msg returned by getMessage()
     */
    public ICCProfileException (String msg) {
        super (msg); 
    }


    /**
     * Empty constructor
     */
    public ICCProfileException () { }
}




